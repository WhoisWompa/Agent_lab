---
title: "When Faster Decisions Do Not Make Better Agents: An Empirical Study of Jev in Agent Workflows"
authors: Yuchen Ling et al.
date: 2026-10
arxiv: 2610.13092
url: https://arxiv.org/abs/2610.13092
venue: arXiv
category: agent-evaluation-benchmarks
pdf: agent as a judge papers/decision models/open models/evaluations/When Faster Decisions Do Not Make Better Agents - Jev in Agent Workflows (Ling 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "evaluations"]
topics: ["decision models", "judge and decision-model audits"]
---
# When Faster Decisions Do Not Make Better Agents: An Empirical Study of Jev in Agent Workflows

## One line
Swaps the LLM action selector in five text-only agents (ALFWorld and AndroidWorld) for Jev, a typed decision model, and shows that a 66-78% cut in per-decision cost does not reliably become cheaper or faster delivered tasks, because extra workflow work, failed recovery and premature completion eat the savings.

## Method
The problem: Jev (TypeSafe AI's "System One Model") returns probabilities over supplied candidates and is sold as fast and cheap, but an agent's decisions are sequential, so a cheap wrong choice can cost more downstream than it saved. The paper asks whether local decision savings transfer to task-level efficiency and reliability.

The idea is an accounting shift rather than a new system: replace only the bounded action-selection step (one Jev call per step, choosing among admissible commands, UI targets or tools, plus a THINK option that hands off to an LLM) and keep everything else. Then judge the swap not per decision but by task success, total task cost and time including auxiliary LLM calls, and cost and time per delivered success, which charges failed attempts to the successes. An LLM-Choice control (an LLM given Jev's same candidate list) separates the effect of the candidate interface from the effect of the decision model. Failed and mixed executions are hand-coded into seven behaviour labels (wrong target, prerequisite violation, failed recovery, premature completion, ineffective search, and others) to explain where savings go.

## Evaluated on
- Decisions get much cheaper and faster everywhere: per-decision cost falls 66.1-78.4% and time 73.9-81.5% (from 4.13-8.13 s to 1.04-1.75 s), despite 53.5-134.9% more tokens per decision, because Jev input is cheap and output is free.
- Task-level gains are smaller and uneven: task cost falls 17.1-68.8%, but task time falls only 10.6% (T3A) and 5.7% (AutoDroid) and rises 0.7% for FastAgent; ReAct, where selection was 68.31 of 71.17 s, keeps a 47.6% time cut.
- Success holds on ALFWorld but not on mobile: ReAct and Reflexion lose 1.49 and 1.74 pp (1.00 and 0.00 pp against LLM-Choice), while T3A and FastAgent lose 13.22 and 18.10 pp, both with intervals entirely below zero.
- Cheaper attempts can mean dearer successes: T3A's cost per delivered success rises 7.7% (68.70 to 73.97 mUSD; interval spans zero), and FastAgent's time per success rises from 239.4 to 377.8 s (interval positive).
- Recovery, not first choice, is the failure point: Reflexion-J wins more first trials (95.27% vs 93.53%) but recovers only 11/19 initial failures vs 25/26 for baseline, so final success is lower; in persistent Jev losses, 40/57 Jev executions show failed recovery vs 3/57 baseline.

## Limitations admitted by the authors
- Text-only observations and bounded action interfaces only, because Jev accepts only text; transfer to visual agents, open-ended tool creation and longer workflows is untested.
- Three runs on fixed task instances with one seed measure execution variability, not variation across new environments or task distributions.
- Comparisons are of whole integrations, not of Jev alone: candidate construction, auxiliary generation and feedback all differ, and the LLM-Choice control exists only on ALFWorld, so the large mobile losses cannot be cleanly attributed to the decision model.
- Two interface confounds remain: ALFWorld baselines generate commands without candidate lists, and FastAgent-J runs one tool per step while baseline can batch, which alone produced 44.1% more decisions.
- Costs rest on fixed experimental prices and hosted latency, so a pricing or model-version change can flip the trade-off; the T3A per-success cost rise is itself within noise.

## Limitations found by others

## What it leaves untried
- No completion or recovery check is added on top of Jev, though the paper's own traces locate the failures there (premature completion, failed recovery); a cheap Jev verifier on "is the goal state reached" would test whether the savings can be kept.
- Jev's probabilities are never used: low-confidence selections could be routed to the LLM, the cascade the related-work section describes but the study does not try.
- No LLM-Choice control on AndroidWorld, so whether the 13-18 pp mobile losses come from Jev or from the integration stays open.

## Topics
[[Topic - decision models]] · [[Topic - judge and decision-model audits]]
