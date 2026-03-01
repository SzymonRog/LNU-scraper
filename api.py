import os
import time
import json
import requests
from collections import defaultdict
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
security = HTTPBearer()

API_PASSWORD = os.getenv("API_PASSWORD", "changeme")
LNU_URL = "https://edu.t-lem.com/"


# ── AUTH ─────────────────────────────────────────────────────

def verify(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.credentials != API_PASSWORD:
        raise HTTPException(status_code=401, detail="Nieprawidłowe hasło")
    return credentials


# ── MODELE ───────────────────────────────────────────────────

class TokensBase(BaseModel):
    lem_token: str
    events_token: str
    lnu_session: str

class SubmitByPath(TokensBase):
    path_prefix: str
    delay: float = 3.0

class SubmitByTask(TokensBase):
    task_id: int
    solution_raw: str  # JSON string z {"files": [...]}

class SubmitByCount(TokensBase):
    limit: int
    delay: float = 3.0


# ── HELPERS ──────────────────────────────────────────────────

def make_session(tokens: TokensBase) -> requests.Session:
    session = requests.Session()
    session.cookies.set("LEM_TOKEN",    tokens.lem_token,    domain=".t-lem.com")
    session.cookies.set("EVENTS_TOKEN", tokens.events_token, domain=".t-lem.com")
    session.cookies.set("LNU_SESSION",  tokens.lnu_session,  domain="edu.t-lem.com")
    return session


def build_payload(task_id: int, files: list) -> list[tuple]:
    data = [
        ("act[id]",       "lekcja"),
        ("act[module]",   "lekcja"),
        ("act[params][]", "compile"),
        ("act[params][]", str(task_id)),
    ]
    for i, f in enumerate(files):
        data += [
            (f"act[params][2][{i}][name]", f.get("fileName", "solution")),
            (f"act[params][2][{i}][code]", f.get("code", "")),
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


def submit_task(session, task_id: int, solution_raw: str) -> dict:
    files = json.loads(solution_raw).get("files", [])
    if not files:
        return {"task_id": task_id, "skipped": True}

    resp = session.post(
        LNU_URL,
        data=build_payload(task_id, files),
        headers={"X-Requested-With": "XMLHttpRequest"},
    )
    data = resp.json().get("data", {})
    return {
        "task_id":    task_id,
        "is_correct": data.get("isCorrect", False),
        "build_ok":   data.get("buildStatus", False),
        "errors":     data.get("compilationErrors", False),
    }


def get_solutions_from_db(path_prefix: str = None, limit: int = None) -> list[dict]:
    """Pobiera rozwiązania z lokalnej DB."""
    import sqlite3
    conn = sqlite3.connect("lnu_tasks.db")
    conn.row_factory = sqlite3.Row

    rows = conn.execute("""
        SELECT id, title, path, sort_order, solution
        FROM tasks
        WHERE has_code = 1 AND solution IS NOT NULL
        ORDER BY sort_order ASC
    """).fetchall()
    conn.close()

    result = [dict(r) for r in rows]

    if path_prefix:
        result = [r for r in result if (r["path"] or "").startswith(path_prefix)]
    if limit:
        result = result[:limit]

    return result


# ── ENDPOINTS ────────────────────────────────────────────────

@app.post("/submit/task")
def submit_single(body: SubmitByTask, _=Depends(verify)):
    """Wyślij konkretne zadanie z podanym kodem."""
    session = make_session(body)
    result = submit_task(session, body.task_id, body.solution_raw)
    return result


@app.post("/submit/path")
def submit_by_path(body: SubmitByPath, _=Depends(verify)):
    """Wyślij wszystkie rozwiązania pasujące do path_prefix."""
    session = make_session(body)
    tasks = get_solutions_from_db(path_prefix=body.path_prefix)

    if not tasks:
        raise HTTPException(status_code=404, detail="Brak zadań dla podanego path")

    results = []
    for task in tasks:
        r = submit_task(session, task["id"], task["solution"])
        results.append(r)
        time.sleep(body.delay)

    return {
        "total":   len(results),
        "correct": sum(1 for r in results if r.get("is_correct")),
        "results": results,
    }


@app.post("/submit/count")
def submit_by_count(body: SubmitByCount, _=Depends(verify)):
    """Wyślij pierwsze N rozwiązań."""
    session = make_session(body)
    tasks = get_solutions_from_db(limit=body.limit)

    results = []
    for task in tasks:
        r = submit_task(session, task["id"], task["solution"])
        results.append(r)
        time.sleep(body.delay)

    return {
        "total":   len(results),
        "correct": sum(1 for r in results if r.get("is_correct")),
        "results": results,
    }


@app.get("/paths")
def list_paths(_=Depends(verify)):
    """Zwraca listę unikalnych path z DB — do wyboru w UI."""
    import sqlite3
    conn = sqlite3.connect("lnu_tasks.db")
    rows = conn.execute(
        "SELECT DISTINCT path FROM tasks WHERE path IS NOT NULL ORDER BY path"
    ).fetchall()
    conn.close()
    return {"paths": [r[0] for r in rows]}