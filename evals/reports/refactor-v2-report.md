# Ledgerly refactor: change report

Target: `<tests>\round5\refactor-v2` (index.html, invoices.html, signup.html, styles.css). Still static HTML + CSS, no JS at all (the two `onclick` handlers were replaced by real links), no dependencies.
Work folder: `<tests>\round5\refactor-v2-work` (`before/` snapshot, `shots-before/`, `shots-after/`, `shots-after-full/` (full-height), `scan-after.txt`, `check_refactor-final.txt`).

Assumed top tasks (could not ask): 1) see what is overdue and chase it, 2) create and send an invoice, 3) sign up for a free account.
Personality held throughout: neutral system sans, blue brand, 6px radius, plain calm wording.

## Mini-audit (what was wrong), in fix order

| # | Problem (before) | Rule |
|---|---|---|
| 1 | Section names were jargon: Launchpad, The Vault, Hive, Pulse, Toolbox; invoices page had no h1, a `<title>` "Billing Documents Manager" that matched nothing clicked, and a large bold breadcrumb standing in for the screen name | UR2, UR6.3, UR6.5 |
| 2 | Landing page never said what Ledgerly is: "Welcome to Ledgerly!", motto "Work. Smarter.", a buzzword paragraph, five solid buttons in three colors ("Learn More", "Let's Go!"), a "Which one are you?" chooser, 8 shouting promos (18 exclamation marks), 114 words of happy talk, the only real content (three feature bullets + signup) at the very bottom, and the signup link was a black `<span onclick>` that did not look clickable | UR7, UR5, UR3.5, VR1.9 |
| 3 | Signup for a free account asked for 11 fields incl. phone, address, date of birth, household income and card number, with digit-only `pattern=` formats, placeholder-only labels, 89 words of instructions, an always-visible "Error: invalid input.", a "Clear form" button beside Submit, "Cancel my subscription" on a signup form, and "Your privacy is very important to us" | UR9, UR8, UR5 |
| 4 | Invoices: five differently colored solid buttons with a giant uppercase red DELETE as the loudest thing; "Mark as paid" styled as disabled (1.68:1) though it is not; label:value wall; the key fact (one invoice overdue) never led with: it was one cell in a nine-row label wall and one word in a status column | VR1.9, VR1.6, VR1.1 |
| 5 | 3.5% processing fee hidden in 11px #bbb footer text (1.92:1) | UR8 |
| 6 | 9 utility links before the brand; brand pushed to the top right by `order:3`; search hint text set as a real value; search "Go" was an unlabeled empty `<span onclick>` | UR6.1 |
| 7 | No system: 14 font sizes (13/14/15/16/17), weight 300 body, line-height 1.2, 15 greys, 18 spacing values, 3 radii, two shadows lit from the side/below, 17 borders, 0 tokens, 0 media queries, 0 hover/focus rules, 10 contrast failures, 25%-width sidebar | VR2.3, VR3.1, VR4, VR5.7, VR7.1 |
| 8 | Broken images: `icons/check-16.svg` (a 16px icon scaled to 96px) and `people/a|b|c.jpg` do not exist in the folder; no alt text; no landmarks, skip link, labels | VR6.3, UR10 |

## What changed and why

Global (styles.css fully rewritten around tokens; only tokens that are used)
- Tokens: 6 cool greys, 4 brand blues, danger/success tints, 8-step spacing scale, 8-step type scale in rem, one radius, one shadow. Scan: font sizes 14 -> 8, spacing values 18 -> tokens only, greys 15 -> 6, `var()` declarations 0 -> 310, hover rules 0 -> 13, contrast candidates 10 -> 0 (VR2.3, VR3.1, VR4.1).
- Body 16px/1.5, weights 400/600/700 only, no pure black (VR1.3, VR3.5).
- Header: brand top-left linking home plus an explicit Home item, sections next, 3 quiet utilities right. FAQ, Blog, Careers, Press, Partners, Investors moved to the landing footer, nothing deleted (UR6.1).
- Nav renames: "Launchpad" -> "Home", "The Vault" -> "Invoices" (see disposition). Hive, Pulse, Toolbox kept verbatim. Same names and order on every page; current item marked with color + underline bar, `aria-current` (UR6.4, UR7).
- Button roles instead of colors: one solid primary per screen, outline secondary, text tertiary, quiet red text for Delete (VR1.9).
- `:focus-visible` brand ring, hover states, skip link, header/nav/main/footer landmarks, `@media (max-width: 760px)` layout (UR10).

index.html
- `<title>` "Ledgerly - Invoicing for small teams"; tagline beside the brand; h1 "Send invoices, see what's overdue, get paid."; two-sentence lede built from the original feature bullets (UR7).
- One primary CTA "Create your free account" -> signup.html (the original ghost link's wording), tertiary "Watch video", separate returning-user entry "Already have an account? Log in". Removed "Learn More", "Let's Go!", "Read the Blog" (Blog is in the footer) (UR7 entry points, VR1.9).
- The three real feature bullets moved up directly under the hero, each with a short heading made from words already in the bullet, CSS check icons instead of the broken 96px image (VR7.2).
- Fee sentence, verbatim, now in readable 16px text beside "See pricing", together with the summer sale (UR8).
- Eight promos -> one quiet "More from Ledgerly" grid of six, exclamation marks and red/orange shouting removed, facts kept ($10, #1 FinOps Weekly, Acme Corp, iOS/Android, Webinar Thursday, Pulse). "We're hiring" dropped because Careers is in the footer (UR7 promo overload, UR3.5).
- About paragraph (114 words) -> one sentence with its only facts: founded 2019, thousands of customers, small studios to large teams (UR5).
- "Which one are you?" chooser demoted to a quiet "Ledgerly for: Personal / Business / Professional" line at the bottom (UR2 up-front decisions).

invoices.html
- `<title>` "Invoices - Ledgerly", h1 "Invoices", small breadcrumb with ">" separators, real links, bold current item (UR6.3, UR6.5).
- Sidebar: fixed 208px, no fill or border so the content cards are the only raised surface, "Sent" marked current (VR2.7, VR1.4).
- Detail card: label wall replaced by invoice number + status pill, client contact card without labels, amount bold at right with "12 days overdue", Issued/Due as small caps label over bold value (VR1.6).
- Actions: "Send reminder" solid primary, "Mark as paid" outline, "Download PDF" and "Duplicate" text, "Delete" quiet red at the far end (VR1.9).
- Metrics: label-over-value stat blocks; direction now carried by arrow + word ("Up 8%", "Down 14%", "Down 3"), not color alone (VR4.6). See open question 5.
- Table: 7 columns -> 5 with merged two-line cells (client over number, due over issued), amount and its header right-aligned with tabular figures, status pills dark-on-tint, per-row "Archive" quiet grey instead of danger-colored; heading "ALL SENT DOCUMENTS" -> "Sent invoices". At 400px rows become two-column cards (VR7.6, VR3.7, VR2.6).
- Recurring: "No data." -> "No recurring invoices yet" with one sentence; filter, sort and Export hidden while there is nothing to filter (VR7.5).
- Quick Find moved here from the landing page as a labelled search form that reads as a sentence: "Search by [Keyword] for [____] [Search]"; all four scopes kept, "Doc number" -> "Invoice number" (UR6.1 search).
- Both off-axis shadows removed; one shadow lit from above (VR5.7).

signup.html
- h1 "Create your free account" (matches the CTA), `<title>` "Sign up - Ledgerly", header reduced to brand, Home, Help, Log in (UR6.1 forms exception).
- Fields: Full name, Email, Password only. Removed phone, street, city, ZIP, date of birth, occupation, household income, card number (UR9; brief: "needs only what's required to create an account").
- Real `<label for>`, `type=email`, `autocomplete`, 44px inputs in a 440px card; no `pattern=`.
- Per-field plain-words errors shown only after a bad entry via CSS `:user-invalid` + `:has()` (no JS); generic always-on error removed. "Clear form" removed. "Submit" -> "Create account".
- Instructions, fake-sincerity line, broken avatars, "Cancel my subscription" removed. Fee sentence shown in readable text under the button.

## Ambition pass (existing data only)

| Change | Derived from |
|---|---|
| Lead card headline "1 invoice overdue: $4,250.00" with "Northwind Traders, due Aug 31, 2026" | The single row/detail with Status = Overdue: INV-2041, Amount $4,250.00, Due 2026-08-31. Counted by status, not by date (see open question 4) |
| "Send reminder" is the one solid button and sits in that same card | Existing "Send Reminder" button of the INV-2041 detail panel |
| "12 days overdue" in red next to the amount | Existing "Days Overdue: 12" field |
| Sidebar counts: Sent 6, Overdue 1 (red pill), Paid 3, Recurring 0 | 6 rows in the "all sent documents" table shown under the Sent crumb; 1 row Overdue; 3 rows Paid; Recurring panel says "No data." All and Drafts get no count because drafts are not on screen |
| Overdue row tinted with a red left bar; statuses as word pills | Existing Status column |
| Merged table cells and human dates ("Aug 31, 2026") | Same dates, reformatted only |
| "23 days" unit | The metric's own label "Avg. days to pay" |
| Landing h1 and feature headings "Create and send / See what's overdue / Get paid" | Words of the three original bullets and the product brief |
| Fee + sale next to "See pricing" | Original footer sentence and "Summer Sale" promo, verbatim figures 3.5% and 20% |
| Finishing touches (3): 4px brand band at page top / card top, short accent bar under the hero headline, check icons in tinted circles for the feature list | n/a, decoration only (VR7.2, VR7.3) |

No figure was invented or summed. No button was added for a function that did not exist.

## Verification

- `scan.py` after: mechanical candidates 63 -> 1, words candidates 21 -> 1. Remaining: `.empty` centered text (two short lines, fine, VR3.7); "16 links in the header area" on invoices (the scan counts sidebar filters and breadcrumbs; utilities are 3).
- `contrast.py` on new pairs: secondary text on page 6.70, on table header 6.39, on overdue tint 6.59; white on primary button 5.87; pills 7.31 (sent), 9.31 (overdue), 8.15 (paid); danger text 8.14; success text 6.47; tertiary grey (breadcrumb ">") 4.58; input border 3.61 (needs 3:1). All pass.
- Screenshots at 1280 and 400px were viewed for all three pages; two mobile defects found and fixed (table cells flowing into the wrong grid slots, utilities wrapping under the nav).

### check_refactor.py final output (verbatim)

```

[3] navigation labels no longer present
   "Join"
   "Launchpad"
   "The Vault"
   -> Renaming a jargon label to a plain word is fine if its target proves the meaning: say so in the report. If you cannot tell what a label means, KEEP it and flag it; do not delete product sections.

3 item(s) to revert or to list under 'Open questions for the owner'.
```

Disposition
1. "Join" -> renamed "Sign up". Its target was signup.html, a create-account form; the function is unchanged and still in the header. Kept as renamed; owner to confirm wording (Q1).
2. "Launchpad" -> renamed "Home". Its target was index.html, the home/landing page, and it was the first nav item. Target proves meaning. Kept as renamed (Q1).
3. "The Vault" -> renamed "Invoices". Its target was invoices.html, which contains only invoices and invoice filters. Target proves meaning. Kept as renamed (Q1).

An earlier run also listed a "new navigation entry: Ledgerly Invoicing for small teams". That was the brand link with the tagline inside it, a false positive; I moved the tagline outside the `<a>` and it cleared. Nothing else was flagged: no data lost or changed, no new amounts, no stub controls, no new claims.

## Left alone on purpose

- "Hive", "Pulse", "Toolbox": meaning cannot be proven from the files (Pulse is probably analytics per the promo, but its link is `#`). Kept verbatim.
- All sample data, all `href="#"` fixture links, the "#1 by FinOps Weekly" and "thousands of customers" claims (they are the owner's, pre-existing).
- Red/green meaning of the metrics was not flipped (Q5).
- No "New invoice" button was added even though creating an invoice is a top task (Q2).

## Open questions for the owner

1. Confirm the renames Launchpad -> Home, The Vault -> Invoices, Join -> Sign up.
2. There is no control anywhere to create an invoice (only "Duplicate"). That is the product's first top task and the biggest remaining usability gap; the Invoices header and the Recurring empty state both have room for it. I did not invent one.
3. What are Hive and Toolbox (and is Pulse analytics)? They should get plain names.
4. Data inconsistencies I did not touch: INV-2038 (due Aug 24) and INV-2037 (due Aug 20) are past due relative to INV-2041 (due Aug 31, 12 days overdue) yet have status "Sent"; "Outstanding $9,120" does not equal the unpaid rows ($4,637.25). The overdue headline counts by status. Should "overdue" be computed from the due date?
5. Metrics: originally "Outstanding 14%" and "Avg. days to pay 3" used class `down` in red. If those numbers fell, that is good news and should be green. I show "Down 14%" / "Down 3" in neutral grey with an arrow, and kept Collected "Up 8%" green. Confirm direction and good/bad, and what the comparison period is.
6. "Mark as paid" looked disabled (grey on grey) but had no `disabled` attribute. I treated it as a live secondary action. Correct?
7. Quick Find was on the signed-out landing page, where searching client IDs cannot work; I moved it to the Invoices page. OK, or should it be in the header on every signed-in screen? "Doc number" became "Invoice number".
8. Recurring: filter/sort/Export are hidden while the list is empty. If Export was meant to export all invoices, it belongs in the Invoices header instead.
9. The breadcrumb level "INV-2041" was dropped because the page is a list with one invoice open, and the screen name must match "Invoices". If invoices get their own page, that page's h1 should be the invoice number.
10. "Which one are you? Personal / Business / Professional" is kept as a quiet "Ledgerly for:" line. The product is for small teams; is this segmentation real? If not, delete it.
11. Removed without replacement: "Learn More", "Let's Go!", "Read the Blog" buttons, "We're hiring" promo, "Offer ends soon", "Cancel my subscription" on signup (belongs under Account), avatars, the eight non-essential signup fields. Card number: if billing needs it, ask at upgrade time.
12. "Webinar Thursday" has no date and will go stale; the sale has no end date.
13. Missing assets `icons/check-16.svg` and `people/*.jpg` were never in the folder; both image uses were removed.
14. Does the "Sent" filter mean "everything sent, any status" (6 rows) or "status = Sent" (2 rows)? I counted the former, matching the original panel title "All sent documents" under the Sent breadcrumb. The filter name and the status name collide (UR4); one of them should be renamed.

## Needs a human eye or a usability test

- Whether newcomers understand the landing page in five seconds, and whether returning users find "Log in".
- The signup error messages rely on `:user-invalid` and `:has()` (current Chrome, Edge, Safari, Firefox); older browsers fall back to the native validation bubble. Error, hover and focus states were not screenshotted (the script captures the resting state only).
- Text-size bump and keyboard walk-through were reasoned from the code (rem sizes, min-heights, no fixed heights on text containers), not tested by hand.

## Skill harness notes

Scripts
- `scan.py`: worked. Useful before/after. Noise after refactor: "many links before the content starts" counts sidebar filter links and breadcrumbs as header links (16 on invoices though utilities are 3). Contrast items tagged "ASSUMED page background" need manual checking. It appears not to resolve `var()` colors (not verified in its source): after tokenizing, its contrast pass listed nothing, which can give false comfort, so every pair had to be run through `contrast.py` by hand.
- `screenshot.py`: worked on local files, `--mobile` worked. Prints mixed `/` and `\` in paths on Windows (harmless). Fixed 1400px viewport means pages longer than that are cut unless `--full` is used; cannot capture hover/focus/invalid states.
- `contrast.py`: worked, including `hsl()` input and `--size`.
- `check_refactor.py`: worked, exit code 1 with 3 expected items. One false positive: a brand link that contains the tagline is reported as a "new navigation entry" because `known()` only forgives labels made purely of `<title>` words. Blind spots worth knowing: it treats a label as "still present" if its words appear anywhere in the after text (so "Sent" or "All" could be deleted from the sidebar unnoticed), it does not notice removed non-nav controls (Learn More, Export, filter/sort selects, the chooser, Cancel my subscription), and it does not look at `<select>` options (my "Doc number" -> "Invoice number" rename went unflagged). I listed those in the open questions anyway.
- `scan_words.py` exists in `scripts/` but is not in SKILL.md's script list; `scan.py` output appears to include its pass.
- `check_report.py`: not used (analyze mode only).

Ambiguous, contradictory or missing in the skill
- "Keep functionality and information" vs UR7 "resist promo overload" and VR7.5 "hide chrome that needs data": the skill does not say whether deleting promos or hiding Export/filter on an empty list counts as dropping functionality. I kept promo facts in a quieter form and hid the empty-list chrome, and flagged both.
- "Surfacing an existing function is fine" does not say whether moving a function to another page (Quick Find from landing to Invoices) is surfacing or a behaviour change.
- The ambition-pass example "counts on existing filters" does not address filters whose counts are only partly derivable (All, Drafts). I counted only what the rows prove.
- The "one primary action per screen" rule and the ambition-pass advice "the overdue summary carries a Send reminder" collide when the screen already has a detail panel with the same button; I merged summary and detail into one card to keep a single primary.
- The refactor mode says "Focused diffs. No drive-by rewrites", but a stylesheet with zero tokens and 199 raw values cannot be fixed by a focused diff; the skill should say when a full stylesheet rewrite is acceptable (here the user authorized a large change set).
- SKILL.md says to snapshot to "a scratch folder" and measuring.md says screenshots go in a scratch dir; neither mentions saving the scan/check outputs, which the report step then needs verbatim.
- Refactor step 1 says "condensed analyze" but does not say whether `audit-checklist.md` and both rules files must be read in full for refactor (the file table says yes; the mode text does not).
