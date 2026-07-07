# Incident `live_ais__fc236be87a968c`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Equatorial Guinean Exclusive Economic Zone (Equatorial Guinea) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: ICCAT, IOTC, WCPFC  ·  IMO 8912998
- **Vessel:** 🇫🇷 F/V GUERIDEN  ·  **signal:** AIS gap
- **When (UTC):** 2026-06-26T04:44:48.000Z → 2026-07-03T20:50:20.000Z
- **Gap:** 184.1 h dark, 62.0 nm offshore
- **Where:** -0.249, 5.246

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 62 nm offshore for 184 h
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
- **Integrity (SHA-256 of canonical facts):** `e9c8bcf2303d9304bc8f30fcc918ffbb60954cb7cf84ec21b52dd12593adbe99`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
