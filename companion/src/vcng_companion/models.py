from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Literal

Mode = Literal["changed", "unchanged", "increased", "decreased"]


@dataclass(frozen=True)
class Candidate:
    offset: int
    width: int
    before: int | float
    after: int | float
    kind: str
    score: float = 0.0

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass(frozen=True)
class TelemetrySummary:
    rows: int
    health_counts: dict[str, int]
    max_regions: int
    max_readable_regions: int
    max_mapped_bytes: int
    max_pages_checked: int
    max_read_failures: int
    max_pages_changed: int
    max_deltas: int
    max_candidates: int
    latest_health: str | None

    def to_dict(self) -> dict:
        return asdict(self)
