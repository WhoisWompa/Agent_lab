"""start(), on_start(), on_message() and on_stop(): what main.py calls. One AGENT span per hook around src/, every output line checked."""
import json

from .config import error
from .mcp import close, connect, loop
from .trace import tracer

src = None                                   # the agent's package, imported by start() and not before, so a file under src/ can run on its own
CRASH = error("crash: agent stopped, see the trace in Phoenix")


def start():
    """Import src/, check its hooks, start the MCP servers. Called once by main.py before anything else."""
    global src
    try:
        with tracer.start_as_current_span("startup", openinference_span_kind="chain"):   # a failure here is recorded on the span
            import src as package                # src/ does `from base import model, tools`
            src = package
            has_start = callable(getattr(src, "on_start", None))
            has_message = callable(getattr(src, "on_message", None))
            if not (callable(getattr(src, "on_stop", None)) and (has_start or has_message)):
                raise RuntimeError("src/__init__.py must define on_stop() and at least one of on_start() or on_message(text)")
            loop.run_until_complete(connect())
    except Exception:                            # src/ would not load, or a server would not start: tell, die
        print(error("startup: agent failed to start, see the trace in Phoenix"), flush=True)
        raise


def _checked(output):
    """Every stdout line carries 'response' or 'error'. Anything else becomes an error line."""
    if not isinstance(output, str) or not output.strip():
        return error("empty: agent returned nothing to show")
    if output.lstrip().startswith("{"):
        try:
            keys = json.loads(output).keys()
        except (json.JSONDecodeError, AttributeError):
            return output                        # not valid JSON: the app shows it as plain speech
        if not ("response" in keys or "error" in keys):
            return error("empty: agent returned nothing to show")
    return output


def _hook(name, run, text=None):
    """One src/ hook inside one AGENT span, which holds every model and tool span it causes. An exception is recorded on it, then still dies."""
    with tracer.start_as_current_span(name, openinference_span_kind="agent") as span:
        if text is not None:
            span.set_input(text)
        try:
            output, done = loop.run_until_complete(run())
        except Exception:
            print(CRASH, flush=True)
            raise
        output = _checked(output)
        span.set_output(output)
        span.set_attribute("done", done)
        return output, done


def on_start():
    """Before the first input, if src/ defines on_start(). Otherwise: nothing to say, not done."""
    if not callable(getattr(src, "on_start", None)):
        return None, False
    return _hook("on_start", src.on_start)


def on_message(text):
    """One user line. If src/ has no on_message(), the agent takes no input: say so and end."""
    if not callable(getattr(src, "on_message", None)):
        return error("input: this agent takes no messages"), True
    return _hook("on_message", lambda: src.on_message(text), text)


def on_stop():
    """Stop was pressed: src/'s last words, then the MCP servers go down."""
    async def run():
        output = await src.on_stop()
        await close()
        return output, True
    return _hook("on_stop", run)[0]
