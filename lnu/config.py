from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True, slots=True)
class Config:
    base_url: str = "https://edu.t-lem.com/"
    sqlite_path: str = "lnu_tasks.db"
    requests_per_minute: int = 10
    submit_delay_seconds: float = 0.0
    submit_max_attempts: int = 5
    solve_max_attempts: int = 3
    backoff_base_seconds: float = 1.0
    backoff_max_seconds: float = 30.0

    # AI provider settings
    ai_provider: str = "ollama"  # or "none"
    ollama_base_url: str = "http://127.0.0.1:11434"
    ollama_model: str = "qwen2.5-coder:3b"


def load_config(path: str | None = None, env: dict[str, str] | None = None) -> Config:
    """Load configuration from YAML (optional) + env overrides.

    Design decision: YAML is optional; env remains the primary mechanism
    (keeps backward compatibility with your existing `.env` usage).
    """

    data: dict[str, Any] = {}
    if path:
        p = Path(path)
        if p.exists():
            try:
                import yaml  # type: ignore
            except Exception as e:  # pragma: no cover
                raise RuntimeError("PyYAML is required to load YAML config") from e
            data = yaml.safe_load(p.read_text(encoding="utf-8")) or {}

    env = env or {}

    def _get(key: str, cast, default):
        if key in env and env[key] != "":
            try:
                return cast(env[key])
            except Exception:
                return default
        return data.get(key, default)

    defaults = Config()
    return Config(
        base_url=str(_get("base_url", str, defaults.base_url)),
        sqlite_path=str(_get("sqlite_path", str, defaults.sqlite_path)),
        requests_per_minute=int(_get("requests_per_minute", int, defaults.requests_per_minute)),
        submit_delay_seconds=float(_get("submit_delay_seconds", float, defaults.submit_delay_seconds)),
        submit_max_attempts=int(_get("submit_max_attempts", int, defaults.submit_max_attempts)),
        solve_max_attempts=int(_get("solve_max_attempts", int, defaults.solve_max_attempts)),
        backoff_base_seconds=float(_get("backoff_base_seconds", float, defaults.backoff_base_seconds)),
        backoff_max_seconds=float(_get("backoff_max_seconds", float, defaults.backoff_max_seconds)),
        ai_provider=str(_get("ai_provider", str, defaults.ai_provider)),
        ollama_base_url=str(_get("ollama_base_url", str, defaults.ollama_base_url)),
        ollama_model=str(_get("ollama_model", str, defaults.ollama_model)),
    )

