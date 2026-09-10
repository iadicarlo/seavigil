# Incident `live_ais__4033b3d1938ed2`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Madagascan Exclusive Economic Zone (Madagascar) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)  ·  IMO 9103130
- **Vessel:** 🇳🇴 STAR HARMONIA  ·  **signal:** AIS gap
- **When (UTC):** 2026-09-04T04:17:31.000Z → 2026-09-04T17:53:36.000Z
- **Gap:** 13.6 h dark, 83.0 nm offshore
- **Where:** -25.087, 49.505

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 83 nm offshore for 14 h
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
- **Integrity (SHA-256 of canonical facts):** `876473aa81515fe143be227305ef8565e06d6cc8cf3ab81763b1ca15fdfe6888`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
