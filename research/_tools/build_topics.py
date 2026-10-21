"""Regenerate the topic notes from the registry and the notes' `topics:` fields.

Usage, from the repo root:
    python -I -X utf8 research/_tools/build_topics.py [<notes folder>]

Reads `research/topics.md` (the registry: group headings and tables of Topic | Definition) and
every paper note in the notes folder (default research/agent_as_a_judge/notes). Then:
- rewrites each paper note's `## Topics` section to wikilinks for the topics in its `topics:` field;
- writes one `Topic - <name>.md` per registry topic, listing its papers with their one-line
  summary and the other topics each paper also carries;
- writes `Topics.md`, the overview: every topic by group with its paper count;
- removes any `Topic - *.md` whose name is no longer in the registry.
A `topics:` value that is not in the registry is reported and dropped from the links, never written.
Idempotent.
"""
import sys, os, re, io, json, collections

REGISTRY = "research/topics.md"
D = sys.argv[1] if len(sys.argv) > 1 else "research/agent_as_a_judge/notes"


def read_registry(path):
    groups = collections.OrderedDict(); group = None
    for ln in io.open(path, encoding="utf-8"):
        if ln.startswith("## ") and ln.strip() != "## How a paper gets its topics":
            group = ln[3:].strip(); groups.setdefault(group, collections.OrderedDict())
        elif group and ln.startswith("|") and not ln.startswith("| Topic") and not ln.startswith("|---"):
            cells = [c.strip() for c in ln.strip().strip("|").split("|")]
            if len(cells) >= 2 and cells[0]:
                groups[group][cells[0]] = cells[1]
    return groups


def split_fm(s):
    m = re.match(r"^---\n(.*?)\n---\n", s, re.S)
    return (m.group(1), s[m.end():]) if m else (None, s)


def fm_dict(fm):
    d = {}
    for ln in (fm or "").split("\n"):
        if ":" in ln:
            k, v = ln.split(":", 1); d[k.strip()] = v.strip()
    return d


def one_line(body):
    m = re.search(r"^## One line\s*\n(.*?)(?=\n## |\Z)", body, re.S | re.M)
    return m.group(1).strip().split("\n")[0].strip() if m else ""


def strip_topics_section(body):
    return re.sub(r"\n+## Topics\n.*?(?=\n## |\Z)", "\n", body, flags=re.S).rstrip("\n") + "\n"


groups = read_registry(REGISTRY)
definition = {t: d for g in groups.values() for t, d in g.items()}
group_of = {t: g for g, ts in groups.items() for t in ts}

notes = {}; unknown = collections.Counter()
for f in sorted(os.listdir(D)):
    if not f.endswith(".md") or f.startswith("_") or f.startswith("Topic - ") or f == "Topics.md":
        continue
    stem = f[:-3]; path = os.path.join(D, f)
    s = io.open(path, encoding="utf-8").read()
    fm, body = split_fm(s); d = fm_dict(fm)
    try:
        topics = json.loads(d["topics"]) if d.get("topics") else []
    except json.JSONDecodeError:
        topics = []
    keep = [t for t in topics if t in definition]
    for t in topics:
        if t not in definition: unknown[t] += 1
    body = strip_topics_section(body)
    if keep:
        body = body.rstrip("\n") + "\n\n## Topics\n" + " · ".join(f"[[Topic - {t}]]" for t in keep) + "\n"
    new = f"---\n{fm}\n---\n{body}" if fm is not None else body
    if new != s:
        io.open(path, "w", encoding="utf-8", newline="\n").write(new)
    notes[stem] = dict(topics=keep, line=one_line(body) or d.get("title", stem).strip('"'))

members = collections.defaultdict(list)
for stem, n in notes.items():
    for t in n["topics"]: members[t].append(stem)

for f in os.listdir(D):
    if f.startswith("Topic - ") and f.endswith(".md") and f[len("Topic - "):-3] not in definition:
        os.remove(os.path.join(D, f)); print("removed stale", f)

for t, defn in definition.items():
    rows = []
    for stem in sorted(members[t]):
        others = [o for o in notes[stem]["topics"] if o != t]
        also = (" (also: " + ", ".join(f"[[Topic - {o}]]" for o in others) + ")") if others else ""
        rows.append(f"- [[{stem}]] — {notes[stem]['line']}{also}")
    siblings = [o for o in groups[group_of[t]] if o != t]
    L = ["---", "type: topic", f"group: {group_of[t]}", "---", f"# Topic - {t}", "", defn, "",
         f"Group: {group_of[t]}. See [[Topics]]." + (" Same group: " + ", ".join(f"[[Topic - {o}]]" for o in siblings) + "." if siblings else ""),
         "", f"## Papers ({len(rows)})"] + rows + [""]
    io.open(os.path.join(D, f"Topic - {t}.md"), "w", encoding="utf-8", newline="\n").write("\n".join(L))

L = ["---", "type: topic-index", "---", "# Topics", "", f"Every topic in `research/topics.md`, with how many notes carry it. {len(notes)} notes in all.", ""]
for g, ts in groups.items():
    L += [f"## {g}"] + [f"- [[Topic - {t}]] ({len(members[t])}) — {definition[t]}" for t in ts] + [""]
io.open(os.path.join(D, "Topics.md"), "w", encoding="utf-8", newline="\n").write("\n".join(L))

print("notes:", len(notes), "| topics in registry:", len(definition))
print("papers per topic:", {t: len(members[t]) for t in definition})
print("topics per note:", dict(sorted(collections.Counter(len(n["topics"]) for n in notes.values()).items())))
if unknown: print("UNKNOWN topics dropped from links (fix the note or the registry):", dict(unknown))
