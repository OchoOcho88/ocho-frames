<!--
Competitor Video Analysis: marketing-conversion lens (12-section framework).

This file is designed to be passed as-is to the video-analyzer skill via --prompt-file.
Everything below is sent to the model as the analysis prompt. See
recipes/analyze-video-with-gemini.md for the exact shell invocation.

Lens: marketing-conversion (why this ad converts), not pure creative-craft.
Section 1 still captures craft details so the visual-design lens isn't lost.
-->

You are analyzing a competitor's video ad. Your job is to produce a structured marketing breakdown so a creator can study what works and steal the *patterns*, not the content.

Use the 12 sections below in this exact order, with the exact headings shown. Use `MM:SS` timestamps wherever you reference a specific moment. Quote on-screen text and voiceover **verbatim**, never paraphrased.

Output format: clean markdown. Each section gets a `##` heading. Use bullet points where the section calls for a list; use prose where the section calls for a paragraph.

---

## 1. Format & Production Style

- **Format type:** UGC (phone-shot, creator-style), motion graphics, animation, talking-head, mixed, etc.
- **Aspect ratio:** vertical 9:16 / square 1:1 / horizontal 16:9 (and which platforms that targets)
- **Length:** total runtime, plus pacing style (conversational / fast-cut / cinematic / etc.)
- **Visual craft:** dominant color palette (name 3-5 key colors as hex if you can infer, otherwise descriptive), typography (serif/sans/display, weight, scale relative to screen), motion language (snappy / smooth / static / popping), use of footage vs animation vs both
- **Audio craft:** voiceover present? (human / AI / accent / pace / energy), music (mood / instrumentation / level relative to voice), sound design (transitions, UI sounds, emphasis hits), caption/subtitle treatment (position, style, sync)

## 2. The Hook (first 3 seconds)

- **On-screen text (0:00-0:03):** verbatim
- **Opening visual:** what the viewer actually sees in the first frame and the first action
- **Hook formula:** identity callout / curiosity gap / shock / before-after / problem-amplification / pattern interrupt / etc. (name the formula)
- **Why it stops the scroll:** specific tension, hook, or signal that earns the next 2 seconds of attention

## 3. Target Audience

- **Who this is for:** demographic + psychographic (e.g., "busy moms 25-45 who value clean ingredients")
- **Signals that point to that audience:** what in the video tells you who it's for (setting, props, wardrobe, vocabulary, references)
- **Their state coming in:** what the viewer is feeling/believing BEFORE this ad lands

## 4. Core Pain Point / Desire

- **Pain:** the problem being addressed (be specific: not "self-tanner is bad" but "self-tanner stains clothes and takes hours to dry")
- **Desire:** the outcome being sold
- **Verbatim quotes:** lines from voiceover OR on-screen text that name the pain or desire, with `MM:SS` timestamps

## 5. The Angle

- **The reframe:** the specific framing or repositioning the ad uses (e.g., "not a treatment, it's a lotion")
- **What it's positioning AGAINST:** the obvious category default or competitor expectation the ad is rejecting
- Why this angle is differentiated (vs. running the same play as the category)

## 6. Product Introduction

- **First appearance:** timestamp when the product is first shown on screen
- **Brand name + how it's shown:** logo on label / voice mention / on-screen text (be specific)
- **Attribute the intro leans on:** mechanism (how it works) / ingredient story / ease-of-use / outcome / social proof. Which lever does the intro pull?

## 7. Proof & Credibility

- **Real-time demo moments:** with timestamps and a one-line description of what's demonstrated
- **Verbatim claims:** quotes that make a specific claim, with timestamps
- **Hard evidence shown:** numbers, comparisons, before/after, expert/customer references, ingredient callouts
- **Risky proof:** any "stress test" moment where the product is being deliberately challenged in front of the viewer (white shirt, white couch, slow-mo, etc.)

## 8. Beat-by-Beat

A timestamped scene-by-scene breakdown covering the entire video, end to end. Format each beat as:

- `MM:SS-MM:SS`: one-line description of the beat (what happens + its purpose in the funnel)

Aim for 5-10 beats. Don't skip dead air or transitions. They're part of pacing.

## 9. CTA

- **Style:** hard sell / soft referral / URL drop / discount code / "link in bio" / etc.
- **Verbatim words:** exactly what the CTA says (voiceover and/or on-screen text)
- **Timestamp:** when the CTA appears, and how long it's on screen
- **Friction level:** how easy is it to act on this CTA right now?

## 10. What Works

3-5 specific techniques that make this ad effective. For each:

- **Name the technique** (in a memorable phrase, e.g., "white shirt stress test", "identity anchor", "fear-benefit bridge")
- **Why it works:** the underlying psychology or attention mechanic in one sentence

## 11. What's Weak

2-3 specific weaknesses or missed opportunities. For each:

- **Name the issue**
- **Suggest a concrete fix** that a creator could apply if they were rebuilding this ad

## 12. Steal-Worthy Patterns

3 transferable patterns we could apply to a *different* brand or product. For each:

- **Name the pattern** (in a memorable phrase)
- **How to translate it:** one concrete example of how this pattern would look applied to a different category or brand

---

## Critical rules (read before responding)

- **Quote verbatim, never paraphrase.** When you cite on-screen text or voiceover, the words must match what's actually in the video.
- **No invented narrators or quotes.** If there is no voiceover, state that explicitly in Section 1 and again in Section 4 if relevant. Do NOT make up speaker names, dialogue, or audio that isn't there.
- **Label inferences.** When a section asks you to read intent (target audience, hook formula, what works), it's fine to infer. Just write "Inferred: …" or "Likely: …" so the reader knows it's a read, not an observation.
- **N/A is a valid answer.** If a section genuinely doesn't apply (e.g., no CTA in the video), write `N/A: [one-line reason]` instead of fabricating content.
- **Timestamps are required** wherever you reference a moment. `MM:SS` format.
- **No em dashes (—).** Use periods, commas, colons, or parentheses instead. This is a workspace-wide rule (see `brand/agency-brand-kit.md`).
