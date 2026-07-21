# Incident `live_ais__de66aa372045a6`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Mauritanian Exclusive Economic Zone (Mauritania) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: ICCAT, IOTC, WCPFC  ·  IMO 8613267
- **Vessel:** 🇪🇸 ALBONIGA  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-17T06:31:10.000Z → 2026-07-17T19:27:54.000Z
- **Gap:** 12.9 h dark, 146.0 nm offshore
- **Where:** 19.278, -19.325

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 146 nm offshore for 13 h
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
- **Integrity (SHA-256 of canonical facts):** `3d77593645fef7a52adb7203d10b87734d7c74eb35389743d52767d6efab8f6c`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
