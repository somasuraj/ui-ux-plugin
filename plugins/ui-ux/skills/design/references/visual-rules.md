# Visual rules (auditable)

What makes an interface look deliberately designed. Distilled in our own words from *Refactoring UI* (Wathan & Schoger). Everything is [RUI] unless tagged [ext] (this skill's addition). Section numbers are cited by the audit checklist as `VR n`. Concrete CSS values and component anatomies live in `recipes.md`; scales and palette in `design-tokens.md`.

Core idea: "looks good" comes mostly from **hierarchy, spacing, and constrained systems**, not decoration.

## VR1 Hierarchy

1. **Rank everything.** Each screen has a primary element, secondary content, tertiary content, and the styling says which is which. When everything competes, it reads as noise.
2. **Size is not the only lever.** Shrink the primary element a little and make it bold; bring secondary text back up to a readable size and demote it with color. A healthy component spans roughly 1.5 to 2x between its largest and smallest text (e.g. 16 to 24px), not 14 to 30px.
3. **About three text colors and two weights.** Dark, grey, lighter grey; normal (400/500) and heavy (600/700). No weight under 400 in UI: de-emphasize with color or size instead. Tertiary text is still not pale (around 45 to 50% lightness on white).
4. **Emphasize by de-emphasizing.** If the main thing doesn't stand out, quiet its competitors. Active nav item not popping: make inactive items soft grey. Sidebar competing with content: take away its card/background so only the main content is a raised surface.
5. **No grey text on colored backgrounds.** Grey on white works because it lowers contrast. On color, use the same hue as the background, lighter, with saturation kept up. Not neutral grey, and not white at reduced opacity (looks disabled; the background bleeds through over images or patterns).
6. **Labels are a last resort** (for displaying data, not form inputs):
   - Drop the label when format or context explains the value (an email, a phone number, a price, a job title under a name).
   - Fold the label into the value, bold number plus regular unit: "**12** left in stock", "**3** bedrooms". An icon can stand in for a label.
   - When needed, the label is secondary: smaller, lighter, often small tracked uppercase above a large bold value whose unit is set smaller.
   - Spec-sheet pages where people scan for the label: emphasize the label, keep the value only one step lighter.
7. **Visual hierarchy is not document hierarchy.** Choose tags for semantics, style for hierarchy. App page titles are often modest (16 to 20px is normal in app chrome); section titles act like labels and should not overpower content. A section title can stay in the markup and be visually hidden when the content explains itself.
8. **Balance weight and contrast.** Heavy things (solid icons) next to text get a softer color: same hue as the text, far lighter. Faint things that need presence get weight, not darkness: a 2px very light rule beats a 1px darker one.
9. **Actions follow a pyramid, not semantics.**
   - Primary: solid, high contrast. Normally one per screen.
   - Secondary: outline or low-contrast fill. Tertiary: styled like a link.
   - On dark or colored backgrounds the pyramid adapts (see `recipes.md`): primary is a bright or inverted white fill, secondary an outline or translucent fill, tertiary bare text.
   - **Repeated per-row actions are never primary.** Solid or semantic-colored buttons down every table row make a wall of color.
   - **Destructive is not automatically big and red.** If it isn't the primary action, give it secondary (red text on white) or tertiary (plain grey or link-colored text) treatment and place it away from the primary action. The loud red treatment belongs in the confirmation step, where deleting *is* the primary action (solid red, or dark red on a red tint).

## VR2 Layout and spacing

1. **Start with too much whitespace, then remove.** Adding space until it stops looking bad yields the minimum, not the good amount. Judge in the context of the full screen, not element by element. Card padding should be comfortably larger than the gaps between the card's own items.
2. **Density is a decision.** Dashboards and data tables may be compact on purpose: achieve it with small labels over bold values and thin row dividers, not by shrinking all padding uniformly. Don't flag deliberate density in a data table as a flaw; flag it when readability or targets suffer.
3. **Use a spacing/sizing scale** (`design-tokens.md`). One-off values (13, 17, 22) and "multiples of 4" are not a system. A component should resolve to 2 to 3 spacing values with symmetric padding.
4. **No ambiguous spacing.** Where nothing but space groups things, the gap around a group must be at least about 2x the gap inside it; equal gaps are a fail. Label-to-input tighter than field-to-field; more space above a heading than below; list items further apart than their own line gap; the same horizontally (icon-to-count vs pair-to-pair). Groups with a visible separator (border, background) are exempt.
5. **Don't fill the screen because it's there.** Give content the width it needs. Stretching pulls related things apart (item name far left, price far right). A full-width nav above a narrow centered column is fine. To use spare width, split into columns (settings: section title plus help text on the left, fields at their ideal width on the right) instead of stretching inputs.
6. **Design small first.** Start near 400px wide, then expand and fix only what felt compromised.
7. **Grids are a tool.** Fixed widths for things with a natural size (sidebars, avatars, media in cards); the main area flexes. Use `max-width` and shrink only when the viewport forces it. Symptoms of grid-worship: a percent-width sidebar that wastes space when wide and wraps labels when narrow; an element that is wider at a medium breakpoint than at a large one. Card grids reflow by changing column count, not by stretching.
8. **Relative sizing doesn't scale.** Large things must shrink faster than small things on small screens. Buttons aren't a zoom: big ones get proportionally more padding, small ones tighter. Don't tie padding or headline size to the base font with em.

## VR3 Text

1. **A constrained type scale** in px or rem. No em for sizes that can nest (1.25em x 0.875em = 17.5px, off scale). Ratio-based scales give fractional values and too few UI sizes; hand-pick.
2. **Fonts.** Neutral sans or the system stack is the safe default. Filters: 5+ weights (10+ styles), no condensed or short-x-height face for body UI, sort by popularity, inspect what well-made sites use.
3. **Line length 45 to 75 characters**, including paragraphs inside a wider layout.
4. **Baseline-align mixed sizes** on one line (`align-items: baseline`), most visible when the texts sit close together.
5. **Line-height is proportional**: more for small text and wide columns, less for large text.
6. **Links.** In prose, links keep color and underline. In link-dense UI (lists, grids, nav) use weight or a darker color instead of blanket link-blue; ancillary links may reveal underline or color on hover only.
7. **Alignment.** Left-align by default. Center only short blocks (2 to 3 lines), and sibling centered blocks should wrap to the same line count: shorten the copy. Right-align numeric columns **and their headers** so decimals stack. Justified text needs `hyphens: auto`.
8. **Letter-spacing.** Leave alone by default; tighten big headlines set in a wide text face; widen all-caps. Never widen a display face to make it work small.

## VR4 Color

1. **Work in HSL**, and build a real palette: 8 to 10 greys, 1 to 2 primaries with 5 to 10 shades, semantic colors (danger, warning, success) with shades, plus separate categorical accents if the UI color-codes series, tags, or events. A modest UI easily needs 15+ swatches. No true black.
2. **Define shades up front**; never `lighten()`/`darken()` on the fly, and resist adding shades later.
3. **Keep saturation alive at the extremes**, and use **hue rotation** to change brightness without washing out (details in `design-tokens.md`).
4. **Greys have a temperature**; keep it consistent across the scale.
5. **Accessible without ugly.** 4.5:1 normal text, 3:1 large text. White on a colored fill needs a surprisingly dark color, which then hogs attention: flip the contrast (dark text on a light tint). For colored text on a colored panel that must pass, rotate hue toward a bright hue rather than drifting to white.
6. **Never rely on color alone.** Metrics and statuses carry an icon, sign, or word. Charts stay distinguishable in greyscale: vary lightness, not just hue. Check also that red/green actually matches good/bad for that metric [ext].

## VR5 Depth

1. **Light comes from above.** Raised: slightly lighter top edge (an opaque lighter tint of the element's own color) plus a small, tight shadow below. Inset (wells, inputs, checkboxes): dark inset shadow at the top plus a lighter bottom lip. Never mix raised and inset cues on one element; don't chase photo-realism.
2. **Shadows express elevation** on a small fixed scale matched to z-position: button < dropdown < panel/dialog < modal. A floating layer with only a 1px border and no shadow looks flat.
3. **Shadows respond to interaction.** A pressed button's shadow shrinks (or disappears); a dragged item gains a raised background and a shadow.
4. **Two-part shadows**: a big soft one keeps things subtle while a tight dark one keeps the edge defined; the tight part fades with height.
5. **Flat designs still need depth**: lighter than the background reads as raised, darker as inset; short solid shadows with zero blur in an opaque tint of the background.
6. **Overlap to create layers**: elements straddling two backgrounds, controls centered on a card edge; overlapping images get a border in the surface color.
7. One consistent light direction across the product [ext: a shadow offset upward or sideways contradicts the rest].

## VR6 Images

1. **Use good photos.** Professional or quality stock; don't design around placeholders.
2. **Text over an image needs consistent contrast across the whole text box**: overlay (dark under light text, light under dark text), lowered image contrast with brightness compensated, colorize (lower contrast, desaturate, multiply a solid fill), or a soft glow text-shadow (large blur, no offset).
3. **Everything has an intended size.** Don't scale small icons past about 2x: put them at native size inside a tinted shape, or use a large-format set. Don't shrink full screenshots until text is unreadable: capture at a smaller viewport, crop, or draw a simplified version. Redraw logos for favicon size.
4. **User-uploaded images**: fixed-ratio container, cover-cropped and centered, so rows stay even. Stop light images bleeding into the page with a subtle translucent inner edge, not a solid colored border.

## VR7 Borders and finishing touches

1. **Fewer borders.** Separate with spacing, a different background, or a shadow first. A shadow can replace a border only when the element's fill differs from its background. If a region has its own fill *and* a border, the border is redundant. List rows: spacing or fill before rules.
2. **Supercharge defaults**: icons for bullets, oversized tinted quote marks, custom link underlines, brand-colored checkboxes and radios.
3. **Accent borders** in a small set of places: top of a card, under the active nav item, left edge of an alert, a short bar under a headline, top of the page. One color and thickness per position.
4. **Decorate backgrounds** sparingly: a section color change, a gentle gradient (hues within about 30 degrees), a low-contrast pattern or shape. Never at the cost of text contrast.
5. **Design empty states**: what to do (not "nothing found"), exactly one primary call to action, optional illustration, and hide chrome that needs data (tabs, filters, sort, search) rather than disabling it.
6. **Think outside the box**: dropdowns can have columns, icons, and descriptions; non-sortable table columns can merge into stacked cells; statuses can be tinted pills; a radio group that is the main decision on the screen can be selectable cards.
7. **Consistency of personality**: one radius family, one button shape, one tone of voice (see `design-process.md`).
