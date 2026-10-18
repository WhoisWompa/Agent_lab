"""Carry the base from agent_template/base/ into every agent under agents/.

    python sync.py            overwrite agents/<name>/base/ with the template's base/, for every agent
    python sync.py --check    only say which agents differ from the template; write nothing

base/ is the only folder the template owns inside an agent. Everything else in an agent
folder (src/, base_settings.json, .env, data/, logs/, handoff.md) is the agent's and is never touched.
"""
import filecmp
import os
import shutil
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(ROOT, "agent_template", "base")
AGENTS = os.path.join(ROOT, "agents")
SKIP = shutil.ignore_patterns("__pycache__", "*.pyc")


def differs(a, b):
    """True if the two folders differ in any file, ignoring caches."""
    if not os.path.isdir(b):
        return True
    cmp = filecmp.dircmp(a, b, ignore=["__pycache__"])
    if cmp.left_only or cmp.right_only or cmp.diff_files or cmp.funny_files:
        return True
    return any(differs(os.path.join(a, d), os.path.join(b, d)) for d in cmp.common_dirs)


def main(check):
    agents = sorted(d for d in os.listdir(AGENTS) if os.path.isdir(os.path.join(AGENTS, d)))
    stale = []
    for name in agents:
        target = os.path.join(AGENTS, name, "base")
        if not differs(TEMPLATE, target):
            print(f"{name}: up to date")
            continue
        stale.append(name)
        if check:
            print(f"{name}: differs from the template")
            continue
        if os.path.isdir(target):
            shutil.rmtree(target)
        shutil.copytree(TEMPLATE, target, ignore=SKIP)
        print(f"{name}: base/ replaced")
    return 1 if (check and stale) else 0


if __name__ == "__main__":
    sys.exit(main(check="--check" in sys.argv[1:]))
