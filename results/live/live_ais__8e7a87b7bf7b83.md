# Incident `live_ais__8e7a87b7bf7b83`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Marshallese Exclusive Economic Zone (Marshall Islands) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: FFA, WCPFC  ·  IMO 9217357
- **Vessel:** 🇳🇷 ORIENTAL MARINE  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-24T04:33:58.000Z → 2026-07-26T09:01:36.000Z
- **Gap:** 52.5 h dark, 84.0 nm offshore
- **Where:** 2.673, 168.869

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 84 nm offshore for 52 h
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
- **Integrity (SHA-256 of canonical facts):** `6bcf1d97607e6896637e0eef67249a12764c249c67b7a5e757016f227efbbe1b`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
