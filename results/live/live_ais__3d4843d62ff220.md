# Incident `live_ais__3d4843d62ff220`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Papua New Guinean Exclusive Economic Zone (Papua New Guinea) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: FFA, IOTC, WCPFC  ·  IMO 9619323
- **Vessel:** 🇰🇷 SAJO FAMILIA  ·  **signal:** AIS gap
- **When (UTC):** 2026-09-08T19:03:38.000Z → 2026-09-26T02:22:23.000Z
- **Gap:** 415.3 h dark, 146.0 nm offshore
- **Where:** -1.081, 153.529

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 146 nm offshore for 415 h
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
- **Integrity (SHA-256 of canonical facts):** `209cf656701010adf56fcc190e236af33db2e165f86b3a770fecd56a406724d6`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
