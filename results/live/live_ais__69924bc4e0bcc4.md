# Incident `live_ais__69924bc4e0bcc4`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Nauruan Exclusive Economic Zone (Nauru) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: FFA, WCPFC  ·  IMO 9764415
- **Vessel:** 🇸🇧 SOUTHERN SEAS 301  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-04T11:16:49.000Z → 2026-07-13T00:54:59.000Z
- **Gap:** 205.6 h dark, 179.0 nm offshore
- **Where:** -1.041, 165.307

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 179 nm offshore for 206 h
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
- **Integrity (SHA-256 of canonical facts):** `0bfe986bc9069b40113492df8a6f6bf15bfbab75b4a430d374e37d93d2fce00f`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
