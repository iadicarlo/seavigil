# Incident `great_barrier_reef_marine_park__503756000_0000`

- **MPA:** Great Barrier Reef Marine Park
- **Severity:** LOW (multi-use protected area)  ·  boundary sample-approx-2024
- **Vessel:** 🇦🇺 REEF ADVENTURE  ·  **gear:** unknown
- **When (UTC):** 2026-06-26T06:42:46Z → 2026-06-26T06:43:47Z (0.017 h)
- **Apparent fishing:** 2 of 2 in-MPA positions; mean p=0.56, max p=0.56
- **Where:** -16.922, 145.781 (centroid)
- **Track:** 2 positions, (-16.922, 145.781) → (-16.922, 145.781)
- **Vs. speed baseline:** the trivial rule (speed < 10.7 kn) also flags 100% of these positions; here the speed rule alone suffices.

## Why this was flagged

_mean per-position SHAP (fishing class) over the incident's fishing positions._

| feature | mean value | mean SHAP |
|---|---:|---:|
| `distance_from_shore` | 6628.914 | +0.167 |
| `distance_from_port` | 1094.265 | -0.113 |
| `speed` | 0.000 | +0.030 |
| `speed_roll_std` | 0.000 | -0.022 |
| `hour_sin` | 0.983 | +0.012 |

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
- **Integrity (SHA-256 of canonical facts):** `35b3eaff3641c9f30a8a5c1c63f39cc60669b9b11770ef84fdce918ada5e60c0`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
