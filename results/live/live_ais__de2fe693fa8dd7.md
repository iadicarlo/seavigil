# Incident `live_ais__de2fe693fa8dd7`

- **MPA:** AIS disabling (going dark)
- **Severity:** MEDIUM (foreign vessel, authorization unverified)
- **EEZ:** New Zealand Exclusive Economic Zone (Tokelau) (New Zealand) -- FOREIGN-flagged vessel
- **Authorization:** No vessel identity; authorization not checkable
- **Vessel:** 🇮🇷 BUOY 245-986    12V6  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-25T18:34:21.000Z → 2026-07-27T18:33:54.000Z
- **Gap:** 48.0 h dark, 211.0 nm offshore
- **Where:** -7.265, -172.870

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 211 nm offshore for 48 h
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
- **Integrity (SHA-256 of canonical facts):** `5d3178122bbfa8fcaae1f8814e58a287a4cb2820710e977b40597a57697a1e36`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
