from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Protocol

from lnu.logging_utils import get_logger

log = get_logger(__name__)

try:
    import httpx  # type: ignore
except Exception:  # pragma: no cover
    httpx = None  # type: ignore


class AIClient(Protocol):
    async def complete(self, prompt: str) -> str: ...

    @property
    def name(self) -> str: ...


@dataclass(slots=True)
class OllamaClient:
    """Free/local provider via Ollama.

    Requires Ollama running locally (`ollama serve`) and the model pulled.
    """

    base_url: str = "http://127.0.0.1:11434"
    model: str = "qwen2.5-coder:3b"
    timeout_seconds: float = 120.0

    @property
    def name(self) -> str:
        return f"ollama:{self.model}"

    async def complete(self, prompt: str) -> str:
        if httpx is None:  # pragma: no cover
            raise RuntimeError("Missing dependency: httpx. Install with `pip install -r requirements.txt`.")
        async with httpx.AsyncClient(base_url=self.base_url, timeout=httpx.Timeout(self.timeout_seconds)) as client:
            resp = await client.post(
                "/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False,
                },
            )
            resp.raise_for_status()
            data = resp.json()
            return str(data.get("response", ""))


class NoopAIClient:
    """Fallback provider when no AI is configured."""

    @property
    def name(self) -> str:
        return "none"

    async def complete(self, prompt: str) -> str:
        raise RuntimeError(
            "No AI provider configured. Configure Ollama or plug in another provider."
        )


def extract_json_from_text(text: str) -> dict[str, Any]:
    """Best-effort extraction of a JSON object from model output."""
    text = text.strip()
    if text.startswith("{") and text.endswith("}"):
        return json.loads(text)

    # Common pattern: fenced block ```json ... ```
    start = text.find("{")
    end = text.rfind("}")
    if start >= 0 and end > start:
        return json.loads(text[start : end + 1])
    raise ValueError("Model output does not contain a JSON object")

