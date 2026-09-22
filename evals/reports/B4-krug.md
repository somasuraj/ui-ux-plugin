# B4 - Gap review: usability references vs. Don't Make Me Think (2nd ed.)

Reviewed: `references/usability.md`, `references/audit-checklist.md`, `references/usability-test-script.md` against the full book text (to p.191) and all 48 page images.

Page numbers are the **printed book pages** (the `[ N ]` folio). PDF page / image file number = book page + 13 for arabic-numbered pages (e.g. book p.91 = `p104.png`); front matter differs (p.xi = PDF 12). All points are paraphrased.

---

## 1. Missing or under-specified (priority order)

### 1.1 Trunk test: the procedure and the worked-example critique moves (p.85-93)
`usability.md` s7 keeps the six questions but drops how to run it and everything the author actually does with it.

- **Procedure (p.86):** pick a random deep page, print/screenshot it, hold at arm's length or squint so details blur, then *quickly circle* each of the six items. Not every page has all six. Practise on a dozen random pages from other products to calibrate. Related footnote (p.85): fill a template with nonsense text and see whether people can still identify page title and site nav by appearance alone. -> `usability.md` s7 trunk test; `audit-checklist.md` "How to run an audit" step 2.
- **Example 1 defects (p.90):** a local-nav group heading is styled so it reads as the page name while the real page name is absent; the local list has no current-item marker; a large content-rich product has no search at all. Fix: page name at top of the content area, pointer + bold on the current local-nav item, search link added to utilities.
- **Example 2 defects (p.91):** Site ID sits *below* the nav and next to a promo of similar look, so it reads as an ad; the link to the parent level is placed *under* the page heading, so visual order inverts logical order; no search; in the owner's redesign the utilities became two stacked rows of underlined links (hard to read - avoid stacking underlined links). Fix: parent link above page name; page name more prominent and **flush left** (left/right alignment signals hierarchy better than centering); search button **beside** the box, not centered under it.
- **Example 3 defects (p.92):** navigation scattered around the page so nav, ads, promos and content blur together; the row that looks like "sections" is really a list of sibling products, and the current product isn't in it; breadcrumbs are the only thing locating the user; the page "keeps starting over" - stacked banners/promos mean you must scroll to find where content begins. Fix: tint the side column so the content region is obvious; attach the page name visibly to the content region. Meta-move: say when a screen is **beyond tweaking** - structural/IA dilemmas must be resolved before layout.
- **Example 4 (p.93), a near-pass:** search labelled with a different word here than elsewhere in the same product; scoped search should read as a sentence ("Search [scope] for [___]"); page name nudged larger to sharpen the nav/content boundary.
-> All of the above: new "Trunk-test defect patterns" sub-list in `usability.md` s7 and checks in `audit-checklist.md` B (see s3 below).

### 1.2 Home/first-screen critique moves (p.101-121)
`usability.md` s8 lists the ingredients but none of the defects the author calls out.

- **Tagline attachment (p.101, p.118, p.121):** a tagline is read as describing whatever it is visually attached to. Tucked inside a panel (e.g. a category box) it's read as that panel's caption, not the product's. It must sit directly beside/under/over the identity. -> s8 Tools.
- **Blurb position and length (p.119-120):** the welcome blurb must come *before* promos/featured items, not under them; the one differentiating fact (there: "unbiased, no vendor influence") must not be buried in a long sentence. -> s8.
- **Ambiguous region = defect (p.118):** if a viewer can't tell whether an area is promos or an (abstract) explanation of the product, that is a finding in itself. Cryptic promo copy makes it worse. -> s8 / s4 clearly defined areas.
- **Anti-text-block techniques (p.102, p.105):** lead-in words (Why / How / Plus) turning the blurb into a de facto bulleted list; bolding a few keywords so the blurb scans. -> s8 Welcome blurb.
- **Section-list heading states purpose (p.102):** "Shop by department" tells people the list is for buying, not reading. -> s8 entry points.
- **Reinforcement (p.102):** on a novel proposition nearly every element (tagline, blurb, list heading, testimonial with a face that draws the eye) retells the story. -> s8 "use as much space as needed".
- **New vs returning entry points (p.116-117):** a big generic start button ("Let's go!") works for first-timers but keeps trapping returning users who should have signed in; name it for what it does ("Sign up") and give returning users an equally clear sign-in on the first screen. Don't merge sign-in with a pulldown. -> s8 entry points.
- **Non-clickable things that invite clicks (p.116-117):** people clicked the step numbers and illustrations first. Author's tested conclusion: keep the 1-2-3 numbering anyway because it's the conceptual glue; removing it made the page worse, and a "more literal" illustration made the concept seem more complicated. Lesson: things need to *seem* to make sense; test before "fixing". -> s12 / s8.
- **Stay on the main point (p.115):** the first screen that worked best resisted touting secondary features. -> s8.
- **Strip right of the identity (p.101):** may be used to expand on the mission only if it clearly reads as modifying the identity; users expect a banner ad there and ignore it. -> s8.
- **"New here?" link (p.100):** fine for complex/novel products but no substitute for stating the big picture in plain sight - people click it only after failing. Also the five excuses for not explaining (p.100), esp. "people who need us already know" - testers routinely say "I'd use that, I just couldn't tell what it was". -> s8.
- **Signed-in state (p.96):** show that the user is signed in. -> s8 must-carry list.
- **Home vs persistent nav (p.107-109):** home nav may add per-section descriptions or list subsections, change orientation, and give identity more room; but also keep typeface, colors and capitalization. Concrete failure modes: section renamed, section vanishes, new section appears, same names in a different order. Trivial wording variants are fine when obviously equivalent. -> s8 bullet on landing nav.
- **Utilities vs promos (p.120-121):** utility links lumped into the same footer block as promos; fix by separating, and grouping promos with the other featured items. -> s8.
- **When to break a convention (p.121):** genuinely meaningful award badges laid out in the conventional badge row look like worthless badges. -> s4 conventions.
- **Tagline extras (p.104-106):** too short fails as much as too long (a 2-word slogan says nothing; a 10-word one isn't absorbed); clever is good only if it doesn't mislead about scope (a witty tagline implied "store only" for a product that was also an advice resource); even household names benefit, and an offline brand's online mission differs. -> s8 Tagline.
- **Above the fold / scanning depth (p.97):** people scan down only until they find a plausible link, so the top of the first screen is what matters. -> s8.

### 1.3 Site ID and "a way home" (p.64-67)
- ID must *look* like an ID: distinctive type plus a mark recognisable at any size; placed so it frames the whole page, not as the most prominent element (except perhaps on the home screen) (p.64).
- Logo-links-home is a convention many users don't know. Also provide an explicit Home item in sections or utilities, or add a discreet "Home" to the ID on every screen except home (p.66-67). The checklist's "identity ... links home" currently passes a logo-only home.
- Utilities: 4-5 most-needed in persistent nav; the rest grouped on the home page (p.66). Utilities are things that aren't part of the content hierarchy (help, cart, about, contact) (p.65).
-> `usability.md` s7 Persistent navigation.

### 1.4 Page names (p.72-74)
- Highlighting the current item in nav is **not** a substitute for a page name (p.72) - the ref says "every screen needs one" but omits this specific excuse.
- Usually the largest text on the page; position + size + color + typeface must say "heading for the whole page" (p.73).
- When an exact match with the clicked words is impossible: match as closely as possible *and* make the reason for the difference obvious (p.74). The mismatch spectrum (p.73): exact -> truncated -> parent category with no mention of the item -> error page.
-> s7 Screen names.

### 1.5 Search details (p.38 fn, p.67-69, p.93)
- Button label "Go" is acceptable only when the box itself is labelled "Search" (p.38 fn, p.67).
- If scope could be misread (this product? this section? the whole web?), spell it out (p.68).
- Use a search *box* rather than a link to a search page unless there's little reason to search (p.67).
- Same label on every screen (p.93).
- Evidence worth keeping (p.68): first thing test users do with search is look for something they know exists, to see if it works; options up front caused failed first searches through misread options.
-> s7 Search.

### 1.6 Clickability and noise specifics (p.37-39)
- When all text is colored, colored links can't be told apart; only elements with a shape (button) or underline invited clicks (p.37).
- A "click here" arrow must point *toward* its label; pointing away reads as pointing at something else (p.38).
- Noise fix shown: keep dividers but grey them out (p.39). Tolerance for clutter varies by person; default to "it's noise until proven otherwise".
-> s3 Clickability, s4 noise.

### 1.7 Instructions: the before/after edit moves (p.47-48)
Worked cut from 103 to 41 words: drop the intro that restates the obvious; don't explain how to operate standard controls (those who need it don't know the control names anyway); **keep** the time-to-complete because it helps the decide-whether-to-bother moment; move an instruction to where it's acted on (end of the form) - up front it only makes the block look daunting; if you send people elsewhere ("contact support instead"), say how and link it. Also: extra words imply you must read them, making the screen look harder than it is (p.45). -> s6.

### 1.8 Breadcrumbs (p.76-79)
- Breadcrumbs show the path, not position in the whole; alone they're not a nav scheme because they don't reveal at least the top two levels (p.77). Most useful for deep hierarchies or tying separate sub-products together (p.78).
- Below the top of the page they compete with primary nav ("which is the real navigation?") (p.78).
- Prefix with "You are here" (p.78) - omitted in ref and checklist.
- Don't enlarge the last crumb to double as the page name: headings are expected flush-left or centered, not at the end of a list (p.79).
-> s7 Breadcrumbs.

### 1.9 Tabs (p.80-84)
- Plain button bars at the top get overlooked surprisingly often in tests; tabs don't, and they create an at-a-glance nav/content split (p.80).
- Color coding: repeat the active tab's color in the other nav elements of that section; vivid active vs neutral inactive gives contrast color-blind users still perceive; roughly half of users don't register color coding at all (p.83).
- The three-state drawing (p.82): no connection/no pop; connected but same color/limited pop; connected + contrasting/full pop.
-> s7 Tabs.

### 1.10 Hierarchy placement rule from triage (p.157 fn)
An item should live in one place in the hierarchy, with a prominent "see also" cross-link wherever else people look for it - not duplicated. -> s5 or s7; audit-checklist triage.

### 1.11 Ch.12 / closing moves (p.185)
- A rule may be bent only if you (a) know what you're doing, (b) have a good reason, (c) will *actually* test it - not just intend to. (c) is the actionable part.
- Behind a stakeholder's bad idea there's usually a legitimate intention; identify it to make the case for an alternative.
- Why execs ask for sizzle (p.183): they're only ever shown static comps, so "does it look good" is all they can judge. Counter by showing them a session.
-> s12; audit report "Top fixes" rationale.

### 1.12 Goodwill nuances (p.162-167)
- Amateurish looks drain goodwill, but almost nobody leaves over looks alone (p.165) - supports keeping pure-aesthetic findings at Minor.
- A visible support number keeps people self-serving longer because they know they *could* call (p.164).
- Hidden pricing pattern: several screens of marketing before any hint of cost (p.164).
- Situation-specific content: when an event makes one question dominant, the first screen must address it; stale "latest news" and promos in the way drain goodwill (p.161-162).
- FAQ: this week's top five from support at the top of the support page; no marketing questions in disguise (p.167).
-> s9.

### 1.13 Self-blame (p.18-19)
People who struggle tend to blame themselves and tough it out rather than leave, so absence of complaints/abandonment isn't evidence of usability, and test participants will self-blame - facilitators should expect it and reassure. -> s1; test script Facilitator rules.

### 1.14 Testing-as-accessibility (p.175) and the type-resize check (p.169)
The author's 3-second accessibility check is bumping the text size and seeing if anything changes. Make it the first, quick test. Also: watch (or read observations of) screen-reader users before applying guidelines (p.175). -> s11.

### 1.15 Accessibility sequence (p.174-179)
Book's order: fix general usability first; read the screen-reader observation study; read one accessibility book; adopt CSS (content in logical source order, resizable text); only then the markup fixes. The ref flattens this into one list; restore the order so auditors don't start with alt-text while the UI is still confusing. -> s11.

### 1.16 Conventions: the innovate test (p.36)
A replacement for a convention qualifies only if it needs no learning or is worth a small learning curve - practical signal: everyone you show it to reacts with "wow". Otherwise use the convention. -> s4.

---

## 2. Wrong or distorted

| Where | Issue | Book |
|---|---|---|
| `usability.md` line 5: principles "apply equally to web apps, mobile apps, and desktop UIs" | **Contradicts the author.** The preface says web applications are deliberately *not* covered: many principles carry over, but it's a subject for a different book by someone else. Mobile isn't discussed at all (2005). Re-word as "this skill extends the book's website principles to apps; the extension is ours". | p.xi |
| s7 trunk test applied to "any deep screen" of an app | The test's premise is arriving mid-site from a search engine or external link with no prior exposure to the nav. Native/desktop apps are normally entered from their own start screen; deep links/notifications are the partial analogue. Label as extension; "How can I search?" and "major sections" are often legitimately n/a in an app. | p.85 |
| s2 "guessing wrong is cheap (Back)" | Rests on the browser Back button (most-used feature, 30-40% of clicks) and fast page loads. Where there's no universal Back/undo (desktop apps, destructive actions, slow loads), the book itself says people choose more carefully. State the dependency. | p.25, p.58 |
| s8 mapping "Home page" -> "landing/first-run/dashboard" | The home-page burdens (deals, promos, teases, timely content, one-size-fits-all, stakeholder turf wars) are content/commerce-site specifics. A dashboard or first-run screen doesn't carry them; the five questions transfer, the ingredient list mostly doesn't. Label as extension. | p.95-98 |
| s7 "Identity top-left" / checklist "top-left by convention" | Book: top of page, usually in or near the upper left, *for left-to-right languages*; RTL readers may expect it on the right. The principle is "frames the whole page". | p.64 + fn |
| s7 Search: "no scope options up front" (and checklist B "no options up front") | Slightly too absolute. Book agrees options in the persistent box are seldom worth it and scoping belongs on the results screen, but adds two things the ref lacks: spell out the scope whenever it could be misread, and a scope control is acceptable when it reads as a sentence (he keeps one in his own revision of example 4). | p.68, p.93 |
| s8 "the single most important thing to test" | Book says *one of* the most important. | p.103 |
| s1 law 2 parenthetical | OK, but book's exceptions are three: repeated drill-downs, repeated sequences **in a web application**, slow loads. Worth keeping the app mention since it's one of the few places the book speaks about apps - and it *weakens* the "clicks are cheap" rule there. | p.41 fn |
| s11 item 3 "Don't rely on script-only interactions without accessible fallbacks/ARIA" | Modern gloss. Book: avoid JavaScript without good reason; use client-side image maps. Label as updated practice, not [Krug]. Same for "visible focus" (book only says keyboard-operable). | p.179 |
| `audit-checklist.md` G: errors "explained plainly next to the field ... without losing input" | Not in the book; Krug only says provide graceful, obvious recovery and defers to *Defensive Design for the Web*. Tag as extension. | p.167 |
| `audit-checklist.md` G: "Tone is consistent with the chosen personality"; "meaningful headings" | Not Krug (RUI / general). Section is tagged [Krug]. | - |
| `audit-checklist.md` H: "interrupting pop-ups" as plain fail | Book treats pop-ups as a legitimate *informed business decision* if the numbers justify it. Check should be "deliberate and evidenced, or accidental?" | p.165 |
| `audit-checklist.md` B: "Forms/checkout use reduced navigation" | Under-specified: keep Site ID, a Home link, and only utilities that help complete the form. And it's "can sometimes", not a rule. | p.63 |
| `audit-checklist.md` A header "[Krug]" on "The five first-screen questions" | Book frames four questions plus a fifth ("where do I start?") answered separately for search / browse / sample best stuff, plus process entry and sign-in. | p.99, p.106-107 |
| s12 "designers want looks, developers want features, management wants pizzazz" | Book adds business development (deals) and the hype-vs-craft split; also says there *are* things that are clearly wrong - they're just not what teams argue about. Without that, "test everything" over-generalises. | p.126-129 |

---

## 3. Audit-checklist additions (pass/fail)

**A. Clarity at a glance**
- [ ] Tagline is visually attached to the product identity (not inside a panel where it reads as that panel's caption). (p.101, p.118)
- [ ] Tagline says what the thing *is* (not a motto, not generic benefits that fit any product), roughly 6-8 words; cleverness doesn't misstate scope. (p.104-105)
- [ ] Explanatory blurb appears before promos/featured content and above the fold; the differentiating fact is findable in one glance (list form or bolded keywords, not a paragraph). (p.102, p.119)
- [ ] Every first-screen region is identifiable as promo, explanation, navigation, or utility; none is ambiguous. (p.118)
- [ ] Headings over section/category lists state what the list is for. (p.102)
- [ ] Separate, plainly named entry points for new users (sign up / start) and returning users (sign in); no large generic button that returning users will hit by mistake. (p.116-117)
- [ ] Signed-in state is shown. (p.96)
- [ ] Utility links are not mixed in the same block as promos. (p.120)
- [ ] Nothing non-interactive invites a click (numbered steps, illustrations); if it does, either make it clickable or record it as a known, tested trade-off. (p.116-117)
- [ ] Links are distinguishable from other colored text at a glance. (p.37)
- [ ] Pointer/arrow graphics point toward the label they belong to. (p.38)
- [ ] There's some sign of life/currency; nothing stale presented as "latest". (p.96, p.162)
- [ ] When a current event makes one user question dominant, the first screen addresses it. (p.161)

**B. Navigation and wayfinding**
- [ ] Trunk test run blurred (squint / arm's length / thumbnail), not by close reading. (p.85-86)
- [ ] Site ID looks like a brand mark, is at the top framing the page, and is not beside or styled like a promo/ad. (p.64, p.91)
- [ ] There's an explicit Home affordance beyond a clickable logo (Home item, or "Home" on the ID). (p.66-67)
- [ ] No group heading or section title is styled so that it could be mistaken for the page name. (p.90)
- [ ] Page name exists even when nav highlights the current item; it's the largest text, flush left (or clearly centered over the content), and visibly attached to the content region. (p.72-73, p.91-92)
- [ ] Link/parent to the level above sits above the page name, not below it (visual order = logical order). (p.91)
- [ ] Where link text and page name differ, the difference is small and its reason obvious. (p.74)
- [ ] Current item is marked at *every* visible level (section, subsection, local list). (p.75, p.90)
- [ ] The row that looks like primary sections really is this product's sections and includes the current one (not sibling products/suites). (p.92)
- [ ] Navigation is gathered in consistent regions, not scattered among ads/promos/content. (p.92)
- [ ] The start of the content is visible without scrolling; the page doesn't "start over" several times (stacked banners/promos/headers). (p.92)
- [ ] No stacked rows of underlined text links. (p.91)
- [ ] Search uses the same label on every screen; button says "Search", or "Go" only with a box labelled "Search"; button sits beside the box. (p.67, p.91, p.93)
- [ ] Any search scope control reads as a sentence ("Search X for ___"); ambiguous scope is spelled out; every scope option returns sensible results (test one known item per scope). (p.68-69, p.93)
- [ ] Home/first-screen nav vs persistent nav: no section renamed, dropped, added, or reordered; typeface/color/caps carried over. (p.108-109)
- [ ] Breadcrumbs: at very top, tiny, ">" separators, "You are here" prefix, last item bold, last item *not* enlarged to replace the page name, and not the only thing showing location. (p.77-79)
- [ ] Tabs: active tab contrasts *and* connects to the panel; section color (if any) repeated in that section's other nav; tab shapes not used for plain buttons. (p.82-83)
- [ ] Each item lives in one place in the hierarchy with "see also" links from other plausible places. (p.157 fn)
- [ ] Form/checkout screens keep identity + Home + only form-relevant utilities. (p.63)
- [ ] Visited links/steps are distinguishable where the product is large enough to get lost in. (p.57 fn) [web only]
- [ ] Verdict option: "beyond tweaking - structural issue" is allowed instead of a list of cosmetic fixes. (p.92)

**G. Words and forms**
- [ ] Remaining instructions: no restating the obvious, no how-to-use-a-form text; time/effort estimate kept; each instruction placed where it's acted on; any "go elsewhere instead" is a link. (p.48)
- [ ] Section-front / category screens carry no filler intro. (p.46)
- [ ] Support contact visible (ideally every screen). (p.164)
- [ ] Cost is shown before the user has invested multiple steps. (p.164)
- [ ] FAQ contains real, current, candid questions; top-asked items first. (p.167)

**H. Accessibility / goodwill**
- [ ] Bump browser text size: does text actually grow and the layout hold? (first, 3-second check) (p.169)
- [ ] Any user-unfriendly pattern (pop-up, forced registration) is recorded as a deliberate, evidenced business decision. (p.165)
- [ ] Where the product can't do what users expect, it says so and apologises. (p.167)

**Triage additions**
- Pure-aesthetic complaints: Minor unless the UI looks sloppy/unprofessional (p.165).
- A rule-bend is acceptable only with a reason *and* a test actually scheduled (p.185).
- Report delivery: the book replaces the long written report with a walkthrough call ending in agreed fixes (p.138); the audit's "3 to 7 top fixes" aligns - keep the findings table short.

---

## 4. Test-script corrections

**In the script but not in this book (label as extensions; they come from Krug's later testing material or general practice - grep of the book text finds none of them):**
- "Read each task aloud, then hand over a written copy."
- "Everyone who watched lists the three most serious problems."
- "Ask observers' follow-ups" in wrap-up.
- "Note what they do over what they say"; "Don't ask leading questions or for design opinions" (consistent in spirit, not stated).
- "Video call with recording / remote" - book setup is in-person with screen recorder and observers in another room (p.142-143). Fine as a modernisation; label it.
- Fixed timings (3/3/5/30-40/5 min) - book gives only: whole session 45-60 min, tasks no more than ~45 min, 3-4 more tasks after the first (p.141, p.155).

**Deviations / omissions that change what the facilitator does:**
- **Facilitator choice (p.143):** anyone patient, calm, empathetic, a good listener, fair; not the office crank. Script says only "one facilitator".
- **Use the script openly (p.146):** read from it, ad-lib a little; being visibly comfortable making small mistakes relaxes the participant.
- **Admit ignorance; be a listener, not an expert (p.148).** Digress briefly to build rapport, then return (p.149).
- **Background questions in the book (p.148-149):** occupation; hours per week online; what they do with that time; favourite sites; whether/what they've bought online. Script's "how they use similar products" is a fair generalisation.
- **Product hidden until the moment of first reaction (p.150):** browser open but minimised; maximise only when you ask for first impressions.
- **First-screen probes (p.150-153):** "what is it, what strikes you, what would you click first" - *no clicking yet*; if stuck: "if you had to take a guess?"; "if you were at home, what would you click first?"; then, *before* they click, ask about any element the team assumes everyone uses ("what did you make of these?" / "any reason you didn't pay attention to them?").
- **Think-aloud prompt** is used only when the participant goes quiet (p.152).
- **Task handoff (p.154-155):** let them name their own instance of the task; at hesitation ask "which one do you think you'd click?" then "go ahead and do it"; stop rules match the script.
- **Aesthetic comments (p.151, p.165):** ignore unless about three of four use strongly negative words. Script says "nearly everyone" - close; give the 3-of-4 rule.
- **Consent (p.147):** recording consent and, if needed, NDA - both short, plain language; promise recording is seen only by the project team; mention observers are watching elsewhere; tell them recording means you take fewer notes.
- **"I'll keep us moving, but it should be fun" (p.147)** - sets pace expectation; missing.
- **Recruiting (p.139-141):** "within limits" - basic web/app literacy is the floor; try to reflect the audience but don't get hung up; exceptions: single-type audience when it's no harder to recruit; clearly split audiences (sample every group in at least one round, even if that round is larger than usual); domain knowledge (at least one round). Pay a bit above the going rate (shows you value them; they turn up on time); prefer the curious over the money-motivated; even a 30-min session costs them an extra hour of travel; friends and neighbours are fine; don't describe the product *or the organisation* beforehand. Three reasons loose recruiting works: experts also muddle through; don't design so only the target can use it; experts aren't insulted by clarity.
- **Rounds (p.138-139):** with the first round's blockers fixed, the next three users reach problems the first three couldn't; >4 per round produces more notes than can be processed, mostly nits. Hire a professional/recruiter only if it doesn't reduce the number of rounds (p.137, p.140).
- **Observers (p.143-144):** ask executives to "drop in for a few minutes for morale" - they tend to stay. Observers in a separate room. A morning-only format raises attendance (p.159).
- **Debrief (p.156):** goal is deciding *what to try next*, not the perfect solution; serious problems will be obvious to everyone who watched. Book: no report at all, just decisions at lunch (p.159).
- **Triage wording (p.157-158):** kayak = all affected users notice quickly, recover unaided, aren't fazed; kayak problems usually stem from an ambiguity with no clean resolution (item fits two categories) - fix is a cross-link, not a move. Feature requests: probe - they usually already have another source and wouldn't switch.
- **What testing is for (p.131-135):** don't test to choose between two aesthetics - testing usually shows the argument was beside the point (nobody understood the value proposition). Can't prove A beats B. Changes after launch are costly because users resist change - argument for early tests (p.134).
- **Focus groups (p.133):** script frames them only negatively. Book: good *early* for whether the concept/value proposition appeals, for testing feature names, and for feelings about competitors; optionally late to fine-tune messaging; never for "can people use it".
- **Testing competitors first (p.144):** also gives a new facilitator pressure-free practice and the team a thick skin. Use the product yourself, then watch one or two people.
- **Cubicle test (p.145):** specifically *print* the new screen (esp. forms) and show it to the next person (the "2-minute" figure is the script's own).
- **Accessibility (p.175):** regular testing and fixing what confuses everyone is the best single accessibility step; consider observing assistive-tech users. Could be one line in Principles.
- **Live demo value (p.134):** a sub-10-minute test with a volunteer on someone else's product reliably yields pages of notes - supports offering a "10-minute version" of the script.
