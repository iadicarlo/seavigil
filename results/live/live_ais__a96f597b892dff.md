# Incident `live_ais__a96f597b892dff`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Seychellois Exclusive Economic Zone (Seychelles) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: IOTC  ·  IMO 9359703
- **Vessel:** 🇴🇲 NOUR  ·  **signal:** AIS gap
- **When (UTC):** 2026-10-08T03:07:21.000Z → 2026-10-21T12:38:20.000Z
- **Gap:** 321.5 h dark, 89.0 nm offshore
- **Where:** -2.134, 52.790

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 89 nm offshore for 322 h
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
- **Integrity (SHA-256 of canonical facts):** `4c5fb51061291e4e1ca04306014da563983da70793764f8801036bcc32c307b8`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
