# Purpose of this project

This project main focus is building **agent architectures**: Python programs that run as a process.

# Workflow

The main session is the second voice: the user brings ideas, the session
pushes back, and designs take shape in the conversation. Two teams are
called from the main session, never on their own initiative.

The user leads. The session answers what is asked, pushes back where it
disagrees, and offers an idea when it has one. It does not set direction:
no plans, no step lists, no "what I need from you", no next-steps closing.
The only writes allowed on `.env` are the ones `provider.py` makes on the
user's word: appending a blank key name when a provider is added, removing
the key's line when it is removed. The user fills the value.

## Discussion

The default mode. Ideas, designs and implementations are talked through.
Nothing is spawned.

## Building team

Called once a direction is picked or an idea is worth trying out. The
builder gets one narrow brief for one idea and implements it in the real
agent folder. Before the builder is called, the main session shows the user the
files, the function signatures and their docstrings with the `Returns:` section,
and the reason for the split; the builder is called only once the user agrees,
and writes the bodies under those exact signatures. It never builds an agent end to end. The same goes for an MCP server:
the main session shows the tools, their arguments and their outputs, and the
`mcp-builder` writes `mcp/<name>/` once the user agrees. Both builders follow
the `one-job-per-file` skill. The main session runs
the result; what happens feeds back into discussion. Git discards what
did not work.

## Stale review

Called by the main session after every builder pass, with the builder's
report. The `stale-reviewer` reads only the files that report names, greps the
folder for what references them, and reads only the files that do. Within that
neighbourhood it removes what nothing uses: a function nothing calls, a file
nothing imports, a prompt nothing reads, a package nothing imports, a settings
key nothing reads, a README row for a file that is gone, a docstring or comment
describing behaviour that no longer exists. A file or folder the brief
deliberately left blank is named in the reviewer's brief and is not stale. For
each file it reads it also says in one line what the file does; if that line
needs "and", it reports the file as two jobs and does not split it, since a
split changes the tree and the tree is agreed in discussion. It reports what it
removed and what it flagged; the main session relays that. It adds nothing,
changes no behaviour, and never reads beyond the neighbourhood.

## Paper team

Called when PDFs need notes: the user says so, or a research run has
downloaded papers. The main session invokes the `paper-ingest` skill, which
spawns one `paper-reader` per paper, five at a time. The reader writes the
note and picks its topics from `research/topics.md`, the one registry. A paper
carries every topic whose definition it satisfies; the definition decides, not
the folder the PDF sits in.

Topics are classified by this rule. The reader proposes a new topic if and
only if no topic in the registry fits the paper. The main session then reads
the whole registry and decides: if an existing topic fits, it tells the reader
`use <names>`; if the proposal names a real gap, it adds the row (name,
one-sentence definition, right group) and tells the reader `added <name>`.
Readers never edit the registry, and the main session never adds a topic
without a proposal. When a topic is added mid-run, the notes already classified
are swept for it before the run is reported. After the run, `build_topics.py`
regenerates the topic notes and the graph is rebuilt.

# Rules that must be followed during the session

`list_of_agents.md` is one table with two columns:

| Column | What goes in it |
|---|---|
| **Agent** | The folder name. |
| **Description** | Two to four sentences: what the agent does, what it works with (e.g. email, a calendar, a folder of files, a specific API), and what it produces. Just enough that when the user describes a change in plain words, the right agent can be picked out or the list narrowed to two or three. It is an identification aid, not documentation. |

Every agent lives in its own folder under `agents/`, one folder per agent. `list_of_agents.md` is at the root so a session can find the right agent without opening every folder.

At the start of session:

1. Read `list_of_agents.md`.
2. If the user's opening message clearly indicates which agent in the table, start on it. Do not ask.
3. Otherwise, match what the user describes against the Description column. If one agent clearly fits, confirm it in a line and proceed. If several could fit, offer those candidates plus "new agent" and let the user choose.

**Stale means gone.** This holds for code, prompts, docstrings, `handoff.md`, this file, the skills and the agent definitions. Anything out of date is removed or rewritten, never marked. No "this rule is stale", no "deprecated", no commented-out code, no "kept for reference". A stale line costs context on every read and says nothing true.

While building the source code:
1. Inside an agent, `base/` is the base. It is read-only, never edited, for any reason: it is a copy of `agent_template/base/`, and `sync.py` overwrites it. The builder writes only `src/`.
2. Code under `src/` has two shapes, and each tells one thing. The graph is the agent in time; the file tree is the agent in parts. Reading the node names in order and the folder and file names should be enough to know what the agent does. Opening a file is only for seeing how one thing is done.
   - **Depth is dependency.** The more foundational a piece of code, the closer to the root of `src/` it sits. A root file imports nothing of ours. A folder imports root files and nothing beside it.
   - **Closed form.** A function is complete where it stands. One job is never scattered over several files.
   - **A family is a folder.** Parts that only make sense together live in one folder. Two different jobs are two folders.
   - **The graph is the flow.** On LangGraph, one node per step of the agent's reasoning: each check, decision and action, named in the agent's own words, so a trace says which step broke. A decision is a node too. A step made of smaller steps is a subgraph. Steps live in `flow/`, one file per step and one folder per subgraph; their bodies call the families, which do the work and are never nodes.
   - **The two axes run opposite ways.** Going deeper in `flow/` is zooming into a step; going deeper in a family is going from shared to specific. The flow imports down into its subgraphs and across into the families; the families import up toward the root; nothing imports `flow/`.

   The tree grows one agreed piece at a time. The main session shows names and places only for what the discussion has settled; what has not been discussed is blank, a name at most, never a body, a signature or a guessed behaviour.

## Keeping the table up to date.

The summary describes the agent in high level overview. It should contain enough that anyone reading it knows what the agent does, without technical detail.

**If the agent direction changes, always show the new proposed summary to the user before writing it to `list_of_agents.md`.**

## Creating a new agent

1. Before drafting, the session asks whatever it needs to get the big picture of what the agent is supposed to do. The aim is a summary detailed enough that a future session reading `list_of_agents.md` can tell this agent apart from every other one. Questions about the idea only, never about how to build it or what the session needs. Then it drafts the row (folder name and summary) and shows it, with one more question: which provider, which models, and which `.env` variable name the agent's first key goes under. If the user doesnt provide a name, give some options for the user to choose from, or tell the user to enter its own preferred name.
2. The user edits or agrees. Redraft until agreed. Nothing is written before.
3. On agreement: add the row to `list_of_agents.md`, copy `agent_template/` to `agents/<name>/`, create an empty `.env` there (no `.env` is tracked, so the copy will not have one), run `provider.py add` for the first provider, and set the matching `langchain-<provider>` package in `src/requirements.txt`.
4. Report that the folder exists and which key name is blank in `.env`, in a line, and stop. No plan, no open questions, no suggestion of what to build first. The user says what comes next.
5. Never read `.env`.

## Changing the base

A change to the base is made in `agent_template/base/` only, then carried into every agent with `python sync.py` at the repo root. `python sync.py --check` says which agents are behind without writing. A base change must never make an agent's existing `base_settings.json` or `.env` invalid without a startup message that names what to fix.

## Providers and keys

A provider is one key and the models it serves: a block in the agent's `base_settings.json` plus one `KEY=` line in its `.env`, joined by the variable name in the block's `key`. An agent has any number of them; the template has none. They are added and removed only with `provider.py` at the repo root, on the user's word:

```
python provider.py add <agent> <label> --provider <pkg> --base-url <url> --key <ENV_VAR> --models <name> [<name> ...]
python provider.py remove <agent> <label>
```

`add` writes the block and appends the blank line; the user fills the value. `remove` deletes both. The script prints variable names, never values. A model name belongs to exactly one provider in an agent; the base refuses to start otherwise. There is no default model: `src/` always calls `self.model("<name>")`.

## Repo layout

| Path | What it is |
|---|---|
| `agents/<agent-name>/` | One folder per agent. `agents/` holds nothing else. Contents in the next table. |
| `agent_template/` | The blank agent folder. Copied and renamed to start every new agent. Its `base/` is the one place the base is edited. |
| `list_of_agents.md` | The index of agents. |
| `sync.py` | Copies `agent_template/base/` into every agent's `base/`. `--check` only reports. |
| `provider.py` | Adds or removes a provider in one agent: the settings block and the `.env` line together. |
| `git_sync.py` | Commits, then pulls or pushes so the laptop and GitHub match. Run by the session hooks; see **Commits**. |
| `mcp/` | Shared MCP servers that agents may list in their `base_settings.json`. |
| `scenarios/` | The pool the `examiner` writes and the `judge` reads: one folder per target agent, one file per scenario, the judge's results beside them. Vetted by the user, so tracked. |
| `research/` | Paper corpora: one folder per topic area, each with `notes/` (one note per paper, in `_TEMPLATE.md`'s shape, with `topics:` from the registry). `research/topics.md` is the topic registry; `research/_tools/` is the ingest pipeline. The graphify graph over all of it lives in `graphify-out/` at the root, gitignored, rebuilt with `graphify update . --force`. |
| `.claude/agents/` | Subagents. `agent-builder` writes an agent's logic from a brief; `mcp-builder` writes an MCP server in `mcp/<name>/` from a brief; `stale-reviewer` removes what nothing uses from the neighbourhood of a builder's change. `research-searcher`, `research-reader`, `research-librarian` and `deep-reader` are the deep-read team, spawned by the deep-read workflow only. `paper-reader` writes one paper's note from its extracted text and picks its topics from `research/topics.md`, spawned by the `paper-ingest` skill. |
| `.claude/hooks/` | `builder_paths.py` enforces the read and write limits of `agent-builder` and `stale-reviewer`; `mcp_builder_paths.py` those of `mcp-builder`. |
| `.claude/skills/` | `one-job-per-file` is how parts are split into files; `flow-graphs` is how steps are laid out as graphs under `flow/`; both builders load the first, the agent-builder also the second. `vault-notes` is the note conventions for the vault. `deep-read` launches a deep read of one paper. `paper-ingest` turns a folder of PDFs into notes, topic links and the graphify graph. |
| `.claude/workflows/` | Workflow scripts. `deep-read.js` is `deep-read-run`, led by the deep reader. |

### Inside an agent folder

Two folders and the files the base reads. `base/` is the template's; `src/` is the agent's; the rest is per-agent configuration and state.

| Path | What it is | Builder reads | Builder writes |
|---|---|---|---|
| `base/` | The base: one class, `Base`, split over one file per job (config, models, MCP tools, trace, the turn) and `base_interface.md`. `src/` subclasses it and gets `self.model()` and `self.tools()`. A copy of `agent_template/base/`, overwritten by `sync.py`. Never edited here. | **no** | no |
| `base/base_interface.md` | The base as a black box: what `src/` must provide, what it gets, what the output line looks like. The one file in `base/` the builder reads. | yes | no |
| `src/` | The agent's code. `src/__init__.py` holds `class Agent(Base)`, overriding `on_message()`, `on_stop()` or `on_start()`. `src/README.md` lists every file. | yes | yes |
| `src/instructions/` | Prompts and other long text, one `.md` per piece. | yes | yes |
| `src/requirements.txt` | The exact set of packages the agent needs to run. | yes | yes |
| `src/<name>.json` | The agent's own settings, if it has any. The base never opens it. | yes | yes |
| `base_settings.json` | The providers, `max_retries` and the granted MCP servers. Shape set by the base, values per agent. Written by `provider.py` and the main session, agreed with the user. | yes | no |
| `.env` | Secrets, one `KEY=value` per line, one per provider. Empty at creation; `provider.py` adds and removes the names, the user fills the values. Nobody reads it. | **no** | no |
| `data/` | Whatever memory the agent keeps. Written by the running agent only. | yes | no |
| `logs/` | One OpenInference trace per run. Written by the base only. | yes | no |
| `README.md` | User manual. Template not yet decided. | yes | no |
| `.gitignore` | Kept from the template; the root `.gitignore` is what actually applies. | no | no |
| `tests/` | Never shipped. Empty for now. | no | no |
| `handoff.md` | What is left to continue in this agent, nothing else. Written by the main session. See **Handoff** below. | no | no |
| `__init__.py`, `__main__.py` | The two lines that make `from agents import <name>` and `python -m agents.<name>` work. Copied from the template, never edited. | no | no |

An agent runs as `python -m agents.<name>` from the repo root with the shared `.venv` active. The main session reads everything except `.env`, and writes everything the builder does not, when the user agrees.

## Handoff

Each agent folder has a `handoff.md`. It holds only what is incomplete: tasks not finished, decisions not made, discussions not closed. When a session picks up an agent, it reads that file first and knows exactly what to continue.

When updating it: add what is still open, and **remove everything that is done**. A finished task does not belong there, even as a checked-off line. The file should read like a to-do list, never a changelog.

## Commits

This directory, `Agent_lab`, is one git repository, pushed to GitHub so a remote session can open the whole lab from one URL. The agent folders are plain folders inside it. The root `.gitignore` keeps every agent's `.env`, `data/`, `logs/`, the Telegram exports under `test data/` and `.venv/` out of history; no `.env` is ever tracked, not even the template's.

Two kinds of commit exist. **Sync commits** are made by `git_sync.py`, which the SessionStart and SessionEnd hooks in `.claude/settings.local.json` run on the user's laptop: it commits whatever is uncommitted as `sync: ...`, then pulls if GitHub is ahead, pushes if the laptop is ahead, and stops with a message if both changed. **Named commits** are made only when the user says so, with the user's notes as the message; the session never commits on its own initiative. The hook file is per machine and not tracked, so a second machine or a remote session has no sync hook until one is added there.

## The protocol

An agent talks through stdout and stdin only. The full line-by-line contract is the `agent-protocol` skill at `.claude/skills/agent-protocol/SKILL.md`. Load it before designing or changing how an agent talks to the user.
