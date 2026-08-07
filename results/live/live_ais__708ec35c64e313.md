# Incident `live_ais__708ec35c64e313`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Namibian Exclusive Economic Zone (Namibia) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇭🇰 COSCO UNIVERSE  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-02T16:57:01.000Z → 2026-08-03T07:32:55.000Z
- **Gap:** 14.6 h dark, 214.0 nm offshore
- **Where:** -29.617, 13.838

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 214 nm offshore for 15 h
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
- **Integrity (SHA-256 of canonical facts):** `97104ea6ae708fbc10dbbb8d8ed042dd48d9c6ba6d0f6e16ef5f076c1c4c972f`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
