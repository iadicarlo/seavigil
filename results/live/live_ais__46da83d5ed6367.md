# Incident `live_ais__46da83d5ed6367`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Somali Exclusive Economic Zone (Federal Republic of Somalia) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇮🇳 M.S.V NOORE AL AMINA  ·  **signal:** AIS gap
- **When (UTC):** 2026-09-13T13:15:24.000Z → 2026-09-18T10:36:42.000Z
- **Gap:** 117.4 h dark, 80.0 nm offshore
- **Where:** 12.321, 48.597

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 80 nm offshore for 117 h
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
- **Integrity (SHA-256 of canonical facts):** `5dffe48f4cef0da223620822483712dc59225840c2aef128b936baf2f4c9c584`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
