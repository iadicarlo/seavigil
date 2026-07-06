# Incident `live_ais__e4d1fa66ea5a04`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Costa Rican Exclusive Economic Zone (Costa Rica) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇲🇹 TRUST STAR  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-02T04:40:06.000Z → 2026-07-02T21:01:01.000Z
- **Gap:** 16.3 h dark, 68.0 nm offshore
- **Where:** 11.078, -80.166

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
- **Integrity (SHA-256 of canonical facts):** `7719aa2b93beadf28fd7b13b6823214178547b70e13fd8e3ce1f6ee628ae4194`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
