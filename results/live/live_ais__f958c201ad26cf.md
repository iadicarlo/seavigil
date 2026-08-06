# Incident `live_ais__f958c201ad26cf`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** United States Exclusive Economic Zone (Alaska) (United States) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇸🇬 EVER SUMMIT  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-02T05:32:08.000Z → 2026-08-02T18:05:55.000Z
- **Gap:** 12.6 h dark, 110.0 nm offshore
- **Where:** 54.020, -155.008

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 110 nm offshore for 13 h
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
- **Integrity (SHA-256 of canonical facts):** `ac4ee18cfb35de032471f5ed43556c13b19691c7125288812b57aeecca3b6ee4`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
