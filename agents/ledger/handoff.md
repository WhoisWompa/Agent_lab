# Ledger: what is open

## Next: the read path

Build the path from the tools to memory: `src/` calls `telegram_chats` and
`telegram_messages` (granted in `base_settings.json`, from `mcp/telegram/`) from
code, not from the model, one chat at a time, turns the messages into
`Entity` and `Context` nodes from `src/memory/nodes.py`, and saves them as
a set of nodes in `data/`. Nothing reads or writes nodes yet; `memory/` has
only the two dataclasses. The main session shows the files and signatures
before the builder is called, and the builder follows `one-job-per-file`.

Decisions not yet made on that path: how nodes are stored on disk, how the
model is asked to extract contexts from a batch of messages, how the ledger
remembers where it last read up to per chat, and which model name `src/`
passes to `model()` now that there is no default (the provider block lists
`claude-haiku-5-5`; the name belongs in a settings file under `src/`).

## Before the ledger can read Telegram

- `TELEGRAM_API_ID` and `TELEGRAM_API_HASH` are blank in `.env`, as is
  `ANTHROPIC_API_KEY`. The Telegram pair comes from my.telegram.org, API
  development tools.
- No session file yet. The first run of `test data/export_telegram.py` does
  the phone-and-code login and leaves `data/telegram.session`, which
  the MCP server then uses. The server refuses to start without it.
- The test set is not exported yet. Which chats, and the window, are the
  user's call. Output goes to `test data/telegram chats/`, git-ignored.
- The exporter is throwaway, but it is also the only login path. Delete it
  only after the login and the export are done, or first give the login its
  own tiny script in `mcp/telegram/`. Not decided.
- The `telegram` entry in `base_settings.json` runs `python` from the PATH, so
  the ledger must be started with the shared `.venv` active or `telegram_mcp`
  is not found.

## Later

- A timer for how often the ledger runs, then Bayesian optimisation of that
  interval by time of day.
- A lookup tool at question time, messages around one id, once the ledger
  asks for it. Not needed for the read path.
- Sender ids in a tool result's `users` table are strings, ids inside
  messages are numbers. Whatever builds nodes converts one side.
