# Incident `live_ais__357a9f04f349b7`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** New Zealand Exclusive Economic Zone (New Zealand) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇮🇪 250400394  ·  **signal:** AIS gap
- **When (UTC):** 2026-10-03T14:37:44.000Z → 2026-10-05T16:40:07.000Z
- **Gap:** 50.0 h dark, 185.0 nm offshore
- **Where:** -49.295, 171.783

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 185 nm offshore for 50 h
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
- **Integrity (SHA-256 of canonical facts):** `5b7a3a97f2ccb1be40f2cebb905fa5caf5655a3bf4e1066a9c2ecd14d9dfd84c`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
