# Incident `live_ais__dd19ae476e351d`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Saudi Arabian Exclusive Economic Zone (Saudi Arabia) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)  ·  IMO 7504158
- **Vessel:** 🇹🇬 TRUST 1  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-30T00:08:25.000Z → 2026-09-01T10:19:45.000Z
- **Gap:** 58.2 h dark, 50.0 nm offshore
- **Where:** 19.538, 39.618

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 50 nm offshore for 58 h
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
- **Integrity (SHA-256 of canonical facts):** `0b12ae97f8414e0b29be5e133ec4aeff6616fcb6a86fcedccee573ccbb79e02e`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
