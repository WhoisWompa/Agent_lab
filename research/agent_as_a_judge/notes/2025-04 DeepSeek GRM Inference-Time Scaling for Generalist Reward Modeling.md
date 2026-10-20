---
title: Inference-Time Scaling for Generalist Reward Modeling (DeepSeek-GRM)
authors: Zijun Liu et al.
date: 2025-04
arxiv: 2504.02495
url: https://arxiv.org/abs/2504.02495
venue: arXiv (DeepSeek)
category: trained-judges-reward-models
---
# Inference-Time Scaling for Generalist Reward Modeling (DeepSeek-GRM)

## One line
Pointwise generative RM that writes its own principles then critiques; trained with Self-Principled Critique Tuning (online RL) and scaled at inference by parallel sampling plus a meta RM that filters samples before voting.

## Method
- Rejective fine-tuning then rule-based online RL (SPCT). Pointwise scores for any number of responses.
- Inference: k parallel samples, vote on scores; Meta RM picks reliable samples.

## Evaluated on
- DeepSeek-GRM-27B: greedy 69.9 overall; voting@32 71.0; MetaRM@32 72.8 (RewardBench 90.4, PPE Pref 67.2, PPE Correctness 63.2, RMB 70.3) vs GPT-4o 71.3, Nemotron-4-340B-Reward 70.5 ([HTML](https://arxiv.org/html/2504.02495v3)).

## Limitations admitted by the authors
- 'Challenges in efficiency and specific tasks'; generative RM costs much more compute than a scalar RM.
- Weaker on verifiable correctness (PPE Correctness ~60) than scalar RMs and later reasoning judges.

## Limitations found by others
- J1 (arXiv:2505.10320): J1-Qwen-32B 76.8 vs DeepSeek-GRM-27B 59.8 on PPE Correctness.

## What it leaves untried
- Tool-backed verification for correctness-heavy prompts.
