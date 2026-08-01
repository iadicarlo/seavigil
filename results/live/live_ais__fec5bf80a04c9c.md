# Incident `live_ais__fec5bf80a04c9c`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Vanuatuan Exclusive Economic Zone (Vanuatu) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: FFA, WCPFC  ·  IMO 9686091
- **Vessel:** 🇨🇳 ZHONGSHUI727  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-27T19:14:42.000Z → 2026-07-28T12:09:13.000Z
- **Gap:** 16.9 h dark, 74.0 nm offshore
- **Where:** -13.643, 169.015

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 74 nm offshore for 17 h
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
- **Integrity (SHA-256 of canonical facts):** `d28af3d30e30b2a772958f33ec23454422787ef4f7611ff6317dfe77353d04ac`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
