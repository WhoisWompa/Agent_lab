---
title: Thought Communication in Multiagent Collaboration
authors: Yujia Zheng et al.
date: 2025-10
arxiv: 2510.20733
url: https://arxiv.org/abs/2510.20733
venue: NeurIPS 2025
category: topology-communication
pdf: research/multiagent_llm_systems/pdfs/2510.20733.pdf
folder: ["multiagent_llm_systems"]
topics: ["communication topology and channels", "multi-agent debate and consensus"]
---
# Thought Communication in Multiagent Collaboration

## One line
Agents in a debate stop exchanging only text: a sparse autoencoder pulls latent "thoughts" out of every agent's hidden state, and each agent receives the thoughts relevant to it as a learned prefix, which lifts MATH and GSM8K accuracy and agreement over a multiagent-finetuning baseline.

## Method
- Problem: natural-language messages are lossy and ambiguous, and the authors cite earlier failure analyses that trace many multi-agent failures to vague messages and misalignment. Token and token-embedding exchange still inherits that limit.
- Model: before each round, the concatenated hidden states H of all agents are assumed to be an invertible, twice-differentiable function f of latent thoughts Z. Which thoughts feed which agent's state is the non-zero pattern of the Jacobian of f.
- Theory: in a nonparametric setting with no auxiliary labels, and under an l0 sparsity penalty on the estimated Jacobian, three results are proved, each up to permutation of the latents. (1) For any pair of agents, the thoughts they share are disentangled from all others. (2) Each agent's private thoughts are disentangled likewise. (3) The agent-to-thought sharing structure is identifiable. This is deliberately weaker than recovering every latent, which the authors say is impossible without extra assumptions. The proofs rest on a Jacobian-spanning assumption and use Hall's marriage theorem.
- System (ThoughtComm): an autoencoder trained to reconstruct hidden states with an l1 Jacobian penalty extracts thoughts. Each agent gets only the thoughts its state depends on, grouped by how many agents share each one and reweighted by that count. An adapter maps the result to a prefix prepended to the agent's token embeddings next round, in the style of prefix-tuning. The adapter is trained so a short continuation stays close in meaning and fluent against the no-latent-communication output. Only the autoencoder and adapter are trained, not the LLM, so cost scales with the embedding dimension, not the parameter count. The authors argue the pieces are task-agnostic and reusable, but do not test transfer across tasks.

## Evaluated on
- Identifiability holds on synthetic data. Shared and private regions are recovered by the sparse model but not by an unregularised baseline (R2 plot only, no numbers in the text). Mean correlation stays above the identifiable threshold across 8 setups from 124 to 1024 dimensions.
- Beats multiagent finetuning, the strongest baseline, on MATH with five small models (0.6B to 8B). Qwen3-1.7B reaches 93.0% against 75.8% for that baseline and 43.6% for a single answer. The average gain is 19.06% relative over the baseline and 67.23% over a single answer.
- Agreement rises with accuracy. Qwen3-0.6B on MATH has consensus 91.2% against 90.07%, with accuracy 85.0% against 71.2%.
- Not uniformly better. On GSM8K, Llama-3-8B scores 68.4% against 69.2% for the baseline, a gap inside the reported standard deviation of about 2. Qwen3-1.7B on GSM8K is 85.0% against 84.2%.
- Robust to more debate rounds (2 to 6). Multiagent finetuning loses accuracy while its consensus holds or rises, so its agents converge on wrong answers. ThoughtComm gains on both.
- Robust to design choices. Prefix length 1 to 16 changes accuracy by under 5%. Latent size matters up to about 512 to 1024 dimensions, then saturates. Going from 2 to 3 agents helps, and beyond 3 accuracy plateaus or dips for the baseline but holds for ThoughtComm.

## Limitations admitted by the authors
- Needs access to the models' hidden states, which closed-source API models do not expose. The proposed workaround, embedding each agent's response text and using that as a stand-in for the state, is described but not run.
- Extension to other modalities is claimed but not tested. Producing suitable embeddings is called a separate problem.
- High consensus does not imply correctness: the baseline's agreement rises while accuracy stalls. Consensus is therefore a weak signal on its own.
- One run misses a point because of a runtime limit (the agent-count figure).

## Limitations found by others

## What it leaves untried
- Theory and practice differ: the theorems assume an l0 penalty, but training uses l1, and invertibility of f and the Jacobian-spanning assumption are never checked on real LLM states. The paper does not test whether the recovered thoughts are the true shared and private ones in real models, only whether accuracy improves.
- No comparison against text-based debate with no fine-tuning, or against other latent-channel methods. The only multi-agent baseline is multiagent finetuning, and tests are math only, with 500 training and 500 test questions. Whether the gain comes from the identifiable-thought structure or merely from an injected learned prefix is not ablated.
- The task-agnostic claim, that the module is pretrained once and reused, is not tested across tasks.

## Topics
[[Topic - communication topology and channels]] · [[Topic - multi-agent debate and consensus]]
