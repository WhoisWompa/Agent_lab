# The base, from the outside

Every agent folder has a fixed `base/` package: `main.py`, the base code and this file, together called the base. It is copied from `agent_template/base/` by `sync.py` and never edited inside an agent. You do not read its code. This file is everything you need to know about it to write `src/`.

The base reads one line from the user, hands it to your `on_message()`, prints what you return, and repeats. On Stop it calls your `on_stop()`. If you define `on_start()`, it runs once before the first line is read. In between, it gives you models and tools through two names you import from `base`.

An agent is started as `python agents/<name>/base/main.py`, from any working directory, with the shared `.venv` at the repo root active.

## What `src/` must provide

`src/__init__.py` defines `on_stop()` at module level, and at least one of `on_message()` or `on_start()`.

```python
async def on_message(text: str) -> tuple[str, bool]:   # optional if on_start() is defined
    ...
    return line, done

async def on_stop() -> str:
    ...
    return line

async def on_start() -> tuple[str, bool]:      # optional if on_message() is defined
    ...
    return line, done
```

| | |
|---|---|
| `text` | One line the user typed. Plain string, no trailing newline. A tapped option arrives the same way as typed text; you cannot tell them apart. |
| `line` | One line for the user. See "The output line" below. |
| `done` | `True` when the agent has nothing more to do. The process exits after this line is printed. `False` to wait for the user's next line. |
| `on_message()` | Called once per line the user types. Leave it out for an agent that does its whole job in `on_start()` and returns `done = True`. If `on_start()` returns `done = False` and there is no `on_message()`, the base answers the first line with an `error` and exits. |
| `on_stop()` | Called once when the user presses Stop. Return your last words. The process exits after. |
| `on_start()` | Define it only if the agent speaks before the first input. Called once, before the first line is read. A greeting carries `awaiting`; for an agent that runs without a user, do the whole job here and return the result with `notify` and `done = True`. |

All hooks run on one event loop that lives for the whole process, so anything you keep at module level in `src/` survives between calls.

The base imports `src/` only when `main.py` asks, so any file under `src/` can also be run on its own, as `python -m src.<module>` from the agent folder, for a quick check.

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
from base import model, tools
```

| Call | Returns |
|---|---|
| `model(name, fallback=None, **params)` | A chat model for `name`, built with the key of the provider that lists it in `base_settings.json`. `fallback` names another listed model, switched to when a call to `name` fails; it may sit under a different provider, so a different key. Raises `ValueError` if either name is not listed under any provider. Extra keywords (`temperature=0`, ...) go to the model. There is no default model: always pass a name, and take it from your brief or from a settings file of your own under `src/`. |
| `tools("<server>", ...)` | LangChain tools from those MCP servers, names prefixed with the server: `files_read`. Raises `ValueError` if a server is not in `mcpServers`. |

**What `model()` returns** is a LangChain chat model instance. Use it as LangChain documents: `.invoke()`, `.ainvoke()`, `.bind_tools()`, `.with_structured_output()`, streaming, or as a node in a LangGraph graph. `.invoke()` returns an `AIMessage`. Read `.text` for the words and `.tool_calls` for tool requests; never `.content`, which is provider-shaped (a string on some providers, a list of blocks on others). Call `model()` as many times as you like; each call is a separate instance.

#### Example:
```python
llm = model("claude-haiku-5-5")
reply = llm.invoke("What's the capital of France?")
reply.text         # "The capital of France is Paris."
reply.tool_calls   # []

reply = llm.bind_tools(tools("files")).invoke("Read notes.txt")
reply.text         # ""
reply.tool_calls   # [{"name": "files_read", "args": {"path": "notes.txt"}, "id": "call_abc123", "type": "tool_call"}]

city = llm.with_structured_output(City).invoke("Tell me about Paris")   # City: a Pydantic class or a dict schema
city               # City(name="Paris", country="France"), already parsed, not a message

safe = model("claude-haiku-5-5", fallback="deepseek/deepseek-chat")     # a second key takes over if the first call fails
```

`.text` is always one string, whichever provider is behind it. Thinking blocks and provider metadata stay on the message; leave them there, the provider needs them back when the message goes into a history.

**What `tools()` returns** is a list of LangChain tool objects, already executable. Each knows its name, description and argument schema. Bind them to a model, pass them to `create_agent`, put them in a `ToolNode`, or invoke one directly with a tool-call dict. Invoking one runs it on the MCP server and returns a `ToolMessage`. A server listed in `base_settings.json` is granted in full: every tool on it runs when asked, no further permission.

#### Example:
```python
fs = tools("files")
[t.name for t in fs]          # ["files_read", "files_write", ...]
fs[0].description             # what the server says the tool does
fs[0].args                    # {"path": {"type": "string", ...}}: the argument schema

out = await fs[0].ainvoke({"path": "notes.txt"})        # by arguments: the raw result
msg = await fs[0].ainvoke(reply.tool_calls[0])          # by tool call: a ToolMessage, ready for the history

# the loop by hand: ask, run every tool call, ask again with the results
llm = model("claude-haiku-5-5").bind_tools(fs)
by_name = {t.name: t for t in fs}
history = [("user", "Read notes.txt and summarise it")]
reply = await llm.ainvoke(history)
while reply.tool_calls:
    history += [reply] + [await by_name[c["name"]].ainvoke(c) for c in reply.tool_calls]
    reply = await llm.ainvoke(history)
reply.text

# or let LangChain run that loop
graph = create_agent(model("claude-haiku-5-5"), fs, system_prompt=instructions("system"))
```

Tools from MCP servers are async: use `.ainvoke()`, not `.invoke()`. Passing a tool-call dict returns a `ToolMessage` with the matching `tool_call_id`; passing plain arguments returns the bare result.

Every model and tool must come from these two functions. Anything constructed another way skips the provider lookup, the retries and the fallback.

## What the base already does

You do not write any of this.

- Reads `.env` into `os.environ` and `base_settings.json` at startup. Refuses to start, with a line naming the reason, if there are no providers, a model name is listed under two providers, a provider's key is blank in `.env`, its `langchain-<provider>` package is not installed, a block lacks one of `provider`, `base_url`, `key`, `models`, or the file has a key the base does not know.
- Starts every MCP server in `base_settings.json` once, before the first message, and keeps them running until Stop.
- Retries a failed model call on rate limits and server errors, `max_retries` times from `base_settings.json`.
- Applies the fallback when asked, and warns on stderr when the main model and its fallback share a key.
- Traces every run to Phoenix, at the `phoenix` address in `base_settings.json` (a local `http://localhost:6006` when absent), in the OpenInference format: one AGENT span per hook call carrying the user line and the output line, with every model call and tool call as child spans. The agent's folder name is the Phoenix project; one process start is one Phoenix session. If Phoenix is not running the run goes on and the trace is lost. You never write a trace line.
- Catches your exceptions, as above.
- Sets stdin and stdout to UTF-8.

## Where things live

Paths are relative to the agent folder, `agents/<name>/`.

| Path | Yours? | What |
|---|---|---|
| `src/` | yes | Your code. Any files you like; `src/__init__.py` holds `on_stop()`, and `on_message()` or `on_start()` or both. `src/README.md` lists every file. |
| `src/instructions/` | yes | Prompts and any other long text, one `.md` per piece. Read them at runtime; do not paste prose into Python. |
| `src/requirements.txt` | yes | The exact set of packages the agent needs to run. Add what `src/` imports, remove what nothing imports. Never remove the base's own packages, listed below. |
| `src/<name>.json` | yes | The agent's own settings, if it has any: model names, intervals, which chats to read. Read with `json.load`; the base never opens it. |
| `base_settings.json` | read only | The providers (each one key and the models it serves), `max_retries`, which MCP servers are granted, and `phoenix`, where the trace goes. If you need a model or a server that is not there, say so in your report. |
| `data/` | at runtime | Keep the agent's own memory here if it needs any, in whatever shape. |
| `.env` | no | Secrets. Never read. Every line is loaded into `os.environ` before `src/` is imported, so read a secret by the variable name the brief gives, e.g. `os.environ["TELEGRAM_BOT_TOKEN"]`. |
| `base/` | no | The base. This file replaces it. |
| `base/base_interface.md` | read | This file. |

`src/__init__.py` defines `HERE` as the `src/` folder, from `__file__`. Build every path from it: `os.path.join(HERE, "instructions", "system.md")` for a prompt, `os.path.join(HERE, "..", "data", "notes.json")` for memory.

The base's own packages in `src/requirements.txt`, never removed:

```
langchain
langchain-<provider>      # one per provider value in base_settings.json: langchain-anthropic, langchain-openai, ...
langgraph
langchain-mcp-adapters
openinference-instrumentation-langchain
openinference-semantic-conventions
opentelemetry-sdk
opentelemetry-exporter-otlp-proto-http
```

`deepagents` is also present at creation; keep it only if `src/` uses it.
