"""tools(): the MCP servers in settings.json, started once and kept up for the whole run on one event loop."""
import asyncio
import contextlib

from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.tools import load_mcp_tools

from .config import HERE, settings

loop = asyncio.new_event_loop()              # one loop for the whole run: MCP servers stay up between messages
_tools = {}                                  # server name -> its LangChain tools, filled by connect()
_client = MultiServerMCPClient({name: {"cwd": HERE, **cfg} for name, cfg in settings["mcpServers"].items()})


def tools(*servers):
    """LangChain tools from the named MCP servers. Every name must be in settings.json mcpServers."""
    out = []
    for name in servers:
        if name not in _tools:
            raise ValueError(f"MCP server '{name}' is not in settings.json mcpServers")
        out += _tools[name]
    return out


async def connect():
    """Start every MCP server in settings and fetch its tools. Runs once at startup."""
    global _ready, _stop, _keeper
    _ready, _stop = asyncio.Event(), asyncio.Event()
    _keeper = asyncio.ensure_future(_hold())
    await _ready.wait()
    if _keeper.done():
        _keeper.result()                     # re-raise whatever stopped it


async def _hold():
    """One task owns the server connections for the whole run, so they survive between messages."""
    try:
        async with contextlib.AsyncExitStack() as stack:
            for name in settings["mcpServers"]:
                session = await stack.enter_async_context(_client.session(name))
                _tools[name] = await load_mcp_tools(session, server_name=name, tool_name_prefix=True)
            _ready.set()
            await _stop.wait()
    finally:
        _ready.set()


async def close():
    """Shut the MCP servers down. Runs after on_stop()."""
    _stop.set()
    await _keeper
