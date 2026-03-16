from __future__ import annotations

import asyncio
import time


class RateLimiter:
    """Async rate limiter (requests per minute).

    Design decision: simple leaky-bucket based on timestamps, queues callers
    by awaiting. This prevents bursts that can trigger bans.
    """

    def __init__(self, requests_per_minute: int) -> None:
        if requests_per_minute <= 0:
            raise ValueError("requests_per_minute must be > 0")
        self._rpm = requests_per_minute
        self._interval = 60.0 / float(requests_per_minute)
        self._lock = asyncio.Lock()
        self._next_allowed = 0.0

    async def acquire(self) -> None:
        async with self._lock:
            now = time.monotonic()
            wait = self._next_allowed - now
            if wait > 0:
                await asyncio.sleep(wait)
            self._next_allowed = max(now, self._next_allowed) + self._interval

