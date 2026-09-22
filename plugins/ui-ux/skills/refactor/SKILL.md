---
name: refactor
description: Improve an existing UI: audit it, then apply the highest-impact visual and usability fixes
argument-hint: "[path | screen | component] [optional focus, e.g. spacing, hierarchy, color]"
disable-model-invocation: true
---

Run the `ui-ux:design` skill in **refactor** mode.

Input: $ARGUMENTS

Invoke it with the Skill tool (skill `ui-ux:design`, args: `refactor $ARGUMENTS`). If the Skill tool is unavailable, read `${CLAUDE_PLUGIN_ROOT}/skills/design/SKILL.md` and follow it; it lists the reference files and scripts each mode needs.

Rules for this command:
- Snapshot the UI source first; start with a condensed audit and list what you will fix.
- Keep functionality and information. Labels you can't interpret are kept and flagged, not deleted. No invented features, placeholder buttons, or unsourced claims. Don't silently change meaning.
- Use the project's tokens, components, and conventions; add only the tokens you use.
- Do the ambition pass with existing data only, then verify: `scan.py`, `contrast.py`, after-screenshots at desktop and 400px, and `check_refactor.py --before <snapshot> --after <ui dir>`.
- Report what changed and why, what you left alone, and open questions for the owner.
