# Do-it-yourself usability testing

A lightweight testing method distilled (in our own words) from *Don't Make Me Think* [Krug]. Use it to validate a design, settle a review disagreement, or as an audit's "how to verify" section. Claude can't run sessions itself; it can prepare the plan, tasks, and script, and help triage the notes.

- **Tags:** untagged = from the book. `[ext]` = this skill's addition, not in the book.
- **Scope:** the book's method is for websites tested in person. Apps and remote sessions are this skill's extension.

## Principles

- One participant beats none; one early beats fifty near launch. After launch, users resist change, so fixes cost more.
- **3 to 4 participants per round.** More yields unprocessable notes, mostly nits.
- **Two rounds of 3 beat one of 8:** with round one's blockers fixed, the next three reach problems the first three never got to.
- Iterate: test, fix, test again. Aim for **one morning a month**; mornings-only also raises observer attendance.
- **What it is for:** informing judgment. It cannot prove A beats B or settle a taste argument; sessions usually show the argument was beside the point (nobody understood the offer).
- **Focus groups are a different tool.** Useful early: concept appeal, feature names, feelings about competitors. Optionally late, to tune messaging. Never for "can people use it".
- Testing and fixing what confuses everyone is the best single accessibility step. Consider watching assistive-technology users too.
- Hire a professional or recruiter only if it does not mean fewer rounds.

## Setup

**Recruiting**
- Recruit loosely, grade on a curve. Floor: basic web/app literacy. Reflect the audience if easy; don't get hung up on it.
- Why it works: experts muddle through too; a product only its target can use is badly designed; clarity insults nobody.
- Three exceptions: (1) single-type audience that is no harder to recruit: use it; (2) clearly split audiences: sample every group in at least one round, even if larger; (3) domain knowledge needed: at least one round with people who have it.
- Pay slightly above the going rate: it shows you value them and they turn up on time (a short session still costs them an hour of travel). Prefer the curious over the money-motivated.
- Friends and neighbours are fine. Never describe the product or organisation beforehand.

**Facilitator**
- Patient, calm, empathetic, fair, a good listener. Not the office crank.

**Room and kit**
- Quiet room, device, screen and audio recorder.
- Product loaded but hidden (minimised) until the first-reaction moment.
- Observers sit in a separate room. Invite executives to "drop in for a few minutes for morale"; they tend to stay, and one watched session out-persuades any argument.
- Consent form (plus NDA if needed): short, plain language.
- `[ext]` Remote: video call with screen share and recording; observers join muted, cameras off.

## What to test, when

- **Before designing:** competitors. Use one yourself, then watch one or two people. A free working prototype, pressure-free facilitator practice, and a thicker skin for the team.
- **Early:** sketches and wireframes.
- **During build:** prototypes and finished key flows.
- **Any new screen, especially forms: the cubicle test.** Print it and show it to the next person who has not seen it.

Two kinds of test:
- **"Get it" test:** first screen only. Do they grasp what it is, what it offers, how it is organised, where to start?
- **Key task test:** give a task and watch. Let them choose their own instance ("find something you would actually buy"): real knowledge, real motivation.

**10-minute mini version:** one volunteer, any product, first-screen reactions plus one task. Even this fills pages of notes; good for convincing a sceptical team.

## Session script (45 to 60 minutes; tasks no more than about 45)

Read the script openly and ad-lib a little; being relaxed about your own small slips relaxes the participant. `[ext]` Step timings are rough.

**1. Welcome** `[ext: 3 min]`
- "It's the product on trial here, not you. There are no wrong moves."
- "Be blunt. Nothing you say will upset anyone." (If true: "I didn't make it.")
- "As you go, say aloud what you are looking at, trying to do, and thinking."
- "I may hold questions until the end; we need to see what happens with nobody around to help."
- "I'll keep us moving so we finish on time, but this should be fun."
- Consent: only the project team sees the recording; colleagues are watching elsewhere; recording means fewer notes for you. Get signatures.

**2. Background** `[ext: 3 min]`
- Occupation; weekly hours online or in similar products; what they do there; favourites; online purchases.
- Purpose: relax them, show you listen, gauge experience; accuracy is irrelevant. Brief rapport digressions are fine.

**3. First-screen reactions** `[ext: 5 min]`
- Reveal the product now. **No clicking yet.**
- "Just look for a moment. What is this? What stands out? What could you do here?"
- If stuck: "If you had to guess?"
- "If you were at home, what would you click first?"
- Still before any click, ask about elements the team assumes everyone uses: "What did you make of these?" or "Any reason you passed over them?"

**4. Tasks** `[ext: 30 to 40 min]`
- First task plus 3 to 4 more, covering the top things people come to do; they name their own instance where possible.
- `[ext]` Read each task aloud, then hand over a written copy.
- At a hesitation: "Which one do you think you would pick?" then "Go ahead and do it."
- Stop when they finish, get truly frustrated, or you stop learning.

**5. Wrap-up** `[ext: 5 min]`
- Answer the questions you deferred. `[ext]` Ask observers' follow-ups. Thank and pay.

## Facilitator rules

- Stay neutral. Do not help, hint, explain, or defend.
- Listener, not expert. If you do not know, say so.
- Use the think-aloud prompt only when they go quiet: "What are you thinking?" "What are you looking at?"
- Expect self-blame: strugglers blame themselves and push on. Reassure them: the confusion is the product's fault and exactly what you need to see. (So no complaints is not proof of usability.)
- Aesthetic comments: ignore unless about 3 of 4 participants use strongly negative words; almost nobody leaves over looks.
- `[ext]` No leading questions and no requests for design opinions ("Would you like it if...").
- `[ext]` Weight what they do over what they say.

## Debrief (same day, over lunch)

- Aim: decide **what to try next**, not the perfect solution. Serious problems will be obvious to everyone who watched.
- `[ext]` Each observer lists the three most serious problems they saw.
- Then: (1) **triage** what to fix now; (2) **problem-solve** the smallest fix for each.

Typical findings: concept not understood; the words they look for are missing (wrong categories or names); too much noise, so they miss what is in front of them.

Triage rules:
- **Kayak problems:** everyone affected notices quickly, recovers unaided, and is not fazed. Ignore them. Usual cause: a real ambiguity (item fits two categories). Usual fix: a cross-link, not a move.
- Do not add explanations; remove what obscures the meaning.
- **Feature requests:** probe. They usually already get it elsewhere and would not switch.
- Head-slappers and cheap, visible wins first.
- Check each fix breaks nothing that worked.

No report: a short list of decisions, then another round next month.

## Template Claude can fill in

```markdown
# Usability test plan: <product> - round <n>
**Goal of this round:** ...
**Participants (3 to 4):** who, how recruited, which exception applies (if any), incentive
**Facilitator:** ...
**What's being tested:** competitor / sketches / prototype / build; device; in person or remote [ext]
**"Get it" questions:** ...
**Elements we assume everyone uses (ask before first click):** ...
**Tasks (first + 3 to 4):**
1. <scenario in the user's words, no UI terms; let them pick their own instance> - success looks like: ...
2. ...
**Things we're specifically unsure about:** ...
**Logistics:** date, room/link, recorder, observer room, executives invited, consent form / NDA
**Debrief:** time, attendees; output = decisions on what to try next
```

Write tasks as realistic scenarios without UI labels (say "you want to stop getting the weekly emails", not "go to Notification Settings").
