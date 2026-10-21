---
title: Agent-Oriented Planning in Multi-Agent Systems
authors: Ao Li et al.
date: 2024-10
arxiv: 2410.02189
url: https://arxiv.org/abs/2410.02189
venue: arXiv
category: orchestrator-worker
pdf: research/multiagent_llm_systems/pdfs/2410.02189.pdf
folder: ["multiagent_llm_systems"]
topics: ["orchestration and delegation"]
---
# Agent-Oriented Planning in Multi-Agent Systems

## One line
AOP has a meta-agent draft a fast sub-task plan, then checks and repairs that plan with a cheap learned reward model, a similarity lookup and an LLM detector, so every sub-task fits an agent that can solve it.

## Method
The problem: a meta-agent that splits a query and assigns sub-tasks from agent descriptions alone often produces plans the agents cannot execute. A sub-task may bundle two entities in one search, and a description such as "commonsense agent" does not say what it knows. The authors name three principles a plan must meet. Solvability: one agent can fully resolve each sub-task. Completeness: no key fact of the query is dropped. Non-redundancy: no sub-task is duplicated or irrelevant.

The plan is treated as a draft, not a final result.
- **Fast decomposition.** The meta-agent sees the query and all agent descriptions. It outputs sub-tasks with a suggested agent and dependencies in one pass.
- **Reward model for solvability.** Trying every agent on every sub-task costs m x n calls. Instead a small model predicts, from the sub-task text and the agent description alone, how good the agent's answer would be. It is a frozen MiniLM embedding plus a three-layer MLP, trained on scores of real agent responses (correctness, relevance, completeness). A high score accepts the assignment. A low score makes the model rank all agents and reassign. If even the best agent scores very low, the meta-agent replans that sub-task.
- **Representative works.** Each agent keeps a store of sub-tasks it has fully solved. If a sub-task is close to a stored one by cosine similarity, the agent can probably do it but the wording is off, so the sub-task is re-described in the stored style. If nothing is close, the sub-task is judged too complex and is planned in detail, meaning split further.
- **Detector.** An LLM with a role prompt lists the query's key elements, matches them to sub-tasks, and flags missing information or overlapping sub-tasks. It gives the meta-agent repair suggestions. The authors say plain instructions still left more than 15% of queries with such defects.
- **Feedback loop.** Sub-tasks from solved queries are added to the solving agent's store if they are distinct enough, so allocation improves during use.

The idea is to spend a few cheap, learned or lightweight checks on the plan rather than extra agent calls.

## Evaluated on
- Beats single-agent and planning baselines on Husky-QA (numerical reasoning that needs search plus calculation): 43.7% accuracy vs 39.6% for HUSKY, 37.6% for ReAct, 33.3% for plain GPT-4o and 30.0% for a plain meta-agent.
- Cost is that of other multi-agent planners, about 11,869 s vs 10,394 s for HUSKY, and far above single calls at 1,968 s. The authors call this affordable.
- Each part matters in the ablation: accuracy falls to 36.6% without the detector, 38.7% without the reward model and 41.1% without representative works.
- Plan quality rises, judged by an LLM: solvability 0.938 vs 0.763 for raw GPT-4o, completeness 0.969 vs 0.822. Non-redundancy was already near the ceiling at 0.986 vs 0.993.
- Gains hold on DROP (34.0 vs 28.0 for HUSKY) and IIRC (41.5 vs 36.5). A reward model trained on Husky-QA and reused there drops only slightly, to 32.0 and 39.0.

## Limitations admitted by the authors
- The reward model depends on its training labels. Human scoring raised accuracy from 43.7% to 46.9%, and tuning the embeddings as well gave 47.9%. The default LLM scorer is therefore a ceiling on quality.
- Results rest on agent descriptions. LLM-generated descriptions cost accuracy (40.4% vs 43.7%) and expert-written ones helped a little (44.2%). Descriptions still need prompt-engineering effort.
- Cost is several times a single call, and the authors only argue it is worth it. Extra token spend is 1.12M prompt tokens vs 0.02M for GPT-4o.
- Scaling to many agents is limited by the meta-agent's context window, since all descriptions must fit in the prompt. The proposed fix, grouping agents and choosing a group first, is not tested.
- Redundancy between agents is deliberately left alone, since duplicated agents give fault tolerance (Appendix B).

## Limitations found by others

## What it leaves untried
- Only four agent types, one planner LLM (GPT-4o) and a small test set (292 queries on Husky-QA) are used. The paper does not test large or overlapping agent pools, where selection is hardest.
- The detector's missing-dependency check lifts accuracy from 43.7% to 46.2% but is not in the main system. Why it was left out is not argued.
- Evaluation uses GPT-4o as answer judge, and plan quality is also scored by an LLM. The paper does not check either against human judgments.

## Topics
[[Topic - orchestration and delegation]]
