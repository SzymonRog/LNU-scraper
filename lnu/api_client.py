from __future__ import annotations

import asyncio
import json
import os
from pathlib import Path
from dataclasses import dataclass
from typing import Any

from lnu.logging_utils import get_logger

log = get_logger(__name__)

try:
    from dotenv import load_dotenv  # type: ignore
except Exception:  # pragma: no cover
    load_dotenv = None  # type: ignore

try:
    import httpx  # type: ignore
except Exception:  # pragma: no cover
    httpx = None  # type: ignore

try:
    import requests  # type: ignore
except Exception:  # pragma: no cover
    requests = None  # type: ignore


def _load_dotenv_fallback(dotenv_path: str | None = None) -> None:
    """Minimal `.env` loader fallback.

    Design decision: keep CLI usable even if `python-dotenv` isn't installed.
    Only loads KEY=VALUE pairs; ignores comments and blank lines.
    """
    path = Path(dotenv_path or ".env")
    if not path.exists():
        return
    try:
        for raw_line in path.read_text(encoding="utf-8").splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if key and key not in os.environ:
                os.environ[key] = value
    except Exception:
        # Never fail hard just because `.env` parsing is imperfect.
        return


@dataclass(frozen=True, slots=True)
class AuthCookies:
    lem_token: str
    events_token: str
    lnu_session: str

    @staticmethod
    def from_env(env: dict[str, str] | None = None) -> "AuthCookies":
        # Try loading from `.env` (either via python-dotenv or fallback parser)
        if load_dotenv is not None:
            load_dotenv()
        else:
            _load_dotenv_fallback()

        env = env or os.environ
        lem = env.get("LEM_TOKEN", "")
        events = env.get("EVENTS_TOKEN", "")
        session = env.get("LNU_SESSION", "")
        if not (lem and events and session):
            raise RuntimeError("Missing auth cookies in env: LEM_TOKEN/EVENTS_TOKEN/LNU_SESSION")
        return AuthCookies(lem_token=lem, events_token=events, lnu_session=session)


class LnuApiClient:
    """Async API client for `https://edu.t-lem.com/` backend."""

    def __init__(self, base_url: str, cookies: AuthCookies, timeout_seconds: float = 30.0) -> None:
        self.base_url = base_url.rstrip("/") + "/"
        self._timeout_seconds = timeout_seconds
        self._cookies = cookies

        # Prefer httpx if available, but keep a robust requests fallback.
        self._mode: str = "requests"
        self._client: Any = None
        self._requests_session: Any = None

        if httpx is not None:
            try:
                self._client = httpx.AsyncClient(
                    base_url=self.base_url,
                    timeout=httpx.Timeout(timeout_seconds),
                    headers={"X-Requested-With": "XMLHttpRequest"},
                )
                # Domain cookie scoping matters for the platform
                self._client.cookies.set("LEM_TOKEN", cookies.lem_token, domain=".t-lem.com")
                self._client.cookies.set("EVENTS_TOKEN", cookies.events_token, domain=".t-lem.com")
                self._client.cookies.set("LNU_SESSION", cookies.lnu_session, domain="edu.t-lem.com")
                self._mode = "httpx"
            except Exception:
                self._client = None
                self._mode = "requests"

        if self._mode == "requests":
            if requests is None:  # pragma: no cover
                raise RuntimeError(
                    "Missing dependency: httpx or requests. Install with `pip install -r requirements.txt`."
                )
            self._requests_session = requests.Session()
            self._requests_session.headers.update({"X-Requested-With": "XMLHttpRequest"})
            self._requests_session.cookies.set("LEM_TOKEN", cookies.lem_token, domain=".t-lem.com")
            self._requests_session.cookies.set("EVENTS_TOKEN", cookies.events_token, domain=".t-lem.com")
            self._requests_session.cookies.set("LNU_SESSION", cookies.lnu_session, domain="edu.t-lem.com")

    async def aclose(self) -> None:
        if self._mode == "httpx" and self._client is not None:
            await self._client.aclose()
        if self._mode == "requests" and self._requests_session is not None:
            try:
                self._requests_session.close()
            except Exception:
                return

    async def _post(self, data: list[tuple[str, str]]) -> dict[str, Any]:
        if self._mode == "httpx" and self._client is not None:
            try:
                resp = await self._client.post("", data=data)
                resp.raise_for_status()
                return resp.json()
            except RuntimeError as e:
                # Some environments misconfigure transports and httpx raises:
                # "Attempted to send an sync request with an AsyncClient instance."
                msg = str(e)
                if "sync request" in msg and "AsyncClient" in msg:
                    log.warning("httpx async transport issue; falling back to requests", extra={"error": msg})
                    self._mode = "requests"
                    if self._requests_session is None:
                        if requests is None:  # pragma: no cover
                            raise
                        self._requests_session = requests.Session()
                        self._requests_session.headers.update({"X-Requested-With": "XMLHttpRequest"})
                        c = self._cookies
                        self._requests_session.cookies.set("LEM_TOKEN", c.lem_token, domain=".t-lem.com")
                        self._requests_session.cookies.set("EVENTS_TOKEN", c.events_token, domain=".t-lem.com")
                        self._requests_session.cookies.set("LNU_SESSION", c.lnu_session, domain="edu.t-lem.com")
                    return await self._post(data)
                raise

        # requests fallback (run in a thread so our API remains async)
        assert self._requests_session is not None

        def _do() -> dict[str, Any]:
            r = self._requests_session.post(self.base_url, data=data, timeout=self._timeout_seconds)
            r.raise_for_status()
            return r.json()

        return await asyncio.to_thread(_do)

    async def post_act(self, act_id: str, module: str, params: list[str], extra_params: list[tuple[str, str]] | None = None) -> dict[str, Any]:
        data: list[tuple[str, str]] = [
            ("act[id]", act_id),
            ("act[module]", module),
        ]
        for p in params:
            data.append(("act[params][]", p))
        data += [
            ("act[last_ping_time]", "0"),
            ("act[ping_count]", "0"),
        ]
        if extra_params:
            data.extend(extra_params)

        return await self._post(data)

    async def get_menus(self) -> list[dict[str, Any]]:
        payload = await self.post_act("menus", "menus", ["get"])
        return payload["data"]["menus"]

    async def save_last_id(self, lesson_id: int) -> dict[str, Any]:
        """Entry like: act[id]=save, act[module]=menus, params=saveLastId,<id>."""
        return await self.post_act("save", "menus", ["saveLastId", str(lesson_id)])

    async def get_lesson(self, lesson_id: int) -> dict[str, Any]:
        payload = await self.post_act("lekcja", "lekcja", ["get", str(lesson_id)])
        data = payload.get("data", {})
        if not isinstance(data, dict):
            return {}
        return data

    async def get_lesson_summary(self, lesson_id: int) -> dict[str, Any]:
        """Entry like: act[id]=lekcja, act[module]=lekcja, params=summary,<id>."""
        payload = await self.post_act("lekcja", "lekcja", ["summary", str(lesson_id)])
        data = payload.get("data", {})
        return data if isinstance(data, dict) else {}

    async def compile_solution(self, lesson_id: int, files: list[dict[str, str]], telemetry: dict[str, str] | None = None) -> dict[str, Any]:
        # Mirrors the existing "compile" action used by your current Submitter.
        data: list[tuple[str, str]] = [
            ("act[id]", "lekcja"),
            ("act[module]", "lekcja"),
            ("act[params][]", "compile"),
            ("act[params][]", str(lesson_id)),
        ]
        for i, f in enumerate(files):
            data += [
                (f"act[params][2][{i}][name]", f.get("fileName", "solution")),
                (f"act[params][2][{i}][code]", f.get("code", "")),
            ]
        # Telemetry fields appear required/expected by the backend; keep defaults.
        telemetry = telemetry or {}
        data += [
            ("act[params][3][deltaTime]", telemetry.get("deltaTime", "60")),
            ("act[params][3][deltaClick]", telemetry.get("deltaClick", "20")),
            ("act[params][3][deltaKeys]", telemetry.get("deltaKeys", "120")),
            ("act[params][4][0][eventType]", "MOUSE"),
            ("act[params][4][0][payload][buttonType]", "COMPILE"),
            ("act[params][4][0][timestamp]", telemetry.get("timestamp", "0")),
            ("act[last_ping_time]", telemetry.get("last_ping_time", "35")),
            ("act[ping_count]", telemetry.get("ping_count", "14")),
        ]

        return await self._post(data)

    @staticmethod
    def parse_is_correct(payload: dict[str, Any]) -> bool | None:
        data = payload.get("data")
        if isinstance(data, dict) and "isCorrect" in data:
            try:
                return bool(data.get("isCorrect"))
            except Exception:
                return None
        return None

    @staticmethod
    def extract_task_fields(lesson_payload: dict[str, Any]) -> dict[str, Any]:
        """Extracts a stable subset of fields from `get_lesson` payload.

        Design decision: backend schema may evolve; we keep raw payload too.
        """
        lekcja = (lesson_payload.get("lekcja") or {}) if isinstance(lesson_payload, dict) else {}
        user = (lesson_payload.get("user") or {}) if isinstance(lesson_payload, dict) else {}
        if not isinstance(lekcja, dict):
            lekcja = {}
        if not isinstance(user, dict):
            user = {}

        return {
            "id": lekcja.get("id"),
            "title": lekcja.get("s_tytul"),
            "label": user.get("custom") or None,
            "is_correct": bool(lekcja.get("isCorrect")) if lekcja.get("isCorrect") is not None else None,
            # Observed solution field in your current scraper:
            "solution_raw": lekcja.get("t_code") or None,
            # Likely task text fields (best-effort; safe if missing):
            "content_html": lekcja.get("t_tresc") or lekcja.get("t_opis") or lekcja.get("t_zadanie") or None,
        }

