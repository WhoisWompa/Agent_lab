"""Servers: the MCP servers in base_settings.json, started once and kept up for the whole run on the agent's event loop."""
import asyncio
import contextlib

from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.tools import load_mcp_tools


class Servers:
    """Needs self.folder, self.settings and self.loop. Fills self._tools: server name -> its LangChain tools."""

    def tools(self, *servers):
        """Returns: LangChain tools from the named MCP servers, names prefixed with the server.
        Raises ValueError if a server is not in base_settings.json mcpServers."""
        out = []
        for name in servers:
            if name not in self._tools:
                raise ValueError(f"MCP server '{name}' is not in base_settings.json mcpServers")
            out += self._tools[name]
        return out

    async def _connect(self):
        """Start every MCP server in settings and fetch its tools. Runs once, from __init__."""
        self._tools = {}
        self._ready, self._stop = asyncio.Event(), asyncio.Event()
        self._keeper = asyncio.ensure_future(self._hold())
        await self._ready.wait()
        if self._keeper.done():
            self._keeper.result()                # re-raise whatever stopped it

    async def _hold(self):
        """One task owns the server connections for the whole run, so they survive between messages."""
        servers = self.settings["mcpServers"]
        client = MultiServerMCPClient({name: {"cwd": self.folder, **cfg} for name, cfg in servers.items()})
        try:
            async with contextlib.AsyncExitStack() as stack:
                for name in servers:
                    session = await stack.enter_async_context(client.session(name))
                    self._tools[name] = await load_mcp_tools(session, server_name=name, tool_name_prefix=True)
                self._ready.set()
                await self._stop.wait()
        finally:
            self._ready.set()

    async def _close(self):
        """Shut the MCP servers down. Runs after on_stop()."""
        self._stop.set()
        await self._keeper
