# R2-T3 refactor report: Ledgerly (fixture-refactor2)

**Mode:** ui-ux `refactor`. **Files changed:** `index.html`, `invoices.html`, `signup.html`, `styles.css` (all rewritten in place; still static HTML + one CSS file, no JS, no build, no dependencies).
**Evidence used:** code read, `scan.py` before/after, screenshots before/after (desktop 1280 and true 400px), `contrast.py` on every new color pair.
**Assumed top user tasks (from the brief):** 1) create and send an invoice, 2) see what is overdue and chase it, 3) get paid / sign up free to start.
**Assumptions (could not ask):** a large change set is authorized; the brief's "signup needs only what's required to create an account" authorizes removing signup fields; `href="#"` stubs and missing images are fixture artifacts.

## 1. Mini-audit (priority order, what I set out to fix)

| # | Sev | Screen | Finding (before) | Rule |
|---|---|---|---|---|
| 1 | Critical | signup | Free signup demands card number, DOB, household income, address, phone, occupation (11 fields, 8 required) | UR9, UR8 |
| 2 | Critical | signup | 10 of 11 controls have no label (placeholder only); generic always-visible "Error: invalid input." | UR10.5, UR9 |
| 3 | Critical | index | "Create your free account" is a black, non-underlined `<span onclick>`: the main entry point does not look clickable and is not keyboard reachable; search "go" is an empty `<span onclick>` | UR2, UR10.5 |
| 4 | Major | index | First screen does not say what Ledgerly is: "Welcome!", motto "Work. Smarter.", jargon paragraph; 5 equal rainbow buttons incl. "Let's Go!"; no start point | UR7, UR5, VR1.9 |
| 5 | Major | global | Section names are cute ("Launchpad", "The Vault"); active item nearly identical to inactive (#4d4d4d vs #555); brand at far right after the nav; 9 bold blue utilities louder than the sections | UR2, UR6.1, UR6.4, VR1.4 |
| 6 | Major | index | 8 shouting promos (red caps, "!!!") sit above the only real product description; "Which one are you?" up-front decision; "About this section" happy talk | UR7, UR3.5, UR2, UR5 |
| 7 | Major | invoices | No h1/screen name; `<title>` "Billing Documents Manager" matches nothing; breadcrumb is 16px bold and stands in for the name; no current marker in local nav | UR6.3, UR6.4, UR6.5 |
| 8 | Major | invoices | 5 solid buttons in 5 colors; Delete is the biggest, red, uppercase; "Mark as paid" looks disabled (1.68:1); red-underlined "Archive" on every row | VR1.9 |
| 9 | Major | invoices | Metrics use red/green only, no sign or word; "Outstanding" and "Avg. days to pay" going down are shown in red | VR4.6 |
| 10 | Major | global | Contrast failures: hero motto 2.30, hero paragraph 2.55, green btn 3.28, orange btn 2.77, grey btn 1.68, sidebar links 3.82, empty text 2.32, footer (which carries the 3.5% fee) 1.92 | VR4.5, VR1.5, UR8 |
| 11 | Major | global | No system: 14 font sizes (11/12/13/14/15/16/17...), 22 colors, 18 spacing values, 0 tokens, 0 media queries; weight 300 body; line-height 1.2; pure black; em sizes | VR2.3, VR3.1, VR1.3, VR4.1 |
| 12 | Major | global | 400px: nothing reflows; nav, hero buttons, tables and panels are cut off; 25% sidebar | VR2.6, VR2.7 |
| 13 | Minor | invoices | `label: value` wall in a fully ruled table; all-caps 22px panel titles; two shadows lit from the side/below; borders everywhere (17 declarations); amount column not right-aligned; status as plain text | VR1.6, VR1.7, VR5.7, VR7.1, VR3.7 |
| 14 | Minor | invoices | Empty state "No data." with filter, sort and Export still shown | VR7.5 |
| 15 | Minor | signup | "Become a Ledgerly Insider" title, instruction paragraph explaining how to type in a field, "Clear form" reset next to Submit, "Submit" label, "Cancel my subscription" on a signup form, "Your privacy is very important to us", rigid `pattern=` formats, full-width inputs | UR5, UR8, UR9, VR2.5 |
| 16 | Minor | global | No landmarks, skip link, focus style; 4 images without alt; h1 then h3; 16px icon blown up to 96px | UR10.5, UR10.6, VR6.3 |

## 2. What changed and the rule behind it

**Words and clarity**
- Nav: "Launchpad" -> "Home", "The Vault" -> "Invoices" (meaning is inferable: it links to `invoices.html`) (UR2, UR6.1). Same names, order and markup on every page (UR7 last nav bullet).
- Index hero: h1 now says what it is, "Send invoices, see what's overdue, get paid"; tagline "Invoicing for small teams" sits beside the identity (UR7). The three existing feature bullets were halved and moved up into the hero with bold lead-ins (UR7 welcome blurb, UR1.3). "Welcome", motto and jargon paragraph deleted (UR5).
- Entry points: one primary "Create free account" (real link to `signup.html`), separate "Log in" for returning users, "Watch video" as tertiary (UR7, VR1.9). "Let's Go!", "Learn More" removed; "Read the Blog" lives on as Blog in the footer; "See Pricing" became a Pricing utility plus an inline "see pricing" link.
- Fee line (3.5% per payment, prices exclude taxes) moved from an 11px #bbb footer to readable text directly under the CTA, and kept in the footer (UR8 "be upfront").
- "Which one are you?" chooser removed as an up-front decision; its information is kept as "Plans for personal, business and professional use: see pricing" (UR2).
- Promos: all 8 kept, moved below the value proposition into one quiet "News and offers" grid, no caps/red/exclamation marks (UR7 promo overload, UR3.5).
- "About this section" (95 words) cut to one sentence keeping the facts: founded 2019, thousands of customers, small studios to large teams (UR5).
- Utilities cut from 9 to 4 (Help, Pricing, Log in, Sign up); FAQ, Blog, Careers, Press, Partners, Investors parked in the footer, none deleted (UR6.1). "Join" -> "Sign up".
- Search: "Quick Find" + mode select + hint-as-value + blank span replaced with a labelled box and a real "Search" button; now on both app-chrome pages (UR6.1).
- Invoices: `<title>` and h1 "Sent invoices", breadcrumb small with ">" separators and bold current item, above the name (UR6.3, UR6.5). "DOCUMENT INFORMATION"/"ALL SENT DOCUMENTS" -> "INV-2041"/"All sent invoices" (UR2: users say invoice, not document).
- Signup: title "Create your free account", lead "Free to sign up, no card needed.", submit "Create account"; instruction paragraph, fake-sincerity line, reset button and generic error removed; "Already have an account? Log in" added as the go-elsewhere link (UR5, UR8, UR9, checklist G).

**Signup fields (UR9, severity anchor "sensitive data the task doesn't need")**
- Kept: full name, email, password. Removed: phone, street, city, ZIP, date of birth, occupation, household income, card number, and both `pattern=` attributes. Chrome reduced to identity, Home, Help, Log in (UR6.1 forms exception). Avatar row (3 broken, unlabeled images of unknown purpose) removed.
- Per-field error pattern added next to the email field (hidden by default, plain words; `aria-describedby` + `aria-invalid` to be set only in the error state), replacing the always-on generic error (UR9 [ext]).

**Hierarchy**
- Button variants are roles now (`btn-primary`, `btn-secondary`, `btn-tertiary`) instead of colors; exactly one solid primary per screen (VR1.9). On the blue hero the pyramid inverts: white fill, translucent fill, bare text (recipes 1).
- Invoice panel: Send reminder = primary (top task "get paid"); Mark as paid, Download PDF, Duplicate = outline; Delete = grey text at the far end of the row (VR1.9, recipes 1). Row "Archive" = grey text link with an `aria-label` naming the invoice (VR1.9, UR10.3).
- Invoice details de-labelled: big bold amount, dates in grey under it, client name bold with email and phone grey beneath; status folded into an "Overdue 12 days" pill beside the number (VR1.6, recipes 3). No data point dropped.
- Metrics: small tracked caps label over a bold value with the delta beneath; arrow + word ("Up 8%", "Down 14%", "Down 3 days") so nothing relies on color (VR4.6, recipes 3).
- Active nav: color + bold + 2px accent bar, inactive items grey; sidebar current item tinted + bold (UR6.4, VR1.4). Sidebar lost its fill and border so only main content is a raised surface (VR1.4); fixed 176px instead of 25% (VR2.7).
- Panel titles 18px sentence case instead of 22px caps (VR1.7).

**Systems, spacing, type, color, depth**
- Introduced only the tokens used (38 custom properties, names from `design-tokens.md` since the project had none): 7 spacing steps, 7 type sizes in rem, 2 weights, cool greys, primary/danger/success shades, one radius + pill, one shadow. The brand blue was already about primary-500 (#1a6fe0 = hsl 214 79% 49%), so the palette extends the existing brand rather than replacing it.
- Body 16px / 400 / 1.5, no weight under 400, no pure black, no em sizes (VR1.3, VR3.1, VR3.5, VR4.1). Paragraphs capped at 65ch; hero and news in a 960px column; signup card 448px (VR3.3, VR2.5). Hero copy left-aligned instead of a centered 3-line 13px paragraph (VR3.7).
- Borders 17 -> 6 declarations: panels are white cards with one from-above shadow on a grey-50 page; table keeps thin row dividers only; caps headers get 0.05em tracking; Amount and its header right-aligned with tabular numbers (VR7.1, VR5.7, VR3.7, VR3.8).
- Status pills: dark-on-tint with the word (recipes 3, VR4.5). Selected invoice row tinted so the detail panel and the list are visibly related (UR3.1).
- Label-to-input 8px, field-to-field 24px; panel padding 24px with 16px inside gaps (VR2.4).

**States and accessibility**
- Recurring empty state: "No recurring invoices yet."; filter, sort and Export kept in the markup with `hidden` (plus labels) until data exists (VR7.5).
- `header`/`nav`/`main`/`footer` landmarks, skip link, one h1 per page, no level jumps, `:focus-visible` ring (white on the hero), `aria-current` on nav, sidebar, breadcrumb; every control labelled; `th scope`; hover/active button states, pressed primary loses its shadow (UR10.5, UR10.6, VR5.3).
- One `@media (max-width: 720px)` block: header stacks, sidebar becomes a wrapped row of links, metrics 2-up, news 2-up, hero h1 36 -> 24px while body stays 16 (VR2.6, VR2.8), table rows become stacked cards so amount and status stay visible.

## 3. Deliberately left alone

- **"Hive", "Pulse", "Toolbox"** nav labels: meaning cannot be inferred from the fixture (the skill names "Hive" as the keep-and-flag case). The promo hints Pulse = analytics, but I did not rename on a hint.
- **No "New invoice" button.** Top task 1 has no affordance anywhere in the fixture; adding one would be inventing a feature. Gap noted below. Same for a CTA in the Recurring empty state (the rule wants exactly one; no such function exists).
- All 8 promos, all 6 parked utilities, every invoice data point, all 5 invoice actions, Archive per row, Filter/Sort/Export: kept.
- ISO dates (2026-08-01) and the dense table on desktop: deliberate density is fine (VR2.2); date format is an owner call.
- Page composition of `invoices.html` (list + one invoice's detail + month metrics + a Recurring panel on one screen): I reordered to summary -> selected invoice -> list -> recurring but did not split screens.
- System font stack, the blue brand color, 4px radius: kept.
- `href="#"` stubs and sample data: fixture artifacts.

## 4. Open questions for the owner

1. **Metric direction (meaning change, please confirm).** Before, Outstanding "14%" and Avg. days to pay "3" used a class named `down` rendered red, with no sign. I read `down` as direction, wrote "Down 14%" / "Down 3 days", and colored them green because less outstanding and faster payment are good. If `down` actually meant "got worse", the words and color are wrong. Also unknown: compared with what period?
2. What are Hive, Pulse and Toolbox? Plain names would help (Pulse -> Analytics?).
3. Where does "New invoice" live? It should be the primary action of the Invoices section and the CTA of the Recurring empty state.
4. `invoices.html` is both the "Sent" list and the INV-2041 detail. The old breadcrumb ended in INV-2041; I ended it at "Sent" and named the screen "Sent invoices". A separate invoice-detail screen would be cleaner. "Recurring" is both a sidebar item and a panel here (UR4: one place).
5. Is full name needed at signup? Strictly email + password create an account; I kept name because invoices need a sender. Phone/address/DOB/occupation/income/card were removed: if billing details are ever required, ask at first payment, not at signup.
6. "Cancel my subscription" was removed from the signup form; it belongs under Account. A privacy-policy link should replace the removed "Your privacy is very important to us".
7. "Learn More" and "Let's Go!" had no inferable destination and were dropped; the 3 avatars on signup (testimonials?) too. Say if any was meaningful.
8. Search scope options (Keyword / Client ID / Doc number / Tag) were removed from the persistent box per UR6.1; scoping should be offered on the results page.
9. "Summer sale ... offer ends soon" and "Webinar Thursday" carry no dates: stale-content risk (UR7 signs of life).
10. Landing visitors see app sections (Invoices, Hive...) while logged out, and the home page shows Log in while invoices shows Log out; signed-in state handling is outside a static fixture.

## 5. Verification performed

**scan.py** (worked, before and after; outputs saved as `shots/r2-T3/scan-before.txt` and `scan-after.txt`)

| | Before | After |
|---|---|---|
| Candidate items | 64 in 20 groups | 2 in 2 groups |
| Font sizes | 14 (incl. 4 em) | 7 (all tokens, rem) |
| Weights | 700, 300 | 700, 400 |
| Colors | 22 (15 unrelated greys) | 24 incl. shadow/translucent entries, all defined once as tokens (7 greys, one temperature) |
| Spacing values | 18 | 7 tokens + one raw 2px (pill) |
| Shadows | 2 (side/below lit) | 1 (from above) |
| Radii | 3 | 2 (4px + pill) |
| Border declarations | 17 | 6 |
| Tokens / media queries | 0 / 0 | 38 / 1 |

Remaining 2 candidates, both checked: `.form-alt` centered text is one short line (fine, VR3.7); `.hero .btn-secondary 1.00:1` is a scan false positive, it compares white text with the button's own translucent-white fill without compositing over the hero. Composited fill is #3e6fb3, white on it = 5.09:1. Its hover fill (30% white) gives 3.98:1 for 16px bold text: below 4.5, hover-only, left as is and flagged here.

**contrast.py** (worked) on new pairs: white on primary-600 button 5.87; primary-700 link/outline text on white 8.34; white on hero 8.34; primary-100 muted text on hero 7.31 (same hue, not grey or translucent white, VR1.5); sidebar current 7.31; pills: sent 10.38, overdue 9.31, paid 8.15; grey-600 on page 6.70, on white 7.01, on selected row 6.15; grey-500 sidebar heading on page 4.58; success-700 delta 6.47; danger-700 error 8.14; input border 3.61 and focus ring 4.14 (both need 3:1).

**Screenshots: yes, I opened and looked at them.** Before: index, index-mobile, invoices-mobile, signup (4 of 6). After: all 6 (index, invoices, signup at 1280 and at true 400px). What I noticed and fixed as a result:
- The script's `--mobile` images are not 400px layouts on this machine: headless Chrome clamps the window to about 500px and the PNG is a 400px crop, so everything looked cut off at the right (before and after alike). I built a scratch wrapper page with a 400px-wide iframe (`shots/r2-T3/wrap/`) and shot that instead; the after `*-400.png` files are true 400px renders. The clamped after `-mobile` files were deleted to avoid confusion; before `-mobile` shots are the clamped kind.
- At 400px the tagline was pushed to the far right edge away from the identity: removed `space-between` so it sits beside the brand (UR7).
- The three hero CTAs wrapped with "Watch video" orphaned on its own line: shortened the label to "Create free account".
- Footer gutter (24px) did not line up with the 16px page gutter on mobile: aligned.
- The invoice table at 400px hid Amount and Status (the columns that answer "what's overdue") behind horizontal scroll: replaced with stacked row cards on small screens, amount and status pill top right.
- A `hidden` attribute on the `.actions` flex container would have been overridden by `display:flex`: added `[hidden]{display:none !important}` and confirmed in the screenshot that the filters are gone.
- `aria-selected` on a plain table row is invalid ARIA: switched to a class.
- Added a white focus ring inside the hero after measuring that the blue ring would not show on blue.
- In final review: my signup email input pointed `aria-describedby` at the hidden error text, which screen readers would still announce on a pristine form. Removed it; the comment now says to add it only in the error state.

Not verified / needs a human: keyboard run-through and screen reader (the mobile stacked table uses `display:grid` on `tr`, which can weaken table semantics in some screen readers); text-size bump was reasoned from code (rem sizes, no fixed heights), not rendered; hover/focus/active states were not rendered; mobile header is 4 rows (about 175px) before content, acceptable but worth a look; no build/lint exists for this project. Only a usability test can confirm the wording ("News and offers", the hero headline) works for outsiders.

## Skill harness notes

**(a) Delivery.** The skill text was delivered by the Skill tool (`ui-ux`, args passed through and echoed in "Arguments:"), including the base directory. I did not need to Read SKILL.md.

**(b) References and scripts used.**
- Read: `usability-rules.md`, `visual-rules.md`, `audit-checklist.md`, `measuring.md`, `recipes.md`, `design-tokens.md`. Not read: `design-process.md`, `usability-test-script.md` (not called for in refactor mode).
- `scan.py`: worked first time on Windows/Git Bash; candidates with file:line were accurate (every one confirmed). One false positive after the refactor: translucent button fill treated as the text's background without compositing (reports 1.00:1).
- `contrast.py`: worked; accepts hex, hsl() and rgba. First output line is enough for batch use.
- `screenshot.py`: worked for desktop. `--mobile` silently produces a wrong image on Windows headless Chrome (window min-width clamp, about 500px layout cropped to 400px). This is the most important harness defect: both before and after shots look "cut off", which can mislead an agent into thinking its responsive CSS failed (or, worse, hide that it did). Suggest the script wrap the target in a 400px iframe or use `--force-device-scale-factor`/device emulation, and `measuring.md` should mention it. `--full` leaves 2600px of blank canvas on short pages (harmless, wastes image tokens).

**(c) Ambiguous, contradictory, missing, or guessed.**
- UR2 "use the obvious word" vs rule of engagement "if a label's meaning can't be inferred, keep it and flag". The boundary is left to the agent: I renamed labels with code evidence (The Vault -> `invoices.html`) and kept the rest. A one-line test ("rename only when the target or content proves the meaning") would remove the guess.
- "Keep functionality and information" vs checklist A "no up-front decision (which one are you)" and UR7 promo overload: the skill does not say whether removing a chooser or demoting promos counts as dropping functionality. I kept the information and removed the decision. Same tension for the signup: "don't drop fields the task needs" vs UR9; here the brief settled it, but without the brief an agent would have to guess whether it may delete a card-number field.
- "Don't silently change meaning (metric direction)" vs VR4.6 "check red/green matches good/bad": the skill says flag, but not whether to also change. I changed and flagged; an agent could defensibly do either.
- VR7.5 wants "exactly one primary call to action" in an empty state, but "don't invent features" forbids adding one when the function does not exist. Skill does not resolve it; I followed "don't invent".
- Refactor step 1 says "mini-audit (condensed analyze)" without saying what condensed means (findings table? coverage table? severities?). I used a ranked findings table without the coverage table.
- Refactor mode does not list which reference files to read (create mode does). I read six; the table at the top implies it but an explicit line would save a decision.
- Search: the fixture had search only on the home page. UR6.1 says persistent; "don't invent features" says don't add. I treated it as surfacing an existing function. Guess.
- Nothing says where tokens come from when the project has none and the brand color is only implied; I checked the existing blue against the starter palette by hand (it matched). A note such as "compare the existing brand hue to primary-500 before adopting the starter palette" would help.
- Step 4 says screenshots "at desktop and 400px" but nothing about before-screenshots in refactor mode; "Always do first" step 2 covers it implicitly.

**(d) Too long or wasted.**
- `design-tokens.md`: the full palette and Tailwind/platform section were mostly unused; about a third of the file mattered (scales, usage rules, the measured notes beside shades, which were useful).
- `recipes.md` sections 6 to 8 and 12 (depth, text over images, images, hue rotation) were irrelevant for this task; section headers make them easy to skip, but a Read pulls the whole file.
- `usability-rules.md` UR6.8 trunk-test defect list and UR11 were not needed for refactoring.
- The SKILL.md body delivers all five modes; only "Always do first", "refactor", and "Judgment" were needed (about half).
- The audit checklist's report format section is analyze-only but is loaded for refactor.
