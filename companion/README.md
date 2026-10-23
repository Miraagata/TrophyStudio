# VCNG Companion — Phase 1

PC-side deterministic analysis layer for VitaCheat NG. The goal is not to make the user operate Cheat Engine manually. The goal is to expose small, testable tools that an agent (Gemini in Antigravity, or another orchestrator) can call while the Vita remains the sensor/executor.

## Current scope

- Parse/summarize VitaCheat NG 0.14.7 Discovery telemetry (`*.discovery-telemetry.tsv`).
- Compare two equal-size raw memory snapshots with `changed`, `unchanged`, `increased`, or `decreased` filters.
- Integer widths: 8/16/32/64-bit; float: 32/64-bit.
- JSON-only tool output for reliable agent consumption.
- Read-only by policy. No memory write or code patch endpoint exists in Phase 1.

## Quick start

```bash
cd companion
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -e .

vcng policy
vcng telemetry "PCSB00000.discovery-telemetry.tsv"
vcng compare before.bin after.bin --mode decreased --width 4
```

## Direction

1. Validate the Vita memory-read path from 0.14.7 telemetry.
2. Add a minimal authenticated Vita↔PC transport.
3. Stream region maps and snapshots to this companion.
4. Let the agent choose deterministic experiments, never raw guesses.
5. Add multi-observation intersection/ranking, struct inference, pointer/AoB jobs.
6. Only after cross-context validation, allow export of disabled cheats.
