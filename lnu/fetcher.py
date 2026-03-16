from __future__ import annotations

import asyncio
import os
import re
import json
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from lnu.api_client import LnuApiClient
from lnu.logging_utils import get_logger
from lnu.models import Task
from lnu.rate_limit import RateLimiter
from lnu.storage import TaskStore

log = get_logger(__name__)


def _sanitize(name: str) -> str:
    name = name.strip()
    return re.sub(r'[<>:"/\\|?*]', "", name)


def _extract_menu_ids(menus: list[dict[str, Any]], path: str = "", out: dict[int, dict[str, Any]] | None = None) -> dict[int, dict[str, Any]]:
    if out is None:
        out = {}
    for item in menus:
        segment = _sanitize(str(item.get("title") or item.get("id") or ""))
        current_path = os.path.join(path, segment) if path else segment
        sub = item.get("submenus")
        if isinstance(sub, list) and sub:
            _extract_menu_ids(sub, current_path, out)
        else:
            try:
                task_id = int(item["id"])
            except Exception:
                continue
            out[task_id] = {"id": task_id, "title": item.get("title", ""), "path": current_path}
    return out


@dataclass(slots=True)
class TaskFetcher:
    api: LnuApiClient
    store: TaskStore
    rate_limiter: RateLimiter | None = None

    async def fetch_new_tasks(self) -> list[Task]:
        """Fetch tasks that are missing locally (solution is NULL), excluding SQL paths.

        Design decision: uses menu as the source of truth for task list/order,
        and stores raw payload for future-proofing/debugging.
        """
        # Only tasks with missing solution, but skip anything from "Język SQL"
        rows = self.store.list_missing_solution(exclude_path_contains="Język SQL")
        ordered = [int(r["id"]) for r in rows]

        fetched: list[Task] = []
        total = len(ordered)
        for idx, task_id in enumerate(ordered, 1):
            if self.rate_limiter:
                await self.rate_limiter.acquire()
            try:
                lesson_payload = await self.api.get_lesson(task_id)
                fields = self.api.extract_task_fields(lesson_payload)

                # Keep existing DB path/sort_order when doing "missing solution" refreshes
                title = fields.get("title")
                path = None
                sort_order = None
                solution_raw = fields.get("solution_raw")
                if isinstance(solution_raw, dict):
                    solution_raw = json.dumps(solution_raw, ensure_ascii=False)

                row = {
                    "id": task_id,
                    "title": title,
                    "label": fields.get("label"),
                    "path": path,
                    "is_correct": 1 if fields.get("is_correct") else 0,
                    "has_code": 1 if solution_raw else 0,
                    "solution": solution_raw,
                    "sort_order": sort_order or 0,
                    "raw_json": self.store.dump_raw_json(lesson_payload),
                    "downloaded_at": datetime.utcnow().isoformat(),
                    "last_fetched_at": datetime.utcnow().isoformat(),
                    "last_submit_at": None,
                    "submit_attempts": None,
                    "solve_attempts": None,
                    "last_error": None,
                    "scraped_at": None,
                }
                self.store.upsert_task_row(row)
                fetched.append(
                    Task(
                        id=task_id,
                        title=title,
                        path=path,
                        sort_order=sort_order,
                        label=fields.get("label"),
                        is_correct=fields.get("is_correct"),
                        downloaded_at=datetime.utcnow(),
                        raw=lesson_payload,
                    )
                )
                log.info("Fetched task", extra={"task_id": task_id, "idx": idx, "total": total, "is_correct": fields.get("is_correct")})
            except Exception as e:
                log.warning("Fetch failed", extra={"task_id": task_id, "idx": idx, "total": total, "error": repr(e)}, exc_info=True)
                self.store.upsert_task_row(
                    {
                        "id": task_id,
                        "title": None,
                        "label": None,
                        "path": None,
                        "is_correct": None,
                        "has_code": None,
                        "solution": None,
                        "sort_order": 0,
                        "raw_json": None,
                        "downloaded_at": None,
                        "last_fetched_at": datetime.utcnow().isoformat(),
                        "last_submit_at": None,
                        "submit_attempts": None,
                        "solve_attempts": None,
                        "last_error": repr(e),
                        "scraped_at": None,
                    }
                )

        return fetched

    async def periodic_sync(self, interval_seconds: float = 300.0, stop_event: asyncio.Event | None = None) -> None:
        while True:
            if stop_event and stop_event.is_set():
                return
            await self.fetch_new_tasks()
            await asyncio.sleep(interval_seconds)

