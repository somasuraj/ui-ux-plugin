# UI/UX audit: Ledgerly

**Screens reviewed:** index.html (landing), invoices.html (app), signup.html (form)   **Evidence:** code read / scan.py / screenshots at desktop and 400px / live inspection
**Assumed top user tasks:** 1) Understand what Ledgerly does and sign up / log in 2) Manage and view invoice status 3) Complete account registration

## Verdict

Ledgerly shows significant foundational issues that block core tasks: excessive CTAs and marketing noise overwhelm the landing page, the signup form collects unnecessary personal data with accessibility barriers, and key pages lack proper semantic structure (no h1 on invoices, no landmarks). The app screens are dense but functional. These are beyond cosmetic fixes and require structural decisions before layout tweaks.

## Top fixes

1. **Remove unnecessary fields from signup form and add accessible labels** - The form collects household income and card numbers upfront (not needed for free signup), and 15 controls lack labels, blocking signup for screen-reader users - Critical - findings 1, 2, 16
2. **Consolidate hero CTAs and remove "Which one are you?" decision** - Five competing buttons and a confusing segmentation make the primary action unclear; each belongs elsewhere (pricing, video link, etc.) - Major - findings 3, 4
3. **Reduce promo grid to max 3-4 cards** - Eight cards with loud red titles and exclamation marks swamp the main proposition; rotate or move to dedicated page - Major - findings 5, 6
4. **Add semantic HTML structure and accessibility** - Landmarks (<header>, <nav>, <main>), skip link, proper h1 on invoices, and form labels transform keyboard and screen-reader usability - Major - findings 16, 17, 18, 19, 20, 21
5. **Fix contrast on hero paragraph, buttons, and footer** - Hero paragraph is 2.55:1 (fails 4.5:1 normal text), footer 1.92:1, several button labels and accents below 3:1; apply stronger colors - Major - findings 7, 8, 10, 22
6. **Replace rigid input patterns with flexible validation** - Phone and card patterns reject valid formats (spaces, dashes); accept input and normalize server-side - Major - finding 14

## Coverage

| Screen | A | B | C | D | E | F | G | H |
|--------|---|---|---|---|---|---|---|---|
| Global | - | - | - | 1 | 2 | 1 | - | 4 |
| index  | 2 | ok | 2 | ok | ok | 4 | 1 | 1 |
| invoices | ok | 1 | 1 | 1 | ok | 2 | ok | ok |
| signup | 1 | ok | ok | ok | 1 | ok | 3 | 2 |

## Findings

| # | Sev | Screen | Area | Finding | Evidence | Rule | Fix |
|---|-----|--------|------|---------|----------|------|-----|
| 1 | Critical | signup | H | Screen-reader and keyboard users cannot complete signup: 10 of 15 form inputs have only placeholder text, no associated labels; placeholder alone does not expose the field's purpose to assistive technology | signup.html:40-57 | UR10.5 | Add `<label for>` tied to each input with descriptive text; placeholder alone is not a label |
| 2 | Critical | signup | G | Signup task is compromised: form collects unnecessary sensitive data upfront (household income, full credit card number) for a free account; users must provide this before proceeding, when the task needs only name/email/password | signup.html:56-57 | UR9 | Remove income and card fields; collect payment info only at checkout if needed |
| 3 | Critical | index | C | Primary signup task is blocked: five CTAs in hero compete equally for attention; first-time visitor cannot identify what to do next ("Learn More", "Watch Video", "See Pricing", "Read the Blog", "Let's Go!" all solid buttons, same visual weight) | index.html:49-53 | UR1, VR1 | Keep only one solid primary button (e.g. "Sign up free"); move others to dedicated pages or footer |
| 4 | Major | index | A | "Which one are you?" section asks users to choose Personal/Business/Professional with no context on what these mean or why the choice matters | index.html:57-62 | UR2, UR7 | Either explain each option inline (one sentence per), or remove and let users discover after signup |
| 5 | Major | index | C | Promo grid of 8 cards with bright red all-caps titles and exclamation marks creates visual noise that swamps the main value proposition | index.html:64-73 | UR3, VR1 | Reduce to 2-4 most important promos; demote the rest to a dedicated "News" page or carousel |
| 6 | Major | index | A | Blurb in hero is generic marketing prose ("synergistic solutions that empower...") rather than a clear differentiator | index.html:47 | UR5, UR7 | Rewrite to: what Ledgerly *is*, why it's better, in ~15 words. Current form fails the "would a newcomer say that?" test |
| 7 | Major | index | F | Hero paragraph text (rgba(255,255,255,0.45)) is 2.55:1 contrast on #2456c9 background, below 4.5:1 WCAG AA normal text threshold | styles.css:42 | VR4 | Use solid white or off-white for body text on the blue background |
| 8 | Major | index | F | Hero motto "Work. Smarter." is 2.30:1 contrast (#9a9a9a on #2456c9), below 4.5:1 threshold | styles.css:41 | VR4 | Use darker grey or white; test at 4.5:1 minimum for body-sized text |
| 9 | Major | invoices | B | No h1 or screen name on invoices.html; breadcrumb "Launchpad / The Vault / Sent / INV-2041" reads as navigation, not a screen identifier | invoices.html:1-24 | UR1, UR6 | Add prominent h1 above main content or integrate into breadcrumb styling (e.g. "INV-2041" bold and large) |
| 10 | Major | invoices | F | Footer "Copyright 2026..." text is 1.92:1 (#bbb on white), below 4.5:1 WCAG AA | styles.css:124 | VR4 | Use #666 or darker grey; footer text must meet minimum contrast |
| 11 | Major | invoices | C | Key-value table layout uses many label-value pairs in a dense format that is harder to scan than data grouped by importance | invoices.html:42-52 | VR1 | Highlight the most critical fields (Status, Amount, Days Overdue) prominently; demote others to expandable detail or secondary position |
| 12 | Major | invoices | D | Sidebar width is 25% (percent-width, not fixed); sidebar should be fixed width so main content width adapts predictably | styles.css:84 | VR2 | Change to `width: 240px;` (or similar fixed px value); `.main` remains `width: 75%` or switches to `flex: 1` |
| 13 | Major | invoices | F | Two box-shadows cast from wrong direction: "3px -2px..." (negative y) and "-4px 6px..." (negative x); light should come from above | styles.css:110-111 | VR5 | Fix to positive offsets from top-left: e.g., `2px 4px 8px rgba(0,0,0,0.15)` |
| 14 | Major | signup | G | Rigid input patterns (phone `[0-9]{10}`, card `[0-9]{16}`) reject valid formats like "(555) 123-4567" or "5551234567"; users cannot enter data they think is correct | signup.html:43, 57 | UR8, UR9 | Remove `pattern=` attributes; accept flexible input and normalize server-side (trim spaces, strip dashes/parens) |
| 15 | Major | signup | G | Reset button ("Clear form") appears beside Submit; wipes all user input if clicked by accident | signup.html:67 | UR9 | Remove reset button; or if genuinely needed, place far from Submit and label it "Start over" |
| 16 | Major | signup | H | Email input has only placeholder ("Email"), no associated label | signup.html:41 | UR10 | Add `<label for="email">Email</label>` or add aria-label="Email" to input |
| 17 | Major | Global | H | No skip-to-main-content link on any page; keyboard users must tab through nav on every screen | index.html:11-30, invoices.html:11-25, signup.html:11-30 | UR10 | Add `<a href="#main" class="skip-link">Skip to main</a>` as first element; style to show only on focus |
| 18 | Major | Global | H | No semantic landmarks on any page (<header>, <nav>, <main>, <footer>); screen-reader users cannot navigate by region | index.html:11-42 (no <header>, <nav>, <main>; <div> tags used instead), invoices.html:11-92, signup.html:11-76 | UR10 | Wrap topbar in `<header>`, nav in `<nav>`, main content in `<main>`, footer in `<footer>` |
| 19 | Major | index | H | Heading-level jump from h1 to h3 (no h2); h2 appears later in "About this section" | index.html:45, 76 | UR10 | Either add h2 for sections, or move h2 before its content |
| 20 | Major | Global | H | Four images lack alt text: three avatars in signup and one icon in index features; screen-reader users hear nothing or hear file paths | index.html:81, signup.html:61, signup.html:62, signup.html:63 | UR10 | Add meaningful alt: `alt="Example team member"` for avatars, `alt="Check mark"` for icon; empty alt="" if decorative |
| 21 | Minor | Global | H | Click handlers on non-interactive elements: `<span onclick>` used in index.html:39 (search button) and index.html:88 (link), cannot be accessed by keyboard | index.html:39, 88 | UR10 | Change to `<button>` or `<a>` tags; ensure all interactive elements are focusable and keyboard-operable |
| 22 | Minor | index | F | Promo bold text (#ee7d11 on white) is 2.77:1 contrast, below 4.5:1 threshold for body text | styles.css:66 | VR4 | Darken orange to ~#c65c00 or use a darker accent; verify 4.5:1 |
| 23 | Minor | signup | A | Instruction text explaining how to fill the form ("Please fill in each of the text fields...") is classic happy talk; a clearer form design would make instructions unnecessary | signup.html:35-36 | UR5 | Reduce to one line: "All fields required." or remove entirely if form is self-explanatory |
| 24 | Minor | index | G | Placeholder text in Quick Find ("Type a keyword here...") looks like user input; misuses placeholder attribute | index.html:38 | UR5 | Use a label or aria-label instead; placeholder is for hints, not instructions |
| 25 | Minor | Global | E | Button text uses em padding and em font-size (1em, 0.6em, 1.1em), which nests off-scale when buttons inherit parent font-size | styles.css:47-48 | VR3 | Use px: `padding: 10px 18px; font-size: 14px;` |
| 26 | Minor | signup | E | Form h1 uses 2.5em (37.5px based on body 15px), creating a large jump; suggest 28-32px for consistency with index h1 (46px) | styles.css:115 | VR3 | Change to fixed px, e.g., `font-size: 28px;` |
| 27 | Minor | Global | F | Pure black text (#000) used on white background; softer black (#1a1a1a or #333) is easier on the eyes | styles.css:3, 8 | VR4 | Change body color to `#333` or `#1a1a1a` |
| 28 | Minor | index | F | Green button contrast (#1fa34a on white) is 3.28:1, below 4.5:1 for normal text (3:1 is only for large/bold text >= 24px or UI boundaries) | styles.css:57 | VR4 | Darken green to ~#146b2d; verify 4.5:1 for button labels |
| 29 | Minor | Global | E | 14 distinct font sizes in use (13, 14, 15, 16, 17, 18, 21, 22, 46, plus em variants); consolidate to 5-6 key sizes | scan.py output | VR3 | Define scale: 12, 14, 16, 18, 20, 28, 32px; replace near-duplicates |
| 30 | Minor | Global | D | Spacing values are fragmented (18 distinct values); no clear scale or system | scan.py output | VR2 | Define spacing scale: 4, 8, 12, 16, 20, 24px; replace one-offs like 3, 6, 7, 9, 10, 13, 14, 18, 22, 26, 30 |

## System health

**Font sizes:** 14 distinct (13, 14, 15, 16, 17, 18, 21, 22, 46 px; 0.875em, 1em, 2.5em). No scale. Recommend consolidating to 5-6 key sizes.

**Font weights:** 2 distinct (300, 700). No 400/500 medium weight. Hierarchy relies on color and size, not weight progression. Body is 300 (light), which reduces readability; should be 400.

**Line-height:** 1 value (1.2). Body text line-height of 1.2 is tight for comfortable reading; recommend 1.5 for body.

**Colors:** 22 distinct colors (15 neutral greys, 3 blues, 2 greens, 2 oranges, 1 red, 1 dark red, 5 other one-offs). No clear palette system or tokens. Greys lack consistent temperature; multiple near-duplicates (#999, #aaa, #bbb, #c9c9c9, #dfe6f5, #e8e8e8, #eee, #f5f5f5 apparent).

**Spacing/padding/gap:** 18 distinct values (3, 4, 6, 7, 8, 9, 10, 12, 13, 14, 16, 18, 20, 22, 26, 30, plus 0.6em, 1.1em). No scale. Recommend system: 4, 8, 12, 16, 20, 24.

**Box shadows:** 2 distinct (both directionally incorrect: "3px -2px 9px" and "-4px 6px 2px"). Should both come from top-left (positive x, positive y).

**Border radius:** 3 distinct (0, 4px, 18px). Minimal system; mostly square or pill buttons. Consistent.

**Borders:** 17 declarations. Overused for separation; could use spacing, background, or shadow instead.

**Media queries:** 0. No responsive CSS; layout is liquid/flexbox. Mobile screenshots show responsive behavior (likely flexbox reflow), but no deliberate small-screen design.

**CSS variables / tokens:** 0. All raw values in CSS; no design system.

**Interactive state rules:** No `:hover`, `:focus`, `:focus-visible`, `:active`, `:disabled` styles. Buttons and links have no visible feedback on interaction.

**Accessibility:** No skip link, no landmarks, 15+ form controls without labels, 4 images without alt, heading-level jump, click handlers on non-interactive elements, two inputs with non-interactive elements, no focus indicators.

## What's working

- **Navigation is persistent and consistent:** Same sections (Launchpad, The Vault, Hive, Pulse, Toolbox) on every screen at the same visual weight.
- **Invoices data is well-organized:** Key document information table is clear, and metrics are visually distinct (color + bold numbers for "Collected" / "Outstanding").
- **Mobile layout adapts gracefully:** Promo grid reflows to 1-2 columns, sidebar content becomes accessible, buttons stack at 400px.
- **Color coding for status is intuitive:** Red for overdue/negative, green for paid/positive, orange for secondary actions.
- **Form inputs have clear visual affordance:** Input borders and dropdowns are obvious; placeholder hints guide users toward format.

## Not verified

- **Real users signing up or managing invoices:** Heuristic review cannot confirm whether the 11-field form completion rate is actually blocked by missing labels, or whether users find the "Which one are you?" decision confusing. A moderated usability test with 5-6 target users on signup and invoice lookup tasks would confirm pain points and validate fixes.
- **Keyboard navigation and screen-reader experience:** No focus indicators visible, no landmarks defined; cannot verify that keyboard users can reach all controls or that screen readers announce context properly. Run NVDA or JAWS on each page.
- **Rendered contrast on actual displays:** Contrast was computed from declared colors; monitor calibration, brightness, and individual eyesight may shift perceived contrast. Test on a real monitor after color fixes.
- **Interactive states (:hover, :focus, :active):** No visible styles defined; test by tabbing through forms and hovering over buttons to confirm feedback exists or is missing.
- **Performance and load time:** No metrics captured. Check waterfall if the page feels slow (large promos or images).

## Offer

A usability-test plan is available in `usability-test-script.md` if validation with real users is prioritized. The top 3 task scenarios (sign up, manage invoice, view metrics) are candidates for testing.
