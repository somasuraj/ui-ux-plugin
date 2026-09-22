---
name: analyze
description: Audit the UI/UX of a screen, flow, or whole app (read-only) and report prioritized fixes
argument-hint: "[path | screen | URL | blank for whole app]"
disable-model-invocation: true
---

Run the `ui-ux:design` skill in **analyze** mode.

Input: $ARGUMENTS

Invoke it with the Skill tool (skill `ui-ux:design`, args: `analyze $ARGUMENTS`). If the Skill tool is unavailable, read `${CLAUDE_PLUGIN_ROOT}/skills/design/SKILL.md` and follow it; it lists the reference files and scripts each mode needs.

Rules for this command:
- Don't modify the project's files (writing the report to a file is fine if asked).
- Run the skill's `scan.py` first and render the screens with its `screenshot.py` (or a URL) so the audit isn't code-only; if rendering is impossible say so and still compute contrast from the code.
- Cover every screen in scope; disposition every scanner candidate.
- Output the skill's report format and pass `check_report.py` before delivering.
- For a whole multi-screen app you may delegate to the `ui-ux-designer` agent and relay its report.
