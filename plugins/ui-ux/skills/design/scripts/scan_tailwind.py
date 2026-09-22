#!/usr/bin/env python3
"""Utility-class (Tailwind-style) pass for the ui-ux scanner. Called by scan.py; can also run alone.
Standard library only.

In a utility-class codebase the design values live in class names, not in CSS rules, so this pass
enumerates them from class / className strings and lists candidates with file:line.

Usage: python scan_tailwind.py <dir-or-file> [more ...]
"""
import os
import re
import sys
from collections import Counter, defaultdict

MARKUP = {".html", ".htm", ".jsx", ".tsx", ".vue", ".svelte", ".astro", ".js", ".ts"}
SKIP = {"node_modules", "dist", "build", ".git", "vendor", ".next", "out", "coverage", ".cache"}
SIZES = {"xs", "sm", "base", "lg", "xl", "2xl", "3xl", "4xl", "5xl", "6xl", "7xl", "8xl", "9xl"}
WEIGHTS = {"thin", "extralight", "light", "normal", "medium", "semibold", "bold", "extrabold", "black"}
PALETTE = ("slate|gray|zinc|neutral|stone|red|orange|amber|yellow|lime|green|emerald|teal|cyan|sky|blue|indigo|"
           "violet|purple|fuchsia|pink|rose")
CLASS_RE = re.compile(r"class(?:Name)?\s*=\s*(?:\"([^\"]*)\"|'([^']*)'|\{\s*`([^`]*)`\s*\}|\{\s*\"([^\"]*)\"\s*\})", re.S)


def collect(paths):
    out = []
    for p in paths:
        if os.path.isfile(p):
            out.append(p)
            continue
        for base, dirs, names in os.walk(p):
            dirs[:] = [d for d in dirs if d not in SKIP and not d.startswith(".")]
            out += [os.path.join(base, n) for n in names
                    if os.path.splitext(n)[1].lower() in MARKUP and not n.endswith(".config.js")]
    return sorted(out)


def line_of(text, pos):
    return text.count("\n", 0, pos) + 1


def base(cls):
    """Strip variants: 'md:hover:bg-blue-600' -> 'bg-blue-600'."""
    return cls.split(":")[-1].lstrip("!-")


def looks_like_utility_codebase(paths):
    n = 0
    for p in collect(paths)[:80]:
        t = open(p, encoding="utf-8", errors="replace").read()
        n += len(re.findall(r"\b(?:p[xytblr]?|m[xytblr]?|gap|text|bg|rounded|flex|grid)-[\w\[\]#.%/-]+", t))
        if n > 40:
            return True
    return False


def report(paths, rel=None, max_items=12):
    files = collect(paths)
    rel = rel or (lambda p: os.path.basename(p))
    text_size, weight, color, spacing, radius, shadow, arbitrary = (Counter() for _ in range(7))
    variants = Counter()
    cand = defaultdict(list)
    per_file_solid = defaultdict(list)
    screens_without_h1, has_landmark = [], set()

    for p in files:
        t = open(p, encoding="utf-8", errors="replace").read()
        f = rel(p)
        for tag in ("main", "nav", "header", "footer"):
            if re.search(r"<" + tag + r"\b", t):
                has_landmark.add(tag)
        if re.search(r"[\\/](screens|pages|routes|views)[\\/]", p.replace("\\", "/") + "/") and os.path.splitext(p)[1].lower() in (".jsx", ".tsx", ".vue", ".svelte"):
            if not re.search(r"<h1\b", t):
                screens_without_h1.append(f)

        for m in CLASS_RE.finditer(t):
            raw = next(g for g in m.groups() if g is not None)
            ln = line_of(t, m.start())
            classes = [c for c in re.split(r"\s+", re.sub(r"\$\{[^}]*\}", " ", raw)) if c]
            bases = [base(c) for c in classes]
            for c in classes:
                for v in c.split(":")[:-1]:
                    variants[v] += 1
            for b in bases:
                if re.search(r"-\[[^\]]+\]$", b):
                    arbitrary[b] += 1
                m2 = re.fullmatch(r"text-(\[[^\]]+\]|\w+)", b)
                if m2 and (m2.group(1) in SIZES or re.fullmatch(r"\[[\d.]+(px|rem|em)\]", m2.group(1))):
                    text_size[b] += 1
                m2 = re.fullmatch(r"font-(\w+)", b)
                if m2 and m2.group(1) in WEIGHTS:
                    weight[b] += 1
                if re.fullmatch(r"(text|bg|border|ring|fill|stroke|from|to|via|divide|placeholder)-(?:(?:" + PALETTE + r")-\d{2,3}|black|white|\[#[0-9a-fA-F]{3,8}\])(/\d+)?", b):
                    color[re.sub(r"^(text|bg|border|ring|fill|stroke|from|to|via|divide|placeholder)-", "", b)] += 1
                if re.fullmatch(r"-?(p|m|gap|space)[xytblrse]?-(\[[^\]]+\]|[\d.]+|px)", b):
                    spacing[re.sub(r"^-?(p|m|gap|space)[xytblrse]?-", "", b)] += 1
                if re.fullmatch(r"rounded(-[trbl]{1,2})?(-(none|sm|md|lg|xl|2xl|3xl|full|\[[^\]]+\]))?", b):
                    radius[re.sub(r"-[trbl]{1,2}(?=-|$)", "", b)] += 1
                if re.fullmatch(r"shadow(-(sm|md|lg|xl|2xl|inner|none|\[[^\]]+\]))?", b):
                    shadow[b] += 1

            bs = set(bases)
            where = f"{f}:{ln}"
            if "font-light" in bs or "font-thin" in bs or "font-extralight" in bs:
                cand["font weight under 400 (font-light / thin)"].append(where)
            if "text-black" in bs or any(re.fullmatch(r"text-\[#0{3,6}\]", b) for b in bs):
                cand["pure black text"].append(where)
            if "uppercase" in bs and not any(b.startswith("tracking-") for b in bs):
                cand["uppercase without letter-spacing (tracking-*)"].append(where)
            if ("outline-none" in bs or "focus:outline-none" in classes) and not any(
                    c.startswith(("focus:ring", "focus-visible:ring", "focus:border", "focus-visible:outline", "focus:outline-2", "focus:shadow")) for c in classes):
                cand["outline-none with no replacement focus style"].append(where)
            for b in bs:
                if re.fullmatch(r"text-(white|black)/\d+|text-opacity-\d+|opacity-\d+", b) and any(x.startswith("text-") for x in bs):
                    if any(re.match(r"bg-(?!white|transparent)", x) for x in bs) or b.startswith("text-white/"):
                        cand["translucent text (white/NN or opacity) - washed out on color; pick a real tint"].append(f"{where} {b}")
                        break
            for b in bs:
                if re.fullmatch(r"w-\[\d+%\]|w-\d/\d+", b) and re.search(r"side|nav|aside|rail", t[max(0, m.start() - 200):m.start() + 50], re.I):
                    cand["percent-width sidebar/nav (usually should be fixed)"].append(f"{where} {b}")
            if "text-center" in bs:
                cand["centered text (fine for short blocks only - check length)"].append(where)
            if any(re.fullmatch(r"(min-)?w-\[\d{3,4}px\]", b) for b in bs):
                cand["large fixed pixel width (breaks small screens)"].append(f"{where} " + " ".join(b for b in bs if re.fullmatch(r"(min-)?w-\[\d{3,4}px\]", b)))
            shadows_arb = [b for b in bs if re.fullmatch(r"shadow-\[[^\]]+\]", b)]
            for s in shadows_arb:
                m3 = re.match(r"shadow-\[(-?[\d.]+)(?:px)?_(-?[\d.]+)", s)
                if m3 and (float(m3.group(2)) < 0 or abs(float(m3.group(1))) > 1):
                    cand["shadow not cast from above (x offset or negative y)"].append(f"{where} {s}")
            tagm = re.search(r"<(\w+)[^<>]*$", t[:m.start()])
            tag = tagm.group(1).lower() if tagm else ""
            solid = [b for b in bs if re.fullmatch(r"bg-(?:(?:" + PALETTE + r")-(?:[5-9]00)|black|\[#[0-9a-fA-F]{3,8}\])", b)]
            if tag in ("button", "a") and solid and not any(b in ("bg-transparent",) for b in bs):
                per_file_solid[f].append((ln, solid[0]))

    if not (text_size or color or spacing):
        return False

    def show(counter, label, note=""):
        vals = sorted(counter.items(), key=lambda kv: (-kv[1], kv[0]))
        print(f"\n{label}: {len(vals)} distinct{note}")
        print("  " + ", ".join(f"{v} x{n}" for v, n in vals[:50]) + (f", +{len(vals) - 50} more" if len(vals) > 50 else ""))

    print("\n" + "=" * 72)
    print("UTILITY-CLASS VALUES (Tailwind-style; enumerated from class names - quote these in 'System health')")
    show(text_size, "text sizes")
    show(weight, "font weights")
    show(color, "colors", "  (palette names and arbitrary hexes; near-duplicates such as gray-400/gray-500/[#8b8b8b] = no grey system)")
    show(spacing, "spacing values (p/m/gap/space)")
    show(radius, "radii", "  (more than one family = inconsistent personality)")
    show(shadow, "shadows")
    arb_kinds = Counter(re.sub(r"^-?", "", a).split("-[")[0] for a in arbitrary.elements())
    print(f"\narbitrary one-off values: {sum(arbitrary.values())} uses, {len(arbitrary)} distinct "
          f"(by kind: " + ", ".join(f"{k} x{n}" for k, n in arb_kinds.most_common(10)) + ")")
    print("  most used: " + ", ".join(f"{v} x{n}" for v, n in arbitrary.most_common(20)))
    resp = sum(n for v, n in variants.items() if v in ("sm", "md", "lg", "xl", "2xl"))
    foc = sum(n for v, n in variants.items() if v.startswith("focus"))
    hov = variants.get("hover", 0)
    print(f"\nvariants: responsive (sm/md/lg/xl) x{resp}, hover x{hov}, focus x{foc}, disabled x{variants.get('disabled', 0)}")
    if resp == 0:
        print("  -> no responsive variants: check small-screen behaviour")
    if foc == 0:
        print("  -> no focus variants: check that keyboard focus is visible")
    missing = [x for x in ("header", "nav", "main") if x not in has_landmark]
    if missing:
        print("  -> no <" + ">, <".join(missing) + "> element anywhere in the components (landmarks)")

    for f, items in per_file_solid.items():
        if len(items) >= 3:
            cand["several solid (filled) buttons in one screen/component: which is THE primary action?"].append(
                f"{f}: {len(items)} solid buttons/links at lines " + ", ".join(str(ln) for ln, _ in items[:10]))
    if screens_without_h1:
        cand["screen component with no <h1> (screen name?)"] += screens_without_h1

    print("\nUTILITY-CLASS CANDIDATES (confirm each in the code)")
    for key in sorted(cand):
        items = cand[key]
        print(f"\n[{len(items)}] {key}")
        for it in items[:max_items]:
            print("   " + it)
        if len(items) > max_items:
            print(f"   +{len(items) - max_items} more")
    print("\nContrast in a utility codebase: resolve the palette names to hex from the Tailwind config or defaults,")
    print("then check pairs with contrast.py. Arbitrary hex pairs can be checked directly.")
    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    report(sys.argv[1:])
