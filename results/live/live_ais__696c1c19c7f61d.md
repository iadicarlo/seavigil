# Incident `live_ais__696c1c19c7f61d`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Yemeni Exclusive Economic Zone (Yemen) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇻🇺 OCEAN DARIA  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-05T10:51:48.000Z → 2026-08-06T06:55:13.000Z
- **Gap:** 20.1 h dark, 80.0 nm offshore
- **Where:** 13.059, 51.775

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 80 nm offshore for 20 h
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
- **Integrity (SHA-256 of canonical facts):** `c5a9ce0e420c711fa81ad12b60fd12ddbb6b2d7c64fcd293d83d021b5c4426e5`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
