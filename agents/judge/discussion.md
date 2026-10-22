# Discussion: the difficulty ladder

Design idea from the session of 2026-10-22. Complements `eval_design.md`,
which covers how a single scenario is graded. This file covers how scenarios
grow harder and how the judge drives a conversation through them.

## The idea in one paragraph

The test set is not a fixed pile of scenarios. It is a ladder. At the bottom
every scenario is one turn: the judge asks, the agent answers, the run ends.
Each rung up adds turns, and each added turn carries one new kind of pressure:
asking for something that does not exist, asking for something the agent must
do something else first to answer, referring back to an earlier turn, and so
on. The agent climbs until it breaks. Where it breaks, and on what, is the
finding.

## Difficulty is the pressure, not the turn count

A conversation of ten unrelated questions is ten level-one scenarios. What
makes a later turn hard is what it does to the earlier ones. The pressures
named so far:

| Pressure | What it tests |
|---|---|
| Refer back | "The one I mentioned earlier." Did the agent keep the thread. |
| Nonexistent thing | Asking for an item that is not in the state. Does the agent invent it. |
| Prerequisite | Asking for an action that needs another step first. Does the agent notice, do it, or ask. |
| Contradiction | The user says something that conflicts with the state or with an earlier turn. |
| Changed mind | "Actually, not that one." |
| Out of scope | Asking for something the agent must refuse. |

A level is how many pressures are stacked in one conversation. The report says
which pressure broke the agent, not only at which turn.

## The scenario is the fence

Every scenario carries its facts and its ground truth. The starting state is
frozen and the facts are fixed; the judge never introduces a fact that is not
in the scenario and never pursues a goal the scenario did not give it.

Inside the fence the judge steers live. It picks which pressure to apply next,
in what order and in what words, reacting to what the agent just said. The
scenario bounds what it may do; the judge decides how.

## Scenarios stack

A higher scenario is built on a lower one. The conversation that passed at the
level below is the prefix; the new pressure is the extension. The agent walks
into the new turn already carrying the earlier ones, so a refer-back has
something real to refer back to. When a level breaks, the level below passed on
the same prefix, so the break is isolated to the one new pressure.

## Monte Carlo over paths

One stacked scenario is a tree: at each turn the judge can choose a different
pressure or wording, and the agent can answer differently. The judge does not
pick one path. It samples many, runs each live from the start, grades every
trajectory against the scenario's ground truth, and reads the statistics.

What this gives:

- Per-pressure survival rates instead of a single pass or fail. The must-line
  gate from `eval_design.md` still applies: a scenario passes only if every
  must line passes on every sampled path. One break in thirty is a finding to
  read, not noise.
- The prefix does not need to be stable. A flaky prefix becomes a measured
  rate about the agent rather than a defect of the harness.
- Failures can be grouped by the sequence of pressures that led to them, so a
  weakness that only shows up in one ordering is visible as such.

The trajectory is the thing checked, as in `eval_design.md`: the trace in
`logs/` plus the reply, graded by coded checks wherever possible.

## Raised in discussion, not decided

- Whether the pressures are a fixed menu the judge picks from, with the harness
  recording which pressure each turn was, or free-form steering under
  instruction. The menu makes "inside the fence" checkable by code and makes
  the per-pressure grouping free.
- Which randomness the Monte Carlo is over: the judge's choices, the agent's
  answers, or both.
- How many paths per scenario, and whether sampling stops on a fixed count or
  once the observed rates have settled.
- Cost: with live steering, every path is a judge call plus an agent call per
  turn. Coded checks keep grading free; the steering is the bill.
