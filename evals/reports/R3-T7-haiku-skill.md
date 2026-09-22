# UI/UX audit: Ledgerly (landing + app + signup)

**Screens reviewed:** index.html (Launchpad landing), invoices.html (The Vault app), signup.html (signup form)  
**Evidence:** code read / scan.py / screenshots at 1280x1400 and 400px / contrast.py measurements

**Assumed top user tasks:** 1) Understand what Ledgerly is and decide to sign up on landing page; 2) Find and manage specific invoice documents in the app; 3) Complete signup form with required information

## Skill harness notes

**Skill files read:** 
- `references/audit-checklist.md` (procedure and checklist)
- `references/usability-rules.md` (UR rules)
- `references/visual-rules.md` (VR rules)
- `references/measuring.md` (screenshots and contrast)

**Scripts run:**
- `scripts/scan.py` - enumerated 14 font sizes, 2 weights, 22 colors, 18 spacing values, 2 shadows, 3 radii, 0 tokens, 0 media queries; confirmed 15+ candidate issues with file:line evidence
- `scripts/screenshot.py --mobile` - produced 6 screenshots (desktop + mobile for each page); rendered successfully
- `scripts/contrast.py` - measured 6 specific color pairs; all flagged pairs confirmed as FAILS

**Procedure followed exactly:** Scope → Mechanical pass (scan) → See it (screenshots) → First-glance pass → Checklist sections A–H per screen → Triage by severity → Report.

**Instruction clarity:** All instructions clear; no ambiguities in procedure.

---

## Verdict

This product has critical usability and accessibility issues across all three screens. The landing page mixes marketing promos with unclear value proposition and contradicts UR7 guidance on clarity. The app screen lacks proper visual hierarchy and keyboard navigation. The signup form collects excessive sensitive data (card number on initial signup) with no labels, rigid input patterns, and a destructive reset button. Navigation lacks landmarks and skip links on all screens. The design system is entirely missing (no tokens, no media queries, inconsistent type/color/spacing). Fix high-severity form and accessibility issues before launch; the landing page and app need fundamental hierarchy and clarity work.

---

## Top fixes

1. **Remove card number field from signup; add clear labels to all inputs** - collecting payment details on initial signup violates trust and UR9. Placeholder-only fields fail accessibility (UR10.5). Fixes findings 4, 7, 8, 15, 21. - **Effort: M** - Finding: 4, 7, 8, 15, 21

2. **Add proper landmarks, skip link, and fix heading structure** - Missing `<header>`, `<nav>`, `<main>`, `<footer>`, no skip link, and h1 missing on invoices.html block three top-task screens from keyboard and screen-reader users. Fixes findings 11, 12, 14, 17, 25. - **Effort: S** - Findings: 11, 12, 14, 17, 25

3. **Fix contrast on hero section and buttons** - Hero motto (2.30:1) and body text (2.55:1) fail on blue background; green button (3.28:1) and orange button (2.77:1) fail for bold text. Fixes findings 19, 20, 22, 23. - **Effort: S** - Findings: 19, 20, 22, 23

4. **Clarify landing page value proposition and reduce button competition** - Mission-statement prose and 8 promos obscure main message; five CTA buttons compete equally (UR7 violation). Hero should answer "what is this, what can I do, why here, where start" clearly. Fixes findings 1, 2, 6, 9, 27. - **Effort: L** - Findings: 1, 2, 6, 9, 27

5. **Remove reset button and rigid input patterns; accept flexible formats** - Reset button wipes form (UR9 anti-pattern); phone and card patterns reject valid input with dashes/spaces (UR8). Phone acceptance must be "normalize on submit, not on input." Fixes findings 5, 13, 16. - **Effort: S** - Findings: 5, 13, 16

6. **Fix shadow directions and stabilize layout sidebars** - Shadows cast from wrong direction on cards (3px -2px and -4px 6px violate VR5.1); sidebar 25% width wastes space and forces sidebar narrower than main on mobile. Use fixed widths and check responsive breakpoints. Fixes findings 10, 24. - **Effort: M** - Findings: 10, 24

7. **Introduce a design system: tokens for type, color, spacing; define media queries** - 14 font sizes (many near-neighbors 13/14/15), 22 colors, 18 spacing values, 0 media queries, 0 tokens. No system means inconsistency, high maintenance, and impossible mobile design. Fixes findings 3, 18, 26, 28. - **Effort: L** - Findings: 3, 18, 26, 28

---

## Coverage

| Screen | A | B | C | D | E | F | G | H |
|--------|---|---|---|---|---|---|---|---|
| Global | - | 1 | - | - | 1 | 3 | 2 | 2 |
| index  | 4 | 3 | 3 | 1 | 4 | 4 | 3 | 3 |
| invoices | 1 | 2 | 2 | 2 | 2 | 3 | 1 | 3 |
| signup | 1 | 1 | 1 | 1 | 2 | 1 | 3 | 4 |

(A=Clarity, B=Navigation, C=Hierarchy, D=Layout, E=Typography, F=Color/depth, G=Words/forms, H=States/accessibility. Count = findings per area; "ok" = checked and clean, but none here reached that status. Each row sums to the findings under that screen.)

---

## Findings

Complete list of confirmed findings, ranked by severity.

| # | Sev | Screen | Area | Finding | Evidence | Rule | Fix |
|---|-----|--------|------|---------|----------|------|-----|
| 1 | Critical | index | A | Landing page copy is mission-statement prose, not clear value proposition | index.html:47 "Ledgerly delivers world-class, best-of-breed synergistic solutions that empower forward-thinking organizations..." - buzzwords that apply to any product, no clear differentiator | UR7 | Replace with terse, concrete benefit (3–4 key facts, not generic boilerplate) |
| 2 | Critical | index | A | Five CTA buttons compete equally; no clear entry point for new users vs returning users | index.html:49-53 all `.btn` with different colors but equal prominence; "Let's Go!" generic | UR7 | One primary action per screen: "Create account" solid blue; secondary "Sign in" outline; reduce other calls to secondary or link style |
| 3 | Critical | Global | E | No design system: 14 distinct font sizes with near-neighbor pairs (13/14/15px), 22 colors with 15 uncoordinated greys, 18 spacing values, font-weight only 300 and 700 (300 too light), no tokens, no media queries | scan.py output: "font-size: 14 distinct", "colors: 22 distinct (15 neutral greys)", "spacing/margin/padding/gap values: 18 distinct", "font-weight: 2 distinct... 300 x3", "custom properties (tokens) defined: 0", "@media queries: 0" | VR3, VR4, VR2 | Build minimal token system: type scale (14, 16, 18, 20, 24px for UI), 10-color grey ramp (maintain temperature), primary palette, 8-step spacing scale (4, 8, 12, 16, 24, 32, 48, 64px), 2 weights (500, 700, no 300) |
| 4 | Critical | signup | G | Signup form collects 11 fields, 8 required; includes card number on initial signup without value prop shown | signup.html:39-57 collects name, email, password, phone (pattern-restricted), address, city, ZIP, DOB (exact format), occupation, income, card number (16-digit pattern) | UR9, UR8 | Remove card number from initial signup; defer payment to checkout flow. Reduce to essentials for this task: name, email, password, phone (flexible format). Accept spaces/dashes, normalize on server. |
| 5 | Critical | signup | G | Rigid input format patterns reject valid input; phone pattern requires digits-only, card pattern requires digits-only | signup.html:43 `pattern="[0-9]{10}"`, signup.html:57 `pattern="[0-9]{16}"` both forbid spaces/dashes that users naturally type | UR8 | Accept flexible input (spaces, dashes, parentheses for phone; spaces for card) and normalize on server: `type="text"` without pattern, client-side trim/replace, server validates canonical format |
| 6 | Critical | index | C | Hero section has five equally prominent CTA buttons (blue, green, orange, blue, green) with no hierarchy; "Let's Go!" is generic and traps returning users | index.html:49-53 `.btn` with different `.btn-*` color classes but identical font-size (1em nests), padding (0.6em 1.1em), no secondary/tertiary variants | VR1 | One primary button per screen: "Create account" (solid blue, 16px, 700 weight). Secondary "Learn more" (outline or muted). Remove "Watch Video", "See Pricing", "Read Blog", "Let's Go!" from CTA row or demote to links below. |
| 7 | Critical | signup | H | 10 of 11 form inputs have no associated label; Email, Password, Phone, Address, City, ZIP, DOB, Income, Card inputs use placeholder-only, which fails accessibility | signup.html:41-57 only input name="n" has `<label>`, rest are placeholder="..."; inputs 40-46 (Email-ZIP) have no label. Scan: "[15] form control with no label / accessible name" | UR10.5 | Add `<label for="fieldid">Label text</label>` before each input; move placeholder to aria-placeholder or helper text below; input names must be semantic |
| 8 | Critical | signup | H | Form fields have no `<label>` elements tied via `for` attribute; field input name="n" suggests single-letter shorthand instead of semantic naming | signup.html:40-57 inputs have attributes: name="n", name="e", name="p", name="ph", name="a1", name="a2", name="zip", name="dob", name="occ", name="rev", name="cc" - no labels, abbreviated names | UR10.5 | Rename inputs to semantic names: `name="fullName"`, `name="email"`, etc. Add `<label for="fullName">Full name</label>` with matching id on input. Placeholder is not a label. |
| 9 | Critical | index | A | Promo grid (8 items) with all-caps red headings and exclamation marks swamps main value proposition; promos distract from "Which one are you?" entry point | index.html:64-73 `.promo` grid 4 columns, uppercase red h3 with "!!!", "Now", "Register now before seats run out!", targeting urgency; 8 items consume more space than the hero value prop | UR7 | Hide or dramatically reduce promos on first screen; no more than 1–2 featured items above the fold. Content should answer UR7's five questions (what, what's here, what can I do, why, where start) before any promo. |
| 10 | Major | invoices | F | Card shadows cast from wrong direction; `card-shadow-a` has offset `3px -2px` (right and up), `card-shadow-b` has offset `-4px 6px` (left and down), both violate light-from-above rule | styles.css:110-111 `.card-shadow-a { box-shadow: 3px -2px 9px rgba(0,0,0,0.35); }` and `.card-shadow-b { box-shadow: -4px 6px 2px rgba(0,0,0,0.5); }` [used in: invoices.html] | VR5.1 | Use consistent shadow direction (top-left light source): `box-shadow: 0 2px 8px rgba(0,0,0,0.1)` for raised, `inset 0 1px 2px rgba(0,0,0,0.05)` for inset. Remove inconsistent x-offset and y-offset that suggest light from other directions. |
| 11 | Major | Global | H | No landmarks defined; no `<header>`, `<nav>`, `<main>`, `<footer>` semantic elements on any screen; blocks screen-reader navigation | scan.py: "[3] missing landmarks... no <header>, <nav>, <main>, <footer>" on index.html, invoices.html, signup.html | UR10.6 | Wrap topbar in `<header>` with `<nav>` for `.topbar .nav`; wrap main content in `<main>`; wrap footer in `<footer>`. Keep skip link after opening body tag. |
| 12 | Major | Global | H | No skip-to-content link; screen-reader and keyboard users must traverse utilities and nav on every screen | scan.py: "[3] no skip-to-content link" on all three screens | UR10.6 | Add `<a href="#main" class="sr-only">Skip to main content</a>` as first element after `<body>`, styled to show only on focus; target the `<main>` element with `id="main"`. |
| 13 | Major | signup | G | Reset button wipes form without confirmation; "Clear form" button violates UR9 (forms should minimize friction, not destroy work) | signup.html:67 `<button type="reset" class="btn btn-blue">Clear form</button>` | UR9 | Remove reset button entirely. Keep submit. If user wants to clear, they can reload or manually delete; destructive action should require confirmation, not offer a button. |
| 14 | Major | invoices | B | invoices.html has no `<h1>` element; screen name is missing from markup; breadcrumb shows "Launchpad / The Vault / Sent / INV-2041" but does not replace heading | invoices.html:1-97 no `<h1>`; scan confirms "invoices.html: 0 <h1>" | UR6.3, UR10.6 | Add `<h1>INV-2041</h1>` or `<h1>The Vault: Sent - INV-2041</h1>` after breadcrumb; make it prominent and match the clicked link ("The Vault"). Breadcrumb assists, does not replace. |
| 15 | Major | signup | G | Help text is verbose and instructional; explains how to use standard form controls (click field, type answer, use dropdown) | signup.html:35-36 `.help` paragraph: "The following form is designed to collect the information that we need in order to create your account and to help us serve you better. Please fill in each of the text fields below by clicking on the field and typing your answer. Use the drop-down menu to select your occupation. When you have completed all of the fields, click the button at the bottom of the form to submit it." | UR5, UR8 | Remove all instructions on how to operate form controls (they are standard). Keep only: why this form exists (create account) and what happens next. Remove "Fields cannot be left blank" (required attr shows this). |
| 16 | Major | signup | G | Placeholder text is hint, not label; "Card number (no spaces or dashes)" tells user what is expected but must be deleted before typing | signup.html:57 input type="text" name="cc" placeholder="Card number (no spaces or dashes)" pattern="[0-9]{16}" required - text is lost on focus | UR9 | Use `<label>` for all fields. Move format instructions to aria-description or helper text *outside* the input, or use constraint attributes (`inputmode="numeric"`) and document format near the label. |
| 17 | Major | Global | B | Brand mark "Ledgerly" does not link home; UR6.1 requires either logo link home or explicit Home item in nav | styles.css and all .html files: `.brand` has no href; nav has no Home link | UR6.1 | Wrap brand in `<a href="index.html">` or add `<a href="index.html" class="nav-item">Home</a>` to nav list. Both are acceptable; one is required. |
| 18 | Major | Global | E | Font-weight 300 used on body and headlines (hero h1, hero .motto); 300 weight is too light for UI per VR1 (minimum 400, prefer 500+600/700 for hierarchy) | styles.css:3 body { font-weight: 300; }, line 40 .hero h1 { font-weight: 300; } [used in: index.html]; line 94 .kv td { font-weight: 300; } [used in: invoices.html] | VR1 | Body should default to 400 (normal) or 500. Hierarchy uses weight: normal text 400, secondary 500, primary 600–700. Remove 300 entirely from UI. |
| 19 | Major | index | F | Hero motto text contrast fails: #9a9a9a on #2456c9 = 2.30:1 (needs 4.5:1 for normal text) | styles.css:41 `.hero .motto { color: #9a9a9a; font-size: 17px; }` on `.hero { background: #2456c9; }` [used in: index.html]; contrast check: 2.30:1 FAILS | VR4 | Lighten text to white or near-white (#f0f0f0) for contrast on blue, or lighten background. Test: white on #2456c9 should be ~9:1. |
| 20 | Major | index | F | Hero paragraph contrast fails: rgba(255,255,255,0.45) on #2456c9 = 2.55:1 (needs 4.5:1) | styles.css:42 `.hero p { color: rgba(255,255,255,0.45); font-size: 13px; }` on blue background [used in: index.html]; contrast check: 2.55:1 FAILS | VR4 | Use white text (no alpha) or increase alpha to 1.0. rgba(255,255,255,0.45) suggests attempted hierarchy but fails. Hierarchy within a colored region should use hue rotation or opacity in greys, not translucent white. |
| 21 | Major | invoices | B | Sidebar link color #1a6fe0 on background #dfe6f5 fails contrast: 3.82:1 (needs 4.5:1 normal text or 3:1 large/UI boundary) | styles.css:85 `.sidebar a { color: #1a6fe0; }` on `.sidebar { background: #dfe6f5; }` [used in: invoices.html]; contrast check: 3.82:1 FAILS for text | VR4 | Darken link text to #1551a8 or darker blue, or adjust background tint. Test darkened link for pass at 4.5:1 on current background. |
| 22 | Major | index | F | Green button contrast fails: white text on #1fa34a (button-blue) = 3.28:1 (needs 4.5:1 for bold 16px) | styles.css:57 `.btn-green { background: #1fa34a; }` with inherited `.btn` white text [used in: index.html, invoices.html]; contrast check: 3.28:1 FAILS bold | VR4 | Use darker green (#147f38 or similar) or white text on light green tint instead. Or use dark text on light tint. White on #1fa34a is not accessible. |
| 23 | Major | index | F | Orange button contrast fails: white text on #ee7d11 = 2.77:1 (needs 4.5:1 for bold 16px) | styles.css:58 `.btn-orange { background: #ee7d11; }` with inherited white text and rounded borders [used in: index.html, invoices.html]; contrast check: 2.77:1 FAILS bold | VR4 | Use darker orange (#c4611a) or white text on light orange tint. #ee7d11 is too light for white text. |
| 24 | Major | invoices | D | Sidebar width 25% creates uneven layout; fixed percentages waste horizontal space on large screens and force sidebar too narrow on mobile | styles.css:84 `.sidebar { width: 25%; }` `.main { width: 75%; }` [used in: invoices.html] | VR2 | Use `width: 200px` or `width: 240px` (fixed) for sidebar instead of 25%. Main content uses remaining space via flex. This scales better and keeps sidebar at readable width. Check mobile: may need full-width stacked layout at 400px. |
| 25 | Major | invoices | H | Missing h1 and landmarks mean screen-reader users cannot navigate to content; no way to skip utility nav and sidebar on a task-focused app screen | invoices.html lacks `<h1>`, `<header>`, `<nav>`, `<main>` landmarks | UR10.6 | Add all four landmarks. h1 should be in `<main>`. Skip link targets `<main>`. See finding 11. |
| 26 | Minor | Global | E | Font sizes include em and % units that nest off-scale; `.btn 1em`, `.formwrap h1 2.5em`, `.help 0.875em` and `.help .tiny 0.875em` produce unpredictable computed values | styles.css:45 `.btn { font-size: 1em; }`, line 115 `.formwrap h1 { font-size: 2.5em; }`, line 116 `.help { font-size: 0.875em; }`, line 117 `.help .tiny { font-size: 0.875em; }` | VR3 | Use px or rem only. `1em` on button (base 15px) = 15px, 2.5em on h1 (on body 15px) = 37.5px, but if nested differently = different result. Standardize to px: h1 32px, button 14px, helper 13px. |
| 27 | Minor | index | A | Jargon product names: "Hive", "Pulse", "Toolbox" are internal product codenames, not descriptive section titles | index.html:26-28 nav items "Hive", "Pulse", "Toolbox" - each needs a descriptor or one-word clear name | UR2 | Rename to clear categories: e.g., "Chat" (for Hive), "Analytics" (for Pulse), "Tools" (for Toolbox). Or use descriptors in UR6 pattern (section name in nav, with description on first screen). |
| 28 | Minor | Global | F | Color palette is uncoordinated: 22 distinct colors with 15 unrelated greys, no temperature consistency, many one-off values | scan.py: "colors: 22 distinct (15 neutral greys)"; greys include #999, #aaa, #4d4d4d, #555, #9a9a9a, #9b9b9b, #bbb, #c9c9c9, #dfe6f5, #e8e8e8, #eee | VR4 | Define a 10-color grey palette (consistent temperature, e.g., all cool or all warm), name them (text-primary, text-secondary, border, bg-tint, etc.), and use tokens. Define primary palette (blue shades), semantic (green, red), and use systematically. Replace all one-off hex values. |

---

## System health

Enumerated from scan.py:

- **Font sizes:** 14 distinct (13, 14, 15, 16, 17, 21, 22, 46px regular; 0.875em, 1em, 2.5em nested; 11, 12, 18px also present). Many near-neighbor sizes (13/14/15) with no scale; em units nest. **No type scale; needs constraint.**
- **Font weights:** 2 distinct (300, 700). No weights in range 400–600; 300 too light per VR1. **Recommend: 400 (normal), 500 (secondary), 700 (primary).**
- **Line-height:** 1.2 on body (tight for UI; 1.4–1.5 recommended for readability).
- **Colors:** 22 distinct (15 neutral greys). Greys are inconsistent temperature and value; no palette. Primaries: #1a6fe0 (blue), #1fa34a (green), #ee7d11 (orange), #e01a1a (red), #c9c9c9 (grey). **No tokens; 15+ one-off values.**
- **Spacing/margin/padding/gap:** 18 distinct (3, 4, 6, 7, 8, 9, 10, 12, 13, 14, 16, 18, 20, 22, 26, 30px; 0.6em, 1.1em nested). Heavy use of 10px and 8px, but no 2x rule for outside-group vs inside-group gaps. **No scale; needs: 4, 8, 12, 16, 24, 32px minimum.**
- **Shadows:** 2 distinct (both with incorrect direction: 3px -2px and -4px 6px instead of consistent top-left light).
- **Border radius:** 3 distinct (0, 4px, 18px). One `border-radius: 0` (hard corners), 4px (buttons), 18px (one button). **No consistency.**
- **Borders:** 17 declarations, all 1px solid #999. Heavy use for every panel/field/region. **No separation by spacing/background first.**
- **Custom properties (tokens):** 0. **Design system does not exist.**
- **@media queries:** 0. **No responsive design; mobile layout is not designed (confirmed in mobile screenshots: full-width nav, sidebar not reflow, form at 100% width).**
- **Declarations using var():** 0. **No variables used.**
- **Declarations using raw values:** 199. **All hardcoded; no reuse.**

**System diagnosis:** Product has no design system. Requires immediate build of minimal token system (type scale, color palette with 8–10 shades per hue, spacing scale, radius family). Mobile layouts are not designed (0 media queries); form and data-dense screens need breakpoints. Font-weight 300 throughout makes text hard to read and provides no hierarchy. Colors are arbitrary; no semantic mapping. Shadows violate VR5 light-direction rule. Current architecture will compound bugs and maintenance debt.

---

## What's working

- **Navigation structure:** Persistent nav shows all sections consistently across screens (Launchpad, The Vault, Hive, Pulse, Toolbox); order and names identical. Sidebar on app screen (All, Drafts, Sent, Overdue, Paid, Recurring) is logical and scannable.
- **Layout skeleton:** Three-screen pattern (landing, app, form) is clear; flex layout for sidebar + main content is sound before fixing width issues.
- **Action placement:** Destructive actions (Delete on invoices, Archive in table) are not emphasized as primary; "Send Reminder" is primary, others secondary (though still competing). This follows hierarchy intent, if not execution.
- **Breadcrumb structure on invoices:** "Launchpad / The Vault / Sent / INV-2041" provides good wayfinding, though needs h1 to complete UR6.

---

## Not verified

- **Real content behavior:** Stub links and dummy images (example.com, people/a.jpg) are fixtures. Real data (invoice list, metrics refresh, form submission) behavior not tested.
- **Keyboard navigation:** Screenshots show visual state only. Tested clicking vs tabbing? Focus indicators present? Dropdowns operable with arrow keys?
- **Screen reader output:** No VoiceOver/NVDA testing. Landmark and label structure will fail, but real form readback unknown.
- **Mobile responsiveness:** 400px screenshot shows no stacking or reflow (0 media queries). Layout breaks (sidebar stays 25%, columns don't reflow, promo grid may squeeze). Cannot verify without testing CSS fixes.
- **Color contrast under zoom/magnification:** Tested at system default size (15px body); user at 200% zoom may see different line-length and measured contrast will differ if text size changes line-height.
- **Real users signing up or using invoices:** Heuristic review only. UR7 first-screen clarity and signup friction should be validated in a usability test; see `usability-test-script.md` for facilitation approach.

A usability test with 5–6 users attempting (1) to understand Ledgerly from the landing page and sign up, and (2) to find and act on an overdue invoice on the app screen, would confirm whether hierarchy, clarity, and task flow work in practice.

---

## Summary counts

- **Total findings:** 28
- **Critical:** 9 (form accessibility, value prop, input patterns, system absence, layout)
- **Major:** 16 (contrast, landmarks, navigation, weight, reset button)
- **Minor:** 3 (font nesting, jargon names, color palette)

**High-impact fixes to prioritize:** Remove card number from signup (#4), add labels to all inputs (#7, #8), remove reset button (#13), add landmarks and skip link (#11, #12, #17), fix hero contrast (#19, #20), build design system (#3). These 6 fixes address 9 of 28 findings and unblock keyboard, screen-reader, and visual-clarity tasks.
