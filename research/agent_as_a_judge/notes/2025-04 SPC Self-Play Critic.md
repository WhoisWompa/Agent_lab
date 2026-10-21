---
title: SPC: Evolving Self-Play Critic via Adversarial Games for LLM Reasoning
authors: Jiaqi Chen et al.
date: 2025-04
arxiv: 2504.19162
url: https://arxiv.org/abs/2504.19162
venue: arXiv
category: self-evolving-tests
topics: ["self-evolving tests", "trained judges and reward models"]
---
# SPC: Evolving Self-Play Critic via Adversarial Games for LLM Reasoning

## One line
A 'sneaky generator' learns to inject subtle reasoning errors and a critic learns to catch them; RL on game outcomes improves both over rounds.

## Method
Two copies of a base model: generator turns correct steps into subtly wrong ones; critic judges step correctness. Winner rewarded, loser penalised. Validity of injected errors is checked via their effect on final answers.

## Evaluated on
ProcessBench error-detection accuracy 70.8% -> 77.7%; gains on PRM800K and DeltaBench; better test-time search guidance on MATH500 and AIME2024 than SOTA PRMs.

## Limitations admitted by the authors
- Limited to math-style step verification with checkable final answers.

## Limitations found by others


## What it leaves untried
- Generalise generative-adversarial evaluation to agent trajectories, where validity of a 'subtle error' is harder to verify.

## Topics
[[Topic - self-evolving tests]] · [[Topic - trained judges and reward models]]
