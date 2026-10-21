---
title: "SwarmBench: Can Large Language Models Act as Agent Swarm Orchestrators?"
authors: Jinshan Gao et al.
date: 2026-08
arxiv: 2608.30661
url: https://arxiv.org/abs/2608.30661
venue: arXiv
category: orchestrator-worker
pdf: research/multiagent_llm_systems/pdfs/2608.30661.pdf
folder: ["multiagent_llm_systems"]
topics: ["agent evaluation benchmarks", "orchestration and delegation"]
---
# SwarmBench: Can Large Language Models Act as Agent Swarm Orchestrators?

## One line
A benchmark that scores an LLM only as the orchestrator of a dynamically spawned subagent swarm (decompose, delegate, aggregate), plus SwarmExp, which replays experience distilled from past trajectories into the orchestrator's context.

## Method
Problem: multi-agent systems are moving from fixed teams to "Agent Swarms", where a main agent creates subagents at runtime, picks their roles, backbone models and tools, runs them in parallel and merges the results. Existing benchmarks come from single-agent work or score only the final answer, so they cannot say whether the orchestration itself was good.

SwarmBench isolates the orchestrator. The evaluated model is the main agent. It may not call tools or answer the task itself, and part of the task context is hidden from it, so that its own knowledge does not carry the result. It must spawn subagents from a shared model pool, each model described by a short card, and aggregate what they return. Eight tasks are grouped by the capability they stress: decomposition (batch download, multi-document understanding, hard math), delegation (multi-perspective paper review, root cause analysis, a treasure-hunt game with scout and carrier roles) and aggregation (long-text generation, wide web search). Beyond accuracy it reports cost, a parallelism rate (average concurrent subagents), a parallelism gain (serial time over actual time) and an LLM-judged score for decomposition, delegation and aggregation quality.

SwarmExp is the improvement method. It runs the swarm, then has an LLM extract three kinds of experience from the trajectories: skills (workflow files for a task class), tricks (short "if condition, do action" rules, retrieved at run time) and model cards (which backbone model worked for which job). These are injected into the main agent's context. No weights change.

## Evaluated on
- Orchestration beats single models: swarms with GPT-5.4 as main agent average 50.49, against 17.87 to 24.41 for the single-model baselines.
- Orchestrator quality is uneven: GPT-5.4 is best on six of eight tasks. The open models are fragmented, e.g. Kimi-k2.5 is strongest on delegation tasks. Qwen3-30b-a3b averages 25.15.
- Cost and parallelism do not buy accuracy: on MPA, LTG, MTU, RCA and WS, higher cost does not give better scores. Kimi-k2.5 has the highest parallelism rate but does not beat Claude-Sonnet-4-6 on gain. Gemini-3-flash has the highest gain at a moderate rate. The authors conclude that the structure of the parallelism matters, not its amount.
- Aggregation is the weak step: LLM-judged aggregation scores are lower than decomposition and delegation across models, and LTG and WS drop most there.
- SwarmExp helps with GPT-5.4: on RCA +6.42 (10.00 to 16.42), on LTG +6.46 (48.19 to 54.65), on WS +2.92, but on MTU only +0.25. It beats the AOrchestra baseline on all four tasks.
- Experience transfers across models: experience extracted from GPT-5.4 improved 14 of 16 model-task settings. Removing the model card costs most in the ablation (-2.49 on average, against -1.22 for skills and -1.75 for tricks).

## Limitations admitted by the authors
- Only eight tasks (50 samples each), so many swarm scenarios are not covered.
- One lightweight scaffold and one fixed subagent pool. This makes models comparable but may limit how far the conclusions generalise.
- Process quality is partly LLM-judged. Human agreement on 50 sampled trajectories per task is Pearson 0.726 to 0.793 (Spearman 0.684 to 0.739), which supports relative comparisons but leaves room for bias.
- Experience transfer depends on the receiving model: Deepseek-v3.2 gains little and loses on two settings (MTU -0.83, LTG -0.16).
- Cross-task transfer is task-dependent: on wide search, experience from other tasks mostly lowers the score (e.g. 19.05 to 11.42 with MTU experience).

## Limitations found by others

## What it leaves untried
- It does not check whether SwarmExp's experience is extracted from the same benchmark tasks it is then tested on. The text does not describe a held-out split, so the gains may partly be memorisation of task-specific patterns. The wide-search result, where only same-task experience helps, points that way.
- Orchestrators are not trained for the job. The paper finds aggregation is weakest but only adds context, with no training or search over orchestration policies.
- Whether the orchestrator gains come from the decomposition or from model selection is not separated. The model card ablation is the largest drop, but no experiment fixes the subagent model and varies only the plan.

## Topics
[[Topic - agent evaluation benchmarks]] · [[Topic - orchestration and delegation]]
