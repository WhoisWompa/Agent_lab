---
title: Critique-out-Loud Reward Models
authors: Zachary Ankner et al.
date: 2024-08
arxiv: 2408.11791
url: https://arxiv.org/abs/2408.11791
venue: arXiv
category: trained-judges-reward-models
topics: ["trained judges and reward models", "preference learning"]
---
# Critique-out-Loud Reward Models

## One line
Reward model first generates a natural-language critique, then a reward head scores the response conditioned on that critique.

## Method
- Base Llama-3-8B/70B; critiques supervised from a stronger model (oracle critiques), then the RM is trained on preference data with the critique in context. Output scalar, pairwise-trained.

## Evaluated on
- RewardBench pairwise accuracy improves by roughly 4.7 (8B) and 5.8 (70B) points over classic RMs; better Best-of-N on ArenaHard (paper abstract, recalled; verify).

## Limitations admitted by the authors
- On-policy critique training matters; off-policy critiques help less.
- Extra inference cost.

## Limitations found by others


## What it leaves untried
- Using the critique for self-consistency voting at scale (DeepSeek GRM does).

## Topics
[[Topic - trained judges and reward models]] · [[Topic - preference learning]]
