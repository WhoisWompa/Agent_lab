---
title: J1: Incentivizing Thinking in LLM-as-a-Judge via Reinforcement Learning
authors: Chenxi Whitehouse et al.
date: 2025-05
arxiv: 2505.10320
url: https://arxiv.org/abs/2505.10320
venue: arXiv (Meta)
category: trained-judges-reward-models
topics: ["trained judges and reward models"]
---
# J1: Incentivizing Thinking in LLM-as-a-Judge via Reinforcement Learning

## One line
RL-trained thinking judge: converts both verifiable and non-verifiable judgment tasks into verifiable-reward format and trains with GRPO.

## Method
- Data: 22K synthetic preference pairs (17K WildChat, 5K MATH). Rewards for correct verdict and position consistency.
- Pairwise, pointwise and multitask variants; thinking traces include self-generated reference answers and criteria.

## Evaluated on
- Overall over five benchmarks: J1-Qwen-32B-MultiTask 80.8 (PPE 71.8, RewardBench 93.6, RM-Bench 90.3, JudgeBench 71.4, FollowBenchEval 77.1); DeepSeek-R1-671B 78.4; o1-mini 72.7; J1-Llama-70B 75.0 ([HTML](https://arxiv.org/html/2505.10320v3)).
- PPE Correctness: J1-Qwen-32B 76.8 vs DeepSeek-GRM-27B 59.8.
- (llm-judge-foundations) State of the art on several judge benchmarks (PPE, RewardBench, JudgeBench, RM-Bench among them) for its size.

## Limitations admitted by the authors
- Pointwise judges produce many ties; pairwise judges are position-sensitive (pointwise better on position-consistent accuracy, pairwise better under random order).
- No dedicated limitations section.

## Limitations found by others
- 'Outcome Accuracy is Not Enough' (arXiv:2602.04649) argues outcome-only RL for judges (J1 style) degrades rationale consistency: right verdicts for wrong reasons.

## What it leaves untried
- Tools (code execution, retrieval) inside the thinking trace (TIR-Judge does this).

## Topics
[[Topic - trained judges and reward models]]
