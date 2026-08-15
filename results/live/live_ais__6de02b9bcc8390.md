# Incident `live_ais__6de02b9bcc8390`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Angolan Exclusive Economic Zone (Angola) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)  ·  IMO 9708502
- **Vessel:** 🇭🇰 NEW VICTORY  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-09T15:17:59.000Z → 2026-08-11T13:41:41.000Z
- **Gap:** 46.4 h dark, 82.0 nm offshore
- **Where:** -6.130, 10.854

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 82 nm offshore for 46 h
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
- **Integrity (SHA-256 of canonical facts):** `4c452f31ceb8de4eeb94b1fbafd87e99249ef686661dea184221c85a75bab094`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
