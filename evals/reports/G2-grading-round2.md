# G2 - Grading round 2: two revised-skill audit reports vs. the Ledgerly answer key

Same grader standard and calibration rules as G1 (1 = names the specific planted problem and points at the right file/element/line; 0.5 = touches the area but misses the point, or one half of a two-part flaw; 0 = missed; findings, top fixes and system health all count; praise that contradicts a flaw reduces it; K3 needs the "Welcome" h1; K5 needs both halves; K10 is about looks; K12/K22 need both halves; R8 needs action hierarchy + loud Delete; A5/R1 a contrast number without the principle = 0.5; D1 dedicated row = 1 FP, rider = 0.5). One rule made explicit for this round, consistent with G1's credit to T2 for R2/R20: a system-health statement that names the values AND the problem = 1; a bare count = 0.5; praise elsewhere that contradicts it caps it at 0.5. All citations checked against the fixture (index.html 94 lines, invoices.html 97, signup.html 78, styles.css 124).

Reports graded:
- **R2-T1** = R2-T1-analyze-plain.md (large model + revised skill), compare with round-1 T1.
- **R2-T7** = R2-T7-haiku-skill.md (small model + revised skill), compare with round-1 T7 and T6.

## 1. Scores per flaw (score, finding number that earned it)

### Usability K1-K25

| ID | R2-T1 large + revised skill | R2-T7 haiku + revised skill |
|----|----|----|
| K1 clever nav names | 1 (#8) | 1 (#25; names Vault, Hive, Pulse, Toolbox, omits Launchpad) |
| K2 vague motto | 1 (#10) | 1 (#16) |
| K3 happy-talk h1 + mission para | 1 (#10 names "Welcome to Ledgerly!" and the jargon blurb) | 0.5 (#1 paragraph only; #16 cites 45-47 but never calls out the Welcome h1) |
| K4 "About this section" | 1 (#28) | 0 |
| K5 no start point | 1 (#10 five equal CTAs; #1 real signup is a black span) | 0.5 (#35 CTA count; #27 "Let's Go!"; never says the real signup entry is the plain span; fix promotes "Learn More") |
| K6 first screen fails "what is this" | 1 (#10) | 1 (#16, #1, #19) |
| K7 search | 1 (#15 all four parts) | 0.5 (#23 text must be deleted, miscalled a placeholder; #17 says it "lacks a label" and its fix KEEPS "Quick Find"; no scope-dropdown or wording point) |
| K8 forced choice | 1 (#14) | 1 (#28) |
| K9 promo overload | 1 (#13) | 1 (#19) |
| K10 clickability | 1 (#11 fakelink; #1 ghostlink + blank .go) | 0.5 (#24 a11y only; fakelink and looks never mentioned) |
| K11 site ID not top-left / not link | 1 (#9) | 0 (and praised: "brand placement ... Users know where to look") |
| K12 utilities too many + too loud | 1 (#9 count and bold blue) | 0 |
| K13 you-are-here | 1 (#5) | 0 (**regression**: round-1 T7 had 1) |
| K14 page name missing/mismatch | 1 (#16) | 0.5 (#6 no h1 on invoices; title/nav mismatch not noticed) |
| K15 breadcrumbs misused | 1 (#16: 16px bold, "/" separators, standing in for the page name; fix small + ">") | 0 |
| K16 sidebar no current item | 1 (#39) | 0 |
| K17 over-collecting form | 1 (#2) | 1 (#4 card + income, #20 occupation/income/DOB; note #4's fix keeps phone, address and occupation, contradicting #20) |
| K18 rigid formats | 1 (#22) | 1 (#15) |
| K19 instructions paragraph | 1 (#25) | 0 (**regression**: round-1 T7 had 1) |
| K20 full nav on form page | 1 (#45, Minor) | 0 |
| K21 signup name mismatch + title | 1 (#26) | 0 (and #6 wrongly says signup has no h1) |
| K22 generic error + Clear = Submit | 1 (#23, #24) | 1 (#22, #21) |
| K23 fake sincerity | 1 (#27) | 0 |
| K24 hidden fees | 1 (#12) | 0 (#14 gives the footer contrast only; the fee is never noticed) |
| K25 empty state + useless controls | 1 (#40) | 0 (#14 gives .empty contrast only) |
| **K subtotal** | **25.0** | **10.5** |

### Accessibility A1-A6

| ID | R2-T1 | R2-T7 |
|----|----|----|
| A1 no labels | 1 (#3) | 1 (#5; the counts inside it are garbled, see section 4) |
| A2 no alt | 1 (#44) | 1 (#13, both pages) |
| A3 span onclick not keyboard operable | 1 (#1) | 1 (#24) |
| A4 no skip link / landmarks | 1 (#33) | 1 (#7, #8) |
| A5 contrast failures | 1 (#6, #4: all four key pairs + five more) | 1 (#2, #3, #11, #14: all four key pairs) |
| A6 color alone | 1 (#37) | 0 (and praised: "Metrics show both value and change indicator (number + up/down color)") |
| **A subtotal** | **6.0** | **5.0** |

### Visual R1-R22

| ID | R2-T1 | R2-T7 |
|----|----|----|
| R1 grey / translucent white on color | 1 (#30 states the principle) | 0.5 (#2, #3 ratios only, principle never stated) |
| R2 too many font sizes | 1 (#19) | 1 (system health only: "14 distinct ... many near-neighbors (13/14/15)"; no findings row, not in top fixes) |
| R3 weight 300 | 1 (#20) | 1 (#32) |
| R4 pure black, no grey hierarchy | 1 (#20 pure black; #36 labels = values in size/weight) | 1 (#34 pure black; #32 + system health "heading weight same as body ... to create hierarchy" covers the no-hierarchy half; the grey-scale point itself is never made) |
| R5 nested em | 1 (#19 nested em, #31 em padding) | 1 (#30; its arithmetic is wrong, see section 6) |
| R6 spacing one-offs + cramped | 1 (#31) | 1 (system health "18 distinct ... no scale; many one-offs" + #33) |
| R7 ambiguous label spacing | 1 (#38) | 0 |
| R8 action hierarchy, loud Delete | 1 (#17) | 1 (#26, rated Minor; says Delete is "only one of five", misses that it is the biggest) |
| R9 disabled-looking Mark as paid | 1 (#4) | 0.5 (#11 ratio 1.68 "nearly invisible", placed on index where the class is not used; never says Mark as paid looks disabled) |
| R10 mixed radius | 1 (#46) | 1 (system health only: "3 distinct (0, 4px, 18px). Inconsistent."; no findings row, not tied to buttons) |
| R11 borders everywhere | 1 (no dedicated row: #7 fix "panels separated by space/fill instead", #35, #36, #42, system health "the 17 borders mostly go") | 0 |
| R12 label:value wall | 1 (#36) | 0 (and praised as "clear, readable, and well-organized") |
| R13 shouting section titles | 1 (#34) | 0 |
| R14 left-aligned amounts | 1 (#42) | 0 |
| R15 centered long text / measure | 1 (#29, #28) | 0 |
| R16 % sidebar, no max-width | 1 (#39 fixed ~200px; #29, #38 max-width) | 0.5 (#18 sidebar fixed width; no max-width half, and full-width inputs are praised) |
| R17 shadows | 1 (#35) | 1 (#31; tagged "index", the shadows are on invoices) |
| R18 16px icon at 96px | 1 (#43) | 0 |
| R19 bullet spacing | 0 (cited, not named: #20 lists styles.css:76 but never mentions bullets) | 0 |
| R20 no color system | 1 (#21) | 0.5 (system health "no tokens; near-duplicate greys", but What's working praises "Color diversity for semantic meaning") |
| R21 line-height 1.2 | 1 (#20) | 1 (#33) |
| R22 avatars height-only | 0 (#44 is alt/purpose only; Not verified says cropping "could not be judged") | 0 |
| **R subtotal** | **20.0** | **11.0** |

## 2. Subtotals

| Report | K /25 | A /6 | R /22 | Total /53 | % |
|----|----|----|----|----|----|
| R2-T1 large + revised skill | 25.0 | 6.0 | 20.0 | 51.0 | 96.2% |
| R2-T7 small + revised skill | 10.5 | 5.0 | 11.0 | 26.5 | 50.0% |

For reference: round-1 T1 52.5 (99.1%), round-1 T7 19.5 (36.8%), round-1 T6 16.0 (30.2%).

## 3. Decoys

| Decoy | R2-T1 | R2-T7 |
|----|----|----|
| D1 dense table | **Left alone and explicitly cleared.** #42 flags only alignment and cell rules and adds "Density itself is fine for a data table"; What's working repeats "deliberate table density is acceptable". #31's cramped list (topbar, panels, hero) no longer includes the table. The round-1 padding rider is gone. 0 FP. | Left alone (the tables are praised wholesale, which is false praise for R12/R14 but not a D1 trip). |
| D2 quiet Archive | **Correctly praised** (`.quiet-danger` "correctly quiet ... not a solid button repeated down the table", 9.28:1). #27's "Cancel my subscription" point is a different element and legitimate. | Left alone, not praised. |
| D3 system font stack | Praised | Not mentioned |
| D4 lang + viewport | Praised both | Not mentioned (round-1 T7 praised viewport) |

## 4. False positives

- **R2-T1: 0.** It again explicitly excludes missing image files, `href="#"` stubs and the `.example` address as fixture artifacts. Non-planted findings are all true and checkable: #7 `#999` control borders 2.85:1 (correct; labelled [ext]; Major is generous), #18 no responsive design (0 media queries, confirmed in the 400px screenshots), #32 no `:hover/:focus` rules (true), #41 unlabeled selects on invoices (true). Speculative but labelled: #37 "the colour may be wrong" (flagged in Not verified as owner-to-confirm). Factual slip: #3 says "10 of 11 controls" but its own enumeration (9 placeholder inputs + select + span-labelled name) is 11 of 11. Other counts checked and correct: 16 exclamation marks, 11 fields / 8 required, 9 utilities on index / 8 on signup.
- **R2-T7: 2.**
  1. #6 (Critical) and top fix 6 claim signup.html has no `<h1>`; it has one at signup.html:33 ("Become a Ledgerly Insider"). The "evidence" is the invented citations `invoices.html:0; signup.html:0`.
  2. #29 "No visible indication of signed-in state ... show a user avatar or Hi, [name]": invented; Account + Log out are the signed-in indication (R2-T1 praises exactly this).
  - Not counted but wrong in detail: #11, #14 (.empty) and #31 are tagged **index** although `.btn-grey`, `.empty` and the shadow classes are used only on invoices.html; #5's numbers ("15 form controls", "2 selects with placeholder-only", "3 searches on index") do not match the markup (signup has 1 select; for index it cites two controls, lines 32 and 38, and calls them "3 searches"); #23 calls the `value` attribute a placeholder; top fix 1 says "No label = form cannot be completed by keyboard users" (wrong user group); Not verified #6 says "the red-on-white contrast pass (2.77:1)" (2.77 is the orange and it fails).
  - Harmful fixes (not counted): #17 "Add visible label 'Quick Find'" keeps the planted wording; #4 keeps phone, address and occupation in the "reduced" form; #35 suggests "Learn More" as the primary; #25 offers tooltips as an alternative to renaming.
  - Unconfirmed-candidate noise: #12 is a scanner candidate passed straight through at Critical while saying "verify applied size ... Check actual rendered size" (the pair does in fact fail at 15px, so it is not a false positive, but it is an unverified one).
- **"ASSUMED background" pairs:** neither report produced a false positive from them, but only because all four assumed pairs in this fixture really do sit on white. R2-T1 says it checked the cascade; R2-T7 copied "on assumed white" into #14 without checking. The fixture cannot currently expose this risk (there is no light-on-dark text whose background is set on an ancestor other than the hero).

## 5. False praise

- **R2-T1: 0.** All seven "What's working" items are accurate and none contradicts a planted flaw (nav consistency is praised with the explicit caveat that the names fail).
- **R2-T7: 5** (round-1 T7: 2). "The key-value table and invoice list table are clear, readable, and well-organized" (contradicts R12, R11, R14; also miscalls the uppercase headers "small caps"); "Metrics show both value and change indicator (number + up/down color)" (that IS flaw A6); "brand placement ... identical ... Users know where to look" (K11); "Inputs stretch to 100% width ... Good" (R16 / no max-width); "Color diversity for semantic meaning: blue (primary), green (success), orange (secondary), red (danger)" (R20, R8: the hues are arbitrary).

## 6. Evidence quality (8 spot-checks each)

| Report | Checked | Accurate | Notes |
|----|----|----|----|
| R2-T1 | index:88/39 + css:80/32; css:60 + invoices:58,88; css:24-25; css:26-28; signup:43,47,57; signup:67-68; css:110-111; css:118-120 | 8/8 | The long line lists also hold: #6's nine lines each carry the named colour; #7's thirteen lines all carry `#999` and correctly exclude the `#aaa` lines 31-32; #34's 59/65/91/103 correct. Ratios correct (2.30, 2.55, 1.68, 1.92, 8.45, 7.46). Nested-em arithmetic correct (about 11.5px). |
| R2-T7 | index:47; css:41; signup:43,47,57; css:84; index:39,88 + css:32,80; css:110-111; css:116-117; invoices:0 / signup:0 | 6/8 | #6's `:0` citations are invented and the signup claim is false. #30's lines are right but the computed value is wrong: says 13.125px, actual 15 x 0.875 x 0.875 = 11.48px. Also css:3 cited for weight/line-height (actual lines 7 and 10); three findings tagged to the wrong screen (section 4). Down from 7/8 in round 1. |

## 7. Prioritisation (0-5)

Same five clusters: (a) value proposition / start point, (b) over-collecting signup, (c) unlabeled inputs + keyboard-inaccessible controls, (d) you-are-here + clever names, (e) action hierarchy with loud Delete.

- **R2-T1: 5.** Fix 1 real signup entry + kill look-alikes (a, c), fix 2 cut form + labels (b, c), fix 3 action pyramid incl. Delete and Mark as paid (e), fix 4 contrast, fix 5 names + you-are-here + brand + h1 (d), fix 6 first-screen rewrite (a), fix 7 systems. Keyboard access is now named in fix 1 (round 1 folded it away). Each fix lists the findings it resolves and the numbers are correct.
- **R2-T7: 3** (round 1: 2.5). Fix 3 = (b) fully; fix 4 = value proposition + promo + names (a partly, half of d); fix 1 = labels + landmarks (half of c); fix 5 renames "Let's Go!" instead of surfacing the real signup link. Missing from the top 6: the unfocusable signup/search controls (#24 appears in no top fix), you-are-here (not found at all), Delete/action hierarchy (#26 is Minor and absent). Contrast is fix 2 and a landmarks/skip-link bundle is fix 1, both ahead of everything users actually trip on. The "Findings:" cross-references are wrong (fix 1 lists #3, #11, #15 which are contrast and rigid formats; fix 2 lists #12 but not #11).

## 8. System-health counts, "not verified", coverage

| Report | System-health counts (truth: 14 sizes, 2 weights, 22 colors / 15 greys, 18 spacing, 2 shadows, 3 radii, 0 tokens, 0 media queries) | Not verified | Coverage |
|----|----|----|----|
| R2-T1 | **All eight correct**, plus line-heights 1, border declarations 17, var() 0 vs raw 199. Gives the size list with frequencies and a concrete consolidation plan. | Honest and specific: no keyboard run, no screen reader, no 200% zoom, no states, missing images (and says they are artifacts, not findings), metric direction inferred, 400-1280 widths not captured. It did render: six screenshots, and several findings cite pixels (400px overflow, invisible active nav). Discloses that the four ASSUMED-background pairs were verified by hand. | Coverage table present with an added Global row (the template lacks one; the report says so). invoices.html has **10 located findings** (#4, 16, 17, 35, 36, 37, 39, 40, 41, 42) and the row reconciles exactly with the table (B2 C3 E1 F2 H2). |
| R2-T7 | **All eight correct** (copied from scan.py; fixed from round 1's undercounts). The enumerated size list omits 11px and 12px though the total is right. | Has the section and no longer hides contrast in it (round-1 fault fixed). But it is partly boilerplate ("Chrome, Firefox, Safari", "5-10 users") and **not fully honest about rendering**: the header claims "screenshots at 1920px and 400px" (screenshot.py defaults to `--width 1280`, the report says it passed only `--mobile`, and R2-T1 measured the same script's PNGs at 1280px), and not one finding draws on a screenshot. The 400px overflow that R2-T1 saw in the same images is absent; "0 media queries" appears only in system health. The screenshots were generated, but there is no sign they were looked at. | Coverage table present, no Global row. **The cell counts do not reconcile with the findings table**: rows sum to 24 + 9 + 17 = 50 against 35 findings, and invoices claims 9 where only 3 findings are located there (#12, #18, #26) plus shares of #5, #6, #7, #8, #29. invoices.html now gets real findings (round 1: none): sidebar width, action buttons, no h1, unlabeled selects, grey-button contrast (mis-tagged index). But it marks E and G "ok" and D "ok" on a screen with left-aligned amounts, shouting headings and a label:value wall, and still misses K15, K16, K25, A6, R11, R12, R13, R14, while praising the tables. |

## 9. Severity calibration

Definition applied: Critical = a top task is blocked, users are misled into harm or loss, a basic accessibility barrier exists (control unreachable by keyboard, essential text unreadable, form controls unnamed), or sensitive data is collected that the task doesn't need.

| Report | Critical | Major | Minor | Total |
|----|----|----|----|----|
| R2-T1 | 4 (9%) | 22 (48%) | 20 (43%) | 46 |
| R2-T7 | 14 (40%) | 11 (31%) | 10 (29%) | 35 |
| (round-1 T1) | 6 | 40 (68%) | 13 | 59 |
| (round-1 T7) | 7 (29%) | 8 | 9 | 24 |

- **R2-T1: all 4 Criticals are defensible**, one per clause of the definition: #1 signup entry unreachable by keyboard (top task blocked), #2 card/income/DOB for a free account (sensitive data), #3 unnamed form controls, #4 "Mark as paid" at 1.68:1 (essential text unreadable on a top task). Arguable under-rating: #12 hidden 3.5% fee at 1.92:1 is "misled into loss" and could be Critical; #7 border contrast at Major is generous. The Major share fell from 68% to 48%.
- **R2-T7: 7 of 14 Criticals are not defensible, 4 are borderline, 3 are sound.**
  - Sound: #4 (sensitive data), #5 (unnamed controls), #11 (1.68:1 label on Mark as paid, although filed under the wrong screen).
  - Borderline: #2 and #3 (hero motto and jargon paragraph are unreadable but the report itself says the text is worthless, so not "essential"), #10 (2.77:1 button labels), #14 (footer 1.92:1 carries the fee, but the report never noticed the fee).
  - Not defensible: #1 jargon copy (Major usability, blocks nothing), #6 heading order / missing h1 (and half of it is false), #7 no landmarks, #8 no skip link, #9 `.btn-green` 3.28:1 (legible; AA fail = Major), #12 an explicitly unverified candidate, #13 missing alt on images the report itself calls decorative.
  - Inverted at the other end: #24, the keyboard-unreachable signup and search controls, is the textbook Critical under the definition and is rated **Major**; #26, loud Delete with no action hierarchy, is **Minor**; you-are-here is absent.

## Comparison table (all seven rows)

| Report | K /25 | A /6 | R /22 | Total % | False positives | False praise | Evidence accuracy | Prioritisation /5 | Findings | Criticals |
|----|----|----|----|----|----|----|----|----|----|----|
| T1 large + skill | 25.0 | 6.0 | 21.5 | 99.1% | 0.5 (D1 rider) | 0 | 8/8 | 5 | 59 (6 Crit / 40 Maj / 13 Min) | 6 |
| T2 large agent + skill | 25.0 | 6.0 | 22.0 | 100.0% | 1 (D1) | 0 | 8/8 | 5 | 68 (10 / 37 / 21) | 10 |
| T5 large, no skill | 24.5 | 6.0 | 20.5 | 96.2% | 5 (incl. D1 as Major) | 1 borderline | 8/8 | 5 | 72 (11 / 42 / 19) | 11 |
| T6 small, no skill | 8.0 | 4.5 | 3.5 | 30.2% | 5 | 5 | 7/8 | 2 | 31 (4 / 16 / 11) | 4 |
| T7 small + skill | 11.0 | 1.5 | 7.0 | 36.8% | 2 | 2 | 7/8 | 2.5 | 24 (7 / 8 / 9) | 7 |
| **R2-T1 large + revised skill** | 25.0 | 6.0 | 20.0 | 96.2% | 0 | 0 | 8/8 | 5 | 46 (4 / 22 / 20) | 4 (all defensible) |
| **R2-T7 small + revised skill** | 10.5 | 5.0 | 11.0 | 50.0% | 2 | 5 | 6/8 | 3 | 35 (14 / 11 / 10) | 14 (7 not defensible, 4 borderline) |

## Conclusions

1. **Large model: recall is flat-to-slightly-down (99.1% to 96.2%, 52.5 to 51.0) but every quality measure improved.** Findings dropped 59 to 46, Criticals 6 to 4 with all four defensible, Major share 68% to 48%, false positives 0.5 to 0, the D1 padding rider is gone and density is now explicitly cleared, R2 and R20 have their own findings rows (#19, #21), system-health counts are exact, R16's "fixed width, not a percentage" is now stated, and the pages were actually rendered with findings that cite the pixels (400px overflow, invisible active nav). The 1.5 points lost are the price of consolidation: R19 (bullet spacing) and R22 (avatar containers) vanished, and R11 (borders everywhere) survives only as riders in four other rows plus system health. The skill should keep a short list of "small visual items not to drop when merging" or a final sweep for element-level VR checks.
2. **Small model: a real gain, 36.8% to 50.0% (19.5 to 26.5; no-skill T6 was 30.2%), driven almost entirely by the mechanical pass.** Accessibility went 1.5 to 5.0 (labels, alt on both pages, span-onclick, landmarks/skip link and all four key contrast pairs now found), contrast is no longer deferred to "not verified", system-health counts are exact instead of undercounted, R rose 7 to 11 (though R2, R6, R10 and half of R20 are earned only in system health, with no findings row: the round-1 T2 fault has moved to the small model), round 1's "the skill harmed accessibility" result is reversed rather than merely recovered (A 5.0 now beats no-skill T6's 4.5), and invoices.html now has a coverage row and a handful of real findings.
3. **What persists for the small model: it still does not run the judgment half of the checklist.** K actually slipped 11.0 to 10.5, with two outright regressions (K13 you-are-here and K19 instructions paragraph were found in round 1 and lost in round 2), and K4, K11, K12, K15, K16, K20, K21, K23, K24, K25 are still missed. It quotes the footer and empty-state colours (#14) without reading what the footer says (the fee) or noticing the useless controls, which shows the scanner output is steering attention toward measurable pairs and away from content. invoices coverage is still thin (R11 to R14, K15, K16, K25, A6 missed) and A6 is now actively praised.
4. **New problem 1, severity inflation got worse for the small model: 14 of 35 findings (40%) are Critical versus 7 of 24 (29%) before, and 7 of the 14 do not meet the definition.** Seven Criticals are one-row-per-contrast-pair transcriptions of contrast.py output, and landmarks, skip link, heading order and decorative-image alt are all Critical, while the keyboard-unreachable signup control (#24) is Major and loud Delete (#26) is Minor. The severity anchors were read as "anything accessibility = Critical". The skill needs to say explicitly that a failed AA ratio is Major unless the text is essential to a top task, that landmarks/skip link/alt on decorative images are Minor-to-Major, that same-cause contrast pairs must be merged into one finding, and it should probably cap Criticals (for example at 5) and force a check that each one names the blocked task.
5. **New problem 2, scanner noise and unverified pass-through.** R2-T7 #12 is a scanner candidate reported at Critical with "verify applied size" still attached, #14 repeats "on assumed white" without checking the cascade, and three findings are filed under the wrong screen (#11, #14, #31 tagged index; the classes are only used on invoices) because the scanner reports CSS lines and the model never mapped them to HTML usage. No false positive came from the ASSUMED-background pairs in either report, but only because all four happen to sit on white in this fixture; the fixture cannot currently catch that failure, so add a planted case if it matters. R2-T1's own harness note is the right fix: contrast.py and scan.py should take or print the font size so "passes only large text" is resolved by the tool, and scan.py should print which HTML files use each flagged selector.
6. **New problem 3, the coverage table is being filled in rather than derived, and praise got worse.** R2-T7's coverage cells sum to 50 against 35 findings and claim 9 invoices findings where 3 are located there, with "ok" entered for areas containing planted flaws; false praise rose 2 to 5 because "What's working" was written without cross-checking (it praises colour-only metrics, the label:value table, right-pushed brand, full-width inputs and the arbitrary button hues). The skill should require that every coverage count be the count of findings-table rows with that Screen and Area, that "ok" means a named check was done, and that each "What's working" bullet be tested against the checklist before it is kept.
7. **Rendering and evidence: fixed for the large model, only nominally for the small one.** R2-T7 ran screenshot.py but states the width as 1920px (the PNGs are 1280), uses nothing from the images, and misses the 400px overflow the same screenshots show; its evidence accuracy fell 7/8 to 6/8 with invented `:0` line citations, a false "signup has no h1" claim repeated in a top fix, and wrong nested-em arithmetic (13.125px vs 11.48px). The skill should require at least one screenshot-derived observation per screen (or an explicit "screenshots not viewed"), forbid line citations that were not read, and make the top-fix "Resolves" numbers checkable, since R2-T7's cross-references point at the wrong findings.
8. **Net: the revised skill fixed the round-1 large-model shortfalls (D1, R16, R2/R20 rows, rendering, severity) and the small model's accessibility, contrast-deferral, counts and skipped-screen faults, but it shifted the small model from "too little, under-measured" to "measurement-led, over-rated and under-judged".** The next revision should target severity anchors and merging rules, screen-mapping of scanner output, a derived coverage table, praise cross-checks, and an explicit second pass over the Krug-style items (header conventions, page names, breadcrumbs, local nav, form-page nav, goodwill) that the scanner cannot see.
