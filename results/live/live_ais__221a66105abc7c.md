# Incident `live_ais__221a66105abc7c`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Congolese (Democratic Republic of) Exclusive Economic Zone (Democratic Republic of the Congo) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇵🇦 UGO 3005  ·  **signal:** AIS gap
- **When (UTC):** 2026-09-14T05:43:23.000Z → 2026-09-14T21:54:08.000Z
- **Gap:** 16.2 h dark, 68.0 nm offshore
- **Where:** -6.353, 11.166

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 68 nm offshore for 16 h
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
- **Integrity (SHA-256 of canonical facts):** `a1e65f7bbd41dbf0012f29e5ba88a0a55a68df7e4ba4648411e1e89c7a7c15e0`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
