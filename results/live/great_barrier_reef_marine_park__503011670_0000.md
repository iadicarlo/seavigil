# Incident `great_barrier_reef_marine_park__503011670_0000`

- **MPA:** Great Barrier Reef Marine Park
- **Severity:** LOW (multi-use protected area)  ·  boundary sample-approx-2024
- **Vessel:** 🇦🇺 QPV PERRY IRWIN  ·  **gear:** unknown  ·  Law enforcement
- **When (UTC):** 2026-06-26T23:53:57Z → 2026-06-26T23:53:57Z (0.0 h)
- **Apparent fishing:** 1 of 1 in-MPA positions; mean p=0.68, max p=0.68
- **Where:** -16.952, 145.773 (centroid)
- **Vs. speed baseline:** the trivial rule (speed < 10.7 kn) also flags 100% of these positions; here the speed rule alone suffices.

## Why this was flagged

_mean per-position SHAP (fishing class) over the incident's fishing positions._

| feature | mean value | mean SHAP |
|---|---:|---:|
| `distance_from_shore` | 10042.837 | +0.210 |
| `distance_from_port` | 2504.321 | -0.088 |
| `speed` | 0.000 | +0.047 |
| `hour_cos` | 1.000 | +0.028 |
| `speed_roll_std` | 0.000 | -0.022 |

## Caveats

- Apparent fishing inferred from AIS movement, not proven illegal fishing.
- AIS-only: blind to vessels not broadcasting AIS (~75% of industrial fishing vessels).
- MPA boundary may be approximate; verify against official WDPA limits.
- An inspection lead, not courtroom evidence.

## Provenance & integrity

- Global Fishing Watch labelled AIS training data (Kroodsma et al., Science 2018). CC BY 4.0.
- WDPA / WD-OECM (World Database on Protected Areas) (UNEP-WCMC and IUCN (2026), June 2026). Protected Planet Terms of Use (non-commercial, display-only).
- Marine Regions Exclusive Economic Zones v12 (Flanders Marine Institute (2024), DOI 10.14284/632). CC BY 4.0.
- **Model confidence:** Fishing probabilities are well-calibrated (Brier 0.0915 on 408,194 held-out positions from vessels not seen in training); read the score as a probability.
- **Integrity (SHA-256 of canonical facts):** `7b5fa1842a69b80c88f227b2612951c09cee42269c83f628a336a71edc5241f5`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
