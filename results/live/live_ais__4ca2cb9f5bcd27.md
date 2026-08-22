# Incident `live_ais__4ca2cb9f5bcd27`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** São Toméan Exclusive Economic Zone (Sao Tome and Principe) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: ICCAT, IOTC, WCPFC  ·  IMO 8912986
- **Vessel:** 🇫🇷 F/V GUEOTEC  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-16T17:26:57.000Z → 2026-08-17T05:34:57.000Z
- **Gap:** 12.1 h dark, 85.0 nm offshore
- **Where:** 0.319, 5.208

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 85 nm offshore for 12 h
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
- **Integrity (SHA-256 of canonical facts):** `f2631860600f9edd6c7a98e0c93c6df232315feea9a61ac88bf38e48e0e52eb5`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
