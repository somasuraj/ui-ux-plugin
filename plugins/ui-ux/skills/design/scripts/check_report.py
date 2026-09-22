#!/usr/bin/env python3
"""Validate a ui-ux audit report before delivering it. Standard library only.

Checks what can be checked mechanically:
  1. Coverage table cells equal the number of findings rows with that Screen and Area, and sum to the total.
  2. Every file:line citation points at a real file and a line that exists (no ':0', no line past EOF).
  3. Criticals: how many, and whether each names the blocked task / harm / barrier.
  4. Likely duplicates (same evidence cited by several rows) that should be merged.
  5. Severity and Area values are well-formed; required sections are present.

Usage:
  python check_report.py <report.md> --src <ui source dir>

Exit code 0 = clean, 1 = problems to fix. Fix the report (not the checker) and run again.
"""
import argparse
import os
import re
import sys
from collections import Counter, defaultdict

AREAS = list("ABCDEFGH")
SEVS = {"critical", "major", "minor"}
SECTIONS = ["Verdict", "Top fixes", "Coverage", "Findings", "System health", "What's working", "Not verified"]
HARM_WORDS = re.compile(
    r"block|cannot|can't|unable|unreachable|not focusable|keyboard|screen.?reader|unreadable|illegible|"
    r"looks disabled|no label|unlabel|unnamed|accessible name|lose|loss|wipe|charged|mislead|misled|"
    r"sensitive|card number|income|date of birth|\bdob\b|personal data|harm|prevent", re.I)


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def tables(lines):
    """Yield (header_cells, [row_cells...], first_line_no) for each markdown table."""
    i = 0
    while i < len(lines) - 1:
        if lines[i].lstrip().startswith("|") and re.match(r"^\s*\|?[\s:|-]+\|[\s:|-]*$", lines[i + 1]):
            head, rows, start = cells(lines[i]), [], i + 1
            i += 2
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                rows.append((cells(lines[i]), i + 1))
                i += 1
            yield head, rows, start
        else:
            i += 1


def main():
    ap = argparse.ArgumentParser(description="Validate a ui-ux audit report.")
    ap.add_argument("report")
    ap.add_argument("--src", required=True, help="directory that the report's file:line citations refer to")
    a = ap.parse_args()
    text = open(a.report, encoding="utf-8", errors="replace").read()
    lines = text.splitlines()
    problems, notes = [], []

    # ---- sections ----
    heads = [re.sub(r"^#+\s*", "", ln).strip().lower() for ln in lines if ln.startswith("#")]
    for s in SECTIONS:
        if not any(h.startswith(s.lower()) for h in heads):
            problems.append(f"missing section: '## {s}'")

    # ---- locate tables ----
    findings, coverage = [], None
    for head, rows, start in tables(lines):
        low = [h.lower() for h in head]
        if "sev" in low or "severity" in low:
            findings.append((low, rows))
        elif low and low[0] == "screen" and all(x in [h.upper() for h in head] for x in AREAS):
            coverage = (head, rows)
    if not findings:
        problems.append("no findings table found (needs columns: # | Sev | Screen | Area | Finding | Evidence | Rule | Fix)")
        return report(problems, notes)

    # ---- parse findings ----
    rows_out = []
    for low, rows in findings:
        def col(*names):
            for n in names:
                if n in low:
                    return low.index(n)
            return None
        ci = {k: col(*v) for k, v in {"num": ("#",), "sev": ("sev", "severity"), "screen": ("screen",),
                                      "area": ("area",), "finding": ("finding",), "evidence": ("evidence",)}.items()}
        for c, ln in rows:
            get = lambda k: c[ci[k]] if ci[k] is not None and ci[k] < len(c) else ""
            rows_out.append({"n": get("num"), "sev": get("sev").lower(), "screen": get("screen"),
                             "area": get("area"), "finding": get("finding"), "evidence": get("evidence"), "line": ln})
    total = len(rows_out)
    sev_count = Counter(r["sev"] for r in rows_out)
    notes.append(f"findings: {total}  (" + ", ".join(f"{k} {sev_count.get(k, 0)}" for k in ("critical", "major", "minor")) + ")")

    for r in rows_out:
        if r["sev"] not in SEVS:
            problems.append(f"row #{r['n']} (report line {r['line']}): severity '{r['sev']}' is not Critical/Major/Minor")
        letters = re.findall(r"\b([A-H])\b", r["area"].upper())
        if not letters:
            problems.append(f"row #{r['n']}: Area '{r['area']}' must be one checklist letter A to H (file it where the fix happens)")
        r["area1"] = letters[0] if letters else "?"
        if not r["screen"]:
            problems.append(f"row #{r['n']}: empty Screen (use Global or the screen name)")

    # ---- coverage reconciliation ----
    if coverage is None:
        problems.append("no coverage table found (Screen | A | B | C | D | E | F | G | H)")
    else:
        head, crow = coverage
        idx = {h.upper(): i for i, h in enumerate(head)}
        actual = defaultdict(Counter)
        for r in rows_out:
            actual[r["screen"].strip().lower()][r["area1"]] += 1
        claimed_total = 0
        seen = set()
        for c, ln in crow:
            scr = c[0].strip().lower()
            seen.add(scr)
            for ar in AREAS:
                raw = c[idx[ar]] if idx[ar] < len(c) else ""
                m = re.match(r"\s*(\d+)", raw)
                claimed = int(m.group(1)) if m else 0
                claimed_total += claimed
                real = actual.get(scr, Counter()).get(ar, 0)
                if claimed != real:
                    problems.append(f"coverage '{c[0]}' area {ar}: table says {raw or 'blank'!s}, findings table has {real} row(s)")
        for scr in actual:
            if scr not in seen:
                problems.append(f"findings use Screen '{scr}' but the coverage table has no such row")
        if claimed_total != total:
            problems.append(f"coverage cells sum to {claimed_total} but there are {total} findings rows (fill the table last, by counting rows)")

    # ---- citations ----
    src_files = {}
    for root, _dirs, names in os.walk(a.src):
        for n in names:
            src_files.setdefault(n.lower(), os.path.join(root, n))
    line_cache = {}
    cited = defaultdict(list)
    checked = bad = 0
    for r in rows_out:
        cites = re.findall(r"([\w./\\-]+\.(?:html?|css|scss|less|jsx?|tsx?|vue|svelte|astro))`?(?::|,?\s+lines?\s+)(\d+)(?:\s*-\s*(\d+))?",
                           r["evidence"], flags=re.I)
        if not cites and not re.search(r"\.(html?|css|scss|less|jsx?|tsx?|vue|svelte|astro)\b|screenshot|scan", r["evidence"], re.I):
            problems.append(f"row #{r['n']}: no evidence cited")
        for fname, l1, l2 in cites:
            checked += 1
            key = os.path.basename(fname).lower()
            if key == "css":
                continue
            path = src_files.get(key)
            if not path:
                bad += 1
                problems.append(f"row #{r['n']}: cites '{fname}' which does not exist under --src")
                continue
            if path not in line_cache:
                line_cache[path] = sum(1 for _ in open(path, encoding="utf-8", errors="replace"))
            top = int(l2 or l1)
            if int(l1) < 1 or top > line_cache[path]:
                bad += 1
                problems.append(f"row #{r['n']}: '{fname}:{l1}{'-' + l2 if l2 else ''}' is outside the file (1 to {line_cache[path]}). Cite lines you actually read")
            cited[(key, l1, l2)].append(r["n"])
    notes.append(f"citations checked: {checked}, invalid: {bad}")
    if total and checked < max(3, total // 3):
        problems.append(f"only {checked} file:line citation(s) for {total} findings: write evidence as `file.ext:LINE` "
                        "(for example `signup.html:41-57`) so it can be verified")

    # ---- criticals ----
    crits = [r for r in rows_out if r["sev"] == "critical"]
    if len(crits) > 5:
        problems.append(f"{len(crits)} Criticals: expect about 5 or fewer. Re-rank with the severity anchors "
                        "(failed contrast, landmarks, skip link, heading order, missing tokens, vague copy are not Critical)")
    for r in crits:
        if not re.match(r"\s*[*_`]*\s*(blocks|harm)\s*[*_`]*\s*:", r["finding"], re.I):
            problems.append(f"Critical #{r['n']}: the Finding must start with 'Blocks: <which top task>' or 'Harm: <what happens>'. "
                            "If you cannot fill that in honestly, lower the severity")
        elif not HARM_WORDS.search(r["finding"]):
            notes.append(f"Critical #{r['n']} names no recognizable barrier or harm: double-check it is really Critical")

    # ---- duplicates ----
    for (f, l1, l2), nums in cited.items():
        if len(nums) >= 3:
            notes.append(f"rows {', '.join('#' + n for n in nums)} all cite {f}:{l1}: same cause? merge if so")

    return report(problems, notes)


def report(problems, notes):
    for n in notes:
        print("note:", n)
    if not problems:
        print("OK: report passes the mechanical checks (judgment quality is still yours)")
        return 0
    print(f"\n{len(problems)} problem(s) to fix before delivering:")
    for p in problems:
        print(" -", p)
    return 1


if __name__ == "__main__":
    sys.exit(main())
