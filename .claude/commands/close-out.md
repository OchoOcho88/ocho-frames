Run the workspace close-out ritual (see "Two environments, one workspace" in CLAUDE.md):

1. Review what was done this session (check the conversation and `git status`).
2. Update the CURRENT STATE block at the top of `memory.md`: refresh the facts, and set the handoff line (date, session number, environment "Claude Code", working tree state).
3. Add a session entry at the TOP of `memory.md`, numbered continuously from the last entry, tagged `(Claude Code)`. Match the existing format: what we did, what we learned, decisions, open questions.
4. Sweep every file touched this session for em dashes and en dashes and remove them.
5. If any internal source doc changed, check its client cut for drift (see the two-doc drift rule) and re-export the PDF if needed.
6. Run `python3 scripts/archive_memory.py` (no-op under 90KB; otherwise it moves the oldest session entries to memory-archive.md).
7. `git add -A && git commit` with a descriptive "Session NNN:" message.
8. Confirm to Hugo the session is closed and what the next session should pick up.
