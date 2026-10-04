# Incident `live_ais__f1782bd9acf900`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Vanuatuan Exclusive Economic Zone (Vanuatu) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: FFA, WCPFC  ·  IMO 9910026
- **Vessel:** 🇨🇳 ZHONG SHUI 777  ·  **signal:** AIS gap
- **When (UTC):** 2026-09-27T18:57:41.000Z → 2026-09-28T15:20:16.000Z
- **Gap:** 20.4 h dark, 53.0 nm offshore
- **Where:** -19.201, 168.163

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 53 nm offshore for 20 h
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
- **Integrity (SHA-256 of canonical facts):** `a96afac7bf7a47e90e6afb2d396c0fcdbaf04d9b5f27251800b163cf4c79399f`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
