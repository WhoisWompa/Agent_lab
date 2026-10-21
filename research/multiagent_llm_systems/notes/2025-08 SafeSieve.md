---
title: "SafeSieve: From Heuristics to Experience in Progressive Pruning for LLM-based Multi-Agent Communication"
authors: Ruijia Zhang et al.
date: 2025-08
arxiv: 2508.11733
url: https://arxiv.org/abs/2508.11733
venue: arXiv (AAAI 2026 copyright notice)
category: topology-communication
pdf: research/multiagent_llm_systems/pdfs/2508.11733.pdf
folder: ["multiagent_llm_systems"]
topics: ["communication topology and channels", "automated pipeline and topology search"]
---
# SafeSieve: From Heuristics to Experience in Progressive Pruning for LLM-based Multi-Agent Communication

## One line
Prunes the communication graph of a multi-agent system during execution by scoring each edge first from LLM-judged role compatibility and then from its record of contributing to correct answers, and cutting edges along cluster boundaries instead of greedy top-k.

## Method
The problem: dense, all-to-all agent conversation costs many tokens, buries key information, and widens the attack surface for prompt injection. Earlier fixes either build a sparse graph before the task (GPTSwarm, G-Designer; cannot adapt at run time) or prune a full graph during the run with greedy top-k (AgentPrune, AgentDropout; may cut critical paths). The authors say no earlier method joins both stages.

SafeSieve starts from a fully connected graph and keeps a score per edge. Three parts:
- **Score that shifts over time.** At the start an edge's score is role-embedding similarity mixed with a quantized (5-level) compatibility rating from an expert LLM. As the run progresses, the weight moves linearly to a historical term: the share of all correct-answer contributions that went through that edge. The reasoning is plan first, adjust with experience later.
- **0-extension clustering.** Instead of dropping the lowest edges one by one, it picks a few terminal agents (at least 2, at most min(sqrt n, n/3)) and assigns every agent to one, minimizing the total inverse-score of edges that cross clusters. Only cross-cluster edges below a rising threshold are pruned (a budget rule tops up to the target rate). The stated purpose is to keep coherent groups and avoid "information islands"; isolated nodes are removed only if more than two agents remain.
- **Warm-up and rescaling.** Pruning begins after a warm-up and scores are re-normalized after each cut.

It needs no GPU or trained network. Its claim that clustering gives "theoretical guarantees" is borrowed from the 0-extension literature; the paper does not prove anything for this use.

## Evaluated on
- **Best average accuracy among pruning methods, with fewer tokens.** With DeepSeek-V3 on six benchmarks: 94.01% average vs AgentPrune 92.78%, AgentDropout 92.62%, G-Designer 92.00%, and single-agent CoT 90.58%. Token cuts of 12.4-27.8% vs peers; on SVAMP 1.03M tokens vs AgentPrune's 1.23M (16.3% less) with 96.60% vs 95.40%.
- **Weaker lead on a small model.** With GPT-4o-mini the average is 87.61% vs AgentPrune 87.28%, and G-Designer beats it on MMLU (87.20% vs 82.32%), so the gain over baselines is a few tenths of a point.
- **Each part matters (HumanEval ablation).** Unpruned graph 95.50%; full method 95.01% at 27.8% fewer tokens. Without history 93.78%, without the LLM heuristic 94.41%, swapping clustering for top-k 93.13%.
- **More robust to injected bad agents.** Average accuracy drop 1.23 points vs AgentDropout 2.21 and AgentPrune 4.59. Suspicious agents get weights 0.1-0.3 vs 0.7-0.9 for normal ones, and are typically pruned within 30 batches.
- **Cheaper with mixed models.** DeepSeek-V3 as commander plus four smaller or other models cuts total cost 13.3% vs AgentPrune (115 to 99.3 cents), with accuracy 96.77% on SVAMP (vs 96.60% homogeneous).

## Limitations admitted by the authors
- The paper has no limitations section. The one weakness it states: on knowledge-heavy MMLU the mixed-model setup falls to 91.42% from 92.39%, which they call a "barrel effect" (weakest model limits the team). HumanEval also drops 1.23 points (93.78% vs 95.01%) for a 14.0% cost cut.
- Pruning is not free in accuracy: the unpruned graph scores 95.50% vs 95.01% on HumanEval, so the savings buy a 0.49-point loss there.

## Limitations found by others

## What it leaves untried
- Scale: only graphs of a few agents are tested; the paper never reports results on large agent counts, though it calls the method scalable (unsupported).
- Cost of the LLM compatibility scoring and the clustering step is not counted in the token savings; whether the saving survives that overhead is not shown.
- The injection test uses low-quality agents; adaptive attackers that mimic good contributions, which would fool a history-based score, are not tried.

## Topics
[[Topic - communication topology and channels]] · [[Topic - automated pipeline and topology search]]
