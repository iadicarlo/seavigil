# Incident `great_barrier_reef_marine_park__503756000_0000`

- **MPA:** Great Barrier Reef Marine Park
- **Severity:** LOW (multi-use protected area)  ·  boundary sample-approx-2024
- **Vessel:** 🇦🇺 REEF ADVENTURE  ·  **gear:** unknown
- **When (UTC):** 2026-06-25T19:01:58Z → 2026-06-25T19:01:58Z (0.0 h)
- **Apparent fishing:** 1 of 1 in-MPA positions; mean p=0.50, max p=0.50
- **Where:** -16.922, 145.781 (centroid)
- **Vs. speed baseline:** the trivial rule (speed < 10.7 kn) also flags 100% of these positions; here the speed rule alone suffices.

## Why this was flagged

_mean per-position SHAP (fishing class) over the incident's fishing positions._

| feature | mean value | mean SHAP |
|---|---:|---:|
| `distance_from_shore` | 6626.252 | +0.162 |
| `distance_from_port` | 1096.553 | -0.127 |
| `speed_roll_std` | 0.000 | -0.035 |
| `speed` | 0.000 | +0.034 |
| `speed_roll_mean` | 0.000 | -0.015 |

## Caveats

- Apparent fishing inferred from AIS movement, not proven illegal fishing.
- AIS-only: blind to vessels not broadcasting AIS (~75% of industrial fishing vessels).
- MPA boundary may be approximate; verify against official WDPA limits.
- An inspection lead, not courtroom evidence.
