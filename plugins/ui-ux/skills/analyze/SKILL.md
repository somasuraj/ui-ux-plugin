---
name: analyze
description: Audit the UI/UX of a screen, flow, or whole app (read-only) and report prioritized fixes
argument-hint: "[path | screen | URL | blank for whole app]"
disable-model-invocation: true
---

Run the `ui-ux:design` skill in **analyze** mode.

Input: $ARGUMENTS

Invoke it with the Skill tool (skill `ui-ux:design`, args: `analyze $ARGUMENTS`). If the Skill tool is unavailable, read `${CLAUDE_PLUGIN_ROOT}/skills/design/SKILL.md` and follow it; it lists the reference files and scripts each mode needs.
