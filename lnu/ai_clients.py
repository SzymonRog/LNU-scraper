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
                    "temperature": 0.7,
                    "options": {
                        "num_predict": 4096,
                    }
                },
            )
            resp.raise_for_status()
            data = resp.json()
            return str(data.get("response", ""))


@dataclass(slots=True)
class GroqClient:
    """Cloud provider via Groq API (free tier available at console.groq.com)."""

    api_key: str
    model: str = "llama-3.3-70b-versatile"
    timeout_seconds: float = 60.0

    @property
    def name(self) -> str:
        return f"groq:{self.model}"

    async def complete(self, prompt: str) -> str:
        if httpx is None:
            raise RuntimeError("Missing dependency: httpx.")
        async with httpx.AsyncClient(timeout=httpx.Timeout(self.timeout_seconds)) as client:
            resp = await client.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={"Authorization": f"Bearer {self.api_key}"},
                json={
                    "model": self.model,
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.3,
                    "max_tokens": 4096,
                },
            )
            resp.raise_for_status()
            return resp.json()["choices"][0]["message"]["content"]


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
    text = text.strip()

    # Usuń thinking block (<think>...</think>) który qwen3 dołącza przed JSONem
    import re
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()

    start = text.find("{")
    end = text.rfind("}")
    if start < 0 or end <= start:
        raise ValueError("Model output does not contain a JSON object")

    candidate = text[start:end + 1]

    # Próba 1: strict parse
    try:
        return json.loads(candidate)
    except json.JSONDecodeError:
        pass

    # Próba 2: strict=False akceptuje niedozwolone control chars (tab, newline w stringach)
    try:
        return json.loads(candidate, strict=False)
    except json.JSONDecodeError:
        pass

    # Próba 3: zamień literal control chars na ich escaped odpowiedniki
    # Dotyczy tylko wnętrza JSON string values, nie struktury
    def escape_control_chars(s: str) -> str:
        result = []
        in_string = False
        escape_next = False
        for ch in s:
            if escape_next:
                result.append(ch)
                escape_next = False
                continue
            if ch == '\\':
                escape_next = True
                result.append(ch)
                continue
            if ch == '"' and not escape_next:
                in_string = not in_string
                result.append(ch)
                continue
            if in_string and ord(ch) < 32:
                # Zamień na escape sequence
                escapes = {'\n': '\\n', '\r': '\\r', '\t': '\\t', '\b': '\\b', '\f': '\\f'}
                result.append(escapes.get(ch, f'\\u{ord(ch):04x}'))
            else:
                result.append(ch)
        return ''.join(result)

    cleaned = escape_control_chars(candidate)
    return json.loads(cleaned)


