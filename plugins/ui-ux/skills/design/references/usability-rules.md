# Usability rules (auditable)

What makes an interface obvious and easy. Distilled in our own words from *Don't Make Me Think*, 2nd ed. (Steve Krug). Section numbers are cited by the audit checklist as `UR n`.

**Scope, honestly.** The book is about **websites**; its author says web applications are a subject for a different book, and it predates mobile. Applying these rules to web apps, mobile, and desktop UIs is **this skill's extension**, marked [ext]. Translate "page" to "screen" and "site" to "product", but check each rule's premise:
- "Guessing wrong is cheap" rests on a fast, universal Back. Where there is no easy undo (desktop apps, destructive or slow actions) people choose more carefully, and wrong guesses cost more [ext].
- The trunk test assumes arriving cold on a deep page from a search engine or link. In an app the analogue is a deep link, notification, or returning after weeks; "major sections" and "search" may legitimately be n/a [ext].
- The home-page burdens (promos, deals, teasers, stakeholder turf) are content/commerce specifics. For a dashboard or first-run screen, the five questions transfer; the ingredient list mostly doesn't [ext].

## UR1 The three laws

1. **Don't make me think.** Every screen self-evident, or at least self-explanatory with minimal effort. The tie-breaker for any design argument.
2. **Clicks are cheap when they're mindless.** Difficulty per choice matters more than the count: roughly three unambiguous clicks equal one that needs thought. Count matters more for steps people repeat, repeated sequences in an application, and slow loads.
3. **Cut half the words, then half of what's left.**

People who struggle tend to blame themselves and tough it out, so an absence of complaints is not evidence of usability.

## UR2 Things that put question marks in heads

- **Names**: cute, clever, marketing, internal, or technical labels. Use the obvious word even if it sounds plain.
- **Clickability**: nobody should wonder whether something is clickable. When all text is colored, colored links can't be told apart; shapes and underlines invite clicks. Nothing static should look interactive, and an arrow must point toward the label it belongs to.
- **Up-front decisions that need thought**: how to search, which category "I am", what format to type in. Accept what people type and do the sensible thing.
- A screen must never raise: Where am I? Where do I start? Where did they put ___? What matters most here? Why did they call it that?

## UR3 Design for scanning

People scan, click the first plausible option, and muddle through without reading. So:

1. **Clear visual hierarchy**: importance = prominence; related things look related; nesting shows what belongs to what. A heading must span only what it governs.
2. **Use conventions.** Replace one only if the replacement needs no learning or is clearly worth a small learning curve (the practical signal: everyone who sees it says "wow"). Occasionally a convention misleads: meaningful award badges in the usual badge row look like the worthless kind.
3. **Clearly defined areas.** A viewer should be able to point at regions and name them (navigation, things I can do, what they sell). An area that can't be classified (promo or explanation?) is itself a finding.
4. **Obvious clickability** (UR2).
5. **Minimize noise**: shouting (everything clamoring, exclamation marks) and background clutter (many small distractions such as heavy rule lines; greying them out is often enough). Assume everything is noise until proven otherwise.

## UR4 Mindless choices

Each option must be unambiguous to an outsider. Watch for abbreviations, insider product names, overlapping categories, and choices where people can't tell which one applies to them. An item lives in **one** place in the hierarchy, with a prominent "see also" wherever else people look for it.

## UR5 Words

- **Kill happy talk**: welcome and intro text that says nothing (the "blah blah" test). Its favourite habitat is landing and section-front screens.
- **Kill instructions.** Nobody reads them until muddling through has failed, and extra words make a screen look harder than it is. If some must stay: drop what's obvious, don't explain how to operate standard controls, **keep** a time-or-effort estimate (it helps people decide to bother), put each instruction where it's acted on, and turn "go elsewhere instead" into a link.

## UR6 Navigation

Navigation supplies the sense of place a screen can't. It helps people find things, tells them where they are, reveals what's here, shows how to use the product, and builds confidence in the makers.

1. **Persistent navigation**, same place and behaviour on every screen:
   - **Identity** that looks like a brand mark, at the top so it frames everything (upper left in left-to-right languages), never beside or styled like a promo where it reads as an ad.
   - **A way home.** The logo should link home, but many people don't know that convention: also give an explicit Home item, or a discreet "Home" on the identity everywhere except home.
   - **Sections** (primary nav), with room for subsections.
   - **Utilities** (things outside the content hierarchy: help, account, cart, about): the 4 to 5 most needed, less prominent than sections. Park the rest elsewhere.
   - **Search** where there's enough content: a box, a button, and the word "Search" (button "Go" only if the box itself is labelled "Search"); the same label on every screen; the button beside the box. No instructions. Avoid options in the persistent box; offer scoping on the results screen. If a scope control stays, make it read as a sentence ("Search [invoices] for [___]"), spell out any ambiguous scope, and make sure every option returns sensible results: people test search first with something they know exists, and a failed first search costs trust.
   - Exceptions: the first screen may differ; forms and checkout can drop to identity, Home, and only the utilities that help finish the form.
2. **Lower levels.** Design navigation for every level before debating first-screen colors. People spend as much time deep in a product as at the top, and third-level navigation is where most products fall apart.
3. **Screen names.** Every screen needs one, even when the nav highlights the current item. It frames the content unique to that screen, is prominent (usually the largest text, flush left or clearly centered over the content), and **matches the words that were clicked**. If an exact match is impossible, stay close and make the reason obvious. The link to the parent level sits above the name, not below it.
4. **"You are here"** markers at every visible level (section, subsection, local list). The usual failure is subtlety: use two distinctions (color plus bold). If it seems to stick out too much, it's about right.
5. **Breadcrumbs** are an accessory: top of the screen, small type, ">" separators, optionally prefixed "You are here", current item bold. They show the path, not the whole, so they never replace navigation, and the last crumb is never enlarged to stand in for the screen name.
6. **Tabs** are self-evident and hard to miss. The active tab connects to its panel and contrasts with the rest; one is selected on entry; color-coding is a bonus cue only (many people never register it). Don't draw tab shapes for plain buttons.
7. **Pulldowns hide options from scanning**, are hard to scan, and feel twitchy. Fine for long alphabetized lists of known names; poor for navigation or for lists where people don't know the name they want.
8. **Trunk test.** Take a random deep screen, blur it (squint, arm's length, thumbnail), and quickly point to: product identity, screen name, sections, local options, "you are here", search. Defects seen in the book's worked examples:
   - A group heading styled so it reads as the screen name while the real name is absent.
   - No current-item marker in the local list.
   - Identity below the nav or next to a look-alike promo.
   - Parent link placed under the heading, so visual order inverts logical order.
   - A "sections" row that is really a list of sibling products and omits the current one.
   - Navigation scattered among ads, promos, and content.
   - A page that "keeps starting over": stacked banners and headers, so the content start needs scrolling.
   - Stacked rows of underlined links.
   - Typical fixes: screen name flush left, larger, attached to the content region; a tinted side column so the content region is obvious; search button beside its box.
   - It is legitimate to conclude a screen is **beyond tweaking**: a structural problem to resolve before layout.

## UR7 The first screen

Five questions it must answer at a glance, correctly, with little effort:
1. What is this? 2. What do they have here? 3. What can I do here? 4. Why here and not somewhere else? 5. **Where do I start?** (to search, to browse, to sample the best stuff, to begin a process, to sign in)

People scan down only until something plausible appears, so the top of the first screen matters most.

- **Tagline**: directly beside, under, or over the identity (inside some other panel it reads as that panel's caption). Says what the thing *is* and why it's better: clear, about 6 to 8 words (two words say nothing, ten aren't absorbed), not a motto, not generic benefits that fit any product; clever only if it doesn't mislead about scope. Even famous brands benefit.
- **Welcome blurb**: terse, prominent, visible without scrolling, *before* promos and featured items, at most about four key points, with the differentiating fact findable at a glance (lead-in words or a few bold keywords rather than a paragraph). Not a mission statement.
- Use as much space as the proposition needs and no more; stay on the main point instead of touting secondary features. A novel proposition may need almost every element to retell the story.
- **Entry points look like entry points** with plain labels ("Search", "Browse by category", "Sign in", "Start here"); headings over lists say what the list is for ("Shop by department"). Give new users and returning users separate, plainly named entries: a big generic "Let's go!" keeps trapping returning users. Show signed-in state.
- "New here?" links help for novel products but don't replace saying it in plain sight: people click them only after failing.
- First-screen nav may change layout, add section descriptions, and give identity more room, but section **names, order, and grouping stay identical** to the persistent nav (no renamed, vanished, added, or reordered sections), with the same typeface, colors, and capitalization.
- Keep utilities separate from promos. **Resist promo overload**: each stakeholder gains from one more promo while the cost is shared by all (tragedy of the commons). Rotate, or cross-promote from other popular screens.
- Show signs of life; nothing stale presented as "latest". When an event makes one user question dominant (outage, strike, recall), the first screen addresses it.
- One of the most important things to test with outsiders: insiders can't see that the main point is missing.

## UR8 Goodwill

People arrive with a limited reservoir of goodwill, varying by person and mood. Problems drain it; one bad moment (a giant registration form) can empty it; considerate touches refill it. Looking amateurish drains it too, though almost nobody leaves over looks alone, so keep purely aesthetic findings minor.

Drains:
- Hiding what people want: support contact, prices, fees, shipping. (Several screens of pitch before any hint of cost is the classic; a visible support number actually keeps people self-serving longer.)
- Punishing input formats. Accept spaces, dashes, and parentheses, then normalize.
- Asking for information the task doesn't need.
- Fake sincerity.
- Sizzle in the way: splash screens, long intros, heavy marketing imagery, autoplay.
- Looking sloppy.

Refills:
- Make the top ~3 things people come to do obvious and easy.
- Be upfront about what you'd rather not say (costs, limits, outages).
- Save steps; show visible effort in content quality and organization.
- Real, current, candid FAQs with this week's top questions first.
- Creature comforts (print-friendly, export).
- Easy error recovery; prevent errors where possible.
- When you can't do what people want, say so and apologize.

A deliberately user-unfriendly choice (a pop-up that measurably raises revenue) is a legitimate **informed business decision**. The finding is when it's accidental or unevidenced.

## UR9 Forms and personal data

- Ask only for what this transaction needs. Extra fields produce fake data, fewer completions, and a worse impression.
- Few optional fields too: the sight of many fields is discouraging.
- Show what people get in exchange. Ask for more later, once there's a relationship.
- [ext] Errors belong next to the field, in plain words, without wiping what was typed. (The book only says recovery must be graceful and obvious.)

## UR10 Accessibility baseline

The real reason: it's the right thing to do, and it changes some people's lives. The book's order matters:

1. **Fix what confuses everyone first.** Confusing UI is worse for people using assistive technology, who recover from confusion less easily. Testing and fixing general usability is the biggest single accessibility step.
2. **Three-second check**: increase the browser's text size. Does the text grow, and does the layout hold?
3. **Screen-reader users scan with their ears**: they listen to the first words of each link, line, and heading and move on. Front-load keywords.
4. Content in a logical source order with layout done in CSS; text that resizes.
5. Low-hanging markup fixes: meaningful `alt` text (empty for decorative images); form controls tied to their labels; a "skip to main content" link; everything operable by keyboard; no scripting without good reason.
6. [ext] Modern practice beyond the book: visible focus styles, landmarks and heading structure, ARIA names for custom controls, 3:1 contrast for control boundaries, color contrast per `design-tokens.md`.

## UR11 Pushing back on harmful requests

Two requests come up constantly; the book answers both.

**"Collect more personal data at signup."** People filling a form ask of every field: why do they want this, and do they need it to give me what I came for? If not, they conclude you are either clueless or willing to annoy them for your own purposes. Consequences: fake data (the more you ask, the more justified people feel in lying), fewer completed forms (length alone deters), and a worse impression even among those who finish. Counter-offer: ask only what this transaction needs, keep optional fields few, show what they get in return, and collect the rest later once there is a relationship.

**"Add more sizzle"** (splash screen, animation, big imagery, music). Stakeholders usually judge static mock-ups, so "does it look impressive" is the only question they can answer. But most people arrive to get something done; anything that slows that reads as clueless or self-regarding. Looks must be professional and attractive, never at the cost of working well. Exceptions: products where the sizzle is the product (entertainment, pure branding, portfolios). Counter-offer: show a recording of a real person using it.

In both cases look for the legitimate goal behind the request (lead quality, brand impression) and serve it another way.

## UR12 When a rule should bend

Almost any idea can be made to work with enough care, and any good idea can be ruined in the details. Bend a rule only if you know which one, have a real reason, and will **actually test** the result. Behind a stakeholder's bad idea there is usually a legitimate intention; find it and serve it another way. There are things that are simply wrong; they're just rarely what teams argue about.
