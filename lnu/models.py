from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Literal


@dataclass(frozen=True, slots=True)
class Task:
    id: int
    title: str | None = None
    path: str | None = None
    sort_order: int | None = None
    label: str | None = None

    # Server-side status
    is_correct: bool | None = None

    # Locally cached artifacts
    downloaded_at: datetime | None = None
    raw: dict[str, Any] | None = None


@dataclass(frozen=True, slots=True)
class SolutionFile:
    file_name: str
    code: str


@dataclass(frozen=True, slots=True)
class Solution:
    task_id: int
    files: list[SolutionFile]
    provider: str = "unknown"
    created_at: datetime = field(default_factory=datetime.utcnow)
    raw: dict[str, Any] | None = None


@dataclass(frozen=True, slots=True)
class SubmissionResult:
    task_id: int
    accepted: bool
    attempt: int
    server_is_correct: bool | None = None
    server_payload: dict[str, Any] | None = None
    status: Literal["accepted", "rejected", "unknown"] = "unknown"


class TaskSolveError(RuntimeError):
    """Raised when task solving/submission fails after retries."""

