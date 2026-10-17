# Purpose of this project

This project main focus is building **agent architectures**: Python programs that run as a process.

# Workflow

The main session is the second voice: the user brings ideas, the session
pushes back, and designs take shape in the conversation. Three teams are
called from the main session, never on their own initiative.

The user leads. The session answers what is asked, pushes back where it
disagrees, and offers an idea when it has one. It does not set direction:
no plans, no step lists, no "what I need from you", no next-steps closing.
The only write allowed is appending a blank key name (`echo KEY= >> agent/.env`) when an agreed design needs a new secret; the user fills the value.

## Discussion

The default mode. Ideas, designs and implementations are talked through.
Nothing is spawned. A paper worth reading in full goes to deep read; a
direction worth trying goes to building.

## Deep read

A paper is read in full only on the user's word, through the `deep-read`
skill. The main session reads back one thing: the report. Nothing else
from the run enters its context.

A run is the `deep-read-run` workflow. The deep reader leads it: it reads
the paper, the librarian checks which references already have notes,
searchers find the missing ones on arXiv and GitHub, readers read the
abstract or README only and write one note per reference, and the deep
reader reads all the summaries and writes the report. That is what creates
the Cites and Cited by links in the vault.

The research run that used to sit in front of this was removed on
2026-10-15. The user is building their own research process outside the
workflow tool.

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

## Documentation team

Runs at the end of a session, via `record`. It writes down the ideas and
decisions made along the way, with the reasoning, as they stood at the
time. Nothing has to be settled to be recorded. The point is that a
future session on the same problem starts from the user's own thinking.

# Rules that must be followed during the session

`list_of_agents.md` is one table with two columns:

| Column | What goes in it |
|---|---|
| **Agent** | The folder name. |
| **Summary** | Two to four sentences: what the agent does, what it works with (e.g. email, a calendar, a folder of files, a specific API), and what it produces. Just enough that when the user describes a change in plain words, the right agent can be picked out or the list narrowed to two or three. It is an identification aid, not documentation. |

Every agent lives in its own folder under `agents/`, one folder per agent. `list_of_agents.md` is at the root so a session can find the right agent without opening every folder.

At the start of session:

1. Read `list_of_agents.md`.
2. If the user's opening message clearly indicates which agent in the table, start on it. Do not ask.
3. Otherwise, match what the user describes against the Summary column. If one agent clearly fits, confirm it in a line and proceed. If several could fit, offer those candidates plus "new agent" and let the user choose.

While building the source code:
1. Inside an agent, `main.py` and `base/` are the base. They are read-only, never edited, for any reason. The builder writes only `src/`, `instructions/` and `requirements.txt`.

## Keeping the table up to date.

The summary describes the agent in high level overview. It should contain enough that anyone reading it knows what the agent does, without technical detail.

**If the agent direction changes, always show the new proposed summary to the user before writing it to `list_of_agents.md`.**

## Creating a new agent

1. Before drafting, the session asks whatever it needs to get the big picture of what the agent is supposed to do. The aim is a summary detailed enough that a future session reading `list_of_agents.md` can tell this agent apart from every other one. Questions about the idea only, never about how to build it or what the session needs. Then it drafts the row (folder name and summary) and shows it, with one more question: which provider and default model the agent runs on. If the user doesnt provide a name, give some options for the user to choose from, or tell the user to enter its own preferred name.
2. The user edits or agrees. Redraft until agreed. Nothing is written before.
3. On agreement: add the row to `list_of_agents.md`, copy `agent_template/` to `agents/<name>/`, set the provider and base URL in `settings.json` and the matching package in `requirements.txt`, and create an empty `agent/.env` (no `.env` is tracked, so the copy will not have one).
4. Report that the folder exists, in a line, and stop. No plan, no open questions, no suggestion of what to build first. The user says what comes next.
5. Never read `agent/.env`.


## Repo layout

| Path | What it is |
|---|---|
| `agents/<agent-name>/` | One folder per agent. `agents/` holds nothing else. Its `agent/` subfolder is the part that ships. Contents in the next table. |
| `agent_template/` | The blank agent folder. Copied and renamed to start every new agent. Never edited directly. |
| `list_of_agents.md` | The index of agents. |
| `mcp/` | Shared MCP servers that agents may list in their `settings.json`. |
| `.claude/agents/` | Subagents. `agent-builder` writes an agent's logic from a brief; `mcp-builder` writes an MCP server in `mcp/<name>/` from a brief. `research-searcher`, `research-reader`, `research-librarian` and `deep-reader` are the deep-read team, spawned by the deep-read workflow only. |
| `.claude/hooks/` | `builder_paths.py` and `mcp_builder_paths.py` enforce the two builders' read and write limits. |
| `.claude/skills/` | `one-job-per-file` is how code is split into files; both builders load it before writing. `vault-notes` is the note conventions for the vault. `record` runs the documentation agent, a fork that writes the session into the vault. `deep-read` launches a deep read of one paper. |
| `.claude/workflows/` | Workflow scripts. `deep-read.js` is `deep-read-run`, led by the deep reader. |
| `notes/` | The Obsidian vault: session, decision, agent, paper, repo, research and topic notes. Tags are arXiv categories. Written by `record` and the deep-read agents. |

### Inside an agent folder

| Path | What it is | Builder reads | Builder writes |
|---|---|---|---|
| `.gitignore` | Kept from the template; the root `.gitignore` is what actually applies. | no | no |
| `agent/main.py` | The stdin/stdout loop. Fixed, never edited by anyone. | **no** | no |
| `agent/base/` | The base, one file per job: config, trace, models, MCP tools, the turn. Gives `src/` `model()`, `tools()` and `settings`. Fixed, never edited by anyone. | **no** | no |
| `agent/base_interface.md` | The base as a black box: what `src/` must provide, what it gets, what the output line looks like. What the builder reads instead of the base code. Fixed. | yes | no |
| `agent/.env` | Secrets, one `KEY=value` per line. Blank at creation; the user fills values. Nobody reads it. When a design needs a new secret, the main session appends the blank key name without reading the file, and the brief tells the builder which environment variable to read. | **no** | no |
| `agent/settings.json` | Provider, base URL, allowed models, granted MCP servers, retries. Written by the main session, agreed with the user. | yes | no |
| `agent/requirements.txt` | The exact set of packages the agent needs to run. | yes | yes |
| `agent/src/` | The agent's code. `src/__init__.py` holds `on_stop()`, and `on_message()` or `on_start()` or both: `on_message()` for an agent that takes input, `on_start()` for one that speaks first or does its whole job at startup. | yes | yes |
| `agent/instructions/` | Prompts and other long text, one `.md` per piece. | yes | yes |
| `agent/data/` | Whatever memory the agent keeps. Written by the running agent only. | yes | no |
| `agent/logs/` | One OpenInference trace per run. Written by the base only. | yes | no |
| `agent/README.md` | User manual. Template not yet decided. | yes | no |
| `tests/` | Never shipped. Empty for now. | no | no |
| `handoff.md` | What is left to continue in this agent, nothing else. Written by the main session. See **Handoff** below. | no | no |

The main session reads everything except `.env`, and writes everything the builder does not, when the user agrees. On `.env` it only appends key names, as above.

## Handoff

Each agent folder has a `handoff.md`. It holds only what is incomplete: tasks not finished, decisions not made, discussions not closed. When a session picks up an agent, it reads that file first and knows exactly what to continue.

When updating it: add what is still open, and **remove everything that is done**. A finished task does not belong there, even as a checked-off line. The file should read like a to-do list, never a changelog.

## Commits

This directory, `Agent_lab`, is one git repository, pushed to GitHub so a remote session can open the whole lab from one URL. The agent folders are plain folders inside it. A commit is made only when the user says so and never on your own initiative. The user's notes are the commit message. The root `.gitignore` keeps every `agent/.env`, `agent/data/`, `agent/logs/`, the Telegram exports under `test data/` and `.venv/` out of history; no `.env` is ever tracked, not even the template's.

## The protocol

An agent talks through stdout and stdin only. The full line-by-line contract is the `agent-protocol` skill at `.claude/skills/agent-protocol/SKILL.md`. Load it before designing or changing how an agent talks to the user.
