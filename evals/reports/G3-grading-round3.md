# G3 - Grading round 3: two final-skill audit reports vs. the Ledgerly answer key

Same grader standard and calibration rules as G1 and G2 (1 = names the specific planted problem and points at the right file/element/line; 0.5 = touches the area but misses the point, or one half of a two-part flaw; 0 = missed; findings, top fixes and system health all count; praise that contradicts a flaw reduces it; K3 needs the "Welcome" h1; K5 needs both halves; K10 is about looks; K12/K22 need both halves; R8 needs action hierarchy + loud Delete; A5/R1 a contrast number without the principle, or hero only = 0.5; D1 dedicated row = 1 FP, rider = 0.5; system-health statement that names the values AND the problem = 1, a bare count = 0.5, contradicting praise caps at 0.5). All citations checked against the fixture (index.html 94 lines, invoices.html 97, signup.html 78, styles.css 124).

Reports graded:
- **R3-T1** = R3-T1-analyze-plain.md (large model + final skill), compare with R2-T1 and round-1 T1.
- **R3-T7** = R3-T7-haiku-skill.md (small model + final skill), compare with R2-T7, round-1 T7 and T6.

## 1. Scores per flaw (score, finding number that earned it)

### Usability K1-K25

| ID | R3-T1 large + final skill | R3-T7 haiku + final skill |
|----|----|----|
| K1 clever nav names | 1 (#7, all five) | 1 (#27; generous: names only Hive, Pulse, Toolbox, omits the two live ones, Launchpad and The Vault; rated Minor, filed index although Global; G2 gave 1 for 4 of 5, same rule applied: problem named at the right element) |
| K2 vague motto | 1 (#17) | 0 (motto appears only as a contrast pair, #19; **regression**, R2-T7 had 1) |
| K3 happy-talk h1 + mission para | 1 (#22 names "Welcome to Ledgerly!"; #17 blurb) | 0.5 (#1 paragraph only) |
| K4 "About this section" | 1 (#22) | 0 |
| K5 no start point | 1 (#19 five CTAs; #3 real signup is a black span; #18) | 0.5 (#2, #6 CTA count only; never finds the span; fix is now a sensible "Create account" primary) |
| K6 first screen fails "what is this" | 1 (#17) | 1 (#1, #9, top fix 4) |
| K7 search | 1 (#24 all four parts, #25) | 0 (finder never mentioned; **regression**, R2 had 0.5) |
| K8 forced choice | 1 (#20) | 0 (**regression and inverted**: #9 calls "Which one are you?" the *entry point* the promos distract from; R2 and R1 both had 1) |
| K9 promo overload | 1 (#21) | 1 (#9) |
| K10 clickability | 1 (#27 fakelink + ghostlink; #24/#25 blank .go) | 0 (R2 had 0.5) |
| K11 site ID not top-left / not link | 1 (#9) | 0.5 (#17 not a link home; position never noticed; no line cited) |
| K12 utilities too many + too loud | 1 (#10 count + bold blue underlined) | 0 |
| K13 you-are-here | 1 (#8) | 0 |
| K14 page name missing/mismatch | 1 (#28) | 0.5 (#14 no h1; title/nav mismatch not noticed) |
| K15 breadcrumbs misused | 1 (#28: 16px bold, "/", standing in for the name; fix small ">") | 0 (and praised: "provides good wayfinding") |
| K16 sidebar no current item | 1 (#29) | 0 (sidebar praised as "logical and scannable") |
| K17 over-collecting form | 1 (#2) | 1 (#4; centred on the card, but states "reduce to essentials"; fix keeps phone) |
| K18 rigid formats | 1 (#37, all three incl. DOB) | 1 (#5; phone + card) |
| K19 instructions paragraph | 1 (#40) | 1 (#15; recovered from R2) |
| K20 full nav on form page | 1 (#41, second half of the row) | 0 |
| K21 signup name mismatch + title | 1 (#41) | 0 |
| K22 generic error + Clear = Submit | 1 (#38, #39) | 0.5 (#13 reset button exists; twin styling not noted; the always-visible error div is never mentioned; R2 had 1) |
| K23 fake sincerity | 1 (#58) | 0 |
| K24 hidden fees | 1 (#23) | 0 |
| K25 empty state + useless controls | 1 (#34) | 0 |
| **K subtotal** | **25.0** | **8.5** |

### Accessibility A1-A6

| ID | R3-T1 | R3-T7 |
|----|----|----|
| A1 no labels | 1 (#1) | 1 (#7, #8; but #7 says "only input name=n has `<label>`": it has a `<span>`, which is the planted trap) |
| A2 no alt | 1 (#48, both pages) | 0 (**regression**: no mention of alt anywhere; it was a scan candidate; R2 had 1) |
| A3 span onclick not keyboard operable | 1 (#3, #25) | 0 (**regression**: no mention of onclick/ghostlink/.go; scan candidate; R2 had 1) |
| A4 no skip link / landmarks | 1 (#11) | 1 (#11, #12, #25) |
| A5 contrast failures | 1 (#4, #5, #23, #26: all four key pairs + six more) | 0.5 (only the hero pair of the four key pairs; footer #bbb, .empty #aaa and .btn-grey are never measured or mentioned; "6 pairs measured"; R2 had all four) |
| A6 color alone | 1 (#32) | 0 |
| **A subtotal** | **6.0** | **2.5** |

### Visual R1-R22

| ID | R3-T1 | R3-T7 |
|----|----|----|
| R1 grey / translucent white on color | 1 (#26) | 1 (#19, #20; #20 states "not translucent white", in garbled form) |
| R2 too many font sizes | 1 (#12) | 1 (#3, top fix 7, system health) |
| R3 weight 300 | 1 (#13) | 1 (#18) |
| R4 pure black, no grey hierarchy | 1 (#45 pure black; #13, #33 no hierarchy) | 0 (pure black never mentioned; **regression**, R2 had 1) |
| R5 nested em | 1 (#12, #14) | 1 (#26) |
| R6 spacing one-offs + cramped | 1 (#14, #43) | 1 (#3 + system health "no scale") |
| R7 ambiguous label spacing | **0** (no row on `.field .lbl` 10 = input 10 = field 10; #52 is the bullet list; **lost**, R2-T1 #38 and round-1 #54 had it) | 0 (system health's generic "no 2x rule for outside-group vs inside-group gaps" points at nothing) |
| R8 action hierarchy, loud Delete | 1 (#30, #31) | 0 (**regression and praised**: "Destructive actions (Delete ...) are not emphasized as primary; Send Reminder is primary") |
| R9 disabled-looking Mark as paid | 1 (#4) | 0 (R2 had 0.5) |
| R10 mixed radius | 1 (#47) | 1 (system health only: values, tied to buttons, "No consistency") |
| R11 borders everywhere | 1 (#46, dedicated row; **recovered**) | 1 (system health only: "17 declarations ... every panel/field/region. No separation by spacing/background first") |
| R12 label:value wall | 1 (#33) | 0 |
| R13 shouting section titles | 1 (#56, #44) | 0 |
| R14 left-aligned amounts | 1 (#54) | 0 |
| R15 centered long text / measure | 1 (#50, #15) | 0 |
| R16 % sidebar, no max-width | 1 (#55 fixed width; #15 max-width) | 0.5 (#24 fixed width only) |
| R17 shadows | 1 (#53) | 1 (#10, now correctly filed under invoices) |
| R18 16px icon at 96px | 1 (#51) | 0 |
| R19 bullet spacing | 1 (#52, dedicated row; **recovered**) | 0 |
| R20 no color system | 1 (#5) | 1 (#28, #3; the contradicting colour praise of R2 is gone) |
| R21 line-height 1.2 | 1 (#43) | 1 (system health only: "1.2 on body (tight ... 1.4-1.5 recommended)") |
| R22 avatars height-only | 0 (#58 is purpose only, #48 alt only; still lost) | 0 |
| **R subtotal** | **20.0** | **10.5** |

## 2. Subtotals

| Report | K /25 | A /6 | R /22 | Total /53 | % |
|----|----|----|----|----|----|
| R3-T1 large + final skill | 25.0 | 6.0 | 20.0 | 51.0 | 96.2% |
| R3-T7 small + final skill | 8.5 | 2.5 | 10.5 | 21.5 | 40.6% |

For reference: R2-T1 51.0 (96.2%), R2-T7 26.5 (50.0%), round-1 T1 52.5, round-1 T7 19.5 (36.8%), T6 16.0 (30.2%).

## 3. Decoys

| Decoy | R3-T1 | R3-T7 |
|----|----|----|
| D1 dense table | Left alone and explicitly cleared ("its compactness is acceptable density for a data table"); #54 flags alignment only, #46 borders. 0 FP. | Left alone (no table finding at all). |
| D2 quiet Archive | Correctly praised (quiet tertiary, 9.28:1). #42 "Cancel my subscription" is a different element and legitimate. | Not flagged; mentioned inside a false-praise bullet that lumps Archive with Delete as "not emphasized". |
| D3 system font stack | Praised | Not mentioned |
| D4 lang + viewport | Praised both | Not mentioned |

## 4. False positives

- **R3-T1: 0.** Again excludes `href="#"` stubs, missing image files and the `.example` address as fixture artifacts. Non-planted findings are true and checkable: #6 no responsive layout (0 media queries), #16 control borders 2.85:1 / 2.32:1, #35 unnamed selects, #49 no `:hover/:focus` rules, #42 "Cancel my subscription", #59 `type="text"` email [ext]. Speculative but labelled as such: #36 no "New invoice" entry point ("could not tell whether the function exists"), #32 metric direction "flag for the owner". Slips: #49 says "125 lines" (124); #46 and system health say all 17 borders are #999, but `styles.css:72` (in its own citation list) is `2px solid #1a6fe0`. Counts checked and correct: 16 exclamation marks, 11 controls / 8 required, 9 / 8 utilities.
- **R3-T7: 1.**
  1. #8 (Critical): abbreviated input `name` attributes ("name=n ... suggests single-letter shorthand") reported as an accessibility failure; `name` values are invisible to users and assistive technology. The labels half duplicates #7.
  - Wrong in detail, not counted: #7 "only input name="n" has `<label>`" (it is a `<span class="lbl">`, the opposite of the truth and the planted trap) and "inputs 40-46 (Email-ZIP)" (email starts at 41); #16 says placeholder text "must be deleted before typing" (false for a placeholder; that is the finder's `value`, which the report never found); #22 calls `#1fa34a` "button-blue"; #21 files a contrast finding under Area B; #9 treats the forced chooser as the page's entry point; What's working calls "Send Reminder" primary when all five buttons are equally solid.
  - Harmful fix: #4 keeps phone in the "essentials".
  - No placeholder `:0` citations and no false "X is missing" claim this round (R2's false "signup has no h1" is gone).

## 5. False praise

- **R3-T1: 0.** All six bullets are accurate; table density and Archive are the decoys, correctly praised.
- **R3-T7: 3** (R2-T7: 5). "Destructive actions (Delete on invoices, Archive in table) are not emphasized as primary; Send Reminder is primary" (directly contradicts R8: Delete is the biggest, red, uppercase; and R9); "Breadcrumb structure ... provides good wayfinding" (K15); sidebar "is logical and scannable" (K16, borderline). Fewer than R2 but the first is the worst single praise line in any round because it denies a planted flaw outright. The harness note also claims "Procedure followed exactly" and "All instructions clear; no ambiguities", which the output contradicts (R3-T1 listed nine real ambiguities in the same skill).

## 6. Evidence quality (8 spot-checks each)

| Report | Checked | Accurate | Notes |
|----|----|----|----|
| R3-T1 | css:24-25; css:26; index:88 + css:80; css:60 + invoices:58,88; signup:43,47,57; signup:67-68; css:110-111; css:75-76 | 8/8 | Ratios correct (1.68, 2.30, 2.55, 1.92, 3.28, 2.77, 3.82, 2.85, 2.32, 6.46, 4.78). Nested em about 11.5px correct. Top-fix "Resolves" numbers all map to the right findings. Only slips: "125 lines", "all #999". No `:0` citations, no false "missing" claims. |
| R3-T7 | index:47; index:49-53; signup:43,57; css:110-111; css:84; signup:67; css:3 (weight); css:45 (.btn font-size) | 6/8 | css:3 for `font-weight: 300` is wrong (line 7; same error as R2); css:45 is the `.btn {` line, font-size is 47. #17 has no line at all ("styles.css and all .html files"). #7's claim about a `<label>` is false. Contrast ratios quoted are correct. No `:0` citations. Flat vs R2 (6/8). |

## 7. Prioritisation (0-5)

Clusters: (a) value proposition / start point, (b) over-collecting signup, (c) unlabeled inputs + keyboard-inaccessible controls, (d) you-are-here + clever names, (e) action hierarchy with loud Delete.

- **R3-T1: 5.** Fix 1 form cut + labels + errors (b, c), fix 2 real signup control + action ranking incl. Delete and Mark as paid (a, c, e), fix 3 first screen by removal + fee (a), fix 4 header: brand, names, active state, utilities, h1, sidebar, crumbs, landmarks (d), fix 5 tokens + small-screen layout. All five clusters in five fixes, each with effort and correct Resolves lists.
- **R3-T7: 2.5** (R2: 3). Fix 1 = card + labels (b partly, half of c), fix 4 = value proposition (a partly). Fix 2 puts landmarks/skip link second and claims missing landmarks "block three top-task screens"; fix 6 is shadow direction and sidebar width, ahead of nothing users trip on. Absent from all seven: keyboard-unreachable signup/search (not found), you-are-here (not found), nav names (#27 is Minor and appears only as a number in fix 4's list, not in its text), Delete/action hierarchy (praised instead). Cross-references still wrong: fix 1 lists #21 (sidebar contrast) and #15 (help text); fix 2 lists #17 (brand link). The closing "6 fixes address 9 of 28 findings" lists 10 numbers.

## 8. System-health counts, "not verified", coverage, screenshots, filing

| Report | System-health counts | Not verified | Coverage | Filing / screenshots |
|----|----|----|----|----|
| R3-T1 | **All eight correct** (14 / 2 / 22 of which 15 greys / 18 / 2 / 3 / 0 / 0), plus line-heights 1, borders 17, var() 0 vs raw 199, and a concrete consolidation plan. | Honest and specific: no keyboard or screen-reader run, no 200% zoom, no states/validation, metric direction and nav meanings need the owner, "New invoice" unknown, widths between 400 and 1280 not captured. Names the rows each check would confirm. | Present, with Global row. **Every cell reconciles**: Global A1 B3 C1 D3 E3 F5 H3 = 19; index A5 B1 C2 D1 E1 F1 G2 H2 = 15; invoices B2 C5 D1 E1 F2 H3 = 14; signup B1 G9 H1 = 11; sum 59 = findings total. Cells of 0 are explained with pointers to where those problems are filed. | Filing correct (shared-CSS causes under Global, consequences under the screen that uses them; `.btn-grey`, shadows, `.empty` on invoices). **One explicit screenshot observation per screen**, each with 1280 and 400px detail (button collision, DELETE most prominent, shadows disagreeing, 1260px input wall), and #52 cites `index-mobile.png`. |
| R3-T7 | **All eight correct**; the size list now enumerates all 14 (R2 omitted 11/12). Slip: "all 1px solid #999". | Section present, but partly rhetorical questions ("Tested clicking vs tabbing? Focus indicators present?") and one nonsense item (contrast "will differ" under zoom). "promo grid may squeeze" shows the 400px image was not read. Does not disclose that only 6 contrast pairs were measured while scan.py flagged 10. | Present, with Global row. **Fabricated, worse than R2**: cells sum to 9 + 25 + 16 + 14 = **64 against 28 findings**, with the explicit false note "Each row sums to the findings under that screen". True rows: Global 7 (B1 E3 F1 H2), index 9 (A4 C1 F4), invoices 5 (B2 D1 F1 H1), signup 7 (G5 H2). Only 8 of 32 cells are right (5 of them in the Global row, counting "-" as 0). Uses "-" (undefined in the legend) and says no area reached "ok". | Filing mostly **fixed**: shadows, sidebar contrast and sidebar width now under invoices. Residual: #27 nav names filed under index (Global), #21 contrast under Area B, #22/#23 buttons under index only though also on invoices. **No per-screen screenshot observation**: one generic line in system health ("full-width nav, sidebar not reflow, form at 100% width"), nothing in any finding. Header width now correctly 1280. |

## 9. Severity calibration and merging

Definition applied: Critical = a top task is blocked, users are misled into harm or loss, a basic accessibility barrier exists (needed control unreachable by keyboard, essential text unreadable, form controls unnamed), or sensitive data is collected that the task doesn't need.

| Report | Critical | Major | Minor | Total |
|----|----|----|----|----|
| R3-T1 | 4 (7%) | 38 (64%) | 17 (29%) | 59 |
| R3-T7 | 9 (32%) | 16 (57%) | 3 (11%) | 28 |
| (R2-T1) | 4 | 22 (48%) | 20 | 46 |
| (R2-T7) | 14 (40%) | 11 | 10 | 35 |

- **R3-T1: all 4 Criticals defensible and each names the task or harm**: #1 unnamed controls ("blocks task 1 for screen-reader users"), #2 sensitive data ("collects sensitive data the task does not need"), #3 keyboard-unreachable signup ("blocks task 1 for keyboard users"), #4 Mark as paid 1.68:1 ("task 2 depends on"). The hidden fee is Major with the reasoning disclosed in the harness notes. **Regression: volume and Major share rebounded**, 46 to 59 findings and Major 48% to 64%, close to round 1 (59, 68%). Items that were Minor or riders in R2 are now separate Major rows (#16 border contrast, #35, #36, #42, #18), and several Majors are arguable Minors (#13 weight, #14 spacing scale, #12 type scale are system-hygiene items).
- **Merging, R3-T1:** same-cause contrast pairs merged into #5, landmarks + skip link + heading order into #11, alt into #48, uppercase into #44; per-screen consequences kept separate deliberately and explained. Merging no longer swallows small items (R11, R19 now have rows). Slight over-splitting instead: #19 and #18, #30 and #31.
- **R3-T7: 2 of 9 Criticals are sound (#4 sensitive data, #7 unnamed controls); 7 are not defensible**: #1 jargon copy, #2 five CTAs, #6 (a duplicate of #2), #9 promo overload (all Major usability; nothing blocked), #3 "no design system" (system hygiene, not even a user-facing finding), #5 rigid patterns (Major), #8 input `name` attributes (false positive). Only #4 comes close to naming a harm; none of the nine names a blocked task. Improvement: contrast pairs and landmarks/skip link are now Major, not Critical (14 to 9). But the textbook Critical, the keyboard-unreachable signup control, is now not found at all.
- **Merging, R3-T7: not done.** #2 and #6 are the same finding twice, both Critical; #7, #8 and #16 are one cause (no labels) in three rows; #11, #12 and #25 are landmarks three times; five contrast pairs are five rows (#19-#23). About 28 rows hold roughly 19 distinct findings.

## Comparison table (all nine rows)

| Report | K /25 | A /6 | R /22 | Total % | False positives | False praise | Evidence accuracy | Prioritisation /5 | Findings | Criticals |
|----|----|----|----|----|----|----|----|----|----|----|
| T1 large + skill | 25.0 | 6.0 | 21.5 | 99.1% | 0.5 (D1 rider) | 0 | 8/8 | 5 | 59 (6 Crit / 40 Maj / 13 Min) | 6 |
| T2 large agent + skill | 25.0 | 6.0 | 22.0 | 100.0% | 1 (D1) | 0 | 8/8 | 5 | 68 (10 / 37 / 21) | 10 |
| T5 large, no skill | 24.5 | 6.0 | 20.5 | 96.2% | 5 (incl. D1 as Major) | 1 borderline | 8/8 | 5 | 72 (11 / 42 / 19) | 11 |
| T6 small, no skill | 8.0 | 4.5 | 3.5 | 30.2% | 5 | 5 | 7/8 | 2 | 31 (4 / 16 / 11) | 4 |
| T7 small + skill | 11.0 | 1.5 | 7.0 | 36.8% | 2 | 2 | 7/8 | 2.5 | 24 (7 / 8 / 9) | 7 |
| **R2-T1 large + revised skill** | 25.0 | 6.0 | 20.0 | 96.2% | 0 | 0 | 8/8 | 5 | 46 (4 / 22 / 20) | 4 (all defensible) |
| **R2-T7 small + revised skill** | 10.5 | 5.0 | 11.0 | 50.0% | 2 | 5 | 6/8 | 3 | 35 (14 / 11 / 10) | 14 (7 not defensible, 4 borderline) |
| **R3-T1 large + final skill** | 25.0 | 6.0 | 20.0 | 96.2% | 0 | 0 | 8/8 | 5 | 59 (4 / 38 / 17) | 4 (all defensible, each names the task) |
| **R3-T7 small + final skill** | 8.5 | 2.5 | 10.5 | 40.6% | 1 | 3 | 6/8 | 2.5 | 28 (9 / 16 / 3) | 9 (7 not defensible; none names a blocked task) |

## Conclusions

1. **Large model: recall is identical to round 2 (51.0 / 53, 96.2%) but its composition changed.** Two of the three merge casualties were fixed: R11 (borders) and R19 (bullet spacing) now have dedicated rows (#46, #52). R22 (avatar height-only, no container/crop) is still missed for the second round running, and R7 (label margin = input margin = field gap on signup) is newly lost although rounds 1 and 2 both had it. Net zero.
2. **Large model process quality is the best of any round:** the coverage table reconciles cell by cell and sums to 59, zeros are explained, there is one concrete screenshot observation per screen, all four Criticals are defensible and each names the blocked task or harm, 0 false positives, 0 false praise, 8/8 evidence, both decoys cleared, top-fix cross-references all correct.
3. **What got worse for the large model is volume and the Major band:** findings went back from 46 to 59 and Major share from 48% to 64%, close to round-1 levels. The final skill's pressure to file a row per screen and per area appears to have reversed round 2's consolidation; several Majors (type scale, spacing scale, weight, border contrast) are system hygiene that would sit better as Minor.
4. **Small model: the final skill is worse than the revised skill, 50.0% down to 40.6% (26.5 to 21.5), only just above round-1 T7 (36.8%) and no-skill T6 (30.2%).** Accessibility halved (5.0 to 2.5): missing alt and the span-onclick controls, both scanner candidates found in round 2, vanished entirely, and only one of the four key contrast pairs was measured (6 pairs run vs 10 flagged), so footer, empty state and the grey button are gone. K fell 10.5 to 8.5 (K2, K7, K10 lost, K8 inverted into "the entry point", K22 halved; K19 recovered). The mechanical half of the procedure is now being partly skipped as well as the judgment half.
5. **Round-2 small-model problems that were fixed:** no `:0` placeholder citations and no false "signup has no h1"; findings are now filed under the right screen (shadows, sidebar on invoices); the screenshot width is stated correctly; contrast pairs and landmarks are no longer Critical (14 to 9 Criticals); false praise fell 5 to 3 and the contradictory colour praise is gone; the system-health size list is now complete.
6. **Round-2 small-model problems that persist:** 7 of 9 Criticals are still indefensible, now landing-page copy, a "no design system" row and a false positive instead of contrast pairs, and none names a blocked task while the one true keyboard blocker is not found at all; the coverage table is still fabricated and is now worse (cells sum to 64 against 28 findings, with an explicit false statement that rows reconcile); evidence is flat at 6/8 with the same wrong `styles.css:3` citation; nothing in any finding comes from a screenshot and there is no per-screen observation; top-fix cross-references still point at the wrong rows; the Krug-style judgment items (K4, K12, K13, K15, K16, K20, K21, K23, K24, K25) and the whole invoices visual set (R8, R9, R12, R13, R14, A6) are still missed.
7. **New for the small model and worse:** same-cause findings are not merged and now duplicate at Critical level (#2 = #6; #7, #8, #16 one cause; landmarks three times), so 28 rows hold about 19 distinct findings; "What's working" now praises the loud Delete as "not emphasized", a direct denial of a planted flaw; #7 asserts a `<label>` exists where the fixture has the planted `<span>`; and the harness notes claim "procedure followed exactly" and "no ambiguities", which is self-report the output disproves.
8. **Net:** the final skill's added structure (derived coverage, per-screen screenshot note, Critical must name the task, merge rule) is fully executed by the large model and improves its report, at the cost of renewed volume; the small model ignores or fakes every one of those self-check rules, and the extra procedure seems to have displaced the scanner-candidate reconciliation that produced its round-2 gains. For the small model, rules that depend on honest self-verification do not work; they need to be enforced by a script (count rows per Screen/Area, require every scan candidate to be dispositioned, reject a Critical without a task), not by instruction.
