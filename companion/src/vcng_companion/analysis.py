from __future__ import annotations

import math
import struct
from typing import Iterable

from .models import Candidate, Mode

_INT_FORMATS = {
    (1, False): "<B",
    (1, True): "<b",
    (2, False): "<H",
    (2, True): "<h",
    (4, False): "<I",
    (4, True): "<i",
    (8, False): "<Q",
    (8, True): "<q",
}
_FLOAT_FORMATS = {4: "<f", 8: "<d"}


def _matches(mode: Mode, before: int | float, after: int | float) -> bool:
    if isinstance(before, float) or isinstance(after, float):
        if not (math.isfinite(float(before)) and math.isfinite(float(after))):
            return False
    if mode == "changed":
        return after != before
    if mode == "unchanged":
        return after == before
    if mode == "increased":
        return after > before
    if mode == "decreased":
        return after < before
    raise ValueError(f"unsupported mode: {mode}")


def scan_pair(
    before: bytes,
    after: bytes,
    *,
    mode: Mode,
    width: int = 4,
    signed: bool = False,
    floating: bool = False,
    alignment: int | None = None,
    start: int = 0,
    end: int | None = None,
    limit: int | None = None,
) -> list[Candidate]:
    if len(before) != len(after):
        raise ValueError("snapshots must have equal length")
    if floating and width not in _FLOAT_FORMATS:
        raise ValueError("floating width must be 4 or 8")
    if not floating and (width, signed) not in _INT_FORMATS:
        raise ValueError("integer width must be 1, 2, 4, or 8")
    if alignment is None:
        alignment = width
    if alignment <= 0:
        raise ValueError("alignment must be positive")
    end = len(before) if end is None else min(end, len(before))
    if start < 0 or start > end:
        raise ValueError("invalid range")

    fmt = _FLOAT_FORMATS[width] if floating else _INT_FORMATS[(width, signed)]
    kind = ("f" if floating else ("i" if signed else "u")) + str(width * 8)
    out: list[Candidate] = []
    pos = start
    rem = pos % alignment
    if rem:
        pos += alignment - rem

    while pos + width <= end:
        b = struct.unpack_from(fmt, before, pos)[0]
        a = struct.unpack_from(fmt, after, pos)[0]
        if _matches(mode, b, a):
            delta = abs(float(a) - float(b)) if a != b else 0.0
            score = 1.0 + min(delta, 1_000_000.0) / 1_000_000.0
            out.append(Candidate(pos, width, b, a, kind, score))
            if limit is not None and len(out) >= limit:
                break
        pos += alignment
    return out


def intersect_candidates(candidate_sets: Iterable[Iterable[Candidate]]) -> list[Candidate]:
    sets = [list(s) for s in candidate_sets]
    if not sets:
        return []
    by_key = {(c.offset, c.width, c.kind): c for c in sets[0]}
    for items in sets[1:]:
        keys = {(c.offset, c.width, c.kind) for c in items}
        by_key = {k: c for k, c in by_key.items() if k in keys}
    return sorted(by_key.values(), key=lambda c: (-c.score, c.offset))
