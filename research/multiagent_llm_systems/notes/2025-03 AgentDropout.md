---
title: "AgentDropout: Dynamic Agent Elimination for Token-Efficient and High-Performance LLM-Based Multi-Agent Collaboration"
authors: Zhexuan Wang et al.
date: 2025-03
arxiv: 2503.18891
url: https://arxiv.org/abs/2503.18891
venue: arXiv
category: topology-communication
pdf: research/multiagent_llm_systems/pdfs/2503.18891.pdf
folder: ["multiagent_llm_systems"]
topics: ["automated pipeline and topology search", "communication topology and channels"]
---
# AgentDropout: Dynamic Agent Elimination for Token-Efficient and High-Performance LLM-Based Multi-Agent Collaboration

## One line
Learns, from about 40 samples, which agents to drop in each round and which messages to cut, so a multi-round agent team uses roughly a fifth fewer tokens and scores slightly higher.

## Method
Problem: multi-agent teams spend many tokens because every agent speaks in every round. The previous method, AgentPrune, learns a mask that removes redundant edges (messages) but applies one uniform pruning over all rounds and keeps the same agents in every round. The authors argue redundancy has two sources, redundant messages and redundant roles, and that different rounds need different roles (their analogy is human teams reassigning roles as a task progresses; this is motivation, not tested).

The team is a directed graph: nodes are agents, and edges are messages inside a round or from one round to the next. Each edge gets a trainable weight in [0,1], starting at 0.5. A concrete graph is sampled with each weight as the edge probability, forced to be acyclic. Because task accuracy is not differentiable, weights are trained with a policy-gradient estimate over a few sampled graphs, with accuracy as reward.

Two stages, each trained from scratch:
1. Node Dropout: train only the within-round weights for task accuracy, then in each round remove the nodes with the lowest weighted in-degree plus out-degree, with their edges.
2. Edge Dropout: reset the weights on the reduced graph and train within-round and between-round weights for accuracy minus a nuclear-norm sparsity term (a tractable stand-in for low rank), then keep only the top fraction of edges per matrix.

Inference runs the surviving graph and aggregates the final answers. Agent roles and prompts are taken as given (copied from AgentPrune); only the topology is learned. Dropout rates were 0.1 or 0.2.

## Evaluated on
- Beats AgentPrune on six benchmarks (MMLU, four math sets, HumanEval) at all three model sizes. Average accuracy: Llama3-8B 68.70 vs 66.51, Qwen2.5-72B 91.58 vs 90.81, DeepSeek-V3 93.72 vs 93.25. The gain shrinks as the model gets stronger: +2.19, +0.77, +0.47.
- Cuts tokens against the unpruned multi-round team: on average 21.6% fewer prompt tokens and 18.4% fewer completion tokens. AgentPrune mostly cuts prompt tokens only. On Llama3 the average is 3.3M prompt tokens vs 4.2M for AgentPrune and 4.7M unpruned.
- Both stages are needed. Unpruned team 65.72 average, learned node-only 66.83, edge-only 66.06, both 68.70. Random dropout in either stage (66.69, 66.13) does not match learned dropout, which argues the gain is not simply from shorter chains. Training both matrices in one pass instead of two stages gives 66.47, because removing nodes creates new reasoning chains that need re-training.
- Works from other topologies: starting from a layered or random graph still gives about 68.3 and 68.2 average vs 66.1 and 65.8 for the unpruned team, with fewer tokens.
- Transfers across math datasets: a topology learned on AQuA gives +1.59 over AgentPrune on average, on MultiArith +0.81. Harder training sets transferred better, which the authors state as a trend from two data points.
- Trade-off is explicit: raising the dropout rate to 0.8 drops average accuracy to 66.01 but cuts tokens to 856K prompt and 230K completion (vs 3.3M and 839K at 0.2). Even so it stays above the unpruned team's 65.72.

## Limitations admitted by the authors
- Only reasoning, math and code tasks were tested, so generality to other task types is unshown.
- Roles and prompts are hand-defined; a new domain still needs a designer to write the initial roles, since dropout only removes from what exists.
- Token use is still high despite the savings (millions of tokens per benchmark against about 68K prompt tokens for a single-agent run on Llama3), so the multi-agent cost premium remains large.
- On AQuA and HumanEval accuracy barely responds to the dropout rate, which the authors say calls for better-suited frameworks; they give no explanation.

## Limitations found by others

## What it leaves untried
- No variance, repeated runs or significance test is reported, and the gain over AgentPrune on the stronger models is under one point (0.47, 0.77); whether it exceeds sampling noise at temperature 1 is unsupported.
- Rounds are fixed (2 for reasoning and math, 4 for code) and the dropped set is fixed per task after training; there is no per-query decision on who speaks, which the management-theory motivation would suggest.
- No comparison with single-agent compute-matched baselines (for example self-consistency at equal token budget), so it is unclear whether the surviving team beats spending the same tokens on one model.

## Topics
[[Topic - automated pipeline and topology search]] · [[Topic - communication topology and channels]]
