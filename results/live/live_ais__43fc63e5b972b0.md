# Incident `live_ais__43fc63e5b972b0`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Yemeni Exclusive Economic Zone (Yemen) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)  ·  IMO 9597018
- **Vessel:** 🇱🇷 AGISTRI  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-21T01:00:38.000Z → 2026-08-23T18:05:38.000Z
- **Gap:** 65.1 h dark, 54.0 nm offshore
- **Where:** 16.095, 42.303

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 54 nm offshore for 65 h
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
- **Integrity (SHA-256 of canonical facts):** `bef97d7b4e909aee01a9ed62545b1295663b9c399cd2a90290bcf578195d3c82`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
