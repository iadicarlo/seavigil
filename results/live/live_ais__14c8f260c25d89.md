# Incident `live_ais__14c8f260c25d89`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Cape Verdean Exclusive Economic Zone (Cape Verde) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: CCSBT, ICCAT  ·  IMO 8649802
- **Vessel:** 🇹🇼 YEUN HORNG NO.2  ·  **signal:** AIS gap
- **When (UTC):** 2026-10-21T09:56:54.000Z → 2026-10-21T22:50:21.000Z
- **Gap:** 12.9 h dark, 91.0 nm offshore
- **Where:** 17.736, -24.811

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 91 nm offshore for 13 h
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
- **Integrity (SHA-256 of canonical facts):** `6aa2cb764f0c606190ed8dc692901b9526f729f746475200a4763a6389a227d4`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
