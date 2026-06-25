# SeaVigil - outreach pack

Drafts to reach Global Fishing Watch, conservation NGOs, and National Geographic. Sender:
Isma Abdelkader Di Carlo (independent / solo). Ask: **collaboration / feedback** (low-friction).
Links: code https://github.com/iadicarlo/SeaVigil · live map https://iadicarlo.github.io/SeaVigil
(the live map goes up once GitHub Pages is enabled).
Honest framing throughout - lead with what's genuinely ours, name the limits ourselves.

> Before sending, clear the gates in [`DEPLOY.md`](DEPLOY.md): re-verify Skylight still ships
> no per-flag explanation; keep every claim **scoped** ("SHAP attribution *of the fishing
> detection itself*"); stay non-commercial; don't imply proof of illegality.

---

## One-pager (paste into an email or a PDF)

**SeaVigil - an auditable, offline triage layer for fishing inside Marine Protected Areas.**

SeaVigil turns vessel-movement signals into a *per-incident, explainable dossier* an
enforcement officer can read, defend, and act on - running on a single laptop, no cloud
account.

**What's genuinely new (and what isn't).** Detection is solved - it's GFW's flagship work,
and even real-time MPA-incursion alerting already ships free (Skylight). SeaVigil doesn't
re-detect. It occupies the seam the incumbents leave open:
- **Per-flag SHAP explanation of the fishing detection itself** - *why this position scored as
  fishing* (speed, turning, distance-to-shore…). No IUU-fishing tool ships this; they expose a
  score, not an attribution.
- **Offline / no-account / laptop-CPU**, for a low-capacity coastal authority that can't depend
  on a foreign-hosted account.
- **An auditable per-incident dossier** (who · where · when · the reason · the caveats).

**How it works.** A RandomForest (trained on GFW's open labels) scores AIS positions with SHAP;
positions are overlaid on MPA boundaries and segmented into incidents; each becomes a dossier.
It **consumes** signal rather than re-detecting: it scores *your own* AIS/VMS feed (GFW doesn't
publish raw AIS), and pulls GFW's published **SAR detections** for the dark fleet.

**Honest limits.** Output is an *inspection lead, not courtroom proof* (VMS outranks public
AIS/SAR in court). "Apparent" fishing, behaviourally inferred. Non-commercial (built on GFW +
WDPA data).

**Proof points.** Runs in ~90 s on CPU. Verified live on GFW SAR: ~6,200 detections / ~1,100
dark inside four large MPAs over 2024. Per-flag SHAP dossiers + a static MapLibre map.
Repo: https://github.com/iadicarlo/SeaVigil · live map: https://iadicarlo.github.io/SeaVigil.

---

## Email 1 - Global Fishing Watch (collaboration / feedback)

**Subject:** An explainable, offline triage layer built on your data - would value your feedback

Hi `[name]`,

I'm Isma Abdelkader Di Carlo, an independent developer. I built a small open, non-commercial tool -
SeaVigil - **on top of your data**: it trains on your open labels and (where useful) consumes
your published SAR detections. I want to be upfront that it reproduces your fishing-detection
*target*; I'm not claiming to have invented detection, and I know Skylight already ships MPA
alerting.

What it adds is a thin layer you (deliberately) leave to others: a **per-flag SHAP
explanation** of *why* a position scored as fishing, an **auditable per-incident dossier**, and
a **laptop-deployable, no-account** footprint aimed at low-capacity coastal authorities. It
treats your output as a signal to *explain and make actionable*, not to re-derive.

I'd genuinely value your feedback - whether this is useful, whether I've framed your work
fairly, and whether there's a complementary direction worth pursuing. Repo and a short demo:
https://github.com/iadicarlo/SeaVigil · https://iadicarlo.github.io/SeaVigil. Happy to talk at whatever depth is useful.

Thank you for making the data open - none of this exists without it.

Isma Abdelkader Di Carlo

---

## Email 2 - Conservation NGO / enforcement partner (collaboration / feedback)

**Subject:** Offline, explainable fishing-in-MPA triage for low-capacity authorities - feedback?

Hi `[name]`,

I'm Isma Abdelkader Di Carlo, an independent developer. I've built SeaVigil, a free, non-commercial tool
that flags apparent fishing and dark (non-broadcasting) vessels **inside Marine Protected
Areas** and produces a per-incident dossier - with a plain, auditable reason for each flag.

The deliberate difference from the cloud platforms: it runs **offline on a laptop, with no
account**, scoring an authority's **own** AIS/VMS feed, and pulls public GFW SAR detections for
the dark fleet. It's meant for the place the well-resourced tools don't reach - a coastal
authority that can't depend on a foreign-hosted login. Output is an *inspection lead, not
proof*, and I keep that explicit.

Given your work in this space, I'd really value your read: is the offline + explainable angle
useful to the partners you serve? What would make it credible enough to pilot? Repo + demo:
https://github.com/iadicarlo/SeaVigil · https://iadicarlo.github.io/SeaVigil.

Thanks for considering it,

Isma Abdelkader Di Carlo

---

## Email 3 - National Geographic (Pristine Seas) / advocacy (feedback / story)

**Subject:** Making MPA enforcement auditable and offline - a Global-South angle, and your thoughts

Hi `[name]`,

I'm Isma Abdelkader Di Carlo, an independent developer. I built SeaVigil, a free, non-commercial tool that
turns vessel-movement and satellite signals into an **auditable, per-incident dossier** of
apparent fishing and dark vessels inside Marine Protected Areas - designed to run **offline on
a laptop** so an under-resourced coastal authority can actually use it.

The story I think is worth telling isn't "new detection" (that exists) - it's the **last mile**:
making the *reason* a vessel was flagged legible and defensible, and putting it in the hands of
people without a cloud budget. I've verified it on real satellite detections inside reserves
like the Galápagos.

I'd value your perspective - whether this resonates with your conservation/enforcement work, and
whether there's a way it could support it. Repo + a short visual demo: https://github.com/iadicarlo/SeaVigil · https://iadicarlo.github.io/SeaVigil. Honest about
the limits: it's an inspection lead, not proof, and strictly non-commercial.

Warm regards,

Isma Abdelkader Di Carlo

---

## What to show them

- **Live map** (https://iadicarlo.github.io/SeaVigil) - AIS apparent-fishing (orange, with a SHAP "why")
  vs dark-vessel SAR (red), click-through to the reason.
- **One AIS SHAP dossier** + **one dark-vessel dossier** from `results/incidents/` (e.g. a
  Phoenix Islands longline incident and a `sar__…` dark detection).
- The honest framing in [`README.md`](../README.md) and the competitive table.

## Before you send (gate)

1. Re-verify Skylight still ships no per-flag explanation (DEPLOY §2) - your one durable moat.
2. Keep claims **scoped** to the fishing-detection explanation; don't claim MPA alerting.
3. If anyone bites on a **pilot**, do the real-data demo first: their AIS feed via `--positions`
   + a real WDPA boundary (DEPLOY §3), out-of-sample.
4. Non-commercial only; attribute Global Fishing Watch.
