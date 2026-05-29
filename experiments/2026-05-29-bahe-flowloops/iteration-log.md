# Iteration log: BAHE FLOWLOOPS LUXE

The running record of the loop. Newest round at the bottom. Each round: what we tested, what came back, what we learned, what we change next.

---

## Round 1 (2026-05-29) status: COMPLETE

### Hypotheses under test
- **Seedance 2.0:** the directorial Subject-to-Constraints format plus a timestamped 3-shot structure plus a separated audio block produces a coherent, on-brief 10s clip from text alone (no references).
- **gpt-image-2:** an ordered natural-language brief with a grouped text-instruction block renders an exact short headline ("FLOW" + "move with ease") and accurate warm product colours.
- Both: explicit negative constraints suppress text/logos/claims and keep the look design-led.

### Prompts
- Video: prompts/seedance-v1.md
- Image: prompts/gpt-image-v1.md

### Results
- Video: results/video-v1.mp4 (done)
- Image: results/image-v1.png (done)

### Analysis
- Video analysis: analysis/video-v1-analysis.md (video-analyzer skill, gemini-3-flash-preview)
- Image analysis: analysis/image-v1-analysis.md (Claude vision)

### Scorecard against brief success criteria
| Criterion | Video v1 | Image v1 |
|---|---|---|
| Aesthetic match (warm, premium, editorial) | Pass | Pass (excellent) |
| Product fidelity (3 loops, warm tones, fabric texture) | Pass | Pass |
| Format compliance (10s / 3 shots; clean headline text) | Pass (3 clean timestamped shots) | Pass (exact text first try) |
| No claims / no clutter / no trademarks | Pass | Pass on claims/marks, soft on clutter (added props) |
| Usable as a social-first asset | Pass | Pass |

### Learnings
- **Seedance 2.0 (text-only baseline is strong).** The 3-shot timestamped structure produced exactly 3 clean beats (0-3 product, 3-6 model applies loop, 6-10 texture close-up). Product colours (cream/rust/espresso) and woven-fabric texture rendered accurately with NO reference image. No identity drift flagged. Negative constraints held (no text, no logos). This validates the directorial format and timestamped multi-shot from text alone.
- **Seedance audio works but tone drifts.** Native audio generated correctly (music present, no dialogue, no speech, as requested). BUT the instrument and mood drifted: we asked for "minimal warm piano + soft percussion, restrained, slow tempo" and got "gentle, upbeat acoustic guitar." The analyzer also did not register the requested SFX (fabric stretch, footsteps) or ambience (birdsong), likely drowned by the music. So: music TYPE/MOOD control from text is weak, and layered SFX/ambience may not surface under music.
- **gpt-image-2 text rendering is production-grade.** Exact two-line headline ("FLOW" / "move with ease") rendered clean, correct weight/case/spacing, first try. The grouped text-instruction block technique works.
- **gpt-image-2 "no clutter" is soft.** It added editorial props (linen throw, wooden vessel) despite the constraint. Tasteful, but for pure product shots we need a harder constraint.

### Promote to docs/platform-prompt-formats.md (candidates)
- Confirmed: gpt-image-2 grouped-text-block technique renders exact short headlines reliably. (Part B already says this; mark as field-validated.)
- Confirmed: Seedance 2.0 timestamped 3-shot from text alone holds structure and product fidelity for a simple product. (Part A.)
- New caveat to add: Seedance 2.0 music tone/instrument is hard to control from text; expect drift, consider `@audio1` reference to lock it. SFX/ambience can be masked by music.

---

## Round 2 (2026-05-29) status: prompt ready, awaiting generation

Hugo steered this round: 15s (his Seedance max), test a logo reveal/fade, and reference the gpt-image-2 hero (no real Sportif product shots available, and his Seedance uses the `@image1` reference path). This combines several variables at once (reference + reveal + 15s + simpler audio), so it is a creative test, not a controlled single-variable round. Logged honestly.

### Prompt
- Video: prompts/seedance-v2.md (attach results/image-v1.png as @image1)

### Hypotheses under test
- `@image1` reference (the gpt-image-2 hero) locks product identity, palette, and the linen surface better than v1's text-only baseline.
- **Key test:** can Seedance reproduce the "FLOW" wordmark cleanly from the reference in the final 2s, or does it garble text (confirming logo belongs in post)? Designed to degrade gracefully: text only in the last beat, so the first 13s stay usable either way.
- Simpler audio ("ambient pad, no melody" + single chime) holds better than v1's piano-that-drifted-to-guitar.

### Result
- Attempt 1: BLOCKED by audio moderation (task ...h8jf8). "ambient pad + chime."
- Attempt 2: BLOCKED again on the moderation-safe boilerplate (task ...xt2j9).
- Attempt 3: audio-off prompt. GENERATED. Saved as results/video-v2.mp4. Analysis: analysis/video-v2-analysis.md.

### Round 2 findings (video-v2)
- **MAJOR (positive): Seedance reproduces text cleanly when it comes from an @image1 reference.** The analyzer read "FLOW" and "move with ease" correctly. So the rule is: Seedance garbles INVENTED text, but preserves text supplied via a reference image. The gpt-image-2 -> Seedance handoff keeps the wordmark. Reusable production pattern: make the branded still in gpt-image-2, reference it into Seedance.
- **MAJOR (constraint): a finished hero reference overrides detailed shot direction.** We got "the still comes alive" (close-up of loops, a hand nudges one, slight camera shift, text fades in ~7s and holds 8s), NOT our planned 4-beat sequence. Use a strong reference for "animate the poster + logo" looks; use a loose/no reference for multi-beat cinematic sequences (v1 showed text-only holds structure).
- Pacing control was weak under the strong reference (text landed at 7s not the planned 12s, held long).
- **AUDIO (confirmed by Hugo):** Seedance generated the music BY ITSELF. Hugo did not toggle anything; the prompt's "Audio: None, silent" was ignored. Key nuance: UNspecified/auto-generated audio PASSES moderation, while user-SPECIFIED music descriptions get BLOCKED (attempts 1 and 2). So the safest way to get audio is to not describe it (let Seedance auto-fill), and the only way to get true silence is the UI audio toggle, not the prompt. Prompt text does not control audio.
- **GLITCH (confirmed by Hugo):** a bad jump-cut / discontinuity around 5 to 7s where the video stopped and glitched. The analyzer missed it (glossed as "camera angle shifts slightly"). Likely a coherence failure strained by the 15s length, the beat transitions, and reference-vs-motion tension. Mitigations to test: "one continuous shot, no cuts" instruction, fewer beats, shorter duration. NOTE: the Gemini video-analyzer does not reliably catch motion glitches, human eyes still needed for that.

### Round 2 scorecard (video-v2) vs brief
| Criterion | Verdict |
|---|---|
| Aesthetic match (warm, premium, editorial) | Pass |
| Product fidelity (3 loops, warm tones, fabric) | Pass (reference locked it well) |
| Format compliance (15s; logo reveal) | Partial: logo reveal CLEAN, but 4-beat plan not executed (reference dominated), pacing front-loaded |
| No claims / no clutter / no trademarks | Pass |
| Usable as a social-first asset | Yes, as an "animated hero + logo" clip, not as a multi-beat film |

### Promote to docs/platform-prompt-formats.md (candidates)
- Add: Seedance renders text cleanly ONLY when supplied via @image reference, not when invented. gpt-image-2 -> Seedance handoff preserves the wordmark.
- Add: a finished hero reference overrides shot direction (animate-the-still vs cinematic-sequence tradeoff).

### KEY LEARNING (Round 2): Seedance 2.0 audio moderation is too strict to rely on, go audio-off
- Attempt 1 (task ...h8jf8): "ambient pad + chime" BLOCKED.
- Attempt 2 (task ...xt2j9): the vendor's own moderation-safe boilerplate ALSO BLOCKED.
- Attempt 3: audio-off (silent, music in post). This is the production answer.
Conclusion: treat Seedance 2.0 native audio as not production-ready. Default every Seedance prompt to audio-off and add music/sound in post. Promoted to docs/platform-prompt-formats.md Part A4. (Cost: zero, blocked generations are not charged.)

### Analysis (fill after generation)
- analysis/video-v2-analysis.md (pending)

### What to watch
- Reference fidelity vs v1 baseline.
- Did the logo text render clean or garble (decides post-overlay vs in-engine).
- Audio tone control.
- 15s / 4-beat pacing.

### Image track (gpt-image-2 v2, lifestyle in-use) status: COMPLETE
- Prompt: prompts/gpt-image-v2.md. Result: results/image-v2.png. Analysis: analysis/image-v2-analysis.md.
- Verdict: strongest asset so far. Person + hands/feet + product + brand text all in one pass, clean.
- Confirmed: gpt-image-2 text rendering reliable a SECOND time, on a complex lifestyle background. Hand/feet anatomy held with explicit anatomy constraints. Promote-confirmed.
- Findings: (1) product reads "draped/decorative" not in functional use, specify a concrete exercise position if real use is needed (trades against the calm editorial vibe). (2) casting skews conventional fitness-aesthetic, strategic flag for Sportif inclusive-vs-aspirational positioning, parked until Lucy's brand direction is known.

### Image track (gpt-image-2 v3, functional-use test) status: COMPLETE
- Prompt: prompts/gpt-image-v3.md (one variable changed from v2: pose forced to taut functional use). Result: results/image-v3.png. Analysis: analysis/image-v3-analysis.md.
- Verdict: BEST asset of the experiment. The explicit "stretched taut, clearly in use, not draped" instruction produced genuine functional product use with NO aesthetic penalty. Resolves the v2 draped/decorative gap.
- RECIPE confirmed (promoted to doc B6): to show real product use, name the exercise position + "loop stretched taut, clearly under tension, not draped or loose."
- Casting varied (more diverse than v2) from pure generation variance, confirms casting must be specified for consistency.

### Accidental run (video-gpt): image prompt fed to Seedance text-to-video, no reference
- Hugo accidentally used the gpt-image-v3 IMAGE prompt as a Seedance text-to-video prompt, no reference. Result: results/video-gpt.mp4. Analysis: analysis/video-gpt-analysis.md.
- Findings: (1) image prompts port to Seedance well, a specific static exercise description yields real functional MOTION with no beat direction; (2) single continuous shot showed NO glitch (vs v2's multi-beat 5-7s jump cut), supports the single-shot glitch fix and likely supersedes a separate video v3; (3) auto-audio reconfirmed (image prompt had no audio block, still got music); (4) casting drifted again (no reference).
- Hugo confirmed: (1) invented "FLOW" text clean and stable (REVISES the "invented text garbles" rule, short wordmarks survive invention); (2) motion smooth, no glitch (CONFIRMS single-shot glitch fix); (3) human action awkward and unnatural, not a believable band use (NEW failure mode: weak human biomechanics; Gemini analyzer over-rated it as "good form"). All promoted to the platform doc.

### Deferred tracks (from Round 1, still open)
- Seedance audio control via `@audio1` reference (if the simpler text line in v2 still drifts).
- gpt-image-2 reference-image edit + harder "only the product" constraint (the clutter finding).
