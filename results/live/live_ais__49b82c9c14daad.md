# Incident `live_ais__49b82c9c14daad`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** United States Exclusive Economic Zone (Jarvis Islands) (United States) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: FFA, WCPFC  ·  IMO 9713985
- **Vessel:** 🇰🇷 F/V.MIRAERO  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-03T06:13:38.000Z → 2026-07-08T11:10:06.000Z
- **Gap:** 124.9 h dark, 109.0 nm offshore
- **Where:** -0.420, -161.829

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 109 nm offshore for 125 h
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
- **Integrity (SHA-256 of canonical facts):** `773437fa12d9663993270834ebf72a7b69a7053a72b2b9798ceeb28c89600918`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
