---
name: design
description: Create, refactor, or analyze the UI/UX of any app (web, mobile, desktop) using principles from Refactoring UI and Don't Make Me Think. Use when asked to design a screen, page, component, or flow; make a UI look better, more polished, or more professional; improve, clean up, or redesign an existing interface; audit, review, or critique UI, UX, or usability; or fix visual hierarchy, spacing, layout, typography, color palette, contrast, shadows/depth, navigation, landing/home page clarity, microcopy, forms, empty states, or accessibility. Also use to set up design tokens (spacing, type, color, shadow scales) or to plan a usability test. Modes - create, refactor, analyze, tokens, test-plan.
allowed-tools:
  - Bash(python "${CLAUDE_SKILL_DIR}/scripts/*)
  - Bash(python3 "${CLAUDE_SKILL_DIR}/scripts/*)
---

# UI/UX: create, refactor, analyze

Two lenses, always together: **does it look designed** (hierarchy, spacing, type, color, depth, systems) and **is it obvious to use** (self-evident screens, navigation, words, goodwill, accessibility).

`<skill-dir>` below is this skill's own directory: `${CLAUDE_SKILL_DIR}` (also shown as the base directory when the skill loads). Read reference files by absolute path, for example `${CLAUDE_SKILL_DIR}/references/core-card.md`, and run scripts as `python "${CLAUDE_SKILL_DIR}/scripts/scan.py" <dir>` (use `python3` where `python` is not available; Python 3.8+).

| File | What it is | Read for |
|---|---|---|
| `references/core-card.md` | The whole skill on one page | **read first, every mode**; enough on its own with the checklist when context is tight |
| `references/usability-rules.md` | Auditable usability rules (`UR n`) | every mode |
| `references/visual-rules.md` | Auditable visual rules (`VR n`) | every mode |
| `references/audit-checklist.md` | Audit procedure, checklist A to H, severity anchors, report format | analyze, refactor, create self-review |
| `references/measuring.md` | Screenshots, squint/grey tests, contrast, enumerating values | whenever you need to see or measure |
| `references/design-tokens.md` | Scales and a contrast-verified palette | tokens; create/refactor when systems are missing |
| `references/recipes.md` | Concrete CSS values and component anatomies | create, refactor |
| `references/design-process.md` | How to go about designing; personality; states | create, big redesigns |
| `references/usability-test-script.md` | Do-it-yourself usability test | test-plan; audits that need verification |

Scripts (Python standard library): `scripts/scan.py` (enumerates real values; lists candidate issues with file:line: markup, accessibility, contrast, plus a words-and-navigation pass for page names, vague labels, competing solid buttons, filler text, buried fees), `scripts/screenshot.py` (headless screenshots of local files or URLs, true 400px mobile), `scripts/contrast.py` (WCAG ratio with `--size`, perceived brightness), `scripts/check_report.py` (validates an audit report: coverage arithmetic, citations, Criticals), `scripts/check_refactor.py` (fidelity: compares the UI before and after a refactor for lost navigation, changed data, stub controls, invented sections, unsourced claims).

## Pick the mode

Arguments: `$ARGUMENTS`

- First word `create`, `refactor`, `analyze`, `tokens`, or `test-plan` (aliases: design/build = create; improve/polish/fix/redesign = refactor; audit/review/critique = analyze). The rest is the target.
- No explicit mode: infer it. "What's wrong with / look at" = analyze. "Make this better" = refactor. "Build / design a ..." = create.
- Torn between analyze and refactor: analyze, present the top fixes, and change files only if changes were asked for.
- Act immediately; no greeting or menu. If you can't ask questions (running as a subagent or told not to), make sensible assumptions and state them.

## Size the job

Pick the size before reading any reference file; it decides how much of the workflow below applies. The scripts and validators run at every size (they are fast and they carry most of the quality); what scales is reading, screens covered, and optional passes.

| Size | When | Read | Run and check | Skip |
|---|---|---|---|---|
| **Small** | One component, one element, or one named property ("fix the button contrast", "tighten this card's spacing") | `core-card.md`, plus only the rules file and checklist section the task touches | `scan.py` on the touched files; one screenshot of the screen it lives on (add 400px if layout changed); `contrast.py` on any color you set; for refactors, still snapshot and run `check_refactor.py` | full A to H pass, other screens, ambition pass, formal report (answer in a few lines: what changed, rule id, what you verified) |
| **Standard** | One or two screens, or one form or flow step | `core-card.md`, both rules files, and the mode's files from the table above | the full workflow for the screens in scope, desktop and 400px | screens outside scope (list them as not covered) |
| **Full** | Whole app, several screens, a redesign, or any audit the user will share | everything the mode lists | the full workflow, every screen | nothing |

When unsure between two sizes, take the larger. Say which size you picked in one line so the user can ask for more.

## Always do first

1. **Ground truth.** Find the UI code, styles, tokens/theme, component library; identify platform and framework. Read before judging.
2. **See it and measure it** (`references/measuring.md`): run `scripts/scan.py` on the UI source and `scripts/screenshot.py` on the screens. Browser tools usually refuse `file://`; the script doesn't need a server. If you truly can't render, say so, and still compute contrast from the code.
3. **Respect what exists.** Use the project's tokens, components, and conventions. Extend; never add a parallel system or a dependency unasked.
4. **Name the top ~3 user tasks.** Everything is judged against making those obvious and easy.

Work in parallel: read the reference files you need in one turn, and run `scan.py` and `screenshot.py` in the same turn (pass every screen to one `screenshot.py` call; it shoots them concurrently).

## Mode: analyze

Follow `references/audit-checklist.md` exactly (after reading both rules files): scope, mechanical pass, see it, first-glance pass, **checklist pass on every screen in scope**, triage, report in its format.

- **Findings table = every confirmed problem**, ranked, one row per distinct problem, each with evidence, rule id, severity from the anchors, and a fix. **Top fixes = the 3 to 7 that matter most.** Both are required; kayak problems and fixture artifacts are in neither.
- The coverage table must show every screen. No screen may be silently skipped.
- Counts come from `scan.py`, contrast from `contrast.py`. Don't estimate.
- **Last step: run `scripts/check_report.py` on the saved report and fix everything it flags** before delivering.
- Note what works (never praise something the checklist fails) and what you couldn't verify.
- Don't modify the project's files. Writing the report to a file is fine when asked.
- For a whole multi-screen app you may delegate to the `ui-ux-designer` agent and relay its report.

## Mode: refactor

0. **Snapshot first.** Copy the UI source to a scratch folder before editing anything: it is the `--before` for the fidelity check.
1. **Mini-audit** (condensed analyze). List what you'll fix, in priority order. Confirm first only if the change is large or alters product behaviour and you're able to ask; otherwise proceed. If the user asked to review before implementation, publish the proposed top screen as a mockup (same way as in create mode) and wait for approval.
2. **Fix in this order:** words and clarity; hierarchy (one primary element and action per screen, demote the rest); spacing and layout; typography; color and contrast; depth and borders; states; accessibility. Use `references/recipes.md` for concrete treatments.
3. **Rules of engagement**
   - Prefer removing to adding; don't fix confusion with more explanatory text.
   - **Keep functionality and information.** Don't drop nav items, fields the task needs, or data points. If a label's meaning can't be inferred ("Hive"), keep it and flag it for the owner instead of deleting or guessing.
   - **Don't invent features.** Surfacing an existing function for a top task is fine; adding placeholder buttons for functions that don't exist is not: note the gap in your report.
   - Don't silently change meaning (which metric direction is "good", what a status implies): flag it.
   - Don't break what works: raising one element lowers another; check other screens sharing a component.
   - Tokens: when one-off values are the root cause, introduce **only the tokens you use**, named in the project's style, and replace the one-offs.
   - Focused diffs. No framework swaps or drive-by rewrites.
4. **Ambition pass** (`references/design-process.md` section 7). Correct is not the same as good: once the problems are fixed, make the top task and the key fact impossible to miss using **only data and functions that already exist** (an overdue summary built from the rows on screen, counts on existing filters, relative dates next to real dates), then apply two or three finishing touches (VR7). Stop before it becomes decoration.
5. **Verify.** Build/typecheck/lint if available; re-run `scan.py` (candidates should drop) and `contrast.py` on new color pairs; take after-screenshots at desktop and 400px and actually look at them; re-check the checklist sections you touched. Then run `python <skill-dir>/scripts/check_refactor.py --before <snapshot> --after <ui dir>`: every item it lists is either reverted or written into the report's open questions. A renamed jargon label is fine when its target proves the meaning; invented sections, stub buttons, changed data, and unsourced claims are not.
6. **Report:** what changed and why (rule ids), what you left alone on purpose, open questions for the owner, what still needs a human eye or a usability test.

## Mode: create

Read `references/design-process.md`, the two rules files, `recipes.md`, and `design-tokens.md` if the project has no system.

**Preview first, only when the user asks for one** ("show me first", "mockup", "preview before building"): once steps 1 to 5 are settled, publish a one-page HTML mockup with the sample data through an Artifact tool if one is available (otherwise write it to a scratch file and open it), share the link, and wait for approval before touching the project's code. Don't do this unasked: it adds a round trip.

1. Understand product, users, top tasks, platform, existing design system. Ask only if it can't be inferred and changes the design.
2. Feature first, smallest useful version. No affordances for things that won't work.
3. State the personality in one line (typeface, color, radius, tone).
4. Systems first: use the project's tokens, or take only what you need from `design-tokens.md`. Then choose only from them.
5. Hierarchy in greyscale thinking first; then color. One primary action per screen.
6. Self-evident: obvious names, mindless choices, minimal words, conventional patterns, navigation that works at every level. First/landing screens answer the five questions (UR7); in-app screens answer "what is this screen, what can I do here, where do I start".
7. Every state: empty, loading, error, success, disabled, hover/focus/active, long content, 400px. In a static deliverable expose states via query params or a labelled demo strip.
8. Accessible markup by default: labels, alt, keyboard, focus, landmarks, measured contrast.
9. **Ambition pass** (`references/design-process.md` section 7): lead with the key fact, make the top task unmissable, apply two or three finishing touches. Everything shown must be real or derivable from the sample data.
10. **Verify like an outsider:** screenshot it and look; run `scan.py` and `contrast.py`; self-review against checklist sections A to H for the screens you built; fix what fails.
11. Present: key decisions with rule ids, where to see each state, assumptions, what to validate with users.

## Helper mode: tokens

Read `references/design-tokens.md`. Run `scan.py` to inventory. Propose tokens in the project's format (extend, never parallel; only what's used). Show the mapping from one-off values to the nearest token, flagging visible changes; confirm if large. Apply, then verify contrast with `contrast.py` and build/lint.

## Helper mode: test-plan

Read `references/usability-test-script.md`. Read the product's routes/screens so tasks match real functionality. Produce the filled-in plan, "get it" questions, 3 to 5 task scenarios in users' words (no UI labels) with success criteria, the adapted facilitator script, and a one-page observer/debrief sheet.

## Judgment

- Strong defaults, not laws. To bend one: know which, have a reason, and test the result.
- The user's brand, design system, and platform conventions outrank this skill's example values.
- The books cover websites; applying them to apps is this skill's extension: check a rule's premise before enforcing it on an app screen.
- A heuristic review predicts problems; only watching real people confirms them.
- Tie-breaker: **which option makes the user think less?**
