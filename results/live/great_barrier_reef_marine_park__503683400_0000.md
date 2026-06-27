# Incident `great_barrier_reef_marine_park__503683400_0000`

- **MPA:** Great Barrier Reef Marine Park
- **Severity:** LOW (multi-use protected area)  ·  boundary sample-approx-2024
- **EEZ:** Australia EEZ (Australia)  (flag matches coastal state)
- **Vessel:** 🇦🇺 RIVERSIDE CATALINA  ·  **gear:** unknown
- **When (UTC):** 2026-06-27T15:08:31Z → 2026-06-27T15:08:31Z (0.0 h)
- **Apparent fishing:** 1 of 1 in-MPA positions; mean p=0.54, max p=0.54
- **Where:** -16.922, 145.782 (centroid)
- **Vs. speed baseline:** the trivial rule (speed < 10.7 kn) also flags 100% of these positions; here the speed rule alone suffices.

## Why this was flagged

_mean per-position SHAP (fishing class) over the incident's fishing positions._

| feature | mean value | mean SHAP |
|---|---:|---:|
| `distance_from_shore` | 6592.573 | +0.166 |
| `distance_from_port` | 1144.006 | -0.122 |
| `speed` | 0.000 | +0.037 |
| `speed_roll_std` | 0.000 | -0.034 |
| `speed_roll_mean` | 0.000 | -0.009 |

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
- **Integrity (SHA-256 of canonical facts):** `32acb8e8704df8f44bbf1f688138c1c6834ffaec3df73c3b4e9b5de9394610da`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
