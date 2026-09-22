---
name: create
description: Design and build a new screen, component, or flow with strong hierarchy and self-evident usability
argument-hint: "<what to build, for whom, and where it lives>"
disable-model-invocation: true
---

Run the `ui-ux:design` skill in **create** mode.

Input: $ARGUMENTS

Invoke it with the Skill tool (skill `ui-ux:design`, args: `create $ARGUMENTS`). If the Skill tool is unavailable, read `${CLAUDE_PLUGIN_ROOT}/skills/design/SKILL.md` and follow it; it lists the reference files and scripts each mode needs.

Rules for this command:
- Infer product, users, top tasks, platform, and design system from the project; ask only when it can't be inferred and would change the design.
- Feature first, smallest useful version; no affordances for things that won't work. State the personality in one line.
- Design every state: empty, loading, error, success, disabled, hover/focus/active, long content, 400px.
- Accessible markup by default; verify like an outsider (screenshots, `scan.py`, `contrast.py`, checklist self-review).
