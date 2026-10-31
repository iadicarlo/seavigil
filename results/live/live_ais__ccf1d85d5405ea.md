# Incident `live_ais__ccf1d85d5405ea`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Japanese Exclusive Economic Zone (Japan) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: NPFC  ·  IMO 9869497
- **Vessel:** 🇨🇳 FU YUAN YU 8675  ·  **signal:** AIS gap
- **When (UTC):** 2026-10-26T14:30:51.000Z → 2026-10-27T08:14:59.000Z
- **Gap:** 17.7 h dark, 253.0 nm offshore
- **Where:** 37.592, 145.737

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 253 nm offshore for 18 h
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
- **Integrity (SHA-256 of canonical facts):** `66c8427696b4ab6d46bc42bcf664b4f9899b9c740d7a24b1433534d66a5b5aab`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
