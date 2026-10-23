# VitaCheat NG — Development Log

Continuous engineering record. This file tracks decisions, hypotheses, audits and gates; release-specific details remain in each version changelog.

## Frozen baseline — 0.14.6

- 0.14.4: kernel/I/O hardening and first reproducible ARM/VPK build with VitaSDK 2026.08.
- 0.14.5: post-audit fixes including FD lifecycle, positional I/O wire structs, stricter fail-closed execution, `$C` button handling, thread unload synchronization and resolver/persistence corrections.
- Real Vita result on 0.14.5: runtime remained active behind the game, but Discovery produced no visible candidates and appeared not to read useful memory.
- 0.14.6: diagnostic build exposing map enumeration, bridge probe, sampler pages, checked/failed reads, changes, deltas and candidate samples.
- 0.14.6 is frozen on branch `vcng-stable-0.14.6`.

## 0.14.7 — current development

Goal: make zero-candidate failures persistently diagnosable instead of depending only on the overlay.

Implemented:
- portable `discovery_diag` classifier shared by UI and reports;
- persistent per-title Discovery telemetry TSV every 10 seconds while active;
- final telemetry snapshot on unload;
- autonomous Discovery report now saves even when zero candidates exist;
- report header includes map/bridge/sampler health and counters;
- new host regression test for health classification and TSV formatting.

Host gates:
- normal host tests: 57/57 PASS;
- ASan + UBSan (`detect_leaks=0`): 57/57 PASS;
- CMake Release + CTest: 57/57 PASS.

ARM/VPK gate:
- During CI, two source-packaging omissions were exposed: `kernel/io_wire.c` and `src/value_compare.c` had been supplied by build-only patches instead of the distributed Vita CMake source. The 0.14.7 source now carries those links directly.
- The release process was also corrected so new untracked source files are staged before patch generation; otherwise `git diff` silently omitted `vcng_discovery_diag.h` and `discovery_diag.c`.
- Final GitHub Actions build: run `39274717858`, job `118135909457`, commit `69d27ddc79968c7ca6b31137fb6c0a6d7e86fb72` — PASS with VitaSDK 2026.08 / GCC 15.2.
- CI ARM artifact SHA-256: `b308d8d3fd480b2461121d1842249bcb47c484a4d2a5462300c23824c5350089`.
- VPK SHA-256: `ced3fcea63a02c3f2af10d2409fe81b9576e1029c1d6905d0870318f6e6db22a`.
- SKPRX SHA-256: `85fccd01b6eae22b391b183a046cc6d6f78517f620df7def0820576ff2dc41a1`.
- SUPRX SHA-256: `2c4ca9fc1ed6a0042534062f51ed93fa7dc39d409d34b118fd7a3c17e328340d`.
- Final self-contained source ZIP SHA-256: `ff41eab8be58e036fab932411c74ebb4b1d82000096bc0bd98076d08244aea60`.
- Final 0.14.6→0.14.7 full patch SHA-256: `6ad21649055b6320e874f21caff72e0b84e5bd8b73fbd9e33bc485d8cd18448b`.
- 0.14.7 remains hardware-pending: ARM success does not prove the Discovery read path on a real Vita.

## VCNG Companion / agentic discovery — Phase 1

Decision: keep automated code discovery as the primary objective. Gemini via Antigravity is introduced as an orchestrator that chooses experiments; deterministic tools remain responsible for all measurements and candidate generation.

Branch: `vcng-agent-companion`.

Implemented:
- PC-side standard-library Python companion under `companion/`;
- raw snapshot pair scanner for changed/unchanged/increased/decreased values;
- 8/16/32/64-bit integer and 32/64-bit float support;
- parser/summarizer for 0.14.7 Discovery telemetry TSV;
- typed JSON CLI intended for Antigravity/Gemini tool calls;
- explicit agent policy: no invented addresses, no semantic promotion from one event, no cheat export before cross-context validation;
- memory writes and code patches intentionally absent from Phase 1;
- `ANTIGRAVITY.md`, roadmap and dedicated Companion development log;
- GitHub Actions CI for tests and JSON CLI smoke test.

Validation:
- local standard-library tests: 3/3 PASS;
- GitHub Actions run `39984849960`, job `120521246424`: PASS;
- next gate: real 0.14.7 telemetry, then authenticated Vita↔PC transport and automated multi-snapshot narrowing.

Next engineering decisions will use real 0.14.6/0.14.7 telemetry to determine whether the root cause is map enumeration, kernel read bridge, sampler coverage or downstream filtering. Larger audit items (K-06/M-01, UI/runtime concurrency, code-patch semantics and multiwrite atomicity) remain queued and are not mixed into the frozen baseline.
