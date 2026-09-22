#!/usr/bin/env python3
"""Fidelity check for a UI refactor: did the redesign stay faithful to the real product?
Standard library only.

Compares the UI source BEFORE and AFTER a refactor and lists what a redesign must never do silently:
  1. navigation labels that disappeared (renamed or deleted?)
  2. data that changed or vanished (amounts, dates, ids, emails, phone numbers, percentages)
  3. new controls that lead nowhere (placeholder features)
  4. new navigation entries (sections the product may not have)
  5. new marketing claims with no source ("no credit card", "trusted by", "#1", ...)

Every item must be either reverted or listed under "Open questions for the owner" in the change report.
Removing form fields, filler copy, or decorative elements is NOT flagged: that is often the point.

Usage:
  python check_refactor.py --before <original dir> --after <refactored dir>

Tip: copy the UI source to a scratch folder before you start editing, so you have a --before.
Exit code 0 = nothing to disposition, 1 = items listed.
"""
import argparse
import html
import os
import re
import sys

MARKUP = {".html", ".htm", ".jsx", ".tsx", ".vue", ".svelte", ".astro"}
SKIP = {"node_modules", "dist", "build", ".git", "vendor", ".next", "out", "coverage"}
MONTHS = {m: i + 1 for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"])}
CLAIMS = [
    r"no (credit )?card( is)? (required|needed)", r"free forever", r"trusted by", r"loved by", r"join [\d,.]+",
    r"[\d,.]+\+?\s*(k|m|thousand|million)?\s*(customers|teams|users|companies|businesses)", r"#\s?1\b", r"award",
    r"guarantee", r"bank[- ]level", r"secure(d)? by", r"\d+[- ]day (free )?trial", r"cancel any ?time",
    r"money[- ]back", r"rated \d", r"\d(\.\d)?\s*(/|out of)\s*5", r"as seen (in|on)", r"soc ?2", r"gdpr", r"99\.\d+%",
]
VOID_HREF = re.compile(r"^(#|javascript:|)$", re.I)


def files_in(root):
    out = []
    for base, dirs, names in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP and not d.startswith(".")]
        for n in names:
            if os.path.splitext(n)[1].lower() in MARKUP:
                out.append(os.path.join(base, n))
    return sorted(out)


def read(p):
    return open(p, encoding="utf-8", errors="replace").read()


def visible(markup):
    t = re.sub(r"<(script|style)\b.*?</\1>", " ", markup, flags=re.S | re.I)
    t = re.sub(r"<!--.*?-->", " ", t, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    return " ".join(html.unescape(t).split())


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def controls(markup):
    """(label, href-or-None, kind) for links and buttons."""
    out = []
    for m in re.finditer(r"<a\b([^>]*)>(.*?)</a>", markup, flags=re.S | re.I):
        href = re.search(r"\bhref\s*=\s*[\"']([^\"']*)", m.group(1), re.I)
        label = visible(m.group(2))
        if label:
            out.append((label, href.group(1) if href else None, "link"))
    for m in re.finditer(r"<button\b([^>]*)>(.*?)</button>", markup, flags=re.S | re.I):
        label = visible(m.group(2))
        if label:
            typ = re.search(r"\btype\s*=\s*[\"']?(\w+)", m.group(1), re.I)
            out.append((label, None, "submit" if typ and typ.group(1).lower() == "submit" else "button"))
    return out


def nav_labels(markup):
    """Labels of links inside <nav>/<header>, or inside elements whose class mentions nav/menu/topbar/sidebar/tabs."""
    labels = []
    blocks = re.findall(r"<(?:nav|header)\b.*?</(?:nav|header)>", markup, flags=re.S | re.I)
    blocks += re.findall(
        r"<(?:ul|ol|div|aside)\b[^>]*class\s*=\s*[\"'][^\"']*(?:nav|menu|topbar|sidebar|tabs|utils)[^\"']*[\"'][^>]*>.*?</(?:ul|ol|div|aside)>",
        markup, flags=re.S | re.I)
    for b in blocks:
        for label, _h, _k in controls(b):
            if len(label) <= 40:
                labels.append(label)
    return labels


def data_tokens(text):
    toks = {}
    for m in re.finditer(r"[$€£]\s?\d[\d,]*(?:\.\d+)?", text):
        toks[("amount", re.sub(r"[\s,]", "", m.group(0)))] = m.group(0)
    for m in re.finditer(r"\b\d+(?:\.\d+)?\s?%", text):
        toks[("percent", m.group(0).replace(" ", ""))] = m.group(0)
    for m in re.finditer(r"\b[A-Z]{2,5}-\d{2,}\b", text):
        toks[("id", m.group(0))] = m.group(0)
    for m in re.finditer(r"\b[\w.+-]+@[\w-]+\.[\w.]+\b", text):
        toks[("email", m.group(0).lower())] = m.group(0)
    for m in re.finditer(r"\(?\b\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}\b", text):
        toks[("phone", re.sub(r"\D", "", m.group(0)))] = m.group(0)
    for m in re.finditer(r"\b(\d{4})-(\d{2})-(\d{2})\b", text):
        toks[("date", (int(m.group(2)), int(m.group(3))))] = m.group(0)
    for m in re.finditer(r"\b([A-Za-z]{3})[a-z]*\.?\s+(\d{1,2})(?:st|nd|rd|th)?\b", text):
        mon = MONTHS.get(m.group(1).lower())
        if mon:
            toks[("date", (mon, int(m.group(2))))] = m.group(0)
    for m in re.finditer(r"\b(\d{1,2})\s+([A-Za-z]{3})[a-z]*\b", text):
        mon = MONTHS.get(m.group(2).lower())
        if mon:
            toks[("date", (mon, int(m.group(1))))] = m.group(0)
    return toks


def main():
    ap = argparse.ArgumentParser(description="Fidelity check: compare UI before and after a refactor.")
    ap.add_argument("--before", required=True)
    ap.add_argument("--after", required=True)
    a = ap.parse_args()
    bf, af = files_in(a.before), files_in(a.after)
    if not bf or not af:
        print("No markup files found in --before or --after.")
        return 2
    b_markup = "\n".join(read(p) for p in bf)
    a_markup = "\n".join(read(p) for p in af)
    b_text, a_text = visible(b_markup), visible(a_markup)
    a_words = " " + norm(a_text) + " "
    b_words = " " + norm(b_text) + " "
    issues = 0

    def section(title, items, hint):
        nonlocal issues
        if not items:
            return
        issues += len(items)
        print(f"\n[{len(items)}] {title}")
        for it in items:
            print("   " + it)
        print("   -> " + hint)

    # 1. navigation labels that disappeared
    lost = []
    for lab in dict.fromkeys(nav_labels(b_markup)):
        if f" {norm(lab)} " not in a_words:
            lost.append(f'"{lab}"')
    section("navigation labels no longer present", lost,
            "Renaming a jargon label to a plain word is fine if its target proves the meaning: say so in the report. "
            "If you cannot tell what a label means, KEEP it and flag it; do not delete product sections.")

    # 2. data changed or vanished
    bt, at = data_tokens(b_text), data_tokens(a_text)
    gone = [f"{k[0]}: {v}" for k, v in bt.items() if k not in at]
    section("data values from the original that are missing or changed", gone,
            "Reformatting a date or amount is fine (it is matched by value). A value that is gone was either removed on "
            "purpose (say so) or changed by accident (restore it). Never alter sample data to make a design look tidier.")
    new_data = [f"{k[0]}: {v}" for k, v in at.items() if k not in bt and k[0] in ("amount", "percent", "id")]
    section("new amounts / percentages / ids not in the original", new_data,
            "Invented figures mislead. Derive them from existing data or remove them.")

    # 3 + 4. new controls
    b_labels = {norm(l) for l, _h, _k in controls(b_markup)}
    existing = {os.path.basename(p).lower() for p in af}
    new_stub, new_nav = [], []
    a_nav = {norm(l) for l in nav_labels(a_markup)}
    seen = set()
    conventional = {"home", "log in", "login", "sign in", "sign up", "signup", "skip to content", "skip to main content",
                    "back", "cancel", "close", "search", "menu"}
    b_sets = [set(x.split()) for x in b_labels if x]
    brand_words = set(norm(" ".join(re.findall(r"<title>(.*?)</title>", b_markup, flags=re.S | re.I))).split())

    def known(n):
        words = [w for w in n.split() if not w.isdigit() and len(w) > 1]   # drop counts ("All 6") and logo letters
        core = " ".join(words)
        if not core or core in conventional or core in b_labels or f" {core} " in b_words:
            return True
        ws = set(words)
        if ws and ws <= brand_words:
            return True
        return any(bs and (bs <= ws or ws <= bs) for bs in b_sets)     # "Delete" vs "Delete invoice"

    for label, href, kind in controls(a_markup):
        n = norm(label)
        if not n or n in seen or known(n):
            continue
        seen.add(n)
        target = (href or "").split("#")[0].split("?")[0]
        leads_nowhere = (kind == "button") or href is None or VOID_HREF.match(href or "") or \
            (target and not re.match(r"^[a-z]+:", target, re.I) and os.path.basename(target).lower() not in existing)
        if n in a_nav:
            new_nav.append(f'"{label}"' + ("  (leads nowhere)" if leads_nowhere else ""))
        elif leads_nowhere and kind != "submit":
            new_stub.append(f'"{label}"  ({kind}{", href=" + href if href else ""})')
    section("new navigation entries that the original does not have", new_nav,
            "Do not invent product sections. Remove them, or list them as a question for the owner.")
    section("new controls that lead nowhere (placeholder features?)", new_stub,
            "Surfacing an existing function is fine; a button for a function that does not exist is not. "
            "Remove it and note the gap, unless the original had the same function under another label (say which).")

    # 5. new claims
    claims = []
    for pat in CLAIMS:
        for m in re.finditer(pat, a_text, flags=re.I):
            if not re.search(pat, b_text, flags=re.I):
                claims.append('"' + a_text[max(0, m.start() - 25):m.end() + 25].strip() + '"')
                break
    section("new marketing claims with no source in the original", claims,
            "Unsourced claims are invented facts. Remove them or list them as assumptions for the owner to confirm.")

    if issues == 0:
        print("OK: no lost navigation, changed data, stub controls, invented sections, or new claims detected.")
        return 0
    print(f"\n{issues} item(s) to revert or to list under 'Open questions for the owner'.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
