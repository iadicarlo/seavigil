# Incident `live_ais__80bb955b22bf90`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Fijian Exclusive Economic Zone (Fiji) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇬🇧 HSD11101-99%  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-30T07:33:06.000Z → 2026-08-03T06:26:46.000Z
- **Gap:** 94.9 h dark, 157.0 nm offshore
- **Where:** -17.806, 176.069

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 157 nm offshore for 95 h
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
- **Integrity (SHA-256 of canonical facts):** `a145b22594c1ed4995e413cb0d8f1083f1ca8a31104190bfc7e6a8e2d892ba8a`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
