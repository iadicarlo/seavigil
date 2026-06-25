# Incident `great_barrier_reef_marine_park__503000239_0000`

- **MPA:** Great Barrier Reef Marine Park
- **Severity:** LOW (multi-use protected area)  ·  boundary sample-approx-2024
- **Vessel:** `503000239`  ·  **gear:** unknown
- **When (UTC):** 2026-06-25T16:24:48Z → 2026-06-25T16:24:48Z (0.0 h)
- **Apparent fishing:** 1 of 1 in-MPA positions; mean p=0.60, max p=0.60
- **Where:** -16.783, 145.736 (centroid)
- **Vs. speed baseline:** the trivial rule (speed < 10.7 kn) also flags 100% of these positions; here the speed rule alone suffices.

## Why this was flagged

_mean per-position SHAP (fishing class) over the incident's fishing positions._

| feature | mean value | mean SHAP |
|---|---:|---:|
| `distance_from_port` | 16859.123 | +0.207 |
| `speed_roll_std` | 0.000 | -0.043 |
| `speed_roll_mean` | 0.200 | -0.033 |
| `hour_cos` | -0.407 | -0.032 |
| `speed` | 0.200 | +0.018 |

## Caveats

- Apparent fishing inferred from AIS movement, not proven illegal fishing.
- AIS-only: blind to vessels not broadcasting AIS (~75% of industrial fishing vessels).
- MPA boundary may be approximate; verify against official WDPA limits.
- An inspection lead, not courtroom evidence.
