# Incident `live_ais__a549b5dfe68491`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Namibian Exclusive Economic Zone (Namibia) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)  ·  IMO 9469546
- **Vessel:** 🇱🇷 NEW ASSIMINA  ·  **signal:** AIS gap
- **When (UTC):** 2026-10-07T12:00:46.000Z → 2026-10-22T22:04:28.000Z
- **Gap:** 370.1 h dark, 409.0 nm offshore
- **Where:** -18.277, 10.045

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 409 nm offshore for 370 h
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
- **Integrity (SHA-256 of canonical facts):** `8bfa7ce6b66196c9f6798153fea4773ad3a1c2b79b936e8395bd1be3e6e9dc13`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
