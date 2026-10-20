---
title: RM-R1: Reward Modeling as Reasoning
authors: Xiusi Chen et al.
date: 2025-05
arxiv: 2505.02387
url: https://arxiv.org/abs/2505.02387
venue: arXiv (UIUC)
category: trained-judges-reward-models
---
# RM-R1: Reward Modeling as Reasoning

## One line
Reasoning reward models: distil reasoning traces, then RL with a binary correctness reward, using a Chain-of-Rubrics rollout that either writes rubrics (chat) or solves the problem first (reasoning).

## Method
- Distillation on about 9K traces from Claude-3.7-Sonnet, about 25% corrected by o3; then GRPO with +1/-1 reward for correct preference.
- Pairwise judge; categorises the prompt first.

## Evaluated on
- 32B variants average 81.2-81.5 across RewardBench, RM-Bench, RMB vs INF-ORM-Llama3.1-70B 78.8 and GPT-4o 77.7; RM-Bench 83.9 with 91.8 math, 74.1 code ([HTML](https://arxiv.org/html/2505.02387)).

## Limitations admitted by the authors
- RL alone insufficient; needs distillation first.
- Future work: active preference collection, multimodal/agentic RMs.

## Limitations found by others
- RewardBench 2 (arXiv:2506.01937) top-20 is still led by classifier Bradley-Terry RMs rather than reasoning RMs.

## What it leaves untried
- Agentic reward modelling with tools.
