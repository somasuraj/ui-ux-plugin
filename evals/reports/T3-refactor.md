# T3 - ui-ux refactor of Ledgerly (fixture-refactor)

**Scope:** index.html (landing), invoices.html (invoice detail + list), signup.html, styles.css. Static HTML + CSS, no JS (the only JS, two inline `onclick`s, was removed).
**Evidence:** code read in full. Rendered UI was NOT seen (see Verification).
**Assumed top user tasks:** 1) create and send an invoice, 2) see what's overdue and chase it, 3) sign up for a free account.

## 1. Mini-audit I started from (priority order; line refs are to the ORIGINAL files)

System pass on the original styles.css: 14 distinct font sizes (px and em mixed), 23 colors, 32 distinct px/em values, 3 radii (0/4/18), 2 shadows (both lit from the wrong direction), 24 border declarations, weights 300/700, no tokens at all.

| # | Sev | Finding | Evidence | Principle |
|---|-----|---------|----------|-----------|
| 1 | Critical | Signup asks for phone, address, ZIP, DOB, occupation, household income and a card number for a free account; punishing formats ("digits only", "no spaces or dashes", "MM/DD/YYYY exactly") | signup.html:43-57 | Ask only what the task needs; accept flexible formats [Krug] |
| 2 | Critical | Inputs have no labels (placeholder-as-label; one `span`, not `label`); search box has help text as its `value` | signup.html:40-57, index.html:38 | Every control has a label [Krug a11y] |
| 3 | Critical | Signup entry point and search button are `span onclick` - not focusable, not keyboard operable; signup link styled as plain black text, while a non-link is styled as a link (`.fakelink`) | index.html:39, 82, 88; styles.css:79-80 | Obvious clickability; keyboard operable |
| 4 | Critical | Unreadable text: grey #9a9a9a and white at 45% on the blue hero; #9b9b9b on #c9c9c9 "Mark as paid"/"Export"; footer fee disclosure at 11px #bbb; body weight 300 | styles.css:7, 41-42, 60, 124 | No grey on color; 4.5:1; no weights under 400 [RUI] |
| 5 | Major | Cute nav names (Launchpad, The Vault, Hive, Pulse, Toolbox); screen names don't match ("Billing Documents Manager", "Become a Ledgerly Insider", link says "Join") | all pages nav; invoices.html:6; signup.html:33; index.html:20 | Obvious names; screen name matches the words clicked [Krug] |
| 6 | Major | Landing never says what Ledgerly is: "Welcome!", motto "Work. Smarter.", buzzword paragraph, "About this section" happy talk; 5 equal CTAs in 3 colors; "Which one are you?" up-front decision; 8 shouting promos | index.html:45-78 | Five first-screen questions; kill happy talk; promo overload; one primary action |
| 7 | Major | You-are-here invisible (#4d4d4d vs #555); brand pushed to the right via `order:3` and not a link; 9 bold blue utilities louder than the sections; nav differs per page | styles.css:24-28 | Trunk test; persistent nav [Krug] |
| 8 | Major | Invoice detail is a bordered `label: value` wall; 5 equal actions in 5 colors, biggest is an uppercase red DELETE | invoices.html:42-58; styles.css:59 | Labels last resort; button pyramid; destructive isn't automatically loud [RUI] |
| 9 | Major | Status and metric direction conveyed by color only; "Quick Find" with a scope dropdown | invoices.html:64-66; index.html:30-39 | Never color alone; search = box + button + "Search" |
| 10 | Major | Empty state "No data." with two dead filters and Export | invoices.html:84-89 | Design empty states |
| 11 | Major | No systems: see counts above; #999 borders on everything; 25%/75% fluid layout, nothing has a max-width; centered 100-word paragraph; em-based sizes nest | styles.css throughout | Limit choices; fewer borders; don't fill the screen [RUI] |
| 12 | Minor | Broken images: `icons/check-16.svg` (a 16px icon forced to 96px) and `people/*.jpg` don't exist, no alt | index.html:81; signup.html:61-63 | Intended size; alt text |
| 13 | Minor | Signup: error box permanently visible ("Error: invalid input."), "Clear form" styled same as Submit, "Cancel my subscription" on a signup form, "Your privacy is very important to us" | signup.html:58-71 | Error recovery; fake sincerity; noise |
| 14 | Minor | No landmarks, skip link, focus style, `th scope`; amounts left-aligned; breadcrumb is the loudest thing on the page and uses "/" | invoices.html:38, 72 | A11y baseline; breadcrumbs are an accessory |

Change set is large; the skill says confirm first, but the task pre-authorized it, so I proceeded.

## 2. What I changed, in the skill's fix order

**1. Clarity and words**
- Nav renamed to plain words: Launchpad > Home, The Vault > Invoices, Pulse > Reports (the old promo said Pulse is analytics). Same wording/order on every page. *Obvious names; persistent nav.*
- Screen names now match the links: every "sign up" link, the page h1, the `<title>` and the submit button all say "Create free account"; invoices page title/h1 "Invoice INV-2041", breadcrumb "Invoices > Sent > INV-2041". *Screen names match what was clicked.*
- Landing: h1 is now the value in plain words ("Send invoices. See what's overdue. Get paid."), one line saying what it is, three short feature blurbs (the original three bullets, cut by about half). Removed: welcome, motto, buzzword paragraph, "About this section", the Personal/Business/Professional chooser, all 8 promos. *Five questions; cut half the words; no up-front decisions; promo overload.*
- The 3.5% fee and tax note moved from 11px light-grey footer text to a readable line under the CTA; added a "Pricing" utility link. *Be upfront about costs.*
- Signup cut from 11 fields to 3 (name, email, password), one value line ("No card needed"), removed instructions paragraph, permanent error, avatars, Clear form, Cancel my subscription, privacy platitude. *Ask only what's needed; kill instructions; fake sincerity.*
- Behaviour change to note: the three kept signup fields gained `required`, `type=email` and `minlength=8` (originally unvalidated; only the removed fields were `required`). *Prevent errors where possible.*
- Search: removed "Quick Find" + scope dropdown from the landing; a real `form role="search"` (labelled box + "Search" button) lives on the invoices page where there is content to search. *Search convention.*

**2. Hierarchy**
- Three button levels replace five color-named classes: `.btn-primary` (solid), `.btn-secondary` (outline), `.btn-tertiary` (link-style). One primary per screen: landing/signup = Create free account; invoice = Send reminder. Mark as paid / Download PDF secondary; Duplicate / Delete tertiary, Delete only turns red on hover. *Button pyramid; destructive not automatically loud.*
- Invoice detail: label/value table replaced by amount (largest), status badge "Overdue by 12 days" (folds Status + Days overdue), client name bold with email/phone as quiet mailto/tel links, "Due ... Issued ..." line. All 9 original data points are still visible. *Labels are a last resort; fold label into value.*
- Section headings dropped from 22px all-caps with rule to 18px sentence case; breadcrumb demoted to small grey with bold current item. *Section titles shouldn't overpower content.*
- Utilities quiet grey, max 4; sections more prominent than utilities. Active nav = color + weight + 4px underline with `aria-current`; sidebar "Sent" marked active to agree with the breadcrumb. *You-are-here needs two distinctions.*

**3. Spacing and layout** - everything on the 4..64 scale; page max-width 1024, form 384, hero copy 65ch; sidebar fixed 192px instead of 25%; panels 24px padding, 32px between groups, heading-to-content 12px (tighter than group gaps); one 640px breakpoint: sidebar stacks, features go single column, headline shrinks 36 > 24px, table scrolls inside its panel. *Scale; unambiguous group spacing; fixed width where content has an ideal size; big things shrink faster.*

**4. Typography** - 8 sizes from the rem scale (12-36), two weights (400/600), body 16px/1.5 (was 15px/300/1.2), headings 1.25; amounts right-aligned; all-caps table headers get letter-spacing; em sizes and em padding removed.

**5. Color** - HSL tokens: cool greys, one blue primary, danger and success as 100/800 pairs. No pure black. Hero is now dark blue text on a light blue tint instead of grey/translucent white on saturated blue. Badges are dark-on-tint. Metrics carry an arrow glyph plus the word "Up/Down"; statuses are text badges. *No grey on color; flip the contrast; never color alone.*

**6. Depth and borders** - 24 border declarations down to: control borders, table row separators, the nav indicator. Panels are white on a grey-50 page with one top-lit two-part shadow (`--shadow-1`); the two mis-lit shadows are gone; one radius (4px) plus pill for badges.

**7. States** - Recurring empty state: one sentence + one CTA, dead filters/Export removed. Hover on nav/buttons/links, `:focus-visible` ring everywhere, `:user-invalid` border on signup fields with native validation messages (no JS).

**8. Accessibility** - `header/nav/main/footer` landmarks, skip link, real `<label for>` on every control, `type=email`, `autocomplete`, password hint via `aria-describedby`, `th scope`, per-row `aria-label` on Archive buttons, `type="button"` on action buttons, span-onclick replaced by real links, broken images removed.

System health after: font sizes 8 (all tokens, 0 raw), colors 20 token definitions (0 raw colors in rules besides `#fff`), radii 2, shadows 1, weights 2.

## 3. Deliberately left alone
- All `href="#"` placeholders (Help, Log in, sidebar filters, Reports...) stay placeholders; I did not invent pages.
- Invoice data, the six sidebar filters, the five invoice actions, per-row Archive, the form's `action="#" method="post"` and field names `n`/`e`/`p`.
- The page still combines detail + month metrics + list + recurring. Splitting it into a list page and a detail page is the better structure but changes product behaviour.
- Invoice numbers in the table are still not links (they weren't before; there is no second detail page to link to).
- System font stack and the blue, small-radius, plain-spoken personality: kept.
- Signup keeps the section nav (Home, Invoices). Krug says forms get stripped-down nav; I only cut the utilities to 2, because the task requires nav between all 3 pages to keep working.
- No dark mode, no loading states (nothing loads).

Judgment calls a human should check:
- **Hive and Toolbox were dropped** from the nav: dead links whose meaning I could not infer. Restore under plain names if they're real sections.
- **Metric colors:** original marked Outstanding 14% and Avg days 3 with class `down` in red. I read `down` as direction; since lower is better for both, they are now green "Down". If the original meant "bad", add a `.trend.bad { color: var(--danger-800) }` variant and use it.
- **Added two placeholder entry points:** "New invoice" (sidebar, secondary) because top task 1 had no entry point at all, and the empty-state CTA. Both are `#` like their neighbours.
- "Archive" was styled as danger; I made it a neutral tertiary action.
- Dates reformatted from ISO to "Aug 1, 2026".

## 4. Verification
- No build/lint exists. Grep checks: 0 `onclick`, 0 `<img`; every non-`#` href resolves to index.html / invoices.html / signup.html / styles.css / an in-page id; inputs vs labels 1:1 on each page; every class used in HTML exists in CSS and vice versa.
- Contrast computed (WCAG formula) for every text pair: white on primary-600 5.66; grey-600 on white 6.5 / on grey-50 6.2; primary-700 links 7.75; hero 12.84 and 9.48; danger badge 8.86; success badge 8.67; secondary button text 9.64. Control border was 2.45 with grey-400, so I switched `--border-control` to grey-500.
- Specificity review (not rendering) found and fixed one bug: `.utils a:hover` outranked `.btn-primary:hover`, turning the header CTA text dark on blue; utilities rule is now `.utils a:not(.btn)`.
- My first greps had false negatives (fixed afterwards): control height 40px and search width 192px were raw one-offs, now `--size-control` / `--size-sidebar`; an unused `.trend.bad` rule was removed. Remaining raw px: 1px borders, 2px focus ring, 4px nav indicator, sr-only/skip-link offsets.
- Re-ran checklist sections A-H against the new files by reading.
- **Not verified:** I never saw the rendered pages. Chrome tools refused `file://`, and over a temporary local server the extension timed out; I stopped after one attempt each and shut the server down. Needs a human eye: header wrapping between about 640 and 900px on the invoices page (search + 3 utilities), table at 400px, hero proportions. `:user-invalid` needs a 2023+ browser; older ones just show native bubbles.
- Worth a 3-person hallway test: "what does this product do?" on the landing, and "this client hasn't paid - do something about it" on the invoice page.

## Skill harness notes

**(a) Delivery.** The Skill tool delivered the SKILL.md text directly (with the base directory and my args substituted into "Arguments:"). I did not need to Read SKILL.md.

**(b) Reference files opened** (all via Read, absolute paths built from the "Base directory" line + the table's relative paths; no trouble finding them):
- `~/.claude\skills\ui-ux\references\audit-checklist.md`
- `...\references\visual-design.md`
- `...\references\usability.md`
- `...\references\design-tokens.md`
- Not opened: `usability-test-script.md` (not needed for refactor). No PDF touched.

**(c) Ambiguous / missing / guessed**
- *No existing design system:* design-tokens.md says introduce its scales "only when nothing exists" - clear - but then offers single AND two-part shadows, 4 radii, and a full 9-step palette without saying how much to adopt. I guessed: a subset (8 spacing steps, 8 type sizes, 1 shadow, 1 radius + pill, only the shades used). Whether to paste the whole block or only used tokens is unstated.
- The semantic colors only ship 100/500/800; the primary-500 "button background" gives about 4:1 with white, so I used 600 for buttons. The file says "verify contrast" but gives no ratios for its own values and no tool/method to compute them.
- `--text-tertiary` is flagged "borderline" by the file itself; I just didn't use it. No token is offered for control borders (3:1 non-text contrast isn't mentioned anywhere); grey-300/400 fail it.
- "If the change set is large ... confirm before proceeding" vs. running as a subagent with pre-authorization: fine here, but the skill has no guidance for non-interactive runs.
- "Mini-audit ... condensed": unclear whether to use the full report format from audit-checklist.md. I used a short findings table and skipped Verdict/What's working.
- "See it if you can" gives no recipe for static files (browser tools reject `file://`). One line like "serve the folder on localhost" plus "if that fails, say so and move on" would help.
- Dead/placeholder links and unknowable labels (Hive, Toolbox): "obvious labels" says rename, "keep behaviour intact" says don't remove, and nothing covers a label whose meaning can't be inferred. I dropped them and flagged it.
- "One primary action per screen" vs. a header "Create free account" button plus the hero CTA (same action twice): I treated same-destination as one action. Not addressed.
- Krug's "forms get reduced navigation" conflicted with the task's "keep nav between the 3 pages"; skill gives no priority rule between a principle and preserving existing nav.
- Adding a "New invoice" entry point: the skill says both "top 3 tasks must be obvious" and "be sceptical of feature ideas". I had to pick.
- Fix order step 7 "loading/error states" for a static page with no JS: no guidance on what is in scope; I did CSS-only states.
- The listing also exposes `ui-refactor`, `ui-create` etc. as separate skills next to `ui-ux refactor`; unclear which is canonical.

**(d) Too long / wasted**
- About 46 KB of references, about 40 KB read. audit-checklist.md sections A-H largely restate visual-design.md and usability.md as checkboxes; for refactor mode the checklist plus tokens would nearly suffice, yet SKILL.md says to read both rule files for "any create/refactor work".
- In design-tokens.md the Tailwind config, "Other platforms", spacing steps 96-768 and type steps 48-72 were irrelevant here; the Tailwind block duplicates the CSS values.
- visual-design.md sections 1 (process), 7 (images), 9 (keep improving) and usability.md sections 2 and 12 are background, not actionable during a refactor.
- SKILL.md itself is compact; the create/analyze/tokens/test-plan mode text was unused but short.
