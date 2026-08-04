# Incident `live_ais__8b781b726f08b1`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** United States Exclusive Economic Zone (Jarvis Islands) (United States) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: FFA, WCPFC  ·  IMO 9781645
- **Vessel:** 🇨🇳 XINSHIJI 111  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-17T16:46:04.000Z → 2026-07-31T23:04:08.000Z
- **Gap:** 342.3 h dark, 158.0 nm offshore
- **Where:** -2.370, -159.486

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 158 nm offshore for 342 h
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
- **Integrity (SHA-256 of canonical facts):** `67ce189791842366a8234f887a0745663da051de5a1593d8321f0c2f1e0aadc2`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
