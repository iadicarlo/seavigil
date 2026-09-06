# Incident `live_ais__5a66e4fd8a589b`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Liberian Exclusive Economic Zone (Liberia) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: ICCAT  ·  IMO 9568861
- **Vessel:** 🇬🇭 PANOFI PATH FINDER  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-24T13:39:18.000Z → 2026-09-02T09:34:35.000Z
- **Gap:** 211.9 h dark, 488.0 nm offshore
- **Where:** 2.623, -11.350

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 488 nm offshore for 212 h
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
- **Integrity (SHA-256 of canonical facts):** `bdc485df2021efa4e0914292ace075162d805378fb3b251ef30f68e16b38926f`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
