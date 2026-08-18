# Incident `live_ais__55f86f52f4e9ad`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Equatorial Guinean Exclusive Economic Zone (Equatorial Guinea) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇱🇷 ADRE  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-12T04:03:35.000Z → 2026-08-14T04:41:35.000Z
- **Gap:** 48.6 h dark, 293.0 nm offshore
- **Where:** -2.394, 4.604

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 293 nm offshore for 49 h
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
- **Integrity (SHA-256 of canonical facts):** `11c0b35913b29fc2adccfe6f5d0bc5720cf783eb2d78849ca1ce09e888f138a7`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
