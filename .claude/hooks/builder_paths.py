"""PreToolUse hook for agent-builder. Blocks any file access outside what the builder is allowed.

Allowed to read:  agents/<agent>/agent/** except .env, main.py and base/ (base_interface.md there is the contract),
                  plus mcp/** and .claude/skills/** at the repo root.
Allowed to write: agents/<agent>/agent/src/**, agents/<agent>/agent/instructions/** and agents/<agent>/agent/requirements.txt only.
Exit 2 blocks the call; the reason on stderr is shown to the subagent.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]            # the repo root, two levels above .claude/hooks/
AGENTS = "agents"                                     # every agent folder lives under agents/
WRITABLE = {"src", "instructions"}
HIDDEN = {".env", "main.py", "base"}                 # inside <agent>/agent/, never read: the secrets and the base


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
    if len(rel) >= 5 and rel[0] == AGENTS and rel[2] == "agent" and rel[3] in WRITABLE:
        sys.exit(0)
    if len(rel) == 4 and rel[0] == AGENTS and rel[2:] == ("agent", "requirements.txt"):
        sys.exit(0)
    block(f"may only write inside agents/<agent>/agent/src/, instructions/ or requirements.txt, not {'/'.join(rel)}")

# Read, Glob, Grep
if rel and rel[0] == "mcp":
    sys.exit(0)
if len(rel) >= 2 and rel[0] == ".claude" and rel[1] == "skills":
    sys.exit(0)
if len(rel) >= 3 and rel[0] == AGENTS and rel[2] == "agent":
    if len(rel) >= 4 and rel[3] in HIDDEN:
        block(f"{rel[3]} is not yours to read; agent/base_interface.md says everything you need")
    sys.exit(0)
block(f"may only read inside agents/<agent>/agent/ (not .env, main.py, base/), mcp/ or .claude/skills/, not {'/'.join(rel)}")
