# UI/UX Design Toolkit for Claude Code

A Claude Code plugin that helps Claude **create, refactor, and audit** the UI/UX of any app. It combines two lenses, always together:

- **Does it look designed?** Hierarchy, spacing, type, color, depth, systems (principles from *Refactoring UI*).
- **Is it obvious to use?** Self-evident screens, navigation, words, goodwill, accessibility (principles from *Don't Make Me Think*).

What makes it different from "a prompt with design advice": it ships **scripts that measure**, so Claude looks at real pixels and real numbers instead of guessing, and **validators** that reject sloppy output.

## Install

```
/plugin marketplace add somasuraj/ui-ux-plugin
/plugin install ui-ux@ui-ux-marketplace
```

From a local clone instead of GitHub:

```
/plugin marketplace add /path/to/ui-ux-plugin
/plugin install ui-ux@ui-ux-marketplace
```

Try it for one session without installing: `claude --plugin-dir /path/to/ui-ux-plugin/plugins/ui-ux`

Requirements: Python 3.8+ on PATH (`python` or `python3`; standard library only). Chrome, Edge, or Chromium for screenshots (optional but strongly recommended). The design skill pre-approves only its own bundled scripts (`allowed-tools`), so they run without a permission prompt; every other command still asks. The grant lasts for the turn that invokes the skill; the `ui-ux-designer` agent (which preloads the skill instead of invoking it) may still ask, so add an allow rule for the scripts in your settings if you use the agent unattended.

## Use

| Command | What it does |
|---|---|
| `/ui-ux:analyze [path or URL]` | Read-only audit: prioritized fixes, complete findings with `file:line` evidence, coverage table, system health |
| `/ui-ux:refactor [path] [focus]` | Audits, fixes in priority order, ambition pass, then verifies and runs a fidelity check |
| `/ui-ux:create <what to build>` | Designs and builds a screen or flow with every state, accessible by default |
| `/ui-ux:tokens [brand or scope]` | Inventories one-off values, proposes and applies design tokens |
| `/ui-ux:test-plan [flow]` | Do-it-yourself usability test plan, tasks, and facilitator script |
| `/ui-ux:design <mode> ...` | The main skill; also triggers on its own when you ask for UI work in plain words |

For whole-app or multi-screen work: "use the ui-ux-designer agent to audit this app". The agent has the skill preloaded.

## What is inside

```
plugins/ui-ux/
  skills/design/                 main skill
    SKILL.md                     modes and workflow
    references/
      core-card.md               the whole skill on one page
      usability-rules.md         auditable rules (UR n), website-vs-app scope stated honestly
      visual-rules.md            auditable rules (VR n)
      audit-checklist.md         procedure, checklist A to H, severity anchors, report format
      measuring.md               rendering, squint/grey tests, contrast, enumerating values
      design-tokens.md           scales + a palette with every contrast pair computed
      recipes.md                 concrete CSS values and component anatomies
      design-process.md          how to design; personality; states; the ambition pass
      usability-test-script.md   lightweight usability testing
    scripts/
      scan.py                    enumerates real values; candidate issues with file:line
      scan_words.py              words-and-navigation pass (page names, vague labels, buried fees, ...)
      scan_tailwind.py           utility-class pass for Tailwind-style codebases
      screenshot.py              headless screenshots of local files or URLs, true 400px mobile
      contrast.py                WCAG ratio (with --size) and perceived brightness
      check_report.py            validates an audit report (coverage arithmetic, citations, Criticals)
      check_refactor.py          fidelity: lost navigation, changed data, stub controls, invented claims
  skills/{analyze,refactor,create,tokens,test-plan}/   thin user-invoked entry points
  agents/ui-ux-designer.md
```

## How well does it work? (measured, not claimed)

Blind tests: fresh agents that never saw the answer keys, graded by a separate neutral agent against deliberately broken apps. Full material is in `evals/`.

- **Strong model:** it already finds about 96% of planted flaws without the skill. The skill does not raise that; it adds discipline: false positives 5 -> 0, Criticals 11 -> 4 (all defensible), accurate enumerated counts, rendered screens, a coverage table that reconciles, no false praise.
- **Small model:** 30% of planted flaws found without the skill -> 57% with it, mostly because the scripts surface what it would otherwise miss.
- **Refactors:** without the skill the agent built a nicer *different* app (deleted the product's real navigation, invented six sections, changed invoice dates). With the skill it improved the *same* app, and `check_refactor.py` now enforces that.
- Honest limits: few runs per cell, synthetic fixtures, keyword-based checks can be gamed, and a heuristic review predicts problems; only watching real users confirms them.

## Develop

Edit `plugins/ui-ux/` directly; it is the source of truth. `python build_plugin.py` writes the version and descriptions into both manifests and checks that no machine-specific paths ship. Then:

```
claude plugin validate . --strict
claude plugin validate ./plugins/ui-ux --strict
```

Bump `VERSION` in `build_plugin.py` when you publish: installed users only receive updates when the version changes.

## Credits and license

Principles are distilled in the authors' own words from *Refactoring UI* (Adam Wathan and Steve Schoger) and *Don't Make Me Think*, 2nd ed. (Steve Krug). No text from either book is reproduced; buy the books, they are worth it. Anything beyond the books is tagged `[ext]` in the references. Code and text in this repository: MIT license.
