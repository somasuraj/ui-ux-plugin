# G5 - Grading round 5 (small model): one audit report vs. the Ledgerly answer key

Same grader standard and calibration rules as G1, G2 and G3 (1 = names the specific planted problem and points at the right file/element/line; 0.5 = touches the area but misses the point, or one half of a two-part flaw; 0 = missed; findings, top fixes and system health all count; praise that contradicts a flaw reduces it; K3 needs the "Welcome" h1; K5 needs both halves; K10 is about looks, "span onclick is inaccessible" alone = 0.5; K12/K22 need both halves; R8 needs action hierarchy + loud Delete, "buttons inconsistent" = 0.5; A5/R1 a contrast number without the principle = 0.5; D1 dedicated row = 1 FP, rider = 0.5; a bad fix attached to a legitimate observation is a harmful fix, not a false positive; system-health statement that names the values AND the problem = 1, a bare count = 0.5, contradicting praise caps at 0.5). All citations checked against the fixture (index.html 94 lines, invoices.html 97, signup.html 78, styles.css 124).

Report graded:
- **R5** = round5/R5-haiku-analyze.md (small model + newest skill revision; scan.py now also lists words-and-navigation candidates: page-name mismatches, buried fees, competing solid buttons). Compare with R3-T7, R2-T7, round-1 T7 and T6.

Judgment calls made once, for this round:
- K1: only "The Vault" is touched, and as a link/title *mismatch*, not as a clever name; the other four names are never mentioned = 0.5.
- K9: framed as punctuation noise (exclamation marks); the fix rewrites the copy and keeps all eight promos = 0.5 (same as T6's "false urgency" framing in G1).
- K12: count is named with the right lines; prominence appears only as the single word "quieter" in the fix, bold blue / styles.css:28 never cited = 0.5 (G1 rule: count only = 0.5).
- R9: `.btn-grey 1.68:1` appears only as one entry in the ten-pair list of #31, "Mark as paid" is never named and "looks disabled" never said = 0 (A5 already credits the pair; R2-T7 got 0.5 for a dedicated row calling it "nearly invisible").
- R13: #20 is the 12px uppercase `th`, not the 22px all-caps h2 section titles = 0.5 (right principle, wrong element).

## 1. Scores per flaw (score, finding number that earned it)

### Usability K1-K25

| ID | R5 haiku + newest skill |
|----|----|
| K1 clever nav names | 0.5 (#6 renames "The Vault" only, as a mismatch; Launchpad, Hive, Pulse, Toolbox never mentioned; R3 and R2 had 1) |
| K2 vague motto | 0 (motto appears only as a contrast pair in #31; same rule as R3) |
| K3 happy-talk h1 + mission para | **1** (#2 names "Welcome to Ledgerly!" as filler, index:45; #3 the jargon paragraph, index:47; first small-model run to get the h1) |
| K4 "About this section" | 0.5 (#5 treats it as a long centred paragraph; "remove filler" is a rider in the fix, the fix otherwise keeps and re-paragraphs the content) |
| K5 no start point | 0.5 (#4 five solid CTAs; the real signup span is seen only as a keyboard problem in #16, called "feature CTA"; #8 relabels "Let's Go!" as "Create free account") |
| K6 first screen fails "what is this" | 1 (#3, top fix 2) |
| K7 search | 0.5 (#10 text must be deleted, miscalled a placeholder although the fix says "remove placeholder value"; #16 .go span; no "Quick Find" wording or scope-dropdown point) |
| K8 forced choice | 0 (chooser never mentioned; R1 and R2 had 1) |
| K9 promo overload | 0.5 (#7 exclamation-mark noise only; keeps all eight promos) |
| K10 clickability | 0.5 (#16 a11y only; .fakelink and looks never mentioned) |
| K11 site ID not top-left / not link | **1** (#11 `order:3` at css:26, "brand should be first (top-left), link to home") |
| K12 utilities too many + too loud | 0.5 (#12 count only; also says signup has 9, it has 8) |
| K13 you-are-here | 0 (top fix 5 says "users can't tell where they are" but no finding on `.nav a.active`) |
| K14 page name missing/mismatch | **1** (#1 + #6: "The Vault" -> title "Billing Documents Manager", no h1) |
| K15 breadcrumbs misused | **1** (#13: "/" separators, 16px bold, "positioned as if screen name", current item not distinguished; invoices:38) |
| K16 sidebar no current item | 0 |
| K17 over-collecting form | 1 (#23, Critical; fix "email, password, optional company name") |
| K18 rigid formats | 1 (#24 phone + card; DOB omitted, same as R3) |
| K19 instructions paragraph | 1 (#26; "89 words" is correct) |
| K20 full nav on form page | 0 (and "same nav bar and utilities on all three" is praised) |
| K21 signup name mismatch + title | **1** (#22, #6: "Join" vs "Become a Ledgerly Insider", title "Ledgerly") |
| K22 generic error + Clear = Submit | 0.5 (#25 reset button exists; twin styling not stated; the always-visible "Error: invalid input." is never mentioned) |
| K23 fake sincerity | 0 |
| K24 hidden fees | **1** (#9: 3.5% fee, 11px, 1.92:1, index:91 + css:124) |
| K25 empty state + useless controls | 0 (`.empty` appears only as a contrast pair in #31) |
| **K subtotal** | **14.0** |

### Accessibility A1-A6

| ID | R5 |
|----|----|
| A1 no labels | 1 (#14; "15 controls" is correct: 2 + 2 + 11; says all 11 signup fields are "placeholder only", the name field has the planted `<span class="lbl">`, not noticed but not denied either) |
| A2 no alt | 0.5 (#28 avatars only, Minor; `.bigicon` on index never mentioned) |
| A3 span onclick not keyboard operable | 1 (#16, both spans, index:39 and 88, Critical) |
| A4 no skip link / landmarks | 1 (#15) |
| A5 contrast failures | 1 (#31: all four key pairs plus six more, all ten ratios and all ten line numbers correct) |
| A6 color alone | 0 (#31 measures `.up` contrast only; "Metrics display ... in one glance" is praised) |
| **A subtotal** | **4.5** |

### Visual R1-R22

| ID | R5 |
|----|----|
| R1 grey / translucent white on color | 0.5 (#31 ratios only; the fix *recommends* grey on the blue hero, "#d0d0d0+ grey", which is the planted anti-pattern and at 4.19:1 still fails its own 4.5 target) |
| R2 too many font sizes | 1 (system health: 14 listed, "too many; no scale"; #30 "off-scale values") |
| R3 weight 300 | 1 (#29) |
| R4 pure black, no grey hierarchy | 1 (#32 pure black; #17 "all in same visual weight"; same credit rule as R2-T7) |
| R5 nested em | 1 (#30; arithmetic wrong, see section 6) |
| R6 spacing one-offs + cramped | 1 (system health "18 distinct (no scale) ... ad-hoc" with the repeated values named; #29 line-height) |
| R7 ambiguous label spacing | 0 |
| R8 action hierarchy, loud Delete | 0.5 (#34 Minor: "one-off button styles ... inconsistent radii and sizing"; five solid actions on invoices and biggest/red/uppercase Delete never stated; #4's "competing solid buttons" is index only) |
| R9 disabled-looking Mark as paid | 0 (see judgment calls) |
| R10 mixed radius | 1 (#34: 0, 4px, 18px, tied to buttons) |
| R11 borders everywhere | 0 (no row, no system-health line; R3-T7 had it in system health) |
| R12 label:value wall | **1** (#17, invoices:42-52; drop labels where the format explains the value) |
| R13 shouting section titles | 0.5 (#20, wrong element) |
| R14 left-aligned amounts | 0 |
| R15 centered long text / measure | 0.5 (#5 centred `.about` only; hero paragraph and line length / max-width never raised) |
| R16 % sidebar, no max-width | 0.5 (#19 fixed width only) |
| R17 shadows | 1 (#21, filed under invoices) |
| R18 16px icon at 96px | 0 |
| R19 bullet spacing | 0 |
| R20 no color system | 0.5 (system health "22 distinct (15 neutral greys) ... no coordinated palette; no tokens", capped by the praise "Color scheme uses blue ... with green and orange as accents - recognizable") |
| R21 line-height 1.2 | 1 (#29) |
| R22 avatars height-only | 0 |
| **R subtotal** | **12.0** |

## 2. Subtotals

| Report | K /25 | A /6 | R /22 | Total /53 | % |
|----|----|----|----|----|----|
| R5 small + newest skill | 14.0 | 4.5 | 12.0 | 30.5 | 57.5% |

For reference: R3-T7 21.5 (40.6%), R2-T7 26.5 (50.0%), round-1 T7 19.5 (36.8%), T6 16.0 (30.2%).

## 3. Decoys

| Decoy | R5 |
|----|----|
| D1 dense table | Left alone. #20 (uppercase headers) is a legitimate in-table point. 0 FP. |
| D2 quiet Archive | **Wrongly flagged, Major**, #18: "quiet-danger style (red underlined text) resembling links more than buttons ... use secondary button style (outline or low-contrast fill)". First small-model run to file the decoy as its own finding (T6 only attached a harmful fix to a colour critique). Six outline buttons down the table is exactly what the quiet treatment avoids. |
| D3 system font stack | Not mentioned |
| D4 lang + viewport | Not mentioned |

## 4. False positives

- **R5: 1.** #18 (D2, Major), see section 3. It reads like a scanner "looks like a link but is a button" candidate passed through without judgment.
- Non-planted findings that are true and acceptable: #27 "Cancel my subscription" on a signup page (R2-T1 and R3-T1 had the same), #33 heading order h1 -> h3 (true: index goes h1, h3 x8, h2), system health "0 :hover/:focus rules" (true).
- Wrong in detail, not counted: #12 "signup ... has 9 links" (8: there is no Join); #7 "18 exclamation marks in promo section" (16 in the promos, 18 on the page); #30 "2.5em (calculates to ~62px)" (15 x 2.5 = 37.5px); #23 cites "WCAG 2.5.1" (pointer gestures, irrelevant) for data minimisation; #14 says keyboard users cannot identify unlabeled fields (wrong user group, same slip as R2-T7); #1 treats "Ledgerly" vs "Welcome to Ledgerly!" on the home page as a mismatch (weak); #28 "why choose an avatar during signup?" and the suggested alt "Choose a profile picture" invent an interaction (hedged rider inside a legitimate alt finding, so logged as harmful fix; G1 counted T7 #20 because there it was the whole finding).
- Harmful fixes: #31 grey `#d0d0d0` on the blue hero (4.19:1, fails, and is the R1 anti-pattern); #18 promote Archive to a button; #28 above; #7 and #5 keep the promo grid and the "About this section" content instead of cutting them; system health recommends 3-4 font weights (the two-weight system is not the problem, weight 300 is).
- Self-undermining: "Not verified" says the patterns may not actually reject input and that the spans "could work with tabindex", while #24 and #16 are rated Critical on exactly those claims.
- No `:0` citations, no false "X is missing" claim, no unverified scanner candidate reported with "verify ..." still attached (R2's fault), no false positive from contrast pairs.

## 5. False praise

- **R5: 2, plus 1 borderline** (R3-T7: 3; R2-T7: 5).
  1. "Color scheme uses blue (#1a6fe0) as a primary consistently, with green and orange as accents - recognizable" (contradicts R20 and R8: the hues are arbitrary, and its own #34 calls them one-off styles).
  2. "Navigation structure is consistent across pages (same nav bar and utilities on all three)" (false on the facts: 9 / 3 / 8 utilities, and it contradicts its own #12; it is also K20, the full nav on the form page, presented as a virtue).
  - Borderline: "Metrics display ... shows key performance indicators in one glance" (the metrics are flaw A6; colour is not explicitly praised).
  - Empty rather than false: "Signup form collects enough information to identify users (even if too much)" against its own Critical #23; "Data table includes status and date columns". Nothing in "What's working" is a real strength; both decoys that deserved praise (Archive, system fonts, lang/viewport, table density) are absent or flagged.

## 6. Evidence quality (8 spot-checks)

| Report | Checked | Accurate | Notes |
|----|----|----|----|
| R5 | css:26 (brand order); invoices:38 (crumbs); index:91 + css:124 (fee, 1.92:1); signup:43,57 (patterns); css:110-111 (shadows); index:39,88 (spans); css:3-4 (weight / line-height); css:45 (.btn font-size) + the 62px claim | 6/8 | css:3-4 is wrong for the third round running (weight is line 7, line-height 10; #32 also cites css:3 for `color:#000`, actual 8). css:45 is the `.btn {` line (font-size is 47) and the 2.5em arithmetic is wrong (37.5px, not 62px). Everything else checked is right, and better than before: #31's ten lines (41, 42, 57, 58, 60, 66, 85, 98, 108, 124) and ten ratios are all correct (spot-recomputed 3.82, 3.28, 2.32, 2.77, 1.92), word counts 114 and 89 are exact, "15 controls" and "11 fields, 8 required" are exact. Flat at 6/8 vs R2/R3, but the errors are now line offsets and one sum rather than false claims. |

## 7. Prioritisation (0-5)

Clusters: (a) value proposition / start point, (b) over-collecting signup, (c) unlabeled inputs + keyboard-inaccessible controls, (d) you-are-here + clever names, (e) action hierarchy with loud Delete.

- **R5: 3.5** (R3-T7 2.5, R2-T7 3). Fix 2 = one CTA + plain value proposition (a, without the real signup link); fix 3 = cut the form + labels + flexible formats (b fully); fix 1 = labels + landmarks and fix 6 = span controls (c, both halves, but the keyboard blocker is last of six); fix 5 = link text matches page name, brand top-left, breadcrumbs (half of d: no you-are-here, no clever-names point); (e) absent, Delete never appears anywhere in the report. Fix 4 (contrast, black, line-height) correctly notes the footer hides the fee.
- **Every "findings" cross-reference is wrong**, worse than R3: fix 1 lists 1, 2, 3, 4, 15, 16, 17 (hero copy, CTAs and the kv table; should be 14, 15, 16, 33); fix 2 lists 5, 6, 7 (should be 2, 3, 4, 8); fix 3 lists 8, 9, 10 = button labels, fee, search (should be 23, 24, 14); fix 4 lists 11-14, 18, 19, 20 (should be 29, 31, 32, 9); fix 5 lists 21, 22, 24, 25, 26 = shadows, patterns, reset, instructions (should be 1, 6, 11, 13, 22); fix 6 lists 27, 28 = cancel link and avatar alt (should be 16). The numbers look like they belong to an earlier ordering of the table. Fix 1 also claims a missing h1 "blocks access by keyboard" users.

## 8. System-health counts, "not verified", coverage, screenshots, filing

| Report | System-health counts (truth: 14 / 2 / 22 of which 15 greys / 18 / 2 / 3 / 0 / 0) | Not verified | Coverage | Filing / screenshots |
|----|----|----|----|----|
| R5 | **All eight correct.** Size list enumerates all 14; weight tallies (700 x5, 300 x3), line-heights 1 and "0 state rules" also correct. Slips: recommends 3-4 weights; "both shadows wrong direction" fine. No border count (R3 had 17). | Short (4 items) and partly self-undermining (doubts its own two Criticals). Honest that 400px was "only layout tested via screenshot". Does not mention missing images, metric direction, screen reader or zoom. | Present, with Global row. **Reconciles cell by cell, first time for a small model**: Global A1 B2 E2 F2 H3 = 10 (#1, 11, 12, 14, 15, 16, 29, 30, 31, 32); index A2 C1 D1 G5 H1 = 10; invoices B1 C1 D2 E1 F2 = 7; signup A1 G5 H1 = 7; sum 34 = findings total. Weakness: every zero is "-" (not in the legend), no cell is "ok", so the table cannot distinguish "checked, nothing" from "not looked at" (invoices C/D/E have planted flaws behind their single counts; invoices G and signup B/C/D/E/F are all "-"). | **Filing correct throughout**: shared-CSS causes under Global (#29-32, #11, #14-16), shadows / sidebar / crumbs / kv / Archive under invoices. Only quibble: #34 button variants filed invoices-only though index uses them too. **No per-screen screenshot observation** although six PNGs exist in round5/shots-haiku; nothing in any finding comes from an image, the 400px overflow is absent, "0 media queries" is system health only. Header widths (1280 / 400) correct. |

## 9. Severity calibration and merging

Definition applied: Critical = a top task is blocked, users are misled into harm or loss, a basic accessibility barrier exists (needed control unreachable by keyboard, essential text unreadable, form controls unnamed), or sensitive data is collected that the task doesn't need.

| Report | Critical | Major | Minor | Total |
|----|----|----|----|----|
| R5 | 4 (12%) | 25 (74%) | 5 (15%) | 34 |
| (R3-T7) | 9 (32%) | 16 (57%) | 3 | 28 |
| (R2-T7) | 14 (40%) | 11 | 10 | 35 |
| (round-1 T7) | 7 (29%) | 8 | 9 | 24 |

- **3 of 4 Criticals are sound and one is not defensible under the G3 standard.** Sound: #14 unnamed controls ("screen reader ... users cannot identify form fields"), #16 keyboard-unreachable search button and signup link ("keyboard users cannot reach ...": the first small-model run to find the keyboard blocker AND rate it Critical; it does not notice that line 88 is the only signup entry on the page, which is the real reason it blocks task 1), #23 sensitive data ("users distrust overreach and abandon"). Not defensible: #24 rigid patterns (G3 ruled this Major; the placeholder states the format, so the task is slowed, not blocked, and the report's own "Not verified" doubts it). All four name a user group, task or harm, which no R3-T7 Critical did.
- **The inflation has moved down a band: 74% Major is the highest share of any run in any round.** Indefensible Majors: #18 (false positive), #20 letter-spacing on 12px table headers, #21 shadow direction, #32 pure black, #19 sidebar width, #33-type hygiene is correctly Minor but #29/#30 are system hygiene at Major. Under-rated or absent at the top: the hidden fee (#9, Major, arguably "misled into loss"), loud Delete (not found).
- **Merging: best small-model showing.** Ten contrast pairs are one row (#31; R3 had five rows, R2 seven Criticals), labels one row (#14), landmarks + skip link one row (#15), both spans one row (#16). Over-split: page-name mismatch is filed three times (#1 Global, #6 index, #22 signup, all the same title / h1 / link-text cause) and #2 / #3 and #4 / #8 overlap. 34 rows hold about 30 distinct findings (R3: 28 rows, about 19).

## Comparison table (small-model rows; first four copied unchanged from G3)

| Report | K /25 | A /6 | R /22 | Total % | False positives | False praise | Evidence accuracy | Prioritisation /5 | Findings | Criticals |
|----|----|----|----|----|----|----|----|----|----|----|
| T6 small, no skill | 8.0 | 4.5 | 3.5 | 30.2% | 5 | 5 | 7/8 | 2 | 31 (4 / 16 / 11) | 4 |
| T7 small + skill | 11.0 | 1.5 | 7.0 | 36.8% | 2 | 2 | 7/8 | 2.5 | 24 (7 / 8 / 9) | 7 |
| **R2-T7 small + revised skill** | 10.5 | 5.0 | 11.0 | 50.0% | 2 | 5 | 6/8 | 3 | 35 (14 / 11 / 10) | 14 (7 not defensible, 4 borderline) |
| **R3-T7 small + final skill** | 8.5 | 2.5 | 10.5 | 40.6% | 1 | 3 | 6/8 | 2.5 | 28 (9 / 16 / 3) | 9 (7 not defensible; none names a blocked task) |
| **R5 small + newest skill (words pass in scanner)** | 14.0 | 4.5 | 12.0 | 57.5% | 1 (D2 Archive flagged, Major) | 2 (+1 borderline) | 6/8 | 3.5 | 34 (4 / 25 / 5) | 4 (3 sound, 1 not defensible; all name a task or harm) |

## Conclusions

1. **Best small-model result in any round: 57.5% (30.5 / 53), up from 40.6% (R3) and 50.0% (R2), and the gain is almost entirely in K (8.5 -> 14.0), the band that three previous skill revisions could not move.** Of the thirteen previously-missed judgment items, six are now fully found: K11 (brand `order:3`, not a home link), K14 (The Vault -> "Billing Documents Manager", no h1), K15 (breadcrumbs: "/", 16px bold, standing in for the page name), K19 (instructions paragraph, recovered), K21 (Join vs "Become a Ledgerly Insider", title "Ledgerly") and K24 (3.5% fee in 11px 1.92:1 footer text); K4 and K12 are half-found; K3's "Welcome" h1 was also caught for the first time by a small model.
2. **That is plausibly the scanner's words pass and not better judgment:** every new hit is something a script can list (title vs h1 vs link text, a fee string in a low-contrast footer, `order` on the brand, "/" in `.crumbs`, link counts, word counts, competing solid buttons on index), the findings quote exact counts (114 and 89 words, 15 controls, 11 fields / 8 required) and ten correct contrast lines, and the same page-name candidate shows up three times (#1, #6, #22), which is what passing a list through looks like.
3. **Still missed are exactly the items no candidate list points at:** K13 (you-are-here, #555 vs #4d4d4d, which IS mechanically detectable and should be added to the scanner), K16 (sidebar current item), K20 (full nav on a form page, actually praised), K23 (fake sincerity), K25 (empty state with useless controls), plus K2 and K8 (both found in earlier rounds, now lost: the chooser is never mentioned), A6, the generic always-visible error, the `.bigicon` alt, and the invoices visual set R8 / R9 / R11 / R14 (Delete and "Mark as paid" appear nowhere in the report; the "competing solid buttons" candidate was applied to index only).
4. **Where a candidate needed interpretation, the model took the literal reading:** K1 became "The Vault doesn't match the title" rather than "these names are clever", K9 became "too many exclamation marks" with all eight promos kept, K4 became "long centred paragraph", R13 landed on the 12px `th` instead of the 22px h2s, and R1's fix recommends grey (#d0d0d0, 4.19:1, still failing) on the blue hero, which is the planted anti-pattern.
5. **What got worse:** the D2 decoy is flagged as a Major finding for the first time by a small model (#18, quiet Archive "resembles links, use a secondary button"), an unjudged candidate turned false positive; the Major band ballooned to 74% (25 of 34), the highest of any run, with letter-spacing, shadow direction, pure black and sidebar width all Major; every one of the six top-fix cross-reference lists points at the wrong findings (worse than R3); "What's working" contains no true strength and claims the utilities are the same on all three pages against its own #12; and "Not verified" casts doubt on two of its own Criticals.
6. **What got better besides recall:** Criticals fell 9 -> 4 with three sound and all four naming a task or harm, the keyboard-unreachable signup/search spans are found and rated Critical for the first time, the coverage table reconciles cell by cell (34 = 34) after being fabricated in R2 and R3, findings are filed under the right screens, same-cause contrast / label / landmark findings are merged into single rows, and there are no invented citations or false "missing" claims.
7. **Unchanged:** evidence accuracy is 6/8 for the third round with the same `styles.css:3` citation for weight and line-height plus a new arithmetic error (2.5em = "62px", actually 37.5px), and no finding draws on the six screenshots, so the script-enforced parts of the procedure now work while anything requiring the model to look, weigh or cut content still does not; the next scanner additions should be the active-vs-inactive nav colour delta, sidebar current-item check, controls next to an empty state, and a lint that top-fix numbers resolve to rows whose text matches.
