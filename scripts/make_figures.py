#!/usr/bin/env python
"""Generate dossier figures from data/paper-inventory.csv (Okabe-Ito palette, 300 dpi PNG).

Figures:
  fig1_timeline.png          records per year, stacked by domain group
  fig2_domain_mechanism.png  heatmap: domain group x enforcement mechanism
  fig3_mechanism_bar.png     horizontal bar: enforcement mechanism counts
  fig4_citations.png         bubble scatter: year vs citations (log), colored by domain
  fig5_problem_types.png     horizontal bar: problem-type counts
  fig6_venues.png            horizontal bar: top venues by record count
"""
from __future__ import annotations

import csv
import re
import sys
from collections import Counter
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
CSV = ROOT / "data" / "paper-inventory.csv"
FIGDIR = ROOT / "figures"

plt.rcParams.update({
    "font.family": "serif", "font.serif": ["Times New Roman", "DejaVu Serif"],
    "font.size": 10, "axes.titlesize": 11, "axes.titleweight": "bold",
    "axes.labelsize": 10, "legend.fontsize": 8.5, "legend.frameon": False,
    "figure.dpi": 300, "savefig.dpi": 300, "savefig.bbox": "tight",
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.alpha": 0.15, "grid.linestyle": "-",
})

# Okabe-Ito (colorblind-safe) + extra distinct hues + grays (>= 11 domain buckets)
COLORS = ["#0072B2", "#E69F00", "#009E73", "#D55E00", "#56B4E9",
          "#CC79A7", "#F0E442", "#004949", "#9467BD", "#8C8C8C",
          "#17BECF", "#B0BEC5", "#7F4F24"]

SLICE_DOMAIN = {
    "A": "Methods & training", "B": "Architectures & operators",
    "C": "Fluids & aerospace", "D": "Energy & power",
    "E": "Biomed & geo & civil", "F": "Materials & mfg",
    "G": "Meta-reviews",
}

DOMAIN_RULES = [
    (r"financ|option|pricing|hjb|portfolio", "Finance"),
    (r"climat|weather|atmospher|gcm", "Climate & weather"),
    (r"biom|cardiac|medic|clinic|tumor|blood|imaging|health|anatom|ecg|patient", "Biomed & healthcare"),
    (r"seism|subsurf|darcy|groundwater|hydrolog|reservoir|geotech|soil|geophys|civil|structural|dam|bridge", "Geoscience & civil"),
    (r"materi|fracture|phase.?field|manufac|additive|weld|melt|crystal|microstruct|elastoplast", "Materials & mfg"),
    (r"batter|grid|power|nuclear|hvac|solar|wind|electrochem|renewab|energ|bms", "Energy & power"),
    (r"fluid|aerospac|aero|turbulen|navier|rans|airfoil|jet|nozzle|heat transfer|thermal|acoustic|hypersonic", "Fluids & aerospace"),
    (r"operat|deepo|fno|transformer|foundation|fourier|siren|decompos|bayes|uncert|uq", "Architectures & operators"),
    (r"theor|converg|error|train|sampl|benchmark|framework|optimi|failure|patholog|weight", "Methods & training"),
    (r"survey|review|bibliom|landscape", "Meta-reviews"),
]


def domain_group(rec: dict) -> str:
    text = (rec.get("domain", "") + " " + rec.get("problem_type", "")).lower()
    for pat, name in DOMAIN_RULES:
        if re.search(pat, text):
            return name
    return SLICE_DOMAIN.get(rec.get("slices", "")[:1], "Other")


def mech_group(rec: dict) -> str:
    m = rec.get("mechanism", "").lower()
    if re.search(r"hard|constrain(t|ed)|architectur.{0,20}constr|marching|lift", m):
        return "Hard constraint"
    if re.search(r"weak|variational|ritz|galerkin|petrov", m):
        return "Weak/variational"
    if re.search(r"energy", m):
        return "Energy-form"
    if re.search(r"operator", m):
        return "Operator/surrogate"
    if re.search(r"hybrid|mix|combin|multi", m):
        return "Hybrid"
    if re.search(r"soft|penalt|residual", m):
        return "Soft penalty (residual)"
    return "Mixed/unspecified"


def parse_cites(rec: dict):
    m = re.match(r"^(\d[\d,]*)", rec.get("citations", "").replace(",", ""))
    return int(m.group(1)) if m else None


def load() -> list[dict]:
    with CSV.open(encoding="utf-8") as f:
        rows = [r for r in csv.DictReader(f) if r.get("title")]
    for r in rows:
        r["_domain"] = domain_group(r)
        r["_mech"] = mech_group(r)
        r["_cites"] = parse_cites(r)
        try:
            r["_year"] = int(re.match(r"^(19|20)\d{2}", r["year"]).group(0))
        except (AttributeError, ValueError):
            r["_year"] = None
    return rows


def fig1_timeline(rows):
    years = list(range(2019, 2027))
    domains = sorted({r["_domain"] for r in rows})
    counts = {d: [0] * len(years) for d in domains}
    for r in rows:
        if r["_year"] in years:
            counts[r["_domain"]][years.index(r["_year"])] += 1
    fig, ax = plt.subplots(figsize=(6.75, 4.1))
    bottom = np.zeros(len(years))
    for i, d in enumerate(domains):
        vals = np.array(counts[d], dtype=float)
        ax.bar(years, vals, bottom=bottom, label=d, color=COLORS[i % len(COLORS)],
               width=0.72, edgecolor="white", linewidth=0.5)
        bottom += vals
    for x, b in zip(years, bottom):
        if b:
            ax.text(x, b + 0.4, f"{int(b)}", ha="center", va="bottom", fontsize=8, color="#444")
    ax.set_xlabel("Publication year")
    ax.set_ylabel("Surveyed papers")
    ax.set_title("Verified dossier papers per year (pre-2021 = seminal anchors)")
    ax.legend(ncol=3, loc="upper center", bbox_to_anchor=(0.5, -0.13), fontsize=7.5)
    fig.savefig(FIGDIR / "fig1_timeline.png")
    plt.close(fig)


def fig2_heat(rows):
    domains = sorted({r["_domain"] for r in rows})
    mechs = ["Soft penalty (residual)", "Hard constraint", "Weak/variational",
             "Energy-form", "Operator/surrogate", "Hybrid", "Mixed/unspecified"]
    M = np.zeros((len(domains), len(mechs)))
    for r in rows:
        if r["_domain"] in domains and r["_mech"] in mechs:
            M[domains.index(r["_domain"])][mechs.index(r["_mech"])] += 1
    fig, ax = plt.subplots(figsize=(7.0, 4.0))
    im = ax.imshow(M.T, cmap="YlGnBu", aspect="auto")
    ax.set_xticks(range(len(domains)))
    ax.set_xticklabels(domains, rotation=35, ha="right", fontsize=8)
    ax.set_yticks(range(len(mechs)))
    ax.set_yticklabels(mechs, fontsize=8.5)
    for i in range(len(domains)):
        for j in range(len(mechs)):
            v = int(M[i][j])
            if v:
                ax.text(i, j, str(v), ha="center", va="center", fontsize=8,
                        color="white" if M[i][j] > M.max() * 0.6 else "#333")
    ax.set_title("Enforcement mechanism x domain group (surveyed papers)")
    ax.grid(False)
    fig.colorbar(im, ax=ax, shrink=0.75, label="papers")
    fig.savefig(FIGDIR / "fig2_domain_mechanism.png")
    plt.close(fig)


def fig3_mech(rows):
    c = Counter(r["_mech"] for r in rows).most_common()
    labels = [k for k, _ in c][::-1]
    vals = [v for _, v in c][::-1]
    fig, ax = plt.subplots(figsize=(4.8, 2.9))
    ax.barh(labels, vals, color=COLORS[0], height=0.58, edgecolor="white", linewidth=0.5)
    for y, v in enumerate(vals):
        ax.text(v + 0.3, y, str(v), va="center", fontsize=8, color="#444")
    ax.set_xlabel("Papers in dossier")
    ax.set_title("How do recent PINN works enforce physics?")
    fig.savefig(FIGDIR / "fig3_mechanism_bar.png")
    plt.close(fig)


def fig4_cites(rows):
    pts = [r for r in rows if r["_cites"] and r["_year"]]
    domains = sorted({r["_domain"] for r in pts})
    fig, ax = plt.subplots(figsize=(6.75, 4.3))
    for i, d in enumerate(domains):
        xs = [r["_year"] for r in pts if r["_domain"] == d]
        ys = [r["_cites"] for r in pts if r["_domain"] == d]
        ax.scatter(xs, ys, s=26, color=COLORS[i % len(COLORS)], label=d,
                   alpha=0.75, edgecolors="white", linewidths=0.4)
    top = sorted(pts, key=lambda r: -r["_cites"])[:8]
    ordered = []
    for yr in sorted({r["_year"] for r in top}):
        ordered += sorted((r for r in top if r["_year"] == yr), key=lambda r: -r["_cites"])
    # Global gutter: labels stacked top-to-bottom with a guaranteed minimum gap,
    # leader lines connecting each label to its true point.
    callouts = [[i, r, float(r["_cites"])] for i, r in enumerate(ordered, 1)]
    callouts.sort(key=lambda t: -t[2])
    for j in range(1, len(callouts)):
        if callouts[j][2] > callouts[j - 1][2] / 1.35:
            callouts[j][2] = callouts[j - 1][2] / 1.35
    for i, r, y_lab in callouts:
        ax.annotate(f"({i})", xy=(r["_year"], r["_cites"]), xytext=(2027.0, y_lab),
                    fontsize=7.5, weight="bold", color="#222", va="center",
                    arrowprops=dict(arrowstyle="-", lw=0.6, color="#999", alpha=0.7),
                    annotation_clip=False)
    ax.set_xlim(2018.5, 2028.6)
    ax.set_yscale("log")
    ax.margins(y=0.10)
    ax.set_xlabel("Publication year")
    ax.set_ylabel("Citations (approx., log scale)")
    ax.set_title("Citations vs year — numbered callouts for 8 most-cited")
    ax.legend(ncol=3, fontsize=6.8, loc="upper center", bbox_to_anchor=(0.5, -0.13))
    lines = ["  ".join(f"({i}) {r['title'][:40]}... {r['_year']}" if len(r['title']) > 40
                       else f"({i}) {r['title']} {r['_year']}")
             for i, r in enumerate(ordered, 1)]
    fig.text(0.01, -0.24, "\n".join(lines), fontsize=6.2, color="#444", va="top")
    fig.savefig(FIGDIR / "fig4_citations.png")
    plt.close(fig)


def fig5_problem(rows):
    c = Counter((r.get("problem_type") or "?").lower().split("/")[0] for r in rows).most_common()
    labels = [k for k, _ in c][::-1]
    vals = [v for _, v in c][::-1]
    fig, ax = plt.subplots(figsize=(4.8, 2.9))
    ax.barh(labels, vals, color=COLORS[2], height=0.58, edgecolor="white", linewidth=0.5)
    for y, v in enumerate(vals):
        ax.text(v + 0.3, y, str(v), va="center", fontsize=8, color="#444")
    ax.set_xlabel("Papers in dossier")
    ax.set_title("Problem classes addressed")
    fig.savefig(FIGDIR / "fig5_problem_types.png")
    plt.close(fig)


def norm_venue(v: str) -> str:
    v = re.sub(r"\s*20\d{2}.*$", "", v).strip()
    if v.lower().startswith("arxiv"):
        return "arXiv preprint"
    return v or "Unknown"


def fig6_venues(rows):
    c = Counter(norm_venue(r["venue"].strip()) for r in rows if r.get("venue")).most_common(14)
    labels = [k if len(k) <= 52 else k[:49] + "..." for k, _ in c][::-1]
    vals = [v for _, v in c][::-1]
    fig, ax = plt.subplots(figsize=(6.0, 4.2))
    ax.barh(labels, vals, color=COLORS[1], height=0.6, edgecolor="white", linewidth=0.5)
    for y, v in enumerate(vals):
        ax.text(v + 0.08, y, str(v), va="center", fontsize=8, color="#444")
    ax.set_xlabel("Papers in dossier")
    ax.set_title("Most frequent venues (top 14, normalized)")
    fig.savefig(FIGDIR / "fig6_venues.png")
    plt.close(fig)


def main() -> int:
    if not CSV.exists():
        print("Run scripts/consolidate.py first.", file=sys.stderr)
        return 1
    FIGDIR.mkdir(exist_ok=True)
    rows = load()
    fig1_timeline(rows); fig2_heat(rows); fig3_mech(rows)
    fig4_cites(rows); fig5_problem(rows); fig6_venues(rows)
    print(f"OK: 6 figures -> {FIGDIR} ({len(rows)} papers)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
