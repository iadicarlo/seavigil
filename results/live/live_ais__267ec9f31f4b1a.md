# Incident `live_ais__267ec9f31f4b1a`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Congolese (Democratic Republic of) Exclusive Economic Zone (Democratic Republic of the Congo) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)  ·  IMO 9425801
- **Vessel:** 🇵🇦 UGO 3005  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-02T11:32:00.000Z → 2026-07-06T06:54:21.000Z
- **Gap:** 91.4 h dark, 70.0 nm offshore
- **Where:** -6.344, 11.103

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 70 nm offshore for 91 h
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
- **Integrity (SHA-256 of canonical facts):** `a9a67cefce6a40169123496ac280bbc7a270f61f8e9707520bf1b02f54f309d8`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
