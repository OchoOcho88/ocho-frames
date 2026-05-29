# Experiment: BAHE FLOWLOOPS LUXE (first prompt loop)

> Date started: 2026-05-29
> Platforms: Seedance 2.0 (video), gpt-image-2 / ChatGPT Images 2.0 (static)
> Spec reference: docs/platform-prompt-formats.md
> Status: Round 1 prompts ready, awaiting generation

## What this is

The first run of the self-improving prompt loop (see experiments/README.md). We take a real, design-led fitness-accessory product as a stand-in for what Sportif might be building, write Stage 4 production prompts for both platforms using the 2.0 format spec, generate, analyze, and learn.

## Why this product

Hugo found the **BAHE FLOWLOOPS LUXE** online: a set of 3 flat fabric resistance loops. It is NOT confirmed to be what Lucy is making, but it sits squarely in the design-led, warm-palette, "fitness equipment as a lifestyle object" lane that the Sportif SWOT flagged as the proven Bala-style playbook. So it is a strong stand-in for learning the prompt patterns we will reuse for Sportif.

## Source product (described from the packaging photo)

- **Brand:** BAHE. **Product:** FLOWLOOPS LUXE, "3 Flat Resistance Loops."
- **Three resistance levels, color-coded:** Light (warm tan/beige), Medium (terracotta/rust red), Heavy (espresso/dark brown).
- **Material:** flat woven fabric loops (not rubber tubes).
- **Aesthetic:** premium minimalist. Warm blush/peach packaging, earthy tone palette, rose-gold and charcoal type. Hero image is a seated woman using the loop around her thighs, design-led and editorial, not gym-bro.
- **Palette to carry into prompts:** blush, warm tan, terracotta, espresso, soft neutrals, natural morning light.

Save the screenshot in `source/` (see source/README.md).

## Intent (what a good output looks like)

- Reads as **premium and design-led**, the product treated as a lifestyle object (Bala reference), not performance gear.
- Warm, calm, editorial. Soft natural light. AU-friendly bright daylight feel.
- **No health-outcome claims** anywhere (hard Sportif rule). Lead with aesthetic, lifestyle, function.
- Product colors and fabric texture render accurately and consistently.
- Generic placeholder branding only. Do NOT reproduce the BAHE or FLOWLOOPS trademarks (also avoids Seedance's brand-name refusal failure mode).

## Success criteria (judge the output against these)

1. Aesthetic match: warm, premium, editorial, design-led.
2. Product fidelity: three loops, correct warm tones, fabric (not rubber) texture.
3. Format compliance: video is 10s and follows the shot/timestamp plan; image renders the headline text cleanly.
4. No claims, no clutter, no competitor trademarks.
5. Usable as a social-first asset (9:16 video, portrait image).

## Decisions for Round 1

- **Video:** 10s, 9:16 vertical (Reels/TikTok/FYP first, per marketing-fundamentals). 3-shot timestamped structure. Native audio on (music + SFX + ambience, no dialogue).
- **Image:** 2:3 portrait product hero (1024x1536), quality high for final, with a short placeholder headline to test gpt-image-2 text rendering.
- **Reference strategy:** Round 1 is text-only (no `@image` refs) to get a clean baseline of the format. Round 2 will add the product photo as `@image1` (identity) and test whether reference-driven fidelity beats text-only. That is the one-variable change.
