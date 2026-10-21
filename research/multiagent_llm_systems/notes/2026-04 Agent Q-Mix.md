---
title: Agent Q-Mix: Selecting the Right Action for LLM Multi-Agent Systems through Reinforcement Learning
authors: Eric Hanchen Jiang, Levina Li et al.
date: 2026-04
arxiv: 2604.00344
url: https://arxiv.org/abs/2604.00344
venue: arXiv
category: topology-communication
pdf: research/multiagent_llm_systems/pdfs/2604.00344.pdf
folder: ["multiagent_llm_systems"]
topics: ["automated pipeline and topology search", "communication topology and channels", "team theory and distributed decision making"]
---
# Agent Q-Mix: Selecting the Right Action for LLM Multi-Agent Systems through Reinforcement Learning

## One line
Each agent in an LLM team picks its own communication action every round with a QMIX-trained policy, and the chosen actions together form the round's communication graph, trading accuracy against token cost.

## Method
Problem: earlier adaptive-topology methods (G-Designer, TopoDIM, GTD) generate the whole communication graph at once with a central generator. Agents therefore make no communication decisions of their own during execution, and the joint topology objective is never split into per-agent contributions.

Idea: treat topology as a cooperative multi-agent RL problem (a "Networked MMDP"). Each agent chooses one of six discrete structural actions per round: solo process (no outgoing edges), broadcast all, selective query (one target), aggregate refine (collect from all), execute verify (pass to the next agent), debate check (mutual edge with one partner). The actions set connectivity only, not message content. Together they map to an adjacency matrix, and agents run in topological order. A final decision node aggregates the outputs.

Each agent's Q-network is a graph neural network over the current graph, then a GRU carrying memory across rounds, then an MLP giving Q-values over the six actions. QMIX mixes the per-agent Q-values with non-negative weights, so greedy per-agent choice also maximises the joint value (the Individual-Global-Max property). That is the reason decentralised execution is justified after centralised training. The reward is accuracy minus a token-cost term capped at a 10,000-token budget.

Design: one team per domain (two specialists plus an analyst agent). Separate checkpoints were trained per domain on 15 examples for 50 episodes, then tested on held-out benchmarks. Math runs 3 rounds, code and reasoning 2.

## Evaluated on
- Highest average accuracy of all methods with GPT-OSS:120B across seven benchmarks: 72.73%, versus 68.60% for AutoGen (the best commercial framework) and 60.37% for GTD (the best adaptive-topology method). With Gemini-3.1-Flash-Lite it also leads: 66.90% versus 64.88% for Microsoft Agent Framework.
- Gains are largest on hard math. HMMT 2025 reaches 53.33% against 43.33% for the next best prior method, and Beyond-AIME reaches 42.00% against 37.00% for AutoGen. On HLE (first 250 multiple-choice items, Gemini) it scores 20.8%, against 19.2% for both LangGraph and Microsoft Agent Framework.
- Robust to a bad agent. With one of three agents replaced by an adversary on MMLU-Pro, accuracy drops 2.86 points (92.86 to 90.00), versus 8.57 for LLM-Debate and 10.00 for GPTSwarm and AutoGen. The authors say the learned adjacency matrices show the adversary's outgoing edges cut sharply.
- Cheaper than most multi-agent baselines. On MMLU-Pro it uses 112K tokens versus 471K to 2.71M for other multi-agent methods. On Beyond-AIME it uses 708K versus 1.00M to 2.68M. The policy picks solo process on near-saturated LiveCodeBench and broadcast all on math.

## Limitations admitted by the authors
- The convergence proof holds only in a realizable tabular setting (finite states, every state-action visited infinitely often). With the GNN, GRU and MLP actually used, the authors say only approximate fixed points are expected, so the theory does not guarantee the trained policy.
- The only explicit hedge is that the policy is trained per domain (three checkpoints, 15 examples each). Whether one policy works across domains is not tested.

## Limitations found by others


## What it leaves untried
- No ablation isolates what QMIX contributes. There is no comparison against a centralised generator trained with the same reward, or against independent per-agent Q-learning, so the claim that decentralised factorisation is what helps is unsupported. Only a rounds ablation is mentioned (Figure 5d), and its numbers are not in the text.
- Small test sets and no variance reporting beyond "median of three runs". AIME and HMMT have 30 problems each and MMLU-Pro has 70, so one problem is 3.3 points on the 30-problem sets. Several gaps are of that size, for example HLE 20.8% versus 19.2%.
- Only teams of three agents are tested, and no result on how the method scales with agent count. The robustness test covers one adversary type, a deliberately wrong answerer. The claim of transfer to new domains rests on Appendix E showing different action mixes, not on an unseen-domain test.

## Topics
[[Topic - automated pipeline and topology search]] · [[Topic - communication topology and channels]] · [[Topic - team theory and distributed decision making]]
