# The base, from the outside

Every agent's `agent/` folder has a fixed `main.py` and a fixed `base/` package, together called the base. You do not read them. This file is everything you need to know about them to write `src/`.

The base reads one line from the user, hands it to your `on_message()`, prints what you return, and repeats. On Stop it calls your `on_stop()`. If you define `on_start()`, it runs once before the first line is read. In between, it gives you models and tools through three names you import from `base`.

## What `src/` must provide

`src/__init__.py` defines two functions at module level, and may define a third.

```python
async def on_message(text: str) -> tuple[str, bool]:
    ...
    return line, done

async def on_stop() -> str:
    ...
    return line

async def on_start() -> tuple[str, bool]:      # optional
    ...
    return line, done
```

| | |
|---|---|
| `text` | One line the user typed. Plain string, no trailing newline. A tapped option arrives the same way as typed text; you cannot tell them apart. |
| `line` | One line for the user. See "The output line" below. |
| `done` | `True` when the agent has nothing more to do. The process exits after this line is printed. `False` to wait for the user's next line. |
| `on_stop()` | Called once when the user presses Stop. Return your last words. The process exits after. |
| `on_start()` | Define it only if the agent speaks before the first input. Called once, before the first line is read. A greeting carries `awaiting`; for an agent that runs without a user, do the whole job here and return the result with `notify` and `done = True`. |

All hooks run on one event loop that lives for the whole process, so anything you keep at module level in `src/` survives between calls.

## The output line

What a hook returns is printed to stdout as one line. It is either plain text or one JSON object.

```python
return "Hello", False
return json.dumps({"response": "Hello"}), False
return json.dumps({"response": "Which folder?", "awaiting": True, "options": ["Inbox", "Archive"]}), False
```

The first two mean the same thing. A JSON line must carry exactly one of `response` or `error`. Keys that may sit beside `response`:

| Key | Type | Meaning |
|---|---|---|
| `awaiting` | `true` | You are waiting for the user's next line. |
| `options` | list of strings | Choices offered to the user. A pick arrives as the next `text`. |
| `notify` | `true` | A heads-up; you are not waiting. Never together with `awaiting`. |
| `file` | path string | A file inside the agent's folder to attach. Optional `caption` string beside it. |

Use only the keys your brief asks for.

**What the base does with your line.** If it is empty, not a string, or a JSON object with neither `response` nor `error`, the base replaces it with an `error` line and the process continues. If it starts with `{` but is not valid JSON, it is printed as is and shows as plain text. Otherwise it is printed unchanged.

**If a hook raises**, the base records the exception on the hook's span, prints an `error` line, and the process exits. Catch what you can recover from; let the rest propagate.

## What `src/` gets

```python
from base import model, tools, settings
```

| Call | Returns |
|---|---|
| `model(name=None, fallback=False, **params)` | A chat model. No `name` gives the default. Raises `ValueError` if `name` is not `models.default` or in `models.allowed`; with `fallback=True` it returns the default instead, and also switches to the default if a call fails. Extra keywords (`temperature=0`, ...) go to the model. |
| `tools("<server>", ...)` | LangChain tools from those MCP servers, names prefixed with the server: `files_read`. Raises `ValueError` if a server is not in `mcpServers`. |
| `settings` | `settings.json` as a dict, for any extra key the brief put there. |

**What `model()` returns** is a LangChain chat model instance. Use it as LangChain documents: `.invoke()`, `.ainvoke()`, `.bind_tools()`, `.with_structured_output()`, streaming, or as a node in a LangGraph graph. `.invoke()` returns an `AIMessage`. Read `.text` for the words and `.tool_calls` for tool requests; never `.content`, which is provider-shaped (a string on some providers, a list of blocks on others). Call `model()` as many times as you like; each call is a separate instance.

#### Example:
```python
reply = model().invoke("What's the capital of France?")
reply.text         # "The capital of France is Paris."
reply.tool_calls   # []

reply = model().bind_tools(tools("files")).invoke("Read notes.txt")
reply.text         # ""
reply.tool_calls   # [{"name": "files_read", "args": {"path": "notes.txt"}, "id": "call_abc123", "type": "tool_call"}]

city = model().with_structured_output(City).invoke("Tell me about Paris")   # City: a Pydantic class or a dict schema
city               # City(name="Paris", country="France"), already parsed, not a message
```

`.text` is always one string, whichever provider is behind it. Thinking blocks and provider metadata stay on the message; leave them there, the provider needs them back when the message goes into a history.

**What `tools()` returns** is a list of LangChain tool objects, already executable. Each knows its name, description and argument schema. Bind them to a model, pass them to `create_agent`, put them in a `ToolNode`, or invoke one directly with a tool-call dict. Invoking one runs it on the MCP server and returns a `ToolMessage`. A server listed in `settings.json` is granted in full: every tool on it runs when asked, no further permission.

#### Example:
```python
fs = tools("files")
[t.name for t in fs]          # ["files_read", "files_write", ...]
fs[0].description             # what the server says the tool does
fs[0].args                    # {"path": {"type": "string", ...}}: the argument schema

out = await fs[0].ainvoke({"path": "notes.txt"})        # by arguments: the raw result
msg = await fs[0].ainvoke(reply.tool_calls[0])          # by tool call: a ToolMessage, ready for the history

# the loop by hand: ask, run every tool call, ask again with the results
llm = model().bind_tools(fs)
by_name = {t.name: t for t in fs}
history = [("user", "Read notes.txt and summarise it")]
reply = await llm.ainvoke(history)
while reply.tool_calls:
    history += [reply] + [await by_name[c["name"]].ainvoke(c) for c in reply.tool_calls]
    reply = await llm.ainvoke(history)
reply.text

# or let LangChain run that loop
graph = create_agent(model(), fs, system_prompt=instructions("system"))
```

Tools from MCP servers are async: use `.ainvoke()`, not `.invoke()`. Passing a tool-call dict returns a `ToolMessage` with the matching `tool_call_id`; passing plain arguments returns the bare result.

Every model and tool must come from these two functions. Anything constructed another way skips the allow-list, the retries and the fallback.

## What the base already does

You do not write any of this.

- Reads `.env` and `settings.json` at startup and refuses to start if a key is blank or `models.default` is missing.
- Starts every MCP server in `settings.json` once, before the first message, and keeps them running until Stop.
- Retries a failed model call on rate limits and server errors, `max_retries` times from `settings.json`.
- Applies the model fallback when asked.
- Traces every run to `logs/trace_<start time>.jsonl` in the OpenInference format: one AGENT span per hook call carrying the user line and the output line, with every model call and tool call as child spans, one JSON span per line. You never write a trace line.
- Catches your exceptions, as above.
- Sets stdin and stdout to UTF-8.

## Where things live

| Path | Yours? | What |
|---|---|---|
| `src/` | yes | Your code. Any files you like; `src/__init__.py` holds `on_message()` and `on_stop()`, and `on_start()` if there is one. |
| `instructions/` | yes | Prompts and any other long text, one `.md` per piece. Read them at runtime; do not paste prose into Python. |
| `requirements.txt` | yes | The exact set of packages the agent needs to run. Add what `src/` imports, remove what nothing imports. Never remove the base's own packages, listed below. |
| `settings.json` | read only | Which provider, which models are allowed, which MCP servers are granted. If you need one that is not there, say so in your report. |
| `data/` | at runtime | Keep the agent's own memory here if it needs any, in whatever shape. |
| `logs/` | no | The base's traces, one file per run. |
| `.env` | no | Secrets. Never read, never needed. |
| `main.py`, `base/` | no | The base. This file replaces them. |
| `base_interface.md` | read | This file. |

The base's own packages in `requirements.txt`, never removed:

```
langchain
langchain-<provider>      # langchain-openai, langchain-anthropic, ... matching settings.json
langgraph
langchain-mcp-adapters
openinference-instrumentation-langchain
openinference-semantic-conventions
opentelemetry-sdk
```

`deepagents` is also present at creation; keep it only if `src/` uses it.
