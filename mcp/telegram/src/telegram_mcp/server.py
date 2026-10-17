"""telegram MCP server: the user's own Telegram chats over stdio. This is the entry: arguments, then run.

The server is started by an agent's base with the agent folder as working
directory. At startup it reads TELEGRAM_API_ID and TELEGRAM_API_HASH from the
.env file there, opens the session file in data/, and keeps that one client for
the whole run. It never asks for a login code: a server has no terminal. Log in
once with a script that calls open_client(interactive=True), such as the
ledger's exporter in test data/, and the session file does the rest.

Files: client.py opens the connection, reader.py reads chats and messages,
convert.py handles dates and JSON, tools.py holds the two tools.
"""

import argparse

from .client import ENV, SESSION
from . import tools


def main():
    p = argparse.ArgumentParser(description="MCP server over the user's Telegram account, stdio transport.")
    p.add_argument("--env", default=ENV, help="file with TELEGRAM_API_ID and TELEGRAM_API_HASH (default .env)")
    p.add_argument("--session", default=SESSION, help="session file path without .session (default data/telegram)")
    args = p.parse_args()
    tools.paths.update(env=args.env, session=args.session)
    tools.mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
