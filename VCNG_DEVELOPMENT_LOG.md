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

Next engineering decisions will use real 0.14.6/0.14.7 telemetry to determine whether the root cause is map enumeration, kernel read bridge, sampler coverage or downstream filtering. Larger audit items (K-06/M-01, UI/runtime concurrency, code-patch semantics and multiwrite atomicity) remain queued and are not mixed into the frozen baseline.
