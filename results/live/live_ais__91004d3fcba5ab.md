# Incident `live_ais__91004d3fcba5ab`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Overlapping claim Western Sahara: Western Sahara / Morocco (Western Sahara) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)  ·  IMO 9795127
- **Vessel:** 🇸🇬 EAGLE SAN FRANCISCO  ·  **signal:** AIS gap
- **When (UTC):** 2026-06-28T19:55:31.000Z → 2026-06-29T15:46:35.000Z
- **Gap:** 19.9 h dark, 84.0 nm offshore
- **Where:** 25.017, -16.385

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 84 nm offshore for 20 h
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
- **Integrity (SHA-256 of canonical facts):** `c69fadf2d742daf1c12f048ceb80d230a8c07fc88836903302054a5353b1e81d`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
