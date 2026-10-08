# Incident `live_ais__a66ccc621253d9`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Overlapping claim Western Sahara: Western Sahara / Morocco (Western Sahara) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: ICCAT  ·  IMO 7409176
- **Vessel:** 🇸🇻 MONTEFRISA NUEVE  ·  **signal:** AIS gap
- **When (UTC):** 2026-10-04T05:36:26.000Z → 2026-10-04T21:25:35.000Z
- **Gap:** 15.8 h dark, 114.0 nm offshore
- **Where:** 20.127, -19.332

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 114 nm offshore for 16 h
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
- **Integrity (SHA-256 of canonical facts):** `8a119530aa7bfbe18f4f8065d9a97eb1fa5abab84a9165e283ce4e409a77b6d7`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
