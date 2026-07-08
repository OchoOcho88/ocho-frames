# Sportif image prompts (source of truth for generated/)

> Every keeper image in `generated/` has its prompt here. Engine: gpt-image-2 unless noted.
> Format follows docs/platform-prompt-formats.md Part B. Voice rules apply: no health claims, no leather, warm neutrals.
> Shared API settings: output_format png. Iterate quality low (Cowork), finals quality high (Claude Code).
> SIZING: Instagram feed = 1088x1360 (4:5 portrait), stories/reels = 1088x1920 (9:16), website hero = 1536x1024 (3:2). The v1 to v4 prompts were 3:2; v5 to v7 are the same three concepts recomposed 4:5 for IG ("product in the lower two thirds, breathing room at the top"). Always ask which placement before generating.

## tagline-row action backgrounds (2026-07-08) SENT TO LUCY, pending her pick

Three text-free 1088x1440 (3:4 grid tile) backgrounds for the tagline row above the grid banner. Prompts live in `clients/sportif/scripts-local/gen_action_bg.py` (training / fashion / ritual); taglines overlaid in real Glacial Indifference via `overlay_action_tiles.py`. Currently rendered quality low; finals need quality high in Claude Code.

Two new reusable prompt rules learned this session:

1. **Exercise poses must be described joint by joint** or the model fakes the anatomy. For the glute bridge: "she lies on her back, the back of her head, shoulders, upper back and arms resting flat on the mat, arms relaxed alongside her body with palms down, knees bent, feet flat on the mat hip-width apart, hips raised so her torso forms one straight diagonal line from shoulders to knees."
2. **A band lying loose in a scene needs the full form spec** or it melts into ribbons and pastry shapes: "a wide flat continuous closed loop of knitted elastic fabric, like an oversized fabric headband, shown as a clean open circle lying flat, not folded, not twisted, not a coiled tube, not a ribbon."

Also produced (same taglines, non-AI): flat terracotta, terracotta gradient + soft text shadow (`build_tagline_tiles.py` / `_v2.py`), and linen/plaster texture backgrounds (`gen_tagline_bg.py`). Grid wordmark banner in three colourways via `build_grid_banner.py` (cream / white / peach variants).

## ig-hero-v8-flat-notext + wordmark overlay (2026-07-07) THE PRODUCTION PATTERN

Same prompt as v7 below but with the text instructions REMOVED and these constraint changes: "a clean calm area of plain wall at the top for a headline to be added later, no text or logos anywhere."
Then the real wordmark is stamped in true Glacial Indifference Bold:
`python3 scripts/overlay_wordmark.py generated/images/ig-hero-v8-flat-notext.png generated/images/ig-hero-v8-flat-wordmark.png`
This is the default for anything publishable: generate text-free, overlay real type. In-image AI text is only for quick concept comps.

## coming-soon-hero-v4-unboxed (2026-07-07)

A high-end product photo of a flat wide elastic fabric resistance band (booty band), a continuous loop of soft knitted stretch fabric in blush peach, half emerging from a caramel cotton drawstring pouch tipped gently on its side on a pale linen surface, as if just unboxed.
Early morning light through a window from the left, gentle long shadows, a sense of quiet ritual.
Style: premium minimalist editorial ecommerce photography, sharp focus on the band and pouch, background softly blurred.
Color palette: warm neutrals only, blush peach, caramel, terracotta, linen white; the band is the most saturated element.
Small woven fabric label on the band, no leather anywhere.
Text instructions: at the top center, a headline that reads exactly "SPORTIF" in bold modern geometric sans-serif, letter-spaced, warm charcoal, all caps. No other text or logos anywhere.
Constraints: 3:2 landscape, calm editorial morning-ritual mood, no people, no clutter, tasteful and elevated, giftable feeling.

## coming-soon-hero-v3-set (2026-07-07)

An overhead flat-lay product photo of a giftable fitness set arranged on pale linen: a flat wide elastic fabric resistance band (a continuous loop of soft knitted stretch fabric in blush peach), a slim vegan ankle strap in caramel with soft fabric padding, and a small caramel cotton drawstring pouch, arranged with generous spacing.
Early morning light, gentle soft shadows, calm and unhurried.
Style: premium minimalist editorial flat-lay photography, everything in sharp focus, composition balanced with negative space.
Color palette: warm neutrals only, blush peach, caramel, terracotta, linen white.
Small woven fabric labels on the products, no leather anywhere.
Text instructions: centered at the top, a headline that reads exactly "SPORTIF" in bold modern geometric sans-serif, letter-spaced, warm charcoal, all caps. No other text or logos anywhere.
Constraints: 3:2 landscape, calm editorial morning-ritual mood, no people, no clutter, tasteful and elevated, looks like a beautiful gift.
Known issues at low quality: ankle strap reads like a watch cuff, labels drift leather-ish. Fix before final.

## coming-soon-hero-v2-flat (2026-07-07)

A high-end product photo of a flat wide elastic fabric resistance band (booty band), a continuous loop of soft knitted stretch fabric in blush peach, lying flat on a pale linen surface, its loop shape clearly visible, next to a small caramel cotton drawstring pouch.
Early morning light through a window from the left, gentle long shadows, calm and unhurried.
Style: premium minimalist editorial ecommerce photography, sharp focus on the band, background softly blurred, shallow depth of field.
Color palette: warm neutrals only, blush peach, caramel, terracotta, linen white; the band is the most saturated element.
The band has a small woven fabric label, no leather anywhere.
Text instructions: at the top center, a headline that reads exactly "SPORTIF" in bold modern geometric sans-serif, letter-spaced, warm charcoal, all caps. No other text or logos anywhere.
Constraints: 3:2 landscape, calm editorial morning-ritual mood, no people, no clutter, tasteful and elevated.

## coming-soon-hero-v1-low (2026-07-07, superseded)

First test. Band read as a woven basket coil and the patch looked like leather. Fixes folded into v2 onward: name the band form explicitly ("flat wide elastic fabric loop, knitted stretch fabric") and forbid leather.
