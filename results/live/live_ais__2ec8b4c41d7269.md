# Incident `live_ais__2ec8b4c41d7269`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** New Zealand Exclusive Economic Zone (Cook Islands) (New Zealand) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇺🇸 DEAD RECKONING  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-31T16:07:58.000Z → 2026-08-04T08:44:04.000Z
- **Gap:** 88.6 h dark, 97.0 nm offshore
- **Where:** -17.766, -161.115

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 97 nm offshore for 89 h
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
- **Integrity (SHA-256 of canonical facts):** `1dd821d6b58d0982ece44e27edff48be5f30f681518156d0bc4022f3c36db89d`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
