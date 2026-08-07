# Incident `live_ais__9ce5eaff6ab18c`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Equatorial Guinean Exclusive Economic Zone (Equatorial Guinea) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: ICCAT  ·  IMO 9808120
- **Vessel:** 🇨🇼 ARTIKE  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-01T05:20:31.000Z → 2026-08-03T05:58:20.000Z
- **Gap:** 48.6 h dark, 200.0 nm offshore
- **Where:** 0.460, 4.043

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 200 nm offshore for 49 h
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
- **Integrity (SHA-256 of canonical facts):** `1688d3d43a8e595735612427efe65ea859763f5ddfaeb2e516d8a93a3a783396`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
