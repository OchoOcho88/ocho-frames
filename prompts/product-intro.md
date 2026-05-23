# Product Intro Video

## When to use
A short, polished intro that introduces a product, feature, or service. Lives on landing pages, in emails, at the start of demos.

## Prompt

```
Using /hyperframes, create a [10 / 15 / 20]-second product intro video.

Product: [name]
One-line description: [what it does, in plain language]
Target audience: [who]
Tone: [confident / playful / serious / cinematic]

Structure:
- Frame 1 (0–2s): logo reveal with subtle motion (scale + fade, or letterform draw)
- Frame 2 (2–6s): the headline — what it is, in one big sentence
- Frame 3 (6–end-2s): 2–3 quick beats showing key features (icon + label + micro-animation)
- Frame 4 (last 2s): CTA — "[try it / book a demo / visit URL]"

Specs:
- Aspect ratio: 16:9
- Resolution: 1920x1080
- FPS: 60 (smooth for product motion)
- Background music: yes, royalty-free, ends with a soft tail
- Sound: subtle UI clicks and woosh transitions

Style:
- Pull all colors, fonts, and motion principles from brand/brand-kit.md
- Generous whitespace
- One idea per frame, never crowded
- Smooth transitions — use shader-transitions from the catalog (flash-through-white, etc.)

Assets I can provide:
- Logo: [path or "use a placeholder"]
- Product screenshots: [paths or "make abstract visuals"]
- Demo footage: [path or "skip — go fully animated"]

Output to my-projects/[project-name]/
```

## Notes
- 15s is the standard — long enough to land the point, short enough to keep attention
- 60fps for product/UI motion makes it feel premium
- The CTA should be specific ("Start free trial" not "Learn more")
