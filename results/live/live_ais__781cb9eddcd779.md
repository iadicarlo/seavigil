# Incident `live_ais__781cb9eddcd779`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Omani Exclusive Economic Zone (Oman) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)  ·  IMO 9448700
- **Vessel:** 🇸🇦 DILAM  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-26T17:28:37.000Z → 2026-07-30T11:33:33.000Z
- **Gap:** 90.1 h dark, 66.0 nm offshore
- **Where:** 14.685, 54.533

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 66 nm offshore for 90 h
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
- **Integrity (SHA-256 of canonical facts):** `5ead61fb1bb9c61db2f459f0d2303f9d74c32507fd691933962e6e3593453d42`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
