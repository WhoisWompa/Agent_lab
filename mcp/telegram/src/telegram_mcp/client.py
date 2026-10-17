"""The Telethon connection: keys from .env, session file on disk, one client."""

import os

from telethon import TelegramClient

ENV = ".env"                 # relative to the working directory, i.e. the agent folder
SESSION = "data/telegram"    # Telethon appends ".session"


def load_env(path):
    """Put the KEY=value lines of `path` into os.environ, without overriding what is already set."""
    with open(path, encoding="utf-8") as f:
        for line in f:
            key, _, value = line.strip().partition("=")
            if key and value and not key.startswith("#"):
                os.environ.setdefault(key, value.strip())


async def open_client(env=ENV, session=SESSION, interactive=False):
    """A connected Telethon client from the keys in `env` and the session file at `session`.

    With interactive=True a missing session asks for phone and code on the terminal.
    Without it a missing session raises, telling the user to log in once.

    Returns:
        A connected, authorised TelegramClient. The caller disconnects it.
    """
    load_env(env)
    for key in ("TELEGRAM_API_ID", "TELEGRAM_API_HASH"):
        if not os.environ.get(key, "").strip():
            raise RuntimeError(f"{key} is missing or blank in {env}")
    os.makedirs(os.path.dirname(session) or ".", exist_ok=True)
    client = TelegramClient(session, int(os.environ["TELEGRAM_API_ID"]), os.environ["TELEGRAM_API_HASH"])
    if interactive:
        await client.start()
        return client
    await client.connect()
    if not await client.is_user_authorized():
        await client.disconnect()
        raise RuntimeError(f"no Telegram session at {session}.session: log in once with the exporter")
    return client
