# Incident `live_ais__2f21b480bfa6f7`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Fijian Exclusive Economic Zone (Fiji) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇱🇮 HSD11602-86%  ·  **signal:** AIS gap
- **When (UTC):** 2026-10-18T06:58:28.000Z → 2026-10-19T00:28:55.000Z
- **Gap:** 17.5 h dark, 80.0 nm offshore
- **Where:** -17.761, 175.734

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 80 nm offshore for 18 h
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
- **Integrity (SHA-256 of canonical facts):** `683b04d5b99d315f8bf336c0edfd5b3afe99a0ff3c02715065a34701fe8a8a4f`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
