# Seedance 2.0 prompt, video v1

> Platform: Seedance 2.0 (text-to-video, no references this round)
> Target: 10s, 9:16 vertical, 3 shots, native audio on
> Techniques under test this round: directorial Subject-to-Constraints format, timestamped 3-shot structure, the audio block, explicit negative constraints. Text-only baseline (no @image refs yet).

## Paste-ready prompt

```text
Duration: 10s, 9:16, 3 shots

Subject: A set of three flat woven-fabric resistance loops in warm tones, light tan, terracotta, and espresso brown. A premium, design-led fitness accessory.

[0s-3s] Shot 1: Close-up of the three loops resting in a neat stack on a pale linen surface in a sunlit room. Camera locked-off, then a very slow push-in. Soft morning light catches the fine woven fabric texture and the warm colours.

[3s-7s] Shot 2: A woman in matching sand-toned activewear sits on a light wooden floor and gently slides the terracotta loop over her thighs, settling into a calm seated position. Medium shot, slow truck right following the movement of her hands, eye level.

[7s-10s] Shot 3: Close-up of the loop as the fabric stretches smoothly with a slow, controlled movement, then relaxes. Gentle push-in, then hold. Warm light, shallow depth of field.

Style: Calm editorial realism, soft diffused morning light, warm neutral and earthy palette, shallow depth of field, subtle film grain, advertising gloss.

Audio:
- Music: minimal warm piano with soft percussion, slow tempo, restrained, no vocals.
- Sound effects: soft fabric stretch, quiet movement on a wooden floor.
- Ambience: airy indoor room tone, faint birdsong from outside.
- No dialogue. No subtitles.

Constraints: Keep the product colours and woven-fabric texture consistent across all shots. Calm, unhurried pacing. One camera move per shot. No on-screen text, no captions, no logos, no brand names. No health or fitness performance claims. No whip pans, no snap zooms, no Dutch angles, no jump cuts. No warped hands, no extra fingers.
```

## Notes for the operator

- Render at the highest resolution your Seedance access allows (1080p if available), 9:16.
- Save the result as `../results/video-v1.mp4`.
- If Seedance flags or refuses: the most likely trigger is a brand cue. There are none here by design, but if it happens, note the exact wording in the iteration log.

## What we are testing (fill in after generation)

- Did the 3-shot timestamped structure produce 3 clean beats in 10s, or did it compress/blur them?
- Did the audio block produce coherent music + SFX + ambience with no dialogue?
- Did the product stay color- and texture-consistent across shots (the known identity-drift risk)?
- Did the negative constraints hold (no text, no logos, no claims)?
