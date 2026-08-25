# Incident `live_ais__fa1b360053a908`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Kiribati Exclusive Economic Zone (Phoenix Group) (Kiribati) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: FFA, WCPFC  ·  IMO 9781645
- **Vessel:** 🇨🇳 XINSHIJI 111  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-01T19:45:05.000Z → 2026-08-21T05:25:26.000Z
- **Gap:** 465.7 h dark, 315.0 nm offshore
- **Where:** -2.384, -175.404

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 315 nm offshore for 466 h
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
- **Integrity (SHA-256 of canonical facts):** `ccc18b663b9d753d96c498c7deccda570426d618e81008f6cef240530e96ff8f`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
