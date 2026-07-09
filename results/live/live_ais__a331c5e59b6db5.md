# Incident `live_ais__a331c5e59b6db5`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Micronesian Exclusive Economic Zone (Micronesia) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: FFA, IOTC, WCPFC  ·  IMO 9874959
- **Vessel:** 🇯🇵 TOKIWA MARU NO.38  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-02T22:24:12.000Z → 2026-07-05T08:17:29.000Z
- **Gap:** 57.9 h dark, 171.0 nm offshore
- **Where:** 6.210, 142.349

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 171 nm offshore for 58 h
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
- **Integrity (SHA-256 of canonical facts):** `83b0e00cd4685c277f7d8eb7dc5f4bab35b29814c901ad4aba1e605968d83b27`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
