# Incident `live_ais__4488f46d978fdc`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** South African Exclusive Economic Zone (South Africa) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇨🇾 ARISTOTELES GRAECIA  ·  **signal:** AIS gap
- **When (UTC):** 2026-10-12T16:02:21.000Z → 2026-10-13T08:47:46.000Z
- **Gap:** 16.8 h dark, 155.0 nm offshore
- **Where:** -35.173, 17.218

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 155 nm offshore for 17 h
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
- **Integrity (SHA-256 of canonical facts):** `4cc8ccd7dcfefd84df40fd073e97de88cbb11ca88c1d50e7c45c41f06f3d2633`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
