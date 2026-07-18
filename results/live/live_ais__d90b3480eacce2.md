# Incident `live_ais__d90b3480eacce2`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Cape Verdean Exclusive Economic Zone (Cape Verde) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: CCSBT, FFA, GFCM, IATTC, ICCAT, IOTC, WCPFC  ·  IMO 9311921
- **Vessel:** 🇯🇵 KINEI MARU NO.135  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-10T16:55:06.000Z → 2026-07-14T10:46:45.000Z
- **Gap:** 89.9 h dark, 296.0 nm offshore
- **Where:** 12.069, -25.325

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 296 nm offshore for 90 h
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
- **Integrity (SHA-256 of canonical facts):** `6e8b64a4a5a3d40a605132ef1d462adf577ee5c3534e7d4994ee3d0116238c63`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
