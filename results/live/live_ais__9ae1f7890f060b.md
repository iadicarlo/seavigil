# Incident `live_ais__9ae1f7890f060b`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** South African Exclusive Economic Zone (South Africa) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)  ·  IMO 9246396
- **Vessel:** 🇬🇧 COSCO ANTWERP  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-01T05:23:04.000Z → 2026-08-02T00:33:53.000Z
- **Gap:** 19.2 h dark, 160.0 nm offshore
- **Where:** -31.873, 14.700

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 160 nm offshore for 19 h
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
- **Integrity (SHA-256 of canonical facts):** `69e16e688581f489e9545d0199f3a46cf47d9b4590de3a389943a141eb92ebfa`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
