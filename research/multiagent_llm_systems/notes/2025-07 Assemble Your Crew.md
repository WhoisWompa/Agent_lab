---
title: Assemble Your Crew: Automatic Multi-agent Communication Topology Design via Autoregressive Graph Generation
authors: Shiyuan Li et al.
date: 2025-07
arxiv: 2507.18224
url: https://arxiv.org/abs/2507.18224
venue: AAAI 2026
category: topology-communication
pdf: research/multiagent_llm_systems/pdfs/2507.18224.pdf
folder: ["multiagent_llm_systems"]
topics: ["automated pipeline and topology search", "communication topology and channels"]
---
# Assemble Your Crew: Automatic Multi-agent Communication Topology Design via Autoregressive Graph Generation

## One line
ARG-Designer generates a task-specific multi-agent team, its size, roles and communication links, from scratch one agent at a time, instead of pruning a fixed template graph.

## Method
Earlier learned-topology methods (AgentPrune, AgentDropout, G-Designer) start from a fixed template with a predefined agent set and densely connected edges, then prune or reweight it. The authors name two consequences. Redundant composition: unneeded agents and links survive pruning, costing tokens and possibly hurting decisions. Limited extensibility: a model trained on one template cannot take in new agent roles, and a template covering every role would be prohibitively expensive.

The paper recasts topology design as conditional graph generation, P(graph | query, role pool). The graph is a directed acyclic graph, factorised autoregressively: at each step the model picks the next agent's role, or a special END token, then decides for each earlier agent whether an edge runs from it to the new one. Team size is therefore decided by the model rather than fixed.

Architecture: GRUs in two levels. A node generator combines the task embedding with a GRU summary of the roles chosen so far, through a learned gate. It scores roles by dot product between a "node intent" vector and role embeddings, which is a retrieval step rather than a fixed-size classifier. An edge generator, a second GRU, then predicts links to each prior node. Because roles are scored by similarity, new roles can be added at inference by appending an embedding row, without retraining. This is the paper's route to extensibility.

Training uses supervised imitation of synthetic graphs in two stages. Stage 1 (cold start) uses rich configurations such as star or mesh with several agents, keeping only graphs that solved the task. Stage 2 (efficiency fine-tuning) mixes simple minimal configurations, pruned versions of stage-1 graphs that still succeed, and a replay slice of stage 1 to avoid forgetting. The aim is to move from correct but dense graphs to correct and sparse ones. Training uses only 40 to 60 queries per dataset.

## Evaluated on
- Best average accuracy across six benchmarks (MMLU, GSM8K, MultiArith, SVAMP, AQuA, HumanEval) with GPT-4o: 92.78 vs 90.04 for G-Designer and 87.53 for LLM-Debate. The vanilla single model scores 80.80. The largest gap over G-Designer is on AQuA (86.45, +4.85).
- Fewer tokens at higher accuracy on GSM8K: 94.40% with 4.1e6 tokens, about half of G-Designer's usage while exceeding its accuracy. Debate-style structures reach good accuracy at much higher token cost.
- Efficiency fine-tuning cuts tokens at no accuracy cost. On MMLU, accuracy rises from 88.23 to 89.54 with nearly 30% fewer tokens. On GSM8K, tokens fall 34% (6.25e6 to 4.1e6).
- Conditioning on the task matters most in the ablation. Without the task embedding the three-benchmark average drops from 91.89 to 89.76. Without history embedding it is 90.64, and without fine-tuning 91.28.
- More robust to a system-prompt attack on one agent: 2.15% degradation, the least among compared topologies. The authors attribute this to distributed risk and redundant paths, but the paper gives no analysis of the generated graphs to confirm it.
- Extensibility is shown by one case. After adding a "Lawyer" role with no retraining, a contract-law MMLU question produced a graph with the lawyer at the centre. This is a single illustrative example, not a measured result.

## Limitations admitted by the authors
- The paper has no dedicated limitations section. The only caveat it states is that the agent count and topology type in training data are generation settings, which it says do not limit the model.

## Limitations found by others

## What it leaves untried
- Generalisation to unseen tasks or domains: the model is trained per dataset on 40 to 60 queries, and no cross-dataset or out-of-distribution test is reported. It is therefore unclear whether it learns a general design principle or memorises dataset-specific graphs.
- Extensibility at scale: new roles are tested in one qualitative case. No quantitative test of accuracy when many unseen roles join the pool, or of how the pool grows.
- Other backbones and tasks: all results use GPT-4o, with role profiles written by GPT-4. Weaker models, long-horizon agentic tasks and a comparison against workflow-search methods such as AFlow are absent.

## Topics
[[Topic - automated pipeline and topology search]] · [[Topic - communication topology and channels]]
