# Generated media (Sportif)

AI-generated production media lives here, split for easy access:

- `images/` for stills (gpt-image-2)
- `videos/` for motion (Seedance or other)

## Rules

1. **Naming:** `purpose-vN-note.png`, e.g. `coming-soon-hero-v4-unboxed.png`. Version numbers never reset; a high-quality final gets `-FINAL` in the name.
2. **The prompt is the source of truth, not the file.** Every keeper image must have its prompt saved in `../image-prompts.md` so it can be regenerated or refined later. Binaries here are cheap and reproducible.
3. **Git ignores the binaries in this folder** (only this README and prompt files are tracked). Back up finals separately if they matter.
4. **Quality workflow:** iterate at `quality: low` in Cowork (fits the 45s shell cap, about 1 cent each), render finals at `quality: high` or 4K in Claude Code on the Mac (no time cap).
5. Lucy's own reference assets stay in `../assets/`, never in here. Real photography also goes in `../assets/`.
