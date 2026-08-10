# Incident `live_ais__1a706b10b99c0b`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Equatorial Guinean Exclusive Economic Zone (Equatorial Guinea) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇹🇻 BRITOIL DILIGENCE  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-01T18:55:38.000Z → 2026-08-06T21:00:40.000Z
- **Gap:** 122.1 h dark, 116.0 nm offshore
- **Where:** -1.266, 3.610

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 116 nm offshore for 122 h
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
- **Integrity (SHA-256 of canonical facts):** `d9204d81b2e0cfeefd2cf9bd9006eb5f251069c2627f513e3363e29dcddbc086`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
