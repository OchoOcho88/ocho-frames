# HyperFrames Workspace

Your personal HyperFrames workspace for creating animated charts, product intros, TikTok-style videos with AI voiceover, PDF/CSV-to-video summaries, and lower-thirds for existing footage.

## Folder layout

```
hyperframes/
├── README.md                ← you are here (workspace overview)
├── memory.md                ← session log: what we did, what we learned
├── .env.example             ← template for API keys (copy to .env, never commit .env)
├── .gitignore               ← prevents secrets and big folders from being committed
│
├── main-source/             ← the official HyperFrames source code
│   └── hyperframes/         ← reference implementation, browse for understanding internals
│
├── examples/                ← real example projects to study and learn from
│   ├── launch-video/        ← HeyGen's actual launch video (production-quality reference)
│   └── student-kit/         ← 12 finished motion-graphics projects + GSAP teaching kit
│
├── my-projects/             ← your own video projects live here
│   └── starter/             ← scaffolded starter project (with 15 AI skills pre-installed)
│
├── assets/                  ← reusable media — shared across projects
│   ├── audio/               ← music, SFX, narration files
│   ├── video/               ← stock footage, b-roll
│   ├── images/              ← logos, photos, illustrations
│   └── fonts/               ← custom typography
│
├── brand/                   ← brand kit: colors, fonts, voice, style guide
│   └── brand-kit.md         ← starter (modern default — customize when you're ready)
│
└── scripts/                 ← content scripts, storyboards, voiceover scripts
```

## Quick commands (run from Terminal)

```bash
# Open the starter project
cd ~/Desktop/hyperframes/my-projects/starter

# Install dependencies (first time only)
npm install

# Preview in browser with live reload
npm run dev

# Check composition for errors
npm run check

# Render to MP4
npm run render
```

## Creating a new project

```bash
cd ~/Desktop/hyperframes/my-projects
npx hyperframes init my-new-video
cd my-new-video
npm install
npm run dev
```

## Working with Claude / AI agents

The starter project has 15 AI skills pre-installed in `.agents/skills/`. When you open the project in Claude Code, Cursor, or another AI agent, you can invoke them with slash commands:

- `/hyperframes` — main composition authoring
- `/hyperframes-cli` — init, lint, preview, render commands
- `/hyperframes-media` — TTS, transcription, background removal
- `/gsap` — timeline animations
- `/tailwind` — utility-class styling
- `/lottie`, `/three`, `/waapi`, `/animejs`, `/css-animations` — specific animation runtimes
- `/website-to-hyperframes` — turn a URL into a video
- `/remotion-to-hyperframes` — port from Remotion

## Goals for this workspace

- Animated charts and dashboards
- Product intro videos
- TikTok-style hook videos with captions synced to AI voiceover
- Turning PDFs and CSVs into video summaries
- Lower-thirds and overlays for existing footage

## Integrations planned

- **OpenAI GPT Image 2.0** — for generated visuals inside compositions
- **HeyGen** — AI avatar narrators and template videos

API keys go in `.env` (copy `.env.example` to start). Never commit `.env`.

## Useful links

- HyperFrames docs: https://hyperframes.heygen.com/introduction
- Catalog (50+ ready-made blocks): https://hyperframes.heygen.com/catalog
- Prompting guide: https://hyperframes.heygen.com/guides/prompting
- vs Remotion: https://hyperframes.heygen.com/guides/hyperframes-vs-remotion
- GitHub: https://github.com/heygen-com/hyperframes
