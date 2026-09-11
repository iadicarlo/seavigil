# Incident `live_ais__1cdeb41b617e02`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Brazilian Exclusive Economic Zone (Brazil) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇸🇬 EAGLE CRATO  ·  **signal:** AIS gap
- **When (UTC):** 2026-09-06T03:44:54.000Z → 2026-09-07T04:47:35.000Z
- **Gap:** 25.0 h dark, 106.0 nm offshore
- **Where:** -24.739, -42.514

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 106 nm offshore for 25 h
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
- **Integrity (SHA-256 of canonical facts):** `41e8cd4a2061c9f4e95212f155e31d8967c980da23d95d661022da3677a4c50f`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
