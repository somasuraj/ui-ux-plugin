#!/usr/bin/env python3
"""Build the distributable Claude Code plugin from the working copy in ~/.claude.

Reads   ~/.claude/skills/ui-ux           (skill, references, scripts)
Writes  ./plugins/ui-ux/                 (the installable plugin)
        ./.claude-plugin/marketplace.json (so this repo is its own marketplace)

Run:  python build_plugin.py            (idempotent; rewrites the plugin folder)
"""
import io
import json
import os
import re
import shutil
import sys

VERSION = "1.0.0"
HERE = os.path.dirname(os.path.abspath(__file__))
HOME = os.path.expanduser("~")
SRC_SKILL = os.path.join(HOME, ".claude", "skills", "ui-ux")
PLUGIN = os.path.join(HERE, "plugins", "ui-ux")
MAIN = "design"            # main skill name inside the plugin  ->  /ui-ux:design
AUTHOR = {"name": "somasuraj", "url": "https://github.com/somasuraj"}


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    assert all(ord(c) < 128 for c in text), "non-ASCII in " + path
    with io.open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def main():
    if not os.path.isfile(os.path.join(SRC_SKILL, "SKILL.md")):
        sys.exit("source skill not found: " + SRC_SKILL)
    if os.path.isdir(PLUGIN):
        shutil.rmtree(PLUGIN)

    # ---- main skill: copy, then make it portable --------------------------------------
    dst = os.path.join(PLUGIN, "skills", MAIN)
    shutil.copytree(SRC_SKILL, dst, ignore=shutil.ignore_patterns("__pycache__", "*.pyc", "*.png", "shots*", "ui-shots"))
    p = os.path.join(dst, "SKILL.md")
    t = io.open(p, encoding="utf-8").read()
    t = re.sub(r"(?m)^name: ui-ux$", "name: " + MAIN, t, count=1)
    old = "`<skill-dir>` below is this skill's base directory (shown when the skill loads; otherwise `~/.claude/skills/ui-ux`). Read reference files by absolute path."
    new = ("`<skill-dir>` below is this skill's own directory: `${CLAUDE_SKILL_DIR}` (also shown as the base directory when the "
           "skill loads). Read reference files by absolute path, for example `${CLAUDE_SKILL_DIR}/references/core-card.md`, and run "
           "scripts as `python \"${CLAUDE_SKILL_DIR}/scripts/scan.py\" <dir>` (use `python3` where `python` is not available; Python 3.8+).")
    assert old in t, "SKILL.md anchor changed"
    t = t.replace(old, new)
    write(p, t)
    for root, _d, names in os.walk(dst):
        for n in names:
            if n.endswith(".md") and n != "SKILL.md":
                fp = os.path.join(root, n)
                s = io.open(fp, encoding="utf-8").read()
                s = s.replace("by default `~/.claude/skills/ui-ux`", "`${CLAUDE_SKILL_DIR}` in SKILL.md")
                write(fp, s)

    # ---- thin user-invoked entry points (the former slash commands) -------------------
    entry = {
        "analyze": ("Audit the UI/UX of a screen, flow, or whole app (read-only) and report prioritized fixes",
                    "[path | screen | URL | blank for whole app]",
                    "analyze",
                    ["Don't modify the project's files (writing the report to a file is fine if asked).",
                     "Run the skill's `scan.py` first and render the screens with its `screenshot.py` (or a URL) so the audit isn't code-only; if rendering is impossible say so and still compute contrast from the code.",
                     "Cover every screen in scope; disposition every scanner candidate.",
                     "Output the skill's report format and pass `check_report.py` before delivering.",
                     "For a whole multi-screen app you may delegate to the `ui-ux-designer` agent and relay its report."]),
        "refactor": ("Improve an existing UI: audit it, then apply the highest-impact visual and usability fixes",
                     "[path | screen | component] [optional focus, e.g. spacing, hierarchy, color]",
                     "refactor",
                     ["Snapshot the UI source first; start with a condensed audit and list what you will fix.",
                      "Keep functionality and information. Labels you can't interpret are kept and flagged, not deleted. No invented features, placeholder buttons, or unsourced claims. Don't silently change meaning.",
                      "Use the project's tokens, components, and conventions; add only the tokens you use.",
                      "Do the ambition pass with existing data only, then verify: `scan.py`, `contrast.py`, after-screenshots at desktop and 400px, and `check_refactor.py --before <snapshot> --after <ui dir>`.",
                      "Report what changed and why, what you left alone, and open questions for the owner."]),
        "create": ("Design and build a new screen, component, or flow with strong hierarchy and self-evident usability",
                   "<what to build, for whom, and where it lives>",
                   "create",
                   ["Infer product, users, top tasks, platform, and design system from the project; ask only when it can't be inferred and would change the design.",
                    "Feature first, smallest useful version; no affordances for things that won't work. State the personality in one line.",
                    "Design every state: empty, loading, error, success, disabled, hover/focus/active, long content, 400px.",
                    "Accessible markup by default; verify like an outsider (screenshots, `scan.py`, `contrast.py`, checklist self-review)."]),
        "tokens": ("Set up or consolidate design tokens (spacing, type, color shades, shadows, radius) and replace one-off values",
                   "[optional: brand color, personality, or scope]",
                   "tokens",
                   ["Inventory with `scan.py` and show the counts.",
                    "Propose tokens in the project's own format (extend, never parallel; only what is used); show the mapping from one-off values; confirm if large; apply; verify contrast and build."]),
        "test-plan": ("Write a lightweight usability test plan (3-4 participants, tasks, facilitator script) for a screen, flow, or app",
                      "[flow or feature to test]",
                      "test-plan",
                      ["Read the product's routes/screens first so tasks match real functionality.",
                       "Produce the filled-in plan, get-it questions, 3 to 5 task scenarios in users' words, the adapted facilitator script, and an observer/debrief sheet."]),
    }
    for name, (desc, hint, mode, rules) in entry.items():
        body = ("---\nname: {n}\ndescription: {d}\nargument-hint: \"{h}\"\ndisable-model-invocation: true\n---\n\n"
                "Run the `ui-ux:{main}` skill in **{m}** mode.\n\nInput: $ARGUMENTS\n\n"
                "Invoke it with the Skill tool (skill `ui-ux:{main}`, args: `{m} $ARGUMENTS`). If the Skill tool is unavailable, read "
                "`${{CLAUDE_PLUGIN_ROOT}}/skills/{main}/SKILL.md` and follow it; it lists the reference files and scripts each mode needs.\n\n"
                "Rules for this command:\n{r}\n").format(n=name, d=desc, h=hint.replace('"', "'"), m=mode, main=MAIN,
                                                        r="\n".join("- " + x for x in rules))
        write(os.path.join(PLUGIN, "skills", name, "SKILL.md"), body)

    # ---- agent -------------------------------------------------------------------------
    a_src = os.path.join(HOME, ".claude", "agents", "ui-ux-designer.md")
    a = io.open(a_src, encoding="utf-8").read()
    a = a.replace("skills: ui-ux\n", "skills:\n  - " + MAIN + "\n", 1)
    start = a.index("## Your playbook")
    end = a.index("## How you work")
    playbook = ("## Your playbook\n\n"
                "Your method is this plugin's `" + MAIN + "` skill, normally preloaded into your context (you will see a heading "
                "\"UI/UX: create, refactor, analyze\"). If it is not there, invoke it with the Skill tool (skill `ui-ux:" + MAIN + "`) "
                "before doing anything else; it tells you where its reference files and scripts live.\n\n"
                "When preloaded, the skill's `$ARGUMENTS` line is empty: take the mode (create / refactor / analyze / tokens / test-plan) "
                "and the target from the task you were given. Then follow the skill's workflow exactly: the \"always do first\" steps, then the mode.\n\n")
    a = a[:start] + playbook + a[end:]
    a = a.replace("use the ui-ux skill directly instead", "use the ui-ux:" + MAIN + " skill directly instead")
    # a personal machine rule must not ship: never tell other people's agents to kill services
    a = re.sub(r"(?m)^- Only when you need to start a project's dev server:.*$",
               "- Only when you need to start a project's dev server: follow the project's own instructions, use a free port, "
               "and never stop services you did not start. Static files need no server.", a)
    assert "3000 to 3009" not in a, "personal port rule left in the plugin agent"
    assert "C:\\Users" not in a and "surajso" not in a, "machine-specific path left in agent"
    write(os.path.join(PLUGIN, "agents", "ui-ux-designer.md"), a)

    # ---- manifests ---------------------------------------------------------------------
    desc = ("Create, refactor, and audit app UI/UX with principles from Refactoring UI and Don't Make Me Think: "
            "a design skill with checklists, tokens and recipes, scanner / screenshot / contrast / report and refactor-fidelity scripts, "
            "five commands, and a ui-ux-designer agent.")
    manifest = {"name": "ui-ux", "displayName": "UI/UX Design Toolkit", "version": VERSION, "description": desc,
                "author": AUTHOR, "license": "MIT",
                "keywords": ["ui", "ux", "design", "usability", "accessibility", "audit", "refactor", "design-tokens", "tailwind"]}
    write(os.path.join(PLUGIN, ".claude-plugin", "plugin.json"), json.dumps(manifest, indent=2) + "\n")
    market = {"name": "ui-ux-marketplace", "owner": AUTHOR,
              "description": "UI/UX design toolkit for Claude Code: create, refactor, and audit interfaces with measurable checks.",
              "plugins": [{"name": "ui-ux", "source": "./plugins/ui-ux", "description": desc, "version": VERSION,
                           "category": "design", "keywords": manifest["keywords"]}]}
    write(os.path.join(HERE, ".claude-plugin", "marketplace.json"), json.dumps(market, indent=2) + "\n")

    # ---- sanity ------------------------------------------------------------------------
    bad = []
    for root, _d, names in os.walk(PLUGIN):
        for n in names:
            s = io.open(os.path.join(root, n), encoding="utf-8", errors="replace").read()
            if n == "plugin.json":
                continue  # the author field legitimately holds a name
            if AUTHOR["name"] in s or "C:\\Users" in s or "/c/Users" in s:
                bad.append(os.path.relpath(os.path.join(root, n), HERE))
    n_files = sum(len(f) for _r, _d, f in os.walk(PLUGIN))
    print("built", os.path.relpath(PLUGIN, HERE), "-", n_files, "files, version", VERSION)
    if bad:
        print("WARNING machine-specific paths remain in:", bad)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
