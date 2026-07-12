# Incident `live_ais__f25d69f7899cf9`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Kiribati Exclusive Economic Zone (Gilbert Islands) (Kiribati) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇵🇦 YU27-8-91%  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-05T12:47:26.000Z → 2026-07-07T20:53:50.000Z
- **Gap:** 56.1 h dark, 173.0 nm offshore
- **Where:** -3.779, 172.683

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 173 nm offshore for 56 h
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
- **Integrity (SHA-256 of canonical facts):** `0018e8df8fa83ff3d67aae55f163c4dbc71cb0898b2174075bf08049abff96e6`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
