"""PreToolUse hook for agent-builder. Blocks any file access outside what the builder is allowed.

Allowed to read:  agents/<agent>/src/**, agents/<agent>/base/base_interface.md, agents/<agent>/base_settings.json,
                  agents/<agent>/README.md, agents/<agent>/data/** and logs/**, plus mcp/** and .claude/skills/** at the repo root.
                  Never .env, never the rest of base/, never handoff.md or tests/.
Allowed to write: agents/<agent>/src/** only (code, instructions/, requirements.txt and README.md all live there).
Exit 2 blocks the call; the reason on stderr is shown to the subagent.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]            # the repo root, two levels above .claude/hooks/
AGENTS = "agents"                                     # every agent folder lives under agents/
READABLE = {"src", "base_settings.json", "README.md", "data", "logs"}   # inside agents/<agent>/
CONTRACT = ("base", "base_interface.md")              # the one file inside base/ the builder reads


def block(reason):
    print(f"agent-builder: {reason}", file=sys.stderr)
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

if tool in ("Edit", "Write"):
    if len(rel) >= 4 and rel[0] == AGENTS and rel[2] == "src":
        sys.exit(0)
    block(f"may only write inside agents/<agent>/src/, not {'/'.join(rel)}")

# Read, Glob, Grep
if rel and rel[0] == "mcp":
    sys.exit(0)
if len(rel) >= 2 and rel[0] == ".claude" and rel[1] == "skills":
    sys.exit(0)
if len(rel) >= 3 and rel[0] == AGENTS:
    if rel[2] in READABLE or rel[2:4] == CONTRACT:
        sys.exit(0)
    if rel[2] == ".env":
        block(".env is not yours to read; the brief names the variable and the base loads it into os.environ")
    if rel[2] == "base":
        block("base/ is not yours to read; base/base_interface.md says everything you need")
block(f"may only read inside agents/<agent>/src/, base_settings.json, base/base_interface.md, data/, logs/, mcp/ or .claude/skills/, not {'/'.join(rel)}")
