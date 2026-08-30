# Incident `live_ais__8a01f91c22a1f5`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** New Zealand Exclusive Economic Zone (Niue) (New Zealand) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇨🇰 MISS SILVER  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-24T09:52:11.000Z → 2026-08-26T18:30:26.000Z
- **Gap:** 56.6 h dark, 206.0 nm offshore
- **Where:** -18.695, -168.578

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 206 nm offshore for 57 h
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
- **Integrity (SHA-256 of canonical facts):** `20eae59efa3d59f35f556eb0d2dfb31ca9787b42cf98fd0ef85acbac615df2fd`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
