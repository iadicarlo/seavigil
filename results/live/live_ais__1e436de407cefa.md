# Incident `live_ais__1e436de407cefa`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** United States Exclusive Economic Zone (Palmyra Atoll) (United States) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇿🇦 IMVUBU  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-16T16:08:21.000Z → 2026-07-17T06:32:40.000Z
- **Gap:** 14.4 h dark, 63.0 nm offshore
- **Where:** 5.020, -162.762

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 63 nm offshore for 14 h
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
- **Integrity (SHA-256 of canonical facts):** `1c1c39e9922c35a3061a9c4896f13274de1c05b83821dc7658f691a9f94ef850`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
