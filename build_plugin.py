#!/usr/bin/env python3
"""Release helper for the plugin. The source of truth is ./plugins/ui-ux/ itself: edit it directly.

Writes  ./plugins/ui-ux/.claude-plugin/plugin.json  and  ./.claude-plugin/marketplace.json  (version, descriptions)
Checks  docs and manifests are ASCII, no machine-specific paths ship, every entry skill points at the main skill

Run:  python build_plugin.py            (idempotent; never copies or deletes plugin files)
Bump VERSION when you publish: installed users only receive updates when the version changes.
"""
import io
import json
import os
import sys

VERSION = "1.1.0"
HERE = os.path.dirname(os.path.abspath(__file__))
PLUGIN = os.path.join(HERE, "plugins", "ui-ux")
MAIN = "design"            # main skill name inside the plugin  ->  /ui-ux:design
AUTHOR = {"name": "somasuraj", "url": "https://github.com/somasuraj"}
KEYWORDS = ["ui", "ux", "design", "usability", "accessibility", "audit", "refactor", "design-tokens", "tailwind"]
DESC = ("Create, refactor, and audit app UI/UX with principles from Refactoring UI and Don't Make Me Think: "
        "a design skill with checklists, tokens and recipes, scanner / screenshot / contrast / report and refactor-fidelity scripts, "
        "five commands, and a ui-ux-designer agent.")


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with io.open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def main():
    if not os.path.isfile(os.path.join(PLUGIN, "skills", MAIN, "SKILL.md")):
        sys.exit("main skill not found: " + os.path.join(PLUGIN, "skills", MAIN, "SKILL.md"))

    # ---- manifests ---------------------------------------------------------------------
    manifest = {"name": "ui-ux", "displayName": "UI/UX Design Toolkit", "version": VERSION, "description": DESC,
                "author": AUTHOR, "license": "MIT", "keywords": KEYWORDS}
    write(os.path.join(PLUGIN, ".claude-plugin", "plugin.json"), json.dumps(manifest, indent=2) + "\n")
    market = {"name": "ui-ux-marketplace", "owner": AUTHOR,
              "description": "UI/UX design toolkit for Claude Code: create, refactor, and audit interfaces with measurable checks.",
              "plugins": [{"name": "ui-ux", "source": "./plugins/ui-ux", "description": DESC, "version": VERSION,
                           "category": "design", "keywords": KEYWORDS}]}
    write(os.path.join(HERE, ".claude-plugin", "marketplace.json"), json.dumps(market, indent=2) + "\n")

    # ---- sanity ------------------------------------------------------------------------
    bad = []
    for root, _d, names in os.walk(PLUGIN):
        if "__pycache__" in root:
            continue
        for n in names:
            p = os.path.join(root, n)
            rel = os.path.relpath(p, HERE)
            s = io.open(p, encoding="utf-8", errors="replace").read()
            if n.endswith((".md", ".json")) and any(ord(c) > 127 for c in s):  # scripts may match symbols like EUR
                bad.append(rel + ": non-ASCII")
            if n != "plugin.json" and (AUTHOR["name"] in s or "C:\\Users" in s or "/c/Users" in s or "/Users/" in s):
                bad.append(rel + ": machine-specific path or name")
            if n == "SKILL.md" and os.path.basename(root) != MAIN and ("ui-ux:" + MAIN) not in s:
                bad.append(rel + ": entry skill does not point at ui-ux:" + MAIN)
    n_files = sum(len(f) for r, _d, f in os.walk(PLUGIN) if "__pycache__" not in r)
    print("checked", os.path.relpath(PLUGIN, HERE), "-", n_files, "files, version", VERSION)
    for b in bad:
        print("PROBLEM", b)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
