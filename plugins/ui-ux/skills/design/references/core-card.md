# Core card (one page)

The whole skill in brief. Read this first. If context is tight, read this plus `audit-checklist.md` and let the scripts do the mechanical work; open `usability-rules.md` (`UR n`) and `visual-rules.md` (`VR n`) only for the rule behind a specific finding.

## Two questions, every screen

1. **Is it obvious?** A newcomer knows what this is, what they can do, and where to start, without thinking. [UR1]
2. **Does it look designed?** One thing is clearly most important, space groups things, and values come from a system. [VR1, VR2]

## Usability in ten lines [Krug]

- Obvious names beat clever ones. Link text, page title, and heading all say the same words. [UR2, UR6.3]
- People scan and click the first plausible thing: make choices mindless, never make them classify themselves. [UR4]
- Cut happy talk and instructions; then cut again. Keep time estimates. [UR5]
- Every screen: identity top-left linking home, a screen name, visible sections, a "you are here" cue with two distinctions, search where warranted. Blur test: can you still point at each? [UR6]
- First screen answers: what is this, what's here, what can I do, why here, where do I start. Tagline by the logo; one clear entry for new users and one for returning users. [UR7]
- Forms ask only what this task needs; accept any format; errors next to the field. [UR9]
- Never hide prices, fees, limits, or contact. [UR8]
- Destructive or irreversible: keep it away from routine actions, confirm it. [VR1.9]
- Accessibility floor: labels, alt text, keyboard reach, visible focus, landmarks, measured contrast. [UR10]
- The books cover websites; for apps check a rule's premise first. [usability-rules intro]

## Visual in ten lines [Refactoring UI]

- Rank everything: primary, secondary, tertiary. De-emphasize competitors instead of shouting. [VR1.1, VR1.4]
- Weight and color before size; about 3 text colors, 2 weights, none under 400. [VR1.2, VR1.3]
- One solid primary action per screen; secondary outline; tertiary link-style; nothing repeated per row is solid. [VR1.9]
- Data: drop or fold labels ("12 left in stock"); the key fact leads. [VR1.6]
- Start with too much space; the gap around a group is at least 2x the gap inside it. [VR2.1, VR2.4]
- Scales, not one-offs: spacing 4 8 12 16 24 32 48 64..., type 12 14 16 18 20 24 30 36 48. [design-tokens]
- Content gets the width it needs: max-width, fixed sidebars, 45 to 75 characters per line. [VR2.5, VR3.3]
- Contrast 4.5:1 text, 3:1 large text and control borders; dark-on-tint badges; never color alone; no grey on color. [VR4, VR1.5]
- Shadows by elevation, light from above; fewer borders. [VR5, VR7.1]
- Design the empty, loading, error, and 400px states. [VR7.5]

## Always run the scripts

`scan.py <src>` (values + candidates + words pass + utility-class pass), `screenshot.py <pages or URLs> --mobile` then look, `contrast.py fg bg --size N`, and at the end `check_report.py` (audits) or `check_refactor.py --before --after` (refactors). Disposition every candidate: finding, or the reason it is fine. A candidate is a lead: read the screen before you believe it, and ask what it implies beyond the literal (many exclamation marks usually means too many promos).

## Severity

Critical = a top task is blocked, people are harmed or misled, or a basic accessibility barrier; write it as `Blocks: <task>` or `Harm: <what>`. Expect 5 or fewer. Failed contrast, missing landmarks, one-off values, vague copy are Major or Minor. Purely aesthetic = Minor. Merge same-cause findings.

## Refactor and create

Keep the product's real navigation, data, and functions; rename only when the target proves the meaning; never add stub features or unsourced claims; flag what you cannot interpret. Then one ambition pass: lead with the key fact and the top task, using only data that exists.

Tie-breaker: **which option makes the user think less?**
