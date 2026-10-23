"""Base: the one class every agent inherits. Setup in __init__, the three hooks src/ overrides, and run(), the stdin/stdout loop.

Nothing happens at import. `Agent()` reads .env and base_settings.json, checks keys, starts the tracer and the MCP servers,
and says nothing. `Agent().run()` speaks first through on_start(), then answers each input line through on_message(),
and on Stop says on_stop()'s line. Each job is a mixin in its own file; this class only puts them together.
"""
import asyncio
import os
import sys
from datetime import datetime

from .config import Config
from .models import Models
from .mcp import Servers
from .trace import Trace
from .turn import Turn


class Base(Config, Models, Servers, Trace, Turn):

    def __init__(self, folder=None):
        """Set up one agent. `folder` is the agent folder; left out, it is found from the file the subclass lives in.
        A startup failure prints one error line and exits."""
        sys.stdout.reconfigure(encoding="utf-8")   # Windows consoles default to cp1252; a non-ASCII print() would crash
        sys.stdin.reconfigure(encoding="utf-8")
        self.folder = folder or self._find_folder()
        self.name = os.path.basename(self.folder)                      # the Phoenix project every span lands in
        self.run_id = datetime.now().strftime("%Y%m%d-%H%M%S")        # one per process start: the Phoenix session
        os.makedirs(os.path.join(self.folder, "data"), exist_ok=True)
        self._load_env()
        self.settings = self._load_settings()
        self.blocks = self._index_blocks()
        self._check_keys()
        self.loop = asyncio.new_event_loop()                           # one loop for the whole run: MCP servers stay up between messages
        self.tracer = self._make_tracer()
        try:
            with self.tracer.start_as_current_span("startup", openinference_span_kind="chain"):   # a failure here is recorded on the span
                self.loop.run_until_complete(self._connect())
        except Exception:                                              # a server would not start: tell, die
            print(self._error("startup: agent failed to start, see the trace in Phoenix"), flush=True)
            raise

    def _find_folder(self):
        """The agent folder, from the file the subclass is defined in: src/__init__.py sits one level under it."""
        file = sys.modules[type(self).__module__].__file__
        return os.path.dirname(os.path.dirname(os.path.abspath(file)))

    # ---- the hooks. src/ overrides the ones it needs.
    async def on_start(self):
        """Override to speak before the first input. Not called unless overridden.
        Returns: (line, done)."""
        return None, False

    async def on_message(self, text):
        """Override to answer one user line.
        Returns: (line, done). Default: an error line and True, this agent takes no messages."""
        return self._error("input: this agent takes no messages"), True

    async def on_stop(self):
        """Override for last words when Stop is pressed.
        Returns: line. Default: empty."""
        return ""

    # ---- the loop
    async def _last(self):
        output = await self.on_stop()
        await self._close()
        return output, True

    def run(self):
        """The stdin/stdout loop. on_start() first if src/ overrides it, its line printed; then one input() and one on_message() per turn until done.
        On Stop (EOF) prints on_stop()'s line. Either way the MCP servers go down at the end. Returns nothing; the process ends after."""
        done = False
        if type(self).on_start is not Base.on_start:                   # the agent speaks first only if src/ overrides on_start()
            output, done = self._hook("on_start", self.on_start())
            print(output, flush=True)
        try:
            while not done:
                text = input()                                         # what the user typed
                output, done = self._hook("on_message", self.on_message(text), text)
                print(output, flush=True)                              # shows up in the chat
        except EOFError:                                               # Stop was pressed: last words, servers down
            print(self._hook("on_stop", self._last())[0], flush=True)
        else:                                                          # done: servers down, nothing more to say
            self.loop.run_until_complete(self._close())
