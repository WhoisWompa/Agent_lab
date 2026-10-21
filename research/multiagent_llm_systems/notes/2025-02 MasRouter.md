---
title: "MasRouter: Learning to Route LLMs for Multi-Agent Systems"
authors: Yanwei Yue et al.
date: 2025-02
arxiv: 2502.11133
url: https://arxiv.org/abs/2502.11133
venue: arXiv
category: orchestrator-worker
pdf: research/multiagent_llm_systems/pdfs/2502.11133.pdf
folder: ["multiagent_llm_systems"]
topics: ["automated pipeline and topology search", "orchestration and delegation"]
---
# MasRouter: Learning to Route LLMs for Multi-Agent Systems

## One line
A learned cascaded controller that, for each query, picks the collaboration mode, the number of agents, each agent's role and each agent's LLM, trained to trade answer quality against token cost.

## Method
Problem: single-agent LLM routers only choose a model per query. A multi-agent system (MAS) also needs a collaboration structure (CoT, reflection, self-consistency, debate, chain, complete graph), a head count and a role per agent. Existing MAS are mostly built from one LLM, and the methods that search structures (GPTSwarm, AFlow, AgentPrune) do not choose models. The authors define "Multi-Agent System Routing" (MASR): given a pool of LLMs, modes and roles, sample for each query a MAS that maximises expected utility minus lambda times cost.

MasRouter factorises that choice into three sampling stages that each see the earlier choices:
- **Collaboration determiner.** A variational latent model maps the query embedding to a distribution over modes. The same latent gives the agent count, k = ceil(difficulty score x gamma), with gamma = 6 the maximum. Easy queries should therefore get a cheap mode and few agents.
- **Role allocator.** Roles are drawn one at a time, each conditioned on the query, the mode and the roles already chosen, so a programmer can precede a test engineer.
- **LLM router.** Each agent's backbone is drawn from a multinomial over the pool, conditioned on query, mode and roles. Roles and models are matched by embedding profiles (including price and benchmark scores), which lets a new LLM be added by writing its profile.

Training is policy gradient on the reward (correctness minus lambda x cost). A Gamma-function relaxation keeps the agent count differentiable. No agent structure is exhaustively tried, which is why training is cheaper than search-based methods.

## Evaluated on
- Beats every baseline on all five benchmarks (MMLU, GSM8K, MATH, HumanEval, MBPP): average 85.93 against 82.42 for RouterDC, the best single-agent router, and 84.20 for AFlow, the best multi-agent baseline. Gains are largest on MBPP, 84.0 against 82.2 for AFlow and 75.2 for RouterDC.
- Cheaper at higher accuracy: on HumanEval cost is $0.185 against $0.363 for AFlow, with 90.5 against 90.2 accuracy. On MBPP it is $1.04 against $1.72 for AFlow at 84.0 against 82.2.
- Training is cheaper: on MMLU the training cost is $1.43 against $4.70 for GPTSwarm and $8.67 for AFlow, since no structure is traversed and validated.
- Works as a plug-in: replacing a fixed LLM in LLM-Debate and MacNet with routed LLMs cuts cost 17-28% on HumanEval and lifts accuracy by 1.55 points, for example $0.488 to $0.404 for MacNet.
- Adds an unseen LLM (DeepSeek-V3) with no retraining of the other parts: it is picked 12.17% of the time on MMLU and 27.19% on MATH, and MMLU accuracy rises from 84.25 to 85.40.
- Ablation: replacing the LLM router with random choice costs the most accuracy (2.09 and 4.34 points on GSM8K and MATH). Removing the cost term leaves accuracy flat but raises cost by 54% and 42%, so the cost penalty is what makes the system adapt to difficulty.

## Limitations admitted by the authors
- The paper has no limitations section. The only trade-offs it states are in the sensitivity study. Raising gamma from 6 to 10 gives marginal accuracy gain for 1.5x per-query cost. Raising lambda from 5 to 25 cuts overhead 17.78% but loses about 1.3% accuracy.

## Limitations found by others

## What it leaves untried
- The search space is fixed by hand: six modes and 26 roles written in advance, with a pool of five LLMs. Whether the router works when roles or topologies must be invented, or with a large LLM pool, is not tested.
- Only single-shot question answering and code benchmarks are used. Tool-using or long-horizon agent tasks, where mode choice may matter more, are not tested.
- Sensitivity to the router's training data is unexamined. It is trained per benchmark, and the unseen-LLM test adds only one model, so transfer to a new task domain is unsupported.

## Topics
[[Topic - automated pipeline and topology search]] · [[Topic - orchestration and delegation]]
