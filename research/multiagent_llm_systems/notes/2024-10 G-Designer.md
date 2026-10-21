---
title: "G-Designer: Architecting Multi-agent Communication Topologies via Graph Neural Networks"
authors: Guibin Zhang et al.
date: 2024-10
arxiv: 2410.11782
url: https://arxiv.org/abs/2410.11782
venue: arXiv
category: topology-communication
pdf: research/multiagent_llm_systems/pdfs/2410.11782.pdf
folder: ["multiagent_llm_systems"]
topics: ["communication topology and channels", "automated pipeline and topology search"]
---
# G-Designer: Architecting Multi-agent Communication Topologies via Graph Neural Networks

## One line
A variational graph auto-encoder, trained on a few dozen queries, outputs a sparse, per-query communication graph for a fixed set of LLM agents, so easy questions get small topologies and hard ones get larger ones.

## Method
The problem: published multi-agent topologies (chain, star, tree, complete, random, GPTSwarm, DyLAN) are static, but the best one depends on the task. On MMLU, a chain matches GPTSwarm on high-school biology at 0.5k tokens versus 7.8k, yet GPTSwarm beats the chain by 8.75% on college math. The paper states this as a "communication protocol" (MACP): a good topology should maximise utility, minimise overhead (adaptiveness) and lose little under adversarial perturbation. This is a three-term objective, not a guarantee.

The solution: each agent (backbone, role, tools) is embedded by a small text encoder (MiniLM) into a node. A virtual "task node", embedded from the query text, is linked to every agent. A user-given or LLM-written simple anchor graph (a chain in all experiments) supplies the starting edges. A two-layer GCN encodes this graph into latent vectors. The decoder first samples a dense edge-probability matrix from agent pairs plus the task node. It then compresses it by a low-rank step that keeps the result close to both the sketch and the anchor and penalises its nuclear norm, which sparsifies the graph. The surviving edges define who sees whose messages over K=3 dialogue rounds. A summarizer agent writes the final answer.

Training: the utility (task correctness) is not differentiable, so the graph sampler is trained with policy gradient (10 sampled graphs per query) on only 40 or 80 queries, then frozen. The idea is that the query embedding makes the graph input-dependent, while the anchor keeps it grounded and the sparsity term keeps it cheap. A suspicious agent can have its edges pruned, which the authors give as the reason for robustness (asserted, not directly tested).

## Evaluated on
- Best average accuracy among all methods: 89.84 over six benchmarks (MMLU, GSM8K, MultiArith, SVAMP, AQuA, HumanEval) against 87.32 for GPTSwarm and 87.01 for LLM-Debate. It is best on five of six; PHP's 95.50 beats G-Designer's 95.07 on GSM8K. All use gpt-4 agents.
- Cheaper at inference and training on GSM8K: 8.5e6 total tokens versus 1.4e7 for GPTSwarm and 2.2e7 for DyLAN, with higher accuracy (95.0 vs 89.7 and 88.1). Training takes 0.3h versus 2.1h for GPTSwarm. On SVAMP it beats DyLAN by 4% with 23.7% of its tokens.
- Topology follows difficulty: a trivial string-length task is reduced to two agents (designer, programmer), while harder tasks get denser graphs. This is shown by example figures, not a measured difficulty correlation.
- Robust to a prompt attack on one of five agents: 0.3% MMLU drop (84.5 to 84.2). Chain and complete graphs lose up to 11.0%, AutoGen 9.9%, DyLAN 6.2%, and GPTSwarm 0.3%.
- Scales to 20 agents using 6.11% of GPTSwarm's prompt tokens and 2.44% higher accuracy. Training with up to 1000 agents needs under 4GB.
- The ablation shows the task node matters most: removing it drops MMLU from 84.5 to 81.3. Removing sparsity makes the attacked GSM8K score fall to 90.7 from 92.5.
- The gain is not from the anchor: G-Designer beats the chain anchor by 9.50% on GSM8K.

## Limitations admitted by the authors
- None are listed. The impact statement claims no ethical concerns and says harmlessness holds if the base LLM is aligned, which is an unsupported assumption.

## Limitations found by others

## What it leaves untried
- Only gpt-4 and gpt-3.5 backbones, five fixed roles, and one attack type (system-prompt corruption of a single agent) are tested. Whether a graph trained for one domain transfers to another, or survives several attackers or attacks on messages, is untested.
- The graph is chosen once per query before dialogue starts. It is never revised mid-conversation from the agents' actual outputs, so a misjudged difficulty cannot be corrected.
- The anchor is always a chain and the training set is 40 to 80 queries. Sensitivity to other anchors and to training-set size or difficulty mix is not reported, so how the small training budget limits the learned designs is unknown.

## Topics
[[Topic - communication topology and channels]] · [[Topic - automated pipeline and topology search]]
