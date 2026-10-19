# Incident `live_ais__07d3d405e25f0e`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Brazilian Exclusive Economic Zone (Brazil) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇸🇬 EAGLE CRATO  ·  **signal:** AIS gap
- **When (UTC):** 2026-10-13T22:32:10.000Z → 2026-10-15T02:50:52.000Z
- **Gap:** 28.3 h dark, 103.0 nm offshore
- **Where:** -24.692, -42.509

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 103 nm offshore for 28 h
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
- **Integrity (SHA-256 of canonical facts):** `d2e113106d96f94a583bc9431fbec0c47e1c4453579ce88dbfbee3fbaede1f67`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
