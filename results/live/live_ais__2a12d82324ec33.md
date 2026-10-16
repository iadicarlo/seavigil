# Incident `live_ais__2a12d82324ec33`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Micronesian Exclusive Economic Zone (Micronesia) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: FFA, IOTC, WCPFC  ·  IMO 9991018
- **Vessel:** 🇯🇵 KOYOMARU NO.78  ·  **signal:** AIS gap
- **When (UTC):** 2026-09-27T01:34:51.000Z → 2026-10-12T02:37:04.000Z
- **Gap:** 361.0 h dark, 132.0 nm offshore
- **Where:** 12.983, 138.744

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 132 nm offshore for 361 h
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
- **Integrity (SHA-256 of canonical facts):** `0542aa2551980317f5f699efc84d6eae0f0fb33ebd9b1542126e67adedc838e8`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
