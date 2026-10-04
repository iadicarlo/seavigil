# Incident `live_ais__7764fcdcc7fe70`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Indonesian Exclusive Economic Zone (Indonesia) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: CCSBT, FFA, GFCM, IATTC, ICCAT, WCPFC  ·  IMO 9658549
- **Vessel:** 🇯🇵 YAHATAMARU NO.5  ·  **signal:** AIS gap
- **When (UTC):** 2026-09-29T13:36:47.000Z → 2026-09-30T03:51:22.000Z
- **Gap:** 14.2 h dark, 234.0 nm offshore
- **Where:** -11.607, 113.840

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 234 nm offshore for 14 h
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
- **Integrity (SHA-256 of canonical facts):** `2079317af985f565be9ec77c6678402b10ce4e94a9303a72afe14a30a7f842aa`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
