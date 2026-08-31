#!/usr/bin/env python3
"""
Session-start briefing for the ocho-frames workspace.

The mirror image of scripts/archive_memory.py + the /close-out command:
close-out writes the state, startup reads it back.

Run at the top of EVERY session, in either environment:

    python3 scripts/startup.py

Prints, in one pass: which environment this is, the next session number,
git state (with a loud warning if the tree is dirty), the CURRENT STATE
block, open loops for the active client, the files that must be read
before writing content, the house rules, and any stale-file flags.

Options:
    --client NAME   override the auto-detected active client
    --short         skip the CURRENT STATE block (state you already know)
"""

import argparse
import datetime as dt
import os
import re
import subprocess
import sys
from pathlib import Path

# --- workspace timezone -----------------------------------------------------
# The Cowork container runs on UTC. Sydney is UTC+10, so any session before
# 10am local sees YESTERDAY if we use the machine's date. That broke the
# pre-push hook and the close-out date check on 2026-09-01. Pin it.
WORKSPACE_TZ = "Australia/Sydney"


def today_local():
    from zoneinfo import ZoneInfo
    import datetime as _dt
    return _dt.datetime.now(ZoneInfo(WORKSPACE_TZ)).date()
# ----------------------------------------------------------------------------


ROOT = Path(__file__).resolve().parent.parent

# Files that must be read before writing any client-facing content.
CONTENT_GATE = ["brand.md", "voice-guidelines.md"]

# Anything older than this many days without a session is worth flagging.
STALE_DAYS = 14

HOUSE_RULES = [
    "NO em dashes and NO en dashes, anywhere. Commas, full stops, brackets.",
    "Anything Hugo ACTS on: heading, then ONE complete self-contained paste block,",
    "  then inputs as bullets. Analysis goes at the END, a few bullets, never woven in.",
    "Generated media -> clients/<client>/generated/. Keeper prompts -> image-prompts.md.",
    "Secrets live in .env only. Never a real key in .env.example, never committed.",
    "Ask for project context before assuming. Flag trade-offs, do not pick silently.",
]


def rule(title=""):
    if title:
        return "\n" + "-" * 66 + "\n  " + title + "\n" + "-" * 66
    return "-" * 66


def sh(cmd):
    try:
        return subprocess.run(
            cmd, cwd=ROOT, shell=True, capture_output=True, text=True, timeout=30
        ).stdout.rstrip()
    except Exception as exc:
        return f"(could not run: {exc})"


def detect_environment():
    """Cowork sandbox paths look like /sessions/<id>/mnt/... ; the Mac is /Users/..."""
    p = str(ROOT)
    if p.startswith("/Users/"):
        return "Claude Code", "Mac, full shell, background jobs survive, local fonts, rm works"
    if "/mnt/" in p or p.startswith("/sessions/"):
        return "Cowork", "sandboxed Linux, ~45s per call, no background jobs, rm blocked in the mount"
    return "Unknown", "path did not match either environment, check before trusting handoff notes"


def read(path):
    f = ROOT / path
    return f.read_text(encoding="utf-8", errors="replace") if f.exists() else ""


def active_client(override=None):
    if override:
        return override
    m = re.search(r"^- Client: \*\*(.+?)\*\*", read("CLAUDE.md"), re.M)
    return m.group(1).strip() if m else None


def last_session(memory):
    """Returns (number, date, environment) of the most recent logged session."""
    m = re.search(r"^## Session (\d+)\s*\(([^,]+),\s*([^)]+)\)", memory, re.M)
    if not m:
        return None, None, None
    return int(m.group(1)), m.group(2).strip(), m.group(3).strip()


def current_state(memory):
    m = re.search(r"^## CURRENT STATE.*?$(.*?)(?=^---\s*$)", memory, re.M | re.S)
    return m.group(1).strip() if m else "(CURRENT STATE block not found in memory.md)"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--client")
    ap.add_argument("--short", action="store_true")
    args = ap.parse_args()

    memory = read("memory.md")
    env, env_note = detect_environment()
    client = active_client(args.client)
    num, date, senv = last_session(memory)
    today = today_local()

    print("=" * 66)
    print("  OCHO-FRAMES :: SESSION START")
    print("=" * 66)
    print(f"  Today        : {today.isoformat()} ({today.strftime('%A')})")
    print(f"  Environment  : {env}")
    print(f"                 {env_note}")
    print(f"  Active client: {client or '(none set in CLAUDE.md)'}")
    if num:
        print(f"  Last session : {num} ({date}, {senv})")
        print(f"  THIS SESSION : {num + 1}   <- use this number at close-out")
    else:
        print("  Last session : (none found in memory.md)")

    # ---------------- git ----------------
    print(rule("GIT (what the other environment did last)"))
    print(sh("git log --oneline -5") or "(no commits)")
    dirty = sh("git status --short")
    print()
    if dirty:
        print("  ** WORKING TREE IS DIRTY **")
        print("  A session somewhere did not close out. Commit or flag before working.")
        print()
        print(dirty)
    else:
        print("  Working tree: clean.")
    ahead = sh("git rev-list --count @{u}..HEAD 2>/dev/null")
    if ahead.isdigit() and int(ahead) > 0:
        print(f"\n  {ahead} commit(s) ahead of the remote. Push at close-out (Claude Code only).")

    # ---------------- current state ----------------
    if not args.short:
        print(rule("CURRENT STATE (memory.md)"))
        print(current_state(memory))

    # ---------------- open loops ----------------
    if client:
        print(rule(f"OPEN LOOPS ({client})"))
        out = sh(f'python3 scripts/memory_tools.py open --client "{client}"')
        print(out or "(none, or memory_tools.py is unavailable)")

    # ---------------- content gate ----------------
    if client:
        cdir = Path("clients") / client.lower()
        print(rule("READ THESE BEFORE WRITING ANY CONTENT"))
        for name in CONTENT_GATE:
            target = cdir / name
            mark = "ok  " if (ROOT / target).exists() else "MISSING"
            print(f"  [{mark}] {target}")
        for note in ("RESUME-NOTE.md", "intake/RESEARCH-RUN-STATUS.md"):
            if (ROOT / cdir / note).exists():
                print(f"  [note] {cdir / note}")

    # ---------------- house rules ----------------
    print(rule("HOUSE RULES (CLAUDE.md, non-negotiable)"))
    for r in HOUSE_RULES:
        print(f"  {r}" if r.startswith("  ") else f"  - {r}")

    # ---------------- flags ----------------
    flags = []
    if date:
        try:
            gap = (today - dt.date.fromisoformat(date)).days
            if gap >= STALE_DAYS:
                flags.append(f"{gap} days since the last logged session. Re-read CURRENT STATE properly, do not skim.")
        except ValueError:
            pass
    if client:
        rn = ROOT / "clients" / client.lower() / "RESUME-NOTE.md"
        if rn.exists() and num:
            m = re.search(r"Session (\d+)", rn.read_text(encoding="utf-8", errors="replace"))
            if m and int(m.group(1)) < num - 2:
                flags.append(f"RESUME-NOTE.md still describes Session {m.group(1)} (we are on {num}). Stale, rewrite or delete.")
    if not (ROOT / ".env").exists():
        flags.append("No .env in the workspace root. API-backed scripts will fail.")

    # S031/S033: Cowork commits cannot unlink inside the mount, so they leave
    # stale locks and tmp_obj files behind. git then wrongly claims another
    # process is running, and git gc fails.
    git_dir = ROOT / ".git"
    locks = sorted(git_dir.glob("*.lock")) if git_dir.exists() else []
    tmp_objs = list(git_dir.glob("objects/*/tmp_obj_*")) if git_dir.exists() else []
    if locks:
        names = ", ".join(f".git/{p.name}" for p in locks)
        flags.append(f"Stale git lock(s): {names}. A previous Cowork commit could not clean up.")
        if env == "Cowork":
            flags.append("  Clear them here with: mkdir -p .git/_stale_locks && mv -f .git/*.lock .git/_stale_locks/")
        else:
            flags.append("  Clear them here with: rm -f .git/*.lock && git gc --prune=now")
    if tmp_objs and env == "Claude Code":
        flags.append(f"{len(tmp_objs)} orphaned tmp_obj file(s) in .git/objects. Run: git gc --prune=now")
    if env == "Cowork":
        flags.append("Cowork: iterate images at quality low (45s cap). Render finals in Claude Code.")
        flags.append("Cowork: file DELETION needs the allow_cowork_file_delete tool. Overwrite with cp -f instead.")

    print(rule("FLAGS"))
    if flags:
        for f in flags:
            print(f"  ! {f}")
    else:
        print("  None.")

    print("\n" + "=" * 66)
    print("  Startup complete. Ask Hugo what this session is for.")
    print("=" * 66)


if __name__ == "__main__":
    sys.exit(main())
