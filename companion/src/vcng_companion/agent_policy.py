from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AgentPolicy:
    allow_reads: bool = True
    allow_writes: bool = False
    allow_code_patch: bool = False
    minimum_validation_contexts: int = 3
    require_resolver_before_export: bool = True


DEFAULT_POLICY = AgentPolicy()

SYSTEM_RULES = """\
VCNG Agent rules:
1. Treat tool output as evidence, not as a conclusion.
2. Never invent addresses, offsets, pointers, AoB signatures, or cheat lines.
3. Never claim a semantic label (HP, stamina, money, etc.) from one correlated change.
4. Require repeated observations with inverse/confirming behavior when possible.
5. Require cross-context validation (loading/respawn/menu/mission) before promotion.
6. Prefer stable resolver evidence (module-relative/pointer/signature) over raw addresses.
7. Generated cheats must remain disabled by default.
8. Memory writes and code patches are disabled in Phase 1.
9. If evidence is insufficient, request the next experiment instead of guessing.
"""
