# Incident `live_ais__fa6e5da8444b2b`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Overlapping claim Western Sahara: Western Sahara / Morocco (Western Sahara) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: NEAFC  ·  IMO 9008732
- **Vessel:** 🇧🇸 BALTIC PEARL  ·  **signal:** AIS gap
- **When (UTC):** 2026-06-26T15:07:41.000Z → 2026-06-27T06:26:05.000Z
- **Gap:** 15.3 h dark, 120.0 nm offshore
- **Where:** 23.336, -18.656

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 120 nm offshore for 15 h
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
- **Integrity (SHA-256 of canonical facts):** `4e7894b7d8fbfb354f4b6f5a42ceb3a2f689ca6afa88241fca02511ae708794e`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
