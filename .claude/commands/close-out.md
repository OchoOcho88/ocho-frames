Run the workspace close-out ritual (see "Two environments, one workspace" in CLAUDE.md). The commit is what makes this session visible to the other environment, so nothing is finished until it lands.

Do the writing first, then let the script check it.

**1. Write the session entry.** Add it at the TOP of `memory.md`, numbered one above the last entry, tagged with the environment you are actually in (`Cowork` or `Claude Code`, whichever `python3 scripts/startup.py` reported). Match the existing format and include a `Client:` line (client name, or `Ochoproductions` for workspace-wide) and a `Tags:` line. Cover what was done, what was learned, what was decided, what is still open.

**2. Refresh the CURRENT STATE block** at the top of `memory.md`: update the facts and the handoff line (date, session number, environment, working tree state). Keep it to about 12 lines. Anything that has settled belongs in `DECISIONS.md`, not here.

**3. Mirror into the registries.** New settled decisions go in `DECISIONS.md`, new or resolved open loops in `OPEN-QUESTIONS.md`. The row schema is at the top of each file.

**4. Check the two-doc drift rule.** If an internal source doc changed, update its client cut and re-export the PDF.

**5. Run the checker:**

```
python3 scripts/closeout.py --commit -m "Session NNN: what happened"
```

It clears stale git locks the right way for this environment, sweeps every changed file for em and en dashes, verifies the session entry exists with the right number, date, environment tag, `Client:` and `Tags:` lines, verifies the CURRENT STATE block was updated today and names this session, checks the registries for rows from this session, runs `archive_memory.py` and `memory_tools.py index`, runs `memory_tools.py check`, and only then commits. It will refuse to commit while anything is failing. Fix what it reports and run it again.

Drop `--commit` to check without committing.

**6. Tell Hugo** the session is closed, what the next session should pick up first, and anything the checker warned about but did not block on.

Notes:
- In Claude Code, `git push` after this so the Mac and GitHub agree. Cowork cannot push reliably.
- This is the mirror of `/startup`. Startup reads the state back out, so if startup ever comes up empty, close-out did not run properly.
