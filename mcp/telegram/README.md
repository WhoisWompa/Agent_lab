# telegram-mcp

An MCP server over the user's own Telegram account, through Telethon. Two tools:

| Tool | Input | Output |
|---|---|---|
| `chats` | `only`: names to keep, `exclude`: names to drop, both optional | One record per chat: `id`, `name`, `kind` (user, group, channel), `unread`, `last_message`. Newest activity first. |
| `messages` | `chat`: the name as Telegram shows it. Optional `start`, `end` (local time, `YYYY-MM-DD` or `YYYY-MM-DD HH:MM`), `limit` (newest N). | `chat` record, `window`, `users` (sender id to user record), `messages` (full Telethon dicts, oldest first). |

## Files

| File | What |
|---|---|
| `client.py` | Reads the two keys from `.env`, opens the Telethon client on the session file. |
| `reader.py` | `list_chats()` and `read_messages()`: the reading, given an open client. |
| `convert.py` | Dates from text, Telethon dicts made JSON-safe. |
| `tools.py` | The two tools and the FastMCP instance that holds the one client. |
| `server.py` | The entry: command-line arguments, then run over stdio. |

## Run

```
pip install -e mcp/telegram
telegram-mcp                      # or: python -m telegram_mcp
```

Talks MCP over stdio. Reads `TELEGRAM_API_ID` and `TELEGRAM_API_HASH` from `.env` in the working directory and the session from `data/telegram.session`; both paths can be changed with `--env` and `--session`.

## Login

The server never asks for a login code. Log in once with a script that calls `open_client(interactive=True)` from `telegram_mcp.client`; it asks for phone and code and leaves the session file. The ledger's `test data/export_telegram.py` does this. Without a session the server refuses to start and says so.

## Grant it to an agent

In the agent's `base_settings.json`:

```json
"mcpServers": {
  "telegram": {
    "transport": "stdio",
    "command": "python",
    "args": ["-m", "telegram_mcp"]
  }
}
```

The base starts it with the agent folder as working directory, so `.env` and `data/` are the agent's own. In `src/`: `tools("telegram")` gives `telegram_chats` and `telegram_messages`.
