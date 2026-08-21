#!/usr/bin/env python3
"""
Mechanical half of the close-out ritual for the ocho-frames workspace.

The mirror of scripts/startup.py. Startup READS the state, close-out
CHECKS and WRITES it. This script does every step that can be verified
by a machine, and refuses to pass while anything is unfinished. The
judgement steps (what actually happened this session, what was decided)
stay in .claude/commands/close-out.md, where a human or an agent writes
them.

    python3 scripts/closeout.py                   # check everything, change nothing but locks and indexes
    python3 scripts/closeout.py --commit          # also git add -A and commit, if all checks pass
    python3 scripts/closeout.py --commit -m "..." # supply the commit message yourself
    python3 scripts/closeout.py --skip-dash       # bypass the dash sweep (rare, say why in the entry)

Exit code is 0 only when every check passes.
"""

import argparse
import datetime as dt
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DASHES = ("\u2014", "\u2013")   # em dash, en dash, written as escapes
                                # so this file never trips its own sweep
TEXT_SUFFIXES = {".md", ".py", ".txt", ".html", ".css", ".js", ".json", ".yml", ".yaml", ".toml", ".sh"}
SKIP_DIRS = {".git", "_archive", "node_modules", "renders", "generated", "assets",
             "__pycache__", "starter", ".agents"}   # starter/.agents are vendored HyperFrames
# Regenerated from other files, never hand-edited, so a dash in here means
# the SOURCE needs fixing, not this file. Do not block the commit on it.
SKIP_FILES = {"memory-index.md"}

results = []   # (status, label, detail) where status is PASS, FAIL or NOTE


def record(status, label, detail=""):
    results.append((status, label, detail))
    icon = {"PASS": "ok  ", "FAIL": "FAIL", "NOTE": "note"}[status]
    print(f"  [{icon}] {label}")
    if detail:
        for line in detail.rstrip().splitlines():
            print(f"         {line}")


def sh(cmd, check=False):
    r = subprocess.run(cmd, cwd=ROOT, shell=True, capture_output=True, text=True, timeout=120)
    out = (r.stdout + r.stderr).rstrip()
    return (r.returncode, out) if check else out


def detect_environment():
    p = str(ROOT)
    if p.startswith("/Users/"):
        return "Claude Code"
    if "/mnt/" in p or p.startswith("/sessions/"):
        return "Cowork"
    return "Unknown"


def read(path):
    f = ROOT / path
    return f.read_text(encoding="utf-8", errors="replace") if f.exists() else ""


# --------------------------------------------------------------------------

def step_locks(env):
    """Cowork cannot unlink inside the mount, so its commits strand lock files."""
    git_dir = ROOT / ".git"
    locks = sorted(git_dir.glob("*.lock"))
    if not locks:
        record("PASS", "No stale git locks")
        return
    if env == "Cowork":
        quarantine = git_dir / "_stale_locks"
        quarantine.mkdir(exist_ok=True)
        stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
        for lock in locks:
            try:
                lock.rename(quarantine / f"{lock.name}.{stamp}")
            except OSError as exc:
                record("FAIL", f"Could not move {lock.name}", str(exc))
                return
        record("PASS", f"Cleared {len(locks)} stale git lock(s) into .git/_stale_locks/")
    else:
        code, out = sh("rm -f .git/*.lock && git gc --prune=now", check=True)
        record("PASS" if code == 0 else "FAIL", f"Cleared {len(locks)} stale git lock(s) and ran git gc", out)


def changed_files():
    out = sh("git status --porcelain")
    paths = []
    for line in out.splitlines():
        if len(line) < 4:
            continue
        path = line[3:].strip().strip('"')
        if " -> " in path:              # renames
            path = path.split(" -> ")[-1]
        paths.append(path)
    return paths


def sweepable(rel):
    p = ROOT / rel
    if not p.is_file() or p.suffix.lower() not in TEXT_SUFFIXES:
        return None
    if any(part in SKIP_DIRS for part in p.relative_to(ROOT).parts[:-1]):
        return None
    if p.name in SKIP_FILES:
        return None
    return p


def fix_dashes_in(p):
    """Replace em and en dashes with the house punctuation. Conservative:
    a spaced dash becomes a comma, which is how they read in practice."""
    t = p.read_text(encoding="utf-8", errors="replace")
    n = sum(t.count(d) for d in DASHES)
    if not n:
        return 0
    # A dash between digits is a RANGE. "2-3 uses" must become "2 to 3 uses",
    # never "2, 3 uses" (S033).
    t = re.sub(rf"(\d)\s*[{DASHES[0]}{DASHES[1]}]\s*(\d)", r"\1 to \2", t)
    for pat, rep in ((f" {DASHES[0]} ", ", "), (f" {DASHES[1]} ", ", "),
                     (DASHES[0], ", "), (DASHES[1], ", ")):
        t = t.replace(pat, rep)
    p.write_text(t, encoding="utf-8")
    return n


def step_dashes(skip, fix=False, scope_all=False):
    if skip:
        record("NOTE", "Dash sweep SKIPPED by flag. Say why in the session entry.")
        return

    if scope_all:
        targets = sh("git ls-files").splitlines()
        label = "the whole repo"
    else:
        targets = changed_files()
        label = "files changed this session"

    hits, fixed, files_fixed = [], 0, []
    for rel in targets:
        p = sweepable(rel)
        if p is None:
            continue
        if fix:
            n = fix_dashes_in(p)
            if n:
                fixed += n
                files_fixed.append(f"{rel} ({n})")
            continue
        try:
            for i, line in enumerate(p.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
                if any(d in line for d in DASHES):
                    hits.append(f"{rel}:{i}: {line.strip()[:90]}")
        except OSError:
            continue

    if fix:
        if fixed:
            record("PASS", f"Fixed {fixed} em/en dash(es) across {len(files_fixed)} file(s) in {label}",
                   "\n".join(files_fixed[:40]))
        else:
            record("PASS", f"No em or en dashes to fix in {label}")
        return

    if hits:
        extra = f"\n... and {len(hits) - 20} more" if len(hits) > 20 else ""
        record("FAIL", f"{len(hits)} em/en dash(es) in {label}",
               "\n".join(hits[:20]) + extra + "\n\nAuto-fix with: python3 scripts/closeout.py --fix-dashes")
    else:
        record("PASS", f"No em or en dashes in {label}")


def step_memory(env):
    memory = read("memory.md")
    today = dt.date.today().isoformat()

    m = re.search(r"^## Session (\d+)\s*\(([^,]+),\s*([^)]+)\)", memory, re.M)
    if not m:
        record("FAIL", "No session entry found at the top of memory.md")
        return None
    num, date, senv = int(m.group(1)), m.group(2).strip(), m.group(3).strip()

    if date != today:
        record("FAIL", f"Top session entry is Session {num}, dated {date}, not today ({today})",
               "Add this session's entry at the TOP of memory.md before closing out.")
    else:
        record("PASS", f"Session {num} entry present and dated today")

    if senv != env:
        record("FAIL", f"Top entry is tagged ({senv}) but this is {env}", "Fix the tag on the session heading.")
    else:
        record("PASS", f"Session entry tagged ({env}) correctly")

    already = sh(f'git log --oneline -40 --grep="Session {num:03d} CLOSE-OUT"')
    if already:
        record("FAIL", f"Session {num} already closed out in a previous commit",
               f"{already.splitlines()[0]}\n"
               f"This is a NEW session. Add a Session {num + 1} entry at the top of memory.md.")

    body = memory[m.end(): m.end() + 4000]
    body = re.split(r"^## Session ", body, flags=re.M)[0]
    for field in ("Client:", "Tags:"):
        if re.search(rf"^\*?\*?{field}", body, re.M):
            record("PASS", f"Session entry has a {field.rstrip(':')} line")
        else:
            record("FAIL", f"Session entry is missing its {field.rstrip(':')} line")

    head = memory[:2000]
    if f"Last updated: {today}" in head:
        record("PASS", "CURRENT STATE block updated today")
    else:
        record("FAIL", "CURRENT STATE block was not updated today",
               "Refresh the facts and the handoff line at the top of memory.md.")
    if re.search(rf"Last session: 0*{num}\b", head):
        record("PASS", f"CURRENT STATE handoff line names Session {num}")
    else:
        record("FAIL", f"CURRENT STATE handoff line does not name Session {num}")
    return num


def step_registries(num):
    if num is None:
        return
    tag = f"S{num:03d}"
    pattern = re.compile(rf"\((?:opened |resolved )?{tag}\)")
    for name in ("DECISIONS.md", "OPEN-QUESTIONS.md"):
        if pattern.search(read(name)):
            record("PASS", f"{name} has at least one {tag} row")
        else:
            record("NOTE", f"{name} has no {tag} row",
                   "Fine if nothing was settled or opened. Add one if something was.")


def step_tools():
    out = sh("python3 scripts/archive_memory.py")
    record("PASS", "archive_memory.py run", out or "(no-op, memory.md under threshold)")

    out = sh("python3 scripts/memory_tools.py index")
    record("PASS", "memory-index.md regenerated", out)

    code, out = sh("python3 scripts/memory_tools.py check", check=True)
    record("PASS" if code == 0 else "FAIL", "memory_tools.py check", out)


def step_commit(do_commit, message, num, env, blocked):
    dirty = "\n".join(l for l in sh("git status --short").splitlines()
                      if "unable to unlink" not in l)
    if not dirty:
        record("PASS", "Working tree already clean, nothing to commit")
        return
    if not do_commit:
        record("NOTE", "Uncommitted changes present. Re-run with --commit, or commit yourself.",
               dirty[:1500])
        return
    if blocked:
        record("FAIL", "Not committing: fix the failures above first")
        return
    if not message:
        message = f"Session {num:03d} CLOSE-OUT ({env})"
    body = f"{message}\n\nCo-Authored-By: Claude Opus 5 <noreply@anthropic.com>\n"
    subprocess.run(["git", "add", "-A"], cwd=ROOT, capture_output=True)
    proc = subprocess.run(["git", "commit", "-q", "-F", "-"], cwd=ROOT,
                          input=body, text=True, capture_output=True)
    # Cowork cannot unlink inside the mount, so a successful commit still
    # prints unlink warnings. They are noise, not failure.
    noise = "\n".join(l for l in (proc.stdout + proc.stderr).splitlines()
                      if "unable to unlink" not in l)
    record("PASS" if proc.returncode == 0 else "FAIL",
           f"Committed: {message}", noise)


# --------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--commit", action="store_true", help="commit if every check passes")
    ap.add_argument("-m", "--message", help="commit subject line")
    ap.add_argument("--skip-dash", action="store_true", help="bypass the dash sweep")
    ap.add_argument("--fix-dashes", action="store_true",
                    help="replace em and en dashes with commas instead of just reporting them")
    ap.add_argument("--all-files", action="store_true",
                    help="sweep every tracked file, not only the ones changed this session")
    args = ap.parse_args()

    env = detect_environment()
    print("=" * 66)
    print("  OCHO-FRAMES :: CLOSE-OUT")
    print("=" * 66)
    print(f"  Environment: {env}")
    print(f"  Date       : {dt.date.today().isoformat()}")
    print()

    step_locks(env)
    step_dashes(args.skip_dash, args.fix_dashes, args.all_files)
    num = step_memory(env)
    step_registries(num)
    step_tools()

    blocked = any(s == "FAIL" for s, _, _ in results)
    step_commit(args.commit, args.message, num, env, blocked)

    fails = [l for s, l, _ in results if s == "FAIL"]
    print("\n" + "=" * 66)
    if fails:
        print(f"  NOT CLOSED. {len(fails)} thing(s) to fix:")
        for f in fails:
            print(f"    - {f}")
    else:
        print("  CLOSE-OUT CLEAN.")
        if env == "Claude Code":
            print("  Remember to git push so the other environment can see it.")
        else:
            print("  Cowork cannot push reliably. Push from the Mac next session.")
    print("=" * 66)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
