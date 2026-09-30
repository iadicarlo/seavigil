# Incident `live_ais__72ef1d0466d3dd`

- **MPA:** AIS disabling (going dark)
- **Severity:** MEDIUM (foreign vessel, authorization unverified)
- **EEZ:** Kiribati Exclusive Economic Zone (Line Group) (Kiribati) -- FOREIGN-flagged vessel
- **Authorization:** No vessel identity; authorization not checkable
- **Vessel:** 🇦🇴 AB6-3-79%  ·  **signal:** AIS gap
- **When (UTC):** 2026-09-25T01:42:02.000Z → 2026-09-26T13:48:03.000Z
- **Gap:** 36.1 h dark, 135.0 nm offshore
- **Where:** -6.965, -152.672

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 135 nm offshore for 36 h
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
- **Integrity (SHA-256 of canonical facts):** `4bef2c595dd14e86e3c0bf8f62d1be755564c01873dd3ea1ab6f4809968b3c9d`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
