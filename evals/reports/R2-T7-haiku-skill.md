# UI/UX audit: Ledgerly (static web app)

**Screens reviewed:** index.html, invoices.html, signup.html  
**Evidence:** code read / scan.py / screenshots at 1920px and 400px widths / contrast.py  
**Assumed top user tasks:** 1) Sign up for an account 2) Manage invoices and track billing 3) Understand what Ledgerly offers

## Skill harness notes

**Skill files read:** audit-checklist.md, usability-rules.md, visual-rules.md, measuring.md

**Scripts run:**
- `scan.py` on fixture directory: ✓ completed successfully, enumerated system values and candidates
- `screenshot.py` on index.html, invoices.html, signup.html with --mobile flag: ✓ completed successfully, generated 6 screenshots (3 desktop, 3 mobile at 400px)
- `contrast.py` on 9 problematic color pairs: ✓ completed successfully

**Instruction clarity:** The audit checklist was clear and well-structured. The procedure matches exactly what was followed: mechanical pass (scan.py), screenshots, first-glance pass, checklist pass per screen, triage, and report format. No ambiguities encountered.

---

## Verdict

Ledgerly's landing page overwhelms users with marketing copy and choice, while the app pages and signup form have serious accessibility and usability gaps. The product looks unfinished: accessibility barriers (missing labels, no landmarks, contrast failures) will block some users entirely, while the signup form collects sensitive payment data during account creation and enforces rigid input formats. Navigation terms ("Hive", "Pulse", "Toolbox") are unexplained jargon. This is **beyond tweaking**—the landing page needs structural rethinking (remove promo overload, clarify value proposition), the form needs to drop unnecessary fields and accept flexible input, and all pages need accessibility foundations (landmarks, labels, contrast, h1 per page).

---

## Top fixes

1. **Restore accessibility baseline (critical)** - Fix form label violations and add landmarks on all pages. No label = form cannot be completed by keyboard users. Effort S. Findings: 3, 5, 6, 7, 8, 11, 13, 15, 17, 18, 19.

2. **Fix contrast failures (critical)** - Raise weak text colors in hero section and buttons to 4.5:1; measure and fix button label contrast. Users with low vision cannot read hero tagline or button labels. Effort M. Findings: 2, 9, 10, 12, 14.

3. **Simplify signup form (critical)** - Drop card number, income, and date fields; accept flexible phone/date input; remove reset button; remove persistent error message. Collects sensitive data not needed for signup and uses rigid patterns that fail real-world input. Effort M. Findings: 4, 20, 21, 22, 23, 24.

4. **Cut landing page jargon and promo overload (major)** - Replace mission-statement hero copy with one sentence saying what Ledgerly is. Remove 6 of 8 promo boxes; rotate instead. Clarify "Hive", "Pulse", "Toolbox" or replace with obvious names. Effort M. Findings: 1, 16, 25.

5. **Clarify entry points and state (major)** - Rename "Let's Go!" to "Create account"; remove "Which one are you?" decision until signup; show logged-in state on app pages. Effort S. Findings: 27, 28, 29.

6. **Fix heading and navigation structure (major)** - Add h1 to invoices.html and signup.html (screen names); use fixed width for sidebar; add skip-to-content link and landmarks on all pages. Effort S. Findings: 16, 17, 18, 19, 26.

---

## Coverage

| Screen | A | B | C | D | E | F | G | H |
|--------|---|---|---|---|---|---|---|---|
| index | 4 | 3 | 3 | 1 | 2 | 4 | 2 | 5 |
| invoices | 1 | 2 | 1 | ok | ok | 2 | ok | 3 |
| signup | 3 | 1 | 1 | 1 | 1 | 1 | 4 | 5 |

---

## Findings

Complete list of confirmed findings, ranked by severity, grouped Global first, then per screen.

| # | Sev | Screen | Area | Finding | Evidence | Rule | Fix |
|---|-----|--------|------|---------|----------|------|-----|
| 1 | Critical | index | G | Hero copy uses marketing jargon ("synergistic solutions", "leverage core competencies", "transformative value") instead of stating what Ledgerly does. | index.html:47 | UR1, UR7 | Replace with one sentence: "Track invoices and get paid faster. See payments in real time." |
| 2 | Critical | index | F | Hero tagline ".hero .motto" (#9a9a9a on #2456c9) contrast 2.30:1, below 4.5:1 threshold; unreadable for users with low vision. | styles.css:41; contrast.py | VR4 | Raise to high contrast; use #ffffff or #f0f0f0 for tagline text. |
| 3 | Critical | index | F | Hero description ".hero p" (rgba(255,255,255,.45) on #2456c9) contrast 2.55:1, below 4.5:1 threshold. | styles.css:42; contrast.py | VR4 | Raise to rgba(255,255,255,1.0) or similar high-contrast white. |
| 4 | Critical | signup | G | Form collects payment card number (16-digit field) and annual household income during account signup—sensitive data not needed for account creation. Delays trust-building. | signup.html:56-57; UR8 | UR8, UR9 | Remove card number and income fields. Ask for payment details only at checkout. Reduce form to: name, email, password, phone, address, occupation. |
| 5 | Critical | signup | H | 15 form controls missing accessible labels: 10 inputs use placeholder-only (email, password, phone, address, etc.), 2 selects with placeholder-only ("Occupation"), 3 searches on index with no labels. Inaccessible to screen-reader users and users who clear form. | signup.html:40-57; index.html:32,38; invoices.html:86-87 | UR10 | Add `<label for>` to every input/select, or use aria-label. Placeholder is not a label. |
| 6 | Critical | index, invoices, signup | H | No `<h1>` on invoices.html and signup.html; index.html has h1 but then jumps to h3 (UR10 violation). Screen names not marked as headings. | index.html:45,65; invoices.html:0; signup.html:0; UR10 | UR10 | Add unique h1 to each page matching the screen name. Remove h3; use h2 for major sections. |
| 7 | Critical | index, invoices, signup | H | No landmark elements on any page: no `<header>`, `<nav>`, `<main>`, or `<footer>`. Navigation and page structure invisible to screen readers. | All three files | UR10 | Wrap topbar in `<header>`, nav list in `<nav>`, main content in `<main>`, copyright in `<footer>`. |
| 8 | Critical | index, invoices, signup | H | No skip-to-content link visible to keyboard users. Must tab through entire topbar and nav to reach main content. | All three files | UR10 | Add `<a href="#main" class="skip-link">Skip to main content</a>` at top of body, with focus-visible styling. |
| 9 | Critical | index | F | ".btn-green" (#fff on #1fa34a) contrast 3.28:1, passes only large text (3:1), fails normal text (4.5:1 required). Button label unreadable at standard size. | styles.css:57; contrast.py | VR4 | Darken green to #0e7c34 or use dark text on light green background. |
| 10 | Critical | index | F | ".btn-orange" (#fff on #ee7d11) contrast 2.77:1, below 4.5:1. Orange button text fails readability. | styles.css:58; contrast.py | VR4 | Darken orange to #c25e00 or switch to dark-on-light button design. |
| 11 | Critical | index | F | ".btn-grey" (#9b9b9b on #c9c9c9) contrast 1.68:1, far below 4.5:1 threshold. Button is nearly invisible. | styles.css:60; contrast.py | VR4 | Use #ffffff text on #c9c9c9, or darker grey background. Reconsider grey as a CTA color. |
| 12 | Critical | invoices | F | ".up" (#1fa34a on #fff) metric text contrast 3.28:1, passes only large text but this is 22px (large), however data labels are typically normal text size (14px); verify applied size. | styles.css:98; contrast.py | VR4 | If used for normal text, darken green to #0e7c34. Check actual rendered size. |
| 13 | Critical | signup | H | 4 images missing alt text: icon on index.html:81, and 3 avatar images on signup.html:61-63. Images are decorative but pattern indicates alt oversight. | index.html:81; signup.html:61-63 | UR10 | Add alt="" (empty) for decorative images, or alt="User avatar" if meaningful. |
| 14 | Critical | index | F | ".promo b" (bold text, #ee7d11 on assumed white) contrast 2.77:1; also ".empty" (#aaa on white) 2.32:1; ".footer" (#bbb on white) 1.92:1. Multiple weak text colors throughout. | styles.css:66,108,124; contrast.py | VR4 | Raise to #2d2d2d or darker; audit all text colors against white backgrounds. |
| 15 | Major | signup | G | Form enforces rigid input patterns: phone field requires exactly 10 digits (pattern="[0-9]{10}"), card number requires exactly 16 digits (pattern="[0-9]{16}"), date requires MM/DD/YYYY exactly. Users cannot enter (555) 765-4321 or 2026-08-01 format. Breaks for international users or different conventions. | signup.html:43,47,57 | UR9 | Accept flexible input and normalize server-side: strip spaces/dashes from phone, parse multiple date formats, use native input types (type="tel", type="date"). |
| 16 | Major | index | A | Landing page tagline and hero are generic. No sentence states "what is Ledgerly" clearly. "Work. Smarter." is a motto, not a differentiator. Users see jargon, promos, and choices instead of clarity about the product. | index.html:45-47 | UR7 | Craft a 6-8 word tagline: "Invoice your clients. Track payments. Get paid on time." Place beside identity. |
| 17 | Major | index | B | "Quick Find" search component lacks a label. Users cannot understand the search scope or what dropdown controls. | index.html:31-39 | UR6 | Add visible label "Quick Find" above or beside, make label associate with select via id/aria-labelledby. |
| 18 | Major | invoices | B | Sidebar width is 25% (percent-width), violating max-width principle. On wide screens the sidebar stretches and wastes space. Main content gets pinched relative to sidebar width. | styles.css:84 | VR2 | Use fixed width: width: 200px (or 220px); main expands to fill. |
| 19 | Major | index | C, G | Promo grid (8 boxes, all with red uppercase headings shouting "HOT!!!" "NEW!" "WEBINAR") dominate the landing page above main value proposition. Promos overwhelm content and confuse what this screen is for. | index.html:64-73 | UR3, UR7 | Move below hero/signup sections, or rotate to show 2-3 promos max. Tone down typography (remove uppercase, reduce font size, use normal weight). |
| 20 | Major | signup | G | Form asks for "Occupation" (dropdown with 3 options), "Annual household income", and "Date of birth"—personal data not required for account creation. Reduces signup completion rate and wastes user trust. | signup.html:48-56 | UR9 | Remove. Collect during onboarding after account exists, or skip entirely unless product genuinely needs it. |
| 21 | Major | signup | H | Reset button ("Clear form") is styled in primary blue (btn-blue), same as submit. Users may click thinking it submits. Reset buttons should not be prominent or discourage accidental clicks. | signup.html:67 | UR9, VR1 | Remove reset button entirely, or style as tertiary link-style button. Form users almost never need this. |
| 22 | Major | signup | G | Error message "Error: invalid input." is persistent, generic, and shown even when form is pristine (no user input yet). Does not relate to any field. Creates confusion and distrust. | signup.html:58 | UR9 | Remove. Show field-level errors only on validation failure, next to the invalid field, in plain words ("Phone must be 10 digits"). |
| 23 | Major | index | G | "Quick Find" input placeholder says "Type a keyword here..." but this is placeholder text that must be deleted to type. Creates cognitive load and appears to be a hint, not a label. | index.html:38 | UR9 | Remove placeholder; add proper label. Or replace with aria-label if visual label space is constrained. |
| 24 | Major | index | H | Two click handlers on non-interactive elements: `.go` span (index.html:39) and `.ghostlink` span (index.html:88) use `onclick="location.href='#'"` but have no focusable element, no keyboard support, no role. Inaccessible. | index.html:39,88; styles.css:32,80 | UR10 | Replace with `<button>` or `<a>` elements. If must use span, add role="button", tabindex="0", and full keyboard event handling. |
| 25 | Major | index | B | Navigation section names are jargon: "Hive", "Pulse", "Toolbox" are unexplained. Users don't know what these sections contain without visiting. "The Vault" (for invoices) is also obscure. | index.html:26-28 | UR2, UR4 | Rename to obvious words: "Team", "Analytics", "Tools" or actual feature names. Or add tooltips. "Invoices" instead of "The Vault". |
| 26 | Minor | invoices | C, F | Multiple action buttons (Send Reminder, Download PDF, Duplicate, DELETE, Mark as paid) fight for attention. No clear primary action. Delete button is loud red (btn-red) but is only one of five equally-spaced buttons. | invoices.html:54-57 | VR1 | Reduce to primary (Send Reminder) and secondary (Download PDF, Duplicate); move Delete to a dropdown menu or separate confirm step. |
| 27 | Minor | index | A | "Let's Go!" button is generic and doesn't say what it does. Is it a CTA for signup, login, or browsing? New users misunderstand; returning users are trapped by the generic label. | index.html:53 | UR7 | Rename to "Create account" for new users, "Sign in" for returning users. Or split into two buttons on the same line, side by side. |
| 28 | Minor | index | A | "Which one are you?" choice (Personal / Business / Professional) is an up-front decision requiring thought. Users pause to think about which category applies. On a landing page, this is cognitive friction. | index.html:57-62 | UR2 | Move to step 2 of signup form, not the landing page. Let users click "Create account" first, then ask about their use case. |
| 29 | Minor | index, invoices | A | No visible indication of signed-in state on app pages (invoices.html). Utilities show "Account" and "Log out" but no username, no sign of the current user. Users may not trust they are logged in. | invoices.html:12-15 | UR7 | Show a user avatar or "Hi, [name]" greeting in top right before the Account menu. |
| 30 | Minor | signup | D, E | Form uses nested em font sizes (help: 0.875em, help .tiny: 0.875em inside 0.875em = 13.125px, off-scale). Body is 15px; tiny becomes smaller than expected. | styles.css:116-117 | VR3, VR2 | Use px sizes throughout: help: 13px; tiny: 12px. Avoid em nesting. |
| 31 | Minor | index | F | Shadows are cast from inconsistent directions: `.card-shadow-a` (3px -2px 9px), `.card-shadow-b` (-4px 6px 2px). Not all shadows point from above (negative y). | styles.css:110-111 | VR5 | Use consistent light-from-above: box-shadow: 0 2px 8px rgba(0,0,0,0.1), 0 4px 12px rgba(0,0,0,0.08). |
| 32 | Minor | all | E | Body font-weight: 300 (light), h1 font-weight: 300 (light). Reduces prominence of headings. | styles.css:3,40 | VR1 | Use font-weight: 400 for body, 600-700 for headings to create hierarchy. |
| 33 | Minor | all | E | Line-height: 1.2 on body is tight. Paragraph measure and line-height are too constrained. | styles.css:3 | VR3 | Raise to line-height: 1.6 for body paragraphs. |
| 34 | Minor | index | F | Pure black text (#000) throughout. No one-off softer alternatives used. Harsh contrast. | styles.css:8 | VR4 | Use #1a1a1a or #2d2d2d instead. Pure black (#000) is rarely necessary in UI. |
| 35 | Minor | index | C | Hero section has 5 equally-weighted buttons in different colors, with no visual hierarchy between them. All appear equally important. | index.html:49-53 | VR1 | Make "Learn More" or primary signup button solid blue; others secondary (outline). Keep only 2-3 buttons. |

---

## System health

Enumerated from scan.py:

- **Font sizes:** 14 distinct (13px, 14px, 15px, 16px, 17px, 18px, 21px, 22px, 46px, plus em/% sizes). No constraint; many near-neighbors (13/14/15). No design token system.
- **Font weights:** 2 distinct (300, 700). No middle weight (400, 500). Heading weight same as body (300).
- **Line-height:** 1 value (1.2). Single fixed value; no scaling for text size.
- **Colors:** 22 distinct (15 greys, 4 semantic: blue #1a6fe0, red #e01a1a, green #1fa34a, orange #ee7d11, plus variants). No tokens; many near-duplicate greys.
- **Spacing/padding/gap:** 18 distinct values (3, 4, 6, 7, 8, 9, 10, 12, 13, 14, 16, 18, 20, 22, 26, 30, plus em). No scale; many one-offs.
- **Shadows:** 2 distinct (both have inconsistent directions, not lit from above).
- **Radii:** 3 distinct (0, 4px, 18px). Inconsistent.
- **Tokens (CSS var()):** 0. No design system.
- **Media queries:** 0. No responsive design for small screens.
- **Declarations using var():** 0 of 199. No systematic property reuse.

**Verdict:** No design tokens or system. Values are ad-hoc. The absence of media queries on a landing page with 400px testing shows no mobile-first design. Spacing, type, and color lack constraints.

---

## What's working

- **Data presentation on app page (invoices.html):** The key-value table and invoice list table are clear, readable, and well-organized. Column headers are in small caps (readable at 12px). Metrics show both value and change indicator (number + up/down color).
- **Consistent topbar across pages:** Nav items, utilities, and brand placement are identical on all three pages. Users know where to look.
- **Form field full-width layout (signup):** Inputs stretch to 100% width, easy to tap on mobile. Good for accessibility.
- **Color diversity for semantic meaning:** Buttons use blue (primary), green (success), orange (secondary), red (danger). Color coding is visible (if contrast issues are fixed).

---

## Not verified

1. **Keyboard navigation:** Did not test tab order, focus visibility, or whether all interactive elements are reachable by keyboard. Test by tabbing through signup form; check that all form fields, buttons, and links receive visible focus outlines.
2. **Screen reader usability:** Did not test with a screen reader. The missing labels, landmarks, and h1s will cause major navigation issues. Test with NVDA or JAWS reading aloud the page structure and form fields.
3. **Real user testing:** Untested with real users. Usability problems (understanding "Hive", deciding which user type to be, filling the signup form) should be validated with 5-10 users attempting the top 3 tasks.
4. **Rendering on Chrome, Firefox, Safari:** Tested with Chromium only. Verify baseline rendering across browsers.
5. **Touch target sizes:** Did not measure button/link sizes at mobile. Some buttons appear tappable but were not measured against 44px minimum (UR10 [ext]).
6. **Color-blind perception:** Did not simulate red/green blindness. The red-on-white contrast pass (2.77:1) may still fail for color-blind users; always pair color with an icon or text label.
7. **Content at 200% zoom / text size bump:** Did not test whether layout holds when browser zoom is 200% or system text size is increased. Sticky fixed heights on containers can break.

---

## Next steps for the owner

1. **Fix critical accessibility barriers first (A1):** Add landmarks, labels, h1, and skip link. These unblock screen reader and keyboard users entirely.
2. **Raise contrast on hero and buttons (A2):** Measure before and after with contrast.py. Users with low vision depend on 4.5:1.
3. **Simplify and shorten signup (A3):** Cut the form to 6 fields; remove card number; use flexible input. Test again with new users.
4. **Test with users:** Once structural issues are fixed, run a quick usability test with 5-10 people trying to (a) understand what Ledgerly is, (b) sign up, (c) view an invoice. Observe where they hesitate or fail.

