# Incident `live_ais__a17696f218fed5`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Cape Verdean Exclusive Economic Zone (Cape Verde) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: ICCAT, IOTC  ·  IMO 9747560
- **Vessel:** 🇪🇸 GARBOLA  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-19T04:12:03.000Z → 2026-08-25T22:55:24.000Z
- **Gap:** 162.7 h dark, 307.0 nm offshore
- **Where:** 12.947, -22.283

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 307 nm offshore for 163 h
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
- **Integrity (SHA-256 of canonical facts):** `c3a9b18deb47cab9c4fd86a392f24bda6447214a5aa6061707dd04cb7bb26665`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
