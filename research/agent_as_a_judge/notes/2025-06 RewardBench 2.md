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
- (llm-judge-foundations) Top: Skywork-Reward-V2-Llama-3.1-8B 84.1 (Precise IF 66.3, Math 77.6). LLM judges: Gemini 2.5 Pro 79.5 (Math 89.8, IF 61.9), Gemini 2.5 Flash 77.7, Claude Opus 4 76.5 (IF 41.9), Claude 3.7 Sonnet 75.4. Pearson r = 0.87 between RB2 score and best-of-N downstream across 113 RMs. PPO: only coarse signal; saturates in 49.8-68.5 range; off-lineage RMs do worse in PPO despite high RB2.

## Limitations admitted by the authors
- Accuracy is necessary, not sufficient for RLHF; PPO study used one policy (Tulu 3 8B SFT); Focus/Ties correlate weakly downstream.
- Accuracy is necessary but not sufficient for RLHF success.
- PPO study used 17 RMs sharing one tokenizer/policy.
- Focus and Ties are not captured by downstream evals.
- Math grading relies on majority vote plus manual checks because answer extraction is brittle.

## Limitations found by others
- Norman et al. 2026 (2606.19544): judge rankings shift by up to 14 places across RewardBench, JudgeBench and MT-Bench, so RewardBench-family scores do not transfer.

## What it leaves untried
- Agentic/multi-turn and tool-using judges.
- Agentic or multi-step trajectories; adversarial/master-key robustness of the scored RMs.

