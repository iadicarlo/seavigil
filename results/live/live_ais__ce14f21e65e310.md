# Incident `live_ais__ce14f21e65e310`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Nauruan Exclusive Economic Zone (Nauru) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: FFA, WCPFC  ·  IMO 9720213
- **Vessel:** 🇹🇼 FONG KUO NO:189  ·  **signal:** AIS gap
- **When (UTC):** 2026-09-19T02:10:02.000Z → 2026-10-01T18:09:14.000Z
- **Gap:** 304.0 h dark, 186.0 nm offshore
- **Where:** -0.013, 165.945

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 186 nm offshore for 304 h
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
- **Integrity (SHA-256 of canonical facts):** `f3ac2fa12c7e526a3a9fd101718ac81251b9a62aa88968f165d07bfce9dbfa61`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
