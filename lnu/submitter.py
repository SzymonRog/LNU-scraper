from __future__ import annotations

import asyncio
import json
import random
import time
from dataclasses import dataclass
from typing import Any

from lnu.api_client import LnuApiClient
from lnu.logging_utils import get_logger
from lnu.models import Solution, SubmissionResult
from lnu.rate_limit import RateLimiter
from lnu.storage import TaskStore

log = get_logger(__name__)


def _exp_backoff(attempt: int, base: float, cap: float) -> float:
    # attempt is 1-based
    delay = min(cap, base * (2 ** (attempt - 1)))
    # jitter helps avoid synchronized retries if running multiple instances
    jitter = random.uniform(0.0, min(1.0, delay * 0.1))
    return delay + jitter


@dataclass(slots=True)
class ReliableSubmitter:
    api: LnuApiClient
    store: TaskStore
    rate_limiter: RateLimiter | None = None
    backoff_base_seconds: float = 1.0
    backoff_max_seconds: float = 30.0
    max_attempts: int = 5
    confirm_poll_seconds: float = 2.0
    confirm_timeout_seconds: float = 20.0

    async def submit_sequential(self, solutions: list[Solution]) -> list[SubmissionResult]:
        results: list[SubmissionResult] = []
        for sol in solutions:
            results.append(await self.submit_with_confirmation(sol))
        return results

    async def submit_with_confirmation(self, solution: Solution) -> SubmissionResult:
        task_id = solution.task_id
        files = [{"fileName": f.file_name, "code": f.code} for f in solution.files]

        for attempt in range(1, self.max_attempts + 1):
            self.store.mark_submit_attempt(task_id, attempt)
            if self.rate_limiter:
                await self.rate_limiter.acquire()

            telemetry = {
                "deltaTime": str(random.randint(20, 300)),
                "deltaClick": str(random.randint(10, 100)),
                "deltaKeys": str(random.randint(10, 500)),
                "timestamp": str(int(time.time())),
                "last_ping_time": "35",
                "ping_count": "14",
            }

            try:
                log.info("Submitting", extra={"task_id": task_id, "attempt": attempt, "files": [f.file_name for f in solution.files]})
                payload = await self.api.compile_solution(task_id, files=files, telemetry=telemetry)
                immediate = self.api.parse_is_correct(payload)

                accepted = await self._confirm_acceptance(task_id, immediate)
                if accepted is True:
                    self.store.update_is_correct(task_id, True)
                    log.info("Accepted", extra={"task_id": task_id, "attempt": attempt})
                    return SubmissionResult(
                        task_id=task_id,
                        accepted=True,
                        attempt=attempt,
                        server_is_correct=True,
                        server_payload=payload,
                        status="accepted",
                    )

                # Not accepted yet (or unknown) -> retry
                log.warning("Not accepted yet", extra={"task_id": task_id, "attempt": attempt, "immediate_is_correct": immediate})
                if attempt < self.max_attempts:
                    delay = _exp_backoff(attempt, self.backoff_base_seconds, self.backoff_max_seconds)
                    await asyncio.sleep(delay)
                    continue

                self.store.update_is_correct(task_id, False)
                return SubmissionResult(
                    task_id=task_id,
                    accepted=False,
                    attempt=attempt,
                    server_is_correct=bool(immediate) if immediate is not None else None,
                    server_payload=payload,
                    status="rejected" if immediate is False else "unknown",
                )
            except Exception as e:
                self.store.mark_submit_attempt(task_id, attempt, last_error=repr(e))
                log.error("Submit error", extra={"task_id": task_id, "attempt": attempt, "error": repr(e)}, exc_info=True)
                if attempt < self.max_attempts:
                    delay = _exp_backoff(attempt, self.backoff_base_seconds, self.backoff_max_seconds)
                    await asyncio.sleep(delay)
                    continue
                return SubmissionResult(task_id=task_id, accepted=False, attempt=attempt, server_is_correct=None, server_payload=None, status="unknown")

        return SubmissionResult(task_id=task_id, accepted=False, attempt=self.max_attempts, status="unknown")

    async def _confirm_acceptance(self, task_id: int, immediate_is_correct: bool | None) -> bool | None:
        if immediate_is_correct is True:
            return True

        deadline = time.monotonic() + self.confirm_timeout_seconds
        while time.monotonic() < deadline:
            await asyncio.sleep(self.confirm_poll_seconds)
            if self.rate_limiter:
                await self.rate_limiter.acquire()
            try:
                lesson = await self.api.get_lesson(task_id)
                fields = self.api.extract_task_fields(lesson)
                is_correct = fields.get("is_correct")
                if is_correct is True:
                    return True
                if is_correct is False:
                    # Confirmed rejection
                    return False
            except Exception:
                # Treat transient errors as "unknown" and keep polling until timeout
                continue

        return None

    @staticmethod
    def parse_solution_json(task_id: int, solution_raw: str) -> Solution:
        payload = json.loads(solution_raw)
        files = payload.get("files", [])
        if not isinstance(files, list) or not files:
            raise ValueError("Solution JSON has no files")
        sol_files = []
        for f in files:
            sol_files.append(
                {
                    "fileName": f.get("fileName", "solution"),
                    "code": f.get("code", ""),
                }
            )
        from lnu.models import SolutionFile

        return Solution(
            task_id=task_id,
            files=[SolutionFile(file_name=f["fileName"], code=f["code"]) for f in sol_files],
            provider=payload.get("provider", "db"),
            raw=payload,
        )

    @staticmethod
    def extract_feedback(server_payload: dict[str, Any] | None) -> str | None:
        """Extract human-readable compile/test feedback from LNU response.

        The backend sometimes returns payload under root or under `data`.
        We try both and return a condensed string suitable for LLM repair attempts.
        """
        if not server_payload:
            return None

        data = server_payload.get("data")
        if isinstance(data, dict):
            p = data
        else:
            p = server_payload

        parts: list[str] = []

        # Compilation errors (best-effort; field names observed in your docs)
        if isinstance(p.get("compilationErrors"), (str, bool)) and p.get("compilationErrors"):
            parts.append(f"compilationErrors={p.get('compilationErrors')}")
        if p.get("buildStatus") is False:
            parts.append("buildStatus=false")
        if p.get("runStatus") is False:
            parts.append("runStatus=false")

        run_data = p.get("runData")
        if isinstance(run_data, dict):
            run_tests = run_data.get("runTests")
            if isinstance(run_tests, dict):
                score = run_tests.get("score")
                passed = run_tests.get("pass")
                if score is not None or passed is not None:
                    parts.append(f"tests: pass={passed} score={score}")

                tests = run_tests.get("tests")
                if isinstance(tests, list) and tests:
                    # Include only failing outputs (result == "0") and cap size.
                    fail_out: list[str] = []
                    for t in tests:
                        if not isinstance(t, dict):
                            continue
                        if str(t.get("result")) != "0":
                            continue
                        out = t.get("output")
                        if isinstance(out, str) and out.strip():
                            fail_out.append(out.strip())
                        if len(fail_out) >= 5:
                            break
                    if fail_out:
                        parts.append("failing_tests_output:\n" + "\n---\n".join(fail_out)[:8000])

        return "\n".join(parts).strip() or None

