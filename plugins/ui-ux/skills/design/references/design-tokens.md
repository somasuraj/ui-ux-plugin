# Design tokens (starter systems)

Drop-in scales that implement "limit your choices". **If the project already has tokens** (theme file, CSS variables, Tailwind config, component library), use and extend those; never add a parallel system. When introducing tokens, **adopt only the ones you actually use** and name them in the project's style. Don't paste this whole file into a project.

Tags: [RUI] = value taken from *Refactoring UI*; [ext] = this skill's own addition. Every contrast figure here was computed with `scripts/contrast.py`.

## Spacing and sizing scale [RUI]

Base 16px, as multipliers (use these when the base is not 16): 0.25, 0.5, 0.75, 1, 1.5, 2, 3, 4, 6, 8, 12, 16, 24, 32, 40, 48.

`4, 8, 12, 16, 24, 32, 48, 64, 96, 128, 192, 256, 384, 512, 640, 768`

- Neighbours differ by roughly 25% or more (slightly looser at the very top; don't "fix" it). A plain "everything is a multiple of 4" rule is not a system: it still leaves 120 vs 124 vs 128.
- Why non-linear: 12 to 16px is a 33% jump and clearly visible; 500 to 520px is 4% and invisible.
- Need more room? Go up one step. A single component should resolve to 2 to 3 spacing values with symmetric container padding.
- Inside vs outside a group: pick values at least one step apart, ideally two (outside gap at least 2x the inside gap).

## Type scale [RUI]

`12, 14, 16, 18, 20, 24, 30, 36, 48, 60, 72` in px or rem, never em. (The book also shows a shorter 12, 14, 16, 18, 20, 24, 32, 48; any hand-picked scale is fine.) A single component should land on about 3 to 4 sizes; near-neighbours like 13/14/15 are the smell.

- Weights: 400 (or 500) normal, 600 to 700 emphasis. Check the font really has the weight you name (Segoe UI has no 500).
- Line-height [RUI]: body about 1.5; small text or wide columns up to 1.75 to 2; large headlines about 1 (up to ~1.2 when multi-line). 1.25 on small body text and 1.5 on a big headline are both wrong.
- Measure: `max-width: 65ch` for paragraphs (45 to 75 characters); a centered intro under a wide section about `34em`.
- Letter-spacing [RUI]: `-0.05em` at most for large headlines set in a text family, `0.05em` for all-caps. Never widen a display/condensed face to make it work small.
- Responsive [RUI]: headline is about 2.5x body on desktop (45/18) but only about 1.5 to 1.7x on phones (20 to 24 over 14). Set sizes per breakpoint; don't derive headlines from body with em.

## Button sizes [RUI]

Padding is tuned per size, not proportional. Larger buttons get relatively more horizontal padding; small ones get tighter.

| Size | Font | Padding (y x) |
|---|---|---|
| xs | 12px | 6px 8px |
| sm | 14px | 8px 10px |
| md | 16px | 12px 16px |
| lg | 20px | 15px 30px (16px 32px on-scale) |

Minimum touch target about 44px high on touch devices [ext].

## Elevation [RUI]

Pick by z-position, not by taste: **1** buttons and cards, **2** dropdowns and button hover, **3** panels, popovers, inline dialogs, **4 to 5** modals. Alpha can drop for quieter uses (the book's dropdown uses level-2 geometry at .1, a dialog level 3 at .15). Build a scale by fixing the smallest and largest first, then filling between in roughly linear steps.

Two-part shadows: big soft shadow = direct light, tight dark shadow = ambient occlusion. The tight one fades as height grows and is gone at the top level. (`.05` at level 4 is correct; it is not a typo for `.5`.)

## CSS variables

```css
:root {
  /* spacing / sizing */
  --space-1: 4px;   --space-2: 8px;   --space-3: 12px;  --space-4: 16px;
  --space-5: 24px;  --space-6: 32px;  --space-7: 48px;  --space-8: 64px;
  --space-9: 96px;  --space-10: 128px; --space-11: 192px; --space-12: 256px;
  --space-13: 384px; --space-14: 512px; --space-15: 640px; --space-16: 768px;

  /* type */
  --text-xs: 0.75rem;  --text-sm: 0.875rem; --text-base: 1rem;   --text-lg: 1.125rem;
  --text-xl: 1.25rem;  --text-2xl: 1.5rem;  --text-3xl: 1.875rem; --text-4xl: 2.25rem;
  --text-5xl: 3rem;    --text-6xl: 3.75rem; --text-7xl: 4.5rem;
  --weight-normal: 400; --weight-bold: 700;
  --leading-none: 1; --leading-tight: 1.2; --leading-normal: 1.5; --leading-relaxed: 1.75; --leading-loose: 2;
  --measure: 65ch;
  --tracking-tight: -0.025em; /* [ext] softer default; the book's example is -0.05em */
  --tracking-caps: 0.05em;
  --font-sans: system-ui, -apple-system, "Segoe UI", Roboto, "Noto Sans", Ubuntu,
               Cantarell, "Helvetica Neue", sans-serif;

  /* elevation: single shadows [RUI] */
  --shadow-1: 0 1px 3px hsla(0, 0%, 0%, .2);
  --shadow-2: 0 4px 6px hsla(0, 0%, 0%, .2);
  --shadow-3: 0 5px 15px hsla(0, 0%, 0%, .2);
  --shadow-4: 0 10px 24px hsla(0, 0%, 0%, .2);
  --shadow-5: 0 15px 35px hsla(0, 0%, 0%, .2);

  /* elevation: two-part shadows [RUI] */
  --shadow-1-2p: 0 1px 3px hsla(0,0%,0%,.12), 0 1px 2px hsla(0,0%,0%,.24);
  --shadow-2-2p: 0 3px 6px hsla(0,0%,0%,.15), 0 2px 4px hsla(0,0%,0%,.12);
  --shadow-3-2p: 0 10px 20px hsla(0,0%,0%,.15), 0 3px 6px hsla(0,0%,0%,.10);
  --shadow-4-2p: 0 15px 25px hsla(0,0%,0%,.15), 0 5px 10px hsla(0,0%,0%,.05);
  --shadow-5-2p: 0 20px 40px hsla(0,0%,0%,.2);

  /* radius: choose ONE personality and stay consistent (pills/avatars excepted) */
  --radius-none: 0;      /* formal */
  --radius-sm: 4px;      /* neutral */
  --radius-md: 8px;      /* friendly [ext] */
  --radius-lg: 12px;     /* playful */
  --radius-full: 9999px;

  --border-1: 1px; --border-2: 2px; /* a soft 2px rule beats a dark 1px rule */
}
```

## Color palette (HSL), built with the book's method

Method [RUI]: choose **500** by eye as the base (no "start at 50% lightness" rule). Choose **900** (darkest text on a tint) and **100** (tinted background) using an alert component as the test piece. Then 700 and 300, then 800/600/400/200. For greys the base doesn't matter: 900 = darkest body text, 100 = subtle off-white.

Shaping rules [RUI]:
- **Saturation is a U-curve**: raise it as lightness moves away from 50%, steeply (the book's chart runs from about 50% at the base to about 90% at both ends). If the base is already near 100%, use hue rotation instead.
- **Hue rotation**: lighter shades rotate toward the nearest bright hue (60, 180, 300), darker shades toward the nearest dark hue (0, 120, 240); keep total swing within about 20 to 30 degrees. Dark yellows must slide toward orange, or they turn olive.
- **Perceived brightness**, not HSL lightness, tells you whether two colors look equally light: `sqrt(0.299 r^2 + 0.587 g^2 + 0.114 b^2) / 255` (`contrast.py --pb`). Yellow 0.94, cyan 0.84, green 0.77, magenta 0.64, red 0.55, blue 0.34 at full saturation.
- **Greys**: one temperature. Cool = hue about 210, warm = hue about 40; saturation about 12% mid-scale rising to 15 to 20% or more at the ends (real UIs go much heavier on the darkest text, e.g. 40 to 55%).
- Values copied from an HSB picker are wrong in CSS: HSB 100% brightness at full saturation is HSL 50% lightness.

```css
:root {
  /* greys: cool. For warm greys use hue ~40 with the same S/L. */
  --grey-50:  hsl(210 40% 98%);
  --grey-100: hsl(210 36% 96%);
  --grey-200: hsl(212 30% 90%);
  --grey-300: hsl(212 24% 82%);
  --grey-400: hsl(212 18% 66%);  /* 2.5:1 on white: decoration and muted icons only, never text or control borders */
  --grey-500: hsl(212 16% 46%);  /* 4.8:1 on white: lightest grey allowed for normal-size text */
  --grey-600: hsl(212 20% 36%);  /* 7.0:1 */
  --grey-700: hsl(212 26% 27%);
  --grey-800: hsl(212 34% 18%);
  --grey-900: hsl(212 44% 11%);  /* darkest text; never pure black */

  /* primary: lighter toward 180, darker toward 240 */
  --primary-100: hsl(204 95% 94%);
  --primary-200: hsl(205 92% 86%);
  --primary-300: hsl(207 88% 74%);
  --primary-400: hsl(209 84% 62%);
  --primary-500: hsl(211 80% 50%);  /* base. White text on it is only 4.1:1 */
  --primary-600: hsl(213 82% 42%);  /* solid buttons with white text: 5.9:1 */
  --primary-700: hsl(215 84% 34%);  /* links/text on white 8.3:1; on primary-100 7.3:1 */
  --primary-800: hsl(218 86% 26%);
  --primary-900: hsl(221 88% 19%);

  /* danger: red sits on a dark hue, so dark shades need no rotation */
  --danger-100: hsl(4 92% 95%);   --danger-200: hsl(3 88% 88%);  --danger-300: hsl(2 84% 77%);
  --danger-400: hsl(1 78% 64%);   --danger-500: hsl(0 74% 52%);  /* white text 4.7:1 */
  --danger-600: hsl(0 76% 43%);   --danger-700: hsl(0 78% 35%);
  --danger-800: hsl(0 80% 27%);   /* on danger-100: 9.3:1 */
  --danger-900: hsl(0 84% 19%);

  /* warning: darker shades slide toward orange and keep saturation */
  --warning-100: hsl(50 100% 90%); --warning-200: hsl(49 98% 80%); --warning-300: hsl(47 96% 68%);
  --warning-400: hsl(45 94% 58%);  /* solid fill takes DARK text: warning-900 on it is 7.2:1 */
  --warning-500: hsl(42 92% 50%);  /* white text is 1.9:1. Never put white on yellow. */
  --warning-600: hsl(38 94% 42%);  --warning-700: hsl(34 94% 34%);
  --warning-800: hsl(30 94% 26%);  /* on warning-100: 7.1:1 */
  --warning-900: hsl(27 94% 19%);

  /* success: lighter toward 180, darker toward 120 */
  --success-100: hsl(156 76% 92%); --success-200: hsl(154 68% 82%); --success-300: hsl(152 60% 68%);
  --success-400: hsl(150 58% 50%); --success-500: hsl(148 62% 38%);  /* white text only 3.5:1 */
  --success-600: hsl(146 66% 31%); /* solid with white text: 4.8:1 */
  --success-700: hsl(144 70% 25%);
  --success-800: hsl(142 74% 19%); /* on success-100: 8.2:1 */
  --success-900: hsl(140 78% 13%);

  /* roles: components reference these, not raw shades */
  --text-primary: var(--grey-900);
  --text-secondary: var(--grey-600);
  --text-tertiary: var(--grey-500);     /* 4.8:1 on white, 4.6:1 on the page surface: the floor */
  --icon-muted: var(--grey-400);        /* icons beside text: same hue as the text, much lighter */
  --surface-page: var(--grey-50);
  --surface-raised: #fff;
  --surface-inset: var(--grey-100);
  --border-subtle: var(--grey-200);     /* dividers: prefer 2px of this over 1px of something darker */
  --border-control: hsl(212 16% 54%);   /* input/checkbox borders need 3:1 [ext]; this is 3.6:1 */
  --focus-ring: var(--primary-500);     /* 4.1:1 on white, fine for a non-text indicator */
  --action-solid: var(--primary-600);
}
```

## Usage rules

- **Do not assume a "500" passes with white text.** Measure every solid button (`scripts/contrast.py`). In this palette: primary and success use 600, danger 500 or darker, warning takes dark text.
- **Badges, pills, alerts: flip the contrast** [RUI]. `--x-800` text on `--x-100`. White on a mid-tone saturated pill typically measures 1.6 to 3.1:1 (far off, not slightly off); darkening the fill until white passes makes the pill the loudest thing in the row; dark-on-tint lands around 9:1 and stays quiet.
- **Muted text on a colored panel**, two cases [RUI]:
  - Just de-emphasizing: same hue as the panel, lighter, saturation kept **high** (teal panel: `hsl(183 70% 84%)`). Never neutral grey, never white at reduced opacity.
  - Must also clear 4.5:1 on a dark panel, where same-hue text ends up looking white: rotate the hue toward a bright hue and raise saturation (panel `hsl(240 34% 34%)`: `hsl(188 100% 85%)` reads as color at 8.7:1).
- **Grey text on white**: lightness at or below about 45% for normal text, about 55% for large text (grey L54% is 3.45:1, L42% is 5.41:1).
- Large text for the 3:1 allowance means **24px regular or about 18.7px bold** (WCAG). The book's looser "about 18px" will pass things WCAG fails [ext].
- Gradients: two hues no more than about 30 degrees apart; rotating hue makes a livelier gradient than changing lightness.
- Charts and categories: add separate categorical accents; for colorblind safety prefer one hue at 3 well-separated lightness steps over several hues.
- Dark mode [ext]: redefine the role variables; raised surfaces get lighter, not more shadowed.

## Tailwind and other platforms [ext]

Tailwind's default spacing, type, and shadow scales already follow this philosophy: prefer them and only constrain or extend (`theme.extend.colors` / `boxShadow` in v3, `@theme` with the CSS variables above in v4). On React Native, Flutter, SwiftUI, or Compose, express the same numbers as a theme object (dp/pt), map elevation levels to the platform's shadow API, and follow platform conventions for navigation, system fonts, and 44pt / 48dp touch targets.
