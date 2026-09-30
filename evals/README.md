# Evaluation material

How the plugin was tested, and everything needed to repeat it. None of this is installed with the plugin.

**Method.** Deliberately broken apps with private answer keys. Every tester is a fresh agent that sees only the app and the skill, never the key or earlier reports. A separate neutral agent grades each report against the key (1 = names the specific problem at the right place, 0.5 = touches the area, 0 = missed) and also counts false positives, false praise, citation accuracy, and whether each "Critical" is defensible.

| Path | What it is |
|---|---|
| `fixture1-ledgerly-html/` | Static HTML/CSS marketing + invoicing app: 53 planted flaws, 4 decoys |
| `fixture2-shiftboard-react/` | React + Tailwind in-app product (hash routed, no build step): 50 planted flaws, 5 decoys. Serve with `python -m http.server 8137` |
| `answer-keys/` | The planted flaws. **Never show these to a tester.** |
| `reports/T*`, `R2-*`, `R3-*`, `R4-*`, `R5-*`, `F2-*` | Tester reports, round by round |
| `reports/G1`, `G2`, `G3`, `G5`, `G6` | Neutral gradings |
| `reports/B1` to `B4` | Gap reviews of the skill's references against the two books (including page illustrations) |
| `side-by-side/compare.html` | Same job, same model, same prompt, without vs with the skill: open it in a browser |
| `scrub_paths.py` | Removes machine-specific paths from this folder before publishing |

## Results

### Audits, large model

| Fixture | Run | Planted flaws found | False positives | Criticals (defensible) | Findings | System-health counts |
|---|---|---|---|---|---|---|
| 1 HTML | no skill | 96.2% | 5 | 11 | 72 | none |
| 1 HTML | with skill (final round) | 96.2% | 0 | 4 (4) | 59 | all 8 correct |
| 1 HTML | with skill v1.1 (sizing, deduped rules, fast screenshots; `R6`, graded in `G7`) | 96.2% | 0 | 3 (3) | 51 | correct |
| 2 React + Tailwind | no skill | 93.0% | 4 | 11 (7) | 79 | none |
| 2 React + Tailwind | with skill | 97.0% | 0 | 4 (4) | 43 | plausible, slightly low |

A strong model finds nearly everything on its own. The skill's measurable effect is precision and calibration: no false positives, a third as many Criticals and all of them defensible, roughly half the rows for the same coverage, enumerated counts, a coverage table that reconciles, top fixes with effort and the findings they resolve.

### Audits, small model (fixture 1)

| Run | Found | Usability /25 | A11y /6 | Visual /22 | Criticals |
|---|---|---|---|---|---|
| no skill | 30.2% | 8 | 4.5 | 3.5 | 4 |
| skill, round 1 | 36.8% | 11 | 1.5 | 7 | 7 |
| skill + scanner and contrast scripts | 50.0% | 10.5 | 5 | 11 | 14 |
| skill + longer procedure text | 40.6% | 8.5 | 2.5 | 10.5 | 9 |
| skill + words-and-navigation scanner pass + report validator | 57.5% | 14 | 4.5 | 12 | 4 |

Lesson: for a small model, more instructions did not help and once hurt; scripts that surface candidates and a validator that rejects bad reports did.

### Refactors (fixture 1, large model), checked by `check_refactor.py`

| Run | Lost nav labels | Invented sections | Changed data | Stub controls | New unsourced claims |
|---|---|---|---|---|---|
| no skill | 10 (incl. the product's Hive / Pulse / Toolbox) | 5 | 4 values | 3 | 1 |
| skill before the fidelity check existed | 3 (legitimate renames) | 0 | 0 | 4 | 1 |
| skill with fidelity check and ambition pass | 3 (legitimate renames) | 0 | 0 | 0 | 0 |

Screenshots of all three are under `side-by-side/shots/`.

## Honest limits

One or two runs per cell, so differences of a few points are noise. Both fixtures are synthetic. The graders are models too. Keyword-based checks in the validators can be gamed by a careless model. Not tested: large production codebases, native mobile, RTL, non-English copy. A heuristic review predicts problems; only watching real users confirms them.

## Re-running a blind test

1. Start a fresh subagent. Do not do it yourself if you have read an answer key.
2. Prompt shape: "Invoke the ui-ux design skill with args `analyze <path to fixture>`. Only look inside that folder and the skill's folder. Save the report to <path>." For refactor, copy the fixture first and point the agent at the copy.
3. Mechanical checks: `check_report.py <report> --src <fixture>` for audits; `check_refactor.py --before <fixture> --after <copy>` for refactors.
4. Grade with a separate neutral agent, giving it the key, the fixture, the report, and one of the `G*` files as the scoring convention.
