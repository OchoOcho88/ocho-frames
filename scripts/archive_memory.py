#!/usr/bin/env python3
"""
archive_memory.py: keeps memory.md light by moving old session entries
into memory-archive.md once the file crosses a size threshold.

Policy:
- CURRENT STATE, all Weekly Reviews, and the Session NNN template always stay.
- The newest KEEP_SESSIONS session entries stay.
- Older session entries move to memory-archive.md (newest batch on top).
- Below THRESHOLD bytes the script is a no-op, so it is safe to run at
  every close-out in either environment (Claude Code or Cowork).

Usage:
  python3 scripts/archive_memory.py            # archive if over threshold
  python3 scripts/archive_memory.py --dry-run  # show what would move
  python3 scripts/archive_memory.py --force    # archive even under threshold
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MEM = ROOT / "memory.md"
ARC = ROOT / "memory-archive.md"
THRESHOLD = 90_000   # bytes; ~90KB keeps plenty of recent context
KEEP_SESSIONS = 6    # newest session entries that always stay

ARCHIVE_HEADER = """# Workspace Memory Archive

Older session entries moved out of memory.md to keep it light.
Same format, same rules, nothing deleted. Newest archived batch at the top.
Weekly Reviews (the summaries) stay in memory.md permanently.

---

"""


def main() -> None:
    dry = "--dry-run" in sys.argv
    force = "--force" in sys.argv

    text = MEM.read_text(encoding="utf-8")
    size = len(text.encode("utf-8"))
    if size < THRESHOLD and not force:
        print(f"memory.md is {size:,} bytes, under the {THRESHOLD:,} threshold. Nothing to do.")
        return

    heads = list(re.finditer(r"(?m)^## ", text))
    if not heads:
        print("No entries found, nothing to do.")
        return

    preamble = text[: heads[0].start()]
    entries = []
    for i, m in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        entries.append(text[m.start():end])

    kept, moved = [], []
    sessions_seen = 0
    for e in entries:
        first_line = e.splitlines()[0]
        is_session = first_line.startswith("## Session") and "Session NNN" not in first_line
        if is_session:
            sessions_seen += 1
            (kept if sessions_seen <= KEEP_SESSIONS else moved).append(e)
        else:
            kept.append(e)

    if not moved:
        print("Nothing old enough to archive (all sessions within the keep window).")
        return

    labels = [e.splitlines()[0].removeprefix("## ").strip() for e in moved]
    print(f"Archiving {len(moved)} session entries:")
    for l in labels:
        print(f"  - {l}")
    if dry:
        print("Dry run, no files changed.")
        return

    batch = "".join(moved)
    if not batch.endswith("\n"):
        batch += "\n"
    stamp = f"<!-- archived batch, moved {__import__('datetime').date.today().isoformat()} -->\n\n"

    if ARC.exists():
        old = ARC.read_text(encoding="utf-8")
        if old.startswith(ARCHIVE_HEADER):
            body = old[len(ARCHIVE_HEADER):]
        else:
            body = old
        ARC.write_text(ARCHIVE_HEADER + stamp + batch + body, encoding="utf-8")
    else:
        ARC.write_text(ARCHIVE_HEADER + stamp + batch, encoding="utf-8")

    new_mem = preamble + "".join(kept)
    MEM.write_text(new_mem, encoding="utf-8")

    print(f"memory.md: {size:,} -> {len(new_mem.encode('utf-8')):,} bytes")
    print(f"memory-archive.md updated ({ARC.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
