# UI/UX audit: Ledgerly invoice management app

**Screens reviewed:** index.html (landing/marketing), invoices.html (app page), signup.html (signup form)
**Evidence:** code read / scan.py / screenshots at 1280px and 400px
**Assumed top user tasks:** 1) Understand what Ledgerly is and sign up for an account 2) View and manage invoices/billing documents 3) Check payment status and take actions on documents

## Verdict

The app has critical usability and accessibility gaps that block key tasks. The landing page floods users with noise (18 exclamation marks, 5 competing CTAs, 9 utilities in header), the marketing copy is vague jargon, the signup form collects excessive sensitive data with rigid validation, and the invoice page lacks a screen name, proper navigation markers, and accessible form controls. Visual hierarchy fails across all screens; pure black text, off-scale font sizing with em units, weak contrast ratios (many below 3:1), and misaligned shadows undermine the professional appearance. Navigation is inconsistent: link text doesn't match page titles, the brand is pushed to the right by CSS `order`, and breadcrumbs use wrong conventions and styling. This is beyond tweaking: the information architecture, data collection model, and visual system need rethinking before shipping.

## Top fixes

1. **Fix critical accessibility: add h1, landmarks, skip link to all pages; make all form controls properly labeled** - blocks access by keyboard and screen reader users - M/L - findings 1, 2, 3, 4, 15, 16, 17
2. **Redesign landing page hero: one primary CTA, drop vague copy, explain what Ledgerly actually is** - first impression is noise, not confidence - M - findings 5, 6, 7
3. **Redesign signup form: drop credit card and income fields; label every input with <label> elements; accept flexible phone/date formats** - form collects sensitive data it doesn't need and rejects valid input - L - findings 8, 9, 10
4. **Fix all contrast ratios to 4.5:1 minimum; replace pure black with dark grey; use 1.5 line-height on body** - text is hard to read; footer hides fee disclosure - S - findings 11, 12, 13, 14, 18, 19, 20
5. **Make nav consistent: ensure link text matches page titles and h1; move brand to top-left; fix breadcrumb styling** - users can't tell where they are or where links go - M - findings 21, 22, 24, 25, 26
6. **Remove click handlers from non-interactive elements; add :focus styles to all interactive elements** - keyboard users can't reach the search button or feature link - S - findings 27, 28

## Coverage

| Screen | A | B | C | D | E | F | G | H |
|--------|---|---|---|---|---|---|---|---|
| Global | 1 | 2 | - | - | 2 | 2 | - | 3 |
| index | 2 | - | 1 | 1 | - | - | 5 | 1 |
| invoices | - | 1 | 1 | 2 | 1 | 2 | - | - |
| signup | 1 | - | - | - | - | - | 5 | 1 |

## Findings

| # | Sev | Screen | Area | Finding | Evidence | Rule | Fix |
|---|-----|--------|------|---------|----------|------|-----|
| 1 | Major | Global | A | Page title and h1 mismatch across all pages, confusing navigation: index.html title "Ledgerly" vs h1 "Welcome to Ledgerly!"; invoices title "Billing Documents Manager" vs no h1; signup title "Ledgerly" vs h1 "Become a Ledgerly Insider" | index.html line 6, 45; invoices.html line 6, 1-97 no h1; signup.html line 6, 33 | UR4, UR6 | Each page needs unique title matching h1; e.g., Invoices: title="Manage Invoices - Ledgerly", h1="Manage Invoices" |
| 2 | Major | index | A | "Welcome to Ledgerly!" is filler (UR5) that repeats the product name; hero should answer "what is this" and "why here" in plain language | index.html line 45 | UR5, UR7 | Replace with value proposition: "Track invoices and get paid faster" or concrete differentiator |
| 3 | Major | index | A | Hero section is vague mission-statement prose, not a differentiator; landing page answers only 2 of UR7's five questions clearly | index.html line 47: "synergistic solutions that empower forward-thinking organizations..." = generic jargon lacking clarity of purpose | UR7, UR1 | Rewrite: 1) What is this: "Invoice management software", 2) Why: concrete differentiator (e.g., "Get paid 2x faster"), 3) Entry point, 4) Why here, 5) Where to start |
| 4 | Major | index | C | Five solid primary-action buttons (Learn More, Watch Video, See Pricing, Read the Blog, Let's Go!) all competing visually; no single clear CTA per screen | index.html line 48-54 all use `.btn.btn-blue` or similar solid classes | VR1, UR1 | Keep one solid primary button (sign up); make others outline/secondary style; group related actions |
| 5 | Major | index | D | About section is a long centered paragraph (114 words) hard to scan | index.html line 77-78, styles.css line 68 | UR3, VR3 | Left-align; break into 2-3 shorter paragraphs with subheadings; remove filler |
| 6 | Major | index | G | Vague link text doesn't match page destinations: "Join" -> signup titled "Become a Ledgerly Insider"; "The Vault" -> invoices titled "Billing Documents Manager" | index.html line 20, 25 | UR4, UR6 | Ensure link text matches page title: "Join" -> "Sign Up", "The Vault" -> "Manage Invoices" |
| 7 | Major | index | G | 18 exclamation marks in promo section creates visual noise and unprofessional appearance | index.html line 65-72: "Hot!!! Summer Sale", "Save 20%!!!", "New! Ledgerly Pulse", "Register now!", "rocketship", "Offer ends soon!" | UR3, VR1 | Rewrite promos with one exclamation max: "Hot summer sale: Save 20% on annual plans" |
| 8 | Major | index | G | Vague button labels: "Learn More", "Let's Go!" give no hint what happens; violates UR7 "say what happens" | index.html line 49, 53 | UR7 | Label by outcome: "Learn More" -> "Read feature list"; "Let's Go!" -> "Create free account"; "Watch Video" -> "See 2-minute demo" |
| 9 | Major | index | G | Fee disclosure buried in footer as small faint grey text (11px, 1.92:1 contrast): "Prices exclude taxes and a 3.5% processing fee per payment" | index.html line 91; styles.css line 124 | UR8 | Move pricing/fee info above the fold where visible before sign-up; use normal text size and contrast |
| 10 | Major | index | G | "Type a keyword here..." is placeholder hint text that user must delete to type a real query | index.html line 38 | UR5 | Remove placeholder value; add `<label for="kw">Search</label>` or `aria-label="Search keywords"` |
| 11 | Major | Global | B | Navigation identity (brand) is pushed to the right by CSS `order:3` instead of top-left | styles.css line 26 `.brand { order:3; margin-left:20px }` | UR6 | Remove `order:3`, use normal flow; brand should be first (top-left), link to home |
| 12 | Major | Global | B | Navigation link count excessive: 9 utilities on index/signup, 3 on invoices; should be 4-5 quieter items | index.html line 12-22 has 9 links; signup line 12-21 has 9 links | UR6 | Keep: Help, Account, Log out; move Blog, Careers, Press, Partners, Investors to footer |
| 13 | Major | invoices | B | Breadcrumb styling is wrong: uses "/" (should be ">"), styled large bold 16px (should be small), not linked, positioned as if screen name | invoices.html line 38 `<div class="crumbs">Launchpad / The Vault / Sent / INV-2041</div>` | UR4, UR6 | Restyle: smaller 12px, ">" separators, make links except current item, current bold, positioned top of content |
| 14 | Critical | Global | H | 15 form controls lack proper labels; signup fields use only placeholder text which is not accessible; screen reader and keyboard users cannot identify form fields | index.html line 32, 38 (Quick Find); invoices.html line 86, 87 (filters); signup.html line 40-57 (11 form fields, each with placeholder only, no label element) | UR10 | Wrap each input in `<label for>` or use `aria-label`; placeholder alone is not accessible (WCAG 2.1 1.3.1) |
| 15 | Major | Global | H | No skip-to-content link and no semantic landmarks (`<header>`, `<nav>`, `main`, `<footer>`); keyboard and screen reader users cannot navigate efficiently | index.html lines 1-94: no skip link, nav not in `<nav>`, main content not in `<main>`; invoices.html lines 1-97: same; signup.html lines 1-78: same | UR10 | Add `<a href="#main" class="skip">Skip to content</a>` at top; wrap header in `<header>`, nav in `<nav>`, main content in `<main>`, footer in `<footer>` (WCAG 1.3.1) |
| 16 | Critical | Global | H | Click handlers on non-interactive elements (span); keyboard users cannot reach search button or feature CTA | index.html line 39 (span.go onclick="location.href='#'"), line 88 (span.ghostlink onclick) | UR10 | Convert spans to `<button>` or `<a>` with role, tabindex, and key handlers; search button must be accessible via Tab (WCAG 2.1 2.1.1) |
| 17 | Major | invoices | C | Label:value data table displayed as `<tr><td>Label:</td><td>Value</td></tr>` wall, hard to scan | invoices.html line 42-52: "Document ID:", "Client Name:", "Client Email:", etc. all in same visual weight | VR1 | Drop labels where format explains value (INV-2041, $4,250.00, Overdue need no prefix); bold numbers, regular text for units |
| 18 | Major | invoices | D | "Archive" buttons in data table use quiet-danger style (red underlined text) resembling links more than buttons | invoices.html line 73-78 all have `<button class="quiet-danger">Archive</button>` | VR1 | Use secondary button style (outline or low-contrast fill), not link styling |
| 19 | Major | invoices | D | Sidebar width is 25% (percent-width); should be fixed width per VR2 to prevent label wrap on narrow screens | styles.css line 84 `.sidebar { width: 25% }` | VR2 | Change sidebar width from 25% to `width: 200px` or similar fixed value |
| 20 | Major | invoices | E | Column headers are all-caps without letter-spacing ("NUMBER", "CLIENT", "ISSUED", "DUE", "AMOUNT", "STATUS"), hard to read | invoices.html line 72; styles.css line 103 `text-transform: uppercase` | VR3 | Add `letter-spacing: 0.1em` to uppercase text; or use title case: "Number", "Client", "Issued" |
| 21 | Major | invoices | F | Box shadows cast from wrong direction: card-shadow-a has negative y-offset (-2px, points upward); card-shadow-b has negative x-offset (-4px, points leftward) | styles.css line 110, 111: `3px -2px 9px rgba(0,0,0,0.35)` and `-4px 6px 2px rgba(0,0,0,0.5)` | VR5 | Shadows cast from light above: use `0 2px 8px rgba(0,0,0,0.1)` and `0 4px 6px rgba(0,0,0,0.1)` (never negative y, never leftward x) |
| 22 | Major | signup | A | Signup page title "Ledgerly" (shared with index, unrecognizable); h1 "Become a Ledgerly Insider" (indirect). Link text "Join" doesn't match page. User arriving from "Join" link is disoriented; doesn't know which page or what to do | signup.html line 6 title "Ledgerly"; line 33 h1 "Become a Ledgerly Insider"; index.html line 20 "Join" link text doesn't match | UR6 | Title: "Sign Up"; h1: "Create your Ledgerly account" — match the "Join" link and make purpose unmissable |
| 23 | Critical | signup | G | Signup form collects excessive sensitive data not needed for trial signup: full name, street address, city, ZIP, date of birth, occupation, annual household income, credit card number. Users distrust overreach and abandon | signup.html line 40-57: 11 fields, 8 required, including credit card (line 57) before any account exists | UR9, UR8 | Reduce to: email, password, (optional) company name. Move phone, address, income, payment to checkout or account upgrade (WCAG 2.5.1) |
| 24 | Critical | signup | G | Form uses rigid input validation patterns that reject common valid input: phone requires exactly 10 digits no spaces/dashes; credit card exactly 16 no formatting. Users with (555) 765-4321 or 4532-1234-5678-9010 cannot complete signup | signup.html line 43 `pattern="[0-9]{10}"`, line 57 `pattern="[0-9]{16}"` | UR9 | Remove pattern attribute; accept common formats ((555) 765-4321, 555-765-4321, 555.765.4321) and normalize on submit; accept spaces/dashes in credit card |
| 25 | Major | signup | G | Form has reset button (Clear form) that wipes input if clicked by accident; modern UX removes reset buttons | signup.html line 67 `<button type="reset" class="btn btn-blue">Clear form</button>` | UR5 | Remove the reset button; submit button is sufficient |
| 26 | Minor | signup | G | Instructions paragraph is 89 words above form telling users how to fill it out; nobody reads instructions | signup.html line 36 | UR5 | Remove instructions; make form obvious via labels and removing unnecessary fields |
| 27 | Minor | signup | G | "Cancel my subscription" link appears on signup page before user has created account; confusing out-of-place link | signup.html line 69 | UR7 | Remove this link; it belongs in account settings after signup completes, not during signup |
| 28 | Minor | signup | H | 3 avatar images at bottom have no alt text; unclear purpose (why choose an avatar during signup?) | signup.html line 61-63 `<img src="people/a.jpg">` etc. with no alt | UR10 | Add descriptive alt text if meaningful ("Choose a profile picture"); hide from a11y tree if decorative with `alt=""` |
| 29 | Major | Global | E | Body text weight is 300 (light) and line-height 1.2 (tight), making text hard to read and scan | styles.css line 3-4 `font-weight: 300` and `line-height: 1.2` | VR3, UR3 | Set body `font-weight: 400` (or 500) and `line-height: 1.5` (reduces eye strain, improves scannability) |
| 30 | Major | Global | E | Font sizes use em units causing nesting issues and off-scale values: .btn 1em, .formwrap h1 2.5em (calculates to ~62px), .help .tiny 0.875em | styles.css line 45 `font-size: 1em`, line 115 `font-size: 2.5em`, line 116-117 `font-size: 0.875em` | VR3 | Replace em sizes with px or rem: use constrained scale (12, 14, 16, 18, 20, 24, 32, 48px); .formwrap h1 should be 32px or 36px |
| 31 | Major | Global | F | 10 contrast pairs below 4.5:1 WCAG AA threshold for normal text: hero motto 2.30:1, hero p 2.55:1, .btn-green 3.28:1, .btn-orange 2.77:1, .btn-grey 1.68:1, .promo b 2.77:1, .sidebar a 3.82:1, .metrics .up 3.28:1, .empty 2.32:1, .footer 1.92:1 | styles.css line 41, 42, 57, 58, 60, 66, 85, 98, 108, 124 | VR4 | Darken foreground or lighten background: hero text on #2456c9 needs #d0d0d0+ grey; button fills need darker color; footer must be ≥4.5:1 (currently hides fee) |
| 32 | Major | Global | F | Pure black (#000) used in body, ghost links, and table cells; VR4 requires dark grey to reduce harshness | styles.css line 3 body `color: #000`, line 80 .ghostlink `color: #000`, line 94 .kv td `color: #000` | VR4 | Replace #000 with #333 or #2a2a2a; maintains contrast while reducing eye strain |
| 33 | Minor | index | H | Heading structure jumps from h1 to h3 (skips h2); should be h1, h2, h3 in order | index.html line 45 h1 "Welcome to Ledgerly!", line 65 h3 "Hot!!! Summer Sale" | UR10 | Change line 65 `<h3>` to `<h2>` for each promo section heading |
| 34 | Minor | invoices | F | Multiple one-off button styles (.btn-blue, .btn-green, .btn-orange, .btn-red, .btn-grey) with inconsistent radii (0, 4px, 18px) and sizing; no coherent design system | styles.css line 45-60 | VR1, VR7 | Define button variants: primary (solid blue, 4px radius), secondary (outline), destructive (red, only in confirmation); consistent sizing |

## System health

**Enumerated from scan.py:**
- Font sizes: 14 distinct (too many; no scale) — 13px x7, 14px x5, 0.875em x2, 12px x2, 15px x2, 16px x2, 17px x2, 22px x2, 11px, 18px, 1em, 2.5em, 21px, 46px
- Font weights: 2 distinct — 700 x5, 300 x3 (should use 3-4: 400 normal, 500 medium, 600 semi-bold, 700 bold)
- Line heights: 1 distinct — 1.2 (too tight; should be 1.4-1.6 for body)
- Colors: 22 distinct (15 neutral greys = too many) — no coordinated palette; no tokens
- Margin/padding/gap: 18 distinct (no scale) — 10px x15, 8px x8, 6px x6, 12px x5 are the only repeated values
- Box shadows: 2 (both have wrong direction)
- Border radii: 3 distinct (0, 4px, 18px = inconsistent)
- Tokens defined: 0
- Media queries: 0 (no mobile-first design)
- Interactive states (:hover, :focus, :active): 0 (no state styles)

**Missing systems:**
- No type scale (sizes and weights lack constraint)
- No spacing scale (margins/padding are ad-hoc)
- No color palette (22 colors, many near-duplicates)
- No button or component tokens
- No responsive design (no breakpoints for 400px mobile)
- No interactive states defined

## What's working

- Navigation structure is consistent across pages (same nav bar and utilities on all three)
- Color scheme uses blue (#1a6fe0) as a primary consistently, with green and orange as accents — recognizable
- Data table on invoices page includes status and date columns, relevant for invoice management
- Metrics display (Collected, Outstanding, Avg. days to pay) shows key performance indicators in one glance
- Signup form collects enough information to identify users (even if too much)

## Not verified

- Whether patterns actually reject valid input formats; would need to test phone (555) 765-4321 and credit card 4532-1234-5678-9010 to confirm user confusion
- Whether keyboard navigation is truly blocked or if tabindex/ARIA bypasses help (the span click handlers could work with tabindex, but shouldn't)
- Mobile responsive behavior at 400px: only layout tested via screenshot; scrolling, touch targets, and interaction not verified
- Real-user usability: heuristic review predicts problems but only watching users can confirm which ones matter most (the vague copy, excessive form fields, and noise on the landing page are the most likely to cause abandonment)

## Appendix: Audit methodology

- **Scope:** all three HTML pages and shared CSS; no backend, no real data
- **Mechanical pass:** Python scan.py enumerated 35 candidates across categories; each disposition requires code review
- **Visual inspection:** screenshots at 1280px desktop and 400px mobile reveal layout, readability, and visual hierarchy issues
- **Usability rules applied:** UR1–UR10 from *Don't Make Me Think*; UR extensions [ext] for apps and mobile
- **Visual rules applied:** VR1–VR7 from *Refactoring UI*
- **Checklist sections:** A–H evaluated per `audit-checklist.md`; findings count represents distinct problems, not occurrences
- **Severity:** Critical = task blocked or user harmed; Major = real hesitation or repeated wrong turns; Minor = polish or aesthetic
