# Perplexity search helper

> Pointer doc. The actual helper lives at [`scripts/perplexity_search.py`](../../scripts/perplexity_search.py).

## What it is

A small Python wrapper around the Perplexity AI API for doing higher-quality market and competitor research than what raw web search returns. Powers SWOT deep-dives, competitor analyses, and segment-specific research throughout the creative-strategy pipeline.

Why it exists: WebSearch results lean heavily on SEO content (marketing blogs). Perplexity surfaces more authoritative primary sources (Statista, eMarketer, industry reports, platform docs), with synthesized answers and attached citations.

## Setup (one-time)

The Perplexity key is **project-scoped** (lives in this workspace's `.env` file, not shell-wide). This keeps the key out of other projects and processes on your Mac.

1. Get a Perplexity API key at https://www.perplexity.ai/settings/api.
2. If `.env` doesn't exist yet at the workspace root, create it by copying the template:
   ```bash
   cp .env.example .env
   ```
3. Open `.env` and add (or update) the line:
   ```
   PERPLEXITY_API_KEY=pplx-your-key-here
   ```
   (No quotes needed. No `export`. Just `KEY=VALUE`.)
4. Save. `.env` is already gitignored, so the key never leaves your Mac.

The script auto-loads `.env` from the workspace root each time it runs. Shell env vars still win if you ever want to override.

**Why project-scoped instead of `~/.zshrc`:** the video-analyzer skill (Session 003) uses `~/.zshrc` because it lives at `~/.claude/skills/` and runs from any directory. This helper lives INSIDE the workspace, so the project `.env` pattern is more appropriate and more secure.

## Usage

```bash
# Default model (sonar-pro), balanced cost and quality
python3 scripts/perplexity_search.py "what are the top Australian Pilates accessories brands in 2026"

# Fast and cheap, for quick facts
python3 scripts/perplexity_search.py "current Australian Meta CPM benchmark for fitness vertical" --model sonar

# Reasoning-heavy, for analysis
python3 scripts/perplexity_search.py "compare positioning of Bala vs Sweat Society vs Move Society" --model sonar-reasoning-pro

# Deep autonomous research (slow, expensive, thorough)
python3 scripts/perplexity_search.py "full competitor analysis of Tropeaka including positioning, content, ads, recent moves" --model sonar-deep-research

# Raw JSON output
python3 scripts/perplexity_search.py "question" --raw
```

Output goes to stdout. Progress and token usage go to stderr. Redirect with `>` to save the answer to a file:

```bash
python3 scripts/perplexity_search.py "competitor analysis prompt" > clients/sportif/competitor-analyses/perplexity-tropeaka-2026-05-28.md
```

## Models cheat sheet

| Model | Speed | Cost | Best for |
|---|---|---|---|
| `sonar` | Fast | Cheap | Quick facts, single-source questions |
| `sonar-pro` | Medium | Mid | Default. Most research tasks. |
| `sonar-reasoning-pro` | Slow | Higher | Multi-step analysis and comparison |
| `sonar-deep-research` | Slowest | Highest | Autonomous deep dives (e.g., full competitor profiles) |

For Sportif's competitor work post-Lucy: start with `sonar-pro`. Escalate to `sonar-deep-research` only for the 2 to 3 most important competitors where depth matters.

## When Claude should use this

Whenever research needs:
- Better source quality than WebSearch (Statista, eMarketer, industry reports, platform docs)
- Multi-source synthesis on a single question
- Citations attached line by line
- Australian, UK, or other localized market data

When NOT to use it (use WebSearch instead):
- Fetching a specific known URL (use `WebFetch`)
- Quick one-off lookups where a single search result suffices
- Topics already deeply covered in this workspace's existing memory

## Cost awareness

Perplexity API pricing is per-request and depends on model + token usage. `sonar-deep-research` queries can run several dollars each. Plan usage:
- Default to `sonar-pro` for most queries.
- Use `sonar-deep-research` only when the deliverable justifies it (e.g., a competitor analysis you'll act on, not curiosity).
- Cap `--max-tokens` if you only need a short answer.

## Related

- Mirrors the install pattern for the video-analyzer skill at [`../video-analyzer/README.md`](../video-analyzer/README.md).
- Referenced in [`../../docs/marketing-fundamentals.md`](../../docs/marketing-fundamentals.md) as part of the research stack.
- Will be used heavily during Sportif Phase 0 once Lucy returns her questionnaire (competitor analyses for the brands she names in Q4).
