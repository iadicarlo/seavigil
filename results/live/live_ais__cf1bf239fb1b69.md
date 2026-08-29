# Incident `live_ais__cf1bf239fb1b69`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Kiribati Exclusive Economic Zone (Gilbert Islands) (Kiribati) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇨🇳 JIN HUI NO.6  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-20T00:13:19.000Z → 2026-08-25T11:31:46.000Z
- **Gap:** 131.3 h dark, 116.0 nm offshore
- **Where:** -3.161, 176.042

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 116 nm offshore for 131 h
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
- **Integrity (SHA-256 of canonical facts):** `eb4e153cd832b3ebf9bbfa30654c77e542b3b9d11108dd3221ebd9db307f41eb`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
