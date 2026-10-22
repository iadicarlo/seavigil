# Incident `live_ais__0c4bdf5cc91c8d`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Japanese Exclusive Economic Zone (Japan) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: NPFC, SPRFMO  ·  IMO 9741853
- **Vessel:** 🇹🇼 WIN FAR HUI 6  ·  **signal:** AIS gap
- **When (UTC):** 2026-10-18T05:19:21.000Z → 2026-10-18T20:29:07.000Z
- **Gap:** 15.2 h dark, 255.0 nm offshore
- **Where:** 33.496, 138.495

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 255 nm offshore for 15 h
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
- **Integrity (SHA-256 of canonical facts):** `367a098b15e4797258e7364ed9df0e6aff9da4f11167aca8994bb029b3c843b2`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
