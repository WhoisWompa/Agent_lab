---
title: "EvoMAS: Learning Execution-Time Workflows for Multi-Agent Systems"
authors: Chengdong Xu et al.
date: 2026-05
arxiv: 2605.08769
url: https://arxiv.org/abs/2605.08769
venue: arXiv
category: orchestrator-worker
pdf: research/multiagent_llm_systems/pdfs/2605.08769.pdf
folder: ["multiagent_llm_systems"]
topics: ["automated pipeline and topology search", "orchestration and delegation"]
---
# EvoMAS: Learning Execution-Time Workflows for Multi-Agent Systems

## One line
Instead of fixing a multi-agent workflow before a task starts, EvoMAS picks a new layered workflow at every stage of the task, using a small policy trained by REINFORCE on final task success.

## Method
**Problem.** Automated multi-agent design methods (GPTSwarm, AFlow, G-Designer, MaAS) optimise one workflow up front and reuse it unchanged. Long tasks change character as they go: early stages need exploration, later ones need verification and refinement. A workflow fixed in advance cannot follow that. The paper gives no direct evidence that this is the cause of the baselines' weakness, only that the baselines do not reliably beat a single model.

**Idea.** Treat workflow choice as a sequential decision problem (a meta-level MDP) along one task run. The meta-state is a structured text summary of the task so far. The meta-action is a workflow: a layered graph (at most 3 layers here) of agents drawn from a fixed pool, with every agent in a layer feeding all agents in the next.

**Task state.** A Planner keeps the subtask list and the active subtask. An Evaluator, an agent with web-research and analysis tools, checks the last stage's output and returns a verdict, a confidence and feedback. An Updater, plain deterministic code and not an LLM, merges plan, workflow, result and feedback into the next state. A compact version of the state conditions the workflow choice. The full state is given to the executing agents as working context.

**Workflow adapter.** The compact state is encoded and cross-attended against an embedding of each candidate agent (built from its role, capabilities and tools). Cosine scores go through a temperature softmax. Agents are sampled without replacement per layer until their cumulative probability reaches a threshold. The same agent can appear in several layers or stages, which allows repeated refinement. An "Early-exit" agent in the pool lets the policy end the run once evidence suffices.

**Training.** Only the adapter is trained, with REINFORCE on sparse, verifiable terminal success. This deliberately avoids optimising against the LLM evaluator, whose judgments may be biased. Evaluator-based process reward is tested separately.

## Evaluated on
- Beats single models and static automated designs on average success: 65.0 for the 7-agent pool against 34.8 for the best baseline (G-Designer/MaAS) and 29.8 for GPT-4o, across GAIA L1 and L2, HLE and DeepResearcher. The test sets are small (50 sampled instances split 8:2 for HLE and DeepResearcher, so 10 held-out items).
- A richer pool helps a lot: going from 4 agents (I/O, Early-exit, Web-search, Ensemble) to 7 (adding Multi-generate, Self-refine, Web-browser) lifts the average from 45.0 to 65.0, and GAIA L2 by 28.7 points.
- Task-state tracking helps independently of learned routing: with the workflow held fixed, switching the Planner-Evaluator-Updater on raised success on GAIA and on HLE under two backbones (shown in plots, no numbers in the text).
- Terminal reward alone trains the adapter on moderate tasks: held-out accuracy rises through training on GAIA L1 and L2.
- Process reward matters only when success is very rare. It leaves GAIA L1 unchanged and lifts L2 from 14.2 to 28.6. On GAIA L3 and BrowserComp, terminal-only training stayed at zero success while process reward gave a first non-zero result.
- A stronger backbone adds more: GPT-4o over GPT-4o-mini gives +22.2 on L1 and +7.2 on L2.
- The case study shows the policy shifting from exploration, to Web-search and Ensemble for verification, to Early-exit. This is qualitative.

## Limitations admitted by the authors
- The agent pool and maximum depth are fixed. The adapter cannot create new agents or choose its own depth, so the gains depend on which candidates the authors supplied (the 4-to-7 jump shows how much).
- Terminal reward is too sparse on very hard tasks: with no successes in a batch there is no gradient. The process-reward fix depends on an evaluator the authors call possibly biased, and calibrated process rewards and better credit assignment are left open.
- Some costly benchmarks are scored on small held-out subsets (as few as 4 items for L3 and BrowserComp, 10 for HLE), so the differences are coarse.
- Results depend on the backbone, prompts, tools and evaluator reliability.

## Limitations found by others

## What it leaves untried
- No cost comparison. Workflows are rebuilt and an Evaluator with web tools is called at every stage, but token and tool-call cost against static baselines is only promised in an appendix template, so the quality gain is not weighed against its price.
- No test of the staged design against a plain single-agent loop with the same planner and evaluator. The baselines are other workflow designers, so how much comes from the task state versus the learned workflow choice is shown only in plots.
- No transfer test. Whether a policy trained on GAIA works on unseen task types or a new agent pool is not examined.

## Topics
[[Topic - automated pipeline and topology search]] · [[Topic - orchestration and delegation]]
