#!/usr/bin/env python3
"""Headless screenshots for the ui-ux skill. Standard library only; needs Chrome, Edge, or Chromium installed.

Works with local files (no server needed) and with URLs. Use it when browser-automation tools
refuse file:// URLs or are not available.

Usage:
  python screenshot.py <file-or-url> [more ...] [--out DIR] [--width 1280] [--height 1400]
                       [--mobile] [--full] [--wait MS] [--browser PATH]

  --mobile   also capture a true 400px-wide layout of every target (suffix -mobile)
             Desktop browsers clamp the headless window to about 500px, so widths under 500 are rendered
             inside an exact-width frame; the grey band on the right of the image is outside the viewport.
             If the framed page comes out blank (the site forbids framing), use --width 500 instead.
  --full     tall viewport (4000px) to capture long pages in one image
  --wait     virtual time in ms to let the page render before the shot (default 10000). Client-rendered
             apps (React/Vue, in-browser Babel, CDN Tailwind) come out BLANK without it; raise it if needed.
  --out      output directory (default: ./ui-shots)

Examples:
  python screenshot.py index.html invoices.html --mobile --out shots
  python screenshot.py "http://localhost:5173/#/settings" "http://localhost:5173/list?state=empty" --out shots

Prints one line per image: OK <path> <bytes>, BLANK <path> (rendered empty: not a usable screenshot),
or FAIL <target> <reason>. Exit code 1 if any failed or came out blank. Then look at the PNGs with the Read tool.
"""
import argparse
import functools
import http.server
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import zlib

CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
]
ON_PATH = ["google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "chrome", "msedge", "microsoft-edge"]
MIN_WINDOW = 500  # headless Chrome/Edge on desktop will not lay out narrower than this


def find_browsers(explicit=None):
    found = []
    if explicit:
        found.append(explicit)
    found += [p for p in CANDIDATES if os.path.isfile(p)]
    found += [w for w in (shutil.which(n) for n in ON_PATH) if w]
    seen, out = set(), []
    for p in found:
        if p not in seen:
            seen.add(p)
            out.append(p)
    return out


def is_url(target):
    return re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", target) is not None


def to_url(target):
    if is_url(target):
        return target
    path, _, query = target.partition("?")
    uri = pathlib.Path(path).resolve().as_uri()
    return uri + ("?" + query if query else "")


def slug(target):
    """File name for a target. Keeps query and hash route: '.../#/shift/12' -> 'shift-12'."""
    rest = re.sub(r"^[a-zA-Z][a-zA-Z0-9+.-]*://[^/]*", "", target) if is_url(target) else target
    path, _, frag = rest.partition("#")
    path, _, query = path.partition("?")
    base = os.path.basename(path.replace("\\", "/").rstrip("/"))
    base = re.sub(r"\.html?$", "", base)
    parts = [x for x in (base, query, frag.strip("/")) if x]
    return re.sub(r"[^A-Za-z0-9._-]+", "-", "-".join(parts)).strip("-") or "page"


def looks_blank(png_path):
    """True when the image is one flat color (the page never rendered). Pure stdlib PNG read."""
    try:
        data = open(png_path, "rb").read()
        pos, idat = 8, b""
        while pos < len(data):
            length = int.from_bytes(data[pos:pos + 4], "big")
            if data[pos + 4:pos + 8] == b"IDAT":
                idat += data[pos + 8:pos + 8 + length]
            pos += 12 + length
        raw = zlib.decompress(idat)
        step = max(1, len(raw) // 200000)
        return len(set(raw[::step])) <= 4
    except Exception:
        return False


def shoot(browser, url, out_png, width, height, wait):
    """Try new headless, then legacy headless. A private profile dir avoids attaching to a running browser."""
    out_png = str(pathlib.Path(out_png).resolve())
    last = "no attempt"
    for mode in ("--headless=new", "--headless"):
        profile = tempfile.mkdtemp(prefix="uiux-shot-")
        try:
            if os.path.exists(out_png):
                os.remove(out_png)
            cmd = [browser, mode, "--disable-gpu", "--hide-scrollbars", "--no-first-run",
                   "--no-default-browser-check", "--disable-extensions",
                   f"--user-data-dir={profile}", f"--window-size={width},{height}",
                   f"--virtual-time-budget={wait}", f"--screenshot={out_png}", url]
            try:
                subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120)
            except subprocess.TimeoutExpired:
                last = "timeout"
                continue
            if os.path.isfile(out_png) and os.path.getsize(out_png) > 0:
                return None
            last = f"{mode} wrote no image"
        finally:
            shutil.rmtree(profile, ignore_errors=True)
    return last


class _Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def framed(url, width, height, tmpdir):
    """Wrapper page holding an iframe of the exact width, so media queries see the real narrow viewport.
    For http targets the wrapper is served from a throwaway local server: a file:// page cannot frame an http app."""
    path = os.path.join(tmpdir, "frame.html")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write('<!doctype html><meta charset="utf-8"><body style="margin:0;background:#ddd">'
                 f'<iframe src="{url}" style="width:{width}px;height:{height}px;border:0;'
                 'background:#fff;display:block"></iframe>')
    if not url.lower().startswith("http"):
        return pathlib.Path(path).resolve().as_uri(), None
    handler = functools.partial(_Quiet, directory=tmpdir)
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return f"http://127.0.0.1:{server.server_address[1]}/frame.html", server


def main():
    ap = argparse.ArgumentParser(add_help=True, description="Headless screenshots (Chrome/Edge/Chromium).")
    ap.add_argument("targets", nargs="+")
    ap.add_argument("--out", default="ui-shots")
    ap.add_argument("--width", type=int, default=1280)
    ap.add_argument("--height", type=int, default=1400)
    ap.add_argument("--mobile", action="store_true")
    ap.add_argument("--full", action="store_true")
    ap.add_argument("--wait", type=int, default=10000)
    ap.add_argument("--browser")
    a = ap.parse_args()

    browsers = find_browsers(a.browser)
    if not browsers:
        print("FAIL no Chrome/Edge/Chromium found; pass --browser PATH, or ask the user for screenshots")
        return 1
    os.makedirs(a.out, exist_ok=True)
    height = 4000 if a.full else a.height
    failed = False
    for t in a.targets:
        jobs = [(a.width, height, "")]
        if a.mobile:
            jobs.append((400, 4000 if a.full else 1600, "-mobile"))
        for w, h, suffix in jobs:
            png = os.path.join(a.out, f"{slug(t)}{suffix}.png")
            err, server = None, None
            tmp = tempfile.mkdtemp(prefix="uiux-frame-") if w < MIN_WINDOW else None
            url, win_w = to_url(t), w
            if tmp:
                (url, server), win_w = framed(url, w, h, tmp), w + 120
            for b in browsers:
                err = shoot(b, url, png, win_w, h, a.wait)
                if err is None:
                    break
            if server:
                server.shutdown()
            if tmp:
                shutil.rmtree(tmp, ignore_errors=True)
            if err is None and looks_blank(png):
                failed = True
                print(f"BLANK {png}  (rendered empty: is the app served over http? does it need a longer --wait? "
                      "does it forbid framing? for the mobile shot try --width 500)")
            elif err is None:
                print(f"OK {png} {os.path.getsize(png)}")
            else:
                failed = True
                print(f"FAIL {t} ({w}px): {err}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
