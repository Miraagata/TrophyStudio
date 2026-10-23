from __future__ import annotations

import json
from pathlib import Path

from .analysis import scan_pair
from .telemetry import summarize_telemetry


def compare_files(
    before_path: str,
    after_path: str,
    *,
    mode: str,
    width: int = 4,
    signed: bool = False,
    floating: bool = False,
    alignment: int | None = None,
    limit: int = 200,
) -> dict:
    before = Path(before_path).read_bytes()
    after = Path(after_path).read_bytes()
    candidates = scan_pair(
        before,
        after,
        mode=mode,  # type: ignore[arg-type]
        width=width,
        signed=signed,
        floating=floating,
        alignment=alignment,
        limit=limit,
    )
    return {
        "tool": "compare_files",
        "mode": mode,
        "width": width,
        "candidate_count_returned": len(candidates),
        "candidates": [c.to_dict() for c in candidates],
    }


def telemetry_summary(path: str) -> dict:
    summary = summarize_telemetry(path)
    return {"tool": "telemetry_summary", **summary.to_dict()}


def dumps(obj: dict) -> str:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True)
