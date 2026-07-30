# Incident `live_ais__194eb21694b78e`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Australian Exclusive Economic Zone (Australia) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇮🇪 GRACIEPLONGLINE6-99%  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-18T19:03:37.000Z → 2026-07-26T16:47:20.000Z
- **Gap:** 189.7 h dark, 74.0 nm offshore
- **Where:** -37.353, 150.669

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 74 nm offshore for 190 h
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
- **Integrity (SHA-256 of canonical facts):** `a23c5b6441f8f179be12c137f2a6f1888ff4649eb6f14e116c592b738d3eb2c0`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
