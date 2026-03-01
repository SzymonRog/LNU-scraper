import json
import re
from pathlib import Path


class Exporter:
    def __init__(self, base_dir: str = "solutions"):
        self.base = Path(base_dir)

    def export(self, task_id: int, title: str, path_str: str, solution_raw: str):
        solution = json.loads(solution_raw)
        files = solution.get("files", [])

        if not files:
            print(f"[{task_id}] Brak plików, pomijam")
            return

        folder = self._build_path(path_str, task_id, title)
        folder.mkdir(parents=True, exist_ok=True)

        for file in files:
            file_name = file.get("fileName", "solution.txt")
            code = file.get("code", "")
            (folder / file_name).write_text(code, encoding="utf-8")

        print(f"[{task_id}] → {folder}")
        return folder

    def export_all(self, db_manager):
        rows = db_manager.get_solutions()
        print(f"Eksportuję {len(rows)} zadań...")
        for row in rows:
            try:
                self.export(
                    task_id=row["id"],
                    title=row["title"] or "bez_tytulu",
                    path_str=row["path"] or "",
                    solution_raw=row["solution"],
                )
            except Exception as e:
                print(f"[{row['id']}] Błąd: {e}")

    def _build_path(self, path_str: str, task_id: int, title: str) -> Path:
        """
        '{^menu_lessons}\\Język C++\\Poziom Podstawowy\\Tablice'
        → solutions/Język C++/Poziom Podstawowy/Tablice/1_Tytuł
        """
        # Usuń prefix {^...}
        clean = re.sub(r"\{[^}]+\}\\?", "", path_str)
        # Podziel po \ i odfiltruj puste
        parts = [self._safe(p) for p in clean.split("\\") if p.strip()]
        return self.base.joinpath(*parts)

    @staticmethod
    def _safe(name: str) -> str:
        """Usuwa znaki niedozwolone w nazwach folderów."""
        return re.sub(r'[<>:"/|?*]', "_", name).strip()
