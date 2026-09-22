# ANSWER KEY - fixture2-shiftboard-react (PRIVATE, never show to testers)

Fixture: `<tests>\fixture2-shiftboard-react\`
Paths below are relative to that folder. Line numbers were verified with grep against the final files.
Counts: K = 18 usability, A = 9 accessibility, R = 23 visual, D = 5 decoys. Planted flaws total 50 (R6 deliberately overlaps K15, and R23 overlaps R9/R10; score each id separately).

Scoring notes
- A finding counts as a hit if it names the problem and points at the right screen/component; exact line is a bonus.
- Several flaws share a line (e.g. a button that is both vaguely labelled and oddly rounded). Score each id separately.
- Anything under "Decoys" that is reported as a problem is a false positive.
- Verification screenshots: `screenshot-schedule.png`, `screenshot-team.png`, `screenshot-shift.png`, `screenshot-settings.png` in this folder (1280x1400, headless Chrome).

## K - Usability (Krug)

| id | file:line | planted flaw | a correct finding says |
|----|-----------|--------------|------------------------|
| K1 | src/components/SideNav.jsx:2-4 | Cute nav labels "The Grid", "Crew HQ", "Control Room" | Nav items use clever/internal names; rename to the obvious words Schedule, Team, Settings. |
| K2 | src/screens/Schedule.jsx:19 and src/screens/Settings.jsx:58 | Page names do not match the nav label clicked ("The Grid" -> "Rota Planner", "Control Room" -> "Preferences") | The page title must match what the user clicked so they know they landed in the right place. |
| K3 | src/screens/Team.jsx:18-38 | Team screen has no page name at all (starts straight with search + Add) | Every page needs a prominent name; Team has none. |
| K4 | src/components/SideNav.jsx:21 | "You are here" is only text-gray-300 vs text-gray-400; also the shift detail page gives no location cue beyond that | The current nav item is practically indistinguishable; make the active state obvious (background, weight, bar). |
| K5 | src/components/TopBar.jsx:20-31 | Ten utilities in the top bar (help, gift, chat, apps, bell, mail, moon, Invite, Refer a cafe, Upgrade) | Too many utilities compete for attention; keep the few that are used, move the rest into a menu. |
| K6 | src/components/TopBar.jsx:33-37 | Brand/logo sits at the far right and is a plain div/img, not a link home | Site ID belongs top-left and should link to the home screen (Schedule). |
| K7 | src/screens/Schedule.jsx:23-28 (also src/screens/ShiftDetail.jsx:84-87, src/screens/Settings.jsx:76-82) | "Welcome to the Rota Planner!..." happy-talk and instructions nobody reads | Cut the welcome/instruction paragraphs; make the UI self-evident instead. |
| K8 | src/screens/ShiftDetail.jsx:115-125 (required at :42) | Required "Assignment mode" choice (Soft-assign / Hard-assign / Tentative hold), unexplained, no default | Forces a decision the user cannot make without thinking; remove it, default it, or explain the options in plain words. |
| K9 | src/screens/ShiftDetail.jsx:136, src/screens/Settings.jsx:96, src/screens/Schedule.jsx:134, src/screens/Team.jsx:36 | Vague button labels "Submit", "OK", "Go", "Add" | Buttons should say what they do: "Save shift", "Save settings", "Filter", "Add staff member". |
| K10 | src/screens/Schedule.jsx:113-136 | Swap requests empty state is "No data" under a row of four filters and a Go button | Empty state should explain what will appear and what to do; hide filters when there is nothing to filter. |
| K11 | src/screens/Schedule.jsx:140-142 | Unfilled count and projected overtime cost buried in an 11px pale footer next to a version string, while the loud summary banner (:64-77) shows less important totals | The numbers a manager most needs (unfilled shifts, overtime cost) must be prominent at the top, not hidden in the footer. |
| K12 | src/screens/ShiftDetail.jsx:127-129 (required at :42) | Form demands cost center code, approving manager employee ID and a reason for change for every edit | Do not ask for information the system already has or does not need (cost center is even shown at :79). |
| K13 | src/screens/ShiftDetail.jsx:37 and :112-113; src/screens/Settings.jsx:43 and :64 | Rigid formats: time must be HH:MM:SS typed into a text box; phone must be +1XXXXXXXXXX with no spaces/dashes; date filters want DD/MM/YYYY (Schedule.jsx:128,132) | Accept what people naturally type (or use time/date pickers) and normalise it, instead of rejecting it. |
| K14 | src/screens/ShiftDetail.jsx:67-69 (always-on banner), :39 and :43 ("Invalid input."), src/screens/Settings.jsx:65 ("Error: invalid value.") | Error banner is rendered permanently, before the user does anything; validation errors are generic and not tied to a field | Errors must appear only when something is wrong, next to the field, saying what is wrong and how to fix it. |
| K15 | src/screens/ShiftDetail.jsx:138-144 (handler :55-59) | "Delete rota entry" sits between Submit and Cancel, same size/shape, deletes immediately with no confirm or undo | Separate the destructive action from routine ones and add a confirm/undo step. |
| K16 | src/screens/Schedule.jsx:44-61 (active style :54) | Day/Week/Fortnight segmented control: active is bg-gray-100, inactive bg-gray-50, same text colour | Cannot tell which view is selected; give the active segment a clearly different treatment. |
| K17 | src/screens/ShiftDetail.jsx:106-110 | Role (4 short options) hidden in a dropdown | Few, short, important options should be visible at once (radio group / segmented buttons), not hidden in a select. |
| K18 | Schedule.jsx:19 "Rota Planner", :32 "Add slot", :67 "shifts", :85 "Open slots"; Team.jsx:43 "Rotas" column; ShiftDetail.jsx:65 "Slot #", :143 "Delete rota entry"; Settings.jsx:50,52 "Open slots", "rota digest"; README/routes say "shift" | The same object is called Shift, Slot, Rota and rota entry | Pick one word (Shift) and use it everywhere. |

## A - Accessibility

| id | file:line | planted flaw | a correct finding says |
|----|-----------|--------------|------------------------|
| A1 | src/components/TopBar.jsx:3-8 (used :20-26) | Seven icon-only buttons with no aria-label/title/text | Icon buttons need an accessible name (and ideally a visible label or tooltip). |
| A2 | src/screens/ShiftDetail.jsx:112-113, :127-130; src/screens/Settings.jsx:62-64 and select :66; src/screens/Schedule.jsx:114,120,126-133 | Inputs use placeholder instead of a label (placeholder vanishes once filled, as on Settings) | Every field needs a persistent visible label tied with for/id. |
| A3 | src/components/SideNav.jsx:14-26 (onClick :16), :32; src/components/TopBar.jsx:27-31; src/screens/Schedule.jsx:89-108 (onClick :91) | Navigation and clickable rows are div/span with onClick: no role, not focusable, no keyboard activation, no href | Use a/button elements so they are keyboard and screen-reader operable. |
| A4 | src/components/TopBar.jsx:34-35; src/screens/Team.jsx:61 | img elements without alt (avatars, logo) | Add alt text (or alt="" when decorative next to the name). |
| A5 | src/components/Layout.jsx:3-8, src/components/TopBar.jsx:15, src/components/SideNav.jsx:9; titles as div at Schedule.jsx:19, ShiftDetail.jsx:65, Settings.jsx:58 | No landmarks (header/nav/main) and page titles are divs, not h1 | Use semantic landmarks and real headings so assistive tech can navigate. |
| A6 | src/components/TopBar.jsx:5; src/screens/Schedule.jsx:31,34,37,40,53,114,120,127,131,134; src/screens/Team.jsx:35,89,92,95; src/screens/ShiftDetail.jsx:61,135,141,150; src/screens/Settings.jsx:46,95 | outline-none with no focus-visible replacement | Keyboard users get no focus indicator; add focus-visible ring styles. |
| A7 | src/screens/Team.jsx:1-5 and :64 (staff status dot); src/screens/Schedule.jsx:96-98 (red/yellow urgency dot) | Status conveyed by colour alone, no text, legend, or accessible name | Add a text label/badge; do not rely on colour only. |
| A8 | src/screens/Schedule.jsx:140 (text-gray-300 11px on white), :103, :136 and :40 ("Publish week" is a live button styled bg-gray-200 text-gray-400 so it looks disabled); src/screens/ShiftDetail.jsx:84 (gray-400 on white); src/components/SideNav.jsx:10,29 (gray-500 on #1f2937) | Low-contrast text and a real button that looks disabled | Text fails WCAG AA contrast; the primary "Publish week" action looks disabled though it is enabled. |
| A9 | src/components/Toggle.jsx:3-9; used at src/screens/Settings.jsx:85-90 | Custom toggle is a div with onClick: no role="switch", aria-checked, tabindex, key handling, and not associated with its text label | Use a checkbox/button with role switch and aria-checked, labelled by the row text. |

## R - Visual (Refactoring UI)

| id | file:line | planted flaw | a correct finding says |
|----|-----------|--------------|------------------------|
| R1 | src/screens/Team.jsx:47 and :63-87 | No hierarchy: headers, names, roles, numbers, contact all text-[15px] font-normal text-black | De-emphasise secondary data (contact, contracted) and emphasise the name; headers should be smaller/quieter. |
| R2 | src/screens/Schedule.jsx:19-21 | Hierarchy by size only: text-4xl / text-2xl / text-xl, all font-normal text-black | Use weight and colour, not just size; the week/location lines should be smaller and greyer. |
| R3 | src/screens/ShiftDetail.jsx:71-81 | Nine "Label: value" lines in one undifferentiated block | Label:value wall; drop labels where the value is self-explanatory, group, and emphasise the values that matter. |
| R4 | src/screens/Schedule.jsx:31-42 (+ Go at :134) | Four/five competing solid buttons in three different brand colours on one screen | One primary action per screen; make the rest secondary/tertiary. |
| R5 | src/screens/Team.jsx:89-97 | Solid blue Edit, solid green Message, solid red Remove repeated on all 12 rows | Row actions should be quiet (text links / overflow menu); 36 solid buttons drown the data. |
| R6 | src/screens/ShiftDetail.jsx:141 | Big solid red "Delete rota entry" as loud as the primary action | Destructive action that is not the main action of the page should be demoted (tertiary/red text) with a confirm. |
| R7 | src/screens/Schedule.jsx:64-76 | Grey text (text-gray-400 / text-gray-300) on the blue bg-brand-600 panel | Grey on a coloured background looks washed out and low contrast; use a tint of the background hue or white. |
| R8 | src/components/TopBar.jsx:5 (opacity-60), :16 (text-white/50), :27-28 (text-white/60) | White text/icons at reduced opacity on the blue bar | Reduced-opacity white on colour looks dull; hand-pick a lighter blue instead. |
| R9 | everywhere, e.g. src/screens/Schedule.jsx:20,23,30,64,84 (mt-[6px], mt-[22px], gap-[9px], p-[13px], w-[37%]), src/components/TopBar.jsx:15-36, src/components/SideNav.jsx:9-32, src/screens/Team.jsx:47-95, src/screens/ShiftDetail.jsx:61-71, src/screens/Settings.jsx:46 | Arbitrary one-off spacing/size values instead of the Tailwind scale | No spacing/sizing system; replace p-[13px], mt-[22px], text-[15px], w-[37%] etc. with scale values. |
| R10 | text sizes: text-[11px], [12px], [13px], [14px], [15px], [17px], [19px], [26px] plus text-sm/xs/xl/2xl/4xl (e.g. Schedule.jsx:66-67,85,140; TopBar.jsx:16,29,36). Greys: text-gray-300/400/500, text-[#8b8b8b] (Schedule.jsx:102), text-[#8a8a8a] (Settings.jsx:76) | Near-duplicate type sizes and greys, including two custom hexes one step apart | Define a small type scale and 2-3 text greys; remove the near-duplicates. |
| R11 | src/components/Layout.jsx:3 | font-light applied to the whole app body text | Light weights are for large headings only; body text at 14-15px should be normal weight. |
| R12 | src/components/Layout.jsx:3 and text-black throughout (Schedule.jsx:19-21,85,99; Team.jsx:47-83; ShiftDetail.jsx:61-116; Settings.jsx:46-87) | Pure black text while the theme defines ink-900/700/500 | Use a dark grey (the unused ink tokens) rather than #000. |
| R13 | src/screens/ShiftDetail.jsx:89-113 (label mb-4 at :89,:103; fields mb-4 at :92,:106,:112...) | Label-to-field gap equals field-to-next-label gap | Ambiguous spacing: labels must sit closer to their own field than to the previous one. |
| R14 | src/components/SideNav.jsx:9 and src/components/Layout.jsx:7 | Sidebar is w-[18%], content w-[82%] | Sidebar should be a fixed width; do not scale it with the viewport. |
| R15 | src/components/Layout.jsx:7; src/screens/Settings.jsx:46 (w-full fields), :76-82; src/screens/Schedule.jsx:23 | Content area has no max-width: settings inputs and paragraphs stretch the full width | Constrain forms and prose with max-w; do not fill the screen just because it is there. |
| R16 | src/screens/Team.jsx:40,47,60-88; src/screens/Schedule.jsx:84,94,111,113; src/screens/Settings.jsx:60,74,85 | Borders on every cell, and bordered rows inside bordered boxes | Too many borders; separate with spacing, background shade or a single row divider instead. |
| R17 | src/screens/Schedule.jsx:31 (rounded-full), :34 (rounded-none), :37 (rounded-2xl), :40 (rounded); cards :84 rounded-none vs :111 rounded-2xl; Team.jsx:35 rounded-2xl vs :89 rounded; Settings.jsx:95 rounded-none; ShiftDetail.jsx:135 rounded-full | Button and card radii mixed at random; theme radius "card" unused on these | Pick one radius language and apply it consistently. |
| R18 | src/screens/Schedule.jsx:84 shadow-[3px_3px_0_#999], :111 and src/screens/ShiftDetail.jsx:71 shadow-[0_-4px_12px_rgba(0,0,0,0.25)], src/components/TopBar.jsx:15 | Arbitrary shadows, one hard offset, one cast upward; theme shadow "card"/"pop" ignored | Light comes from above: shadows go down; define a small elevation scale and reuse it. |
| R19 | src/screens/Settings.jsx:76-82 | Five-line paragraph set text-center | Long text should be left-aligned; centre only a line or two. |
| R20 | src/screens/Team.jsx:68,71,74,77,80 (and header :47) | Numeric columns (count, hours, contracted, rate, cost) left-aligned, no tabular figures | Right-align numbers so magnitudes line up. |
| R21 | src/screens/Team.jsx:47 (15px uppercase black), src/screens/Settings.jsx:61,75, src/screens/Schedule.jsx:66,70,74, src/components/SideNav.jsx:10,29 | Uppercase labels without letter-spacing | Uppercase text needs tracking-wide (and usually a smaller size). |
| R22 | src/components/Layout.jsx:3 (min-w-[1240px]), src/screens/Team.jsx:40 (w-[1100px], row actions fall off a 1280 screen), src/screens/ShiftDetail.jsx:61 (w-[37%]), src/components/WeekGrid.jsx:21 (grid-cols-7 only - acceptable on desktop but no fallback); no sm:/md:/lg: variant anywhere in src | Not responsive: fixed/min widths, horizontal scroll, zero breakpoint variants | Add responsive variants; collapse the sidebar and stack/scroll the table on small screens. |
| R23 | tailwind.config.js:6-13,15-22,35-44 vs src/components/TopBar.jsx:15 and Schedule.jsx:31,134, ShiftDetail.jsx:135, Settings.jsx:95 (bg-[#2f6fed]); Schedule.jsx:34 bg-indigo-600; Team.jsx:35,89 bg-blue-600 | Theme tokens (brand, ink, danger, ok, radius card, shadow card/pop, spacing 18) exist but most screens bypass them with hexes and three different blues | Use the defined design tokens consistently instead of ad-hoc hexes and palette blues. |


## D - Decoys (correct; must NOT be flagged)

| id | file:line | what it is | why it is fine |
|----|-----------|-----------|----------------|
| D1 | src/components/WeekGrid.jsx:1-52 (rendered at src/screens/Schedule.jsx:80) | Deliberately dense 7-column week grid with text-xs cells | A schedule grid is a data-dense tool view; density is appropriate. Cells are real links with focus-visible rings, open shifts say "Open - unassigned" in text plus dashed border (not colour alone), today is labelled in text, theme tokens are used. Flagging "text too small / too dense / needs whitespace" is a false positive. (Its lack of a small-screen fallback is covered by R22 only.) |
| D2 | src/screens/Settings.jsx:99-151 | Danger zone: "Archive this location..." | Correctly demoted (outline, red text, not solid), separated by space and a divider at the bottom of the page, explains consequences and recoverability, requires typing the location name before the solid red confirm button enables, offers "Keep location", has labels and focus rings. Contrast with K15/R6 on the shift form. |
| D3 | src/screens/Team.jsx:21-33 | Staff search | Visible label tied via htmlFor/id, type=search, placeholder only as a hint, visible focus ring, sensible fixed width. (The missing page title next to it is K3, not a problem with the search.) |
| D4 | src/screens/Team.jsx:105-118 | "Time off requests" empty state | Says what is empty, explains what will appear and why it matters, offers one clear primary action, no useless filters, uses a real h2 and section. Contrast with K10. |
| D5 | tailwind.config.js:23-34 and index.html:30-41; applied via font-sans at src/components/Layout.jsx:3 | System font stack | A system UI stack is a legitimate choice for an in-app tool; "no custom/brand font" is a false positive. (font-light on the same line is R11 and is a flaw.) |

## Things a tester may legitimately find that were not planted (neutral, do not penalise)
- Sidebar "Locations" entries do nothing when clicked (SideNav.jsx:30-36).
- Shift detail page has no breadcrumb/back link other than Cancel.
- Settings "OK" gives no success feedback.
- Add slot / Copy last week / Export / Publish week / row buttons have no handlers (fixture is static).
