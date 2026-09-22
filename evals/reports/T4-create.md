# T4 - ui-ux skill, create mode: Pennywise "Add expense" + Expenses list

Output folder: `skilltest/create-test/` - `expenses.html`, `add-expense.html`, `styles.css`, `app.js`.

## IMPORTANT: not visually verified

**I never saw these pages rendered.** The skill says "see it if you can; if you can't, say so". I tried three ways and all failed:

1. Claude-in-Chrome: `file://` URLs rejected, then "Browser extension is not connected".
2. Headless Edge `--screenshot` from Git Bash: no image written, no error.
3. Headless Edge from PowerShell: exit code 0, still no image, empty stderr. A last try with `--headless=old` hung for 90s and was stopped.

Consequences you should know about:
- Every layout claim below (spacing, truncation, the 400px row layout, column widths) comes from reading my own CSS, not from looking at it. Treat them as predictions.
- Contrast ratios ARE real numbers: computed with a script from the HSL token values (table below).
- `app.js` only passed `node --check` (syntax). Its behaviour in a browser is untested.
- Side effects of my attempts, and what I did about them:
  - The failed screenshot runs left **9 orphaned headless `msedge.exe` processes**. I stopped exactly those 9, selected by the `skilltest/create-test` path in their command line (the user's own Edge has no such argument). Re-checked afterwards: 0 left. All were headless, so no stray window was opened.
  - A local `http.server` on port 8741 was started and stopped; re-checked, nothing is listening.
  - **Left behind, not cleaned:** `create-test/shots/` containing an Edge `.profile` directory and an empty `err.txt`. It is junk from my attempts and not part of the deliverable. I did not delete it because I don't hard-delete files; remove it with `Remove-Item -Recurse -Force <create-test>\shots`.

Someone should open both files in a browser at ~400px and ~1100px before trusting this.

## Assumptions (no questions asked, per the brief)

- Users: a team of roughly 3 to 15 who all see one shared expense list. Signed-in user is "Ana Reyes". No roles or approval workflow.
- Top 3 tasks: (1) add an expense fast, (2) confirm it landed / see what was spent recently, (3) find a particular expense.
- USD only, English, one month shown (September 2026). Today = 2026-09-21.
- Categories are a short fixed set: Travel, Meals, Software, Office, Other.
- No backend. `app.js` fakes save (900ms) and passes merchant/amount/category back in the query string.
- "Reports" and "Team" nav items are `href="#"` placeholders so the trunk test has sections to show. They are not designed.
- Left out on purpose (skill: "be a pessimist"): approval status, filters, sort, pagination, edit/delete, notes field, "save and add another", dark mode.

## Personality line

**A careful bookkeeper who is easy to talk to: system sans, indigo primary on cool indigo-tinted greys, small 4px radius throughout, plain friendly copy ("Couldn't save. Everything you entered is still here.").**

Indigo was picked over green so the brand colour never reads as "success", and over red/orange so it never reads as "danger".

## Key design decisions and the principle behind each

| Decision | Principle (source) |
|---|---|
| Built the form and list rows first; nav is 3 plain links added last | Feature first, shell later [RUI s1] |
| All raw values live in the `:root` token block; components use only `var(--...)` | Limit choices with systems [RUI s1, design-tokens.md] |
| List: exactly one solid button, "Add expense". Search is outline. In the empty state the header button is hidden so the blank-slate CTA is the only primary | One primary action, button pyramid [RUI s2] |
| Form: "Save expense" solid, "Cancel" link-style | Pyramid [RUI s2] |
| Button says "Add expense", the screen it opens is titled "Add expense"; back link says "Expenses", lands on "Expenses" | Screen names match the words clicked [Krug s7] |
| Form page drops section nav: identity + "<- Expenses" only | Forms get stripped-down nav [Krug s7] |
| Nav "you are here" = colour + bold + 2px accent bar | Two distinctions, not subtle [Krug s7] |
| Month total is a 36px number with the label folded into a sentence: "spent in September - 6 expenses" | Labels are a last resort [RUI s2] |
| Merchant + category merged into one cell (bold name, small grey category) rather than two columns | Merge columns, hierarchy inside a cell [RUI s8] |
| Amounts right-aligned, tabular numerals | Right-align numbers [RUI s4] |
| Category is 5 selectable chips (radio group), not a dropdown | Dropdowns hide options from scanning [Krug s7]; radio groups as cards [RUI s8] |
| Amount is first, biggest (24px bold) and autofocused; Date defaults to today, Paid by defaults to you | Hierarchy [RUI s2]; save steps / prefill [Krug s9] |
| Amount accepts "$1,234.5", "24", stray spaces and normalises on blur | Don't punish input formats [Krug s9] |
| 5 required-ish fields + 1 optional (receipt). No note, no tags | Ask only what the task needs [Krug s10] |
| Label-to-input gap 4px, field-to-field 24px | No ambiguous spacing [RUI s3] |
| Form capped at 512px, list at 768px, neither stretches | Don't fill the screen [RUI s3] |
| Alerts, the "New" tag and selected chips are dark text on a light tint, each with an icon/tick/word | Flip the contrast; never colour alone [RUI s5] |
| Cards separated by shadow + page background; only hairlines are between rows | Fewer borders [RUI s8] |
| Under 640px table rows turn into two-line entries; the total drops 36 -> 30px while body text stays 16px | Large things shrink faster [RUI s3] |

Rule knowingly bent: input borders use grey-400 (3.67:1), darker than RUI's soft-border taste, so fields are findable for low-vision users.

## States and where to see each

A dashed "Demo only" strip at the bottom of each page links to these. With JS off, both pages show their default state.

| State | Where |
|---|---|
| Default list | `expenses.html` |
| Success | `expenses.html?state=added` (green banner, highlighted top row with a "New" tag, total and count updated). Also reached by really submitting the form |
| Empty + CTA | `expenses.html?state=empty` (search, total and header button hidden) |
| Loading | `expenses.html?state=loading` (skeleton rows, `aria-busy`, SR text) |
| Load error + recovery | `expenses.html?state=error` ("Try again") |
| No search results | type e.g. `zzz` in search on `expenses.html` ("Clear search") |
| Long content | the Sep 11 "Amazon Web Services EMEA SARL..." row: one-line ellipsis wide, 2-line clamp small, full text in `title` |
| Field errors | `add-expense.html?state=invalid`, or press Save on an empty form. First bad field is focused; errors clear as you fix them; input is kept |
| Disabled / saving | `add-expense.html?state=saving` (grey button, spinner, "Saving...") |
| Save failed + recovery | `add-expense.html?state=failed` (red-tint alert, fields still filled) |
| Hover / focus / active | CSS only: Tab through either page (2px indigo ring, offset 4px); primary button loses its shadow when pressed |
| Small screen | either page at ~400px wide |

## Self-review against audit-checklist A to H (code-read only, see caveat at top)

Computed contrast (all pass 4.5:1 text / 3:1 non-text):

| Pair | Ratio |
|---|---|
| secondary text grey-600 on white / page / table header | 7.81 / 7.02 / 7.39 |
| tertiary grey-500 on white (placeholder, "$") | 5.67 |
| white on primary-600 button | 8.20 |
| primary-700 link / nav on white | 10.31 |
| primary-800 on primary-100 (chip, avatar) | 11.38 |
| danger-800 on white / on danger-100 | 10.49 / 8.86 |
| success-800 on success-100; grey-600 on success-100 row | 8.67 / 7.01 |
| disabled grey-600 on grey-200 | 5.99 |
| input border grey-400 on white; error border danger-500 | 3.67 / 4.62 |

**Failed, then fixed**

1. **H - table semantics.** Below 640px the table is set to `display:block/grid`, which can strip table roles in some browsers. Fixed: explicit `role="table/rowgroup/row/columnheader/cell"` on every element.
2. **D - "Paid by" column likely too narrow.** 192px minus padding left ~160px for a 24px avatar + "Marcus Oyelaran"; I predicted wrapping. Fixed by removing per-row avatars (also less noise, C). Predicted, not observed.
3. **E - weight 500 does not exist in Segoe UI**, so "normal" would differ between Windows and Mac. Fixed: normal = 400, heavy = 700.
4. **D/F - one-off values outside the token block** (`40ch`, an inline inset shadow) and two `!important` specificity hacks on the amount column. Fixed: `--measure-narrow`, `--shadow-inset`, and proper `.table .c-amt` selectors. The only `!important` left is the `[hidden]` reset.
5. **A/G - label "Paid to"** sat right above "Paid by" and invited a misread. Changed to the conventional "Merchant".
6. **H - JS called `.focus()` on the save-failed alert, which was not focusable.** Added `tabindex="-1"`.
7. **H - hidden radio inputs were `position:absolute` with no positioned parent** (can cause scroll jumps on focus). Added `position:relative` on `.chip`.

8. **H - signed-in user had no accessible name on small screens** (avatar is `aria-hidden`, name was `display:none`). Name is now visually hidden only.

**Known and not fixed**

- A: no tagline. Marked n/a: signed-in app screen, not a landing page.
- B: Reports / Team are dead links.
- H: the success banner is already in the DOM at load, so `role="status"` may not be announced by screen readers. A real app should inject it after load.
- H: fields are not locked while saving.
- F: `--primary-500` is defined but the button uses 600, because 600 gave safer contrast. Departs from the tokens doc's "500 = button background".
- System count: 7 font sizes, 2 weights, 1 radius (+full), 3 shadows, 11 spacing steps. Remaining raw values outside tokens: animation durations, `50%`, `1fr`.

**Validate with users:** is "Merchant" the word they'd use; do they notice category chips are required; is the two-line mobile row scannable for "who paid".

## Skill harness notes

**(a) Delivery.** The Skill tool worked. SKILL.md arrived as a message with "Base directory for this skill: ~/.claude\skills\ui-ux" and my args substituted into the "Arguments:" line. I did not need to Read SKILL.md.

**(b) Reference files opened** (all by absolute path, one parallel batch, no trouble):
- `...\ui-ux\references\visual-design.md`
- `...\ui-ux\references\usability.md`
- `...\ui-ux\references\design-tokens.md`
- `...\ui-ux\references\audit-checklist.md`
Not opened: `usability-test-script.md` (not needed). No PDFs read.

**(c) Ambiguous / contradictory / missing / guessed**
- "See it if you can" gives no method for static local files. Browser tools reject `file://`; I burned several tool calls on workarounds and still failed. A line such as "for static files, serve on localhost or fall back to a code-only review and say so" would help.
- Create step 1 "ask only if..." vs the caller's "don't ask": resolved in favour of the caller. Fine, but the skill has no "state your assumptions instead" instruction; I took that from the brief.
- Step 9 points at a checklist whose report format is analyze-mode (findings table with file:line, "don't modify files"). No format is given for a create-mode self-review; I invented "failed then fixed / known not fixed".
- Checklist A (tagline, five questions, promos) is landing-page shaped. For an in-app screen most of it is n/a and the skill doesn't say so.
- design-tokens.md: "Level values follow the book's example" is a sentence with nothing attached. Radius offers 4 or 12 with no middle. "500 works as a button background" conflicts in practice with the 4.5:1 rule for many hues; I used 600.
- Create step 6 says "First screen answers the five questions", but neither of my screens is a first/landing screen. I guessed it didn't apply.
- Step 7 lists "success" and "disabled" without saying per-screen or per-flow. I did one of each per flow.
- Nothing says how to expose states in a static deliverable. The `?state=` switcher was my guess (and the caller's hint).
- Table-to-cards on mobile: the skill says "designed, not merely squeezed" but is silent on the accessibility cost of changing table display.

**(d) Too long / wasted**
- ~450 lines of reference read up front for a 2-screen job. Irrelevant here: visual-design s7 Images, s9 Keep improving; usability s8 landing screen, s12 settling arguments; design-tokens Tailwind + other-platforms sections (~35 lines); the checklist's triage rules and report template (~50 lines, analyze-only).
- SKILL.md delivers the analyze, refactor, tokens and test-plan mode text even when the mode is plainly `create`.
- visual-design.md and the checklist restate the same rules (by design), so in create mode most rules are read twice.
