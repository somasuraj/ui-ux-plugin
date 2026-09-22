# Answer key - Ledgerly fixture (testers must NOT see this)

Scoring: a flaw counts as FOUND if the report names the problem and points at the right place (file/element), in findings or top fixes. Partial = mentions the area but not the specific problem.

## Usability flaws [Krug]
K1  Clever/insider nav names (Launchpad, The Vault, Hive, Pulse, Toolbox) - index/invoices/signup nav
K2  Vague motto not a tagline ("Work. Smarter.") - index hero
K3  Happy talk: "Welcome to Ledgerly!" h1 + mission-statement paragraph - index hero
K4  Happy talk section-front: "About this section" blurb - index .about
K5  No clear starting point: 5 equal CTAs; real signup is a plain-looking span at page bottom - index
K6  First screen fails "what is this / what can I do" - value only appears in bullets at the bottom - index
K7  Search: "Quick Find" wording + scope dropdown + instruction text as value + button with no label - index .finder
K8  Forced thoughtful choice: "Which one are you? Personal / Business / Professional" - index .chooser
K9  Promo overload (8 shouting promos, !!!) on first screen - index .promo-grid
K10 Clickability: .fakelink looks like link but isn't; .ghostlink is a link but looks like text; .go is an unlabeled span button - index
K11 Site ID not top-left (brand is pushed to far right via order:3), and not a link home - all pages
K12 Too many utilities (9), more prominent (bold blue) than sections - index/signup
K13 You-are-here too subtle (#555 vs #4d4d4d) - styles .nav a.active
K14 Page name missing / mismatch: clicked "The Vault", title says "Billing Documents Manager", no h1 on page - invoices
K15 Breadcrumbs misused: large bold, "/" separators, not at top-as-accessory, last item not distinguished, acting as page name - invoices .crumbs
K16 Local nav (sidebar) has no current-item indicator - invoices .sidebar
K17 Form asks for unneeded data: phone, address, DOB, occupation, household income, card number for a free signup - signup
K18 Rigid input formats (digits only phone, no spaces in card, exact DOB) - signup
K19 Instructions paragraph above form nobody will read - signup .help
K20 Full persistent nav + 8 utilities on a form page (should be minimal) - signup
K21 Page name mismatch: link says "Join"/"Create your free account", page says "Become a Ledgerly Insider"; <title> just "Ledgerly" - signup
K22 Generic error "Error: invalid input." not tied to field, no recovery; "Clear form" reset button styled same as Submit - signup
K23 Fake sincerity "Your privacy is very important to us." while over-collecting - signup
K24 Fees hidden in tiny light footer text (3.5% processing fee, taxes) - index .footer
K25 Empty state: "No data." with useless filters/sort/export shown - invoices RECURRING panel

## Accessibility
A1  Inputs with placeholder only / span instead of <label> - signup
A2  Images without alt - index .bigicon, signup avatars
A3  Non-keyboard-operable click targets (span onclick) - index .go, .ghostlink
A4  No skip link / no landmarks (all divs), no <main>/<nav>/<header>
A5  Contrast failures: footer #bbb on white, .empty #aaa, hero text rgba white .45 on blue, btn-grey #9b9b9b on #c9c9c9
A6  Color alone for meaning: metrics up/down only colored, no arrows/sign - invoices .metric

## Visual flaws [RUI]
R1  Grey text on colored bg (.hero .motto #9a9a9a on blue) and translucent white (.hero p)
R2  Too many font sizes with near-duplicates (11,12,13,14,15,16,17,18,21,22,46 + em) - no type scale
R3  Body weight 300 for UI text (also h1 300)
R4  Pure black text #000, no grey hierarchy; all text same color/weight => no hierarchy
R5  em-based nested type (.help .875em > .tiny .875em; .btn 1em/em padding; h1 2.5em)
R6  Spacing one-offs/no scale (6,7,9,10,13,14,22px...) and cramped overall (line-height 1.2, tiny padding)
R7  Ambiguous spacing: .field .lbl margin-bottom 10 == input margin-bottom 10 == field gap 10
R8  Button hierarchy: every action solid & loud; 5 solid buttons invoices actions; Delete is biggest/red/uppercase
R9  Disabled-looking primary-ish action: "Mark as paid" in btn-grey looks disabled; Export same
R10 Inconsistent radius (4px, 18px, 0) across buttons
R11 Borders everywhere (#999 on every panel, cell, promo) - use spacing/bg/shadow instead
R12 label: value wall in .kv table - no hierarchy; email/phone/amount need no labels; "12 days overdue" combine
R13 Section titles shouting: ALL-CAPS 22px h2 with border, bigger than content; all-caps without letter-spacing
R14 Numbers left-aligned in table (Amount column) - right-align
R15 Centered long-form text (.about paragraph, hero paragraph) + full-width line length (no max-width / measure)
R16 Sidebar width 25% (percent) - should be fixed; also content stretched full width, no max-width anywhere
R17 Shadows: inconsistent light source (one up-right, one down-left), no elevation scale, harsh
R18 Scaled-up 16px icon to 96px (.bigicon check-16.svg)
R19 Bullets line spacing == line-height (li margin 0, lh 1.2) ambiguous; could use icons
R20 No color system: many raw hexes, four saturated hues competing (blue/green/orange/red), no shades/tokens
R21 Line-height 1.2 for body text too tight, esp. at full-width measure
R22 User/people images fixed height only - no fixed container/cover crop (signup avatars) [minor]

## Decoys (should NOT be flagged as problems; ideally praised or left alone)
D1  Dense invoices table density - deliberate for a data table (flagging borders/alignment inside it is fine; flagging "too dense, add whitespace" as a major issue = false positive)
D2  "Archive" as quiet tertiary destructive action - correct per RUI
D3  System font stack - correct safe choice
D4  lang attribute + viewport meta present - fine

Total planted: K 25 + A 6 + R 22 = 53
