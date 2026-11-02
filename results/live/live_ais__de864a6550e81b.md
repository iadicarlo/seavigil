# Incident `live_ais__de864a6550e81b`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Sudanese Exclusive Economic Zone (Sudan) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)  ·  IMO 7393169
- **Vessel:** 🇵🇦 H ORCA  ·  **signal:** AIS gap
- **When (UTC):** 2026-10-24T16:41:01.000Z → 2026-10-29T01:32:20.000Z
- **Gap:** 104.9 h dark, 57.0 nm offshore
- **Where:** 20.138, 37.856

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 57 nm offshore for 105 h
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
- **Integrity (SHA-256 of canonical facts):** `497bec854f7276836d4328e310010000c8e43dab799ae1be4efe7ea633df6dbd`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
