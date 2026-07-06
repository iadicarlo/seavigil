# Incident `live_ais__cae21901f67c9a`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Overlapping claim Wake Island / Enenkio: United States / Marshall Islands (United States) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: FFA, IATTC, WCPFC  ·  IMO 8782915
- **Vessel:** 🇹🇼 LI CHENG NO.28  ·  **signal:** AIS gap
- **When (UTC):** 2026-06-29T11:46:26.000Z → 2026-07-02T07:30:47.000Z
- **Gap:** 67.7 h dark, 232.0 nm offshore
- **Where:** 17.854, 163.657

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 232 nm offshore for 68 h
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
- **Integrity (SHA-256 of canonical facts):** `369de4c311ccddeccfde303fccb6bfc701840aab37e774329f7b714aad804624`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
