# Discussion: the shape of the examiner

Where the design stands after the sessions of 2026-10-22 to 2026-10-24. The
judge's `discussion.md` and `eval_design.md` are the design of how a run is
executed and graded; this file holds what the examiner must know to author.
Where `eval_design.md` says the judge writes a scenario, a criterion or a
variant, it was written before the split; since the split that work is the
examiner's. Anything still open is in the last section.

## Two agents and a character

One agent in the first draft, now two, because one process is one chat and
the user wants to talk to the scenario-writer and the scenario-runner on
separate occasions, in parallel. The user starts both; neither starts the
other. They share the pool under `scenarios/` at the repo root and nothing
else.

| Who | What it does |
|---|---|
| **`examiner`** | Learns the target: its description, its tools, where its state lives. Clears its open questions with the user. Drafts scenarios one at a time, each complete on its own, walks the user through them, saves the accepted ones to the pool. Reads the judge's results to propose the next ones. Never runs anything. Knows nothing about who the user is or how scenarios stack. |
| **`judge`** | Told which scenarios and what the user wants to find out, proposes the path: the order, the gaps, the restarts, the persona it will play, which lines it will skip or add under that stack, with its reasons. The user approves, then it runs, many paths at once, and writes results to the pool. |
| **Simulated user** | A character the judge plays through a whole path: a persona, a memory of everything it has already told the target, and on each turn what the scenario says it wants. Composes its own words. Lives inside the judge. |

The scenario says what the user knows and what they want on each turn; the
simulated user decides how to say it. Nobody improvises a fact the scenario
did not give. This is the fence, and the examiner is the one who has to give
every fact.

## What the examiner must know about the target

To write trajectory lines the examiner must know the target's tools and what
a sound use of them looks like. Pointing the examiner at a target means
giving it that, not just the name: the description from `list_of_agents.md`,
the MCP servers in the target's `base_settings.json` and the tools they
expose, and where the target's state lives under `data/`, since data entries
are named by the path the target reads. Whether it also reads the target's
code is open.

## A scenario

One folder per scenario, a YAML file and the data files that do not fit
inline. Authored by the examiner, vetted by the user, read by the judge.
Not code: the judge composes and reorders scenarios, and code that runs
cannot be composed.

```
scenarios/<target>/<name>/
  scenario.yaml
  <data files, when not inline>
```

```yaml
name: <scenario name>                    # required, matches the folder
target: <agent name>                     # required, matches the parent folder

context: >                               # required
  <the story, one paragraph>

data:                                    # optional; key = path under the sandbox's data/; dates as offsets from now
  <file name>:
    description: <the truth about this data, in words>
    format: <json | csv | text | folder | ...>
    source: <where it came from: invented, a dataset, an export>
    content: <inline value>              # or:
    file: <file beside scenario.yaml>

conversation:                            # optional; absent when the target runs without a user
  knows: [<data keys the user is allowed to know>]
  turns:
    - wants: <what the user is after on this turn>
      variants:                          # optional; without it the simulated user phrases it
        - <the ask, one way>
        - <the ask, another way>
    - wants: <the next thing>

checklist:                               # required
  <line name>:
    description: <what this line checks, for the user to read>
    check: <judge function>(<arguments>)
    severity: <error | warning>
```

At least one of `data` or `conversation` is present, or there is nothing for
the target to do. `name` and `target` are inside the file so it says what it
is wherever it is read; the judge refuses a scenario whose path disagrees
with them.

### Data

One entry per file the judge plants. The key is the path under the sandbox's
`data/`, which is the path the target reads, so the scenario carries no
planting field: the examiner learns the target's layout and names entries to
match. `description` is the only place the truth about the data lives, in
words, for the person vetting and for the judge verifying claims; the target
never sees it. `format` says how the judge writes the file. `source` says
where the data came from. The data itself is `content` inline or `file`
beside the YAML, one of the two; a CSV or a folder is always a file.

No absolute date anywhere. Every date is an offset from now, `+3d`, `-1d`,
in the content and in the description, and the judge resolves it against the
real clock when it plants. Any model, any day, the dates are fresh and past
any training cutoff, and a scenario placed later on a path moves with its
rung.

### Context

The story in one paragraph. For the person vetting, and the judge hands it
to the simulated user as background.

### Conversation

Only what this ask needs. `knows` lists the data keys whose contents the
simulated user may draw on; that is the fence written down. `turns` is the
wants in order, each what the user is after on that turn, never the words.
`variants` on a turn fixes several ways of asking it; without it the simulated
user phrases the want. The conversation ends after the last turn.

Who the user is, the persona, the voice, the memory across rungs, is the
judge's, one character per target, so two stacked scenarios never disagree
about the person.

### Checklist

Named lines, each yes or no. `description` is for the person vetting, one
short sentence. `check` is which judge function answers the line and its
arguments, plain values only: a tool name of the target, a word or phrase, a
number, a path, a question. `severity` is `error`, a fail fails the scenario,
or `warning`, reported and not gating.

The judge functions a check may name:

| Function | Arguments | Answered by |
|---|---|---|
| `tool_called` | a tool name of the target | code, from the trace |
| `tool_not_called` | a tool name of the target | code, from the trace |
| `tool_before` | two tool names | code, from the trace |
| `tool_argument` | a tool name, an argument name, the expected value | code, from the trace |
| `reply_contains` | a word or phrase | code, from the reply |
| `reply_does_not_contain` | a word or phrase | code, from the reply |
| `reply_length_under` | a number of words | code, from the reply |
| `reply_lists` | what to extract, the data keys it must include | a model extracts a set, code compares |
| `file_exists` | a path in the sandbox | code, from the sandbox |
| `file_matches` | a path, the expected content | code, from the sandbox |
| `ask_model` | a yes-or-no question | a model |

Code first: a code line is free, gives the same answer every run, and is
believed when it fails. `ask_model` is for the line no other function can
answer, and every such line is one the user will later have to check the
grader on. An offset in a check argument is resolved the same way as in the
data, so `reply_contains("+3d")` reads as the resolved date at run time.

Each line names one concrete observable thing a careful stranger could check
by looking. Faults to avoid:

- Compound lines ("lists both invoices and their due dates" is two).
- Hidden reference ("gives the right answer" with the answer not written beside it).
- Unobservable intent ("understands the goal"; write "asks which account before transferring").
- No negative lines. Most real failures are things that should not appear; every checklist has some "does not" lines.

Every checklist has lines on the reply and lines on the trajectory, because a
wrong trajectory can produce a right reply by luck. Where the target writes
rather than reads, lines move to the sandbox's files.

## Writing so that scenarios stack

Every scenario is complete on its own; the judge picks which to stack and in
what order, since A then B tests memory and B then A tests hallucination with
the same two files. Three rules on the examiner's side make any order work:

- **Data adds, never replaces.** When B lands on A, B's `inbox.json` is appended to A's, not written over it; the format says how. The target's memory of A is never contradicted by a vanished world, only by new things.
- **Offsets are from the rung's own now.** The dentist is due `+3d` whichever rung the scenario is.
- **A line names only its own data.** "Lists the dentist" and "does not list the rent as owed" point at things in this scenario's files and stay true whatever ran before. "Lists nothing else" is banned, because it breaks the moment another scenario sits underneath; `reply_lists` is an includes, never an equals.

Inventing is caught by the judge, not by a line: every item the target claims
is looked for in the data of every rung so far, and an item planted nowhere
is a false claim. The judge's own added lines never enter the scenario file
and are reported apart from the vetted ones.

## Variants

The variation is in the ask only; the checklist must stay valid for every
variant. "What did I pay last month" is a different scenario, not a variant,
and a generating model drifts into that kind, so the examiner checks each
variant against the checklist before showing it. Models are rotated when
generating, since different models phrase differently. Variants are
generated once, vetted with the rest, then fixed.

Changing one planted fact at a time is a separate, cheap way to grow the
pool and is where agents break: flip the state so rent is unpaid and "does
not list the rent" becomes "lists the rent due Friday". That is a new
scenario with its own checklist, not a variant.

## Vetting

An examiner that invents a scenario also invents what correct looks like for
it, and may get that wrong. Model-generated scenarios are good at finding
breaks and unreliable at certifying passes. So nothing joins the pool
without the user: the examiner walks the user through each draft, the user
corrects or accepts, and only accepted scenarios are saved.

## Reading the judge's results

The answer key is written from failures, not from theory. The judge runs
the paths, groups failures by line and by variant, writes a one-line note
per trace no line caught, sorts the notes into piles, and reports with
counts and trace ids, its own added lines apart. The examiner reads that
report and proposes: a confirmed pile becomes one line with a judge
function; a judge line that keeps finding something becomes a proposal for a
real line. The user says which piles are real before any of it is drafted. A
judge-found failure is a lead, not a verdict: simulated users are wrong often
enough that a visible share of "failures" are the simulated user's fault. A
failure on one variant only is itself a finding: the target is sensitive to
phrasing.

## The pool

`scenarios/<target>/<name>/`, one folder per scenario, the judge's results
beside them. Tracked in git, since the user vetted every scenario in it. The
examiner writes scenarios there and reads results from there; it reads
nothing else of the judge's.

## `src/` so far

Drafted and not objected to, nothing written:

- `flow/`, graph 0: learn the target, clear questions, draft, walk through, save, read results.
- `target/` family: `describe.py`, `state.py`.
- `scenario/` family: `draft.py`, `variants.py`, `pool.py`.

## Open

- The steps inside `flow/`, in detail.
- The examiner's input: how it is pointed at a target and what the user says to it.
- Whether the examiner sees the target's code or only its description, tools and state.
- Planting for a target whose state lives behind an MCP server that talks to a real service (the ledger and Telegram): the server needs a swappable backing store, or the examiner cannot write a data entry for it.
