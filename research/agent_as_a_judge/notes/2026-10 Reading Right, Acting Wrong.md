---
title: "Reading Right, Acting Wrong: Diagnosing Decision Failures of System One Models in Agent Loops"
authors: Yubo Li et al.
date: 2026-10
arxiv: 2610.18579
url: https://arxiv.org/abs/2610.18579
venue: arXiv
category: agent-evaluation-benchmarks
pdf: agent as a judge papers/decision models/open models/evaluations/Reading Right, Acting Wrong - Decision Failures of System One Models in Agent Loops (Li 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "evaluations"]
topics: ["decision models", "judge and decision-model audits"]
---
# Reading Right, Acting Wrong: Diagnosing Decision Failures of System One Models in Agent Loops

## One line
Pairs each next-action question to a System One decision model with independent factual probes on the same agent state, and finds that most wrong actions by strong models follow correct reading of the facts.

## Method
The problem: System One models (JEV, OpenAI Decisions, open-weight clones) pick an agent's next action by scoring a supplied option list in one pass, with no text. When they choose wrongly there is nothing to inspect, so final-action accuracy cannot tell "misread the trace" (a fix for the state format or context budget) from "read it right and chose badly" (a fix for the decision itself).

The idea is a behavioral split. On one frozen state, the model is asked the next-action question and, separately, closed factual probes whose answers the environment fixes (did the last action succeed, what is held, is this action permitted). Crossing "all probes right" (U) with "action right" (D) gives four outcomes. The one that matters is U1D0, facts right and action wrong. The paper says plainly that U1D0 does not prove the failure is pure decision, because the probes may have missed a relevant fact.

To decide when U1D0 can be blamed on deciding, it adds a model-free sufficiency check: group states that share the same correct probe answers. The probe set is sufficient if one action is gold in every state of the group. If two states have identical probe answers but disjoint gold sets, correct probes cannot fix the action. This can be checked exhaustively in finite environments, not proven on natural data. So the authors also generate states that are sufficient by construction: a four-rule ordered decision list plus four distractor facts, where the rule facts alone fix a unique gold action. Then they add information to the decision request (correct facts, the model's own probe answers, a sub-goal) and measure which addition repairs the error.

## Evaluated on
- Most errors follow correct reading, and the share grows with accuracy: for the six most accurate systems, 73-85% of decision errors happen with every probe right, from 49% (Kev-9B) up to 81% (Gemma) and 85% for the GPT-6.1 reasoning reference.
- The errors are not noise: all 14 competent fast systems make a facts-right, action-wrong error on the same 141 states, where a permutation null expects none. GPT-6.1 gets only 40% of those states right, against 88% overall.
- When the probes are sufficient, the failure is composition: JEV reads the rule facts at 100% and decides at 1.000 from the facts alone, but only 0.791 from the raw trace. Appending its own probe answers gives 0.968, and composing the action in code from them gives 0.996. A cascade that re-asks only below 0.7 confidence reaches 0.932, re-asking on 38% of states.
- On real states the benchmark probes do not carry the missing piece: correct probe answers add only 2.9-7.1 points for most fast systems. On ALFWorld, giving JEV the next sub-goal adds 16.3 points, while decision facts add 5.3. JEV states its own sub-goal correctly in only 66.8% of states.
- Read edits are not acted on: on customer-service policy edits, JEV, Clef, Gemma and Qwen3.8-27B answer every probe on the edited state correctly, yet change the tool call in only 22-57% of relevant edits.

## Limitations admitted by the authors
- Behavioral evidence only: a correct probe answer does not show the model used that fact in deciding, so "decision failure" is an inference from outcomes, not from the model's internal computation.
- On natural states the probes are not sufficient, so U1D0 mixes true decision failures with facts nobody asked about. The clean attribution holds only on the generated procedures and the ALFWorld decision probes.
- Gold sets are stricter than necessary: 5-42% of a system's simulator "errors" are optimal under exact lookahead. For GPT-6.1 that is 34-96%, so its headline 85% facts-right error share is inflated.
- Label errors: 303 ALFWorld location labels name a co-located receptacle rather than the one in the text. Excluding the affected records raises the facts-right share (JEV 0.663 to 0.707), so the headline is conservative.
- It compares deployments, not architectures: readouts, serving stacks and input limits differ, two runtimes truncate states, and a JEV rerun five days later matched on only 96.3% of states.
- Single decisions on frozen traces only, with no closed-loop runs. The follow-up studies cover 12-16 of the 18 systems.

## Limitations found by others

## What it leaves untried
- Closed-loop execution: the remedy (narrow probes composed in code, or a confidence cascade) is shown per decision but never run as an agent's policy. Small per-step gains or the 2-7% of correct states that own answers break could compound over a trajectory.
- Automatic composition when the rules are not explicit: code composition reaches 0.96-1.00 only because the generated procedures spell out the rules. On open tasks like ALFWorld the missing piece is the sub-goal, and no method is tested for producing it cheaply, whether a planner or a sub-goal-trained System One model.
- Using the diagnosis for routing: the paper argues for sending only some states to deliberation, but never builds a router that predicts U1D0-prone states (such as the 141 shared failures) and checks the cost and accuracy trade-off.

## Topics
[[Topic - decision models]] · [[Topic - judge and decision-model audits]]
