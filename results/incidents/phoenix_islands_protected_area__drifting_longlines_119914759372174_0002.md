# Incident `phoenix_islands_protected_area__drifting_longlines_119914759372174_0002`

- **MPA:** Phoenix Islands Protected Area (WDPA 309888)
- **Severity:** MEDIUM (protected area (category not reported))  ·  boundary WDPA/WD-OECM Jun2026
- **Vessel:** `drifting_longlines_119914759372174`  ·  **gear:** drifting_longlines
- **When (UTC):** 2014-08-19T05:46:11Z → 2014-08-20T03:52:38Z (22.108 h)
- **Apparent fishing:** 49 of 54 in-MPA positions; mean p=0.88, max p=1.00
- **Where:** -2.629, -170.982 (centroid)
- **Track:** 54 positions, (-2.619, -171.090) → (-2.554, -170.922)
- **Vs. speed baseline:** the trivial rule (speed < 10.7 kn) also flags 100% of these positions; here the speed rule alone suffices.

## Why this was flagged

_mean per-position SHAP (fishing class) over the incident's fishing positions._

| feature | mean value | mean SHAP |
|---|---:|---:|
| `speed` | 4.735 | +0.131 |
| `speed_roll_mean` | 5.025 | +0.120 |
| `distance_from_shore` | 56943.615 | +0.064 |
| `speed_roll_std` | 1.067 | +0.041 |
| `distance_from_port` | 84845.961 | +0.013 |

## Caveats

- Apparent fishing inferred from AIS movement, not proven illegal fishing.
- AIS-only: blind to vessels not broadcasting AIS (~75% of industrial fishing vessels).
- MPA boundary may be approximate; verify against official WDPA limits.
- An inspection lead, not courtroom evidence.
