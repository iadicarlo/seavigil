# Incident `live_ais__5cde9c497a427b`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Solomon Islands Exclusive Economic Zone (Solomon Islands) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇹🇼 YI SIANG NO.6  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-14T07:06:29.000Z → 2026-08-15T22:41:32.000Z
- **Gap:** 39.6 h dark, 76.0 nm offshore
- **Where:** -9.242, 163.454

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 76 nm offshore for 40 h
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
- **Integrity (SHA-256 of canonical facts):** `6c8e968809f2940e3a04b375de46870a84fb3ade077f9f2a8e839abdba6b611d`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
