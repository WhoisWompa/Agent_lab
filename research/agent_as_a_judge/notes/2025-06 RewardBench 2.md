---
title: RewardBench 2: Advancing Reward Model Evaluation
authors: Saumya Malik et al.
date: 2025-06
arxiv: 2506.01937
url: https://arxiv.org/abs/2506.01937
venue: ICLR 2026
category: trained-judges-reward-models
---
# RewardBench 2: Advancing Reward Model Evaluation

## One line
Harder successor to RewardBench (1,865 prompts, best-of-4 format, new human prompts) that correlates with downstream best-of-N and probes PPO usefulness.

## Method
- Six subsets: Factuality 475, Safety 450, Focus 495, Math 183, Precise IF 160, Ties 102. Each item: one correct vs three incorrect.

## Evaluated on
- Models score about 20 points lower than on RewardBench 1. Top: Skywork-Reward-V2-Llama-3.1-8B 84.1. Precise IF is lowest for nearly every model (many 35-50); Math and Factuality also hard. Pearson r = 0.87 with best-of-N downstream ([HTML](https://arxiv.org/html/2506.01937v2)).
- PPO: RMs from a different lineage or prompt distribution than the policy do much worse despite high benchmark scores.

## Limitations admitted by the authors
- Accuracy is necessary, not sufficient for RLHF; PPO study used one policy (Tulu 3 8B SFT); Focus/Ties correlate weakly downstream.

## Limitations found by others


## What it leaves untried
- Agentic/multi-turn and tool-using judges.
