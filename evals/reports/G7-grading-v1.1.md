# G7 - Grading: R6 audit report vs. the Ledgerly answer key

I used the same standard and calibration rules as G1-G3: 1 means the report names the specific planted problem and points at the right file, element or line; 0.5 means it touches the area but misses the point, or gets only one half of a two-part flaw; 0 means missed. Findings, top fixes and system health all count. Praise that contradicts a flaw reduces its score. Extra rules carried over: K3 needs the "Welcome" h1; K5 needs both halves; K10 is about looks; K12 and K22 need both halves; R8 needs action hierarchy plus the loud Delete; for A5 and R1, a contrast number without the principle, or the hero only, is 0.5; a dedicated D1 row is 1 FP and a D1 rider is 0.5; a system-health statement that names both the values and the problem is 1, a bare count 0.5, and contradicting praise caps it at 0.5.

I checked every citation against the fixture (index.html 94 lines, invoices.html 97, signup.html 78, styles.css 124).

Report graded:
- **R6** = R6-analyze.md. I compare it with **R3-T1** (large model + final skill, G3: 51.0/53, 96.2%, 0 FP, 4 Criticals all defensible, 59 findings).

## 1. Scores per flaw (score, finding number that earned it)

### Usability K1-K25

| ID | R6 | R3-T1 (G3) |
|----|----|----|
| K1 clever nav names | 1 (#1, all five, all three pages cited) | 1 |
| K2 vague motto | 1 (#18 names "Work. Smarter." among the non-answers; top fix 3 replaces it with a 6-8-word tagline beside the logo) | 1 |
| K3 happy-talk h1 + mission para | 1 (#18 "Welcome to Ledgerly!" + buzzword paragraph) | 1 |
| K4 "About this section" | 1 (#25, called happy talk, 114 words, which is correct) | 1 |
| K5 no start point | 1 (#23 five solid buttons, no primary; #21 and #26: the real signup is plain black `<span onclick>`) | 1 |
| K6 first screen fails "what is this" | 1 (#18) | 1 |
| K7 search | 1 (#22 all four parts: scope pulldown, no "Search" wording, hint set as `value`, blank go button; #26 span). Rated Minor, see section 9 | 1 |
| K8 forced choice | 1 (#19) | 1 |
| K9 promo overload | 1 (#20) | 1 |
| K10 clickability | 1 (#21 fakelink blue/underlined but static, ghostlink looks like text; #22 blank go button) | 1 |
| K11 site ID not top-left / not link | 1 (#2 `order:3`, not a link, no Home) | 1 |
| K12 utilities too many + too loud | 1 (#5: 9/8/3 count + "bold link-blue ... vs quiet grey sections") | 1 |
| K13 you-are-here | 1 (#3, #555 vs #4d4d4d, 1.13:1) | 1 |
| K14 page name missing/mismatch | 1 (#4 Vault vs "Billing Documents Manager"; #30 0 `<h1>`) | 1 |
| K15 breadcrumbs misused | 1 (#30 bold 16px, "/", no links, standing in for the name; fix: small linked ">" above an h1). "Last item not distinguished" is not stated, same as R3-T1 | 1 |
| K16 sidebar no current item | 1 (#36) | 1 |
| K17 over-collecting form | 1 (#45) | 1 |
| K18 rigid formats | 1 (#46, all three incl. DOB) | 1 |
| K19 instructions paragraph | 1 (#48, 89 words, which is correct) | 1 |
| K20 full nav on form page | 1 (#42) | 1 |
| K21 signup name mismatch + title | 1 (#4 "Join" opens "Become a Ledgerly Insider" titled "Ledgerly") | 1 |
| K22 generic error + Clear = Submit | 1 (#47 always-visible generic error tied to no field; #43 reset same solid blue as Submit) | 1 |
| K23 fake sincerity | 1 (#48 rider, named explicitly as fake sincerity) | 1 |
| K24 hidden fees | 1 (#24, plus top fix 4) | 1 |
| K25 empty state + useless controls | 1 (#41) | 1 |
| **K subtotal** | **25.0** | **25.0** |

### Accessibility A1-A6

| ID | R6 | R3-T1 |
|----|----|----|
| A1 no labels | 1 (#44; correctly says "Full name" is a span not tied to its input. Slip: "11 of 12 controls", when there are 11 fields and all 11 are unlabeled) | 1 |
| A2 no alt | 1 (#27 index icon, #50 avatars) | 1 |
| A3 span onclick not keyboard operable | 1 (#26, both spans) | 1 |
| A4 no skip link / landmarks | 1 (#17) | 1 |
| A5 contrast failures | 1 (all four key pairs, each with ratio and rule VR4.5: footer #15 1.92, `.empty` #41 2.32, hero #29 2.30/2.55, btn-grey #31 1.68; plus green/orange buttons 3.28/2.77, sidebar 3.82, input borders 2.85) | 1 |
| A6 color alone | 1 (#38 "rely on colour alone ... no sign or arrow") | 1 |
| **A subtotal** | **6.0** | **6.0** |

### Visual R1-R22

| ID | R6 | R3-T1 |
|----|----|----|
| R1 grey / translucent white on color | 1 (#29 both, with principle) | 1 |
| R2 too many font sizes | 1 (#9, 14 sizes, near neighbours listed) | 1 |
| R3 weight 300 | 1 (#8) | 1 |
| R4 pure black, no grey hierarchy | 1 (#8 and #11 pure black; #33 and #34 no hierarchy, every cell the same size and weight) | 1 |
| R5 nested em | 1 (#9 0.875 in 0.875 = 11.5px; #51; #7 em padding) | 1 |
| R6 spacing one-offs + cramped | 1 (#7 18 values incl. 3/6/7/9/13/22/26; #8 cramped) | 1 |
| R7 ambiguous label spacing | **1** (#49 "label-to-input gap (10px) equals field-to-field gap", `styles.css:118-120`; **recovered**, R3-T1 had 0) | 0 |
| R8 action hierarchy, loud Delete | 1 (#32 Delete biggest, 18px uppercase solid red, six solid buttons; #23; top fix 2 pyramid) | 1 |
| R9 disabled-looking Mark as paid | 1 (#31; #41 Export "disabled-looking") | 1 |
| R10 mixed radius | 1 (#14) | 1 |
| R11 borders everywhere | 1 (#13, own row, "separate with spacing and background") | 1 |
| R12 label:value wall | 1 (#33, incl. "12 days overdue" combined and dropping obvious labels) | 1 |
| R13 shouting section titles | 1 (#35; #10 all-caps without tracking) | 1 |
| R14 left-aligned amounts | 1 (#34) | 1 |
| R15 centered long text / measure | 1 (#28, 180-200 chars, max-width ~65ch) | 1 |
| R16 % sidebar, no max-width | 1 (#37 fixed width; #49 1270px inputs + max-width; #28 measure) | 1 |
| R17 shadows | 1 (#39 lit from side/below, differ per panel, "one small shadow scale") | 1 |
| R18 16px icon at 96px | 1 (#27 rider) | 1 |
| R19 bullet spacing | **0** (no finding on `.features li { margin: 0; line-height: 1.2 }`; the bullets are only praised for content; **lost**, R3-T1 had a dedicated row #52) | 1 |
| R20 no color system | 1 (#11) | 1 |
| R21 line-height 1.2 | 1 (#8) | 1 |
| R22 avatars height-only | 0 (#50 is alt and purpose only; still missed, as in every large-model round since round 1) | 0 |
| **R subtotal** | **20.0** | **20.0** |

## 2. Subtotals

| Report | K /25 | A /6 | R /22 | Total /53 | % |
|----|----|----|----|----|----|
| R6 | 25.0 | 6.0 | 20.0 | 51.0 | 96.2% |
| R3-T1 (baseline) | 25.0 | 6.0 | 20.0 | 51.0 | 96.2% |

The total is identical, but one flaw swapped: R6 gains R7 (label spacing) and loses R19 (bullet spacing). Both still miss R22.

## 3. Decoys

| Decoy | R6 |
|----|----|
| D1 dense table | Not flagged as too dense. #34 flags only primary datum, alignment and status pills; #13 flags borders (allowed); #6 flags the table being cut off at 400px (a real responsive issue, not density). 0 FP. It is not explicitly cleared, as R3-T1 did, but it is left alone. |
| D2 quiet Archive | Correctly praised ("link-styled rather than a solid button ... repeated row actions are never primary"). |
| D3 system font stack | Praised. |
| D4 lang + viewport | Praised. |

## 4. False positives

- **R6: 0.** Like R3-T1, it excludes `href="#"` stubs, missing image files and the `.example` address as fixture artifacts, and says so up front. The non-planted findings are all true and checkable:
  - #6: no media queries (0).
  - #12: green/orange button contrast 3.28/2.77.
  - #13 (second half): input borders 2.85:1.
  - #16: 0 state rules.
  - #40: sidebar link 3.82:1.
  - #43: "Cancel my subscription" on a signup form.
  - #27 (third part): h1 jumps to h3. True: the promo h3s at index:65 follow the h1 at :45, and the only h2 is at :76.
  - #41: "no way to create a recurring invoice".
  - #36 (second half): the screen mixes detail with a list.
- **Unhedged assumption, not counted:** #38 asserts that Outstanding and Avg. days to pay went *down* and that the decreases are good. The only direction signal in the fixture is the class name `down`; the visible text is "14%" and "3" with no sign. R3-T1 labelled the same point "flag for the owner". The inference is reasonable and the colour-alone half is certainly right, so it is not an FP, but it should have gone into "Not verified".
- **Count slips, not counted:**
  - "8 red uppercase promos ... with 18 exclamation marks": the promos contain 16 (R3-T1 said 16); 18 is the whole page.
  - "11 of 12 controls": there are 11 fields.
  - "Inputs stretch to 1270px": 1280 minus 2 x 10px padding = 1260px.
  - "44 `#` links": 43 anchors plus one `location.href='#'` handler, so defensible.
- Verified correct: 114-word About, 89-word instructions, 199 declarations, 17 border declarations, six solid buttons on invoices (5 actions + Export), sidebar ~320px at 1280.

## 5. False praise

- **R6: 0.** All five bullets are accurate:
  - Blue 4.78:1 and red 4.85:1 are correct. Keeping the red *fill* in the palette does not contradict #32, which is about Delete's size, placement and prominence.
  - The feature-bullets bullet praises their content, not their spacing, so it does not contradict R19.
  - Archive, the font stack, and lang/viewport are the decoys, correctly praised.

## 6. Evidence quality (8 spot-checks, plus an extended check)

| Report | Checked | Accurate | Notes |
|----|----|----|----|
| R6 | css:26 (`order:3`); css:24-25 (active #4d4d4d); index:39 + :88 (span onclick); invoices:58 + css:60 (btn-grey Mark as paid); css:110-111 (shadows); signup:43, :47, :57 (patterns / "exactly"); signup:58 (error div); css:118-120 (lbl 10 / field 10 / input 10) | 8/8 | **Extended check of about 25 more citations:** css:20/37/41/48/59 (spacing), css:59/65/103 (all-caps), css:64/90/94/102/120 (borders), css:7-10 + 94, invoices:28-35, 41/63, 42-52, 64-66, 71-79, 82-89, index:30-39, 45-53, 57-61, 64-73, 75-77, 81/65, signup:11-30, 36, 61-63, 67-69. All correct.<br>**One loose citation:** #9 cites `styles.css:45` (the `.btn {` line) for the em font size, which is at :47. The scan output itself attributes `.btn 1em` to :45, and the citation sits in a list, so it is not scored as an error. G3 did score this against R3-T7, where it was a pinpoint claim.<br>Contrast ratios checked: 1.13, 1.68, 1.92, 2.30, 2.32, 2.55, 2.77, 2.85, 3.28, 3.82, 4.78, 4.85, all correct. Nested em 11.5px correct. No `:0` citations, no false "missing" claims. Slips as in section 4. |

## 7. Prioritisation (0-5)

The five clusters: (a) value proposition / start point, (b) over-collecting signup, (c) unlabeled inputs + keyboard-inaccessible controls, (d) you-are-here + clever names, (e) action hierarchy with loud Delete.

- **R6: 5.** All five clusters are covered in six fixes, each with effort and a Resolves list:

| Fix | What it does | Clusters | Resolves list |
|----|----|----|----|
| 1 | Cut the form to name/email/password, `<label for>` on every control, remove reset and the always-on error | b, c | #43-48, #51, correct |
| 2 | Action pyramid; Mark as paid gets passing contrast; Delete becomes quiet text with a confirm step | e | #31, #32 |
| 3 | New hero; drop the chooser and promos; make "Create your free account" a real link | a, c (keyboard half) | lists #26 |
| 4 | Fee visible next to the call to action | K24 | |
| 5 | Plain names, logo top-left, two-cue active state, h1/title match | d | #1-4, #30, #36, correct |
| 6 | Tokens, `:focus-visible`, 400px layout | | |

- Cross-reference looseness (minor):
  - Fix 3 lists #27 (icon alt/scale, heading order), which the fix text does not address, and omits #23 (five buttons), which its text does address.
  - Fix 6 omits #11 and #15, which its text covers.

## 8. System-health counts, "not verified", coverage, screenshots, filing

| Report | System-health counts | Not verified | Coverage | Filing / screenshots |
|----|----|----|----|----|
| R6 | **All correct, checked against scan.txt**: font sizes 14 (3 em), weights 2, line-heights 1, colours 22 (15 greys, black x3), spacing 18, shadows 2, radii 3, borders 17, tokens 0 (0 of 199 use `var()`), media queries 0, state rules 0. Names the values and the problem, with a concrete consolidation plan. No "all #999" slip this time. | Honest and specific: nothing wired (no flows or states to inspect), no keyboard/screen-reader run, text-size bump not tested, image content unknown, Hive/Pulse/Toolbox need the owner. It recommends a 5-user test. Omissions: metric direction (asserted in #38 instead) and screen widths between 400 and 1280. | Present, with a Global row. **Every cell reconciles**: Global A1 B4 D2 E3 F5 H2 = 17; index A4 B1 C1 E1 F1 G2 H2 = 12; invoices B2 C5 D1 F3 H1 = 12; signup B1 C1 D1 G4 H3 = 10; sum 51 = findings total. Two small gaps compared with R3-T1: "-" (Global C, G) and "ok" are both used without a legend distinction, and the zero cells are not explained with pointers. | Filing correct: shared-CSS causes under Global, consequences under the screen (btn-grey under invoices, hero contrast under index, form width under signup). **Screenshots used**, but through findings rather than as one explicit observation per screen: #6 (400px nav/utility collision, CTA row and chooser off-screen, invoices table cut off), #3 ("invisible in the screenshots"), #37 (~320px of empty tint), #49 (inputs stretch at 1280). That covers all three screens but is less explicit than R3-T1's per-screen note. |

## 9. Severity calibration and merging

Definition applied (G3): Critical = a top task is blocked, users are misled into harm or loss, a basic accessibility barrier exists (a needed control unreachable by keyboard, essential text unreadable, form controls unnamed), or sensitive data is collected that the task doesn't need.

| Report | Critical | Major | Minor | Total |
|----|----|----|----|----|
| R6 | 3 (6%) | 27 (53%) | 21 (41%) | 51 |
| (R3-T1) | 4 (7%) | 38 (64%) | 17 (29%) | 59 |

- **R6: all 3 Criticals are defensible, and each names the task or harm:**
  - #31 Mark as paid 1.68:1 ("Blocks: recording a payment").
  - #44 unnamed controls ("Blocks: creating an account with a screen reader").
  - #45 sensitive data ("Harm: ... sensitive data the task does not need").
- **Calibration difference from R3-T1:** the `<span onclick>` signup call to action (#26) is Major, not Critical. By the letter of the definition it is a Critical candidate. But the utility link "Join" (`index.html:20`) is a real `<a href="signup.html">`, so keyboard users are not blocked from signing up, and Major is defensible, arguably more accurate. The same reasoning covers the search button, since search does nothing anyway. No penalty.
- **Arguable under-rating:** #22 search (K7, a four-part failure of a core wayfinding tool) is Minor; Major would fit better. #13 borders and #9 type scale as Minor is right (G3 had criticised R3-T1 for filing these hygiene items as Major).
- **Volume and Major band improved over R3-T1:** 59 findings down to 51, and Major share down from 64% to 53%, near R2-T1's 48%. The system-hygiene items G3 flagged as over-rated (type scale, spacing scale, border contrast) are now Minor.
- **Merging:** the report now leans toward over-merging, the opposite of R3-T1's slight over-splitting:
  - #8 combines three flaws (weight 300, line-height, pure black: R3, R21, R4).
  - #27 combines alt + scaled icon + heading order: three unrelated causes in one row.
  - #48 combines instructions + fake sincerity.
  - All are still credited because each is named explicitly. But the R19 loss probably comes from this consolidation: bullet spacing was never given a row, and "line-height 1.2" sits only in the global #8.

## Comparison table

| Report | K /25 | A /6 | R /22 | Total % | False positives | False praise | Evidence accuracy | Prioritisation /5 | Findings | Criticals |
|----|----|----|----|----|----|----|----|----|----|----|
| R3-T1 large + final skill | 25.0 | 6.0 | 20.0 | 96.2% | 0 | 0 | 8/8 | 5 | 59 (4 / 38 / 17) | 4 (all defensible, each names the task) |
| **R6** | 25.0 | 6.0 | 20.0 | 96.2% | 0 | 0 | 8/8 (1 loose list citation, 4 count slips) | 5 | 51 (3 / 27 / 21) | 3 (all defensible, each names the task/harm) |

## Conclusions

1. **Recall is identical to R3-T1: 51.0/53 (96.2%).** One flaw swapped: R6 recovers R7 (label gap = field gap, #49), which R3-T1 lost, and loses R19 (bullet spacing), which R3-T1 had as a dedicated row. R22 (avatar height-only) is missed again.
2. **Process quality is equal to R3-T1:**
   - 0 FP and 0 false praise.
   - 8/8 evidence, with a wide extended check that is also clean.
   - Coverage reconciles to 51.
   - System health correct, now without the "all #999" slip.
   - All Criticals defensible and named.
   - All five priority clusters in the top fixes.
3. **Better than R3-T1:** fewer findings (59 to 51) and a lower Major share (64% to 53%), which answers G3's main criticism of R3-T1. Hygiene items are now Minor.
4. **Slightly worse than R3-T1:**
   - More count slips (18 vs 16 exclamation marks, "11 of 12", 1270 vs 1260px).
   - #38 asserts the metric direction instead of flagging it for the owner.
   - Zero coverage cells are not explained.
   - Screenshots are used inside findings, not as an explicit per-screen note.
   - Consolidation swallows one small item (R19).
