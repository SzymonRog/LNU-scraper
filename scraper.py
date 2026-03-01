import re
import time
import os
from traceback import extract_tb

from bs4 import BeautifulSoup
import requests
import jwt
from dotenv import load_dotenv
from requests import options
from db_menager import DbManager

load_dotenv()


env = os.getenv("ENV")

class Scraper():
    def __init__(self):
        self.session = requests.Session()
        self.set_cookies()
        self.URL = 'https://edu.t-lem.com/'
        self.db = DbManager()

    def set_cookies(self):
        lem_token = os.getenv('LEM_TOKEN')
        events_token = os.getenv('EVENTS_TOKEN')
        lnu_session = os.getenv('LNU_SESSION')


        self.session.cookies.set('LEM_TOKEN',lem_token , domain='.t-lem.com')
        self.session.cookies.set('EVENTS_TOKEN', events_token, domain='.t-lem.com')
        self.session.cookies.set('LNU_SESSION', lnu_session, domain='edu.t-lem.com')





    def is_token_valid(self, token: str) -> bool:
        try:
            payload = jwt.decode(token, options={'verify_signature': False})
            return payload['exp'] > time.time()
        except:
            return False

    def get_data(self):
        resp = self.session.post('https://edu.t-lem.com/', data=[
            ('act[id]', 'menus'),
            ('act[module]', 'menus'),
            ('act[params][]', 'get'),
            ('act[last_ping_time]', '0'),
            ('act[ping_count]', '0'),
        ], headers={'X-Requested-With': 'XMLHttpRequest'})

        return resp.json()['data']['menus']

    def sanitize(self,name: str) -> str:
        name = name.strip()
        name = re.sub(r'[<>:"/\\|?*]', '', name)
        return name

    def extract_ids(self, menus, path="", result=None):
        if result is None:
            result = {}

        for item in menus:
            segment = self.sanitize(item.get('title', str(item['id'])))
            current_path = os.path.join(path, segment) if path else segment

            if 'submenus' in item:
                self.extract_ids(item['submenus'], current_path, result)
            else:
                result[int(item['id'])] = {
                    'id': int(item['id']),
                    'title': item.get('title', ''),
                    'path': current_path,
                }

        return result


    def get_menu(self):
        menus = self.get_data()
        return self.extract_ids(menus)

    def get_lesson_data(self, lesson_id: int) -> dict | None:
        resp = self.session.post(self.URL, data=[
            ('act[id]', 'lekcja'),
            ('act[module]', 'lekcja'),
            ('act[params][]', 'get'),
            ('act[params][]', str(lesson_id)),
            ('act[last_ping_time]', '0'),
            ('act[ping_count]', '0'),
        ], headers={'X-Requested-With': 'XMLHttpRequest'})

        data = resp.json().get('data', {})


        if not isinstance(data, dict):
            return None

        lekcja = data.get('lekcja', {})
        user = data.get('user', {})

        if not lekcja:
            return None

        solution = lekcja.get('t_code') or None

        return {
            'id': lekcja.get('id'),
            'title': lekcja.get('s_tytul'),
            'label': user.get('custom') or None,
            'is_correct': 1 if lekcja.get('isCorrect') else 0,
            'has_code': 1 if solution else 0,
            'solution': solution,
        }

    def update_paths(self, tasks: dict):
        """Aktualizuje path dla zadań już w DB na podstawie danych z menu."""
        updated = 0
        skipped = 0

        for task_id, task_meta in tasks.items():
            result = self.db.conn.execute(
                "UPDATE tasks SET path = ? WHERE id = ?",
                (task_meta['path'], task_id)
            )
            if result.rowcount > 0:
                updated += 1
            else:
                skipped += 1

        self.db.conn.commit()
        print(f"Zaktualizowano: {updated}, pominięto (brak w DB): {skipped}")

    def scrape_all(self):
        print("Pobieram listę zadań...")
        tasks = self.get_menu()

        total = len(tasks)
        for i, (task_id, task_meta) in enumerate(tasks.items(), 1):
            print(f"[{i}/{total}] Zadanie {task_id}...", end=" ")

            try:
                data = self.get_lesson_data(task_id)

                if data is None or data.get('id') is None:
                    print("brak danych, pomijam")
                    continue

                data['path'] = task_meta['path']
                data['sort_order'] = i
                self.db.upsert_task(data)
                status = "✓" if data['is_correct'] else "○"
                print(f"{status} {data['title']}")

            except Exception as e:
                print(f"błąd: {e}")

        print(f"\nGotowe! Zapisano {total} zadań.")

    def update_sort_order(self):
        print("Aktualizuję sort_order...")
        tasks = self.get_menu()  # kolejność z API = realna kolejność w menu

        # NIE sortuj po id — użyj kolejności jak przyszła z API
        for i, (task_id, _) in enumerate(tasks.items(), 1):
            self.db.conn.execute(
                "UPDATE tasks SET sort_order = ? WHERE id = ?",
                (i, task_id)
            )

        self.db.conn.commit()
        print(f"Zaktualizowano sort_order dla {len(tasks)} zadań.")






