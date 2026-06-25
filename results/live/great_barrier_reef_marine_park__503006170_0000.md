# Incident `great_barrier_reef_marine_park__503006170_0000`

- **MPA:** Great Barrier Reef Marine Park
- **Severity:** LOW (multi-use protected area)  ·  boundary sample-approx-2024
- **Vessel:** 🇦🇺 BANDICOOT  ·  **gear:** unknown
- **When (UTC):** 2026-06-25T19:01:18Z → 2026-06-25T19:02:18Z (0.017 h)
- **Apparent fishing:** 2 of 2 in-MPA positions; mean p=0.54, max p=0.54
- **Where:** -16.945, 145.774 (centroid)
- **Track:** 2 positions, (-16.945, 145.774) → (-16.945, 145.774)
- **Vs. speed baseline:** the trivial rule (speed < 10.7 kn) also flags 100% of these positions; here the speed rule alone suffices.

## Why this was flagged

_mean per-position SHAP (fishing class) over the incident's fishing positions._

| feature | mean value | mean SHAP |
|---|---:|---:|
| `distance_from_shore` | 9284.417 | +0.180 |
| `distance_from_port` | 1696.051 | -0.131 |
| `speed` | 0.000 | +0.038 |
| `speed_roll_std` | 0.000 | -0.024 |
| `hour_sin` | -0.964 | -0.013 |

## Caveats

- Apparent fishing inferred from AIS movement, not proven illegal fishing.
- AIS-only: blind to vessels not broadcasting AIS (~75% of industrial fishing vessels).
- MPA boundary may be approximate; verify against official WDPA limits.
- An inspection lead, not courtroom evidence.
