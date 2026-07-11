# Incident `live_ais__7ddc5088a8af49`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** New Zealand Exclusive Economic Zone (Cook Islands) (New Zealand) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: FFA, IATTC, WCPFC  ·  IMO 8654948
- **Vessel:** 🇨🇳 HUA NAN YU 718  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-05T11:04:53.000Z → 2026-07-07T10:16:22.000Z
- **Gap:** 47.2 h dark, 110.0 nm offshore
- **Where:** -8.966, -165.486

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 110 nm offshore for 47 h
- satellite-confirmed AIS gap (GFW Events)

## Could be innocent

Going dark is frequently benign: in open water, where gaps are commonly protecting a fishing ground or waiting out weather. It is most actionable inside or beside a closed zone.

## Caveats

- IUU match is by name only; IUU vessels reuse names, so confirm the identity.
- AIS gaps can be reception loss, not always intentional disabling.
- The position is where AIS dropped; the path while dark is unknown.
- An inspection lead from GFW Events, not proof of illegal activity.

## Provenance & integrity

- NOAA Marine Cadastre AIS (marinecadastre.gov/ais (vessel positions)). US public domain.
- WDPA / WD-OECM (World Database on Protected Areas) (UNEP-WCMC and IUCN (2026), June 2026). Protected Planet Terms of Use (non-commercial, display-only).
- Marine Regions Exclusive Economic Zones v12 (Flanders Marine Institute (2024), DOI 10.14284/632). CC BY 4.0.
- **Integrity (SHA-256 of canonical facts):** `414fe1d6e747f043775357cbd0b8f12312a1cca460a2671a9c8591b1048551b7`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
