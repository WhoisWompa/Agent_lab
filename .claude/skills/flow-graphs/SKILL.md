---
name: flow-graphs
description: "How an agent's reasoning is laid out as LangGraph graphs under src/flow/: one node per step, one folder per graph with its __init__.py wiring it, nested folders for nested graphs, the trace nesting the same way. The time axis; the parts axis is the one-job-per-file skill. Loaded by the agent-builder before it writes anything in flow/."
---

# Flow graphs

The graph is the agent in time: the steps it takes, in order, with the decisions between them. Reading the node names in order tells the story of the agent. When something breaks, the trace names the step.

The parts the steps use are the other axis, laid out by the `one-job-per-file` skill. The two do not have to line up.

## One node per step

A node is one step of the agent's reasoning: a check, a decision, an action. Named in the agent's own words: `read_target`, `ask_user`, `enough`. A decision is a node too, so it shows in the trace; the edge after it reads the result. A node is never a helper, and never a bundle of helpers.

A step's body is short: take what it needs from the state, call a family to do the work, write the result back. Families and root files do the work and are never nodes.

## A folder is a graph

Everything under `src/flow/` is steps. A folder is a graph. Its `__init__.py` is the one place that wires the files beside it into that graph: this node, then that, and where each decision leads. Nothing else lives in it. The files in the folder are the nodes.

A step made of smaller steps is a folder of its own, with its own `__init__.py` and its own graph. The parent adds that whole graph as one node, named after the folder. So:

```
flow/
  __init__.py        graph 0: agent_1, then agent_2, then agent_3
  agent_1/
    __init__.py      graph 1: agent 1's own steps, wired here
    step_a.py
    step_b.py
    decide_c.py
  agent_2/
    __init__.py      graph 2
    ...
  agent_3/
    __init__.py      graph 3
    ...
```

Four `__init__.py` files, four graphs. Graph 0 has three nodes, and each of those nodes is the graph built in the folder below it. If `step_b` is itself made of steps, `agent_1/step_b/` gets its own `__init__.py` and that is graph 5.

Going deeper is zooming in: the same story told in finer steps. The trace nests the same way, a span for `agent_1`, inside it a span for each of its steps. Where the break is, the depth says how far to zoom.

`src/__init__.py` is not a graph. It is the entry, `class Agent(Base)`; it takes the top graph that `flow/__init__.py` built and runs it. A family folder's `__init__.py` is not a graph either; it is empty, there only so Python treats the folder as a package.

## Imports

A step imports down into the graph under it and across into a family. Nothing imports `flow/`. The families never import a step.

## Size is the signal

A step file past about 150 lines, or whose one-line description needs "and", is several steps. It becomes a folder with its own graph. Build it as briefed and say so in the report; do not split it yourself, because the tree is agreed in discussion.

## The worked example

The flow of a made-up agent that answers a question from a folder of notes:

```
flow/
  __init__.py           graph 0: the whole story in five steps
  read_question.py      step: the user's line goes into the state
  find_notes.py         step: the notes that bear on it
  enough.py             decision: enough to answer, or look again
  answer/               graph 1: the "answer" step opened up
    __init__.py         draft, then check
    draft.py            step: write the answer from the notes found
    check/              graph 2: the "check" step opened up
      __init__.py       extract, match, verdict
      extract.py        step: list every claim the draft makes
      match.py          step: find a note behind each claim
      verdict.py        decision: all backed, or send the draft back
  reply.py              step: the line the user sees
```

Read graph 0 and you have the story: read the question, find notes, decide if that is enough, answer, reply. Open `answer/` and the one word becomes draft, then check. Open `check/` and check becomes extract, match, verdict. `check/extract.py` calls `claims/split.py`; `check/match.py` calls `claims/backing.py`; those families are in the `one-job-per-file` example.
