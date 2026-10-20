---
title: JudgeLRM: Large Reasoning Models as a Judge
authors: Nuo Chen et al.
date: 2025-03
arxiv: 2504.00050
url: https://arxiv.org/abs/2504.00050
venue: arXiv
category: trained-judges-reward-models
---
# JudgeLRM: Large Reasoning Models as a Judge

## One line
RL-trained reasoning judges (3B-14B) with judge-specific outcome rewards; shows SFT gains shrink as the share of reasoning-heavy judging samples grows.

## Method
- GRPO with rewards for structure, relation (which answer better) and absolute score closeness.

## Evaluated on
- JudgeLRM-3B/4B exceed GPT-4; 7B/8B/14B beat DeepSeek-R1 by over 2% F1 ([arXiv](https://arxiv.org/abs/2504.00050)).

## Limitations admitted by the authors
- SFT performance gains negatively correlated with proportion of reasoning-demanding samples.

## Limitations found by others


## What it leaves untried
- Harder meta-eval (JudgeBench, RewardBench 2).
