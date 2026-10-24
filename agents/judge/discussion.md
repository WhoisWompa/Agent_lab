# Discussion: the shape of the judge

Where the design landed in the sessions of 2026-10-22 and 2026-10-23.
`eval_design.md` covers how one run is graded: binary criteria, check
shapes, error and warning lines, the user vetting what the judge invents. This
file covers the judge as a whole: its roles, what a scenario is, how runs are
composed, and the sandbox they run in. Anything still open is in the last
section.

## Two agents and a character

The judge was one agent in the first draft. It is now two, because one
process is one chat and the user wants to talk to the scenario-writer and the
scenario-runner on separate occasions, in parallel. The user starts both;
neither starts the other. They share the pool under `scenarios/` at the repo
root and nothing else.

| Who | What it does |
|---|---|
| **`examiner`** | Learns the target: its description, its tools, where its state lives and where fake state can be planted. Clears its open questions with the user. Drafts scenarios, walks the user through them, saves the accepted ones to the pool. Reads the judge's results to propose the next ones. Never runs anything. |
| **`judge`** | Given scenario names, runs them, many at once: one runner per path, each planting the state, starting the target as a process, feeding it, restarting it when the path says a new conversation begins, reading the trace, grading. Writes results to the pool and tells the user what passed and what broke. |
| **Simulated user** | A character living through the scenario: a persona, the facts it is allowed to know, a memory of everything it has already told the target, and what it wants now. Composes its own words. Lives inside the judge, so its memory survives a target restart. Present only when the scenario has a user part. |

The scenario says when the simulated user speaks and what it wants; the
simulated user decides how to say it. Nobody improvises a fact the scenario
did not give. This is the fence.

The judge starts the target as `python -m agents.<target>`, never imports it:
restart is the test, the folder is the sandbox, the chat is the surface under
test, one process is one trace, and a crash stays in the target.

## A scenario

One folder per scenario under `scenarios/<target>/<name>/`: a YAML file
and the data files that do not fit inline. Authored by the examiner, vetted
by the user. Not code: the judge composes and reorders scenarios, and code
that runs cannot be composed. The exact shape, with the judge functions a
check may name, is in `agents/examiner/discussion.md`. What the judge needs
from it: `data`, one entry per file to plant, keyed by its path under the
sandbox's `data/`, every date an offset from now; `conversation`, what the
simulated user knows and wants on each turn; `checklist`, named lines each
naming one judge function and its arguments, with severity `error` or
`warning`. Every scenario is complete on its own and says nothing about who
the user is or what it stacks on.

A target that runs without a user does its job and exits; the judge sees
only output and end state. A timeless target, a data-analysis job, stacks by
"the output of A is the input of B". The year-long simulation of a calendar
agent is the hard end of the same shape, not a different shape.

## A run is a path through the pool

Scenarios stack: A alone, or A then B, or B then A. No scenario depends on
another; the judge picks the order, since A then B tests memory and B then A
tests hallucination with the same two files. It owns one target process
across the path. Each rung's data is added onto what is already planted,
never written over it, and its offsets are resolved from the rung's own now.
The target walks into each rung carrying its own memory and a grown world.

Told which scenarios and what the user wants to find out, the judge proposes
the path first: the order, the gaps, the restarts, the persona it will play,
and which checklist lines it will skip or add under that stack, each with
its reason. The user approves, then it runs. The judge's own lines never
enter a scenario file and are reported apart from the vetted ones.

At any point on the path the judge may re-ask an earlier scenario. The
simulated user composes the re-ask from its memory ("that appointment I
mentioned"), never the original words. The judge, having read the pool,
knows which earlier lines a later rung has made moot and does not re-ask
those.

**New conversation** is one move on the judge's menu: stop the target,
which runs its save hook and exits, then start it again. Disk memory under
`data/` survives, context does not. The simulated user remembers either way.
This separates two kinds of forgetting, reported apart:

| Forgetting | Caught by |
|---|---|
| Within a conversation: long context, drift | re-asking in the same process |
| Across conversations: did it save what mattered | re-asking after a restart |

Randomness in the Monte Carlo is in the simulated user's wording and the
target's answers. The order of pressures on a path is fixed by the scenarios,
so failures group cleanly by rung and by what was asked.

## The verdict

Two sources per run, both ending as yes-or-no lines:

- **The checklist**, fixed at authoring time, run by code wherever its shape allows.
- **Claims**, discovered live: the judge pulls out what the target said it did or found, and verifies each against the planted state and the trace. The model's part is only "what was claimed"; the check is against things the judge holds.

A claim the judge has nowhere to check is a third outcome, *unverified*,
never a fail; counting it as a fail would punish the target for the judge's
blind spot.

**Drift** is a checkable line, not an opinion: a turn that contradicts the
planted state or an earlier turn of the same conversation. The finding is
the turn number and the two conflicting statements. Across many paths this
gives a drift rate per rung, which is the number behind "good enough to put
in front of a real user". Whether the conversation read well stays a
warning: reported, never gating.

**Enough evidence is asymmetric.** One failed error line with a trace behind
it fails the scenario; more runs only add examples. A pass is never proven,
only bounded: N clean paths, N a setting of the judge.

## The sandbox

One per run: a copy of the agent folder in a scratch place, fake state
planted, empty `data/` and `logs/`, thrown away after. Parallel paths are
parallel copies. The code is the repo's code, the venv is the shared one.
The copy must stay importable as `agents.<name>`, since that is how a target
is started.

Docker is not needed for a clean folder. It would add a network cut, so a
target cannot reach its real service during a test, and that is reached for
only when a target has to be cut off. It does not supply a fake service;
that is the planting problem below.

## Time

No scenario carries an absolute date. Every date is an offset from now, and
the judge resolves it against the real clock when it plants a rung, so the
planted dates and the target's "today" agree and are always past any model's
training cutoff. For a later rung the judge moves "now" forward by the gap it
chose. A folder cannot change what day the target thinks it is, so the base
must read today from something the judge can set, falling back to the real
clock when unset. One-line base change, discussed separately, required for
any target that reasons about dates.

## Open

- The judge's `src/` is agreed as `flow/` plus the `user/` family (persona, memory, compose). Everything else the judge needs is not yet placed.
- The steps inside each agent's `flow/`, in detail.
- Planting for a target whose state lives behind an MCP server that talks to a real service (the ledger and Telegram): the server needs a swappable backing store, or the target cannot be graded this way.
- Where the trace lands. `base_interface.md` says Phoenix; `CLAUDE.md` says `logs/`. The judge reads the trajectory from wherever it is.
- The base change that lets the judge set the target's date.
- N clean paths per scenario, and whether it is a fixed count or stops when rates settle.
- Cost: every path is a simulated-user call plus a target call per turn, plus a claim-extraction call per target turn. Coded checks are free.
