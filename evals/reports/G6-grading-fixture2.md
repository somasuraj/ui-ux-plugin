# G6 - Grading fixture 2 (Shiftboard, React + Tailwind): large model WITH skill vs WITHOUT skill

Same grader standard as G1-G3 (1 = names the specific planted problem and points at the right file/element/line; 0.5 = touches the area but misses the point, or one half of a multi-part flaw; 0 = missed; findings, top fixes and system health all count; overlapping ids scored separately; a contrast number without the visual principle = 0.5, as in G3 for A5/R1; a dedicated row on a decoy = 1 FP). Rules fixed for this fixture before scoring, applied to both reports:
- Handler-less demo buttons: a dedicated row presenting "button does nothing" as a flaw = 1 FP (fixture artifact, per the task brief); a "no handler" rider inside an otherwise legitimate finding is listed but not counted. The key's neutral items (dead Locations list, no breadcrumb, no save feedback) are not penalised.
- R1 needs the body-data flatness (name vs secondary data all 15px black), not only "headers look like body".
- R10 needs the near-duplicate point (sizes one px apart / two hexes one step apart), not only "no type scale".
- R16 needs borders-inside-borders beyond the Team table.

All citations checked against the fixture (Layout 11 lines, SideNav 39, TopBar 40, Toggle 19, WeekGrid 52, Schedule 145, Team 121, ShiftDetail 158, Settings 154, data.js 138).

Reports graded:
- **WITH** = round5/F2-analyze-WITH-skill.md (large model + ui-ux skill), 43 findings, numbered #1-#43.
- **WITHOUT** = round5/F2-analyze-WITHOUT-skill.md (same model, no skill), 79 findings, numbered A1-A18, B1-B20, C1-C15, D1-D12, E1-E10, F1-F4. (Report row ids A1.., D1.. are NOT the key's A/D ids; in the tables below the left column is always the key id.)

## 1. Scores per flaw (score, finding that earned it)

### Usability K1-K18

| Key ID | WITH skill | WITHOUT skill |
|----|----|----|
| K1 cute nav labels | 1 (#6, top fix 4) | 1 (A4) |
| K2 page name != nav label | 1 (#6, both pairs + shared `<title>`) | 1 (A4, E6, B1) |
| K3 Team has no page name | 1 (#27) | 1 (D1) |
| K4 you-are-here invisible | 1 (#7, 1.72:1 measured; #39 shift page no way back) | 1 (A3) |
| K5 ten top-bar utilities | 1 (#9, counts 10) | 1 (A8) |
| K6 brand far right, not a link | 1 (#8) | 1 (A12) |
| K7 happy-talk / instructions | 1 (#22, #38, #41: all three places) | 1 (B3, C8, E5: all three) |
| K8 forced Assignment mode | 1 (#35, #32) | 1 (C7) |
| K9 vague labels Submit/OK/Go/Add | 1 (#38, #42, #26, #31: all four) | 1 (C14, E3, B16, D10: all four) |
| K10 "No data" under filters | 1 (#24) | 1 (B16 + B17) |
| K11 key numbers buried in footer | 1 (#23, top fix 5) | 1 (B9) |
| K12 over-asking form | 1 (#35, notes cost center shown at :79) | 1 (C6, same) |
| K13 rigid formats | 1 (#32 time, #40 phone, #26 date) | 1 (C5, E2, B16) |
| K14 permanent banner + generic errors | 1 (#34, #32, #40) | 1 (C1, C2, E2) |
| K15 Delete between Submit/Cancel, no confirm | 1 (#33) | 1 (C3) |
| K16 segmented control state | 1 (#21, 1.05:1) | 1 (B7, 1.05:1) |
| K17 Role (4 options) hidden in a select | **0** (never mentioned) | **0** (never mentioned; the praise of the Role select's `<label>` is true and does not contradict K17) |
| K18 shift/slot/rota/rota entry | 1 (#10) | 1 (B11) |
| **K subtotal** | **17.0** | **17.0** |

### Accessibility A1-A9

| Key ID | WITH | WITHOUT |
|----|----|----|
| A1 icon buttons unnamed | 1 (#4) | 1 (A8) |
| A2 placeholder as label | 1 (#2, all 14 controls across three screens) | 1 (C4, E1, B16) |
| A3 div/span onClick | 1 (#1 nav + rows, #9 spans, #7 locations) | 1 (A2, A11, B13) |
| A4 img without alt | 1 (#4, all three) | 1 (A13, D11) |
| A5 no landmarks / h1 | 1 (#5) | 1 (A15) |
| A6 outline-none | 1 (#3; says 18, true count 21) | 1 (A9; enumerates all 21 lines exactly as the key) |
| A7 colour-only status | 1 (#16, both places) | 1 (B12, D6) |
| A8 low contrast + disabled-looking Publish | 1 (#11, #19, #23) | 1 (F1, B4, B9) |
| A9 Toggle div | 1 (#1; role/state/keyboard; label association not stated) | 1 (E4; all parts incl. label association) |
| **A subtotal** | **9.0** | **9.0** |

### Visual R1-R23

| Key ID | WITH | WITHOUT |
|----|----|----|
| R1 Team: no hierarchy | 0.5 (#30 headers = body only; never says name/secondary data are all equal) | 0.5 (D7 headers only; "secondary text color for the phone" appears only inside D11's fix) |
| R2 size-only hierarchy | 1 (#25) | 1 (B1) |
| R3 label:value wall | 1 (#36) | 1 (C9) |
| R4 competing solid buttons | 1 (#19) | 1 (B5, B4) |
| R5 36 solid row buttons | 1 (#28) | 1 (D2) |
| R6 loud red Delete | 1 (#33) | 1 (C3, C14) |
| R7 grey on coloured panel | 1 (#20: "neutral grey text on the brand blue ... washed out", fix white / brand-100) | 0.5 (B8: contrast numbers only, principle not stated; rated Critical) |
| R8 reduced-opacity white | 1 (#11 "translucent white", #8; fix brand-100 or white) | 0.5 (A10: ratios only; fix suggests "white/90", i.e. still opacity) |
| R9 arbitrary one-off values | 1 (#13, 218 uses / 76 distinct) | 1 (A18, examples, "dozens") |
| R10 near-duplicate sizes and greys | 1 (#14 run 11/12/13/14/15; #12 `#8b8b8b` vs `#8a8a8a`) | 0.5 (A18 "no type scale", lists both hexes as token bypass; never names the near-duplicates) |
| R11 font-light on body | 1 (#14) | 1 (A17) |
| R12 pure black vs ink tokens | 1 (#12, x27) | 1 (A17) |
| R13 label gap = field gap | 1 (#37) | 1 (C11) |
| R14 % sidebar | 1 (#15) | 1 (A1, fix `w-60`) |
| R15 no max-width | 1 (#43, #41 measure) | 1 (E8, C12) |
| R16 borders everywhere | 1 (#18: rows in bordered cards + ruled table) | 0.5 (D7: table cells only) |
| R17 mixed radii | 1 (#17) | 1 (B5, B15) |
| R18 arbitrary / upward shadows | 1 (#17) | 1 (B15, A14) |
| R19 centred long paragraph | 1 (#41) | 1 (E5) |
| R20 left-aligned numbers | 1 (#30) | 1 (D4) |
| R21 uppercase without tracking | 1 (#14, x8) | 1 (A7, D7) |
| R22 not responsive | 1 (#15, #29) | 1 (A1, D3) |
| R23 theme tokens bypassed | 1 (#12, system health) | 1 (A18) |
| **R subtotal** | **22.5** | **20.5** |

## 2. Subtotals

| Report | K /18 | A /9 | R /23 | Total /50 | % |
|----|----|----|----|----|----|
| WITH skill | 17.0 | 9.0 | 22.5 | 48.5 | 97.0% |
| WITHOUT skill | 17.0 | 9.0 | 20.5 | 46.5 | 93.0% |

## 3. Decoys

| Decoy | WITH | WITHOUT |
|----|----|----|
| D1 dense WeekGrid | Correctly praised ("deliberate density that stays readable", contrast measured). 0 FP. | Praised in "does well", but B18 and B19 (Minor) pile feature wishes and nitpicks on it (no per-day totals, no in-column add, hyphen vs en dash, 24h time). Not the key's trigger (too small / too dense), so not counted as a decoy hit; listed as noise. |
| D2 archive danger zone | Correctly praised; held up as the pattern #33 should copy. | Praised at length AND flagged: E10 is a dedicated Minor row ("final button has no onClick ... focus not moved ... opacity-50 only"). **1 FP** (decoy flagged at Minor; half of it is a fixture stub). |
| D3 Team search | Correctly praised | Correctly praised (D9, no-match state, is a legitimate separate point) |
| D4 time-off empty state | Correctly praised, used as the model for #24 | Correctly praised, used as the model for B17 |
| D5 system font stack | Left alone (listed neutrally under "what exists") | Left alone |

## 4. False positives

- **WITH: 0.** Handler-less buttons and the unimplemented Day/Fortnight views are explicitly dispositioned as fixture stubs (harness notes and system health); `Settings.jsx:134 opacity-50` dropped as a legitimate disabled state; the scanner's "7 exclamation marks" recognised as JS negations. Non-planted findings are all true and neutral per the key: #39 no way back, #42 no save feedback, #7 dead Locations. Slips, not counted: system-health says 14 text sizes (15; `text-xs` in WeekGrid omitted), outline-none 18 (21 bare), text-black x27 (29), "5 radius families" (6 classes if `rounded-card` is counted).
- **WITHOUT: 4.**
  1. B6 (Major): "None of Add slot / Copy last week / Export / Publish week / Go do anything ... dead buttons" - fixture stub presented as a design flaw in a dedicated row.
  2. F2 (Major): Tailwind Play CDN, dev React builds, in-browser Babel - this is the fixture's delivery mechanism, not a UI/UX finding.
  3. F3 (Minor): state kept in module globals, edits vanish on refresh - fixture artifact.
  4. E10 (Minor): decoy D2 flagged (see above).
  - Riders, not counted: "no handler" inside A8, A11, B4, D2, D10; B7 "changes nothing".
  - Out of scope but true, not counted: F4 `shortName` crash (code bug, not UX); B12 urgency logic bug; B20 wage bill excludes open shifts (true, a good catch).
  - Wrong in detail, not counted: B3 "60-word" paragraph (it is 78), E5 "80-word" (76), E8 "~1130px inputs" (about 1110 at 1440).
  - Padding that a developer must wade through (feature requests, not defects, none planted): B2 week switcher, B10 currency format, B18, B19, C13 smart assignee picker, D5 hours bar, D8, D12 sorting, E7, E9 timezone labels. About 10 of 79 rows.

## 5. False praise

- **WITH: 0.** All five bullets are accurate; four are the decoys.
- **WITHOUT: 0.** All six bullets accurate (the Role/Assign `<label htmlFor>` praise is true at `ShiftDetail.jsx:89,103`).

## 6. Evidence quality (8 spot-checks each)

| Report | Checked | Accurate | Notes |
|----|----|----|----|
| WITH | SideNav:14-26; Schedule:89-94; Toggle:3-10; ShiftDetail:55-59; ShiftDetail:67-69; Team:40; Settings:43 + 64-65; Schedule:140-142 (+ Team:86 phone format) | 8/8 | Arithmetic right: table 1100 vs about 1006px content at 1280; 9px gap Delete/Submit; 78- and 76-word paragraphs counted correctly; `bg-[#2f6fed]` x5 correct; 14 unlabeled controls correct. Coverage table reconciles cell by cell (18 + 8 + 5 + 8 + 4 = 43 = findings). Citations are basename-only (no `src/screens/`), adequate. |
| WITHOUT | Layout:3,7; SideNav:21; TopBar:27-31; Schedule:40-42; ShiftDetail:35-45 + 132; Team:68,71,74,77,80; Toggle:1-19; data.js:109-112 (+ data.js:42,53) | 8/8 | Full relative paths. A9 lists all 21 outline-none lines exactly. Overflow arithmetic (973px at 1240) right and honestly labelled as arithmetic. Only slips are the two word counts. |

## 7. Prioritisation (0-5)

Most serious clusters per the key: (a) shift form: forced/unneeded fields, rigid time, generic + permanent errors, unconfirmed Delete; (b) keyboard-unreachable nav/rows/toggle, unnamed controls, no focus; (c) Publish week looks disabled / no primary; (d) nav names, page names, you-are-here, top bar; (e) buried unfilled/overtime numbers; (f) tokens bypassed.

- **WITH: 5.** Fix 1 = (a), 2 = (b), 3 = (c), 4 = (d), 5 = (e) + happy talk + vocabulary, 6 = (f) + responsive. Each has effort and a Resolves list; cross-references all map to the right rows.
- **WITHOUT: 4.5.** Fix 1 = (a), 2 = (b), 3 = (c) + (e), 4 = (f), 5 = (d) + messages. Same clusters, equally actionable. Half a point off because its own Critical A1 (responsive) is left out of the top five ("next in line"), which shows the Critical was not believed, and no effort estimates.

## 8. System-health counts, "not verified", coverage

| Report | Enumerated system-health counts | Not verified | Every screen has findings |
|----|----|----|----|
| WITH | **Yes.** Text sizes 14 (true 15), weights 4 (correct: light 1, normal, medium 8, semibold), colours 24, spacing 27, shadows 3 (correct: 3 distinct, 2 not from above), radii 5 (6 incl. `rounded-card`), arbitrary 218 uses / 76 distinct (my broader regex: 245 / 91; same order), responsive 0 (correct), uppercase x8 without tracking (correct, 8 / 0), text-black x27 (29), outline-none 18 (21). Plausible throughout, consistently a little low because the scanner counts class strings, and it omits WeekGrid's `text-xs`. Includes what exists / missing / consolidate and notes the theme is duplicated in two files. | Honest and specific: no true 400px render (500px used, tool failure explained), nothing clicked, no screen reader, no zoom, data volume, business need for the extra fields, no real users. | Yes: Global 18, schedule 8, team 5, shift 8, settings 4; coverage table reconciles. |
| WITHOUT | **No.** Only "dozens of arbitrary pixel values" with examples in A18 and a measured contrast list in F1. No counts of sizes, colours, spacing, radii or one-offs. | Honest and specific: static renders only, no screen reader, contrast assumptions stated, D3 flagged as arithmetic not a measured render, breakpoints/zoom/dark mode, performance, business need, no user testing. | Yes: shell 18, schedule 20, shift 15, team 12, settings 10, cross-cutting 4. No coverage table. |

## 9. Severity calibration

Definition applied: Critical = a top task is blocked, users are misled into harm or loss, a basic accessibility barrier exists (needed control unreachable by keyboard, essential text unreadable, form controls unnamed), or sensitive data is collected that the task doesn't need.

| Report | Critical | Major | Minor | Total |
|----|----|----|----|----|
| WITH | 4 (9%) | 29 (67%) | 10 (23%) | 43 |
| WITHOUT | 11 (14%) | 48 (61%) | 20 (25%) | 79 |

- **WITH: 4 of 4 defensible**, each begins "Blocks:" or "Harm:": #1 nav/rows/toggle unreachable by keyboard; #2 14 unnamed controls; #32 shift save blocked by silent required fields + HH:MM:SS + "Invalid input."; #33 immediate unconfirmed delete (data loss). Arguable under-rating: "Publish week" looks disabled (2.05:1) is Major (#19); G3 accepted the equivalent as Critical. Major band is heavy (67%): #13 spacing scale, #14 type scale, #12 tokens are system hygiene that would sit better as Minor.
- **WITHOUT: 7 of 11 defensible** (A2 keyboard nav, C3 delete, C4 and E1 unnamed controls, E4 toggle, C2 validation that blocks save, B4 Publish unreadable/looks disabled), **1 borderline** (B8 KPI text 1.79/3.09:1: unreadable, but not needed to complete a task), **3 not defensible**: A1 not responsive (no task blocked on the desktop tool; its own top-5 omits it), C1 always-on banner (misleading, but no harm or loss: Major), E3 no save feedback / "OK" label (Major; neutral item per key). Same-cause splitting inflates the count: unnamed controls are two Criticals (C4, E1) plus part of B16; the shift form is four Criticals (C1-C4) where WITH has two.

## Comparison table

| Report | K /18 | A /9 | R /23 | Total % | False positives | False praise | Evidence accuracy | Prioritisation /5 | Findings | Criticals (defensible) |
|----|----|----|----|----|----|----|----|----|----|----|
| WITH skill | 17.0 | 9.0 | 22.5 | 97.0% (48.5/50) | 0 | 0 | 8/8 | 5 | 43 (4 Crit / 29 Maj / 10 Min) | 4 (4 defensible, each names the blocked task or harm) |
| WITHOUT skill | 17.0 | 9.0 | 20.5 | 93.0% (46.5/50) | 4 (B6, F2, F3 fixture artifacts; E10 decoy D2 at Minor) | 0 | 8/8 | 4.5 | 79 (11 / 48 / 20) | 11 (7 defensible, 1 borderline, 3 not: A1, C1, E3) |

## Conclusions

1. **Recall is near parity: 97% with the skill, 93% without, and identical on usability (17/18) and accessibility (9/9).** On a small, readable React/Tailwind codebase a large model finds almost every planted flaw unaided; the skill is not what produces recall here.
2. **The whole 2-point gap is in the visual band and is about naming the principle, not locating the element.** Without the skill the model reported grey-on-blue (R7) and translucent white (R8) purely as contrast ratios (and even suggested `white/90`), said "no type scale" without the near-duplicates (R10), and saw borders only in the Team table (R16); the skill run stated the Refactoring UI rule each time. Nothing planted was caught by the no-skill run and missed by the skill run; the only edge the other way is completeness of detail (all 21 `outline-none` lines vs "18", and the toggle's missing label association).
3. **Both runs missed K17 (four short Role options hidden in a `<select>`) and both only half-hit R1 (Team body data all 15px black with no emphasis on the name).** These are judgment items with no scanner signal: a labelled select looks "correct" in code, and the no-skill run even praised its label. The skill's checklist should prompt "few short important options in a dropdown" and "table body: what is primary vs secondary" explicitly.
4. **What the skill clearly added is precision and a report a developer can act on:** 43 findings against 79, 0 false positives against 4, fixture stubs and scanner false hits explicitly dispositioned, a coverage table that reconciles, effort and Resolves lists on each top fix, and enumerated system-health counts (sizes, colours, spacing, radii, shadows, 218 one-offs) that the no-skill report does not have at all. The no-skill report buries its correct findings among roughly 10 feature-request rows (week switcher, sorting, smart assignee picker, timezone labels), build-tooling complaints and a dedicated "dead buttons" row.
5. **Severity is the second clear gain:** 4 Criticals, all defensible and each naming the blocked task or harm, versus 11 of which 3 are not defensible (not-responsive, the always-on banner, no save feedback) and one is borderline, with the same cause split across several Criticals. The cost is a heavy Major band (67%) in which system-hygiene rows (spacing scale, type scale, tokens) are rated like user-facing problems, and "Publish week looks disabled" arguably under-rated at Major.
6. **The skill's cost on a framework codebase is tooling friction, not audit quality:** the screenshot script reported OK on blank PNGs (no render wait for Babel/Play CDN), the mobile capture never rendered (so there is no true 400px evidence, honestly disclosed), hash routes slug to the last segment, the CSS pass prints misleading "no tokens / no focus styles / no media queries" for a Tailwind project, the words pass counted JS `!` operators, contrast pairs had to be resolved from palette names by hand, and its counts run slightly low (14 of 15 text sizes, 18 of 21 outline-none, 27 of 29 text-black). The no-skill run got 1440 and 390px renders with no trouble.
7. **Implications for the skill on framework codebases:** add a render wait and a blank-image check to `screenshot.py` and slug the full hash; suppress or caveat the CSS pass when 0 declarations are found; resolve Tailwind default palette names to hex inside `scan.py`/`contrast.py` so contrast pairs are automatic; count `!` only in rendered JSX text; count utilities per occurrence across all files including shared components; emit the promised `[used in: ...]` attribution for JSX; read labels held in JS arrays for the nav-label vs page-name check; and spell out the JSX analogue of the `href="#"` stub rule (buttons without `onClick`), which this run had to infer.
8. **Net:** on this in-app product the skill converts an already complete but noisy, over-severe 79-row audit into a tighter, calibrated, zero-false-positive one with system-health numbers, at essentially equal recall; the remaining misses are the same judgment items for both, so the next gains must come from checklist prompts for those items and from fixing the scripts, not from more procedure.
