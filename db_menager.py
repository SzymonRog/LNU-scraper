import json
import sqlite3
from pathlib import Path


class DbManager:
    def __init__(self, db_path: str = "lnu_tasks.db"):
        self.db_path = Path(db_path)

        try:
            self.conn = sqlite3.connect(self.db_path)
            self.conn.execute("SELECT 1")
        except sqlite3.DatabaseError:
            print("⚠️ Database corrupted — recreating")
            self.db_path.unlink(missing_ok=True)
            self.conn = sqlite3.connect(self.db_path)

        self.conn.row_factory = sqlite3.Row
        self._init_db()

    def _init_db(self):
        self.conn.executescript("""
            CREATE TABLE IF NOT EXISTS tasks (
                id          INTEGER PRIMARY KEY,
                title       TEXT,
                label       TEXT,
                is_correct  INTEGER DEFAULT 0,
                has_code    INTEGER DEFAULT 0,
                solution    TEXT,
                scraped_at  TEXT DEFAULT (datetime('now')),
                path        TEXT,
                sort_order  INTEGER DEFAULT 0
            );
        """)
        self.conn.commit()

    # ── ZAPIS ────────────────────────────────────────────────

    def upsert_task(self, task: dict):
        if isinstance(task.get("solution"), dict):
            task["solution"] = json.dumps(task["solution"], ensure_ascii=False)

        self.conn.execute("""
            INSERT INTO tasks (id, title, label, path, is_correct, has_code, solution)
            VALUES (:id, :title, :label, :path, :is_correct, :has_code, :solution)
            ON CONFLICT(id) DO UPDATE SET
                title      = excluded.title,
                label      = excluded.label,
                path       = excluded.path,
                is_correct = excluded.is_correct,
                sort_order = excluded.sort_order,
                has_code   = excluded.has_code,
                solution   = excluded.solution,
                scraped_at = datetime('now')
        """, task)
        self.conn.commit()
    # ── ODCZYT ───────────────────────────────────────────────

    def get_all_ids(self) -> set[int]:
        """Zwraca zbiór wszystkich ID które są już w bazie."""
        rows = self.conn.execute("SELECT id FROM tasks").fetchall()
        return {row["id"] for row in rows}

    def get_solutions(self) -> list[sqlite3.Row]:
        return self.conn.execute("""
            SELECT id, title, label, path, solution,sort_order
            FROM tasks
            WHERE has_code = 1 AND solution IS NOT NULL
            ORDER BY sort_order ASC
        """).fetchall()

    def get_stats(self) -> dict:
        row = self.conn.execute("""
            SELECT
                COUNT(*)       AS total,
                SUM(is_correct) AS correct,
                SUM(has_code)   AS with_code
            FROM tasks
        """).fetchone()
        return dict(row)

    def clean_db(self):
        self.conn.execute("DROP TABLE IF EXISTS tasks")
        self.conn.commit()
        self._init_db()

    def add_column(self, name: str):
        try:
            self.conn.execute(f"ALTER TABLE tasks ADD COLUMN {name} TEXT")
            self.conn.commit()
        except sqlite3.OperationalError:
            print(f"Kolumna '{name}' już istnieje, pomijam")

    # ── CLEANUP ──────────────────────────────────────────────

    def close(self):
        self.conn.close()

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.close()
