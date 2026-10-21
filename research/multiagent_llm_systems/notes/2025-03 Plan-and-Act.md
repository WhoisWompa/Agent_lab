---
title: "Plan-and-Act: Improving Planning of Agents for Long-Horizon Tasks"
authors: Lutfi Eren Erdogan et al.
date: 2025-03
arxiv: 2503.09572
url: https://arxiv.org/abs/2503.09572
venue: arXiv
category: orchestrator-worker
pdf: research/multiagent_llm_systems/pdfs/2503.09572.pdf
folder: ["multiagent_llm_systems"]
topics: ["orchestration and delegation"]
---
# Plan-and-Act: Improving Planning of Agents for Long-Horizon Tasks

## One line
A fine-tuned planner LLM writes and rewrites a high-level plan after every step while a fine-tuned executor LLM turns each plan step into web actions, with the planner trained on synthetic plan data.

## Method
The problem: one model that must both hold a long-horizon strategy and emit low-level actions loses track of its goal. Splitting planning from execution helps, but off-the-shelf LLMs are not trained to produce plans grounded in a specific environment (web pages), and plan-training data does not exist. Prompting alone does not fix it: the prompted baseline reaches 9.85% on WebArena-Lite.

The system has two fine-tuned models. The planner reads the user query and emits a structured step list. The executor sees one plan step plus the page HTML and emits one concrete action, then discards redundant HTML. After each executor step the planner is called again with the current state, the previous plans and the actions taken, and writes a new plan (dynamic replanning). The plan therefore carries forward what has been learned (for example, who the top contributor turned out to be), so no separate memory module is needed. Both models also emit a chain-of-thought trace before output.

The new part is the planner training data, built without human annotation:
- Grounded plan generation: successful action trajectories (filtered by an outcome reward model) are shown to a teacher LLM, which reverse-engineers a plan and labels which low-level actions belong to each plan step. This keeps plans executable, unlike asking a teacher for a plan from the query alone, which gave plans misaligned with how the web task is done.
- Plan expansion: a trajectory gives about 8 executor examples but only 1 plan, so seed query-plan pairs are used to generate 10,000 more, without a simulator.
- Targeted augmentation: failure patterns on a held-out set select related seeds, from which 5,000 more plans are generated.
- Replanning and CoT data are produced the same way by the teacher.

## Evaluated on
- Explicit planning helps even with an untrained executor: 9.85% with no planner vs 29.63% with a static trained planner on WebArena-Lite (165 tasks).
- The planner is the bottleneck, not the executor: doubling executor trajectory data gives only +0.61 points (36.36 to 36.97), while the 10,000 expanded plans add about 10 points and the 5,000 targeted plans add 4-5 more.
- Dynamic replanning is the largest single gain: 43.63% to 53.94% (+10.31), above the prior best WebRL at 49.1%. An unfinetuned executor reaches 44.24% with the replanning planner.
- CoT brings the full system to 57.58%. A Llama-8B model trained on the same data reaches 53.33%, close to the 70B model without CoT (53.94%).
- Full WebArena: 45.7% (Llama-70B) and 48.15% (QwQ-32B), described as on par with prior work (AgentOccam-Judge 45.7%), not clearly better.
- WebVoyager, text only: 81.36% with QwQ-32B vs 73.1% for Agent-E, and 58.08% with an 8B model.

## Limitations admitted by the authors
- Trajectory generation needs a baseline model that can already complete the web tasks. For a benchmark with no training data (WebVoyager) the pipeline depends on that model to collect trajectories, so the data quality is capped by it.
- Replanning after every action is inefficient and slows the agent. No latency or cost numbers are given.

## Limitations found by others

## What it leaves untried
- Letting the executor decide when to replan, or the planner delegate to sub-agents, which the authors name as the fix for per-step replanning cost.
- Showing the design outside web navigation. The paper claims the framework fits other long-horizon digital tasks but tests only web benchmarks.
- Planner fine-tuning with reinforcement learning or multimodal input (named as future work). Naive supervised planner fine-tuning on the 1,113 benchmark plans overfit and did not help (the fine-tuned planner scored below the no-planner executor), so data diversity is carrying the result.

## Topics
[[Topic - orchestration and delegation]]
