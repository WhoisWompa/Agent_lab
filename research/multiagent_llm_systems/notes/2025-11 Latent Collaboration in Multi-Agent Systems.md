---
title: Latent Collaboration in Multi-Agent Systems
authors: Jiaru Zou et al.
date: 2025-11
arxiv: 2511.20639
url: https://arxiv.org/abs/2511.20639
venue: ICML 2026
category: topology-communication
pdf: research/multiagent_llm_systems/pdfs/2511.20639.pdf
folder: ["multiagent_llm_systems"]
topics: ["communication topology and channels"]
---
# Latent Collaboration in Multi-Agent Systems

## One line
LatentMAS lets LLM agents think and hand work to each other entirely through hidden states and shared KV caches instead of text, with no training, cutting tokens and time while raising accuracy.

## Method
Text-based multi-agent systems make each agent decode its reasoning into tokens, which the next agent must re-read. That is slow and compresses the agent's internal state into a narrow discrete channel. LatentMAS replaces both steps with continuous latent operations.

- Latent thoughts: instead of sampling a token, an agent feeds its last-layer hidden state back in as the next input, for m latent steps (tested at 0 to 80). Raw hidden states look unlike token embeddings, so a one-time linear map (the pseudo-inverse of the output head times the input embedding) pulls them back into the valid input space.
- Latent working memory: when an agent finishes, its layer-wise KV cache (input context plus latent thoughts) is prepended to the next agent's cache. The next agent receives the predecessor's full state without re-encoding. Only the last agent decodes text.
- Theory: under a linear-representation assumption, expressing m latent steps in text needs at least on the order of d_h·m / log|V| tokens, which the authors illustrate as 235.7 to 471.4 times more efficient for Qwen3 4B to 14B. They also claim KV transfer is equivalent to passing the predecessor's output as input, and that per-agent cost is lower than text MAS at equal expressiveness.
- The design is architecture-agnostic. It is tested on a sequential chain (planner, critic, refiner, solver) and a hierarchical setup (code, math and science experts feeding a summarizer).

## Evaluated on
- Beats a single model and text MAS on 9 benchmarks with Qwen3 4B, 8B and 14B: average gain over single model 14.6% (sequential) and 13.3% (hierarchical), over text MAS 2.8% and 4.6%.
- Output tokens fall 70.8% (sequential) and 83.7% (hierarchical) versus text MAS, and end-to-end speed is 4.0x and 4.3x faster, even against text MAS served on vLLM (2.6x to 7x).
- Gains over text MAS are small and sometimes negative: on ARC-E, Qwen3-8B 98.8 vs 99.1 text MAS; ARC-C 94.4 vs 94.6. The headline is efficiency at equal or slightly better accuracy.
- Reasoning-heavy tasks work with under 50 latent steps, where text MAS needs over 20K output tokens on AIME24/25.
- The alignment map matters: removing it costs 2.3% to 5.3% accuracy on three tasks. Accuracy peaks around 40 to 80 latent steps, then plateaus or declines.
- A "debug mode" decodes latent thoughts to text. Intermediate text is correct in 96.2% of correct final answers and wrong in 90.0% of wrong ones (80 and 20 cases), so it works as a probe.

## Limitations admitted by the authors
- All agents must share the same transformer layer shape, since KV caches are concatenated layer by layer. Mixed-model teams are not supported. The authors only suggest a trainable adapter, untested.
- Latent thoughts are not human-readable. Auditing needs the debug mode, validated on only 100 cases (80 correct, 20 wrong).
- More latent steps eventually hurt (decline past roughly 40 to 80 steps), so the step budget needs tuning per setup. The paper tunes hyperparameters and gives no rule.
- The latent protocol is not optimised. Post-training it, as is done for text MAS, is named as future work.

## Limitations found by others

## What it leaves untried
- Agents of different models or sizes, the realistic case for mixed-vendor teams. The same-architecture requirement is the main barrier to adoption.
- Open-weight access is required (hidden states and KV caches), so hosted API models cannot join. The paper does not discuss this.
- Any comparison with trained latent-communication methods such as cache-to-cache. They are cited as needing extra training but are not run as baselines in the main results.
- Whether the theory's linear-representation assumption holds in practice. The speedup claims rest on it, and the paper's evidence for it is only an embedding-space visualisation.

## Topics
[[Topic - communication topology and channels]]
