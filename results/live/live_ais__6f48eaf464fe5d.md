# Incident `live_ais__6f48eaf464fe5d`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Somali Exclusive Economic Zone (Federal Republic of Somalia) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇮🇷 ALKHAYYAM  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-01T15:07:11.000Z → 2026-07-08T20:09:18.000Z
- **Gap:** 173.0 h dark, 299.0 nm offshore
- **Where:** 6.275, 51.498

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 299 nm offshore for 173 h
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
- **Integrity (SHA-256 of canonical facts):** `c60d073f7f8b051d971cf85a852dd6af9998d3c3a6006be449bd5d9826f1e958`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
