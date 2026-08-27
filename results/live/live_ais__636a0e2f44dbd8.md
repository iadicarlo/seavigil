# Incident `live_ais__636a0e2f44dbd8`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Sierra Leonean Exclusive Economic Zone (Sierra Leone) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)  ·  IMO 9837688
- **Vessel:** 🇬🇳 KANKAN  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-22T05:49:55.000Z → 2026-08-23T02:21:35.000Z
- **Gap:** 20.5 h dark, 51.0 nm offshore
- **Where:** 8.605, -14.001

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 51 nm offshore for 21 h
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
- **Integrity (SHA-256 of canonical facts):** `13b3d8f08f7b4eeb9847d07c744a62926e11c9d01545d4dafc7e6bf122730d1d`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
