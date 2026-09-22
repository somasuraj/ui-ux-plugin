# Design process (create and large refactors)

How to go about designing, as opposed to what good looks like (`visual-rules.md`, `usability-rules.md`). Loaded for create mode and big redesigns; not needed for audits. [RUI] = *Refactoring UI*, [Krug] = *Don't Make Me Think*, [ext] = this skill's addition.

## 1. How people will actually use it [Krug]

Design for this person, not the attentive reader you imagine:
- **They scan.** They're in a hurry, know most of the screen is irrelevant, and hunt for words matching their task (plus "free", "sale", their own name).
- **They satisfice.** They take the first reasonable option, not the best one, because guessing wrong is usually cheap. It is less cheap where there's no easy undo [ext], so make consequential choices clearer still.
- **They muddle through.** They don't read instructions or build an accurate model, and they stick with whatever works. People who do "get it" find more, see more of what you offer, and feel smart, which brings them back.
- So: design billboards, not brochures. Work at a glance or not at all.

## 2. Start from a feature [RUI]

- **Feature first, shell later.** Design a real piece of functionality with its real content (the search form, the expense row) before the nav, sidebar, and page chrome. You can't decide navigation until you know what it navigates.
- **Low fidelity first.** Skip fonts, shadows, icons at the start. A thick marker on paper makes fussing impossible. Sketches are disposable: stop when a decision is made.
- **Greyscale before color.** Make spacing, size, weight, and contrast carry the hierarchy. The primary action and the selected state must already read in grey; color then enhances.
- **Short cycles.** Design a simple version, build it, fix real problems in the working thing, then design the next piece. Don't try to imagine every edge case in the abstract.
- **Be a pessimist.** Don't design in what you aren't ready to build: every affordance on screen must work. Ship the smallest useful version; nice-to-haves come later, and a version without them still beats nothing shipped.

## 3. Choose a personality on purpose [RUI]

Carried by a few concrete levers, kept consistent everywhere:
- **Typeface**: serif = classic/elegant (often headlines only, sans for UI), rounded sans = playful, neutral sans = plain (lets other elements carry it).
- **Color**: blue = safe/familiar, gold = premium, pink = fun. Trust how it feels. Avoid a brand color that reads as success or danger [ext].
- **Radius**: none = formal, small = neutral, large = playful. Button shape follows (square vs pill). Never mix.
- **Words**: impersonal = official, casual = friendly. Words are everywhere in a UI; they matter as much as color.
- No gut feel? Look at the other products your audience already uses and match that register. Don't copy direct competitors: you'll look like the knock-off.
State the personality in one line before building, then hold to it.

## 4. Build systems before screens [RUI]

Decide once, not per element: type scale, weights, line-heights, spacing/sizing scale, color shades, elevation, radius, border widths, opacity. Use the project's existing tokens; if none exist, take only what you need from `design-tokens.md`.

**Choosing by elimination** is a loop: pick a value from the scale, compare it with its two neighbours; if the middle wins you're done; if a neighbour wins, re-centre on it and compare again. With a constrained scale two of three options usually look obviously wrong.

Whenever you catch yourself deliberating over a low-level value twice, that's a missing system.

## 5. Make it self-evident [Krug]

- A newcomer should know what this is, what they can do, and where to start. Name things with the obvious word. Make every choice mindless.
- Use conventional patterns unless the replacement needs no learning or is clearly worth a small learning curve.
- Work out navigation for every level of the product, not just the top, before polishing any one screen.
- Words: cut happy talk and instructions; then cut again.
- Know the top ~3 things people come to do and make them obvious and short. Surface **existing** functionality for those tasks; be sceptical of inventing **new** features to fix a usability problem [ext: these two don't conflict].

## 6. Design every state [RUI + ext]

Empty (first thing a new user sees: say what to do, one call to action, hide chrome that needs data), loading, error with recovery, success, disabled, hover/focus/active, long and missing content, small screen (start near 400px), signed-out vs signed-in. For a static deliverable, expose states through query parameters or a clearly labelled demo strip so they can be seen and screenshotted [ext].

## 7. Ambition pass: from correct to good

Fixing every finding produces a tidy screen, not necessarily a good one. Before verifying, spend one deliberate pass on making the screen work harder, **using only data and functions that already exist**:

- **Lead with the key fact** [RUI hierarchy, Krug top tasks]. What does the person most need to know on arrival? Say it first and largest: "1 invoice overdue: $4,250", "6 open, 2 overdue", "3 of 5 seats used". Derive it from what is already on the screen; never invent figures.
- **Make the top task one obvious action** near that fact (the overdue summary carries a "Send reminder"; the empty list carries "Add the first one").
- **Give scanning eyes handles**: counts on existing filters or tabs, a relative date beside the real date ("due tomorrow"), status as a word in a tinted pill, the row that needs attention tinted.
- **Rethink one stock component** if it is the heart of the screen [RUI think outside the box]: merged two-line cells, selectable cards for the main decision, a richer empty state.
- **Two or three finishing touches**, no more [RUI]: an accent border on the card that matters, icons for bullets, a tinted section background, a brand-colored focus ring.
- Then stop. If a touch does not help someone find, understand, or do something, it is decoration: leave it out. Everything shown must be true: no placeholder features, no invented numbers, no unsourced claims.

## 8. Verify like an outsider

- Render it (`measuring.md`), squint at it, check it in grey, check 400px.
- Run `scripts/scan.py` on your own output and clear the candidates (both passes). After a refactor, run `scripts/check_refactor.py` against your snapshot. Measure contrast for every non-trivial pair.
- Self-review against `audit-checklist.md` sections A to H for the screens you built (first-screen items in A apply to landing/first-run screens; for in-app screens answer "what is this screen, what can I do, where do I start" instead).
- Hallway check [Krug]: show a new screen, especially a form, to someone who hasn't seen it.

## 9. Settling arguments [Krug]

- Team debates about what "users like" are people projecting their own preferences: designers want looks, developers want features, business wants deals and pizzazz. There is no average user.
- Replace "do people like X?" with "does this X, with this wording, in this context, work for the people likely to use it?" The only answer is to watch people use it (`usability-test-script.md`).
- Requests for sizzle: most people want to get something done, not be engaged. Looks must be professional, never at the expense of working well, except where sizzle is the product (entertainment, pure branding, portfolios). Executives ask for sizzle because static comps are all they're shown; show them a test session.
- Behind a bad request there is usually a legitimate intention. Find it and serve it another way.

## 10. Keep improving your eye [RUI]

- When a design impresses you, ask what the designer did that you wouldn't have thought of (an inverted popover, a button inside an input, a two-color headline).
- Rebuild interfaces you admire without inspecting them; chasing the differences teaches the tricks (tighter heading line-height, tracked uppercase, layered shadows).
