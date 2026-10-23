# VCNG Companion Development Log

## 0.1.0 — Phase 1 foundation

Decision: keep the automated-discovery objective central. Gemini/Antigravity is an orchestrator, not a replacement for deterministic memory tooling.

Implemented:
- standard-library Python package;
- JSON CLI contract for agent calls;
- read-only pairwise snapshot scanner for integer and float values;
- VitaCheat NG 0.14.7 telemetry summarizer;
- explicit agent policy forbidding guessed addresses/codes and premature semantic labels;
- initial tests for integer/float scanning and telemetry parsing.

Safety/quality rule: the companion does not expose memory writes or code patches in Phase 1. The next step is to connect real Vita memory transport only after 0.14.7 telemetry proves where the current read pipeline fails.
