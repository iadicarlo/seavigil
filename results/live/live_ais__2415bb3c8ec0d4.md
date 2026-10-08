# Incident `live_ais__2415bb3c8ec0d4`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Angolan Exclusive Economic Zone (Angola) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: ICCAT, IOTC  ·  IMO 9717943
- **Vessel:** 🇨🇼 HAIZEA BAT  ·  **signal:** AIS gap
- **When (UTC):** 2026-10-02T10:17:19.000Z → 2026-10-04T20:36:15.000Z
- **Gap:** 58.3 h dark, 73.0 nm offshore
- **Where:** -13.674, 11.500

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 73 nm offshore for 58 h
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
- **Integrity (SHA-256 of canonical facts):** `e5ebfb546cebd4983b1e1fc3527cfd2aa792aae7bc9a050f56309def92c7e3f4`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
