# Incident `great_barrier_reef_marine_park__636020322_0000`

- **MPA:** Great Barrier Reef Marine Park
- **Severity:** LOW (multi-use protected area)  ·  boundary sample-approx-2024
- **EEZ:** Australia EEZ (Australia) -- FOREIGN-flagged vessel (licensing not verified)
- **Vessel:** 🇱🇷 KRITI WARRIOR  ·  **gear:** unknown
- **When (UTC):** 2026-06-29T04:04:43Z → 2026-06-29T04:04:43Z (0.0 h)
- **Apparent fishing:** 1 of 1 in-MPA positions; mean p=0.56, max p=0.56
- **Where:** -23.793, 151.184 (centroid)
- **Vs. speed baseline:** the trivial rule (speed < 10.7 kn) also flags 100% of these positions; here the speed rule alone suffices.

## Why this was flagged

_mean per-position SHAP (fishing class) over the incident's fishing positions._

| feature | mean value | mean SHAP |
|---|---:|---:|
| `distance_from_shore` | 6848.209 | +0.174 |
| `distance_from_port` | 8082.713 | -0.112 |
| `speed_roll_std` | 0.000 | -0.032 |
| `speed` | 0.000 | +0.031 |
| `hour_sin` | 0.875 | +0.014 |

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
- **Integrity (SHA-256 of canonical facts):** `8c026b695ffedfeee3f7f24b139f81e99f0687f0675fb77049d589b4caa76a3b`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
