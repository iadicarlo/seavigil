# Incident `live_ais__04187f047de1e4`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** São Toméan Exclusive Economic Zone (Sao Tome and Principe) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇩🇰 CAROLINE THERESA  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-18T08:18:53.000Z → 2026-07-19T11:02:05.000Z
- **Gap:** 26.7 h dark, 99.0 nm offshore
- **Where:** 0.554, 6.851

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 99 nm offshore for 27 h
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
- **Integrity (SHA-256 of canonical facts):** `af2b1f635c3b179457e684387ecbacca0978da1c399085f9f4c1fdb8179cd6a2`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
