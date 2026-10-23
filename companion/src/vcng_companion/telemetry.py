from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

from .models import TelemetrySummary


def _int(row: dict[str, str], *names: str) -> int:
    for name in names:
        value = row.get(name)
        if value not in (None, ""):
            try:
                return int(value, 0)
            except ValueError:
                try:
                    return int(float(value))
                except ValueError:
                    pass
    return 0


def summarize_telemetry(path: str | Path) -> TelemetrySummary:
    p = Path(path)
    with p.open("r", encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        rows = list(reader)

    health = Counter()
    latest_health = None
    max_regions = max_readable = max_mem = max_checked = 0
    max_fail = max_changed = max_deltas = max_candidates = 0
    for row in rows:
        h = row.get("health") or row.get("status") or "UNKNOWN"
        latest_health = h
        health[h] += 1
        max_regions = max(max_regions, _int(row, "regions", "reg"))
        max_readable = max(max_readable, _int(row, "readable_regions", "readable", "r"))
        max_mem = max(max_mem, _int(row, "mapped_bytes", "mem"))
        max_checked = max(max_checked, _int(row, "pages_checked", "checked", "chk"))
        max_fail = max(max_fail, _int(row, "read_failures", "failures", "fail"))
        max_changed = max(max_changed, _int(row, "pages_changed", "changed", "chg"))
        max_deltas = max(max_deltas, _int(row, "deltas", "delta"))
        max_candidates = max(max_candidates, _int(row, "candidates", "cand"))

    return TelemetrySummary(
        rows=len(rows),
        health_counts=dict(health),
        max_regions=max_regions,
        max_readable_regions=max_readable,
        max_mapped_bytes=max_mem,
        max_pages_checked=max_checked,
        max_read_failures=max_fail,
        max_pages_changed=max_changed,
        max_deltas=max_deltas,
        max_candidates=max_candidates,
        latest_health=latest_health,
    )
