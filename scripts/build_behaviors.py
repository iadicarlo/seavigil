#!/usr/bin/env python3
"""Build behavioral-anomaly dossiers (AIS spoofing, going dark) from real AIS tracks.

These are the behaviors that need identity-bearing continuous AIS, which the curated
GFW labels do not have. Source: NOAA Marine Cadastre (US public domain), extracted by
scripts/fetch_noaa_ais.py. AIS spoofing (impossible-speed jumps, MMSI conflicts) is
detectable from terrestrial AIS; going-dark needs satellite AIS to tell intentional
disabling from out-of-receiver-range, so on this terrestrial feed it correctly finds
little. Dossiers are written to results/behaviors/.

Run:  uv run python scripts/build_behaviors.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from seavigil import data, going_dark, spoofing  # noqa: E402
from seavigil.dossier import write_dossiers  # noqa: E402
from seavigil.evidence import enrich_evidence  # noqa: E402
from seavigil.jurisdiction import enrich_jurisdiction  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
TRACKS = ROOT / "data" / "positions" / "noaa_tracks.csv"
OUT = ROOT / "results" / "behaviors"


def main() -> None:
    df = data.load_positions_file(str(TRACKS))  # auto-enriches distance_from_shore
    spoof = spoofing.build_spoofing_dossiers(df)
    dark = going_dark.build_disabling_dossiers(df)
    dossiers = spoof + dark
    enrich_jurisdiction(dossiers)
    enrich_evidence(dossiers)
    write_dossiers(dossiers, OUT)
    print(f"AIS spoofing: {len(spoof)} dossiers | going-dark: {len(dark)} dossiers -> {OUT}")
    if not dark:
        print("(going-dark empty as expected on terrestrial AIS; needs satellite AIS)")


if __name__ == "__main__":
    main()
