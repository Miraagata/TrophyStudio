# VitaCheat NG — Stable baseline 0.14.6

Frozen development baseline: `vcng-stable-0.14.6`.

Hardware evidence known at freeze time:
- 0.14.5 injected successfully and remained active behind a running game.
- Discovery did not produce candidates during the first hardware test and appeared not to be reading useful game memory.
- 0.14.6 added on-screen DIAG/READ counters for map enumeration, bridge read probe, sampler reads, failures, changes, deltas and candidate samples.
- 0.14.6 ARM/VPK build passed with VitaSDK 2026.08.

Policy:
- Do not modify the stable branch in place.
- New work continues on `vcng-development` with normal patch-version increments.
- Hardware-dependent findings stay open until reproduced/validated on a real Vita.
