#!/usr/bin/env python
"""Resolve and download open-access PDFs for every paper in data/paper-inventory.csv.

Resolution order per paper:
  1. arXiv identifier           -> https://arxiv.org/pdf/<id>
  2. DOI -> Semantic Scholar    -> openAccessPdf.url
  3. DOI -> arXiv title search  -> preprint version (difflib title match >= 0.82)
  4. otherwise                  -> paywalled-no-oa (never bypass paywalls)

Writes PDFs to papers/pdf/<ID>.pdf (local only, gitignored) and a resumable manifest
to data/pdf-manifest.csv. Re-running skips papers already downloaded.
"""
from __future__ import annotations

import csv
import difflib
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV_IN = ROOT / "data" / "paper-inventory.csv"
PDF_DIR = ROOT / "papers" / "pdf"
MANIFEST = ROOT / "data" / "pdf-manifest.csv"
UA = {"User-Agent": "Mozilla/5.0 (research-dossier; PINN literature review)"}


def fetch(url: str, timeout: int = 90) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def norm_title(t: str) -> str:
    return re.sub(r"[^a-z0-9 ]", "", t.lower()).strip()


def s2_lookup(doi: str) -> tuple[str, str]:
    """Return (oa_url, arxiv_id) from Semantic Scholar; both may be empty."""
    try:
        import json
        data = fetch(f"https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}"
                     f"?fields=openAccessPdf,externalIds", timeout=45)
        j = json.loads(data)
        oa = (j.get("openAccessPdf") or {}).get("url") or ""
        arx = (j.get("externalIds") or {}).get("ArXiv") or ""
        return oa, arx
    except Exception:
        return "", ""


PUBLISHER_PDF = [
    # DOI prefix -> url template (OA papers only; failures fall through gracefully)
    ("10.1007/", "https://link.springer.com/content/pdf/{doi}.pdf"),
    ("10.1038/", "https://www.nature.com/articles/{suffix}.pdf"),
    ("10.3389/", "https://www.frontiersin.org/journals/{j}/articles/{doi_full}/pdf"),
    ("10.1371/", "https://journals.plos.org/plosone/article/file?id={doi}&type=printable"),
]


def publisher_direct(doi: str) -> str | None:
    for prefix, tpl in PUBLISHER_PDF:
        if doi.startswith(prefix):
            suffix = doi.split("/", 1)[1] if "/" in doi else doi
            j = doi.split("/")[1].split(".")[0] if doi.startswith("10.3389/") else ""
            if "{j}" in tpl and not j:
                return None
            return tpl.format(doi=doi, suffix=suffix, j=j)
    return None


def arxiv_pdf_by_title(title: str) -> str | None:
    try:
        words = norm_title(title).split()
        queries = [f'ti:"{title[:180]}"', 'ti:"' + " ".join(words[:8]) + '"']
        for q in queries:
            xml = fetch(f"http://export.arxiv.org/api/query?search_query="
                        f"{urllib.parse.quote(q)}&max_results=5",
                        timeout=45).decode("utf-8", "replace")
            entries = re.findall(r"<entry>(.*?)</entry>", xml, re.S)
            want = norm_title(title)
            for e in entries:
                t = re.search(r"<title>(.*?)</title>", e, re.S)
                i = re.search(r"<id>https?://arxiv.org/abs/([^<]+)</id>", e)
                if not (t and i):
                    continue
                cand = norm_title(re.sub(r"\s+", " ", t.group(1)))
                if difflib.SequenceMatcher(None, want, cand).ratio() >= 0.82:
                    return "https://arxiv.org/pdf/" + i.group(1)
    except Exception:
        pass
    return None


def download(url: str, dest: Path) -> int:
    data = fetch(url)
    if not data.startswith(b"%PDF") or len(data) < 15_000:
        raise ValueError(f"not a valid PDF ({len(data)} bytes)")
    dest.write_bytes(data)
    return len(data)


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="process only first N pending papers")
    args = ap.parse_args()

    PDF_DIR.mkdir(parents=True, exist_ok=True)
    with CSV_IN.open(encoding="utf-8") as f:
        papers = [r for r in csv.DictReader(f) if r.get("title")]

    done = {m["id"]: m for m in csv.DictReader(MANIFEST.open(encoding="utf-8"))} if MANIFEST.exists() else {}
    rows, n_ok = [], 0
    pending = 0
    for p in sorted(papers, key=lambda r: (int(r["priority"] or 5), r["id"])):
        pid = p["id"]
        dest = PDF_DIR / f"{pid}.pdf"
        if pid in done and done[pid]["status"] == "downloaded" and dest.exists():
            continue
        if args.limit and pending >= args.limit:
            rows.append({"id": pid, "status": "not-attempted", "source_url": "", "bytes": "", "note": ""})
            continue
        pending += 1
        ident = p.get("identifier", "")
        url, status, note = "", "", ""
        m_arx = re.search(r"arXiv[:\s]*([0-9]{4}\.[0-9]{4,5})(v\d+)?", ident, re.I)
        doi = ident[4:].strip() if ident.upper().startswith("DOI:") else ident
        m_doi = re.match(r"^(10\.\d{4,9}/\S+)$", doi.strip())
        try:
            if dest.exists() and dest.stat().st_size > 15_000:
                status, note = "downloaded", "pre-existing"
            elif m_arx:
                url = f"https://arxiv.org/pdf/{m_arx.group(1)}"
                note = f"{download(url, dest)} bytes"
                status = "downloaded"
            elif m_doi:
                time.sleep(1.2)
                oa_url, s2_arx = s2_lookup(m_doi.group(1))
                ok = False
                if oa_url:
                    url = oa_url
                    try:
                        note = f"{download(url, dest)} bytes (S2 OA)"
                        status, ok = "downloaded", True
                    except Exception as e:
                        note = f"S2 OA invalid: {str(e)[:60]}"
                if not ok and s2_arx:
                    try:
                        url = f"https://arxiv.org/pdf/{s2_arx}"
                        note = f"{download(url, dest)} bytes (S2 arXiv id {s2_arx})"
                        status, ok = "downloaded", True
                    except Exception as e:
                        note = f"{note}; S2 arXiv id invalid: {str(e)[:60]}"
                if not ok:
                    pu = publisher_direct(m_doi.group(1))
                    if pu:
                        try:
                            url, note = pu, f"{download(pu, dest)} bytes (publisher direct)"
                            status, ok = "downloaded", True
                        except Exception as e:
                            note = f"{note}; publisher direct invalid: {str(e)[:60]}"
                if not ok:
                    time.sleep(3.0)
                    u2 = arxiv_pdf_by_title(p["title"])
                    if u2:
                        url, note = u2, "arXiv preprint (title match)"
                        download(url, dest)
                        status = "downloaded"
                    elif url and note:
                        status = "failed"
                    else:
                        status = "paywalled-no-oa"
            else:
                status = "no-pdf-webpage" if p.get("type") == "webpage" else "no-identifier"
        except Exception as e:
            status, note = "failed", str(e)[:120]
        if status == "downloaded":
            n_ok += 1
        rows.append({"id": pid, "status": status, "source_url": url, "bytes": note, "note": ""})
        print(f"[{pid}] {status} {note}", flush=True)

    all_rows = {**done, **{r["id"]: r for r in rows}}
    with MANIFEST.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["id", "status", "source_url", "bytes", "note"])
        w.writeheader()
        w.writerows(sorted(all_rows.values(), key=lambda r: r["id"]))
    print(f"DONE: {n_ok} new downloads; manifest -> {MANIFEST}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
