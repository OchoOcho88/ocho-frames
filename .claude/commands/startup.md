Run the workspace session-start protocol (see "Two environments, one workspace" in CLAUDE.md). Do this BEFORE any other work, every session, no exceptions.

1. Run `python3 scripts/startup.py`. It prints the environment, this session's number, git state, the CURRENT STATE block, open loops for the active client, the content gate, the house rules and any flags. Read all of it.
2. If it reports the working tree is DIRTY, stop and tell Hugo before touching anything. A session somewhere did not close out.
3. If it raises any FLAGS, surface them to Hugo in your first message. Do not silently absorb them.
4. Read the top session entry in `memory.md` (the one numbered below THIS SESSION) for the detail the CURRENT STATE block compresses.
5. If this session will produce any client-facing content, read the two files under the content gate now: `clients/<client>/brand.md` and `clients/<client>/voice-guidelines.md`. Do not write a word of content first.
6. Give Hugo a short briefing: what the last session left, what is flagged as first up, what else is waiting. Then ask what this session is for. Do not pick for him.

Notes:
- The script is read-only. It changes nothing, so it is always safe to run.
- `--short` skips the CURRENT STATE block when you already have it in context.
- `--client NAME` overrides the client auto-detected from CLAUDE.md.
- This is the mirror of `/close-out`. Close-out writes the state, startup reads it back. If startup ever comes up empty, the previous session did not close out properly.
