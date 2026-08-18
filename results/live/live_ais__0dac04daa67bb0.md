# Incident `live_ais__0dac04daa67bb0`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Tuvaluan Exclusive Economic Zone (Tuvalu) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: FFA, WCPFC  ·  IMO 8628901
- **Vessel:** 🇨🇳 ZHONGSHUI 701  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-13T20:42:21.000Z → 2026-08-14T11:22:32.000Z
- **Gap:** 14.7 h dark, 124.0 nm offshore
- **Where:** -10.025, 177.430

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 124 nm offshore for 15 h
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
- **Integrity (SHA-256 of canonical facts):** `17d82807d9399b266e0fa30c10ea0c4b47ef03317b84eddf4f80824dc0ad0a56`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
