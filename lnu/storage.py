from __future__ import annotations

import json
import sqlite3
from dataclasses import asdict
from datetime import datetime
from pathlib import Path
from typing import Any

from lnu.logging_utils import get_logger
from lnu.models import Task

log = get_logger(__name__)


class TaskStore:
    """SQLite-backed cache for tasks and their state."""

    def __init__(self, db_path: str) -> None:
        self.db_path = Path(db_path)
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        self._init_db()
        self._migrate()

    def _init_db(self) -> None:
        self.conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id            INTEGER PRIMARY KEY,
                title         TEXT,
                label         TEXT,
                is_correct    INTEGER DEFAULT 0,
                has_code      INTEGER DEFAULT 0,
                solution      TEXT,
                scraped_at    TEXT DEFAULT (datetime('now')),
                path          TEXT,
                sort_order    INTEGER DEFAULT 0
            );
            """
        )
        self.conn.commit()

    def _migrate(self) -> None:
        # Additive migrations only (keep backward compatibility with existing DB).
        for col, ddl in [
            ("raw_json", "TEXT"),
            ("downloaded_at", "TEXT"),
            ("last_fetched_at", "TEXT"),
            ("last_submit_at", "TEXT"),
            ("submit_attempts", "INTEGER DEFAULT 0"),
            ("solve_attempts", "INTEGER DEFAULT 0"),
            ("last_error", "TEXT"),
        ]:
            self._add_column_if_missing(col, ddl)

    def _add_column_if_missing(self, name: str, ddl: str) -> None:
        try:
            self.conn.execute(f"ALTER TABLE tasks ADD COLUMN {name} {ddl}")
            self.conn.commit()
        except sqlite3.OperationalError:
            return

    def close(self) -> None:
        self.conn.close()

    def __enter__(self) -> "TaskStore":
        return self

    def __exit__(self, *_: object) -> None:
        self.close()

    def get_all_ids(self) -> set[int]:
        rows = self.conn.execute("SELECT id FROM tasks").fetchall()
        return {int(r["id"]) for r in rows}

    def upsert_task_row(self, row: dict[str, Any]) -> None:
        self.conn.execute(
            """
            INSERT INTO tasks (
                id, title, label, path, is_correct, has_code, solution, sort_order,
                raw_json, downloaded_at, last_fetched_at, last_submit_at, submit_attempts,
                solve_attempts, last_error, scraped_at
            )
            VALUES (
                :id, :title, :label, :path, :is_correct, :has_code, :solution, :sort_order,
                :raw_json, :downloaded_at, :last_fetched_at, :last_submit_at, :submit_attempts,
                :solve_attempts, :last_error, COALESCE(:scraped_at, datetime('now'))
            )
            ON CONFLICT(id) DO UPDATE SET
                title          = COALESCE(excluded.title, title),
                label          = COALESCE(excluded.label, label),
                path           = COALESCE(excluded.path, path),
                is_correct     = COALESCE(excluded.is_correct, is_correct),
                has_code       = COALESCE(excluded.has_code, has_code),
                solution       = COALESCE(excluded.solution, solution),
                sort_order     = COALESCE(excluded.sort_order, sort_order),
                raw_json       = COALESCE(excluded.raw_json, raw_json),
                downloaded_at  = COALESCE(excluded.downloaded_at, downloaded_at),
                last_fetched_at= COALESCE(excluded.last_fetched_at, last_fetched_at),
                last_submit_at = COALESCE(excluded.last_submit_at, last_submit_at),
                submit_attempts= COALESCE(excluded.submit_attempts, submit_attempts),
                solve_attempts = COALESCE(excluded.solve_attempts, solve_attempts),
                last_error     = COALESCE(excluded.last_error, last_error),
                scraped_at     = datetime('now')
            """,
            row,
        )
        self.conn.commit()

    def mark_submit_attempt(self, task_id: int, attempt: int, last_error: str | None = None) -> None:
        self.conn.execute(
            """
            UPDATE tasks
            SET submit_attempts = ?,
                last_submit_at = datetime('now'),
                last_error = ?
            WHERE id = ?
            """,
            (attempt, last_error, task_id),
        )
        self.conn.commit()

    def mark_solve_attempt(self, task_id: int, attempt: int, last_error: str | None = None) -> None:
        self.conn.execute(
            """
            UPDATE tasks
            SET solve_attempts = ?,
                last_error = ?
            WHERE id = ?
            """,
            (attempt, last_error, task_id),
        )
        self.conn.commit()

    def update_is_correct(self, task_id: int, is_correct: bool) -> None:
        self.conn.execute(
            "UPDATE tasks SET is_correct = ? WHERE id = ?",
            (1 if is_correct else 0, task_id),
        )
        self.conn.commit()

    def update_solution(self, task_id: int, solution_json: str) -> None:
        self.conn.execute(
            "UPDATE tasks SET solution = ?, has_code = 1 WHERE id = ?",
            (solution_json, task_id),
        )
        self.conn.commit()

    def list_incomplete_or_missing(self) -> list[sqlite3.Row]:
        return self.conn.execute(
            """
            SELECT id, title, label, path, is_correct, has_code, sort_order
            FROM tasks
            WHERE downloaded_at IS NULL OR is_correct = 0
            ORDER BY sort_order ASC
            """
        ).fetchall()

    def list_missing_solution(self, *, exclude_path_contains: str | None = None) -> list[sqlite3.Row]:
        """Rows that need fetching because solution is missing (NULL).

        This is used by `sync` when you only want to refresh tasks without cached code.
        """
        if exclude_path_contains:
            return self.conn.execute(
                """
                SELECT id, title, label, path, is_correct, has_code, sort_order
                FROM tasks
                WHERE solution IS NULL
                  AND (path IS NULL OR path NOT LIKE ?)
                ORDER BY sort_order ASC
                """,
                (f"%{exclude_path_contains}%",),
            ).fetchall()

        return self.conn.execute(
            """
            SELECT id, title, label, path, is_correct, has_code, sort_order
            FROM tasks
            WHERE solution IS NULL
            ORDER BY sort_order ASC
            """
        ).fetchall()

    def list_solutions(self, path_prefix: str | None = None) -> list[sqlite3.Row]:
        if path_prefix:
            return self.conn.execute(
                """
                SELECT id, title, label, path, solution, sort_order
                FROM tasks
                WHERE has_code = 1 AND solution IS NOT NULL AND (path LIKE ?)
                ORDER BY sort_order ASC
                """,
                (f"{path_prefix}%",),
            ).fetchall()
        return self.conn.execute(
            """
            SELECT id, title, label, path, solution, sort_order
            FROM tasks
            WHERE has_code = 1 AND solution IS NOT NULL
            ORDER BY sort_order ASC
            """
        ).fetchall()

    @staticmethod
    def task_from_row(r: sqlite3.Row) -> Task:
        return Task(
            id=int(r["id"]),
            title=r["title"],
            path=r["path"],
            sort_order=int(r["sort_order"]) if r["sort_order"] is not None else None,
            label=r["label"],
            is_correct=bool(r["is_correct"]) if r["is_correct"] is not None else None,
        )

    @staticmethod
    def dump_raw_json(payload: dict[str, Any] | None) -> str | None:
        if payload is None:
            return None
        return json.dumps(payload, ensure_ascii=False)

    @staticmethod
    def now_iso() -> str:
        return datetime.utcnow().isoformat()

