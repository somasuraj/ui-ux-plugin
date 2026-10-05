# Seeing and measuring

How to look at the real UI and produce numbers instead of guesses. All scripts are standard-library Python in `<skill-dir>/scripts/` (the skill's base directory is given when the skill loads; `${CLAUDE_SKILL_DIR}` in SKILL.md). Use `python` or `python3`, whichever exists.

## 1. Render it

Code hides spacing, hierarchy, and contrast problems. Look at pixels whenever you can.

```
python <skill-dir>/scripts/screenshot.py index.html settings.html --mobile --out <scratch>/shots
python <skill-dir>/scripts/screenshot.py "http://localhost:5173/invoices?state=empty" --out <scratch>/shots
```

- Works on **local files directly** (no server) and on URLs; finds Chrome, Edge, or Chromium; default viewport 1280x1400 (`--width`, `--height`); `--mobile` adds a true 400px-wide layout (rendered in an exact-width frame, so the grey strip on the right of that image is outside the viewport, not part of the page); `--full` uses a tall viewport. Then open the PNGs with the Read tool.
- Browser-automation tools (the Chrome extension) usually **refuse `file://`**. Don't burn calls on it: use the script. For a framework or single-page app, start its dev server the way the project documents (check its README), screenshot each route by URL (hash routes work: `http://localhost:PORT/#/settings`), then stop the server you started.
- Client-rendered apps (React, Vue, in-browser Babel, CDN Tailwind) need time to render: the script waits 10 s of virtual time by default (`--wait MS`). It prints **BLANK** instead of OK when an image is one flat color; a blank screenshot is not evidence of anything, so fix the capture (serve over http, raise `--wait`) rather than auditing from it.
- Hash and query routes each get their own file name (`#/shift/12` becomes `shift-12.png`, `?state=empty` becomes `...-state-empty.png`).
- Write screenshots to a scratch/temp directory, not into the project.
- Capture each state you can reach by URL (query params, routes). For states you can't reach, read the component code and say so.
- No browser available: ask the user for screenshots, continue code-only, and list "not rendered" under Not verified.
- **Screenshots are the most expensive thing you read**: each image stays in context for the rest of the task. Read each PNG once and note what you saw; don't re-open it. Shoot before and after for what changed, not every screen again after each edit. Prefer the default viewport over `--full` unless the problem is below the fold. Anything countable (sizes, colors, contrast ratios, label counts) comes from `scan.py` and `contrast.py`, not from looking.

Views worth taking: each key screen at desktop width, the same at 400px, the empty state, an error state, a long-content case.

## 2. Squint, grey, and resize tests

- **Squint / blur (trunk test and hierarchy):** look at the screenshot small or from arm's length. Can you still point to identity, screen name, sections, local nav, current location, search? Does one primary element stand out?
- **Greyscale:** does the primary action, the selected state, and the hierarchy still read without color? If color is doing all the work, hierarchy is weak and color-blind users lose meaning.
- **Text-size bump:** with the browser's text size or zoom raised, does text grow and the layout hold? (In code: font sizes in px on the root with fixed-height containers are the usual culprits.)

## 3. Contrast and brightness

```
python <skill-dir>/scripts/contrast.py "#9a9a9a" "#2456c9"              -> 2.30:1 FAILS
python <skill-dir>/scripts/contrast.py "rgba(255,255,255,.45)" "#2456c9"  (translucent text is composited first)
python <skill-dir>/scripts/contrast.py "#1fa34a" white --size 15          (give the font size for a definite pass/fail)
python <skill-dir>/scripts/contrast.py --pb "hsl(60 100% 50%)" "hsl(240 100% 50%)"
```

- Thresholds: **4.5:1** normal text; **3:1** large text (24px regular, or about 18.7px bold) and UI boundaries such as input borders, icons, focus rings.
- Measure every text/background pair that isn't plain dark-on-white, every solid button label, badges, placeholder and helper text, text on tinted panels, disabled-looking controls.
- Not being able to render is not a reason to skip this: the colors are in the code.
- By hand if needed: relative luminance L = 0.2126 R + 0.7152 G + 0.0722 B with each channel linearized (c/12.92 if c <= 0.03928, else ((c+0.055)/1.055)^2.4); ratio = (L1 + 0.05) / (L2 + 0.05).
- Perceived brightness (`--pb`) explains why equal HSL lightness doesn't look equally light and guides hue rotation when building shades.

## 4. Enumerate the system

```
python <skill-dir>/scripts/scan.py <ui source dir>
```

Gives distinct font sizes, weights, line-heights, colors (hex normalized, greys counted), spacing values, shadows, radii, border count, token count, media-query count, and how many declarations use `var()` versus raw values. Counting rules if you must do it by hand: normalize hex case and shorthand (`#fff` = `#ffffff`); count rgba/hsla with alpha as separate colors; count em/% font sizes and note their computed px when nested; ignore `0`, `auto`, `inherit`, `transparent`.

Reading the numbers: more than about 8 to 10 font sizes, several near-neighbour sizes or spacings (13/14/15, 6/7/8/9), many unrelated greys, more than one radius family, no tokens, or no media queries each point to a missing system. In a token-based project judge the token definitions, and treat remaining raw values as leftovers to fold in.

The scan also lists **candidates** with `file:line` (non-interactive click targets, missing alt/labels/landmarks, low-contrast pairs, em sizes, light weights, pure black, uppercase without tracking, centered text, percent-width sidebars, shadows not lit from above, reset buttons, rigid patterns, long forms). They are leads, not findings: confirm each in the code, drop the ones that are fine, and add severity yourself. Contrast pairs marked "ASSUMED page background" must be checked against the element's real background before reporting. For JSX/TSX/Vue/Svelte it checks the same markup patterns. In a **utility-class (Tailwind-style) codebase** the values live in class names, so the scan adds a utility-class pass: distinct text sizes, weights, colors (palette names and arbitrary hexes), spacing values, radius families, shadows, a summary of arbitrary one-off values (`p-[13px]`), responsive/hover/focus variant counts, and candidates such as `outline-none` with no focus replacement, translucent white text, `font-light`, `text-black`, uppercase without `tracking-*`, percent-width sidebars, big fixed pixel widths, screens with no `<h1>`, and several solid buttons in one screen. Also read the Tailwind config: a theme that defines tokens the components bypass with raw hexes is a finding.

## 5. Fidelity after a refactor

```
python <skill-dir>/scripts/check_refactor.py --before <snapshot of the original> --after <ui dir>
```

Lists navigation labels that disappeared, data values that changed or vanished (dates and amounts are matched by value, so reformatting is fine), new controls that lead nowhere, new navigation entries, and new marketing claims. A redesign that replaces the product's real navigation, tidies the sample data, or adds buttons for functions that do not exist has built a different app. Each item is reverted or handed to the owner as a question. Take the snapshot before the first edit.

## 6. What measuring can't tell you

Whether the words are obvious, whether navigation makes sense, whether the right thing is primary, whether density is deliberate, whether anyone can actually complete the task. That is what the checklist, your judgment, and ultimately a usability test are for.
