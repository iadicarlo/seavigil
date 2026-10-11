# Incident `live_ais__ef8f8c8c39a1f8`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** French Exclusive Economic Zone (Réunion) (France) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)  ·  IMO 9606314
- **Vessel:** 🇵🇦 MSC NEW YORK  ·  **signal:** AIS gap
- **When (UTC):** 2026-10-05T09:08:49.000Z → 2026-10-07T02:38:02.000Z
- **Gap:** 41.5 h dark, 107.0 nm offshore
- **Where:** -19.468, 54.074

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 107 nm offshore for 41 h
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
- **Integrity (SHA-256 of canonical facts):** `9f4f412cddd1e877a2dbda8475fd4dbc30612c43a55f27bd7c4aef59e90c0317`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
