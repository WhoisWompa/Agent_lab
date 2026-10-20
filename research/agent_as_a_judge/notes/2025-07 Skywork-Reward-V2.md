---
title: Skywork-Reward-V2: Scaling Preference Data Curation via Human-AI Synergy
authors: Chris Yuhao Liu et al.
date: 2025-07
arxiv: 2507.01352
url: https://arxiv.org/abs/2507.01352
venue: ICLR 2026
category: trained-judges-reward-models
---
# Skywork-Reward-V2: Scaling Preference Data Curation via Human-AI Synergy

## One line
Scalar Bradley-Terry RMs (0.6B-8B) trained on 26M pairs curated from a 40M-pair pool by a human-verified then LLM-scaled curation pipeline; top of RewardBench 2.

## Method
- SynPref-40M; two-stage curation: human annotations verify, LLMs curate automatically guided by them.
- Classic scalar classifier RM, no reasoning.

## Evaluated on
- Claims SOTA on seven RM benchmarks ([arXiv](https://arxiv.org/abs/2507.01352)). On RewardBench 2, Skywork-Reward-V2-Llama-3.1-8B is top at 84.1 (Factuality 84.6, Precise IF 66.3, Math 77.6, Safety 96.7, Focus 98.4, Ties 81.2) ([RB2 HTML](https://arxiv.org/html/2506.01937v2)).

## Limitations admitted by the authors
- Gains attributed to curation, not scale; curation pipeline costly.

## Limitations found by others
- RewardBench 2 PPO study: top benchmark RM is not necessarily best for RLHF if from another model lineage.

## What it leaves untried
- Reasoning or tool use; classifier cannot explain verdicts.
