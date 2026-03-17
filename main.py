from __future__ import annotations

import argparse
import asyncio
import logging
import os
from typing import Any

try:
    from dotenv import load_dotenv  # type: ignore
except Exception:  # pragma: no cover
    load_dotenv = None  # type: ignore

from lnu.ai_clients import NoopAIClient, OllamaClient, GroqClient
from lnu.api_client import AuthCookies, LnuApiClient
from lnu.config import load_config
from lnu.fetcher import TaskFetcher
from lnu.logging_utils import setup_logging
from lnu.rate_limit import RateLimiter
from lnu.solver import TaskSolver
from lnu.storage import TaskStore
from lnu.submitter import ReliableSubmitter


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="lnu", description="LNU task sync/solve/submit automation")
    p.add_argument("--config", default=None, help="Optional YAML config path")
    p.add_argument("--log-level", default="INFO", help="DEBUG/INFO/WARNING/ERROR")

    sub = p.add_subparsers(dest="cmd", required=False)

    sub_sync = sub.add_parser("sync", help="Fetch tasks not downloaded or not completed")
    sub_sync.add_argument("--interval", type=float, default=0.0, help="If >0, keep syncing every N seconds")

    sub_solve = sub.add_parser("solve", help="Solve and submit tasks")
    sub_solve.add_argument("--lesson", type=str, default=None, help="Single lesson/task id to solve")
    sub_solve.add_argument(
        "--path",
        type=str,
        default=None,
        help="Solve all tasks under this DB path prefix (accepts / or \\)",
    )

    sub_submit = sub.add_parser("submit", help="Submit existing solutions from DB")
    sub_submit.add_argument("--path", type=str, default=None, help="Only submit tasks with path prefix")
    sub_submit.add_argument("--delay", type=float, default=0.0, help="Optional delay between tasks (seconds)")

    return p


async def _run(args: argparse.Namespace) -> None:
    if load_dotenv is not None:
        load_dotenv()
    cfg = load_config(args.config, env=os.environ)

    rpm = int(cfg.requests_per_minute)
    limiter = RateLimiter(rpm)

    cookies = AuthCookies.from_env(os.environ)
    api = LnuApiClient(cfg.base_url, cookies=cookies)

    store = TaskStore(cfg.sqlite_path)

    fetcher = TaskFetcher(api=api, store=store, rate_limiter=limiter)
    submitter = ReliableSubmitter(
        api=api,
        store=store,
        rate_limiter=limiter,
        backoff_base_seconds=cfg.backoff_base_seconds,
        backoff_max_seconds=cfg.backoff_max_seconds,
        max_attempts=cfg.submit_max_attempts,
    )

    groq_key = os.getenv("GROQ_API_KEY")
    if groq_key:
        ai_client = GroqClient(api_key=groq_key, model="llama-3.3-70b-versatile")
    else:
        if cfg.ai_provider.lower() == "ollama":
            ai_client = OllamaClient(base_url=cfg.ollama_base_url, model=cfg.ollama_model)
        else:
            ai_client = NoopAIClient()

    solver = TaskSolver(
        api=api,
        store=store,
        submitter=submitter,
        ai_client=ai_client,
        rate_limiter=limiter,
        rate_limit_per_min=cfg.requests_per_minute,
        solve_max_attempts=cfg.solve_max_attempts,
    )

    try:
        if args.cmd == "sync":
            if args.interval and args.interval > 0:
                stop = asyncio.Event()
                await fetcher.periodic_sync(interval_seconds=float(args.interval), stop_event=stop)
            else:
                await fetcher.fetch_new_tasks()
            return

        if args.cmd == "solve":
            if args.lesson:
                await solver.solve_lesson(args.lesson)
                return

            def _norm_path(p: str | None) -> str:
                if not p:
                    return ""
                # Normalize separators so users can pass `/...` even on Windows.
                import re

                p2 = p.strip()
                # Strip optional LNU menu prefix like "{^menu_lessons}\..."
                p2 = re.sub(r"^\{[^}]+\}[\\/]*", "", p2)
                p2 = p2.lstrip("/\\")
                p2 = p2.replace("\\", "/")
                while "//" in p2:
                    p2 = p2.replace("//", "/")
                return p2.casefold()

            wanted = _norm_path(getattr(args, "path", None))

            # If no lesson specified: solve tasks that are downloaded but not completed.
            rows = store.list_incomplete_or_missing()
            if wanted:
                rows = [r for r in rows if _norm_path(r["path"]).startswith(wanted)]

            for r in rows:
                task_id = int(r["id"])
                await solver.solve_lesson(str(task_id))
            return

        if args.cmd == "submit":
            rows = store.list_solutions(args.path)
            for r in rows:
                sol = ReliableSubmitter.parse_solution_json(int(r["id"]), str(r["solution"]))
                await submitter.submit_with_confirmation(sol)
                if args.delay and args.delay > 0:
                    await asyncio.sleep(float(args.delay))
            return

        # Backward-compatible default behavior: do a single sync.
        await fetcher.fetch_new_tasks()
    finally:
        store.close()
        await api.aclose()


def main() -> None:
    parser = _build_parser()
    args = parser.parse_args()
    level = getattr(logging, str(args.log_level).upper(), logging.INFO)
    setup_logging(level=level)
    asyncio.run(_run(args))


if __name__ == "__main__":
    main()

