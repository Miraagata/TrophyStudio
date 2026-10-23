# Gemini / Antigravity operating contract for VitaCheat NG

## Mission

Automate cheat discovery. Do not make the user perform manual First Scan / Next Scan work.

## Tooling model

Use the local `vcng` CLI as the evidence layer. It returns JSON. Treat every result as an observation, never as proof of semantics.

## Mandatory loop

1. Inspect telemetry health first.
2. If the read path is unhealthy, diagnose the failing stage and stop semantic inference.
3. When snapshots are available, formulate one falsifiable hypothesis.
4. Choose a deterministic comparison (`changed`, `unchanged`, `increased`, `decreased`) and a type/width.
5. Ask for another gameplay experiment when evidence is ambiguous.
6. Promote candidates only after repeated confirming and inverse behavior.
7. Require cross-context survival before asking for resolver work.
8. Prefer module-relative/pointer/signature resolvers over raw addresses.
9. Never fabricate a VitaCheat code line.
10. Generated cheats must remain OFF by default.

## Current Phase 1 restrictions

- Read-only analysis.
- No process memory write tool.
- No code-patch tool.
- No automated semantic label from a single event.
- No “confirmed” candidate without at least three independent validating contexts.

## Example investigation

User action: takes damage, then heals, then takes damage again.

Agent plan:
- compare snapshot A→B with `decreased` for u16/u32/f32;
- compare B→C with `increased` using the same types;
- intersect offsets;
- compare C→D with `decreased`;
- rank survivors and request one loading/respawn test;
- only then request pointer/signature stabilization.

The agent's job is to choose the next experiment. The deterministic engine's job is to produce measurements.
