# Incident `live_ais__bc164cde1e1166`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Seychellois Exclusive Economic Zone (Seychelles) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇹🇼 SHIN SHUEN  FAR 668  ·  **signal:** AIS gap
- **When (UTC):** 2026-10-04T18:23:14.000Z → 2026-10-11T06:20:21.000Z
- **Gap:** 156.0 h dark, 196.0 nm offshore
- **Where:** -7.525, 58.691

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 196 nm offshore for 156 h
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
- **Integrity (SHA-256 of canonical facts):** `c6b215fd226747aeabf34fb79f8baa57458e457489630c0a9cdfd8b980e0f1de`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
