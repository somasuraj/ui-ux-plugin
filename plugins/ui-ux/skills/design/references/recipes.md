# Recipes (concrete values and component anatomies)
Worked numbers and build-ready structures that implement the rules in `visual-rules.md` (cited as VRn.n).
Loaded for create/refactor only. Principles: visual-rules.md. Scales and palette: design-tokens.md.

Raw colors are the book's samples: use the project's equivalent token. [RUI pNN] = from the book; [ext] = estimated or added.

## 1. Button pyramid by background (VR1.9)

| Background | Primary | Secondary | Tertiary |
|---|---|---|---|
| White | `--action-solid` fill, white text | white fill, brand border and text | brand text, underlined, no box |
| Dark | bright accent solid fill | transparent, mid-grey outline, white text | bare white text |
| Colored / gradient | white fill, brand-colored text | translucent white fill (about `hsl(0 0% 100% / .2)` [ext]), white text, no border | bare white text |

[RUI p61]
- Destructive: primary = solid red, white text; secondary = white button, subtle border, red text; tertiary = plain grey or link-colored text, no red [RUI p62].
- Placement: non-primary delete sits at the far end of the action row [RUI p61].
- Confirm dialog: title, one consequence sentence, tinted footer strip with right-aligned actions: Cancel as bare text, destructive button last [RUI p62].
- Confirm button: solid red, or dark red on a red tint (`--danger-800` on `--danger-100` [ext]) with a red top accent border and icon [RUI p62, p146].

## 2. Text colors and hierarchy (VR1.2, VR1.3, VR1.5, VR1.8)

- Three text colors on a white card: dark `hsl(202 57% 15%)`, grey `hsl(201 23% 34%)`, light grey `hsl(203 15% 47%)`. Lightest stays under 50% lightness [RUI p40].
- Worked card: title 24/700, price 18/700, body 16 to 18/400, fine print demoted by color. Spread 16 to 24px (was 14 to 30, all 400) [RUI p38-40].
- Muted text on a teal panel. Good: `hsl(183 70% 84%)` (panel hue, saturation kept high). Bad: `hsl(0 0% 78%)` and `hsl(0 0% 100% / .6)` (pattern bleeds through glyphs) [RUI p42-44].
- Icon beside text: text `hsl(212 20% 13%)`, icon `hsl(212 20% 68%)`: same hue and saturation, 55 lightness points lighter [RUI p57].
- Dividers: `1px solid hsl(206 16% 74%)` is noisy; `1px solid hsl(210 23% 95%)` vanishes; `2px solid hsl(210 23% 95%)` balances [RUI p58-59].

## 3. Data display patterns (VR1.6, VR1.7, VR1.9)

- Stat block: label above, `--text-xs`, uppercase, `--tracking-caps`, grey; value large, bold (or light on a solid panel); unit smaller than the number ("82 BPM"); optional small delta beneath. Never a bold label over a plain value [RUI p37, p51].
- Number + unit: bold number, regular unit ("12 left in stock"); a small outline icon may replace the label [RUI p49-50].
- Contact card, no labels: name largest and dark; role in accent color; email and phone small grey [RUI p49].
- Spec sheet: category bold at left; each right-hand line = bold dark label + regular value one step lighter (`--text-secondary`) [RUI p51].
- Merged table cell: bold primary (ticker, name, amount) over a smaller grey second line (long name, role, percent). Headers small uppercase grey [RUI p37, p244].
- Status pill: `--x-800` text on `--x-100`, always with a word [RUI p245].
- Per-row actions: quiet outline buttons or text links, never solid fills [RUI p37].
- App page title: 16px, not 24px; may be smaller than a card's section title [RUI p54-55].

## 4. Spacing worked numbers (VR2.1, VR2.3, VR2.4)

| Case | Inside | Outside | Bad |
|---|---|---|---|
| Label to input / input to next label | 10px | 20px | 20/20 |
| Heading: below / above | 12px | 36px | 24/24 |
| List: line box / between items | 24px | 36px | 24/24 |
| Icon to count / pair to pair | 6px | 36px | 16/16 |

[RUI p97-99]. Snap to the spacing scale in real work.
- One card = two values: nine drifting gaps (26, 24, 15, 21, 13...) become 24px (padding on all sides, around the section divider) and 12px (between related lines) [RUI p70, p74].
- Card padding about 2x the cramped version; tighten inside lists, stay generous around the card and before the CTA [RUI p66-68].

## 5. Layout patterns (VR2.5, VR2.7)

- Narrow column: full-width nav or hero band; content in one centered column near its 400px mobile width, so name and price stay together [RUI p76-79].
- Settings form: one row per section, thin rule between; narrow left = section title + muted help text; right = fields at ideal width [RUI p80-81].
- Sidebar + main: fixed-width sidebar, flexing main with its own grid; cards go 4-up to 2-up. [RUI p85-87].
- Login card: `max-width: 500px`; no per-breakpoint column spans [RUI p88-90].

## 6. Depth recipes (VR5.1 to VR5.6)

```css
/* raised: highlight = opaque lighter tint of the fill, picked per color [RUI p176] */
.btn-raised { box-shadow: inset 0 1px 0 hsl(224 84% 74%), var(--shadow-1); }
/* inset well, input, checkbox; fill darker than the panel around it [RUI p177-178] */
.well { box-shadow: inset 0 2px 2px hsl(0 0% 0% / .1), inset 0 -2px 0 hsl(0 0% 100% / .15); }
/* flat: zero blur, opaque grey a little darker than the page [RUI p192] */
.card-flat { box-shadow: 0 3px 0 hsl(220 7% 83%); }
```

- Pressed: `--shadow-2` drops to `--shadow-1` (or none), fill one shade darker [RUI p183-184].
- Dragged row: white raised background + shadow, handle at left, slightly wider than siblings [RUI p184].
- Overlap: card straddling two sections `margin-bottom: -60px`; card taller than its band `margin: -60px 0`; round carousel buttons on card edges `margin-left/right: -24px` (half their width) [RUI p194-195].
- Overlapping avatars, or avatar on a cover photo: `border: 4px solid` in the surface color [RUI p196].
- Book misprints, do not copy: shadow alpha `.7` (p186, p252), `letter-spacing: 0.8rem` (p252), p177 caption lacks `inset`.

## 7. Text over images (VR6.2)

```css
.hero::before { content: ""; position: absolute; inset: 0; background: hsl(0 0% 0% / .55); } /* [RUI p204] */
.hero-img--pale { filter: brightness(1.4) contrast(.3); } /* + dark text [RUI p204] */
.hero h1 { text-shadow: 0 0 50px hsl(0 0% 0% / .4); }     /* glow, no offset [RUI p206] */
```

- Overlay opposes the text: dark under light text, light under dark [RUI p204].
- Colorize in order: lower contrast, desaturate, multiply a solid fill (`#035581`, `mix-blend-mode: multiply`) [RUI p205].
- Test: check contrast at the brightest and the darkest region the text crosses [RUI p203].

## 8. Images (VR6.3, VR6.4)

```css
.thumb::after { content: ""; position: absolute; inset: 0; border-radius: inherit;
  box-shadow: inset 0 0 0 1px hsl(0 0% 0% / .1); } /* [RUI p217] */
```

- Uploads: fixed-ratio box, `object-fit: cover`, centered, so grid rows stay even [RUI p215].

- Rejected: `border: 2px solid hsl(212 12% 72%)`; opaque rings clash with photos [RUI p216].
- Small icon, big slot: 24px glyph centered in a 48px circle filled `--x-100`, icon a darker shade of that hue. Or use a large-format icon set [RUI p209].
- Screenshots (a 70% shrink makes 16px text about 4px): capture at tablet width, crop to a region, or draw a simplified version [RUI p210-212].
- Favicon: redraw with fewer, thicker strokes [RUI p213].

## 9. Borders replaced (VR7.1)

- Shadow instead of a panel border: only when the panel fill differs from the page; dialog sample is `--shadow-3` at alpha .15 [RUI p239].
- Header, search, footer strips: `background-color: hsl(200 10% 94%)` on white, borders deleted. Fill plus border: drop the border [RUI p240].
- List rows: no dividers, `margin-bottom: 6px` (8px on-scale [ext]); selected row = inset rounded rectangle, not a full-bleed band [RUI p241].

## 10. Finishing touches (VR7.2, VR7.3, VR7.4)

Accent borders (positions [RUI p224-226]; sizes estimated [ext]):
- Card: 4px top band, clipped by the radius.
- Active nav: 2px bar, label width, on the nav's bottom edge.
- Alert: 3 to 4px left bar, darker shade of the panel tint.
- Headline: left-aligned 40 to 60px bar between headline and body.
- Page: full-width top band.

Defaults upgraded [RUI p220-222]:
- Bullets: filled brand check icons, or a topic icon in a muted round chip.
- Quotes: enlarged light-tint marks, opening mark hung in the margin.
- Links: brand color + heavier weight, no underline; or body-colored text with a thick tinted underline overlapping the letter bottoms.
- Checkboxes and radios: larger than default, brand color when checked (`accent-color` [ext]).

Backgrounds [RUI p228-232]:
- Color swap on one card: solid brand body, white and light same-hue text, footer strip flipped to white.
- Alternate section fills (brand, white, near-black, grey); pattern along one edge or in a corner; a very low-contrast dotted map behind centered content.

## 11. Component anatomies (VR7.5, VR7.6)

- Empty state, simple: centered illustration, one action-phrased line, one primary button [RUI p235].
- Empty state, full page: remove toolbar create button, tabs, filter, search; show headline, one sentence, one primary button, large low-contrast illustration bleeding off the right [RUI p236].
- Rich dropdown: wide panel with a caret to its trigger, `--shadow-2`; primary items in a two-column grid (colored outline icon + bold title + one-line muted description, optional NEW pill); secondary links in a tinted section, one per row, description inline [RUI p243].
- Enriched table: stacked cells and pills per section 3 (six columns become four), avatar in the first cell; merge only columns that need no sorting [RUI p244-245].
- Selectable cards: equal-width row; each = stat block (section 3) + price beneath. Selected = brand border + faint brand tint + check badge top right; unselected = white card, `--shadow-1` [RUI p246]. Keep a real radio input inside [ext].

## 12. Hue rotation and gradients (VR4.3)

- Lighten without washing out: `hsl(210 100% 50%)` to `hsl(190 100% 50%)`, S and L untouched; the washed-out alternative is `hsl(210 100% 75%)`. [RUI p155]. The pair also works as a two-stop gradient [ext].
- Darken yellow: `hsl(50 100% 50%)` to `hsl(32 100% 50%)`; holding the hue gives olive [RUI p156].
- Hue plus lightness: panel `hsl(221 49% 33%)`, accent text `hsl(194 49% 73%)`: 27 degrees, same S, +40 L [RUI p156].
