# UI/UX audit: Ledgerly web app

**Scope:** Three screens reviewed: index.html (landing), invoices.html (app dashboard), signup.html (registration form). **Evidence:** Full code read (HTML/CSS only, no live rendering).  
**Assumed top user tasks:** 1) Understand Ledgerly's value and decide to sign up 2) View and manage invoices 3) Create an account

## Skill harness notes

**Skill files read:**
- `references/audit-checklist.md` - contains report format and triage rules
- `references/visual-design.md` - hierarchy, spacing, typography, color, depth principles
- `references/usability.md` - clarity, navigation, forms, accessibility principles

**Clarifications/assumptions:**
- No running app or screenshots available - audit based on code inspection only
- "Active" navigation indicator uses color only (#4d4d4d vs #555) which is very subtle
- Form error message (`<div class="err">`) is hardcoded to always display
- Buttons use em-based padding which creates inconsistent sizing relative to font-size changes
- Placeholder text is used as form labels on most fields, with no associated `<label>` elements

## Verdict

The app has significant usability and clarity problems that block all three top tasks. The landing page doesn't explain what Ledgerly does (hero paragraph is impenetrable jargon), offers five competing CTAs with no primary action, and displays promo overload (8 boxes). Navigation active states are too subtle. The signup form asks for payment information without trust-building context, uses rigid input validation, and relies on placeholder text instead of proper labels. Visual design lacks systems: button styles, shadows, spacing, typography, and colors are inconsistent throughout. These issues would cause users to leave before signing up or creating an account.

## Top fixes (do these first)

1. **Replace hero paragraph with plain-language value statement** - Users can't tell what Ledgerly does; current text is corporate jargon ("synergistic solutions", "leverage core competencies"). Effort: S
2. **Reduce CTAs to 1 primary + 1 secondary; remove 3 less important buttons** - Five equal CTAs create visual chaos and make the primary action unclear. Effort: S
3. **Make active nav indicator bold + color (not color alone)** - Current subtle color change (#4d4d4d) fails the "you are here" trunk test. Effort: S
4. **Add proper `<label>` elements to form fields; remove placeholder-only labels** - Most form inputs lack associated labels (accessibility failure, no keyboard affordance). Effort: S
5. **Remove or reduce promo boxes from 8 to 2-3** - Promo grid creates visual noise and competes with core content; contradicts no up-front promos rule. Effort: S
6. **Remove rigid input validation; accept flexible formats** - Phone (10 digits only), card (16 digits, no spaces), DOB (MM/DD/YYYY exactly) should accept spaces, dashes, alternative formats. Effort: M
7. **Hide error message until validation actually fails** - Error div is always visible (class="err" with text), not triggered by interaction. Effort: S
8. **Standardize button appearance: border-radius, padding, font-size** - Buttons have radius 4px, 18px, or 0px; font-size varies; padding uses em (scales inconsistently). Effort: M

## Findings

| # | Severity | Area | Finding | Evidence | Principle | Fix |
|---|----------|------|---------|----------|-----------|-----|
| 1 | Critical | Clarity | Hero paragraph is incomprehensible jargon; doesn't answer "What is this?" | index.html:47 "synergistic solutions... leverage core competencies... unlock transformative value" | Don't Make Me Think: Five questions must be answered at a glance | Replace with 1-2 sentence benefit statement in plain English (e.g., "Send invoices and get paid faster. Ledgerly automates billing so you focus on growing your business.") |
| 2 | Critical | Clarity | No single primary action on landing; five equal CTAs compete for attention | index.html:49-53 (Learn More, Watch Video, See Pricing, Read Blog, Let's Go) | Hierarchy: one primary action per screen (solid), secondary (outline/muted) | Remove Learn More, Read Blog, Watch Video (lower priority). Keep See Pricing + Let's Go. Make Let's Go primary (solid blue), See Pricing secondary (outline). |
| 3 | Critical | Navigation | Active nav indicator too subtle; fails trunk test ("you are here" must use two distinctions, not one) | styles.css:25 `.nav a.active { color: #4d4d4d; }` - only color differs from #555, not bold | Navigation: active indicator must contrast strongly (color + weight) | Add `font-weight: 700;` to `.nav a.active` |
| 4 | Critical | Accessibility | Most form fields lack `<label>` elements; placeholder text used as label only | signup.html:41-42,44-47,49-56 (Email, Password, Phone, Address, etc. all have placeholder= but no label) | Accessibility: every form control needs an associated label | Add `<label>` tags with `for` attribute linking to input `id` (e.g., `<label for="email">Email</label><input id="email" type="email" ...>`) |
| 5 | Critical | Forms | Form asks for payment card number without trust-building context or HTTPS indicator | signup.html:57 (Card number field in standard signup form) | Goodwill: never hide what people want or ask for sensitive data unexpectedly | Move card field to separate payment setup screen *after* account creation, with trust signals (lock icon, SSL badge, privacy statement) |
| 6 | Critical | Clarity | "Which one are you?" section offers three unclear options (Personal, Business, Professional) with no explanation | index.html:58-61; styles.css doesn't show hover/selection states | Clarity: no up-front decisions requiring thought | Add 2-3 word descriptions under each option (e.g., "Personal: for freelancers"; "Business: for teams") OR remove if not central to signup flow |
| 7 | Critical | Forms | Error message displayed always, not triggered by validation | signup.html:58 `<div class="err">Error: invalid input.</div>` (hardcoded, no conditional display) | States: error state should only appear after failed validation | Hide error div by default; show only when validation fails. Use JavaScript or CSS `:invalid` pseudo-class. |
| 8 | Major | Words | Form instructions (96 words) attempt to explain what should be self-explanatory design | signup.html:36 (help paragraph tells users "click field and type", "use drop-down", "click button") | Words: cut half the words, then half again. No instructions unless UI can't be clear. | Delete help paragraph entirely. Redesign form for clarity: group related fields, add section headings (Personal, Address, Payment), use real labels. |
| 9 | Major | Forms | Form validation requires exact input formats with no normalization | signup.html:43 (phone pattern="[0-9]{10}"), 47 (DOB "MM/DD/YYYY exactly"), 57 (CC pattern="[0-9]{16}") | Forms: accept flexible formats and normalize | Remove pattern attributes. Accept phone with spaces/dashes, normalize to digits. Accept any DOB format, normalize. Accept CC with spaces, normalize. |
| 10 | Major | Visual noise | 8 competing promo boxes on landing page all equally prominent | index.html:64-73; styles.css:63-66 (grid-template-columns: repeat(4, 25%); all same styling) | Clarity / Hierarchy: landing page shouldn't be overloaded with promos competing with main point | Remove 4-5 lowest-priority promos (e.g., Award Winner, Partner Spotlight, Refer friend). Keep 2-3 (e.g., Summer Sale, Ledgerly Pulse). Emphasize highest-priority with larger card or color. |
| 11 | Major | Design system | Buttons have inconsistent styling: border-radius 4px, 18px, or 0px; padding and font-size vary | styles.css:45-60 (.btn-orange has radius 18px; .btn-grey has radius 0px; .btn-red has font-size 18px and larger padding) | Hierarchy / Design system: establish constraints with systems | Standardize button treatment: all primary/secondary use radius 4px. Remove special cases. Use consistent padding (0.6em 1.1em). All buttons same height/baseline. |
| 12 | Major | Design system | Shadows random and inconsistent light source | styles.css:110-111 (.card-shadow-a: 3px -2px; .card-shadow-b: -4px 6px) - opposite directions | Depth: light source must be consistent; shadows express elevation | Define 3 elevation levels with consistent shadow direction (light from top-left). E.g., level 1: `0 2px 4px rgba(0,0,0,0.1)`, level 2: `0 4px 8px rgba(0,0,0,0.15)` |
| 13 | Major | Layout | Topbar cramped and cluttered; padding 6px, line-height 1.2, 9 utility links for non-logged-in users | styles.css:16-22, 27-28; index.html:12-22 | Layout/Goodwill: generous whitespace; don't overload first screen | Increase topbar padding to 12-16px. Reduce utility links from 9 to 4 (Help, Blog, Join, Log in). Group remaining links. Increase line-height to 1.5. |
| 14 | Major | Clarity | Navigation section names are unclear internal jargon ("Launchpad", "The Vault", "Hive", "Pulse", "Toolbox") | index.html:24-28; invoices.html:18-22 | Clarity: use obvious words, no jargon or internal names | Rename: "Launchpad" → "Dashboard", "The Vault" → "Invoices", "Hive" → "Team" (if applicable), "Pulse" → "Analytics", "Toolbox" → "Settings". Match user language. |
| 15 | Major | Accessibility | No focus/hover states defined for interactive elements | styles.css has no :hover, :focus, :active rules | Accessibility / States: fully keyboard operable with visible focus; all interactive elements have hover/active states | Add CSS rules: `a:hover { text-decoration: underline; }`, `a:focus { outline: 2px solid #1a6fe0; }`, `button:hover { opacity: 0.9; }`, etc. |
| 16 | Minor | Clarity | Motto "Work. Smarter." is vague; doesn't convey benefit | index.html:46; styles.css:41 | Clarity: tagline should state value plainly | Replace with benefit-focused statement (e.g., "Send Invoices. Get Paid." or "Billing Simplified.") |
| 17 | Minor | Hierarchy | Form labels and helper text use nested em sizing; not explicit values | signup.html:35-36 (help uses 0.875em which compounds); styles.css:116 (.help { font-size: 0.875em; }) | Typography: use px/rem, not em for scales | Define explicit font sizes in px/rem (e.g., .help { font-size: 13px; } not 0.875em). Establish type scale: 12, 14, 16, 18, 24, 32px. |
| 18 | Minor | Words | "Cancel my subscription" link on signup form; wrong context (user has no subscription yet) | signup.html:69 | Clarity / Goodwill: copy must make sense in context | Remove link from signup form. Move to account settings/billing screen where relevant. |
| 19 | Minor | Design system | Color values hardcoded throughout; no token/variable system | styles.css has #1a6fe0, #1fa34a, #e01a1a, #999, #aaa, etc. scattered with no central definition | Design system: consolidate into tokens | Define color tokens: primary shades (100-900), semantic (red/green/warning), greys. Map all inline colors to tokens. E.g., `--color-primary-600: #1a6fe0;` |
| 20 | Minor | Clarity | Avatar selection at bottom of signup form; purpose unclear | signup.html:60-64 (avatar-row with 3 images, no explanation) | Clarity: everything interactive needs clear purpose | Remove OR explain (if selecting support contact: add label "Choose your support advisor"). Images need alt text. |
| 21 | Minor | Design system | Font sizes inconsistent; many values without clear scale (11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 46px) | styles.css lines 5, 24, 26-27, 31, 40, 42-43, 64, 69, 88, 91, 96, 101, 102, 103, 104, 107, 115, 120, 124 | Design system: establish constrained scale | Define 6-8 point scale: 12, 14, 16, 18, 24, 32, 42, 56px. Map all text to scale. Remove one-off values. |
| 22 | Minor | Accessibility | Images in avatar-row lack alt text | signup.html:61-63 `<img src="people/...">` with no alt attribute | Accessibility: images need meaningful alt or empty alt if decorative | Add alt="" (if decorative) or alt="Option 1", alt="Option 2", etc. (if selectable). |
| 23 | Minor | Navigation | Search ("Quick Find") includes scope dropdown with 4 options up front | index.html:30-39; styles.css:30-32 | Navigation: search should be box + button + label; scope only on results | Remove dropdown. Add simple search box. Show scope filter only after user submits search on results page. |
| 24 | Minor | Forms | Form field styling uses width: 100% and height: 26px (inconsistent with button heights) | styles.css:120 (.field input, .field select { height: 26px; }) vs buttons (no fixed height, padding-based) | Design system: standardize input/button sizing | Define input height (e.g., 40px). Make button height match (44px ideal for touch targets). Consistent padding. |

## System health

**Distinct values (actual count):**
- Font sizes: 12 distinct values (11px, 12px, 13px, 14px, 15px, 16px, 17px, 18px, 21px, 22px, 46px, 2.5em) - EXCESSIVE; scale should be 6-8
- Font weights: 2 (300, 700) - OK but too few; UI text below 400 is discouraged
- Colors: ~18 distinct hex values (#000, #1a6fe0, #1fa34a, #2456c9, #4d4d4d, #555, #9a9a9a, #999, #aaa, #e01a1a, #ee7d11, #c9c9c9, #9b9b9b, #bbb, #dfe6f5, #fff, + 3 rgba) - EXCESSIVE; should be 8-10 greys + 5-10 primary shades
- Spacing values: ~10 distinct (3px, 4px, 6px, 8px, 9px, 10px, 12px, 13px, 14px, 22px) - TOO MANY; scale should be 6-8 steps
- Shadows: 2 inconsistent values with opposite light directions - should be 3 elevation levels consistent
- Border-radius: 3 values (0px, 4px, 18px) - inconsistent; should standardize to 4px for most elements

**Which systems exist:** None formalized. All values are one-offs. No tokens, variables, or scale definitions in code.

**What needs consolidation:** Establish all four core systems first:
1. **Type scale:** Define 6-8 sizes in px/rem (12, 14, 16, 18, 24, 32, 42, 56px). Map all text to scale.
2. **Color tokens:** 8-10 greys, 5+ primary shades, semantic colors (red/green/warning). No inline hex values.
3. **Spacing scale:** 6-8 values (4px, 8px, 12px, 16px, 24px, 32px, 48px, 64px). Replace all padding/margin one-offs.
4. **Elevation scale:** 3-5 consistent shadows (all from same light source). Replace inconsistent shadows.

## What's working

- Responsive viewport meta tag is present (meta name="viewport")
- Global box-sizing: border-box applied (good reset)
- System font stack is modern and accessible
- Navigation is persistent and consistent across screens
- Sidebar layout on app page clearly separates navigation from content
- Data table structure is semantic (uses `<table>` properly)
- Color scheme (blue primary, green/orange secondaries, red semantic) is intentional
- Footer present on all pages with copyright

## Not verified

**What couldn't be checked (code-only audit, no live rendering):**
- Contrast ratios and WCAG compliance - text on colored backgrounds (hero paragraph on blue) needs ratio check
- Actual hover/focus appearance - no CSS states defined to test
- Placeholder text contrast - light text on input backgrounds often fails contrast
- Small-screen layout - code shows no media queries; grid likely breaks under 600px
- Page performance - no images rendered, links not functional
- Form validation behavior - error state is static, can't test real-time validation
- Keyboard navigation - no tabindex/focus management visible

**How to verify (suggested tests):**
1. **Contrast audit:** Run Lighthouse or WebAIM on live rendering. Check hero text on blue background, placeholder text, "Status: Overdue" in red
2. **Keyboard test:** Load in browser, tab through all elements. Every button/link must be reachable and focused. Try signup form with keyboard only (no mouse)
3. **Small-screen test:** Resize to 375px, 480px, 600px. Check sidebar, nav, form wrapping
4. **Usability test:** Watch 3-5 target users (freelancers/small business owners) land on index.html cold. Ask "What is this? Would you sign up?" Observe hesitations
5. **Form validation:** Test phone number with spaces, CC with dashes, DOB with slashes. Verify acceptance or error messaging
6. **Accessibility scan:** WAVE, Axe DevTools for missing labels, unlabeled images, keyboard traps

**Usability test plan** (see `usability-test-script.md` template):
- **Scenario 1:** "You're a freelancer. You need to send an invoice. Land on this site. What would you do?"
- **Scenario 2:** "Create an account. Walk me through the signup process and tell me if anything feels off."
- **Scenario 3:** "Find your past invoices and check how much one client owes you."

Priority: usability test on landing page and signup flow (highest friction points).
