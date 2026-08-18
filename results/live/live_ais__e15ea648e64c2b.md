# Incident `live_ais__e15ea648e64c2b`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Overlapping claim Western Sahara: Western Sahara / Morocco (Western Sahara) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇲🇦 FILAKA-5  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-12T09:13:46.000Z → 2026-08-14T14:30:06.000Z
- **Gap:** 53.3 h dark, 51.0 nm offshore
- **Where:** 24.875, -16.079

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 51 nm offshore for 53 h
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
- **Integrity (SHA-256 of canonical facts):** `b6059bd2a6db80dde2f1dbc7c1d44de80bc9c0ff49630ac6f1c2445fc214c79a`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
