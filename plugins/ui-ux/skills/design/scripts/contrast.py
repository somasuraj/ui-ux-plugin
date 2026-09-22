#!/usr/bin/env python3
"""Contrast and perceived-brightness checker for the ui-ux skill. Standard library only.

Usage:
  python contrast.py "#1a6fe0" "#ffffff"              # contrast ratio of two colors
  python contrast.py "hsl(212 16% 46%)" white          # hsl(), rgb(), hex, white/black accepted
  python contrast.py "rgba(255,255,255,.45)" "#2456c9" # translucent foreground is composited on the background
  python contrast.py "#1fa34a" white --size 15          # font size in px gives a definite pass/fail
  python contrast.py "#1fa34a" white --size 19 --bold   # large text = 24px+, or 18.66px+ bold
  python contrast.py --pb "hsl(60 100% 50%)" "hsl(240 100% 50%)"   # perceived brightness of each color

Thresholds (WCAG 2.x AA): 4.5 normal text; 3.0 large text (>= 24px regular or >= 18.66px bold)
and 3.0 for UI component boundaries and meaningful graphics (input borders, icons, focus rings).
"""
import colorsys
import math
import re
import sys

NAMED = {"white": (1, 1, 1, 1), "black": (0, 0, 0, 1)}


def parse(s):
    s = s.strip().lower()
    if s in NAMED:
        return NAMED[s]
    if s.startswith("#"):
        h = s[1:]
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
        a = int(h[6:8], 16) / 255 if len(h) == 8 else 1
        return (r, g, b, a)
    m = re.match(r"(rgb|hsl)a?\((.*)\)", s)
    if not m:
        raise ValueError("cannot parse color: " + s)
    parts = [p for p in re.split(r"[,\s/]+", m.group(2).strip()) if p]

    def num(p, scale=1.0):
        return float(p.rstrip("%")) / (100 if p.endswith("%") else scale)

    a = num(parts[3]) if len(parts) > 3 else 1
    if m.group(1) == "rgb":
        r, g, b = (num(p, 255) for p in parts[:3])
    else:
        h = float(parts[0].replace("deg", "")) % 360 / 360
        sat, lig = num(parts[1], 100), num(parts[2], 100)
        r, g, b = colorsys.hls_to_rgb(h, lig, sat)
    return (r, g, b, a)


def over(fg, bg):
    a = fg[3]
    return tuple(fg[i] * a + bg[i] * (1 - a) for i in range(3)) + (1,)


def luminance(c):
    def f(v):
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(c[0]) + 0.7152 * f(c[1]) + 0.0722 * f(c[2])


def ratio(fg, bg):
    bg = over(bg, (1, 1, 1, 1))
    fg = over(fg, bg)
    hi, lo = sorted((luminance(fg), luminance(bg)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)


def perceived_brightness(c):
    r, g, b = (v * 255 for v in c[:3])
    return math.sqrt(0.299 * r * r + 0.587 * g * g + 0.114 * b * b) / 255


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    if argv[0] == "--pb":
        for s in argv[1:]:
            print(f"{s}: perceived brightness {perceived_brightness(parse(s)):.2f} (0 dark .. 1 bright)")
        return 0
    bold = "--bold" in argv
    argv = [x for x in argv if x != "--bold"]
    size = None
    if "--size" in argv:
        i = argv.index("--size")
        size = float(argv[i + 1].lower().replace("px", ""))
        del argv[i:i + 2]
    if len(argv) != 2:
        print(__doc__)
        return 2
    r = ratio(parse(argv[0]), parse(argv[1]))
    if size is not None:
        large = size >= 24 or (bold and size >= 18.66)
        need = 3.0 if large else 4.5
        kind = "large" if large else "normal-size"
        verdict = f"{'PASSES' if r >= need else 'FAILS'} for {kind} text at {size:g}px{' bold' if bold else ''} (needs {need}:1)"
    else:
        verdict = ("passes normal text (AA)" if r >= 4.5 else
                   "passes ONLY large text (24px+, or 18.66px+ bold) and UI boundaries (3:1); FAILS normal-size text. Use --size N [--bold] for a definite answer"
                   if r >= 3 else "FAILS text and UI-boundary contrast")
    print(f"{r:.2f}:1  {verdict}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
