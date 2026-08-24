# Incident `live_ais__f9207926e35c0e`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Egyptian Exclusive Economic Zone (Egypt) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)  ·  IMO 9407354
- **Vessel:** 🇱🇷 HORIZON ARMONIA  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-17T18:51:00.000Z → 2026-08-20T11:31:20.000Z
- **Gap:** 64.7 h dark, 53.0 nm offshore
- **Where:** 24.020, 36.302

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 53 nm offshore for 65 h
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
- **Integrity (SHA-256 of canonical facts):** `c5252ea16c62235027e8628792842512e14b908128b3c4bb615fd89208f452b6`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
