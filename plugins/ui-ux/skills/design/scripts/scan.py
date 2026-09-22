#!/usr/bin/env python3
"""Static UI scanner for the ui-ux skill. Standard library only.

Enumerates the design values actually used (so system-health counts are counted, not estimated)
and lists CANDIDATE markup/accessibility/contrast issues with file:line. It reads source text only:
every candidate must be confirmed by reading the code (and the rendered UI when possible) before
it becomes a finding. It cannot judge hierarchy, wording, or whether something is deliberate.

Usage:
  python scan.py <dir-or-file> [more ...] [--max 40]

Scans: .html .htm .css .scss .less .jsx .tsx .vue .svelte .astro  (skips node_modules, dist, build, .git, vendor, .next)
"""
import argparse
import colorsys
import os
import re
import sys
from collections import Counter, defaultdict

EXTS = {".html", ".htm", ".css", ".scss", ".less", ".jsx", ".tsx", ".vue", ".svelte", ".astro"}
SKIP = {"node_modules", "dist", "build", ".git", "vendor", ".next", "out", "coverage", ".cache"}
MARKUP = {".html", ".htm", ".jsx", ".tsx", ".vue", ".svelte", ".astro"}
NAMED = {"white": (1, 1, 1), "black": (0, 0, 0)}
IGNORE_COLORS = {"transparent", "inherit", "currentcolor", "initial", "unset", "none"}


# ---------- color helpers ----------
def parse_color(s):
    s = s.strip().lower()
    if s in NAMED:
        return NAMED[s] + (1.0,)
    m = re.fullmatch(r"#([0-9a-f]{3,8})", s)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        if len(h) not in (6, 8):
            return None
        r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
        return (r, g, b, int(h[6:8], 16) / 255 if len(h) == 8 else 1.0)
    m = re.fullmatch(r"(rgb|hsl)a?\(([^)]*)\)", s)
    if not m or "var(" in s:
        return None
    parts = [p for p in re.split(r"[,\s/]+", m.group(2).strip()) if p]
    if len(parts) < 3:
        return None
    try:
        def num(p, scale):
            return float(p.rstrip("%")) / (100 if p.endswith("%") else scale)
        a = num(parts[3], 1) if len(parts) > 3 else 1.0
        if m.group(1) == "rgb":
            r, g, b = (num(p, 255) for p in parts[:3])
        else:
            hue = float(re.sub(r"[a-z]+$", "", parts[0])) % 360 / 360
            r, g, b = colorsys.hls_to_rgb(hue, num(parts[2], 100), num(parts[1], 100))
        return (r, g, b, a)
    except ValueError:
        return None


def norm_color(s):
    c = parse_color(s)
    if c is None:
        return s.strip().lower()
    r, g, b, a = c
    hexv = "#%02x%02x%02x" % (round(r * 255), round(g * 255), round(b * 255))
    return hexv if a >= 0.999 else f"{hexv}@{a:.2f}"


def lum(c):
    def f(v):
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(c[0]) + 0.7152 * f(c[1]) + 0.0722 * f(c[2])


def contrast(fg, bg):
    bg3 = tuple(bg[i] * bg[3] + 1 * (1 - bg[3]) for i in range(3))
    fg3 = tuple(fg[i] * fg[3] + bg3[i] * (1 - fg[3]) for i in range(3))
    hi, lo = sorted((lum(fg3), lum(bg3)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)


COLOR_RE = re.compile(r"#[0-9a-fA-F]{3,8}\b|(?:rgb|hsl)a?\([^)]*\)|\b(?:white|black)\b")


# ---------- file walking ----------
def collect(paths):
    files = []
    for p in paths:
        if os.path.isfile(p):
            files.append(p)
            continue
        for root, dirs, names in os.walk(p):
            dirs[:] = [d for d in dirs if d not in SKIP and not d.startswith(".")]
            for n in names:
                if os.path.splitext(n)[1].lower() in EXTS and not n.endswith(".min.css"):
                    files.append(os.path.join(root, n))
    return sorted(files)


def line_of(text, pos):
    return text.count("\n", 0, pos) + 1


def css_blocks(path, text):
    """Yield (css_text, offset) for stylesheet files and <style> blocks."""
    ext = os.path.splitext(path)[1].lower()
    if ext in {".css", ".scss", ".less"}:
        yield text, 0
    else:
        for m in re.finditer(r"<style[^>]*>(.*?)</style>", text, re.S | re.I):
            yield m.group(1), m.start(1)


def main():
    ap = argparse.ArgumentParser(description="Static UI scanner (candidates + enumerated system values).")
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--max", type=int, default=40, help="max lines per candidate list")
    a = ap.parse_args()
    files = collect(a.paths)
    if not files:
        print("No UI source files found.")
        return 1
    base = os.path.commonpath([os.path.abspath(f) for f in files])
    if os.path.isfile(base):
        base = os.path.dirname(base)

    def rel(p):
        return os.path.relpath(os.path.abspath(p), base).replace("\\", "/")

    sizes, weights, colors, spacing, shadows, radii, leadings = (Counter() for _ in range(7))
    borders = tokens = media = var_uses = raw_uses = 0
    cand = defaultdict(list)
    rules = []  # (file, line, selector, decl dict)
    class_use = defaultdict(set)  # class name -> markup files using it
    has_components = any(os.path.splitext(p)[1].lower() in (".jsx", ".tsx", ".vue", ".svelte", ".astro") for p in files)
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    try:
        import scan_tailwind
        utility_codebase = scan_tailwind.looks_like_utility_codebase(a.paths)
    except Exception:
        scan_tailwind, utility_codebase = None, False

    for path in files:
        try:
            text = open(path, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        f = rel(path)
        ext = os.path.splitext(path)[1].lower()

        # ----- styles -----
        for css, off in css_blocks(path, text):
            css_nc = re.sub(r"/\*.*?\*/", lambda m: " " * len(m.group(0)), css, flags=re.S)
            media += len(re.findall(r"@media", css_nc))
            tokens += len(re.findall(r"(?m)^\s*--[\w-]+\s*:", css_nc))
            for m in re.finditer(r"([^{};]+)\{([^{}]*)\}", css_nc):
                sel = " ".join(m.group(1).split())
                if sel.startswith("@"):
                    continue
                ln = line_of(text, off + m.start(1) + len(m.group(1)) - len(m.group(1).lstrip()))
                decl = {}
                for d in m.group(2).split(";"):
                    if ":" in d:
                        k, v = d.split(":", 1)
                        decl[k.strip().lower()] = v.strip()
                rules.append((f, ln, sel, decl))
                for k, v in decl.items():
                    vl = v.lower()
                    if k == "font-size":
                        sizes[vl] += 1
                    elif k == "font-weight":
                        weights[vl] += 1
                    elif k == "line-height":
                        leadings[vl] += 1
                    elif k == "box-shadow" and vl != "none":
                        shadows[" ".join(vl.split())] += 1
                    elif k == "border-radius":
                        radii[vl] += 1
                    elif k in ("border", "border-top", "border-bottom", "border-left", "border-right") and vl not in ("0", "none"):
                        borders += 1
                    if k.startswith(("margin", "padding")) or k in ("gap", "row-gap", "column-gap"):
                        for px in re.findall(r"(-?\d*\.?\d+)px", vl):
                            if float(px) != 0:
                                spacing[px.lstrip("-") + "px"] += 1
                        for em in re.findall(r"(-?\d*\.?\d+)(r?em)\b", vl):
                            spacing[em[0] + em[1]] += 1
                    for c in COLOR_RE.findall(v):  # includes token definitions: they are the palette
                        if c.lower() not in IGNORE_COLORS:
                            colors[norm_color(c)] += 1
                    if "var(" in vl:
                        var_uses += 1
                    elif not k.startswith("--"):
                        raw_uses += 1

        # ----- markup -----
        if ext in MARKUP:
            for m in re.finditer(r"class(?:Name)?\s*=\s*[\"']([^\"']+)", text):
                for cname in m.group(1).split():
                    class_use[cname].add(f)
            for m in re.finditer(r"<(span|div|p|li|td|img|i|svg|h[1-6])\b[^>]*\son[cC]lick\s*=", text):
                cand["click handler on non-interactive element (not focusable/keyboard operable)"].append(f"{f}:{line_of(text, m.start())} <{m.group(1)}>")
            # buttons / links whose only content is an icon: they need an accessible name
            for m in re.finditer(r"<(button|a)\b((?:[^>\"'{}]|\"[^\"]*\"|'[^']*'|\{(?:[^{}]|\{[^{}]*\})*\})*)>(.*?)</\1>", text, re.S):
                attrs, inner = m.group(2), m.group(3)
                if re.search(r"aria-label(ledby)?\s*=|\btitle\s*=", attrs):
                    continue
                no_tags = re.sub(r"<[^<>]*>", " ", inner)               # drop child tags together with their attributes
                visible_txt = re.sub(r"\{[^{}]*\}", " ", no_tags)
                has_expr_text = re.search(r"\{[^{}]+\}", no_tags)        # a {label} / {"text"} child counts as text
                if not re.search(r"[A-Za-z0-9]", visible_txt) and not has_expr_text and re.search(r"<\s*(svg|img|i\b|[A-Z]\w*)", inner):
                    cand["icon-only button/link with no accessible name (aria-label)"].append(f"{f}:{line_of(text, m.start())} <{m.group(1)}>")
            for m in re.finditer(r"<img\b[^>]*>", text, re.I):
                if not re.search(r"\salt\s*=", m.group(0), re.I):
                    cand["<img> without alt"].append(f"{f}:{line_of(text, m.start())}")
            label_for = set(re.findall(r"<label\b[^>]*\b(?:for|htmlFor)\s*=\s*[\"'{]+([^\"'}]+)", text, re.I))
            for m in re.finditer(r"<(input|select|textarea)\b[^>]*>", text, re.I):
                tag = m.group(0)
                typ = (re.search(r"\btype\s*=\s*[\"']?(\w+)", tag, re.I) or [None, "text"])[1].lower()
                if typ in ("hidden", "submit", "button", "reset", "image"):
                    continue
                idm = re.search(r"\bid\s*=\s*[\"']([^\"']+)", tag, re.I)
                inside_label = text.rfind("<label", 0, m.start()) > text.rfind("</label>", 0, m.start())
                named = re.search(r"aria-label(ledby)?\s*=", tag, re.I)
                if not ((idm and idm.group(1) in label_for) or inside_label or named):
                    note = " (placeholder only)" if re.search(r"\bplaceholder\s*=", tag, re.I) else ""
                    cand["form control with no label / accessible name"].append(f"{f}:{line_of(text, m.start())} <{m.group(1).lower()}>{note}")
                if re.search(r"\bpattern\s*=", tag, re.I):
                    cand["rigid input format (pattern=)"].append(f"{f}:{line_of(text, m.start())}")
                vm = re.search(r"\bvalue\s*=\s*[\"']([^\"']{8,})", tag, re.I)
                if vm and typ == "text" and re.search(r"(type|enter|search|here|\.\.\.)", vm.group(1), re.I):
                    cand["hint text set as a real value (user must delete it)"].append(f"{f}:{line_of(text, m.start())} \"{vm.group(1)[:40]}\"")
            for m in re.finditer(r"<(?:button|input)\b[^>]*\btype\s*=\s*[\"']reset", text, re.I):
                cand["reset button (wipes the form)"].append(f"{f}:{line_of(text, m.start())}")
            for m in re.finditer(r"<form\b.*?</form>", text, re.S | re.I):
                n = len(re.findall(r"<(?:input|select|textarea)\b(?![^>]*type\s*=\s*[\"']?(?:hidden|submit|button|reset))", m.group(0), re.I))
                req = len(re.findall(r"\brequired\b", m.group(0)))
                if n >= 6:
                    cand["long form (check every field is needed for THIS task)"].append(f"{f}:{line_of(text, m.start())} {n} fields, {req} required")
            # a single-page-app shell (index.html with a mount node and component files) is judged by its components
            spa_shell = ext in (".html", ".htm") and has_components and re.search(r"id\s*=\s*[\"'](root|app)[\"']", text)
            if ext in (".html", ".htm") and not spa_shell:
                missing = [t for t in ("header", "nav", "main", "footer") if not re.search(rf"<{t}\b", text, re.I)]
                if missing:
                    cand["missing landmarks"].append(f"{f}: no <{'>, <'.join(missing)}>")
                if not re.search(r"href\s*=\s*[\"']#(main|content|skip)[^\"']*[\"']|skip to", text, re.I):
                    cand["no skip-to-content link"].append(f)
                h1 = len(re.findall(r"<h1\b", text, re.I))
                if h1 != 1:
                    cand["h1 count is not 1 (screen name?)"].append(f"{f}: {h1} <h1>")
                levels = [int(x) for x in re.findall(r"<h([1-6])\b", text, re.I)]
                for prev, cur in zip(levels, levels[1:]):
                    if cur - prev > 1:
                        cand["heading level jump"].append(f"{f}: h{prev} then h{cur}")
                        break
                tm = re.search(r"<title>(.*?)</title>", text, re.S | re.I)
                cand["_titles"].append((f, " ".join(tm.group(1).split()) if tm else "(none)"))
            n_hash = len(re.findall(r"href\s*=\s*[\"']#[\"']", text))
            if n_hash:
                cand["_stubs"].append(f"{f}: {n_hash} href=\"#\"")
            if not utility_codebase:  # in a utility-class codebase the dedicated pass summarizes these instead
                for m in re.finditer(r"class(?:Name)?\s*=\s*[\"'{`]+([^\"'`}]*)", text):
                    for arb in re.findall(r"[\w:-]+-\[[^\]]+\]", m.group(1)):
                        cand["Tailwind arbitrary value (one-off outside the scale)"].append(f"{f}:{line_of(text, m.start())} {arb}")

    # ----- rule-level CSS candidates -----
    page_bg = (1, 1, 1, 1.0)
    bg_by_sel = {}
    color_by_sel = {}
    for f, ln, sel, d in rules:
        if "color" in d and parse_color(d["color"]):
            for s in sel.split(","):
                color_by_sel[s.strip()] = parse_color(d["color"])
        bg = d.get("background-color") or d.get("background")
        if bg:
            cm = COLOR_RE.search(bg)
            c = parse_color(cm.group(0)) if cm else None
            if c:
                for s in sel.split(","):
                    bg_by_sel[s.strip()] = c
                if re.fullmatch(r"(html|body)", sel.strip()):
                    page_bg = c
    for f, ln, sel, d in rules:
        if "color" in d:
            fg = parse_color(d["color"])
            if fg:
                own = d.get("background-color") or d.get("background")
                cm = COLOR_RE.search(own) if own else None
                bg, how = (parse_color(cm.group(0)), "own background") if cm else (None, "")
                if bg is None:
                    first = sel.split(",")[0].strip().split(" ")
                    for i in range(len(first) - 1, 0, -1):
                        anc = " ".join(first[:i])
                        if anc in bg_by_sel:
                            bg, how = bg_by_sel[anc], f"background of '{anc}'"
                            break
                assumed = bg is None
                if assumed:
                    bg, how = page_bg, "ASSUMED page background - verify"
                r = contrast(fg, bg)
                # assumed + near-identical = e.g. white button text whose real fill is set by another class
                if r < 4.5 and not (assumed and r < 1.3):
                    cand["text contrast below 4.5:1 (3:1 is enough only for large text)"].append(f"{f}:{ln} {sel}  {r:.2f}:1 on {how}")
        elif d.get("background-color") or d.get("background"):
            # modifier class with its own fill (.btn-green): text color usually comes from the base class (.btn)
            own = d.get("background-color") or d.get("background")
            cm = COLOR_RE.search(own)
            bg = parse_color(cm.group(0)) if cm else None
            bm = re.fullmatch(r"(\.[A-Za-z][\w]*?)[-_]{1,2}[\w-]+", sel.strip())
            base_fg = color_by_sel.get(bm.group(1)) if (bg and bm) else None
            if base_fg:
                r = contrast(base_fg, bg)
                if r < 4.5:
                    cand["text contrast below 4.5:1 (3:1 is enough only for large text)"].append(
                        f"{f}:{ln} {sel}  {r:.2f}:1 (text color inherited from '{bm.group(1)}')")
        up = d.get("text-transform", "").lower() == "uppercase"
        if up and "letter-spacing" not in d:
            cand["uppercase without letter-spacing"].append(f"{f}:{ln} {sel}")
        ta = d.get("text-align", "").lower()
        if ta == "center":
            cand["centered text (fine for short blocks only - check length)"].append(f"{f}:{ln} {sel}")
        if ta == "justify" and "hyphens" not in d:
            cand["justified text without hyphens"].append(f"{f}:{ln} {sel}")
        w = d.get("width", "")
        if w.endswith("%") and w != "100%" and re.search(r"side|aside|nav|rail|drawer", sel, re.I):
            cand["percent-width sidebar/nav (usually should be fixed)"].append(f"{f}:{ln} {sel} width:{w}")
        fs = d.get("font-size", "")
        if re.fullmatch(r"[\d.]+(em|%)", fs):
            cand["font-size in em/% (nests off-scale)"].append(f"{f}:{ln} {sel} {fs}")
        fw = d.get("font-weight", "")
        if fw.isdigit() and int(fw) < 400 or fw in ("lighter",):
            cand["font-weight under 400"].append(f"{f}:{ln} {sel} {fw}")
        if re.search(r"(^|[\s,])(#000(000)?|black)\b", d.get("color", ""), re.I):
            cand["pure black text"].append(f"{f}:{ln} {sel}")
        sh = d.get("box-shadow", "")
        sm = re.match(r"\s*(?:inset\s+)?(-?[\d.]+)(?:px)?\s+(-?[\d.]+)(?:px)?", sh)
        if sm and sh != "none" and "inset" not in sh and (float(sm.group(2)) < 0 or abs(float(sm.group(1))) > 1):
            cand["shadow not cast from above (x offset or negative y)"].append(f"{f}:{ln} {sel} {sh}")
        lh = d.get("line-height", "")
        if re.fullmatch(r"[\d.]+", lh) and float(lh) < 1.4 and re.search(r"^(html|body|p|li|\.?(text|body|copy|prose))", sel, re.I):
            cand["tight line-height on body text"].append(f"{f}:{ln} {sel} {lh}")
        # "you are here": an active/current state that barely differs from its siblings
        st = re.search(r"(\.(?:active|current|selected|is-active|is-current)|\[aria-current[^\]]*\])\s*$", sel)
        if st:
            base_sel = sel[:st.start()].strip()
            base_fg = color_by_sel.get(base_sel)
            act_fg = parse_color(d["color"]) if "color" in d else None
            other_cues = [k for k in d if k in ("font-weight", "background", "background-color", "border", "border-bottom",
                                                "border-left", "box-shadow", "text-decoration", "outline")]
            if act_fg and base_fg and not other_cues:
                ratio = contrast(act_fg, base_fg)
                if ratio < 1.5:
                    cand["'you are here' state barely differs from the other items (needs two clear cues)"].append(
                        f"{f}:{ln} {sel}: only the color changes, {ratio:.2f}:1 against '{base_sel}'")
            elif not d or (len(d) == 1 and act_fg and base_fg and contrast(act_fg, base_fg) < 1.5):
                cand["'you are here' state barely differs from the other items (needs two clear cues)"].append(f"{f}:{ln} {sel}")

    def used_in(sel):
        names = re.findall(r"\.([A-Za-z_][\w-]*)", sel.split(",")[0])
        if not names:
            return ""
        pages = set.intersection(*[class_use.get(n, set()) for n in names]) if all(n in class_use for n in names) else set()
        if not pages:
            return "  [class not found in scanned markup]"
        return "  [used in: " + ", ".join(sorted(pages)) + "]"

    for key, items in cand.items():
        if key.startswith("_"):
            continue
        for i, it in enumerate(items):
            m = re.match(r"(\S+\.(?:css|scss|less|vue|svelte|html|htm|astro):\d+) (\S.*?)(  .*)?$", it) if isinstance(it, str) else None
            if m and "." in m.group(2) and "<" not in m.group(2):
                items[i] = it + used_in(m.group(2))

    # ---------- report ----------
    def show(counter, label, note=""):
        vals = sorted(counter.items(), key=lambda kv: (-kv[1], kv[0]))
        print(f"\n{label}: {len(vals)} distinct{note}")
        print("  " + ", ".join(f"{v} x{n}" for v, n in vals[:60]) + (f", +{len(vals) - 60} more" if len(vals) > 60 else ""))

    print(f"ui-ux scan: {len(files)} files under {base.replace(os.sep, '/')}")
    print("=" * 72)
    if not rules and utility_codebase:
        print("STYLESHEET VALUES: no CSS rules found. This is a utility-class codebase: the values live in class")
        print("names. Use the UTILITY-CLASS VALUES block below for 'System health'.")
    else:
        print("SYSTEM VALUES (enumerated; quote these counts in 'System health')")
        show(sizes, "font-size")
        show(weights, "font-weight")
        show(leadings, "line-height")
        greys = [c for c in colors if (p := parse_color(c.split("@")[0])) and max(p[:3]) - min(p[:3]) < 0.04]
        show(colors, "colors", f" ({len(greys)} neutral greys; hex normalized, alpha shown as @a)")
        show(spacing, "margin/padding/gap values")
        show(shadows, "box-shadow")
        show(radii, "border-radius")
        print(f"\nborder declarations: {borders}   custom properties (tokens) defined: {tokens}   @media queries: {media}")
        print(f"declarations using var(): {var_uses}   using raw values: {raw_uses}")
        pseudo = Counter()
        for _f, _ln, sel, _d in rules:
            for ps in re.findall(r":(hover|focus-visible|focus-within|focus|active|disabled)\b", sel):
                pseudo["focus" if ps.startswith("focus") else ps] += 1
        print("interactive state rules: " + ", ".join(f":{k} x{pseudo.get(k, 0)}" for k in ("hover", "focus", "active", "disabled")))
        if not utility_codebase:
            if not pseudo.get("focus"):
                print("  -> no :focus/:focus-visible styles: check that keyboard focus is visible")
            if not pseudo.get("hover"):
                print("  -> no :hover styles: check that interactive elements respond")
            if media == 0:
                print("  -> no media queries: check small-screen behaviour")
        if tokens == 0 and not utility_codebase:
            print("  -> no design tokens / CSS variables found")
        elif var_uses:
            print("  -> token-based styles: judge the system by the token definitions; raw values above are the leftovers")

    print("\n" + "=" * 72)
    print("CANDIDATES (confirm each by reading the code; not findings yet)")
    titles = cand.pop("_titles", [])
    stubs = cand.pop("_stubs", [])
    for key in sorted(cand):
        items = cand[key]
        print(f"\n[{len(items)}] {key}")
        for it in items[:a.max]:
            print("   " + it)
        if len(items) > a.max:
            print(f"   +{len(items) - a.max} more")
    if titles:
        print("\n<title> per page (should name the screen and match what was clicked):")
        for f, t in titles:
            print(f"   {f}: {t}")
    if stubs:
        print("\nFixture/stub links (do NOT report as design findings unless they ship): " + "; ".join(stubs))
    if utility_codebase and scan_tailwind:
        try:
            scan_tailwind.report(a.paths, rel)
        except Exception as exc:
            print(f"\n(utility-class pass skipped: {exc})")
    try:
        import scan_words
        scan_words.report(a.paths, rel)
    except Exception as exc:  # the words pass must never break the main scan
        print(f"\n(words-and-navigation pass skipped: {exc})")
    print("\nNot covered by either pass: whether the hierarchy is right, states, responsive layout, inherited")
    print("backgrounds beyond one ancestor, images' real content, and whether anyone can actually finish the task.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
