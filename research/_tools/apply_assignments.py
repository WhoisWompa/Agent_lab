"""Write topic assignments from classifier JSON into the notes' frontmatter.

Usage, from the repo root:
    python -I -X utf8 research/_tools/apply_assignments.py <out.json> [<out.json> ...]

Each JSON is {"assignments": [{"note": <stem>, "topics": [<name>, ...]}], "proposals": [...]}.
For each assignment the note's `topics:` line is replaced, or added after the last of
`category:` / `pdf:` / `folder:`, with the given list, keeping only names in research/topics.md.
Proposals are printed, never applied: the main session decides on them. Then run build_topics.py.
"""
import sys, os, re, io, json, collections

D = "research/agent_as_a_judge/notes"
REGISTRY = "research/topics.md"


def registry_names(path):
    names = set(); in_table = False
    for ln in io.open(path, encoding="utf-8"):
        if ln.startswith("| Topic"): in_table = True; continue
        if in_table and ln.startswith("|") and not ln.startswith("|---"):
            names.add(ln.strip().strip("|").split("|")[0].strip())
        elif not ln.startswith("|"): in_table = False
    return names


valid = registry_names(REGISTRY)
assigned = {}; proposals = []; dropped = collections.Counter()
for p in sys.argv[1:]:
    d = json.load(io.open(p, encoding="utf-8"))
    for a in d.get("assignments", []):
        keep = [t for t in a["topics"] if t in valid]
        for t in a["topics"]:
            if t not in valid: dropped[t] += 1
        assigned[a["note"]] = keep
    proposals += d.get("proposals", [])

written = 0; missing = []
for stem, topics in assigned.items():
    path = os.path.join(D, stem + ".md")
    if not os.path.exists(path): missing.append(stem); continue
    s = io.open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", s, re.S)
    if not m: missing.append(stem + " (no frontmatter)"); continue
    lines = m.group(1).split("\n"); line = f"topics: {json.dumps(topics)}"
    if any(ln.startswith("topics:") for ln in lines):
        lines = [line if ln.startswith("topics:") else ln for ln in lines]
    else:
        anchor = max([i for i, ln in enumerate(lines) if ln.split(":")[0] in ("category", "pdf", "folder")] or [len(lines) - 1])
        lines.insert(anchor + 1, line)
    new = "---\n" + "\n".join(lines) + "\n---\n" + s[m.end():]
    if new != s:
        io.open(path, "w", encoding="utf-8", newline="\n").write(new); written += 1

print(f"assignments: {len(assigned)} | notes rewritten: {written} | empty topic lists: {sum(1 for t in assigned.values() if not t)}")
if dropped: print("dropped names not in registry:", dict(dropped))
if missing: print("notes not found:", missing)
print(f"proposals: {len(proposals)}")
for pr in proposals:
    print(f"  - {pr.get('note')}: NEW '{pr.get('name')}' — {pr.get('definition')}\n      why none fit: {pr.get('why_none_fit')}")
