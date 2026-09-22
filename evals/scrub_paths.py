#!/usr/bin/env python3
"""Replace machine-specific absolute paths in the evaluation material with neutral placeholders.
Run from the repo root:  python evals/scrub_paths.py <user-name>
"""
import io
import os
import re
import sys

user = re.escape(sys.argv[1]) if len(sys.argv) > 1 else r"[^\\/\s]+"
SEP = r"[\\/]+"
PATTERNS = [
    (re.compile(r"[A-Za-z]:" + SEP + "Users" + SEP + user + SEP + "AppData" + SEP + "Local" + SEP + "Temp" + SEP + "claude"
                + SEP + r"[^\\/\s`\"')]+" + SEP + r"[^\\/\s`\"')]+" + SEP + "scratchpad", re.I), "<scratch>"),
    (re.compile(r"[A-Za-z]:" + SEP + "Users" + SEP + user + SEP + r"\.claude" + SEP + "ui-ux-skill-tests", re.I), "<tests>"),
    (re.compile(r"[A-Za-z]:" + SEP + "Users" + SEP + user + SEP + r"\.claude", re.I), "~/.claude"),
    (re.compile(r"/c/Users/" + user, re.I), "~"),
    (re.compile(r"[A-Za-z]:" + SEP + "Users" + SEP + user, re.I), "~"),
    (re.compile(r"D--E-Drive-[\w-]+", re.I), "<project>"),
]
TEXT = {".md", ".txt", ".html", ".json", ".css", ".jsx", ".js"}

root = os.path.dirname(os.path.abspath(__file__))
changed = 0
for base, _dirs, names in os.walk(root):
    for name in names:
        if os.path.splitext(name)[1].lower() not in TEXT:
            continue
        path = os.path.join(base, name)
        old = io.open(path, encoding="utf-8", errors="replace").read()
        new = old
        for rx, rep in PATTERNS:
            new = rx.sub(rep, new)
        if new != old:
            io.open(path, "w", encoding="utf-8", newline="\n").write(new)
            changed += 1
print("scrubbed files:", changed)
