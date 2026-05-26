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
├── compositions/             ← your own video projects live here
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
├── scripts/                 ← INPUTS: content scripts, storyboards, voiceover scripts
│
└── outputs/                 ← OUTPUTS: AI-generated content lands here
    ├── video-analyses/      ← markdown reports from video-analyzer (tracked in git)
    ├── downloads/           ← competitor videos (gitignored)
    ├── generated-images/    ← AI image generations (gitignored)
    └── voiceovers/          ← AI narration audio (gitignored)
```

## Quick commands (run from Terminal)

```bash
# Open the starter project
cd ~/Desktop/hyperframes/compositions/starter

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
cd ~/Desktop/hyperframes/compositions
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
- HyperFrames GitHub: https://github.com/heygen-com/hyperframes

## First time setting this up on a new machine?

This workspace lives at https://github.com/OchoOcho88/ocho-frames. To clone it fresh:

```bash
# Clone the repo
git clone https://github.com/OchoOcho88/ocho-frames.git ~/Desktop/hyperframes
cd ~/Desktop/hyperframes

# Restore the ~940MB of reference repos (not committed to keep this repo small)
./setup.sh

# Set up your API keys
cp .env.example .env
# then open .env and fill in real values

# Install the starter project's dependencies
cd compositions/starter
npm install
npm run dev
```

Requirements: Node.js v22+, FFmpeg, Git. See session 001 in `memory.md` for the exact setup steps if anything's missing.

## Contributing

This is currently a personal workspace, but if you're collaborating with me:

1. **Branch for your work.** Don't commit directly to `main`.
   ```bash
   git checkout -b your-name/short-description
   ```

2. **Update `memory.md`.** Every session that does meaningful work should add an entry at the top, following the format in the template comment at the bottom of the file.

3. **Save new prompts to `prompts/`** if you've refined a workflow over 2–3 uses.

4. **Save new recipes to `recipes/`** when a workflow is proven. Use `_template.md` as the starting point.

5. **Keep secrets out of git.** Never commit `.env`, API keys, or anything in `assets/` that's licensed or personal. The `.gitignore` covers `.env` but be deliberate about other media.

6. **Push when done.** Open a PR back to `main` if you have one set up, or commit + push directly if we're moving fast.
   ```bash
   git add .
   git commit -m "what changed, in one line"
   git push -u origin your-name/short-description
   ```

7. **Ask Claude for help.** Most of the prompt templates, brand alignment, and recipe writing can be delegated. See `prompts/` for starting points.
