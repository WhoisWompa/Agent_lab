# Discussion: the shape of the examiner

Where the design stands after the sessions of 2026-10-22 to 2026-10-28. The
judge's `discussion.md` and `eval_design.md` are the design of how a run is
executed and graded; this file holds what the examiner must know to author,
and the scenario file's shape, which both agents read. Where `eval_design.md`
says the judge writes a scenario, a criterion or a variant, it was written
before the split; since the split that work is the examiner's. Anything still
open is in the last section.

## Two agents and a character

One agent in the first draft, now two, because one process is one chat and
the user wants to talk to the scenario-writer and the scenario-runner on
separate occasions, in parallel. The user starts both; neither starts the
other. They share the pool under `scenarios/` at the repo root and nothing
else.

| Who | What it does |
|---|---|
| **`examiner`** | Learns the target from its README, its tools and where its state lives. Writes the target's decision list and always-lines, with the user. Drafts scenarios one at a time, one per cell of the grid, walks the user through each, saves the accepted ones to the pool. Reads the judge's results to propose new rows. Never runs anything. Knows nothing about who the user is or how scenarios stack. |
| **`judge`** | Enumerates paths through the pool by code, shows the list, runs the approved paths many at once, flips the switches as it plants each step, checks every line against the switches as they stand, and writes results to the pool. |
| **Simulated user** | A character the judge plays through a whole path: a persona, a memory of everything it has already told the target, and on each turn what the scenario says it wants. Composes its own words. Lives inside the judge. Written from the target's `logs/` once the target has been used for real. |

The scenario says what the user knows and what they want on each turn; the
simulated user decides how to say it. Nobody improvises a fact the scenario
did not give. This is the fence, and the examiner is the one who has to give
every fact.

## The unit is a decision

An agent is a thing that makes decisions, so the test is: every decision the
target makes, in every direction it can go. A decision is a question the
target has to answer where answering it wrong changes what the user sees.
"Is this a reply owed?" is one. "Open the Telegram connection" is not, there
is no judgment in it. If a clear yes case and a clear no case cannot both be
written, it is a step, not a decision.

The thousand ways a person could use the target all land on the same few
decisions. Phrasing is covered by variants on a turn, history by the judge's
stacking. Neither is written as a scenario.

## What the examiner reads on its own

Pointing the examiner at a target is naming it. From the name it reads:

- the target's `README.md`, which must say what the target decides and how a
  person talks to it, not only what it does;
- the target's row in `list_of_agents.md`;
- the tools of the MCP servers in the target's `base_settings.json`: names,
  arguments, descriptions. A tool's interface is not its implementation;
- the layout of the target's `data/`, since a data entry is keyed by the path
  the target reads;
- a few real records of the data the target works with, which the user puts
  in `agents/<target>/test data/`. Gitignored, so they stay on the user's
  machine. Read once, on the first run for that target, so the examiner gets a
  feel for what the target usually deals with: who writes, about what, how
  messy, in what shape. Its first job on that run is to write what it learned
  into its notes; every later run loads the notes and never opens the samples
  again. That is a rule in the entry, not in the prompt: the samples are given
  only when there is no notes file for the target.

It never reads the target's code. What the user talks like is the judge's
problem, not the examiner's; the examiner's realism is realism of the world
and of the wants.

## Once per target: two files in the pool

Before any scenario, the examiner writes two files in `scenarios/<target>/`
and the user vets each.

**`decisions.yaml`** is the decision list: every decision the target is known
to make, one entry each, with a short name, the question, a clear yes case, a
clear no case, and the borderline cases the user has named. It is the map of
the whole test and the source of every switch name. It is complete as far as
anyone can tell, never more, and it grows from the judge's failures.

**`always.yaml`** is the lines that go in every scenario of this target,
whatever decision the scenario tests: read the source before answering, invent
nothing, reply under some length, finish within the scenario's turns, never say
it will act on the user's behalf. Plus the path rules, which hold across a
whole stack and not one reply: never list a date that has passed, never report
a thing as open after the message that closed it. All specific to the target.
Stamped onto every scenario by the judge; the scenario file does not repeat
them.

## The grid

Decisions down the side, directions across: yes, no, each borderline case the
user named. Every cell is one scenario. An empty cell is a hole by definition,
so the examiner never looks for holes; it reads them off. Drafting means
picking an empty cell and filling it. A scenario is only drafted to fill a
cell. When no cell is empty the examiner says so, with the count, and stops;
the user may ask for more, the examiner never proposes more on its own.

Decisions are never paired. A scenario tests one decision going one way, so a
failure names the decision. Interactions between decisions are the judge's,
by stacking.

A hole noticed while drafting, "what if Sam said no rush?", is a new borderline
on that decision's row, and so a new empty cell. The list is the hole list.

## Drafting one scenario

Checklist first, then the world around it. The line is the test; the scenario
is the smallest world in which the line can be checked.

1. Pick an empty cell: a decision and a direction.
2. Write the line. The user rules on it before anything else is written,
   because if the line is wrong the rest is wasted. A borderline cell's answer
   is the user's; the examiner cannot guess it.
3. Plant the one message that makes the line checkable, then two or three
   around it so the right answer is not the only thing in the data.
4. The turns: what the user wants, never the words.
5. The story, one paragraph.
6. Show the whole draft. The user corrects or accepts.
7. Save. Next empty cell.

What the drafter is given: the cell, the always-lines, the notes it has
learned about this target, and the names of the existing scenarios with one
line each, so it does not reuse a name or plant Sam asking the same thing
twice. Never the full text of earlier scenarios: a model that reads them
writes something similar enough. Two scenarios differ because their cells
differ, and that is enforced by what they are.

Two other ways to draft, beside the grid:

- **Flip one fact.** Take an accepted scenario and change one planted thing:
  Sam adds "no rush", the rent is now unpaid. The line flips with it. This one
  reads a previous scenario on purpose, because the similarity is the point: a
  failure is pinned to that one fact. The usual way to fill a borderline cell.
- **A whole day.** Much later, once the grid is full: a realistic day with no
  particular decision in mind, run to see whether anything happens that no row
  covers. For finding missing rows, not for filling cells.

## What the examiner remembers

What the user corrects in one draft must carry into the next, or the examiner
invents the same wrong world again. It keeps one note per target under its
own `data/`: what the real data looks like, learned from the samples on the
first run, and which rulings the user gave. This
is not the persona, which is the judge's; it is the texture of the world and
the answers to the borderline cases.

## Switches

Stacking changes right answers. A plants Sam asking for 40; B plants "sent
it". A then B: after B the 40 must not be listed. B then A: after A it must.
Same two files, opposite right answers, decided by order. No line written as
"lists the 40" survives that.

So scenarios and lines are joined by switches, and the code does the joining.

- The decision list defines the switches. Each decision is a kind of switch;
  an instance is named `<decision>.<instance>`: `owed.sam`, `date.dentist`,
  `reply.jo`.
- A planted data entry says which switches it `sets` and which it `clears`.
  A scenario leaves alone any switch it does not name.
- A checklist line may hang on one switch with `when`. On: the check must
  pass. Off: its negation must pass. Only functions with a negation take
  `when`: `reply_contains`/`reply_does_not_contain`, `tool_called`/
  `tool_not_called`, `reply_lists`/its complement, `file_exists`/its absence,
  `ask_model`/the answer no. A line without `when` is checked once, on its
  own scenario's turn.
- The judge walks a path in order, flipping switches as it plants each step.
  At any step every switch is whatever the last scenario that touched it left
  it as. A stack of fifteen is the same loop as a stack of two.
- At a turn marked `full`, the user asking for everything that is open, the
  judge checks every `when` line in the pool so far against the switches as
  they stand. A narrow turn, "where do things stand with Sam", checks only its
  own scenario's lines.

No model is anywhere in this. The judge's model calls, the simulated user and
the graders, never see a switch name.

## A scenario

One folder per scenario, a YAML file and the data files that do not fit
inline. Authored by the examiner, vetted by the user, read by the judge.
Not code: the judge composes and reorders scenarios, and code that runs
cannot be composed.

```
scenarios/<target>/
  decisions.yaml
  always.yaml
  <name>/
    scenario.yaml
    <data files, when not inline>
```

```yaml
name: <scenario name>                    # required, matches the folder
target: <agent name>                     # required, matches the parent folder
decision: <name from decisions.yaml>     # required
direction: <yes | no | the borderline case's name>   # required

context: >                               # required
  <the story, one paragraph>

data:                                    # optional; key = path under the sandbox's data/; dates as offsets from now
  <file name>:
    description: <the truth about this data, in words>
    format: <json | csv | text | folder | ...>
    source: <where it came from: invented, a dataset, an export>
    sets: [<switch>, ...]                # optional
    clears: [<switch>, ...]              # optional
    content: <inline value>              # or:
    file: <file beside scenario.yaml>

conversation:                            # optional; absent when the target runs without a user
  knows: [<data keys the user is allowed to know>]
  turns:
    - wants: <what the user is after on this turn>
      full: true                         # optional; the user asks for everything open
      variants:                          # optional; without it the simulated user phrases it
        - <the ask, one way>
        - <the ask, another way>
    - wants: <the next thing>

checklist:                               # required: the decision line(s); the always-lines are not repeated here
  <line name>:
    description: <what this line checks, for the user to read>
    check: <judge function>(<arguments>)
    severity: <error | warning>
    when: <switch>                       # optional; see Switches
    canary: true                         # optional; see Canaries
```

At least one of `data` or `conversation` is present, or there is nothing for
the target to do. `name` and `target` are inside the file so it says what it
is wherever it is read; the judge refuses a scenario whose path disagrees
with them, or whose `decision` is not in `decisions.yaml`.

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
step.

### Context

The story in one paragraph. For the person vetting, and the judge hands it
to the simulated user as background.

### Conversation

Only what this ask needs. `knows` lists the data keys whose contents the
simulated user may draw on; that is the fence written down. `turns` is the
wants in order, each what the user is after on that turn, never the words.
`variants` on a turn fixes several ways of asking it; without it the simulated
user phrases the want. The conversation ends after the last turn; a target
still asking questions then has failed the always-line that says so.

Who the user is, the persona, the voice, the memory across steps, is the
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
| `never_after` | two switch or tool names | code, over the whole path; `always.yaml` only |

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
- No negative lines. Most real failures are things that should not appear; the
  no cases of the grid and the `when` flips supply them.

Every scenario has lines on the reply and, through the always-lines, lines on
the trajectory, because a wrong trajectory can produce a right reply by luck.
Where the target writes rather than reads, lines move to the sandbox's files.

## Writing so that scenarios stack

Every scenario is complete on its own; the judge picks which to stack and in
what order. Three rules on the examiner's side make any order work:

- **Data adds, never replaces.** When B lands on A, B's `inbox.json` is appended to A's, not written over it; the format says how. The target's memory of A is never contradicted by a vanished world, only by new things.
- **Offsets are from the step's own now.** The dentist is due `+3d` whichever step the scenario is.
- **A line names only its own data, through its switch.** "Lists the dentist" and "does not list the rent as owed" point at things in this scenario's files and flip with their switches whatever ran before. "Lists nothing else" is banned; `reply_lists` is an includes, never an equals.

A line that would need voiding under some stack is a wrong line, and the
examiner fixes it. The judge never drops a line.

Inventing is caught by the judge, not by a line: every item the target claims
is looked for in the data of every step so far, and an item planted nowhere
is a false claim. The judge's own added checks never enter the scenario file
and are reported apart from the vetted ones.

## Variants

The variation is in the ask only; the checklist must stay valid for every
variant. "What did I pay last month" is a different scenario, not a variant,
and a generating model drifts into that kind, so the examiner checks each
variant against the checklist before showing it. Models are rotated when
generating, since different models phrase differently. Variants are
generated once, vetted with the rest, then fixed.

## Vetting

An examiner that invents a scenario also invents what correct looks like for
it, and may get that wrong. Model-generated scenarios are good at finding
breaks and unreliable at certifying passes. So nothing joins the pool
without the user: the decision list, the always-lines, and every scenario,
line first. Each is vetted once and reused on every run and every rebuild of
the target. The rulings on the borderline cases are the one thing that stays
the user's, because they are what the user wants, not a fact anyone can check.

## Canaries and the broken target

An all-pass is suspect, and the pool must prove it can fail.

- **Canaries** are lines that must always fail: a `reply_contains` for a word
  planted nowhere, an `ask_model` whose honest answer is always no. Their
  `description` and `check` read like any ordinary line. The mark is the
  `canary` key, which the judge's code reads and no prompt ever contains, so
  the graders cannot know. A canary that passes means the judge is broken.
- **The broken target** is the same pool run against the target with a tool
  removed, a cheaper model, or a blank system prompt. If nothing fails, the
  pool has no teeth. This tests the pool; the canary tests the judge.
- **The no cases** mean the grid cannot be passed by a trivial strategy: a
  target that lists everything fails every no case, one that lists nothing
  fails every yes case.
- An all-pass on a pool's first run is flagged by the judge as a reason to run
  the broken-target check before believing it.

What the user reads is the number of `ask_model` lines, not the number of
scenarios: code lines cannot quietly pass when they should not.

## Paths are code

A path is a list the judge's code builds before the run: plant A, A's turns,
check; plant B on top, B's turns, check; restart the target; plant C, and so
on. Every scenario alone, every ordered pair both ways, a few seeded long
orders with a restart dropped in. The judge shows the list, the user approves
it, the code runs it. Nothing is chosen mid-run, so the same seed gives the
same paths tomorrow and a failure can be reproduced. A path has a ceiling on
turns, as a budget; a scenario the ceiling kept from running is not run, not
failed.

## Reading the judge's results

The answer key is written from failures, not from theory. The judge runs
the paths, groups failures by decision and by variant, writes a one-line note
per trace no line caught, sorts the notes into piles, and reports with
counts and trace ids, its own checks apart. The examiner reads that report
and proposes what each pile is: a new decision, usually one about relating
things across time ("which earlier promise does this message close?"), which
gets a row and is then tested by single scenarios like any other; or a new
always-line, when it is about how the target works rather than what it
judges. The user says which piles are real before any of it is drafted. A
judge-found failure is a lead, not a verdict: simulated users are wrong often
enough that a visible share of "failures" are the simulated user's fault. A
failure on one variant only is itself a finding: the target is sensitive to
phrasing.

## The pool

`scenarios/<target>/`, the two per-target files, one folder per scenario, the
judge's results beside them. Tracked in git, since the user vetted every
scenario in it. The examiner writes there and reads results from there; it
reads nothing else of the judge's.

## `src/`

The flow, as settled:

1. Pick the target; learn it.
2. Decision list: draft, show, correct until accepted, save.
3. Always-lines: the same.
4. Scenarios: pick a cell, line, rule, data, turns, story, vet, save; until
   the grid is full.
5. Results: read, propose, rule, back to 2.

Steps 2 and 3 happen once per target. Step 4 is a subgraph. Step 5 is the
loop that never ends. The tree and signatures are agreed in discussion one
slice at a time before the builder writes them.

## Open

- Planting for a target whose state lives behind an MCP server that talks to a
  real service (the ledger and Telegram): the server needs a swappable backing
  store, or the examiner cannot write a data entry for it.
- The target README's two sections, "what it decides" and "how you talk to
  it": their shape, and writing the ledger's, which is empty.
- The judge's side of today's decisions: the switch walk, the `full` turn,
  carried `when` lines, `never_after`, canaries, the broken-target run, path
  enumeration by code, the turn ceiling. To be carried into the judge's
  `discussion.md`.
- How many canaries per target, and whether they live in `always.yaml` or in
  one scenario of their own.
