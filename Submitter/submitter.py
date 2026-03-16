import json
import logging
import random
import time
from collections import defaultdict
from typing import Any

from lnu.logging_utils import get_logger, setup_logging


class Submitter:
    def __init__(self, session, url: str = "https://edu.t-lem.com/"):
        self.session = session
        self.url = url
        setup_logging(logging.INFO)
        self.log = get_logger(__name__)

    # ── PUBLICZNE API ─────────────────────────────────────────

    def submit(
        self,
        task_id: int,
        solution_raw: str,
        *,
        max_attempts: int = 5,
        backoff_base_seconds: float = 1.0,
        backoff_max_seconds: float = 30.0,
        confirm_timeout_seconds: float = 20.0,
        confirm_poll_seconds: float = 2.0,
    ) -> dict:
        solution = json.loads(solution_raw)
        files = solution.get("files", [])

        if not files:
            self.log.warning("No files in solution; skipping", extra={"task_id": task_id})
            return {}

        last_result: dict[str, Any] = {}
        for attempt in range(1, max_attempts + 1):
            try:
                self.log.info("Submitting", extra={"task_id": task_id, "attempt": attempt})
                resp = self.session.post(
                    self.url,
                    data=self._build_payload(task_id, files),
                    headers={"X-Requested-With": "XMLHttpRequest"},
                )
                last_result = resp.json()
                immediate = last_result.get("data", {}).get("isCorrect", None)

                accepted = self._confirm_acceptance(
                    task_id,
                    immediate_is_correct=bool(immediate) if immediate is not None else None,
                    timeout_seconds=confirm_timeout_seconds,
                    poll_seconds=confirm_poll_seconds,
                )
                if accepted is True:
                    self.log.info("Accepted", extra={"task_id": task_id, "attempt": attempt})
                    return last_result

                self.log.warning(
                    "Not accepted yet; will retry",
                    extra={"task_id": task_id, "attempt": attempt, "immediate_is_correct": immediate},
                )
            except Exception as e:
                self.log.error("Submit failed", extra={"task_id": task_id, "attempt": attempt, "error": repr(e)}, exc_info=True)

            if attempt < max_attempts:
                delay = self._exp_backoff(attempt, backoff_base_seconds, backoff_max_seconds)
                time.sleep(delay)

        return last_result

    def submit_by_path(self, db_manager, path_prefix: str, delay: float = 2.0):
        rows = db_manager.get_solutions()
        filtered = sorted(
            [r for r in rows if (r["path"] or "").startswith(path_prefix)],
            key=lambda r: r["sort_order"]
        )
        print(f"Znaleziono {len(filtered)} zadań dla path: '{path_prefix}'")
        self._send_batch(filtered, delay)

    def submit_by_count(self, db_manager, limit: int, delay: float = 2.0):
        rows = sorted(db_manager.get_solutions(), key=lambda r: r["sort_order"])[:limit]
        print(f"Wysyłam {len(rows)} zadań (limit={limit})")
        self._send_batch(rows, delay)

    def submit_grouped(self, db_manager, delay: float = 2.0, group_delay: float = 5.0):
        rows = sorted(db_manager.get_solutions(), key=lambda r: r["sort_order"])

        groups = defaultdict(list)
        for row in rows:
            groups[row["path"] or "inne"].append(row)

        print(f"Znaleziono {len(groups)} grup, {len(rows)} zadań łącznie\n")

        for path, tasks in groups.items():
            print(f"── {path} ({len(tasks)} zadań)")
            self._send_batch(tasks, delay)
            print(f"   Przerwa między działami ({group_delay}s)...\n")
            time.sleep(group_delay)

    # ── POMOCNICZE ────────────────────────────────────────────

    def _send_batch(self, rows, delay: float):
        for row in rows:
            try:
                self.submit(row["id"], row["solution"])
                time.sleep(delay)
            except Exception as e:
                self.log.error("Batch submit error", extra={"task_id": row["id"], "error": repr(e)}, exc_info=True)

    def _build_payload(self, task_id: int, files: list) -> list[tuple]:
        data = [
            ("act[id]",       "lekcja"),
            ("act[module]",   "lekcja"),
            ("act[params][]", "compile"),
            ("act[params][]", str(task_id)),
        ]
        for i, file in enumerate(files):
            data += [
                (f"act[params][2][{i}][name]", file.get("fileName", "solution")),
                (f"act[params][2][{i}][code]", file.get("code", "")),
            ]
        data += [
            ("act[params][3][deltaTime]",              str(random.randint(20,300))),
            ("act[params][3][deltaClick]",             str(random.randint(10, 100))),
            ("act[params][3][deltaKeys]",               str(random.randint(10, 500))),
            ("act[params][4][0][eventType]",           "MOUSE"),
            ("act[params][4][0][payload][buttonType]", "COMPILE"),
            ("act[params][4][0][timestamp]",           str(int(time.time()))),
            ("act[last_ping_time]",                    "35"),
            ("act[ping_count]",                        "14"),
        ]
        return data

    @staticmethod
    def _exp_backoff(attempt: int, base: float, cap: float) -> float:
        delay = min(cap, base * (2 ** (attempt - 1)))
        jitter = random.uniform(0.0, min(1.0, delay * 0.1))
        return delay + jitter

    def _get_lesson_is_correct(self, task_id: int) -> bool | None:
        resp = self.session.post(
            self.url,
            data=[
                ("act[id]", "lekcja"),
                ("act[module]", "lekcja"),
                ("act[params][]", "get"),
                ("act[params][]", str(task_id)),
                ("act[last_ping_time]", "0"),
                ("act[ping_count]", "0"),
            ],
            headers={"X-Requested-With": "XMLHttpRequest"},
        )
        payload = resp.json().get("data", {})
        if not isinstance(payload, dict):
            return None
        lekcja = payload.get("lekcja", {})
        if not isinstance(lekcja, dict):
            return None
        if "isCorrect" not in lekcja:
            return None
        return bool(lekcja.get("isCorrect"))

    def _confirm_acceptance(
        self,
        task_id: int,
        *,
        immediate_is_correct: bool | None,
        timeout_seconds: float,
        poll_seconds: float,
    ) -> bool | None:
        if immediate_is_correct is True:
            return True
        deadline = time.monotonic() + timeout_seconds
        while time.monotonic() < deadline:
            time.sleep(poll_seconds)
            try:
                status = self._get_lesson_is_correct(task_id)
                if status is True:
                    return True
                if status is False:
                    return False
            except Exception:
                continue
        return None