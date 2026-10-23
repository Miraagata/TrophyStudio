# VCNG Companion Roadmap

## Phase 1 — deterministic offline analysis (implemented)
- telemetry parser
- raw snapshot pair comparison
- JSON CLI tools
- read-only agent policy

## Phase 2 — Vita transport
- authenticated local TCP session
- title/PID handshake
- memory map enumeration
- bounded chunked reads
- snapshot capture with region metadata
- rate limits and fail-closed disconnect behavior

## Phase 3 — automated narrowing
- multi-snapshot candidate intersection
- temporal behavior scoring
- changed/unchanged/increased/decreased mixed evidence
- type/representation inference
- candidate neighborhood/structure clustering

## Phase 4 — stabilization
- module-relative anchors
- pointer search jobs
- AoB uniqueness jobs
- cross-loading reacquisition
- resolver confidence and revocation

## Phase 5 — agentic discovery
- Gemini/Antigravity chooses experiments
- agent consumes only typed JSON tools
- deterministic evidence ledger
- no semantic promotion without explicit evidence thresholds

## Phase 6 — controlled validation/export
- reversible data-write tests behind an explicit user gate
- cross-context validator
- disabled VitaCheat code generation
- hardware evidence logged per title/build
