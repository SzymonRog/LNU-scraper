import json
import time
from collections import defaultdict


class Submitter:
    def __init__(self, session, url: str = "https://edu.t-lem.com/"):
        self.session = session
        self.url = url

    # ── PUBLICZNE API ─────────────────────────────────────────

    def submit(self, task_id: int, solution_raw: str) -> dict:
        solution = json.loads(solution_raw)
        files = solution.get("files", [])

        if not files:
            print(f"[{task_id}] Brak plików, pomijam")
            return {}

        # DEBUG
        for f in files:
            print(f"  [{task_id}] Plik: {f['fileName']}")
            print(f"  [{task_id}] Kod (pierwsze 100 znaków): {f['code'][:100]!r}")

        resp = self.session.post(
            self.url,
            data=self._build_payload(task_id, files),
            headers={"X-Requested-With": "XMLHttpRequest"},
        )
        result = resp.json()
        is_correct = result.get("data", {}).get("isCorrect", False)
        print(f"[{task_id}] {'✓' if is_correct else '✗'} isCorrect={is_correct}")
        return result

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
                print(f"  [{row['id']}] Błąd: {e}")

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
            ("act[params][3][deltaTime]",              "5"),
            ("act[params][3][deltaClick]",             "0"),
            ("act[params][3][deltaKeys]",              "0"),
            ("act[params][4][0][eventType]",           "SYSTEM"),
            ("act[params][4][0][payload][buttonType]", "COMPILE"),
            ("act[params][4][0][timestamp]",           str(int(time.time()))),
            ("act[last_ping_time]",                    "35"),
            ("act[ping_count]",                        "14"),
        ]
        return data