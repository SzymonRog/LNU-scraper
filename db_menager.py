import json
import sqlite3
from typing import Any

from lnu.storage import TaskStore


class DbManager(TaskStore):
    """Backward-compatible wrapper around the new `TaskStore`.

    Design decision: keep old public methods (`upsert_task`, `get_solutions`, ...)
    working, while the new architecture uses `lnu.storage.TaskStore` directly.
    """

    def __init__(self, db_path: str = "lnu_tasks.db"):
        super().__init__(db_path=db_path)

    def upsert_task(self, task: dict[str, Any]):
        if isinstance(task.get("solution"), dict):
            task["solution"] = json.dumps(task["solution"], ensure_ascii=False)

        row = {
            "id": task.get("id"),
            "title": task.get("title"),
            "label": task.get("label"),
            "path": task.get("path"),
            "is_correct": task.get("is_correct"),
            "has_code": task.get("has_code"),
            "solution": task.get("solution"),
            "sort_order": task.get("sort_order", 0),
            "raw_json": None,
            "downloaded_at": None,
            "last_fetched_at": None,
            "last_submit_at": None,
            "submit_attempts": None,
            "solve_attempts": None,
            "last_error": None,
            "scraped_at": None,
        }
        self.upsert_task_row(row)

    def get_solutions(self) -> list[sqlite3.Row]:
        return self.list_solutions()

    def get_stats(self) -> dict:
        row = self.conn.execute(
            """
            SELECT
                COUNT(*)         AS total,
                SUM(is_correct)  AS correct,
                SUM(has_code)    AS with_code
            FROM tasks
            """
        ).fetchone()
        return dict(row) if row else {"total": 0, "correct": 0, "with_code": 0}

    def clean_db(self):
        self.conn.execute("DROP TABLE IF EXISTS tasks")
        self.conn.commit()
        self._init_db()
        self._migrate()

    def add_column(self, name: str):
        # Keep method for compatibility; new code uses migrations.
        try:
            self.conn.execute(f"ALTER TABLE tasks ADD COLUMN {name} TEXT")
            self.conn.commit()
        except sqlite3.OperationalError:
            return
