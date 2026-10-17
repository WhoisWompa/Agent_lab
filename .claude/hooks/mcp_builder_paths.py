"""PreToolUse hook for mcp-builder. Blocks any file access outside what the MCP builder is allowed.

Allowed to read:  mcp/** and .claude/skills/**. Never any .env.
Allowed to write: mcp/<server>/** only.
Exit 2 blocks the call; the reason on stderr is shown to the subagent.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]            # the repo root, two levels above .claude/hooks/


def block(reason):
    print(f"mcp-builder: {reason}", file=sys.stderr)
    sys.exit(2)


data = json.load(sys.stdin)
tool = data.get("tool_name", "")
raw = data.get("tool_input", {}).get("file_path") or data.get("tool_input", {}).get("path")
if not raw:                                           # Glob/Grep with no path search the cwd: allow
    sys.exit(0)

try:
    rel = Path(raw).resolve().relative_to(ROOT).parts
except ValueError:
    block(f"{raw} is outside the repo")

if ".env" in rel:
    block(".env is never yours to read; secrets reach a server as files it opens at runtime")

if tool in ("Edit", "Write"):
    if len(rel) >= 3 and rel[0] == "mcp":
        sys.exit(0)
    block(f"may only write inside mcp/<server>/, not {'/'.join(rel)}")

# Read, Glob, Grep
if rel and rel[0] == "mcp":
    sys.exit(0)
if len(rel) >= 2 and rel[0] == ".claude" and rel[1] == "skills":
    sys.exit(0)
block(f"may only read inside mcp/ or .claude/skills/, not {'/'.join(rel)}")
