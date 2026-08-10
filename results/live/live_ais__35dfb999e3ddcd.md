# Incident `live_ais__35dfb999e3ddcd`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Fijian Exclusive Economic Zone (Fiji) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇭🇺 SEIN 11 #8-94%  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-05T16:02:51.000Z → 2026-08-06T20:44:09.000Z
- **Gap:** 28.7 h dark, 93.0 nm offshore
- **Where:** -20.613, 179.448

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 93 nm offshore for 29 h
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
- **Integrity (SHA-256 of canonical facts):** `b26f9b30a6250219c0e831dcb181fc463187b3aee804a894b364893d8f4d7dd7`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
