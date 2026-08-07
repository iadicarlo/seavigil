# Incident `live_ais__a4922dad265956`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Australian Exclusive Economic Zone (Australia) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇮🇸 ESBJORN 08-99%  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-02T01:08:37.000Z → 2026-08-03T14:53:59.000Z
- **Gap:** 37.8 h dark, 51.0 nm offshore
- **Where:** -35.690, 151.889

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 51 nm offshore for 38 h
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
- **Integrity (SHA-256 of canonical facts):** `7143bc2e81731cc646288ef5c09f4489293cc856d9d0e5133493d90f9c96a6d8`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
