# Incident `live_ais__b3765e5e93b8dc`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Senegalese Exclusive Economic Zone (Senegal) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇵🇹 BENJAMIN CONFIDENCE  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-03T11:27:22.000Z → 2026-08-04T16:47:01.000Z
- **Gap:** 29.3 h dark, 124.0 nm offshore
- **Where:** 12.425, -19.095

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 124 nm offshore for 29 h
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
- **Integrity (SHA-256 of canonical facts):** `4f76bc4f0e4b1299a9f23bc8f08739f82e1f1cacc55a1adba3599224f8f246a3`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
