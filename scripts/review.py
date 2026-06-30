#!/usr/bin/env python3
"""Operator triage for SeaVigil cases: the VERIFY stage, as a CLI.

An operator works the ranked queue and records a decision per case; it is written to a committed,
auditable state file (data/review_state.json) and applied at build time. The confirm / dismiss calls
also become the labelled set the accuracy report uses, so the false-positive rate stops being an
estimate.

  uv run python scripts/review.py list                       # the open queue (new, ranked)
  uv run python scripts/review.py show <case_id>             # full case
  uv run python scripts/review.py set <case_id> dismissed --note "sun glint" --by alice
  uv run python scripts/review.py stats                      # coverage + operator-derived precision
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from seavigil.review import (STATUSES, apply_review, case_fingerprint, load_state,  # noqa: E402
                             precision_from_reviews, save_state, set_review)

CASES = ROOT / "results" / "cases" / "cases.json"


def _load_cases() -> list[dict]:
    if not CASES.exists():
        raise SystemExit(f"No cases at {CASES}; run scripts/build_cases.py first.")
    cases = json.loads(CASES.read_text())
    apply_review(cases)
    return cases


def _find(cases: list[dict], cid: str) -> dict:
    exact = [c for c in cases if c.get("case_id") == cid]
    if exact:
        return exact[0]
    pref = [c for c in cases if (c.get("case_id") or "").startswith(cid)
            or (c.get("case_id") or "") == f"case_{cid}"]
    if len(pref) == 1:
        return pref[0]
    if len(pref) > 1:
        raise SystemExit(f"'{cid}' is ambiguous ({len(pref)} cases match); use more of the id")
    raise SystemExit(f"no case matches '{cid}'")


def _line(c: dict) -> str:
    badge = "IUU" if c.get("iuu_listed") else ("CORROB" if c.get("corroborated") else "")
    return (f"{c['case_id']}  {c.get('severity', '?'):6} conf {c.get('confidence', 0):.2f}  "
            f"{c.get('n_sensors', 1)}x {','.join(c.get('sources', [])):16} {badge:6} "
            f"[{c.get('review_status', 'new')}]  {c.get('eez_iso_sov') or '--':4} "
            f"{(c.get('flag') or '').strip():4} {(c.get('summary') or '')[:46]}")


def cmd_list(a, cases):
    sel = cases
    if a.status:
        sel = [c for c in sel if c.get("review_status") == a.status]
    if a.severity:
        sel = [c for c in sel if c.get("severity") == a.severity]
    sel = [c for c in sel if (c.get("confidence") or 0) >= a.min_confidence]
    sel.sort(key=lambda c: (c.get("iuu_listed", False), c.get("corroborated", False),
                            c.get("confidence") or 0), reverse=True)
    print(f"{len(sel)} case(s)  [status={a.status or 'any'} severity={a.severity or 'any'} "
          f"conf>={a.min_confidence}]")
    for c in sel[:a.limit]:
        print("  " + _line(c))
    if len(sel) > a.limit:
        print(f"  ... {len(sel) - a.limit} more (raise --limit)")


def cmd_show(a, cases):
    c = _find(cases, a.case_id)
    keys = ("case_id", "severity", "confidence", "corroborated", "n_sensors", "sources", "iuu_listed",
            "centroid_lat", "centroid_lon", "eez_iso_sov", "flag", "ship_name", "identity_type",
            "identity_value", "time_start_utc", "summary", "review_status", "review_by", "review_note",
            "review_ts", "review_stale", "members")
    print(json.dumps({k: c.get(k) for k in keys}, indent=1))


def cmd_set(a, cases):
    c = _find(cases, a.case_id)
    state = load_state()
    set_review(state, c["case_id"], a.status, case_fingerprint(c), by=a.by, note=a.note)
    save_state(state)
    print(f"{c['case_id']} -> {a.status} (by {a.by}){': ' + a.note if a.note else ''}")
    print("apply to the published view + accuracy report with: uv run python scripts/build_cases.py")


def cmd_stats(a, cases):
    p = precision_from_reviews(cases)
    print(json.dumps(p, indent=1))
    if p["judged"]:
        print(f"\noperator-derived precision {p['operator_precision']} "
              f"(false-positive rate {p['false_positive_rate']}) over {p['judged']} judged case(s)")
    else:
        print("\nno confirm/dismiss decisions yet; triage with: "
              "review.py set <case_id> confirmed|dismissed")


def main() -> None:
    ap = argparse.ArgumentParser(description="SeaVigil case triage (VERIFY)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    pl = sub.add_parser("list", help="show the queue")
    pl.add_argument("--status", choices=list(STATUSES) + ["new"], default="new")
    pl.add_argument("--severity", choices=["high", "medium", "low"])
    pl.add_argument("--min-confidence", type=float, default=0.0)
    pl.add_argument("--limit", type=int, default=20)
    sub.add_parser("show", help="full case detail").add_argument("case_id")
    pe = sub.add_parser("set", help="record a triage decision")
    pe.add_argument("case_id")
    pe.add_argument("status", choices=STATUSES)
    pe.add_argument("--note", default="")
    pe.add_argument("--by", default="operator")
    sub.add_parser("stats", help="coverage + operator-derived precision")
    a = ap.parse_args()
    handlers = {"list": cmd_list, "show": cmd_show, "set": cmd_set, "stats": cmd_stats}
    handlers[a.cmd](a, _load_cases())


if __name__ == "__main__":
    main()
