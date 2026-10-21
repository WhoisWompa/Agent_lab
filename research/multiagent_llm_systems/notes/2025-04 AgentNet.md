---
title: "AgentNet: Decentralized Evolutionary Coordination for LLM-based Multi-Agent Systems"
authors: Yingxuan Yang et al.
date: 2025-04
arxiv: 2504.00587
url: https://arxiv.org/abs/2504.00587
venue: arXiv
category: topology-communication
pdf: research/multiagent_llm_systems/pdfs/2504.00587.pdf
folder: ["multiagent_llm_systems"]
topics: ["communication topology and channels", "automated pipeline and topology search", "orchestration and delegation"]
---
# AgentNet: Decentralized Evolutionary Coordination for LLM-based Multi-Agent Systems

## One line
Agents with no central orchestrator route tasks to each other over a graph whose edges and per-agent skills are updated after every task, with each agent's expertise held in a small retrieval memory of its own past steps.

## Method
The problem: most multi-agent systems use a central controller or a fixed workflow with fixed roles. The authors say this causes a scalability bottleneck, a single point of failure, no way to adapt roles as agent performance shifts, and no cross-organisation sharing because proprietary knowledge cannot be pooled. These are stated as motivation. The paper does not measure them.

Each agent has a router and an executor, both on the same LLM. A new task goes first to the agent whose capability vector is most similar to the task's required capabilities. That agent's router then chooses one of three actions. It can forward the task unchanged to a better-suited agent. It can split the task, do the part it is good at, and route the rest. Or it can execute the whole task. Forwarding leaves the task state unchanged, and the state changes only when an agent finishes a part, so the routing path stays acyclic. On a split, only subtask results travel onward, not the decomposition reasoning. The authors argue this stops one agent's bad decomposition from spreading.

Three things evolve:
- **Edges.** Each edge weight is an exponential average of past routing success. Edges below a threshold are pruned, so the graph starts fully connected and thins out.
- **Capability vectors.** These are also exponential averages, nudged by what the agent just did successfully.
- **Memory.** Each agent keeps a fixed-capacity pool of its own step fragments (query, partial context, action), kept separately for router and executor. The top-k similar fragments are retrieved as few-shot examples, and an LLM decides which fragment to drop when the pool is full.

Specialisation is meant to emerge from this loop. No roles are assigned. The agent-memory idea is close to earlier trajectory-retrieval work, and the new part is combining it with decentralised routing and an edge-pruning topology.

## Evaluated on
- **Accuracy is competitive, not dominant.** With three agents on MATH, BBH and API-Bank, across three backbones, AgentNet scores 92.86 / 94 / 30 with DeepSeek-V3. It is best or tied on most columns. It is not best everywhere: with Qwen-turbo, AFLOW scores 82.14 on MATH against AgentNet's 81.43, and with GPT-4o-mini the MATH score of 85.00 ties AFLOW and GPTSwarm. Test sets are 140, 100 and 100 problems, so a 3-point gap is three problems. No variance is reported.
- **The learning phase matters.** Without the evolution phase (GPT-4o-mini), MATH is 77.86 against 85.00, API-Bank 23 against 32, and BBH 76 against 86.
- **Decentralised routing beats random and matches a central router.** On BBH, test accuracy is 86 for AgentNet and 83 for a centralised global router. Random next-agent choice gets 82 and random operations get 71. The 3-point gap over the global router is small and unrepeated.
- **Heterogeneity depends on team size.** The homogeneous team is best at 3 agents (0.86 against 0.81 for the mixed-LLM and mixed-skill teams). At 5 agents mixing wins (0.85 against 0.79 homogeneous). The authors give no cause beyond "coordination overhead in small groups".
- **Scaling gains are small.** Going from 3 agents with 30 executors to 9 agents with 40 gives 80.38 to 81.18 in training. Test scores swing between 80 and 86 across configurations.
- **Specialisation is shown as a picture.** Per-agent ability scores diverge more as agents are added, and the 5-agent graph's edge weights spread out from a uniform 1.00. This is qualitative, with no check that the specialisation helps beyond the ablation above.

## Limitations admitted by the authors
- Heterogeneous agents (different models, tools, workflows, data) are not handled well. Their effect on routing and resource allocation is called an open question, and the 3-agent result above shows a loss from mixing.
- The router picks from a small, predefined pool. With hundreds or thousands of agents, finding the right delegate gets much harder, and no experiment goes past 9 agents.
- The router cannot discover agents outside its candidate set. The authors propose exploration incentives but do not build them.
- Scaling shows diminishing returns, which the authors read as an "optimal point" for resources.

## Limitations found by others

## What it leaves untried
- Testing the headline claims of fault tolerance and privacy. No experiment removes an agent or measures what data leaks, so both are asserted from the design alone.
- Comparing against a centralised system on cost, latency or token use. Pruning is said to reduce communication overhead, but no cost figures are given.
- A larger or open agent population, where entry-agent selection by capability similarity is the part most likely to break.

## Topics
[[Topic - communication topology and channels]] · [[Topic - automated pipeline and topology search]] · [[Topic - orchestration and delegation]]
