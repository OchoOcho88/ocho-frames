# Sportif image prompts (source of truth for generated/)

> Every keeper image in `generated/` has its prompt here. Engine: gpt-image-2 unless noted.
> Format follows docs/platform-prompt-formats.md Part B. Voice rules apply: no health claims, no leather, warm neutrals.
> Shared API settings: output_format png. Iterate quality low (Cowork), finals quality high (Claude Code).
> SIZING: Instagram feed = 1088x1360 (4:5 portrait), stories/reels = 1088x1920 (9:16), website hero = 1536x1024 (3:2). The v1 to v4 prompts were 3:2; v5 to v7 are the same three concepts recomposed 4:5 for IG ("product in the lower two thirds, breathing room at the top"). Always ask which placement before generating.

## fresh-explore: first gpt-image-2 GENERATIONS (from scratch, not edits) (2026-07-22)

Exploratory Sportif key visuals generated from detailed prompts (our first use of the
`images/generations` endpoint, vs edits). Script + full prompts: `scripts-local/gen_fresh_explore.py`
(the source of truth). Six proofs kept at `generated/images/fresh-explore/` (force-committed as
keepers since low proofs do not regenerate identically). All 1024x1536, quality low, no text
(we overlay type). Shared blocks: warm-neutral PALETTE, modest/elevated GUARD (no glam, no leather),
BAND = flat wide knitted-fabric loop.
- **bw1 / bw2** brand-world lifestyle (blush set by a sunlit window / caramel ritual on a jute rug).
- **ch1 / ch2** campaign hero (blush activewear on a terracotta wall with a long shadow / mid-shot
  holding the flat knitted band, sculptural light).
- **bu1 / bu2** band-in-use editorial (standing abduction in a reformer studio / squat with the band
  visibly tensioned).
Casting came back naturally diverse (fits Sportif's inclusive positioning). Note the bands are
AI-imagined here (not the real SPORTIF label) — stamp the real label for product-accurate use.
Next: rerun winners at high quality (native Terminal) + add photoreal directives to cut the AI look.

## reference-reskin: pilates-studio ad to Sportif waitlist poster (2026-07-22)

Reskin of a reference layout Lucy sent (a pilates-studio "WE'RE OPEN" ad). Technique = **no-text AI plate + our own PIL type layer** (we always own the type). Two scripts are the source of truth; finals gitignored.

**Plate (gpt-image-2 images/edits, `scripts-local/reskin_pilates_ref.py`).** Source `clients/sportif/products/reference-layouts/pilates-open-ref.png`, size 1024x1536, quality low. Prompt strips ALL text + the big watermark, adds a blush booty band, removes the black ankle weights, keeps layout/poses/warm palette. Two variants: `asis` (keep the raised-leg glute bridge) and `bridge` (convert to a standard two-foot glute bridge so the band loops both thighs). Shared prompt verbatim in the script's `COMMON` string. bridge is the pick.

**Type layer (PIL, `scripts-local/layout_reskin.py`, system python).** Copy set "Find your resistance", all Glacial Indifference, navy #13253D / cream #F4EEE5 (sampled from the reference):
- kicker: `meet` (Regular 34) over `SPORTIF` (Regular 60, real lockup tracking -0.059) = the logotype
- headline: `FIND YOUR` / `RESISTANCE` (Bold, fit to 84% width, cream, soft drop-shadow for contrast over the photo)
- watermark: faint oversized `SPORTIF` (~12% alpha, lower area)
- CTA: solid terracotta #833827 `JOIN THE WAITLIST` pill, cream text, soft lift shadow (bottom-anchored)
- footer: SPORTIF lockup + `@sportifcollection`
- bridge only: a framed single-band product card in the left void (blush MEDIUM card, rounded + shadow + cream border) — ties product to lifestyle inside one still.
Finals: `generated/images/reference-reskin/reskin-bridge.png` (lead), `reskin-asis.png` (alt). No dates (trademark hold). Every copy/colour/size is a one-line edit.

## cosmos-peach series (2026-07-20) LUCY-APPROVED, 15 finals

Batch edit of the whole renamed `assets/Cosmos pictures` folder (15 of 16 jpegs; `bw-arms-detail` hard-blocked by moderation 3x). Per-image prompts live verbatim in `scripts-local/gen_cosmos_peach.py` (JOBS dict). Shared recipe: images/edits, gpt-image-2, per-image instruction + palette block + KEEP block (same person/pose/lighting, recompose 4:5, no text) + the moderation-safety sentence. Proofs 1024x1280 low, finals 1088x1360 high. Narrow lockup (62 percent width, y 0.49) via `scripts/overlay_logo.py`, cream #F4F2EA, except peach #F0CDB3 on the two palest images (lookbook-grid-9up, bw-forward-fold). Group shots use a palette MIX (peach/caramel/cream/terracotta, one per model). Outputs in `generated/images/cosmos-peach/` with text-free bases in `notext/`.

## cosmos-babyblue edit (2026-07-18) FIRST USE OF THE EDITS ENDPOINT

Reference-image edit, not a generation. Source: `assets/Cosmos pictures/cosmos_form-backbend-editorial.jpeg` (the FORM editorial backbend image; renamed 2026-07-20 from `cosmos_sportif logo.jpeg` in the folder-wide descriptive rename). Endpoint: `images/edits`, model gpt-image-2, size 1024x1280 (4:5), quality high, output png. Prompt:

"Edit this photo. Two changes only. 1) Recolour the model's fitted ribbed athletic outfit (currently dark chocolate brown shorts and top) to a soft pastel baby blue, keeping the exact same fabric texture, ribbing, seams, fit, shadows and highlights. 2) Completely remove the large white 'FORM' text overlay, cleanly reconstructing the model's body, outfit and the warm beige studio background that sit behind the letters. Keep everything else identical: the same model, her one-arm backbend pose with the extended leg, her hair, the white crew socks, the warm beige seamless backdrop, the soft diffused lighting, the subtle film grain, the crop and framing. No text, no logos, no watermarks anywhere in the output. This is a tasteful, professional athletic fitness editorial photograph of a gymnast in modest full-coverage sportswear, suitable for a mainstream sportswear catalogue."

Then the REAL Sportif logo lockup stamped via `scripts/overlay_logo.py`: SPORTIF in Glacial Indifference REGULAR (not Bold), tracking -0.059 em, plus the short centred underline rule (43 percent of wordmark width, thickness 4.5 percent of cap height, sitting 44 percent of cap height below the baseline). All geometry measured off `assets/05-logo-sportif-white-on-peach.png`. Cream `#F4F2EA` (sampled from the original FORM letters), logo block centred at 49 percent height. Main = 76 percent of image width (matches FORM's footprint), narrow variant = 62 percent. Files: `cosmos-babyblue-notext.png` (text-free base, reusable), `cosmos-babyblue-wordmark.png` (main), `cosmos-babyblue-wordmark-narrow.png`.

Learnings: (1) the edits endpoint preserved pose, grain and backdrop with no mask needed, two-instructions-only prompts work well; (2) OUTPUT moderation false-positived [sexual] at quality high on the backbend pose (low passed); appending the "tasteful professional athletic editorial, modest full-coverage sportswear" sentence cleared it, keep that sentence for any bodysuit or backbend imagery; (3) baby blue is OFF-PALETTE, an intentional concept exploration Hugo confirmed, not a new brand colour; (4) MISTAKE CAUGHT BY HUGO: the first pass stamped a styled wordmark (Bold, wide tracking, no rule) instead of the actual logo. The real lockup lives in `assets/05-logo-sportif-white-on-peach.png` and `08-logo-sportif-peach-on-cream.png`: light weight, tight tracking, underline rule. Always stamp the lockup via `overlay_logo.py`, not a hand-styled wordmark; `overlay_wordmark.py` remains for plain headline text only.

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
