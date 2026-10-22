# Discussion: the judge's flow and the difficulty ladder

Design idea from the session of 2026-10-22. Complements `eval_design.md`,
which covers how a single scenario is graded. This file covers the judge's
overall flow, how scenarios grow harder, and how the judge drives a
conversation through them. Items marked *to be confirmed* are the user's own
open points.

## The flow

1. **Learn the target.** The judge reads the agent's description, its tools,
   and its code (*to be confirmed* whether the judge sees the code). The aim
   is to know what the agent can and cannot do before anything else.
2. **Clear open questions with the user.** The judge converses with the user
   until it has no open questions about the target.
3. **Create scenarios.** The judge writes scenarios with their details: the
   ground truth, plus the other contents of a scenario (*to be confirmed*
   what else a scenario carries).
4. **The user vets.** The user reads each scenario and accepts or rejects it.
   Only accepted scenarios are run.
5. **Simulate.** For an accepted scenario the judge calls a fake user with a
   persona and has it interact with the agent. The judge tracks the entire
   conversation.
6. **Verify claims with tools.** When the agent says it did something with an
   effect, such as booking a flight or saving data, the judge calls a tool to
   check that the effect is real.
7. **The judge ends the session.** Only when the judge determines it has
   collected enough data does it choose to end the session.

## Difficulty is a ladder of turns

The test set is not a fixed pile of scenarios. At the bottom every scenario is
one turn: the fake user asks, the agent answers, the run ends. Each rung up
adds turns, and each added turn carries one new kind of pressure. The agent
climbs until it breaks. Where it breaks, and on what, is the finding.

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
frozen and the facts are fixed; the fake user never introduces a fact that is
not in the scenario and never pursues a goal the scenario did not give it.

Inside the fence the judge steers live. It picks which pressure to apply next,
in what order and in what words, reacting to what the agent just said. The
scenario bounds what may happen; the judge decides how.

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
`logs/` plus the reply, graded by coded checks wherever possible, plus the
tool checks of step 6 for any effect the agent claims.

## Open

From the user:

- Whether the judge sees the agent's code or only its description and tools.
- What a scenario carries beyond the ground truth.

Raised in discussion, not decided:

- Whether the pressures are a fixed menu the judge picks from, with the harness
  recording which pressure each turn was, or free-form steering under
  instruction. The menu makes "inside the fence" checkable by code and makes
  the per-pressure grouping free.
- Which randomness the Monte Carlo is over: the fake user's choices, the
  agent's answers, or both.
- How many paths per scenario, and whether sampling stops on a fixed count or
  once the observed rates have settled.
- What "enough data" means for step 7, in terms the harness can check.
- Cost: with live steering, every path is a fake-user call plus an agent call
  per turn. Coded checks keep grading free; the steering is the bill.
