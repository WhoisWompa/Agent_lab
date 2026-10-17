---
name: one-job-per-file
description: "How code in this repo is split into files: one job per file, the entry file holds only the entry points, backend work lives in files named for the job, and a table lists every file. Loaded by both builders before they write anything, in agents/<name>/agent/src/ and in mcp/<name>/."
---

# One job per file

A reader opens a folder and knows from the file names what is where. A file is opened to see how one thing is done, not to find out what things exist. That is the whole rule, and the rest of this page is what it means in practice.

## The entry file holds only entry points

Every package has one file the outside world calls into. For an agent it is `src/__init__.py`, with `on_message()`, `on_stop()` and maybe `on_start()`. For an MCP server it is `tools.py`, with one function per tool. That file contains those functions and nothing else. Each body is a line or two that calls into the other files. No loops, no parsing, no file access, no API calls in the entry file.

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

## Backend files are named for their job

Split the rest by what each piece touches, and name the file after the job. The split that recurs:

| Job | File | Holds |
|---|---|---|
| Connecting | `client.py` | Opening the connection to the outside thing: keys, session, login. The only file that knows how to authenticate. |
| Reading or writing the outside thing | `reader.py`, `writer.py`, or named for the thing (`mail.py`, `calendar.py`) | The calls that fetch or send, given an open connection. |
| Shapes | `convert.py` | Parsing inputs (dates from text) and making outputs serialisable (objects to JSON). |
| Storage | `store.py` or a `memory/` package | The agent's own data on disk, how it is read back. |
| Prompts | `instructions/*.md` | Prose for the model, never inline in Python. |
| The command line | `server.py` | Arguments, then run. Nothing else. |

Not every package has every row; a package with no storage has no `store.py`. But a package never has one file doing two rows.

Functions take their dependencies as arguments. `read_messages(client, chat, ...)` takes the client, it does not import a global one. That is what lets a script use the reader without the server, and the server use it without the script.

## Imports flow one way

Entry imports backend. Backend files import `convert.py` and the standard library. `convert.py` imports nothing of ours. Nothing imports the entry file. If two backend files need each other, the shared part moves to a third file.

## Size is the signal

A file past about 150 lines, or a file whose docstring needs "and" to say what it does, is two files. Split it before writing more into it.

## Every file is listed

Each package carries a table, one row per file, saying what the file does in a sentence or two. For an agent it is `src/README.md`. For an MCP server it is the `## Files` section of the server's `README.md`. Whoever adds, renames or removes a file updates the table in the same change. The table is an identification aid: enough to pick the right file, not documentation of it.

## When the brief gives a layout

If the calling session's brief names the files and their functions, build exactly that layout. The rule above is for what the brief leaves open, and for noticing when a brief's single file has quietly become three.

## The worked example

`mcp/telegram/src/telegram_mcp/` is the shape to copy:

```
client.py    reads the two keys from .env, opens the Telethon client on the session file
reader.py    list_chats() and read_messages(), given an open client
convert.py   dates from text, Telethon dicts made JSON-safe
tools.py     the two tools and the FastMCP instance that holds the one client
server.py    command-line arguments, then run over stdio
```
