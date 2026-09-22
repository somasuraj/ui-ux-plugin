# G1 - Grading round 1: five audit reports vs. the Ledgerly answer key

Grader standard: 1 = names the specific planted problem and points at the right file/element/line; 0.5 = touches the area but misses the point, or catches only one half of a two-part flaw; 0 = missed. One finding may earn several IDs. Findings, top fixes and system-health sections all count (per the key), but praise that contradicts a flaw reduces it. All citations were checked against the fixture (index.html 94 lines, invoices.html 97, signup.html 78, styles.css 124).

Calibration rules applied identically to all five:
- K3 needs the "Welcome to Ledgerly!" h1 called out, not only the jargon paragraph (paragraph alone = 0.5).
- K5 needs both halves: 5 equal CTAs AND the real signup being a plain span at the bottom (one half = 0.5).
- K10 is about looks/affordance (fakelink, ghostlink, unlabeled .go). "span onclick is inaccessible" alone earns A3 but only 0.5 on K10.
- D1: a dedicated row saying the table is too dense / needs padding = 1 false positive; a padding rider inside another finding = 0.5.
- A bad fix attached to a legitimate observation is logged as a harmful fix, not a false positive.
- K12 needs count AND prominence (one half = 0.5). K22 needs generic untied error AND Clear-form-styled-as-Submit (one half = 0.5).
- R8: "buttons inconsistent" without action hierarchy / loud Delete = 0.5. A5 / R1: a contrast number without the principle, or hero only = 0.5.

## 1. Scores per flaw (score, finding number that earned it)

### Usability K1-K25

| ID | T1 plain+skill | T2 agent+skill | T5 large no-skill | T6 haiku no-skill | T7 haiku+skill |
|----|----|----|----|----|----|
| K1 clever nav names | 1 (#1) | 1 (#1) | 1 (A1) | 0 | 1 (#14) |
| K2 vague motto | 1 (#7) | 1 (#17) | 1 (B2) | 0 | 1 (#16) |
| K3 happy-talk h1 + mission para | 1 (#7) | 1 (#17) | 1 (B2) | 0.5 (#6 para only) | 0.5 (#1 para only) |
| K4 "About this section" | 1 (#14) | 1 (#29) | 1 (B10) | 0 | 0 |
| K5 no start point | 1 (#9,#10) | 1 (#20,#21) | 1 (B4,B1) | 0.5 (#7 CTA count only) | 0.5 (#2 CTA count only; keeps "Let's Go!" as primary) |
| K6 first screen fails "what is this" | 1 (#7,#15) | 1 (#17,#35) | 1 (B2,B11) | 1 (#6) | 1 (#1) |
| K7 search | 1 (#5,#6) | 1 (#23,#24,#25) | 1 (B6) | 0.5 (#31 vague; fix keeps Quick Find + dropdown) | 0.5 (#23 dropdown only) |
| K8 forced choice | 1 (#12) | 1 (#26) | 1 (B9) | 0.5 (#30 wants a better heading) | 1 (#6) |
| K9 promo overload | 1 (#13) | 1 (#27) | 1 (B8) | 0.5 (#8 framed as false urgency, not overload) | 1 (#10) |
| K10 clickability | 1 (#5,#10,#11) | 1 (#21,#22,#24) | 1 (B7,B6) | 0.5 (#1 a11y only) | 0 |
| K11 site ID not top-left / not link | 1 (#2) | 1 (#3) | 1 (A3) | 0 | 0 |
| K12 utilities too many + too loud | 1 (#3) | 1 (#4) | 1 (A4,A5) | 0 (#5 is about href="#") | 0.5 (#13 count only) |
| K13 you-are-here | 1 (#4) | 1 (#2) | 1 (A2) | 1 (#10) | 1 (#3) |
| K14 page name missing/mismatch | 1 (#29) | 1 (#36,#37) | 1 (A8,C12) | 0 | 0 |
| K15 breadcrumbs misused | 1 (#31) | 1 (#37) | 1 (C11; no "/" or page-name point, but bold/heavy + last item) | 0 | 0 |
| K16 sidebar no current item | 1 (#30) | 1 (#38) | 1 (C13) | 0 | 0 |
| K17 over-collecting form | 1 (#47) | 1 (#58) | 1 (D1) | 0.5 (#4/#25 card security only) | 0.5 (#5 card only, as a trust-cue issue) |
| K18 rigid formats | 1 (#48) | 1 (#59) | 1 (D7) | 1 (#15,#16) | 1 (#9) |
| K19 instructions paragraph | 1 (#45) | 1 (#56) | 1 (D11) | 0 | 1 (#8) |
| K20 full nav on form page | 1 (#43) | 1 (#65) | 0.5 (D17, Minor; framed as "app nav shown to logged-out user", fix is right) | 0 | 0 |
| K21 signup name mismatch + title | 1 (#44,#43) | 1 (#55) | 1 (D14,B16,A8) | 0 | 0 |
| K22 generic error + Clear = Submit | 1 (#49,#50) | 1 (#63,#61) | 1 (D4,D5) | 0.5 (#3 always-visible; #20 reset, not the twin styling) | 0.5 (#7 always-visible only) |
| K23 fake sincerity | 1 (#57) | 1 (#67) | 1 (D16) | 0.5 (#25 wants it moved above the form) | 0 |
| K24 hidden fees | 1 (#19) | 1 (#33) | 1 (B12) | 0 | 0 |
| K25 empty state + useless controls | 1 (#41) | 1 (#52) | 1 (C14) | 0.5 (#26 no CTA; controls not noticed) | 0 |
| **K subtotal** | **25.0** | **25.0** | **24.5** | **8.0** | **11.0** |

### Accessibility A1-A6

| ID | T1 | T2 | T5 | T6 | T7 |
|----|----|----|----|----|----|
| A1 no labels | 1 (#46) | 1 (#57) | 1 (D3) | 1 (#2) | 1 (#4) |
| A2 no alt | 1 (#17,#52) | 1 (#31,#66) | 1 (B14,D15) | 1 (#19) | 0.5 (#22 avatars only, Minor) |
| A3 span onclick not keyboard operable | 1 (#5,#10) | 1 (#21,#24) | 1 (B1,B6) | 1 (#1) | 0 |
| A4 no skip link / landmarks | 1 (#59) | 1 (#6) | 1 (A6) | 0 (and praised "semantic sections") | 0 |
| A5 contrast failures | 1 (#8,#34,#58) | 1 (#11,#18,#19,#33,#41,#52) | 1 (B3,C2,E2) | 0.5 (#9 hero only, wrong ratios) | 0 (deferred to "not verified") |
| A6 color alone | 1 (#36) | 1 (#45) | 1 (C6) | 1 (#23) | 0 |
| **A subtotal** | **6.0** | **6.0** | **6.0** | **4.5** | **1.5** |

### Visual R1-R22

| ID | T1 | T2 | T5 | T6 | T7 |
|----|----|----|----|----|----|
| R1 grey / translucent white on color | 1 (#8) | 1 (#18,#19) | 1 (B3) | 0.5 (#9 number only) | 0 |
| R2 too many font sizes | 1 (#22) | 1 (top fix 7 + system health; no table row) | 1 (A13) | 0 | 1 (#21) |
| R3 weight 300 | 1 (#20) | 1 (#8) | 1 (A9,B17) | 0 | 0.5 (system health aside; also calls the 2 weights "OK") |
| R4 pure black, no grey hierarchy | 1 (#20,#33) | 1 (#10,#43) | 1 (A9,E3) | 0 | 0 |
| R5 nested em | 1 (#22) | 1 (#13,#56,#68) | 0.5 (D11 notes 0.875 x 0.875; principle never stated) | 0 | 1 (#17,#11) |
| R6 spacing one-offs + cramped | 1 (#21) | 1 (#34 + system health) | 1 (A13,C17) | 0 | 1 (system health + #13) |
| R7 ambiguous label spacing | 1 (#54) | 1 (#64) | 1 (D13) | 0 | 0 |
| R8 action hierarchy, loud Delete | 1 (#35) | 1 (#40,#42) | 1 (C1,C3) | 0.5 (#11 inconsistency; #12 no confirm) | 0.5 (#11 inconsistency only) |
| R9 disabled-looking Mark as paid | 1 (#34) | 1 (#41) | 1 (C2) | 0 | 0 |
| R10 mixed radius | 1 (#25) | 1 (#12) | 1 (A14) | 1 (#11) | 1 (#11) |
| R11 borders everywhere | 1 (#27) | 1 (#14) | 1 (A12) | 0 | 0 |
| R12 label:value wall | 1 (#33) | 1 (#43) | 1 (C4,C5) | 0 | 0 |
| R13 shouting section titles | 1 (#37) | 1 (#47) | 1 (C12) | 0 | 0 |
| R14 left-aligned amounts | 1 (#39) | 1 (#49) | 1 (C8) | 0 | 0 |
| R15 centered long text / measure | 1 (#16) | 1 (#30) | 1 (B10) | 0 | 0 |
| R16 % sidebar, no max-width | 0.5 (#16,#53 max-width; #24 treats 25% as a responsive issue, never says fixed width) | 1 (#54) | 1 (C13,A13) | 0.5 (#14 form max-width only) | 0 |
| R17 shadows | 1 (#26) | 1 (#48) | 1 (C15) | 0 | 1 (#12) |
| R18 16px icon at 96px | 1 (#17) | 1 (#31) | 1 (B14) | 0 | 0 |
| R19 bullet spacing | 1 (#18) | 1 (#32) | 1 (B15) | 0 | 0 |
| R20 no color system | 1 (#23) | 1 (top fix 7, #12, system health; no dedicated row) | 1 (E1) | 0 | 0.5 (#19 no tokens, but praises the 4-hue scheme as "intentional") |
| R21 line-height 1.2 | 1 (#20) | 1 (#9) | 1 (A9) | 1 (#17) | 0.5 (#13 topbar only) |
| R22 avatars height-only | 1 (#52) | 1 (#66) | 0 (D15 is alt/purpose/missing file only) | 0 | 0 |
| **R subtotal** | **21.5** | **22.0** | **20.5** | **3.5** | **7.0** |

## 2. Subtotals

| Report | K /25 | A /6 | R /22 | Total /53 | % |
|----|----|----|----|----|----|
| T1 large + skill | 25.0 | 6.0 | 21.5 | 52.5 | 99.1% |
| T2 large agent + skill | 25.0 | 6.0 | 22.0 | 53.0 | 100.0% |
| T5 large, no skill | 24.5 | 6.0 | 20.5 | 51.0 | 96.2% |
| T6 small, no skill | 8.0 | 4.5 | 3.5 | 16.0 | 30.2% |
| T7 small + skill | 11.0 | 1.5 | 7.0 | 19.5 | 36.8% |

The large model is at ceiling on recall with or without the skill; the fixture does not discriminate there. The differences are in sections 3 to 8.

## 3. Decoys

| Decoy | T1 | T2 | T5 | T6 | T7 |
|----|----|----|----|----|----|
| D1 dense table | Left alone, mostly. #39 (Minor) is about alignment/thead but its fix slips in "8 to 12px cell padding"; #21 lists "table cells 3px" as tight. Counted as **half a false positive**: same substance as T2 #50 but only a rider inside another finding, not its own row. | **Wrongly flagged**, #50 Minor: "Dense table ... No evidence the density is deliberate", fix "8 to 12px padding". | **Wrongly flagged, Major**, C10: "Table is extremely cramped", fix 10-12px padding. Repeated in top fix 5 ("give tables breathing room"). | Left alone | Left alone (no invoices-page findings at all) |
| D2 quiet Archive | Legitimate colour critique (#40 Minor, danger colour on reversible action) and **correctly praises** `.quiet-danger` as "a genuinely good pattern". | Legitimate colour critique (#51 Minor). Not praised. #16 lists the 13px text-only Archive among small targets: borderline lean toward "too quiet", not counted. | C7 Major: colour critique is legitimate; the added "13px with zero padding, hit target below 24x24" pushes toward "too quiet" but is a defensible WCAG 2.5.8 point. Borderline, not counted. Praises its contrast. | Legitimate colour critique (#13), rated **Major**. Not a false positive under the rubric, but a harmful fix: a solid `.btn-grey` / blue button per row would undo the correct quiet treatment. | Left alone |
| D3 system font stack | Praised | Praised | Praised | Praised (loosely, inside a false "consistent typography" line) | Praised |
| D4 lang + viewport | Praised both | Praised both | Praised both | Praised viewport only | Praised viewport only |

## 4. False positives

- **T1: 0.5.** The D1 padding rider in #39/#21 (see section 3). Otherwise clean: it explicitly declines to report `href="#"` stubs and says missing image files mean alt text cannot be judged. Two speculative but labelled items: #38 (list rows are not links) and #42 (no "New invoice" action; the report itself says this depends on an assumption). Minor factual slip: "13 exclamation marks" (actual 16).
- **T2: 1.** #50 (D1, Minor). Same speculative #51 "invoice numbers not links". Minor slip: "14 exclamation marks".
- **T5: 5.** A10 (dead `href="#"` links, Minor); B14 part ("file does not exist in the fixture (broken image)"); D15 part ("people/ files do not exist ... broken images"); D18 (`action="#"`, no loading state, Minor); C10 (D1, Major). Borderline noise not counted: D2 (card field "no security cues / PCI" rated Critical on a static stub), D10 (password rules/show toggle), C16 (ISO dates), C18 (mailto/tel links). Slip: "20+ exclamation marks".
- **T6: 5.** #5 (`href="#"` links, **Major**); #27 (`.example` TLD "invalid"); #28 (placeholder text "too large": invented, nothing in the CSS supports it, and the fix makes placeholders lighter, worsening contrast); #29 (sidebar background "insufficient contrast" with white: wrong on the facts, the real issue is link contrast on it); #4 (demands SSL/PCI disclosure text, Critical). Harmful fix (not counted): #13 promotes Archive to a solid button. Borderline: #12 "Delete has no confirmation" cannot be known from static markup. Its own summary statistics are wrong (says Major 15 / Minor 12; the report actually contains 16 Major / 11 Minor; per-file issue counts do not add up).
- **T7: 2.** #5 ("no HTTPS indicator" / SSL badge, Critical: not a design finding for a static file); #20 (calls the avatars an "avatar selection" and proposes "Choose your support advisor": invents an interaction). Weak: #24 (input height "inconsistent with button heights"). Harmful fix: #2 keeps the vague "Let's Go!" as the primary CTA although it does not lead to signup.

## 5. False praise

- **T1: 0.** (Praises "fee is at least disclosed" and "status values are words" but both are accurate and neither contradicts a planted flaw.)
- **T2: 0.**
- **T5: 1 borderline.** "native `required`/`pattern` give at least baseline client-side validation": those patterns are the K18 rigid formats (which it does flag in D7).
- **T6: 5.** "Clean, minimal visual design ... uses whitespace effectively" (contradicts R6, R11, K9); "Good page structure - proper use of semantic sections" (contradicts A4: everything is a div); "Consistent typography ... readable base sizes" (R2, R3, R21, and its own #17); "good information hierarchy" on invoices (R4, R8, R12, R13); "Color contrast in most areas" (A5: footer, empty state, grey button, green/orange buttons all fail).
- **T7: 2.** "Color scheme (blue primary, green/orange secondaries, red semantic) is intentional" (R20, R8: the hues are arbitrary); "Font weights: 2 (300, 700) - OK" in system health (R3). Borderline: "Sidebar layout ... clearly separates navigation from content" (R16/K16 untouched).

## 6. Evidence quality (8 spot-checks each, cited line vs. fixture)

| Report | Checked | Accurate | Notes |
|----|----|----|----|
| T1 | css:26 brand order; index:39 .go; css:36/41/42 hero; invoices:58,88 btn-grey; css:110-111 shadows; signup:58 err; css:118-120 field spacing; index:91 + css:124 footer | 8/8 | Computed contrast ratios also check out (2.30, 2.55, 1.68, 1.92). |
| T2 | css:24-25; css:26; index:88 + css:80; invoices:57 + css:59; css:110-111; signup:67-68; css:102-103; css:115 | 8/8 | Also css:7/40/94 (weight 300) and signup:36 correct. |
| T5 | css:24-25; index:41 + css:26; invoices:94 / signup:75 footers; css:43 cta-row; invoices:57 + css:59; signup:39 form; css:1,5; css:84-85 | 8/8 | A13's size list omits 18px; ratios correct. |
| T6 | index:39,88; signup:41-57; signup:58; css:41-42; css:24-25; css:56-60; invoices:64-66; invoices:84-85 | 7/8 | Lines are right, but #9's ratios are wrong (claims 3.2:1 and 2.8:1; actual 2.30:1 and 2.55:1). #28's claim has no evidence at all. |
| T7 | index:47; index:49-53; css:25; signup:41-42,44-47,49-56; signup:43,47,57; css:110-111; css line list in #21; signup:35-36 + css:116 | 7/8 | #21's line list is padded: css 5 is font-family, 43 is .cta-row, 96 is .metric, 104 and 107 are blank; none has a font-size. #4's range skips the phone (43) and card (57) inputs, which are also placeholder-only. System-health counts are undercounts (see 8). |

## 7. Prioritisation quality (0-5)

Serious clusters: (a) value proposition / no start point, (b) over-collecting signup, (c) unlabeled inputs + keyboard-inaccessible controls, (d) invisible you-are-here + clever nav names, (e) action hierarchy with loud Delete.

- **T1: 5.** Top 7 = names/you-are-here (d), hero + one action (a), cut form + labels (b, c), button pyramid incl. Delete and Mark-as-paid (e), header, body text, tokens. Keyboard access is folded into fixes 2 and 5 rather than named.
- **T2: 5.** Top 7 = action hierarchy (e), make entry points real controls (c, a), contrast, form cut + labels (b, c), plain names + you-are-here (d), cut landing (a), tokens. Cleanest mapping of the five.
- **T5: 5.** Five bundled fixes cover b+c, a, e, d, tokens. Each "fix" is a bundle of 5 to 10 findings, so less actionable as a do-first list, but the order is right.
- **T6: 2.** Labels, hero contrast, span controls, hide error, standardise buttons. Hits (c) only. Value proposition, over-collection, nav names, you-are-here and Delete are absent from the top 5; "hide the error div" outranks all of them.
- **T7: 2.5.** Hero copy and CTA reduction (a, partly), you-are-here (half of d), labels (half of c). Missing from the top 8: over-collection (b), the unfocusable signup/search controls (c), nav names (it has them as finding #14 but not as a top fix), Delete/action hierarchy (e). Cosmetic button radius standardisation made the list instead.

## 8. System-health counts and honesty about what was not verified

| Report | System-health counts | States what was not verified |
|----|----|----|
| T1 | Yes: 14 font sizes, 2 weights, 20 colors (+2 rgba), 16 spacing values, 2 shadows, 3 radii, 1 line-height, border usage x14. States its counting rules. Accurate. | Yes, thorough: nothing rendered, contrast computed not measured, behaviour, missing images, assumed top tasks, no AT run, plus a concrete test plan. |
| T2 | Yes: 14 declared / 15 effective sizes, 2 weights, 22 colors, 16 spacing, 2 shadows, 3 radii, border widths. Accurate. | Yes, thorough; also reports the failed single browser attempt honestly. |
| T5 | No counts. A13/E1 list raw values without totals. | One line in the scope paragraph ("no browser", ratios +/-0.1). No section; does not flag assumptions about behaviour. |
| T6 | None. | None. Presents wrong contrast numbers as fact and "no confirmation on Delete" as fact. |
| T7 | Yes, but undercounted: 12 sizes (actual 14), ~18 colors (20+), ~10 spacing values (16); omits #e8e8e8, #eee, #8a1c1c, and 7/16/18/20/26/30px. | Yes, has the section, but uses it as an escape hatch: lists contrast as "couldn't be checked" when the hex values were in the CSS and could be computed (T1/T2 did). That single choice cost A5 and R1. |

## Comparison table

| Report | K /25 | A /6 | R /22 | Total % | False positives | False praise | Evidence accuracy | Prioritisation /5 | Findings |
|----|----|----|----|----|----|----|----|----|----|
| T1 large + skill | 25.0 | 6.0 | 21.5 | 99.1% | 0.5 (D1 rider) | 0 | 8/8 | 5 | 59 (6 Crit / 40 Maj / 13 Min) |
| T2 large agent + skill | 25.0 | 6.0 | 22.0 | 100.0% | 1 (D1) | 0 | 8/8 | 5 | 68 (10 / 37 / 21) |
| T5 large, no skill | 24.5 | 6.0 | 20.5 | 96.2% | 5 (incl. D1 as Major) | 1 borderline | 8/8 | 5 | 72 (11 / 42 / 19) |
| T6 small, no skill | 8.0 | 4.5 | 3.5 | 30.2% | 5 | 5 | 7/8 | 2 | 31 (4 / 16 / 11) |
| T7 small + skill | 11.0 | 1.5 | 7.0 | 36.8% | 2 | 2 | 7/8 | 2.5 | 24 (7 / 8 / 9) |

## Conclusions

1. **Large model: the skill adds about 3 to 4 points of recall (96.2% to 99-100%), which is inside the noise of a fixture the large model already saturates.** The measurable gain is discipline: false positives drop from 5 to 0.5-1 (the no-skill run reported `href="#"` stubs, missing image files, `action="#"` and rated the deliberate table density Major), and only the skill runs produce accurate system-health counts and a specific "Not verified" section. The few recall gains are all visual-system items (R5 nested em as a principle, R22 photo containers) plus K20 (reduced nav on forms).
2. **Small model: the skill adds about 6.6 points overall (30.2% to 36.8%, 16.0 to 19.5 of 53) but the gain is lopsided.** Usability K rose 8.0 to 11 (it now names clever nav names, the vague motto, the instructions paragraph and the forced choice with the right principle) and Visual R doubled 3.5 to 7 (type scale, nested em, spacing one-offs, shadows), false praise fell from 5 to 2 and false positives from 5 to 2. But **Accessibility regressed from 4.5 to 1.5**: the no-skill haiku found the span-onclick controls, missing alt on both pages and color-only metrics; the skill-run haiku found none of those.
3. **The skill helps most with Krug-style naming/wording flaws and with system-level visual flaws (scales, tokens, shadows); it helps least with element-level visual flaws and did harm on accessibility for the small model.**
4. **Biggest with-skill shortfall: T7 effectively skipped a whole screen.** It has no finding located in invoices.html except the nav labels, so everything planted there was missed: K14, K15, K16, K25, A6, R8 (Delete), R9, R11, R12, R13, R14, R16 (it caught the shadows, R17, only because they sit in styles.css). The skill needs a per-screen coverage check ("every screen in scope must have its own checklist pass; state findings per screen") because a small model stops after the landing page and the form.
5. **Other specific T7 misses to drive skill changes:** A3 and K10 (never inspected `onclick` spans or link-looking spans: add an explicit "grep for onclick on non-button elements; list anything styled as a link that is not one and vice versa" step); A5 and R1 (deferred contrast to "not verified" instead of computing it from hex: the skill should say "when you cannot render, compute WCAG ratios from the declared colors; do not defer"); A4 (no landmark/skip-link check); K11, K12 prominence, K20, K21, K23, K24 (header conventions, form-page nav, name matching, goodwill items: present in the checklist but not executed); K17 reduced to "card field lacks trust cues" rather than "ask only what the task needs"; K5 (kept "Let's Go!" as primary and never found the real signup link); R4, R7, R15, R18, R19, R21 body-level, R22.
6. **Large-model with-skill shortfalls are small but real:** T1 missed R16's "sidebar should be fixed width, not a percentage" (treated only as a responsive issue); T2 tripped decoy D1 ("no evidence the density is deliberate") and T1 half-tripped it with an "8 to 12px cell padding" rider, so the skill should state that data tables are a legitimate place for density and that borders/alignment, not padding, are the things to flag there; T2 put R2 and R20 only in system health/top fixes with no findings row; none of the skill runs rendered the pages (file:// blocked) and the skill offers no fallback such as starting a static server.
7. **Severity inflation and noise persist with the skill.** T1 rates 40 of 59 findings Major (68%); T2 has 10 Criticals including you-are-here and the Clear-form twin; T7 rates 7 of 24 Critical (29%), including the chooser and the always-visible error div, while missing alt is Minor and over-collection is not rated at all. The skill's "top 3 to 7 fixes, not an exhaustive dump, skip kayak problems" did not constrain volume: skill runs still produced 59 and 68 rows (partly because the test prompt asked for all findings; both reports flagged this conflict). The skill needs explicit severity anchors (e.g. Critical = blocks a top task or excludes a user group; cap Criticals; placement of labels/alt/landmarks in the scale) and an explicit statement of whether the findings table is exhaustive or trimmed.
8. **Evidence accuracy is a model-size effect, not a skill effect:** all three large-model reports were 8/8; both haiku reports were 7/8, and T7 padded a line-number list and undercounted its system-health values, so the skill should require that counts be produced by enumerating the actual values (as T1/T2 did) rather than estimated.
