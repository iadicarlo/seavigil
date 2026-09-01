# Incident `live_ais__e4ff343f0be356`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Tuvaluan Exclusive Economic Zone (Tuvalu) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇨🇳 LUYUANYU136--02  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-17T20:46:54.000Z → 2026-08-28T20:45:23.000Z
- **Gap:** 264.0 h dark, 153.0 nm offshore
- **Where:** -7.343, 179.161

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 153 nm offshore for 264 h
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
- **Integrity (SHA-256 of canonical facts):** `365784e7a960d48a933ddadb1547dfb40f0c3b3e575f51a0bca7e6ad43761b76`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
