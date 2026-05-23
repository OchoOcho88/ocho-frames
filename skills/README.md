# Custom Skills

Workspace-level skills that extend what AI agents can do beyond what ships with HyperFrames.

## How skills work in this workspace

There are **two places** skills can live:

### 1. Project-scoped skills (already set up)
Live in `my-projects/<project>/.agents/skills/`. The 15 HyperFrames skills (hyperframes, gsap, lottie, three, etc.) are installed there per-project, automatically loaded when an AI agent opens that project.

### 2. Workspace-scoped custom skills (this folder)
Live in `skills/` at the workspace root. These are skills *we* add — third-party or hand-rolled — that should be available everywhere, not just inside one project.

## What goes here

- Skills that aren't part of the HyperFrames bundle
- Custom skills we build ourselves
- Third-party skills we trust and want to share across projects

Examples of skills that might live here:
- **video-analyzer** — view and break down videos (great for competitor research)
- **brand-extractor** — sample colors and fonts from a reference image
- **script-doctor** — review and tighten a voiceover script
- **stock-finder** — search a stock library for matching b-roll

## Naming convention

One folder per skill. Inside each folder:
```
skills/<skill-name>/
├── SKILL.md          ← the actual skill definition (instructions for the AI)
├── README.md         ← human notes about what it does and when to use it
└── [any helper files the skill needs]
```

## How to make a skill available to a project

Two options:

**Option A (simple, for one project):** Copy or symlink the skill folder into the project's `.agents/skills/`:
```bash
ln -s ~/Desktop/hyperframes/skills/video-analyzer \
      ~/Desktop/hyperframes/my-projects/my-project/.agents/skills/video-analyzer
```

**Option B (workspace-wide):** When starting a Claude / Cursor session, just point the agent at the workspace root — it can read SKILL.md files from anywhere it has access.

## Current skills

_None yet. The first one (video analysis for competitor research) is on its way._
