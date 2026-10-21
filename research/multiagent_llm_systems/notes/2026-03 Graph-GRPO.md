---
title: Graph-GRPO: Stabilizing Multi-Agent Topology Learning via Group Relative Policy Optimization
authors: Yueyang Cang et al.
date: 2026-03
arxiv: 2603.02701
url: https://arxiv.org/abs/2603.02701
venue: arXiv
category: topology-communication
pdf: research/multiagent_llm_systems/pdfs/2603.02701.pdf
folder: ["multiagent_llm_systems"]
topics: ["automated pipeline and topology search", "communication topology and channels"]
---
# Graph-GRPO: Stabilizing Multi-Agent Topology Learning via Group Relative Policy Optimization

## One line
Trains a generator of per-query agent communication graphs by sampling a group of graphs and scoring each edge by how much its presence goes with success relative to the group, instead of rewarding the whole graph with a 0/1 outcome.

## Method
The problem: learned-topology methods (G-Designer, EIB-Learner) train with REINFORCE on one sampled graph and a binary correctness reward. The authors name two faults. First, variance from task difficulty. On an easy query nearly any graph gets reward 1, so redundant edges are reinforced. On a hard query every graph fails, so there is no gradient. Second, credit assignment. A success credits every edge equally, so edges that did nothing are rewarded along with the ones that mattered.

The fix borrows GRPO from LLM reasoning training. The policy is kept as in G-Designer: a fixed MiniLM encoder embeds each agent's role plus the query, and a graph attention network produces an edge probability matrix. A DAG mask allows edges only from earlier agents to later ones. For each query, K graphs are sampled by independent Bernoulli draws per edge. All K are executed and given a 0/1 reward.

Each edge gets a score: the success rate among sampled graphs that contain it (a counterfactual-style estimate of P(success | edge present)). Scores are normalized by their mean and standard deviation over the active edges in the group, giving an edge advantage. Above-average edges are pushed up and below-average edges down. When every graph succeeds, all scores are equal and the advantage is near zero, so the update is blocked. This is the stated mechanism for ignoring "easy-win" noise. A KL term to the supervised-initialized reference policy keeps updates stable, and there is no critic network. At inference the graph is the edge probabilities thresholded at 0.5, a single static topology per query.

## Evaluated on
- Beats the prior best learned topology on six benchmarks, averaging 92.45% against 91.38% for EIB-Learner (+1.07). Per-benchmark gains include +0.9 on GSM8K and +2.1 on HumanEval. Backbone is GPT-3.5-Turbo, group size K=16, and baseline numbers are copied from the EIB-Learner paper.
- Edge-level credit matters. Giving every edge in a sampled graph the same advantage (graph-level GRPO) drops the average by 1.82 points. The drop is largest on HumanEval (-2.18), on MMLU/GSM8K/HumanEval only.
- Denser is not better. A complete graph averages 82.16%, below a plain chain (84.53%), which the authors read as information overload.
- Cost sits near the pruning methods. The token-efficiency plot shows usage comparable to AgentPrune and EIB-Learner with higher accuracy, while debate and complete graphs cost far more. This is shown only as a figure, with no token counts in the text.

## Limitations admitted by the authors
- The policy is a GAT with O(N^2) cost. It was run with at most 6 agents, and the authors expect bottlenecks on swarms of N>100.
- Each query gets one static topology. Multi-turn dialogues, where the best structure may change per turn, would need turn-level adjustment.

## Limitations found by others

## What it leaves untried
- No variance, seeds or significance are reported. The gains over EIB-Learner are 0.5 to 2 points on benchmarks where the baseline is already at 83 to 97%, so it is unclear whether they exceed run-to-run noise.
- The abstract claims better training stability and faster convergence, but the text shows no training curves or gradient-variance measurement. Only final accuracy is compared, so the stability claim is unsupported.
- Only GPT-3.5-Turbo and short single-turn reasoning and code tasks are tested. Whether the edge scores identify causal edges is also untested. Edges are sampled independently, so an edge's success rate can be confounded by the other edges that happened to co-occur in the same 16 samples. No analysis of the learned graphs or of the 16-sample estimate's reliability is given.
- Cost of training is not reported. Each query needs K=16 full multi-agent executions, which may offset the inference-time token savings.

## Topics
[[Topic - automated pipeline and topology search]] · [[Topic - communication topology and channels]]
