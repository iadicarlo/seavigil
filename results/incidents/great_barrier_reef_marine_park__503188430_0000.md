# Incident `great_barrier_reef_marine_park__503188430_0000`

- **MPA:** Great Barrier Reef Marine Park
- **Severity:** LOW (multi-use protected area)  ·  boundary sample-approx-2024
- **Vessel:** `503188430`  ·  **gear:** unknown
- **When (UTC):** 2026-06-25T15:43:31Z → 2026-06-25T15:43:31Z (0.0 h)
- **Apparent fishing:** 1 of 1 in-MPA positions; mean p=0.52, max p=0.52
- **Where:** -16.931, 145.780 (centroid)
- **Vs. speed baseline:** the trivial rule (speed < 10.7 kn) also flags 100% of these positions; here the speed rule alone suffices.

## Why this was flagged

_mean per-position SHAP (fishing class) over the incident's fishing positions._

| feature | mean value | mean SHAP |
|---|---:|---:|
| `distance_from_shore` | 7586.166 | +0.161 |
| `distance_from_port` | 501.568 | -0.129 |
| `speed` | 0.000 | +0.035 |
| `speed_roll_std` | 0.000 | -0.032 |
| `speed_roll_mean` | 0.000 | -0.011 |

## Caveats

- Apparent fishing inferred from AIS movement, not proven illegal fishing.
- AIS-only: blind to vessels not broadcasting AIS (~75% of industrial fishing vessels).
- MPA boundary may be approximate; verify against official WDPA limits.
- An inspection lead, not courtroom evidence.
