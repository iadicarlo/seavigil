# Incident `live_ais__a9ad3bcb8a75ed`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Senegalese Exclusive Economic Zone (Senegal) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)  ·  IMO 9303730
- **Vessel:** 🇲🇹 SEAEAGLE II  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-27T14:34:18.000Z → 2026-08-05T09:31:20.000Z
- **Gap:** 211.0 h dark, 136.0 nm offshore
- **Where:** 16.051, -19.475

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 136 nm offshore for 211 h
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
- **Integrity (SHA-256 of canonical facts):** `1dd77077cd8ff21f43de77a204527c1d82edc4c784bb1e00f3051c82ce5b20cd`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
