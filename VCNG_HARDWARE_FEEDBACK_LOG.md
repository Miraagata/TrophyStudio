# VitaCheat NG — Hardware Feedback Log

## 0.14.5

Observed on a real PS Vita:
- plugin/runtime stayed active behind the game;
- no codes/candidates were separated during the test;
- after normal gameplay and value changes, Discovery still showed no useful candidates;
- working hypothesis: memory enumeration/read bridge/sampler coverage was not producing usable observations.

Interpretation:
- injection/runtime stability: positive partial evidence;
- Discovery memory read path: not validated;
- candidate generation: not validated.

## 0.14.6 — frozen diagnostic baseline

Status:
- source and ARM/VPK built successfully;
- branch `vcng-stable-0.14.6` freezes the build state;
- waiting for real DIAG/READ capture after 20–30 seconds of active Discovery gameplay.

Expected evidence:
- region count, readable/writable count, mapped bytes;
- enum/sampler return codes;
- bridge probe result/address;
- sampler pages, initialized/checked/failed reads;
- pages changed, exact deltas and candidate samples.

## 0.14.7

Status:
- host 57/57 PASS, ASan/UBSan 57/57 PASS, CMake/CTest 57/57 PASS;
- ARM/VPK build PASS in GitHub Actions run `39274717858`, job `118135909457`;
- hardware behavior still pending.

New hardware evidence will also be persisted to:
- `ux0:data/vitacheat-ng/state/<TITLEID>.discovery-telemetry.tsv`
- `ux0:data/vitacheat-ng/generated/<TITLEID>.discovery.txt`

The report is now written even when Discovery finds zero candidates. The next hardware gate is to verify those files are created, then inspect the persisted health/counter sequence to distinguish map enumeration failure, bridge read failure, sampler coverage failure or downstream filtering.
