# Seedance 2.0 prompt, video v2

> Platform: Seedance 2.0 (reference-driven, @image1)
> Target: 15s, 9:16 vertical, logo-reveal ending, native audio on
> Reference: attach results/image-v1.png as @image1 in the Seedance UI
> Techniques under test this round:
>   1. @image1 reference (the gpt-image-2 hero) for product identity, palette, surface, and composition
>   2. a logo reveal / fade ending (does Seedance reproduce the "FLOW" wordmark cleanly from the reference, or does it garble it?)
>   3. 15s max duration with a 4-beat structure
>   4. a simpler, more forceful audio line (v1's "warm piano" drifted to "upbeat guitar")
> Note: this round changes several things at once (reference + reveal + duration + audio), so it is a combined creative test, not a controlled single-variable round. Logged as such.
>
> AUDIO MODERATION (2026-05-29): BLOCKED TWICE then resolved by going audio-off.
>   Attempt 1 (task ...h8jf8): "soft warm ambient pad + single chime" blocked.
>   Attempt 2 (task ...xt2j9): the moderation-safe boilerplate ALSO blocked.
>   Conclusion: Seedance 2.0 audio moderation is too strict to rely on right now, even safe boilerplate fails. Audio block below is set to OFF. Generate silent, add music in post. Failed generations are not charged.

## Setup before generating
- Attach `results/image-v1.png` as the reference image `@image1` in your Seedance interface.

## Paste-ready prompt

```text
Duration: 15s, 9:16, 4 beats, reference-driven, logo-reveal ending

Reference: Use @image1 for product identity (three flat woven-fabric resistance loops in light tan, terracotta, and espresso brown), the warm earthy palette, the pale linen surface, and the calm editorial composition.

[0s-4s] Beat 1: Extreme close-up of the woven-fabric texture of the loops as soft morning light slides slowly across the weave. Very slow push-in. Sensory and tactile.

[4s-8s] Beat 2: Slow pull-back to reveal the three loops resting on a pale linen surface in a sunlit room, exactly the palette and surface of @image1. A hand gently fans the three loops apart. Slow truck right, eye level.

[8s-12s] Beat 3: The camera settles and holds on the hero composition matching @image1: the three loops fanned on linen, soft window light from the left, generous empty space at the top of the frame.

[12s-15s] Beat 4 (logo reveal): The frame stills and the wordmark softly fades in within the empty top space, matching @image1 exactly: the headline "FLOW" in bold geometric sans-serif, all caps, warm charcoal, with generous letter spacing, and a smaller tagline beneath reading "move with ease" in light-weight sans-serif. Gentle light bloom as it resolves.

Style: Calm editorial realism, soft diffused morning light, warm neutral and earthy palette, shallow depth of field, subtle film grain, advertising gloss. Consistent with @image1.

Audio: None. Generate a completely silent video with no music, no sound effects, no dialogue, and no ambience. Music will be added in post. (If the interface has an audio/sound toggle, turn it OFF too.)

Constraints: Keep product colours and woven-fabric texture consistent with @image1 across all beats. The only text in the entire video is "FLOW" and "move with ease" and it appears only in the final beat, rendered clean and legible exactly as in @image1. No other text, no other logos, no brand names. No health or fitness performance claims. Calm, unhurried pacing. One camera move per beat. No whip pans, no snap zooms, no jump cuts. No warped hands, no extra fingers.
```

## Save the result as
`results/video-v2.mp4`

## What we are testing (fill in after generation)
- **Reference fidelity:** did @image1 lock the exact product look, palette, and linen surface better than v1's text-only baseline?
- **Logo reveal (the key test):** did Seedance render "FLOW" and "move with ease" cleanly in the final 2s, or did it garble the text? This decides whether logo text can come from Seedance or must be a post overlay.
- **Audio:** did the simpler "ambient pad, no melody" line hold better than v1's piano-that-became-guitar? Did the single chime land on the reveal?
- **15s pacing:** did 4 beats over 15s stay calm, or feel stretched?

## Production fallback (important)
If the text garbles (likely, given Seedance's weak text rendering), the production answer is: generate this clip ending on the clean negative-space hero frame (no text), then overlay the real wordmark in post (use the gpt-image-2 text or a real logo file). That is the reliable pattern and a valid learning, not a failure.
