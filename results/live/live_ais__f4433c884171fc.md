# Incident `live_ais__f4433c884171fc`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Namibian Exclusive Economic Zone (Namibia) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)  ·  IMO 9463669
- **Vessel:** 🇱🇷 REDMER OLDENDORFF  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-02T07:29:29.000Z → 2026-08-03T09:07:56.000Z
- **Gap:** 25.6 h dark, 136.0 nm offshore
- **Where:** -27.180, 13.036

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 136 nm offshore for 26 h
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
- **Integrity (SHA-256 of canonical facts):** `b65d5b165de79b3587a624555b6de577f40b1c1f0946ad2a59f0c48c453de54b`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
