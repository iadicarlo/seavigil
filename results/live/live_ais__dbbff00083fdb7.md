# Incident `live_ais__dbbff00083fdb7`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Nigerian Exclusive Economic Zone (Nigeria) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)  ·  IMO 9127344
- **Vessel:** 🇬🇧 SVITZER MELTON  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-30T06:45:09.000Z → 2026-07-30T18:51:07.000Z
- **Gap:** 12.1 h dark, 113.0 nm offshore
- **Where:** 4.498, 3.073

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 113 nm offshore for 12 h
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
- **Integrity (SHA-256 of canonical facts):** `c7d18ec6e56d98703361d3e646f25ee81c0416f4cd82b93a15e5158ab6c1bc6d`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
