# Incident `live_ais__2e64bfde41132e`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Seychellois Exclusive Economic Zone (Seychelles) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)  ·  IMO 9320403
- **Vessel:** 🇵🇦 MSC LORENA  ·  **signal:** AIS gap
- **When (UTC):** 2026-10-07T04:19:14.000Z → 2026-10-10T19:54:09.000Z
- **Gap:** 87.6 h dark, 179.0 nm offshore
- **Where:** -1.271, 56.389

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 179 nm offshore for 88 h
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
- **Integrity (SHA-256 of canonical facts):** `9a579ddb02afac02fdd0ed5f2ff4108f829ccafc362cb8bb10c4f20f36fcf047`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
