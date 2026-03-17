from __future__ import annotations

import asyncio
import json
from dataclasses import dataclass
from typing import Any

from lnu.ai_clients import AIClient, extract_json_from_text
from lnu.api_client import LnuApiClient
from lnu.logging_utils import get_logger
from lnu.models import Solution, SolutionFile, Task, TaskSolveError
from lnu.rate_limit import RateLimiter
from lnu.storage import TaskStore
from lnu.submitter import ReliableSubmitter

log = get_logger(__name__)


def _html_to_text(html: str) -> str:
    html = html or ""
    # Prefer BeautifulSoup if available (you already use bs4 elsewhere in the repo)
    try:
        from bs4 import BeautifulSoup  # type: ignore

        soup = BeautifulSoup(html, "html.parser")
        return soup.get_text("\n", strip=True)
    except Exception:
        import re

        # Very small fallback: strip tags, keep spacing
        text = re.sub(r"<\s*br\s*/?\s*>", "\n", html, flags=re.I)
        text = re.sub(r"</\s*p\s*>", "\n", text, flags=re.I)
        text = re.sub(r"<[^>]+>", "", text)
        return re.sub(r"\n{3,}", "\n\n", text).strip()


def _build_prompt(task: Task, lesson_fields: dict[str, Any]) -> str:
    title = task.title or lesson_fields.get("title") or ""
    content = lesson_fields.get("content_text") or ""
    path = task.path or ""

    required_files = lesson_fields.get("required_files") or []
    starter_files = lesson_fields.get("starter_files") or []
    previous_feedback = lesson_fields.get("previous_feedback") or ""

    starter_signatures = []
    import re as _re
    for sf in starter_files:
        for match in _re.finditer(r'^def\s+\w+\([^)]*\)\s*:', sf.get("code", ""), _re.MULTILINE):
            starter_signatures.append(match.group(0))

    sig_block = ""
    if starter_signatures:
        sig_block = (
                "CRITICAL: Keep EXACTLY these function signatures (do NOT add or remove parameters):\n"
                + "\n".join(f"  {s}" for s in starter_signatures)
                + "\n\n"
        )

    feedback_block = ""
    if previous_feedback:
        feedback_block = (
            "CRITICAL — PREVIOUS ATTEMPT FAILED. You MUST fix these errors:\n"
            f"{previous_feedback}\n"
            "Do NOT repeat the same mistakes. Read the errors carefully before writing any code.\n\n"
        )

    # Design decision: force a strict JSON output to enable reliable parsing
    # and strongly bias the model toward simple, correct, lesson-aligned code.
    return (
        "You are solving an educational coding task.\n"
        "System constraints:\n"
        "- Your code MUST include all required imports explicitly (add `import ...` / `from ... import ...` for every package/module you use).\n"
        "- Prefer standard library where possible.\n"
        "- Do not create extra files, do not rename files.\n"
        "- Be extremely precise with syntax – no missing colons, wrong names, or bad indentation.\n"
        "- IMPORTANT: If the task does not explicitly specify otherwise, do not add any arguments to the function — always assume that it should be executed without parameters.\n"
        "- Solve each task in the simplest correct way that matches the lesson description.\n"
        "- Think carefully about edge cases and test your logic mentally on a few inputs before finalizing.\n"
        "Return ONLY a single JSON object with this schema:\n"
        '{ "files": [ { "fileName": "...", "code": "..." } ] }\n'
        "No markdown, no explanations.\n\n"
        + feedback_block
        + sig_block
        + "IMPORTANT: You MUST use EXACTLY these file names and only these:\n"
        + "\n".join([f"- {name}" for name in required_files])
        + "\n\n"
        "Starter code (edit it, keep file names):\n"
        + "\n\n".join([f"FILE: {f['fileName']}\n{f.get('code','')}" for f in starter_files])
        + "\n\n"
        + (f"Previous LNU compile/test feedback (fix these issues):\n{previous_feedback}\n\n" if previous_feedback else "")
        + f"Task id: {task.id}\n"
        + f"Path/topic: {path}\n"
        + f"Title: {title}\n"
        + f"Assignment:\n{content}\n"
    )


@dataclass(slots=True)
class TaskSolver:
    api: LnuApiClient
    store: TaskStore
    submitter: ReliableSubmitter
    ai_client: AIClient
    rate_limiter: RateLimiter | None = None
    rate_limit_per_min: int = 10
    solve_max_attempts: int = 3

    async def solve_task(self, task: Task, *, previous_feedback: str | None = None) -> Solution:
        """Generate a solution for a single task (no submission).

        Request flow aligned with captured traffic:
        - menus/saveLastId (best-effort)
        - lekcja/get (fetch t_tresc)
        - (optional) lekcja/summary (best-effort)
        - LLM generation from lesson content
        """
        if self.rate_limiter:
            await self.rate_limiter.acquire()

        # Best-effort "save last visited lesson" like the UI does.
        try:
            await self.api.save_last_id(task.id)
        except Exception:
            pass

        lesson = await self.api.get_lesson(task.id)
        fields = self.api.extract_task_fields(lesson)

        # Optional stats call (not required for solving, but matches observed requests).
        try:
            summary = await self.api.get_lesson_summary(task.id)
            fields["summary"] = summary
        except Exception:
            fields["summary"] = None

        html = fields.get("content_html") or ""
        fields["content_text"] = _html_to_text(str(html)) if html else ""
        if not fields["content_text"]:
            raise ValueError("Lesson content is empty (missing t_tresc)")
        if previous_feedback:
            fields["previous_feedback"] = previous_feedback

        # Canonical file list comes from `lekcja.t_code.files`.
        lekcja = lesson.get("lekcja") if isinstance(lesson, dict) else None
        t_code = lekcja.get("t_code") if isinstance(lekcja, dict) else None
        template_files: list[dict[str, Any]] = []
        if isinstance(t_code, dict) and isinstance(t_code.get("files"), list):
            template_files = [f for f in t_code["files"] if isinstance(f, dict) and f.get("fileName")]
        if not template_files:
            log.warning(
                "Skipping task — no t_code.files template (likely a theory/reading lesson)",
                extra={"task_id": task.id}
            )
            return None

        required_names = [str(f["fileName"]) for f in template_files]
        fields["required_files"] = required_names
        fields["starter_files"] = [{"fileName": str(f["fileName"]), "code": str(f.get("code", ""))} for f in template_files]

        prompt = _build_prompt(task, fields)
        raw = await self.ai_client.complete(prompt)
        payload = extract_json_from_text(raw)
        files_raw = payload.get("files", [])
        if not isinstance(files_raw, list) or not files_raw:
            raise ValueError("AI returned no files")

        ai_map: dict[str, str] = {}
        for f in files_raw:
            if not isinstance(f, dict):
                continue
            name = str(f.get("fileName", "")).strip()
            code = str(f.get("code", ""))
            if not name:
                continue
            ai_map[name] = code

        # Build final submission files: exactly template names, filled with AI code when available,
        # otherwise keep starter code. Ignore any AI-proposed unknown files.
        unknown = [n for n in ai_map.keys() if n not in required_names]
        if unknown:
            log.warning("AI proposed unknown files; ignoring", extra={"task_id": task.id, "unknown_files": unknown, "required_files": required_names})

        final_files: list[SolutionFile] = []
        for tf in template_files:
            name = str(tf["fileName"])
            starter_code = str(tf.get("code", ""))
            code = ai_map.get(name, starter_code)
            final_files.append(SolutionFile(file_name=name, code=code))

        return Solution(task_id=task.id, files=final_files, provider=self.ai_client.name, raw=payload)

    async def solve_and_submit_task(self, task: Task) -> None:
        """Solve a task and submit until accepted, up to `solve_max_attempts`."""
        debug_context: dict[str, Any] = {"task_id": task.id, "path": task.path, "title": task.title, "attempts": []}
        previous_feedback: str | None = None

        for attempt in range(1, self.solve_max_attempts + 1):
            self.store.mark_solve_attempt(task.id, attempt)
            try:
                solution = await self.solve_task(
                    Task(id=task.id, title=task.title, path=task.path, sort_order=task.sort_order, label=task.label),
                    previous_feedback=previous_feedback,
                )

                if solution is None:
                    log.info("Task skipped (no template)", extra={"task_id": task.id})
                    return  # nie rzucaj błędu, po prostu idź dalej

                # Persist solution in DB (backward compatible format)
                solution_json = json.dumps(
                    {
                        "provider": solution.provider,
                        "files": [{"fileName": f.file_name, "code": f.code} for f in solution.files],
                    },
                    ensure_ascii=False,
                )
                self.store.update_solution(task.id, solution_json)

                result = await self.submitter.submit_with_confirmation(solution)
                feedback = ReliableSubmitter.extract_feedback(result.server_payload)
                log.warning(
                    "Feedback po odrzuceniu",
                    extra={
                        "task_id": task.id,
                        "raw_payload": result.server_payload,  # ← cały payload
                        "feedback": feedback,  # ← co z niego wyciągnęło
                    }
                )
                debug_context["attempts"].append(
                    {
                        "attempt": attempt,
                        "submitted_attempt": result.attempt,
                        "accepted": result.accepted,
                        "feedback": feedback,
                    }
                )
                if result.accepted:
                    return
                log.warning("Solve attempt rejected", extra={"task_id": task.id, "solve_attempt": attempt})
                previous_feedback = feedback
            except Exception as e:
                debug_context["attempts"].append({"attempt": attempt, "error": repr(e)})
                self.store.mark_solve_attempt(task.id, attempt, last_error=repr(e))
                log.error("Solve attempt failed", extra={"task_id": task.id, "solve_attempt": attempt, "error": repr(e)}, exc_info=True)

            if attempt < self.solve_max_attempts:
                await asyncio.sleep(1.0)

        log.error("TaskSolveError", extra={"debug": debug_context})
        raise TaskSolveError(f"Task {task.id} failed after {self.solve_max_attempts} solve attempts")

    async def solve_lesson(self, lesson_id: str) -> None:
        """Solve one lesson by id (string for CLI convenience)."""
        task = Task(id=int(lesson_id))
        await self.solve_and_submit_task(task)

