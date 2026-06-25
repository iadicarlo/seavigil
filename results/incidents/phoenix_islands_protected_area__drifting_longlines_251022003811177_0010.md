# Incident `phoenix_islands_protected_area__drifting_longlines_251022003811177_0010`

- **MPA:** Phoenix Islands Protected Area
- **Severity:** HIGH (strict no-take reserve)  ·  boundary sample-approx-2024
- **Vessel:** `drifting_longlines_251022003811177`  ·  **gear:** drifting_longlines
- **When (UTC):** 2014-12-13T06:48:46Z → 2014-12-13T10:52:38Z (4.064 h)
- **Apparent fishing:** 148 of 148 in-MPA positions; mean p=0.88, max p=0.97
- **Where:** -3.482, -171.038 (centroid)
- **Track:** 148 positions, (-3.494, -171.139) → (-3.472, -170.928)
- **Vs. speed baseline:** the trivial rule (speed < 10.7 kn) also flags 100% of these positions; here the speed rule alone suffices.

## Why this was flagged

_mean per-position SHAP (fishing class) over the incident's fishing positions (sampled 50 of 148)._

| feature | mean value | mean SHAP |
|---|---:|---:|
| `speed_roll_mean` | 4.338 | +0.148 |
| `speed` | 4.420 | +0.146 |
| `speed_roll_std` | 0.725 | +0.036 |
| `distance_from_shore` | 37370.264 | +0.026 |
| `hour_cos` | -0.658 | +0.013 |

## Caveats

- Apparent fishing inferred from AIS movement, not proven illegal fishing.
- AIS-only: blind to vessels not broadcasting AIS (~75% of industrial fishing vessels).
- MPA boundary may be approximate; verify against official WDPA limits.
- An inspection lead, not courtroom evidence.
