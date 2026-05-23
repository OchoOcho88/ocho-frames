# Brand Kit (Modern Default)

This is a starter brand kit. Customize freely — colors, fonts, voice, and visual style should reflect *you* once we know the direction.

## Color palette

### Primary
- **Ink** `#0F172A` — main text, headings, dark backgrounds
- **Mist** `#F8FAFC` — page backgrounds, light surfaces
- **Accent** `#6366F1` — buttons, highlights, brand moments (indigo, modern + versatile)

### Supporting
- **Steel** `#475569` — secondary text, borders
- **Cloud** `#E2E8F0` — dividers, subtle backgrounds
- **Glow** `#A5B4FC` — soft accent, hover states

### Semantic
- **Success** `#22C55E`
- **Warning** `#F59E0B`
- **Error** `#EF4444`
- **Info** `#3B82F6`

## Typography

### Display (titles, hero text)
- **Primary:** Inter Tight, weights 600–800
- **Fallback:** -apple-system, BlinkMacSystemFont, sans-serif

### Body (captions, paragraphs)
- **Primary:** Inter, weights 400–500
- **Fallback:** -apple-system, BlinkMacSystemFont, sans-serif

### Mono (code, data labels)
- **Primary:** JetBrains Mono, weight 400–500

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
- **Default duration:** 400ms for most transitions, 200ms for micro-interactions, 800ms for hero reveals
- **Reduced motion:** always respect `prefers-reduced-motion: reduce`

## Voice & tone (placeholder — customize)

- **Confident, not cocky.** Make claims you can back up.
- **Plain language over jargon.** "Faster" beats "performant."
- **Short sentences.** Cut anything that doesn't earn its place.
- **One idea per scene.** Video moves fast — don't crowd it.

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
