"""The two tools the server offers, and the one Telethon client they share."""

import contextlib

from mcp.server.fastmcp import FastMCP

from .client import ENV, SESSION, open_client
from .convert import parse
from .reader import list_chats, read_messages

_client = None
paths = {"env": ENV, "session": SESSION}     # server.py overrides these from the command line


@contextlib.asynccontextmanager
async def _lifespan(server):
    """Open the one Telethon client for the run; close it when the server stops."""
    global _client
    _client = await open_client(paths["env"], paths["session"])
    try:
        yield {}
    finally:
        await _client.disconnect()


mcp = FastMCP("telegram", lifespan=_lifespan)


@mcp.tool()
async def chats(only: list[str] | None = None, exclude: list[str] | None = None) -> list[dict]:
    """The user's Telegram chats, newest activity first, one record each:
    id, name, kind (user, group or channel), unread count, last_message (ISO date of the newest message).
    `only` keeps just the chats with these names; `exclude` drops the chats with these names."""
    return await list_chats(_client, only, exclude)


@mcp.tool()
async def messages(chat: str, start: str | None = None, end: str | None = None, limit: int | None = None) -> dict:
    """Every message in the Telegram chat named `chat` (the name as Telegram shows it, see `chats`),
    oldest first, each as the full Telethon record. `start` and `end` bound the window in local time,
    "YYYY-MM-DD" or "YYYY-MM-DD HH:MM", either may be omitted. `limit` keeps only the newest N of the window.
    Returns {"chat", "window", "users" (sender id -> user record), "messages"}."""
    return await read_messages(_client, chat, parse(start), parse(end), limit)
