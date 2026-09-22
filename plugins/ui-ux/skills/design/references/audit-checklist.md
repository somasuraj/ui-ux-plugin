# UI/UX audit: procedure, checklist, report

Used in **analyze** mode and as step 1 of **refactor**. Items are terse on purpose; the rule behind each is in `usability-rules.md` (`UR n`) or `visual-rules.md` (`VR n`). Read those two files once before auditing. [ext] marks checks that go beyond the two books.

Ground rule: **evidence or it didn't happen.** Every finding cites `file:line` (or screen + element) that you actually read. Never pad a line list, never cite a placeholder line such as `:0`, never estimate a count, and re-check any "X is missing" claim against the file before reporting it.

## Procedure

1. **Scope.** List every screen/route/state in scope and the top ~3 things users come to do (infer them and say so if nobody told you).
2. **Mechanical pass.** Run `python <skill-dir>/scripts/scan.py <ui source dir>`. It enumerates the real font sizes, colors, spacing values, shadows, and radii, and lists candidate issues with `file:line`: click handlers on non-interactive elements, images without alt, unlabeled controls, missing landmarks/skip link/h1, low contrast pairs, em font sizes, light weights, pure black, uppercase without tracking, centered text, percent-width sidebars, shadows not lit from above, reset buttons, rigid `pattern=` formats, long forms. The same run ends with a **words-and-navigation pass**: link text that does not match the page it opens, shared or generic `<title>`s, several solid buttons on one screen, vague labels (Submit, Learn more, Let's go), long paragraphs where people scan, "Welcome to" filler, exclamation marks, fees or limits in small or faint text, a displaced brand, too many header links, breadcrumb misuse. These are the judgment items that get forgotten: **disposition every one** (finding, or a reason it is fine). **Confirm each candidate in the code before reporting it.** Quote the enumerated counts in "System health". No Python? Do the same sweeps with Grep.
3. **See it.** `python <skill-dir>/scripts/screenshot.py <pages or URLs> --mobile --out <dir>` and Read the PNGs (details: `measuring.md`). If rendering is impossible, say so, and still **compute contrast from the declared colors** with `scripts/contrast.py`: "could not render" never excuses skipping contrast.
4. **First-glance pass, per key screen**, before close reading: what is this, what matters most, where do I start? Squint at the screenshot (trunk test, UR6.8). Note every question mark.
5. **Checklist pass, screen by screen.** For **each screen in scope**, walk sections A to H. Global problems (nav, tokens, type) are recorded once under "Global". A screen with no findings must be a conclusion you reached, not a screen you skipped: the coverage table in the report proves it.
   - **The scan only covers mechanical items.** Sections A, B, C, and G are judgment: for every screen, read the words and the navigation themselves (header conventions, screen name vs what was clicked, breadcrumbs, local nav, what's on a form page, fees and fine print, empty states). Don't let measurable pairs crowd these out: a footer's *content* (a hidden fee) matters more than its contrast ratio.
   - Write down at least one observation per screen that comes from the screenshot, or state "not viewed".
6. **Triage** with the severity anchors below.
7. **Reconcile before writing.** Every confirmed scan candidate and every failed checklist item maps to a findings row (merged into a broader row is fine; silently dropped is not). Use the scan's `[used in: ...]` tags to file each finding under the right screen. Then write the report.
8. **Validate the report.** Save it to a file and run `python <skill-dir>/scripts/check_report.py <report.md> --src <ui source dir>`. It checks that the coverage table matches the findings rows, that every `file:line` exists, that Criticals are few and each names the blocked task or harm, and flags likely duplicates. Fix the report until it passes; do not deliver a report that fails. (It needs the findings table columns exactly as in the format below, with one letter A to H in the Area column.)

Don't report test-fixture or prototype artifacts as design problems (`href="#"` stubs, buttons with no handler in a static demo, missing sample images, example.com addresses, build tooling such as CDN scripts) unless they would ship. Don't pad the list with feature requests either: a missing feature is a finding only when a top task cannot be done without it.

## A. Clarity at a glance (UR1, UR2, UR7)

First-screen items (tagline, blurb, five questions, entry points) apply to whatever a newcomer lands on: marketing/landing page, login, first-run. For in-app screens ask instead: what is this screen, what can I do here, where do I start; mark the rest n/a.

- [ ] A newcomer can say what this product/screen is and what it's for within seconds.
- [ ] First screen answers: what is this, what's here, what can I do, why here, **where do I start**.
- [ ] Tagline sits with the identity, says what the thing is (not a motto, not generic benefits), about 6 to 8 words.
- [ ] Short blurb before any promos, above the fold, differentiator findable at a glance; no mission-statement prose.
- [ ] Entry points look like entry points and are plainly named; separate, clear entries for new users (sign up/start) and returning users (sign in); no big generic button ("Let's go") that traps returning users.
- [ ] Labels use obvious words: no cute, internal, marketing, or jargon names.
- [ ] Everything interactive looks interactive; nothing static looks clickable; links distinguishable from other colored text.
- [ ] No up-front decision that needs thought (search modes, "which one are you", input formats).
- [ ] Every region is identifiable (navigation, explanation, promo, utility); promos don't swamp the main point; utilities aren't mixed into promo blocks.
- [ ] Signs of life; nothing stale shown as "latest"; signed-in state visible.

## B. Navigation and wayfinding (UR4, UR6)

Trunk test on a deep screen, blurred:
- [ ] Identity visible at the top, looks like a brand mark, not beside/like a promo; links home **and** there is an explicit Home affordance.
- [ ] Screen name present even if nav highlights the item; prominent, attached to the content; no group heading masquerading as the screen name.
- [ ] Sections visible, and they are this product's sections (including the current one).
- [ ] Local options visible; current item marked at **every** visible level.
- [ ] "You are here" uses two distinctions (e.g. color + weight); not subtle.
- [ ] Search (if warranted): box + button + the word "Search", same label everywhere, button beside box, no instructions; any scope control reads as a sentence and every option works.

Also:
- [ ] Persistent nav identical in place, look, and wording on every screen; first-screen nav keeps the same section names, order, grouping.
- [ ] Screen name matches the words clicked (link text, `<title>`, heading agree); parent link sits above the name.
- [ ] Utilities: about 4 to 5, quieter than sections.
- [ ] Deep levels have designed navigation, not ad-hoc links.
- [ ] Breadcrumbs (if any): top, small, ">" separators, current item bold, not standing in for the screen name or for navigation.
- [ ] Tabs (if any): active tab connects to its panel and contrasts; one selected on entry.
- [ ] Forms/checkout: reduced to identity, Home, and utilities that help finish.
- [ ] No pulldown hiding options people need to scan: a select holding only a few short options (role, status, priority, plan) should be visible choices (radios, segmented control, cards). Each item lives in one place with "see also" links.
- [ ] Content starts without scrolling; the screen doesn't "start over" behind stacked banners.
- [ ] Verdict "beyond tweaking: structural problem" is allowed instead of cosmetic fixes.

## C. Visual hierarchy (VR1, UR3)

- [ ] One evident primary element per screen; secondary and tertiary visibly quieter; squint test passes.
- [ ] Hierarchy uses weight and color, not size alone; about 3 text colors and 2 weights; none under 400; size spread within a component about 1.5 to 2x.
- [ ] Exactly one primary (solid) action per screen; secondary outline/muted; tertiary link-style; variants are roles, not colors.
- [ ] Destructive action not loud unless it is the primary action (confirm step); placed away from the primary; no solid/semantic buttons repeated on every row.
- [ ] Nothing important looks disabled (low-contrast grey buttons).
- [ ] Data not shown as a `label: value` wall; labels dropped, merged into values, or demoted; key facts lead. In tables and lists, each row has a primary datum (name, title, amount) that is visibly stronger than its secondary data: a row where every cell has the same size, weight, and color fails.
- [ ] Headings styled by need, not tag level; app/section titles don't overpower content; all-caps titles aren't shouting.
- [ ] Icons beside text are softened; inactive nav items quieter than the active one; secondary columns don't share the primary content's raised surface.
- [ ] No grey or translucent-white text on colored backgrounds.
- [ ] Related things look related; headings span only what they govern.
- [ ] Low noise: few rules, few competing colors, no exclamation-mark shouting.

## D. Layout and spacing (VR2)

- [ ] Generous whitespace, judged at full-screen level. Density is acceptable when deliberate (data tables, dashboards): flag it only if reading or hitting targets suffers.
- [ ] Spacing values come from a scale; a component resolves to 2 to 3 values with symmetric padding; no near-duplicate one-offs (quote the scan).
- [ ] Outside-group gap at least ~2x inside-group gap; equal gaps fail (label/input vs field/field, above vs below headings, list items vs line gap, horizontal clusters too).
- [ ] Content has sensible max-widths; nothing stretched to fill; related items not pulled to opposite edges; long forms not full-width inputs.
- [ ] Fixed widths for sidebars/avatars/media; `max-width` rather than per-breakpoint spans; nothing wider at medium than at large.
- [ ] Small screens are designed, not squeezed (check the 400px screenshot; any media queries at all?); large elements shrink more than small ones.
- [ ] Buttons aren't pure zoom (no em padding); touch targets about 44px on touch devices [ext].

## E. Typography (VR3)

- [ ] Sizes from a constrained scale (quote the scan); about 3 to 4 sizes per component; no near-neighbours (13/14/15); px/rem, no nested em.
- [ ] Suitable UI typeface; the weights named actually exist in it.
- [ ] Paragraph measure 45 to 75 characters, including centered intros.
- [ ] Line-height fits: body about 1.5 (more when small or wide), big headlines about 1 to 1.2.
- [ ] Mixed sizes on a line are baseline-aligned.
- [ ] Left-aligned by default; centered blocks are 3 lines or fewer; numeric columns and their headers right-aligned; justified text hyphenated.
- [ ] All-caps text has letter-spacing; no display face patched for small sizes.
- [ ] Link-dense UI isn't blanket link-blue; links in prose keep color + underline.

## F. Color, depth, images, borders (VR4 to VR7)

- [ ] Systematic palette as tokens: 8 to 10 greys, primary and semantic shades; no dozens of near-identical values (quote the scan); no pure black; greys share one temperature.
- [ ] Shade scales keep saturation at the extremes; dark yellows/oranges aren't olive.
- [ ] **Contrast measured, not guessed**: 4.5:1 normal text, 3:1 large text (24px, or ~18.7px bold) and control boundaries [ext]; every solid button's label measured; badges use dark-on-tint rather than white-on-saturated.
- [ ] Meaning never by color alone (status, metrics, chart series); red/green actually matches bad/good for that metric [ext].
- [ ] Shadows from a small elevation scale matched to z-position; floating layers aren't flat; one light direction (from above); pressed/dragged states respond.
- [ ] Separation by spacing/background/shadow before borders; no region with both fill and border; lists not fully ruled. In a data table, borders and alignment are fair game; density alone is not.
- [ ] Text over images legible across the whole text box.
- [ ] Icons and screenshots near their intended size; user uploads cover-cropped in fixed boxes with a translucent inner edge.
- [ ] One radius family, one button shape; accent borders and decoration consistent and never hurting contrast.

## G. Words and forms (UR5, UR8, UR9)

- [ ] No happy talk (welcome/intro/section-front filler); no instructions a clearer UI would make unnecessary. Remaining instructions: nothing obvious, time estimate kept, placed where acted on, "go elsewhere" is a link.
- [ ] Copy scans: short, keywords first. Tone consistent [RUI personality].
- [ ] Forms ask only what this task needs (challenge every field, especially on "free" signups); few optional fields; the value of signing up is shown.
- [ ] Inputs accept flexible formats and normalize (no digits-only, no exact-date patterns).
- [ ] Errors: prevented where possible; shown next to the field in plain words without wiping input [ext]; no always-visible or generic error; no reset button beside submit.
- [ ] Submit label says what happens ("Create account", not "Submit"); nothing on the screen raises "why is that here?".
- [ ] Prices, fees, limits, and support contact easy to find, before people have invested steps.
- [ ] No fake sincerity; any user-unfriendly pattern (pop-up, forced registration) is a deliberate, evidenced decision.

## H. States and accessibility (VR7.5, UR10)

- [ ] Empty states: say what to do, exactly one primary call to action, data-dependent chrome (filters, sort, tabs, export) hidden.
- [ ] Loading, error, success, disabled, hover, focus, active states exist and differ.
- [ ] Top ~3 tasks are obvious and short from the relevant screens.
- [ ] Nothing in the way: splash, forced intro, autoplay, accidental pop-ups.
- [ ] Text-size bump: text grows and layout holds.
- [ ] Every image has `alt` (empty if decorative); every control has a label/accessible name (placeholder is not a label).
- [ ] Everything operable by keyboard: no click handlers on span/div without role, tabindex, and key handling; visible focus [ext].
- [ ] Skip link; landmarks (`header`, `nav`, `main`, `footer`); one `h1`; no heading-level jumps [ext].
- [ ] Link and button text makes sense out of context, keywords first.

## Severity anchors

- **Critical**: a top task is blocked, users are misled into harm or loss, or a basic accessibility barrier exists (a needed control unreachable by keyboard, essential text unreadable, form controls unnamed). Also: collecting sensitive data the task doesn't need. **Each Critical's Finding text must start with `Blocks: <which top task>` or `Harm: <what happens to the person>`** (the validator rejects Criticals without it; if you cannot fill it in honestly, it is not Critical). Expect few: more than about 5 means re-rank.
  - A failed contrast ratio is **Major**, not Critical, unless the text or control is essential to a top task and close to unreadable (roughly under 2:1, or it looks disabled).
  - Missing landmarks, skip link, heading-order slips, and missing alt on decorative images are Major or Minor, never Critical.
  - A keyboard-unreachable control that a top task depends on *is* Critical. A loud destructive button beside routine actions is at least Major.
- **Merge same-cause findings.** Ten low-contrast pairs caused by one missing palette are one finding with a list of locations, not ten rows. Same for repeated unlabeled inputs, repeated one-off values, repeated borders.
- **Major**: real hesitation or repeated wrong turns on a key screen; costs, fees, or limits that are hidden or hard to find (Critical only if people end up charged without having seen them); unclear value proposition or starting point; broken hierarchy; invisible "you are here"; a missing system that causes visible inconsistency.
- **Minor**: polish; people notice or recover instantly. Purely aesthetic complaints are Minor unless the UI looks sloppy enough to cost trust.
- **Not findings**: "kayak" problems (everyone recovers at once, unfazed); deliberate, evidenced trade-offs; fixture artifacts.

Prioritizing fixes: prefer removing to adding (don't fix confusion with more text); head-slappers and cheap visible wins first; be sceptical of feature ideas; check each fix doesn't de-emphasize something that worked. Teams can find far more problems than they can fix: the **top fixes** list is what matters.

## Report format

```markdown
# UI/UX audit: <product / scope>

**Screens reviewed:** ...   **Evidence:** code read / scan.py / screenshots at <widths> / live inspection
**Assumed top user tasks:** 1) ... 2) ... 3) ...

## Verdict
2 to 4 sentences: overall state, biggest problem, biggest strength. ("Beyond tweaking" is a valid verdict.)

## Top fixes
3 to 7 items, ordered by impact per effort: <fix> - why it matters - effort S/M/L - finding numbers it resolves.

## Coverage
| Screen | A | B | C | D | E | F | G | H |
|--------|---|---|---|---|---|---|---|---|
| Global | - | 4 | 1 | 1 | 2 | 3 | - | 2 |
| index  | 3 | 1 | 2 | ok | ok | 1 | 2 | n/a |
(count of findings; "ok" = checked and clean; "n/a" = not applicable; "-" in the Global row = nothing cross-screen in that area. A Global row for cross-screen problems, then a row for every screen in scope. A finding that spans areas is counted once, under the area where the fix happens. **Each cell must equal the number of findings rows with that Screen and Area, and the cells must sum to the findings total.** Fill this table last, by counting the rows.)

## Findings
Complete list of confirmed findings. Group them: Global first, then one group per screen; inside each group order by severity (Critical, Major, Minor). Number rows continuously.
| # | Sev | Screen | Area | Finding | Evidence | Rule | Fix |
|---|-----|--------|------|---------|----------|------|-----|
| 1 | Critical | signup | H | Blocks: creating an account with a screen reader. 10 of 11 inputs have no label | `signup.html:41-57` | UR10.5 | `<label for>` on each |
Merge duplicates; one row per distinct problem, not per occurrence. System-level problems (type scale, palette, spacing) get rows too, not only a mention below.

## System health
Enumerated from scan.py: font sizes N, weights N, colors N (greys N), spacing values N, shadows N, radii N, tokens N, media queries N. What systems exist, what's missing, what to consolidate.

## What's working
Things to preserve. Test each bullet against the checklist before keeping it: never praise something that fails a check or contradicts one of your own findings (whitespace, hierarchy, and "clean design" are the usual false praise).

## Not verified
What couldn't be checked and how to check it (rendering, real content, keyboard run-through, screen reader, real users). Offer a test plan (`usability-test-script.md`) when stakes are high.
```

A heuristic review predicts problems; only watching users confirms them.
