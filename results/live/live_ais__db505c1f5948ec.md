# Incident `live_ais__db505c1f5948ec`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Australian Exclusive Economic Zone (Christmas Island) (Australia) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇬🇧 LUSH  ·  **signal:** AIS gap
- **When (UTC):** 2026-10-14T15:16:47.000Z → 2026-10-15T11:21:56.000Z
- **Gap:** 20.1 h dark, 79.0 nm offshore
- **Where:** -9.224, 103.362

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 79 nm offshore for 20 h
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
- **Integrity (SHA-256 of canonical facts):** `470dd1df45fd1477218aa5fc7b075f1ea0fde78b66f271b9bab0cc1e05398a43`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
