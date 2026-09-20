# Incident `live_ais__b2e7c350640ee7`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Congolese (Democratic Republic of) Exclusive Economic Zone (Democratic Republic of the Congo) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇳🇬 MV MOUNFIQ  ·  **signal:** AIS gap
- **When (UTC):** 2026-09-16T04:09:13.000Z → 2026-09-16T18:27:45.000Z
- **Gap:** 14.3 h dark, 66.0 nm offshore
- **Where:** -6.234, 11.174

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 66 nm offshore for 14 h
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
- **Integrity (SHA-256 of canonical facts):** `78c97b2fd70f199300c6f306731efcbcffdfdc208d18de1d3782b2567f19fe78`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
