---
title: "TopoDIM: One-shot Topology Generation of Diverse Interaction Modes for Multi-Agent Systems"
authors: Rui Sun et al.
date: 2026-01
arxiv: 2601.10120
url: https://arxiv.org/abs/2601.10120
venue: arXiv
category: topology-communication
pdf: research/multiagent_llm_systems/pdfs/2601.10120.pdf
folder: ["multiagent_llm_systems"]
topics: ["automated pipeline and topology search", "communication topology and channels"]
---
# TopoDIM: One-shot Topology Generation of Diverse Interaction Modes for Multi-Agent Systems

## One line
Learns, with reinforcement learning, a per-query agent graph whose edges are of three types (conditioned, feedback, debate), generated in one pass so that no multi-round dialogue is needed.

## Method
Problem: topology methods such as GPTSwarm and G-Designer mix intra-round (within a round) and inter-round (across rounds) dialogue. Every extra round triggers another full round of agent talk, so token cost compounds. Single-round schemes are cheap but, the authors say, hard to keep accurate.

Idea: move the interaction richness out of repeated rounds and into the edge types of a single graph.
- Three edge types. Conditioned: the receiver answers the query given the sender's output. Feedback: the receiver critiques the sender's output and the sender re-answers. Debate: the receiver challenges the sender for two rounds, then answers with that context. A fourth option is no edge.
- A relational graph encoder runs over a prior agent graph written by an LLM (GPT-5), with node features from role and query embeddings. An autoregressive decoder then picks an edge type for each agent pair, with a mask that keeps the graph acyclic.
- Adaptive sparsification keeps the top-scoring edges by a budget ratio alpha and drops agents left without edges. Execution is breadth-first from the root.
- Training is policy gradient on a reward that mixes task success (0/1) with the Shannon entropy of the edge-type mix, to stop the policy collapsing onto one edge type. A moving-average baseline and an entropy bonus reduce variance and aid exploration.
- Decentralisation: the central policy is distilled (KL divergence) into a small local network per agent, so each agent decides its own links, for adaptability and privacy. The privacy benefit is asserted, not measured.

## Evaluated on
- Beats the strongest baseline on six reasoning, math and code benchmarks across three base models. Average gain over the strongest baseline: 1.35% (Gemma-3-12B), 1.50% (GPT-OSS-120B), 1.38% (DeepSeek-V3.2). On GPT-OSS-120B the average is 90.32 vs 88.98 for G-Designer.
- Cheaper: the abstract claims 46.41% fewer total tokens than state-of-the-art methods. Figure 4 shows savings of 1.42M tokens on MMLU-Pro and 2.44M on LiveCodeBench (GPT-OSS-120B), at equal or better accuracy.
- Edge diversity helps: adding feedback and debate edges to conditioned-only graphs gives +2.21% on MMLU-Pro and +2.18% on LiveCodeBench.
- The LLM-written graph prior and the learned topology both matter: random heterogeneous edges lose 5.60% on average, and a fully connected graph with random edge types loses 1.99%.
- Sparsity matters: accuracy peaks at alpha = 0.7, and the authors attribute denser graphs' drop to redundant channels and hallucination (the mechanism is not tested).
- Mixed-size teams (three GPT-OSS-20B, two GPT-OSS-120B) gain 1.86% over homogeneous-topology baselines, by pruning low-contribution agents.
- Cheap to train: gains are largest within the first 40 optimisation queries, and 40 distillation queries are enough for the local policies.

## Limitations admitted by the authors
- Only three direct interaction forms are covered. Coalition formation and other organisational structures are not studied, so the claim of "diverse" modes is narrow.
- Heterogeneous teams are hard to get right: adding random agents gives small gains when the task exceeds their ability. Serving models with different architectures also needs engineering effort.
- Multi-agent systems still cost more tokens and latency than a single LLM. The authors stay with text-based topologies for compatibility with proprietary models, rather than latent-space communication.

## Limitations found by others

## What it leaves untried
- No comparison with latent-space communication. The authors name it as an alternative that cuts cost, yet it is the main competitor to cheaper text topologies.
- The per-edge-type contribution is tested only as adding types in a fixed order (conditioned, then feedback, then debate). Which type carries the gain, and on which task, is not separated.
- The decentralised policy is never compared with the central one on accuracy. The text reports only that 40 samples are "robust", and the privacy gain is not tested.

## Topics
[[Topic - automated pipeline and topology search]] · [[Topic - communication topology and channels]]
