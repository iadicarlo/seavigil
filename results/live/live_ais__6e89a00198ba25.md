# Incident `live_ais__6e89a00198ba25`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Congolese (Democratic Republic of) Exclusive Economic Zone (Democratic Republic of the Congo) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)  ·  IMO 9727209
- **Vessel:** 🇭🇰 COSDIGNITY LAKE  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-23T17:13:02.000Z → 2026-08-24T10:37:02.000Z
- **Gap:** 17.4 h dark, 74.0 nm offshore
- **Where:** -6.299, 11.043

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 74 nm offshore for 17 h
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
- **Integrity (SHA-256 of canonical facts):** `0652867c73881e711cf2094770a57405c41a6fe899968d34e470c376ab4cbdbb`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
