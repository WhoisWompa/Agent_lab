# ledger

## Files

One row per file under `src/`. Whoever adds, renames or removes a file updates this table in the same change.

| File | What it does |
|---|---|
| `__init__.py` | The entry the base calls. `on_message()` takes one line from the user and returns the reply; `on_stop()` runs when the user presses Stop. `instructions()` loads a prompt from `instructions/<name>.md`. Both entry bodies are empty for now. |
| `memory/__init__.py` | Package marker for the ledger's memory: the account on disk and how it is read back. Nothing in it yet. |
| `memory/nodes.py` | The two node kinds the memory is made of. `Entity` is a person or thing. `Context` is something read from a chat (an event, a promise, a reply owed) that names entities and so links them. Nothing reads or writes these yet. |
