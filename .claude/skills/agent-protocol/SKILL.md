---
name: agent-protocol
description: "The stdout/stdin protocol every agent in this repo speaks: response and error lines, the awaiting, options, notify, tokens and file keys, how a run ends. Load before designing or changing how an agent talks to the user."
---

# The protocol

An agent talks through stdout and stdin only. It works when run by hand in a terminal: start it, type replies, watch the output.

### Core

The chat does not function without these.

| Piece | What it is |
|---|---|
| **Speech out** | A line printed to stdout. Either a plain line, or a JSON object line with `"response"`. Both are the agent's speech in its chat. Every line carries exactly one of `"response"` or `"error"`; a plain line counts as `"response"`. Never neither. |
| **Hearing in** | One plain line on stdin per message from the user, in order. A tapped option and a typed reply arrive the same way; the agent cannot tell them apart. |
| **Exit = done** | The process exiting ends the run. Nothing to print; just return. |

`{"response": "Hello"}` and a plain `Hello` are the same thing.

### How a run ends

| Who | How | What the agent does |
|---|---|---|
| **The agent** | `on_message()` or `on_start()` returns `done = True`. | Nothing more. |
| **The user presses Stop** | The app hangs up the agent's stdin. The next read raises `EOFError`. | `on_stop()` runs: last words, saving memory. Then the process ends. |

### Optional keys

Put these on the same JSON line as `"response"`. Unknown keys are ignored.

| Key | Type | What it does |
|---|---|---|
| `awaiting` | `true` | The agent is **waiting for the user** and reads stdin next. |
| `options` | list of strings | Options the user can choose from, given the response. |
| `notify` | `true` | A **ping**: the agent does **not** wait. For "done", reminders, heads-ups. |
| `tokens` | number | Usage reported for this line. |
| `file` | path string | Attaches a file to this line. Must be inside the agent's own folder. Optional `caption` string beside it. |
| `error` | string | The line is a failure, not speech. Appears **instead of** `response`, never beside it. Prefixed with its kind: `startup:`, `crash:` or `empty:`. If the process exits right after, the run ended abnormally. |

`awaiting` vs `notify`: both surface to the user; only `awaiting` blocks. Never set both on one line.
