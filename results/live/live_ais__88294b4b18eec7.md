# Incident `live_ais__88294b4b18eec7`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Nigerian Exclusive Economic Zone (Nigeria) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)  ·  IMO 9150810
- **Vessel:** 🇱🇷 CARIBBEAN STAR  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-14T15:06:07.000Z → 2026-08-15T12:09:13.000Z
- **Gap:** 21.1 h dark, 202.0 nm offshore
- **Where:** 2.947, 5.587

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 202 nm offshore for 21 h
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
- **Integrity (SHA-256 of canonical facts):** `2e9639bb4a367a61f34d68efcdb3c0723f291392a752369ea3b4992dc567476b`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
