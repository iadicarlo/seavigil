# Incident `live_ais__9625beb197f3a6`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Papua New Guinean Exclusive Economic Zone (Papua New Guinea) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: FFA, IOTC, WCPFC  ·  IMO 9874959
- **Vessel:** 🇯🇵 TOKIWA MARU NO.38  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-21T23:27:21.000Z → 2026-08-03T07:41:38.000Z
- **Gap:** 296.2 h dark, 158.0 nm offshore
- **Where:** 1.483, 146.492

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 158 nm offshore for 296 h
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
- **Integrity (SHA-256 of canonical facts):** `aaa20acb19fa93b6bc842dcf127e7643a0380ff73442d229f07c1709ef949e09`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
