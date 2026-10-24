# Discussion: the shape of the examiner

Where the design landed in the sessions of 2026-10-22 and 2026-10-23, as it
bears on the examiner. Imported on 2026-10-24 from `agents/judge/discussion.md`
and `agents/judge/eval_design.md`, which remain the design of how a run is
executed and graded. This file holds what the examiner must know to author.
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
| **`examiner`** | Learns the target: its description, its tools, where its state lives and where fake state can be planted. Clears its open questions with the user. Drafts scenarios, walks the user through them, saves the accepted ones to the pool. Reads the judge's results to propose the next ones. Never runs anything. |
| **`judge`** | Given scenario names, runs them, many at once, planting the state, starting the target as a process, feeding it, restarting it when the path says a new conversation begins, reading the trace, grading. Writes results to the pool. |
| **Simulated user** | A character living through the scenario: a persona, the facts it is allowed to know, a memory of everything it has already told the target, and what it wants now. Composes its own words. Lives inside the judge. The examiner writes the character; the judge plays it. |

The scenario says when the simulated user speaks and what it wants; the
simulated user decides how to say it. Nobody improvises a fact the scenario
did not give. This is the fence, and the examiner is the one who has to give
every fact.

## What the examiner must know about the target

To write trajectory lines the examiner must know the target's tools and what
a sound use of them looks like. Pointing the examiner at a target means
giving it that, not just the name: the description from `list_of_agents.md`,
the MCP servers in the target's `base_settings.json` and the tools they
expose, and where the target's state lives (`data/`, a fake folder, a
backing store behind a server). Whether it also reads the target's code is
open.

## A scenario

A data file in one fixed shape, authored by the examiner, vetted by the
user. Not code: the judge composes and reorders scenarios, and code that
runs cannot be composed. Where a scenario needs code, planting a fake folder
or checking an end state, that is a named step inside the shape, a line or
two.

| Part | Holds | Present |
|---|---|---|
| **Plant** | The fake state the target starts from, or the delta on the state of the scenario it needs. | always |
| **Checklist** | The lines the target must do, each with its check shape and its must or should tier. Written against the state as planted. | always |
| **Needs** | Which scenario this one stacks on, if any. | always, may be empty |
| **User** | Persona, what the user knows, what the user wants, at which point they come. | when the target converses |
| **Clock** | What day it is for the target, and how time moves between rungs. | when the target reasons about dates |

A target that runs without a user does its job and exits; the scenario has
no user part. A timeless target has no clock part and stacks by "the output
of A is the input of B".

## The plant

- The starting state must be constructible from a file: fake inbox,
  calendar, folder, database, created before the run and thrown away after.
  An agent that only talks to the real service cannot be graded this way.
- A scenario that stacks on another plants a delta, not a fresh world: the
  target walks into the rung carrying its own memory and a changed world.
- **Training leak.** A scenario set in a period the target model saw in
  training lets it answer from memory instead of from the data, and the
  judge cannot tell. Every planted date is after the target model's training
  cutoff, or the values cannot exist in any training set; the first covers
  the second. The examiner must know the cutoff per model and asks the user
  when it does not.
- Where the target reasons about dates, the planted dates and the clock part
  must agree.

## The checklist

Binary lines, never a graded scale. Six to fifteen per scenario. Each names
one concrete observable thing a careful stranger could check by looking.
"Mentions the 14-day refund window" is a line; "handles the refund policy
correctly" is a scale in disguise and is not allowed.

Faults to avoid:

- Compound lines ("lists both invoices and their due dates" is two).
- Hidden reference ("gives the right answer" with the answer not written beside it).
- Unobservable intent ("understands the goal"; write "asks which account before transferring").
- No negative lines. Most real failures are things that should not appear; every checklist has some "does not" lines.

Every checklist has lines on the reply and lines on the trajectory, because
a wrong trajectory can produce a right reply by luck. An agent that guesses
the right reply from the inbox alone passes the reply lines and fails the
trajectory lines, and the result shows the reply was not earned. Where the
target writes rather than reads, lines move to the end state.

Every line carries its reason, naming the planted fact it rests on ("does not
list the rent, because the bank feed shows it paid Monday"), so the user can
check the examiner's reasoning when vetting.

**Tiers.** Each line is a *must* (failure makes the reply wrong: listed the
rent, called send) or a *should* (quality: under 150 words, due dates given).
A scenario passes only if every must line passes on every variant. Should
lines are reported, never gate. Whether the conversation read well is always
a should line.

**Shapes.** A check is not fresh code. It is one of a fixed set of shapes with
parameters, picked and filled by the examiner at authoring time, executed by
the judge at grading time:

| Shape | Parameters |
|---|---|
| tool called | tool name |
| tool not called | tool name |
| tool argument matches | tool name, argument, expected value |
| tool A before tool B | two tool names |
| reply contains | string or pattern |
| reply does not contain | string or pattern |
| reply length under | number |
| file exists / file matches | path, expected content |

In order of preference a line is answered by code (end state, then
trajectory, then a stable string in the reply), else by a model reading the
reply for a narrow yes or no, else by the user. A line that fits no shape is a
signal: it belongs to the prose layer, or the plant did not expose the fact
well enough, in which case fix the plant rather than accept a model grader.
Fresh code is kept for end-state checks that are genuinely scenario-specific,
a line or two against the planted folder.

Tool arguments should be structured on the target's side (a date range field,
not a free-text query), or argument lines are impossible; the examiner says
so when a target's tools make a line unwritable.

**Drift** is a checkable line the judge discovers live, not one the examiner
writes: a turn that contradicts the planted state or an earlier turn.

## Variants

One scenario keeps one plant and one checklist and carries several ways of
asking: terse, chatty, with a typo, general then specific, a detail given up
front or withheld. The variation is in the request only; the checklist must
stay valid for every variant. "What did I pay last month" is a different
scenario, not a variant, and a generating model drifts into that kind, so
the examiner checks each variant against the checklist before showing it.
Different models phrase differently, so models are rotated when generating.
Variants are generated once, stored in the scenario file, vetted with the
rest, then fixed. Each run of a scenario is one run per variant.

Variants made by changing one planted fact at a time are a separate, cheap
way to grow the pool and are where agents break: flip the state so rent is
unpaid and "does not list the rent" becomes "lists the rent due Friday". That
is a new scenario with its own checklist, not a variant.

## Vetting

An examiner that invents a scenario also invents what correct looks like for
it, and may get that wrong. Model-generated scenarios are good at finding
breaks and unreliable at certifying passes. So nothing joins the pool
without the user: the examiner walks the user through each draft, the user
corrects or accepts, and only accepted scenarios are saved. The user is
agreeing with the examiner's reasoning line by line, which is why every line
carries its reason.

## Reading the judge's results

The answer key is written from failures, not from theory. A checklist written
before any run lists what one imagines matters and misses what the agent
actually does wrong. So the loop is: the judge runs the vetted scenarios,
groups failures by line and by variant, writes a one-line note per trace no
line caught, sorts the notes into piles, and reports with counts and trace
ids. The examiner reads that report and proposes: a confirmed pile becomes
one line with a check shape; the traces it came from become scenarios, the
day's state frozen into a plant with the request kept. The user says which
piles are real before any of it is drafted. A judge-found failure is a lead,
not a verdict: simulated users are wrong often enough that a visible share of
"failures" are the simulated user's fault.

A failure on one variant only is itself a finding: the target is sensitive
to phrasing.

## The pool

`scenarios/<target>/`, one file per scenario, the judge's results beside
them. Tracked in git, since the user vetted every file in it. The examiner
writes scenarios there and reads results from there; it reads nothing else
of the judge's.

## `src/` so far

Drafted and not objected to, nothing written:

- `flow/`, graph 0: learn the target, clear questions, draft, walk through, save, read results.
- `target/` family: `describe.py`, `state.py`.
- `scenario/` family: `draft.py`, `variants.py`, `pool.py`.

## Open

- The steps inside `flow/`, in detail.
- Whether the examiner sees the target's code or only its description, tools and state.
- The exact shape of a scenario file: format and field names for the five parts, the check shapes and the variants. Agreed in words, not written down.
- Where each model's training cutoff is recorded, so the examiner can plant past it.
- Planting for a target whose state lives behind an MCP server that talks to a real service (the ledger and Telegram): the server needs a swappable backing store, or the examiner cannot write a plant for it.
