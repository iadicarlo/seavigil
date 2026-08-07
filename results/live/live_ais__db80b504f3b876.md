# Incident `live_ais__db80b504f3b876`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Congolese (Democratic Republic of) Exclusive Economic Zone (Democratic Republic of the Congo) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇵🇦 SURFER 19004  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-31T21:30:10.000Z → 2026-08-03T00:30:55.000Z
- **Gap:** 51.0 h dark, 58.0 nm offshore
- **Where:** -6.223, 11.267

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 58 nm offshore for 51 h
- satellite-confirmed AIS gap (GFW Events)

## Could be innocent

Going dark is frequently benign: in open water, where gaps are commonly protecting a fishing ground or waiting out weather. It is most actionable inside or beside a closed zone.

## Caveats

- AIS gaps can be reception loss, not always intentional disabling.
- The position is where AIS dropped; the path while dark is unknown.
- An inspection lead from GFW Events, not proof of illegal activity.

## Provenance & integrity

- NOAA Marine Cadastre AIS (marinecadastre.gov/ais (vessel positions)). US public domain.
- WDPA / WD-OECM (World Database on Protected Areas) (UNEP-WCMC and IUCN (2026), June 2026). Protected Planet Terms of Use (non-commercial, display-only).
- Marine Regions Exclusive Economic Zones v12 (Flanders Marine Institute (2024), DOI 10.14284/632). CC BY 4.0.
- **Integrity (SHA-256 of canonical facts):** `fea212ddbdd4900af83b5006691e1637f9b5701568428f4c043a2c0f8bc1c277`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
