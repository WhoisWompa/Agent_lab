---
title: Rethinking the Evaluation of Efficiency Methods for Multi-Agent Systems
authors: Jiamu Zhang et al.
date: 2026-09
arxiv: 2609.05933
url: https://arxiv.org/abs/2609.05933
venue: arXiv
category: failure-analysis-survey
pdf: research/multiagent_llm_systems/pdfs/2609.05933.pdf
folder: ["multiagent_llm_systems"]
topics: ["communication topology and channels", "automated pipeline and topology search", "agent evaluation benchmarks"]
---
# Rethinking the Evaluation of Efficiency Methods for Multi-Agent Systems

## One line
A controlled benchmark re-tests five published methods that prune agents or communication edges to cut multi-agent cost, and finds many reported gains come from the setup, structural collapse or easy-to-prune starting systems, not from better structure.

## Method
The problem: methods such as AgentPrune, AgentDropout, AGP, DAGP and GPTSwarm start from a multi-agent system (MAS) and return a cheaper one. Each paper reports its gains under its own prompts, agent classes, tool access, backbone and starting graph, so a method may look good only because it started from a stronger setup. The authors add a second threat: in settings that do not need multi-agent interaction, a single agent or a randomly pruned system already keeps accuracy, so success there proves little.

The fix is to pin everything except the optimizer's output. A MAS is a tuple of topology, agent assignment, LLM and method hyperparameters. Topology is three binary masks: who sends to whom within a round, whose previous-round output reaches whom, and which agent is active in which round. Agent types come from one shared registry and each node index keeps a fixed role. Without that, deactivating node 2 silently shifts every later role, so an accuracy change could come from removed communication or swapped prompts. The runtime filters each agent's inputs to the senders the topology allows, so the topology is a causal lever. The released code of each method runs with its learning algorithm unchanged.

The test grid has 38 cells. It starts from an anchor (Star, 6 agents, 2 rounds, no tools) and moves one axis at a time: starting topology, agent count, round depth, tool access. Each cell reports the optimized-minus-original difference in accuracy, prompt tokens (the cost an API bills), edge-passing tokens (the cost earlier papers report), tool calls and structure counts. A matched random-pruning control with the same edge budget tests whether the optimizer beats the budget alone.

## Evaluated on
Four tasks (GSM8K, MMLU, HumanEval, LiveCodeBench), each with one small 4B to 8B backbone.
- Learned pruning barely beats random pruning. Over the 20 main cells, optimized systems change accuracy by -0.77 points against -0.44 for random pruning of the same size. Methods beat their random control in 12 of 25 comparisons; only DAGP stands out (4 of 5, +1.29 vs +0.08).
- No method is consistent across starting topologies. Dense graphs have slack: AgentPrune gains 5.40 points on MMLU with a fully connected graph. Sparse chains have none: AGP drops 13.04 points on HumanEval, and 10.56 on Layered.
- Edge pruning can raise the bill. AgentPrune on Star GSM8K removes edges but appends a decision node, adding 2.83K prompt tokens while accuracy falls 0.84 points. Which method looks efficient depends on the token metric reported.
- Collapse shows up as a cheap score. GPTSwarm on Chain GSM8K loses 86.27 accuracy points with almost no cost change, because it cut a choke-point edge. AGP on Random HumanEval cuts 11.39K tokens but loses 17.39 points. GPTSwarm also permutes roles in 13 of 38 cells.
- Tool pathways get removed. Methods can cut cost by disabling sandbox or retrieval agents, which tests removing tools, not compressing the MAS. The authors give this as an argument; the evidence is in the appendix tables.
- Where the full MAS beats the single agent, differences between methods are informative (GSM8K and HumanEval on Star). On LiveCodeBench the full MAS is often no better than one agent, so kept accuracy says little.
- Benign cases (DAGP on Star HumanEval, +2.49 accuracy and -1.22K tokens) remove only redundant node-rounds and keep the decision path.

## Limitations admitted by the authors
- Only methods that restructure an existing MAS are covered. Methods that build a MAS from scratch produce components the protocol does not accept.
- The grid is four task families plus a HotpotQA extension. Long-horizon planning, interactive environments and heterogeneous tools are untested, so the conclusions are diagnostic for these settings, not for all deployments.
- Repeated runs exist for one task only (MMLU). Run-to-run standard deviation is 0.6 to 2.1 points, about the size of most reported gains. The random control is a single sample per budget, and significance tests do not cover the full grid.
- All backbones are small open models (4B to 8B). Behaviour may change with stronger models.
- Pinned prompts and a shared registry remove each method's own prompt engineering, which some papers count as part of their contribution.
- Cost uses whitespace token counts, and prompt tokens are an upper bound, so absolute costs are not comparable across papers. Tasks are English only.

## Limitations found by others

## What it leaves untried
- Extending the protocol to from-scratch MAS construction, where head-to-head comparison is currently almost impossible.
- Running several random-pruning samples per budget with full-grid significance tests. With noise near 2 points, the 0.33-point gap between optimized and random pruning cannot be judged.
- Stronger backbones and the native prompts of each method, which would show whether the setup-dependence survives.

## Topics
[[Topic - communication topology and channels]] · [[Topic - automated pipeline and topology search]] · [[Topic - agent evaluation benchmarks]]
