# Incident `live_ais__ff04305dbb85c3`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Sierra Leonean Exclusive Economic Zone (Sierra Leone) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇧🇸 NESTOR RAY  ·  **signal:** AIS gap
- **When (UTC):** 2026-10-04T17:35:04.000Z → 2026-10-05T08:27:49.000Z
- **Gap:** 14.9 h dark, 147.0 nm offshore
- **Where:** 6.300, -15.109

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 147 nm offshore for 15 h
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
- **Integrity (SHA-256 of canonical facts):** `682f7621a5ac9ba2ffdaa9470596cec287c3b6a2a18fd6c4040988062c2972aa`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
