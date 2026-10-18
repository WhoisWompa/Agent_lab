"""Keep this laptop and GitHub in step. Run by the SessionStart and SessionEnd hooks in .claude/settings.local.json.

    python git_sync.py start|end [--dry-run]

1. Commit anything uncommitted, as "sync: <start|end> of session <time>".
2. Fetch origin and compare main with origin/main:
   same          nothing to do
   GitHub ahead  pull (fast-forward only)
   laptop ahead  push
   both changed  stop and say so; a human settles it
Offline or not on main: say so and do nothing. Never exits non-zero, so a session always opens.
"""
import json
import os
import subprocess
import sys
from datetime import datetime

BRANCH = "main"
ROOT = os.path.dirname(os.path.abspath(__file__))


def git(*args, check=True):
    r = subprocess.run(["git", *args], capture_output=True, text=True, cwd=ROOT)
    if check and r.returncode:
        raise RuntimeError(f"git {' '.join(args)}: {r.stderr.strip() or r.stdout.strip()}")
    return r.stdout.strip()


def sync(when, dry_run):
    """One line saying what happened."""
    if git("rev-parse", "--abbrev-ref", "HEAD") != BRANCH:
        return f"not on {BRANCH}, no sync"
    if git("status", "--porcelain"):
        if dry_run:
            return "would commit the uncommitted changes, then compare with GitHub"
        git("add", "-A")
        git("commit", "-q", "-m", f"sync: {when} of session {datetime.now():%Y-%m-%d %H:%M}")
    r = subprocess.run(["git", "fetch", "-q", "origin", BRANCH], capture_output=True, text=True, cwd=ROOT, timeout=30)
    if r.returncode:
        return "GitHub unreachable, no sync"
    local, remote = git("rev-parse", BRANCH), git("rev-parse", f"origin/{BRANCH}")
    base = git("merge-base", BRANCH, f"origin/{BRANCH}")
    if local == remote:
        return "laptop and GitHub match"
    if local == base:
        n = git("rev-list", "--count", f"{BRANCH}..origin/{BRANCH}")
        if not dry_run:
            git("pull", "-q", "--ff-only", "origin", BRANCH)
        return f"{'would pull' if dry_run else 'pulled'} {n} commit(s) from GitHub"
    if remote == base:
        n = git("rev-list", "--count", f"origin/{BRANCH}..{BRANCH}")
        if not dry_run:
            git("push", "-q", "origin", BRANCH)
        return f"{'would push' if dry_run else 'pushed'} {n} commit(s) to GitHub"
    return "laptop and GitHub both changed since they last agreed: nothing pulled or pushed, merge by hand"


if __name__ == "__main__":
    when = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("-") else "start"
    dry_run = "--dry-run" in sys.argv
    try:
        line = sync(when, dry_run)
    except Exception as e:                       # a failed git step: report it, never block the session
        line = f"sync failed: {e}"
    out = {"systemMessage": f"git sync: {line}"}
    if when == "start":
        out["hookSpecificOutput"] = {"hookEventName": "SessionStart", "additionalContext": f"git sync at session start: {line}"}
    print(json.dumps(out))
