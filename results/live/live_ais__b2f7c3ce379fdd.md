# Incident `live_ais__b2f7c3ce379fdd`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Cape Verdean Exclusive Economic Zone (Cape Verde) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: ICCAT  ·  IMO 7409176
- **Vessel:** 🇸🇻 MONTEFRISA NUEVE  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-03T09:35:40.000Z → 2026-07-07T20:06:02.000Z
- **Gap:** 106.5 h dark, 57.0 nm offshore
- **Where:** 18.064, -20.683

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 57 nm offshore for 107 h
- satellite-confirmed AIS gap (GFW Events)

## Could be innocent

Going dark is frequently benign: in open water, where gaps are commonly protecting a fishing ground or waiting out weather. It is most actionable inside or beside a closed zone.

## Caveats

- IUU match is by name only; IUU vessels reuse names, so confirm the identity.
- AIS gaps can be reception loss, not always intentional disabling.
- The position is where AIS dropped; the path while dark is unknown.
- An inspection lead from GFW Events, not proof of illegal activity.

## Provenance & integrity

- NOAA Marine Cadastre AIS (marinecadastre.gov/ais (vessel positions)). US public domain.
- WDPA / WD-OECM (World Database on Protected Areas) (UNEP-WCMC and IUCN (2026), June 2026). Protected Planet Terms of Use (non-commercial, display-only).
- Marine Regions Exclusive Economic Zones v12 (Flanders Marine Institute (2024), DOI 10.14284/632). CC BY 4.0.
- **Integrity (SHA-256 of canonical facts):** `def18411bfe88730a85391a74063ae17b5f2a17fab7d91c5ed518a3054134389`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
