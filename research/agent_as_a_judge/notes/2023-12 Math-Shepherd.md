---
title: Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations
authors: Peiyi Wang et al.
date: 2023-12
arxiv: 2312.08935
url: https://arxiv.org/abs/2312.08935
venue: ACL 2024
category: trained-judges-reward-models
topics: ["trained judges and reward models", "judges as reward signals"]
---
# Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations

## One line
Labels steps automatically by Monte Carlo rollouts (a step is good if completions from it reach the right answer) and uses the resulting PRM for reranking and step-by-step PPO.

## Method
- Synthetic, completion-based step labels (hard or soft estimation).

## Evaluated on
- Mistral-7B with step-by-step PPO: GSM8K 77.9 to 84.1, MATH 28.6 to 33.0; with verification 89.1 and 43.5 (paper abstract, recalled).

## Limitations admitted by the authors
- MC labels are noisy; depends on completer strength.

## Limitations found by others
- Qwen PRM lessons (arXiv:2501.07301): MC-estimated labels give worse performance and generalisation than LLM-as-judge or human labels.
- ProcessBench (arXiv:2412.06559): Math-Shepherd-PRM-7B averages 31.5 F1; 23.8 on Omni-MATH.

## What it leaves untried
- Label steps by checking validity rather than reachability of the answer.

## Topics
[[Topic - trained judges and reward models]] · [[Topic - judges as reward signals]]
