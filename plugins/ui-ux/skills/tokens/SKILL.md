---
name: tokens
description: Set up or consolidate design tokens (spacing, type, color shades, shadows, radius) and replace one-off values
argument-hint: "[optional: brand color, personality, or scope]"
disable-model-invocation: true
---

Run the `ui-ux:design` skill in **tokens** mode.

Input: $ARGUMENTS

Invoke it with the Skill tool (skill `ui-ux:design`, args: `tokens $ARGUMENTS`). If the Skill tool is unavailable, read `${CLAUDE_PLUGIN_ROOT}/skills/design/SKILL.md` and follow it; it lists the reference files and scripts each mode needs.

Rules for this command:
- Inventory with `scan.py` and show the counts.
- Propose tokens in the project's own format (extend, never parallel; only what is used); show the mapping from one-off values; confirm if large; apply; verify contrast and build.
