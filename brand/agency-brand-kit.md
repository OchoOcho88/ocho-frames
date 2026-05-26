# Agency Brand Kit (Ochoproductions)

> This is the agency's own brand kit. Distinct from client brand kits, which live at `clients/<client>/brand.md`.

## Agency identity

- **Company:** Ochoproductions
- **Domain:** ochoproductions.com
- **Owner:** Hugo
- **Contact:** hugo@ochoproductions.com

### Current state (as of 2026-05)

The agency itself is in the same pre-launch state as some of its clients. Visual identity is intentionally TBD until it's worked out properly.

- **Logo:** not yet designed
- **Landing page:** not yet built (ochoproductions.com is the future home)
- **Brand colors:** not yet defined. Defaults below are placeholders.
- **Typography:** not yet defined. Defaults below are placeholders.
- **Tagline / one-liner:** not yet written
- **Positioning statement:** not yet written

### What IS locked (treat as ground truth even before the visual identity exists)

- The **voice and tone rules** below. These apply to every piece of copy, regardless of whether the visual identity is in place.
- The agency name **Ochoproductions** and email **hugo@ochoproductions.com**. Use these exactly, capitalization included, in client communications and signoffs.

## Voice & Tone (locked rules)

These rules apply to ALL copy produced by or through this workspace. That includes client-facing emails, prompts the AI runs, generated marketing content, internal docs, and anything else written in this agency's voice.

### Hard rules (non-negotiable)

1. **No em dashes (—). Ever.** Em dashes are an AI tell. Use periods, commas, colons, or parentheses depending on context. Hyphens (-) and en dashes (–) are fine.
2. **Friendly and professional, to the point.** Short sentences. Cut anything that doesn't earn its place. If a comma is doing the work of a period, use the period.
3. **Plain language over jargon.** "Faster" beats "performant." "We can ship by Friday" beats "We are positioned to deliver an EOW release."
4. **One idea per sentence.** If a sentence has two ideas, split it.
5. **Confident, not cocky.** Make claims you can back up. Avoid hedging filler ("just", "maybe", "I think") unless genuinely uncertain.

### Punctuation substitutes (when you'd reach for an em dash)

| Original instinct | Use instead |
|---|---|
| "Take your time — there's no wrong answer." | "Take your time. There's no wrong answer." |
| "We did X — and Y." | "We did X, and Y." |
| "A few things — X, Y, Z." | "A few things: X, Y, Z." (colon) |
| "(by the way — important)" | "(by the way: important)" or parenthetical recast |
| "Same idea — any brand." | "Same idea. Any brand." |
| "It works — well." (for emphasis) | "It works. Well." or just "It works well." |

### Voice anchors

- We write like we talk to a friend who happens to be a smart business owner. Direct, warm, no filler.
- We don't perform expertise. We just are useful.
- Specific over general. "Friday at 5pm" beats "later this week."

## Color palette (modern default, customize when needed)

### Primary
- **Ink** `#0F172A`. Main text, headings, dark backgrounds.
- **Mist** `#F8FAFC`. Page backgrounds, light surfaces.
- **Accent** `#6366F1`. Buttons, highlights, brand moments (indigo, modern and versatile).

### Supporting
- **Steel** `#475569`. Secondary text, borders.
- **Cloud** `#E2E8F0`. Dividers, subtle backgrounds.
- **Glow** `#A5B4FC`. Soft accent, hover states.

### Semantic
- **Success** `#22C55E`
- **Warning** `#F59E0B`
- **Error** `#EF4444`
- **Info** `#3B82F6`

## Typography

### Display (titles, hero text)
- **Primary:** Inter Tight, weights 600 to 800
- **Fallback:** -apple-system, BlinkMacSystemFont, sans-serif

### Body (captions, paragraphs)
- **Primary:** Inter, weights 400 to 500
- **Fallback:** -apple-system, BlinkMacSystemFont, sans-serif

### Mono (code, data labels)
- **Primary:** JetBrains Mono, weight 400 to 500

### Type scale (1.25 ratio)
- Hero: 64px
- H1: 48px
- H2: 36px
- H3: 28px
- Body large: 20px
- Body: 16px
- Caption: 14px
- Micro: 12px

## Motion principles

- **Default ease:** `cubic-bezier(0.4, 0, 0.2, 1)` (Material standard, feels natural)
- **Snappy ease:** `cubic-bezier(0.34, 1.56, 0.64, 1)` (gentle overshoot, modern UI)
- **Default duration:** 400ms for most transitions, 200ms for micro-interactions, 800ms for hero reveals.
- **Reduced motion:** always respect `prefers-reduced-motion: reduce`.

## CSS variables (drop into any HyperFrames composition)

```css
:root {
  /* Color */
  --c-ink: #0F172A;
  --c-mist: #F8FAFC;
  --c-accent: #6366F1;
  --c-steel: #475569;
  --c-cloud: #E2E8F0;
  --c-glow: #A5B4FC;
  --c-success: #22C55E;
  --c-warning: #F59E0B;
  --c-error: #EF4444;
  --c-info: #3B82F6;

  /* Typography */
  --font-display: 'Inter Tight', -apple-system, sans-serif;
  --font-body: 'Inter', -apple-system, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;

  /* Type scale */
  --t-hero: 64px;
  --t-h1: 48px;
  --t-h2: 36px;
  --t-h3: 28px;
  --t-body-lg: 20px;
  --t-body: 16px;
  --t-caption: 14px;
  --t-micro: 12px;

  /* Motion */
  --ease-natural: cubic-bezier(0.4, 0, 0.2, 1);
  --ease-snappy: cubic-bezier(0.34, 1.56, 0.64, 1);
  --dur-micro: 200ms;
  --dur-default: 400ms;
  --dur-hero: 800ms;
}
```
