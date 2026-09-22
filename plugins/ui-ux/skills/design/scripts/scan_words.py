#!/usr/bin/env python3
"""Words-and-navigation pass for the ui-ux scanner (called by scan.py; can also run alone).
Standard library only.

Turns usability judgment items into CANDIDATES with file:line, so they are not forgotten:
  - link text that does not match the name (title / h1) of the page it leads to
  - pages sharing one <title>, or a <title> that does not name the screen
  - several solid (filled) buttons competing on one screen
  - vague control labels (Submit, Click here, Learn more, Let's go, OK ...)
  - long paragraphs near the top of a screen or above a form (happy talk / instructions?)
  - "Welcome to ..." filler
  - exclamation-mark shouting
  - costs, fees, taxes, limits written in small or low-contrast text
  - brand / logo pushed away from the top-left by CSS
  - many links before the content starts (utilities overload)
  - breadcrumbs using "/" or acting as the page heading
A candidate is a lead, not a finding: read the screen and decide.

Usage: python scan_words.py <dir-or-file> [more ...]
"""
import html
import os
import re
import sys
from collections import defaultdict

MARKUP = {".html", ".htm", ".jsx", ".tsx", ".vue", ".svelte", ".astro"}
STYLES = {".css", ".scss", ".less"}
SKIP = {"node_modules", "dist", "build", ".git", "vendor", ".next", "out", "coverage", ".cache"}
VAGUE = {"submit", "click here", "here", "learn more", "read more", "more", "let s go", "lets go", "go", "ok", "okay",
         "continue", "next", "get started", "start", "yes", "no", "send", "details", "info"}
QUIET = re.compile(r"secondary|outline|ghost|link|tertiary|text|quiet|subtle|plain|muted", re.I)
STOP = {"the", "a", "an", "to", "of", "for", "and", "your", "my", "our", "in", "on", "with", "new", "all", "view", "see",
        "go", "open", "manage", "page"}
MONEY = re.compile(r"\b(fees?|tax(es)?|charges?|surcharge|per (month|user|payment|seat|transaction)|exclud\w*|"
                   r"billed|renews?|auto-?renew\w*|minimum|limits?|restocking|shipping|interest)\b", re.I)


def collect(paths):
    out = []
    for p in paths:
        if os.path.isfile(p):
            out.append(p)
            continue
        for base, dirs, names in os.walk(p):
            dirs[:] = [d for d in dirs if d not in SKIP and not d.startswith(".")]
            out += [os.path.join(base, n) for n in names if os.path.splitext(n)[1].lower() in MARKUP | STYLES]
    return sorted(out)


def strip(markup):
    t = re.sub(r"<(script|style)\b.*?</\1>", " ", markup, flags=re.S | re.I)
    return " ".join(html.unescape(re.sub(r"<[^>]+>", " ", t)).split())


def words(s):
    return {w for w in re.sub(r"[^a-z0-9]+", " ", s.lower()).split() if w not in STOP and len(w) > 1}


def stem(w):
    return re.sub(r"(ing|es|s)$", "", w)


def line_of(text, pos):
    return text.count("\n", 0, pos) + 1


def lum(rgb):
    def f(v):
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(rgb[0]) + 0.7152 * f(rgb[1]) + 0.0722 * f(rgb[2])


def hexrgb(s):
    m = re.fullmatch(r"#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})", s.strip())
    if not m:
        return None
    h = m.group(1)
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


def report(paths, rel=None):
    files = collect(paths)
    rel = rel or (lambda p: os.path.basename(p))
    css = {}
    for p in files:
        ext = os.path.splitext(p)[1].lower()
        text = open(p, encoding="utf-8", errors="replace").read()
        blocks = [text] if ext in STYLES else re.findall(r"<style[^>]*>(.*?)</style>", text, flags=re.S | re.I)
        for b in blocks:
            b = re.sub(r"/\*.*?\*/", " ", b, flags=re.S)
            for m in re.finditer(r"([^{};]+)\{([^{}]*)\}", b):
                decl = {}
                for d in m.group(2).split(";"):
                    if ":" in d:
                        k, v = d.split(":", 1)
                        decl[k.strip().lower()] = v.strip()
                for sel in m.group(1).split(","):
                    css.setdefault(" ".join(sel.split()), {}).update(decl)

    def class_decl(cls):
        """Merged declarations of every rule whose last compound selector mentions .cls"""
        out = {}
        for sel, d in css.items():
            last = sel.split(" ")[-1]
            if re.search(r"\." + re.escape(cls) + r"(?![\w-])", last):
                out.update(d)
        return out

    def is_solid(classes):
        if any(QUIET.search(c) for c in classes):
            return False
        bg = None
        for c in classes:
            d = class_decl(c)
            v = d.get("background-color") or d.get("background")
            if v:
                bg = v
        if not bg or re.search(r"transparent|none|var\(--(surface|white|bg)", bg, re.I):
            return False
        m = re.search(r"#[0-9a-fA-F]{3,6}\b", bg)
        rgb = hexrgb(m.group(0)) if m else None
        return not (rgb and lum(rgb) > 0.8)  # near-white fills are not "solid"

    pages = {}
    for p in files:
        if os.path.splitext(p)[1].lower() in MARKUP:
            pages[p] = open(p, encoding="utf-8", errors="replace").read()
    cand = defaultdict(list)
    names = {}
    for p, t in pages.items():
        if os.path.splitext(p)[1].lower() not in (".html", ".htm"):
            continue  # components have no <title>; only real documents are compared
        title = re.search(r"<title>(.*?)</title>", t, flags=re.S | re.I)
        h1 = re.search(r"<h1\b[^>]*>(.*?)</h1>", t, flags=re.S | re.I)
        names[os.path.basename(p).lower()] = (strip(title.group(1)) if title else "", strip(h1.group(1)) if h1 else "")

    # titles
    by_title = defaultdict(list)
    for f, (title, _h) in names.items():
        by_title[title.lower()].append(f)
    for title, fs in by_title.items():
        if len(fs) > 1:
            cand["pages share one <title> (each screen needs its own name)"].append(f'"{title}": ' + ", ".join(sorted(fs)))

    for p, t in pages.items():
        f = rel(p)
        body = re.sub(r"<(script|style)\b.*?</\1>", lambda m: " " * len(m.group(0)), t, flags=re.S | re.I)

        # link text vs target page name
        for m in re.finditer(r"<a\b([^>]*)>(.*?)</a>", body, flags=re.S | re.I):
            href = re.search(r"\bhref\s*=\s*[\"']([^\"'#?]+)", m.group(1), re.I)
            label = strip(m.group(2))
            if not href or not label:
                continue
            target = os.path.basename(href.group(1)).lower()
            if target not in names or target == os.path.basename(p).lower():
                continue
            title, h1 = names[target]
            lw = {stem(w) for w in words(label)}
            tw = {stem(w) for w in words(title + " " + h1)}
            brandish = {stem(w) for w in words(" ".join(n[0] for n in names.values()))} if len(names) > 1 else set()
            common = lw & tw
            shared_everywhere = {w for w in common if all(w in {stem(x) for x in words(n[0] + " " + n[1])} for n in names.values())}
            if lw and not (common - shared_everywhere) and label.lower() not in ("home",) and not (lw <= brandish and len(lw) == 1 and target.startswith("index")):
                cand["link text does not match the name of the page it opens (ask too: is the label itself a plain, obvious word?)"].append(
                    f'{f}:{line_of(t, m.start())} "{label}" -> {target} (title "{title}", h1 "{h1 or "none"}")')

        # solid buttons per screen
        solid = []
        for m in re.finditer(r"<(a|button)\b[^>]*class\s*=\s*[\"']([^\"']+)[\"'][^>]*>(.*?)</\1>", body, flags=re.S | re.I):
            classes = m.group(2).split()
            if any(re.search(r"btn|button|cta", c, re.I) for c in classes) and is_solid(classes):
                solid.append((line_of(t, m.start()), strip(m.group(3))))
        if len(solid) >= 3:
            cand["several solid (filled) buttons on one screen: which is THE primary action?"].append(
                f"{f}: {len(solid)} solid buttons: " + ", ".join(f'"{s}"@{ln}' for ln, s in solid[:8]))

        # vague labels
        for m in re.finditer(r"<(a|button)\b[^>]*>(.*?)</\1>|<input\b[^>]*type\s*=\s*[\"']submit[\"'][^>]*value\s*=\s*[\"']([^\"']+)",
                             body, flags=re.S | re.I):
            label = strip(m.group(2) or m.group(3) or "")
            key = re.sub(r"[^a-z]+", " ", label.lower()).strip()
            if key in VAGUE:
                cand["vague control label (say what happens)"].append(f'{f}:{line_of(t, m.start())} "{label}"')

        # long paragraphs early or above a form
        form_pos = [m.start() for m in re.finditer(r"<form\b", body, re.I)]
        n_par = 0
        for m in re.finditer(r"<p\b[^>]*>(.*?)</p>", body, flags=re.S | re.I):
            n_par += 1
            txt = strip(m.group(1))
            wc = len(txt.split())
            above_form = any(0 < fp - m.end() < 1500 for fp in form_pos)
            if wc >= 40 and (n_par <= 4 or above_form):
                why = "above a form: instructions nobody reads?" if above_form else "near the top: happy talk?"
                cand["long paragraph where people scan (cut it)"].append(f'{f}:{line_of(t, m.start())} {wc} words, {why} "{txt[:60]}..."')
        for m in re.finditer(r">\s*(Welcome to[^<]{0,60})", body, re.I):
            cand['"Welcome to ..." filler instead of saying what this is'].append(f'{f}:{line_of(t, m.start())} "{strip(m.group(1))}"')

        # shouting
        if os.path.splitext(p)[1].lower() in (".html", ".htm"):
            bangs = strip(body).count("!")
        else:  # in component files count only "!" inside text nodes and string literals, never JS operators
            texty = re.findall(r">([^<>{}]*)<", body) + re.findall(r"[\"'`]([^\"'`\n]{3,})[\"'`]", body)
            bangs = sum(len(re.findall(r"\w!(?=\s|$|[\"'<)])", s + " ")) for s in texty)
        if bangs >= 4:
            cand["exclamation-mark shouting (ask too: should all these promos/messages exist at all?)"].append(f"{f}: {bangs} exclamation marks")

        # error text that is always in the markup
        for m in re.finditer(r"<(\w+)\b([^>]*class\s*=\s*[\"'][^\"']*\b(?:err|error|errors|alert-danger|invalid-feedback)\b[^\"']*[\"'][^>]*)>([^<]{3,200})<",
                             body, flags=re.S | re.I):
            if not re.search(r"\bhidden\b|aria-live|display\s*:\s*none|role\s*=\s*[\"']alert", m.group(2), re.I):
                cand["error message always present in the markup (generic? tied to a field? shown before any mistake?)"].append(
                    f'{f}:{line_of(t, m.start())} "{" ".join(m.group(3).split())[:70]}"')

        # choosers that make people classify themselves
        for m in re.finditer(r">\s*((?:which|what)\s+(?:one|type|kind)[^<]{0,40}\?|(?:are you|i am)\s+an?[^<]{0,30}\??)\s*<", body, re.I):
            cand["up-front self-classification choice (does it need thought? is it needed at all?)"].append(
                f'{f}:{line_of(t, m.start())} "{strip(m.group(1))}"')

        # costs in small or faint text
        for m in re.finditer(r"<(\w+)\b[^>]*class\s*=\s*[\"']([^\"']+)[\"'][^>]*>([^<]{0,400})", body, flags=re.S | re.I):
            txt = " ".join(m.group(3).split())
            if not MONEY.search(txt) or not re.search(r"\d", txt):
                continue
            d = {}
            for c in m.group(2).split():
                d.update(class_decl(c))
            size = re.match(r"([\d.]+)px", d.get("font-size", ""))
            rgb = hexrgb(d.get("color", "")) if d.get("color") else None
            small = size and float(size.group(1)) <= 12
            faint = rgb is not None and (1.05) / (lum(rgb) + 0.05) < 4.5
            if small or faint:
                why = ", ".join(x for x in ("small text " + d.get("font-size", "") if small else "", "low contrast " + d.get("color", "") if faint else "") if x)
                cand["cost / fee / limit written in small or faint text"].append(f'{f}:{line_of(t, m.start())} ({why}) "{txt[:80]}"')

        # links before content
        cut = re.search(r"<main\b|<h1\b|class\s*=\s*[\"'][^\"']*(hero|content|main)", body, re.I)
        head = body[:cut.start()] if cut else body[:3000]
        n_links = len(re.findall(r"<a\b", head, re.I))
        if n_links >= 12:
            cand["many links before the content starts (utilities should be 4 to 5, quieter than sections)"].append(f"{f}: {n_links} links in the header area")

        # breadcrumbs
        for m in re.finditer(r"<(\w+)\b[^>]*class\s*=\s*[\"']([^\"']*(?:crumb)[^\"']*)[\"'][^>]*>(.*?)</\1>", body, flags=re.S | re.I):
            txt = strip(m.group(3))
            d = {}
            for c in m.group(2).split():
                d.update(class_decl(c))
            notes = []
            if " / " in txt and ">" not in txt:
                notes.append('uses "/" separators (convention is ">")')
            size = re.match(r"([\d.]+)px", d.get("font-size", ""))
            if (size and float(size.group(1)) >= 16) or d.get("font-weight", "") in ("700", "bold", "600"):
                notes.append("styled large/bold: breadcrumbs are a small accessory, not the screen name")
            if "<a" not in m.group(3).lower():
                notes.append("levels are not links")
            if notes:
                cand["breadcrumb conventions"].append(f"{f}:{line_of(t, m.start())} " + "; ".join(notes))

    # brand pushed away by CSS
    for sel, d in css.items():
        if re.search(r"brand|logo|site-?id", sel, re.I):
            order = d.get("order", "0")
            if (order.lstrip("-").isdigit() and int(order) > 0) or d.get("margin-left") == "auto" or d.get("float") == "right":
                cand["brand / logo moved away from the top-left by CSS"].append(f"{sel} {{ order:{d.get('order', '-')}; margin-left:{d.get('margin-left', '-')}; float:{d.get('float', '-')} }}")

    print("\n" + "=" * 72)
    print("WORDS AND NAVIGATION CANDIDATES (judgment items; read the screen, then decide)")
    if not cand:
        print("\n(none)")
    for key in sorted(cand):
        print(f"\n[{len(cand[key])}] {key}")
        for it in cand[key][:25]:
            print("   " + it)
        if len(cand[key]) > 25:
            print(f"   +{len(cand[key]) - 25} more")
    print("\nStill yours to judge: is it obvious what this is and where to start? are names plain? are choices mindless?")
    print("is the top task easy? is anything hidden that people want (prices, contact)? what would you cut?")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    report(sys.argv[1:])
