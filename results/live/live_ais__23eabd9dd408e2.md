# Incident `live_ais__23eabd9dd408e2`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Angolan Exclusive Economic Zone (Angola) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)  ·  IMO 9734654
- **Vessel:** 🇲🇭 SEAWAYS TRITON  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-16T19:32:08.000Z → 2026-08-17T19:03:48.000Z
- **Gap:** 23.5 h dark, 69.0 nm offshore
- **Where:** -7.673, 11.781

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 69 nm offshore for 24 h
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
- **Integrity (SHA-256 of canonical facts):** `d83cfab6897a20254695d77994327297cc0708e6bcfd70e98e20f667fa80cff7`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
