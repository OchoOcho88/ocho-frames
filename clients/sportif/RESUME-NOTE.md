# Resume note

This file used to hold a hand-written session-start briefing. It went stale (it still described Session 013 four months later), which is exactly the failure a hand-maintained note invites.

It has been replaced by a command that reads the live state instead of remembering an old one.

## Start every session with this

```
python3 scripts/startup.py
```

- In Claude Code the same thing is `/startup`
- `--short` skips the CURRENT STATE block when you already have it
- `--client NAME` overrides the client auto-detected from CLAUDE.md

That prints the environment, this session's number, the last five commits, a dirty-tree warning, the CURRENT STATE block, open loops for the active client, the two files that gate content work, the house rules and any flags. It is read-only, so it is always safe to run.

Close the session with `python3 scripts/closeout.py --commit -m "Session NNN: ..."` (`/close-out` in Claude Code).

Settled in S033, see D-035.
