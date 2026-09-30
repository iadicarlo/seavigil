# Incident `live_ais__30685fc3ec6703`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Solomon Islands Exclusive Economic Zone (Solomon Islands) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇹🇼 JIN JINN YI NO.168  ·  **signal:** AIS gap
- **When (UTC):** 2026-09-25T04:41:32.000Z → 2026-09-26T06:48:44.000Z
- **Gap:** 26.1 h dark, 126.0 nm offshore
- **Where:** -12.816, 162.856

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 126 nm offshore for 26 h
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
- **Integrity (SHA-256 of canonical facts):** `0f2a151e07fd1ae4a1642ac63117004523eb1c8553f5c9789b819a058d263ed4`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
