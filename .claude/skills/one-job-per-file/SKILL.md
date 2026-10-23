---
name: one-job-per-file
description: "How code in this repo is split into files: one job per file, the entry file holds only the entry points, parts live in families named for the job, imports point toward the root, and a table lists every file. The parts axis; the time axis is the flow-graphs skill. Loaded by both builders before they write anything, in agents/<name>/src/ and in mcp/<name>/."
---

# One job per file

A reader opens a folder and knows from the file names what is where. A file is opened to see how one thing is done, not to find out what things exist. That is the whole rule, and the rest of this page is what it means in practice.

This page is about the parts of an agent: what it is made of and where each part sits. The steps an agent takes, in order, are the other axis, and that is the `flow-graphs` skill. The two do not have to line up.

## The entry file holds only entry points

Every package has one file the outside world calls into. For an agent it is `src/__init__.py`, holding `class Agent(Base)` with `on_message()`, `on_stop()` and maybe `on_start()`. For an MCP server it is `tools.py`, with one function per tool. That file contains those and nothing else. Each body is a line or two that hands off: for an agent on LangGraph, it takes the top graph that `flow/` built and runs it. No loops, no parsing, no file access, no API calls in the entry file.

Wrong, everything in the entry:

```python
@mcp.tool()
async def messages(chat, start=None, end=None, limit=None):
    dialog = None
    async for d in client.iter_dialogs():          # finding the chat
        ...
    async for m in client.iter_messages(...):       # reading it
        ...
    return {"chat": plain(...), ...}                 # shaping the result
```

Right, the entry delegates:

```python
@mcp.tool()
async def messages(chat, start=None, end=None, limit=None):
    """..."""
    return await read_messages(_client, chat, parse(start), parse(end), limit)
```

## A family is a folder

Under `src/`, the parts are grouped by what they are for. Parts that only make sense together live in one folder, named for the job: `notes/`, `claims/`, `persona/`. Two different jobs are two folders, even when both are "an agent inside the agent". A file that every family uses sits at the root of `src/`, not in any family.

The more foundational a part, the closer to the root it sits. Going deeper is going from shared to specific.

## Files are named for their job

Inside a family, split by what each piece touches and name the file after the job. The split that recurs:

| Job | File | Holds |
|---|---|---|
| Connecting | `client.py` | Opening the connection to the outside thing: keys, session, login. The only file that knows how to authenticate. |
| Reading or writing the outside thing | `reader.py`, `writer.py`, or named for the thing (`mail.py`, `calendar.py`) | The calls that fetch or send, given an open connection. |
| Shapes | `convert.py` | Parsing inputs (dates from text) and making outputs serialisable (objects to JSON). Reshaping only, never deciding. |
| Storage | `store.py` or a `memory/` package | The agent's own data on disk, how it is read back. |
| Prompts | `src/instructions/*.md` | Prose for the model, never inline in Python. |
| The command line | `server.py` | Arguments, then run. MCP servers only. |

These are the names to use when that kind of work comes up, not files every agent has. A family with no storage has no `store.py`. A name that says the job better wins over the table. But a file never does two rows.

Functions take their dependencies as arguments. `read_messages(client, chat, ...)` takes the client, it does not import a global one. That is what lets a script use the reader without the server, and the server use it without the script.

## Imports point toward the root

A root file imports nothing of ours. A family imports root files and nothing beside it. `flow/` imports down into its own graphs and across into families. Nothing imports the entry file, and nothing imports `flow/`. If two families need each other, the shared part moves to the root.

## Size is the signal

A file past about 150 lines is the tripwire: stop and say in one line what the file does. If that line needs "and", the file is two jobs. Split it before writing more into it. A family file that is two jobs becomes two files. A step file that is two jobs becomes a folder with its own graph; see `flow-graphs`.

## Every file is listed

Each package carries a table, one row per file, saying what the file does in a sentence or two. For an agent it is `src/README.md`. For an MCP server it is the `## Files` section of the server's `README.md`. Whoever adds, renames or removes a file updates the table in the same change. The table is an identification aid: enough to pick the right file, not documentation of it. A row that needs "and" is a file that needs splitting.

## When the brief gives a layout

If the calling session's brief names the files and their functions, build exactly that layout. The rule above is for what the brief leaves open. If a file in the brief turns out to be more than one job while you write it, build it as briefed and say so in the report; do not split it, because the tree is agreed in discussion.

## The worked example

The parts of a made-up agent that answers a question from a folder of notes:

```
src/
  __init__.py       class Agent(Base): runs the top graph that flow/ built
  README.md         one row per file
  state.py          root: what the graph carries from step to step
  convert.py        root: shapes every family shares
  flow/             the steps, in order; see flow-graphs
  notes/            a family
    store.py        the notes on disk, read back
    search.py       which notes match a question
  claims/           a second family, a different job
    split.py        the claims in a piece of text
    backing.py      whether one claim is backed by one note
```

Read the folders and you have the parts: notes, claims. Open one and the file names say which piece is where. The root files are the ones every family shares.
