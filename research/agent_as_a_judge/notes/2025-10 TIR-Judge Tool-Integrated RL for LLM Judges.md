---
title: Incentivizing Agentic Reasoning in LLM Judges via Tool-Integrated Reinforcement Learning (TIR-Judge)
authors: Ran Xu et al.
date: 2025-10
arxiv: 2510.23038
url: https://arxiv.org/abs/2510.23038
venue: ICLR 2026
category: trained-judges-reward-models
---
# Incentivizing Agentic Reasoning in LLM Judges via Tool-Integrated Reinforcement Learning (TIR-Judge)

## One line
End-to-end RL for judges that can call a code executor while reasoning, across pointwise, pairwise and listwise formats.

## Method
- Iterative RL from base without distillation (TIR-Judge-Zero matches distilled version); verifiable and non-verifiable domains.

## Evaluated on
- Seven benchmarks: up to +6.4% pointwise and +7.7% pairwise over reasoning judges; listwise comparable to Claude-Opus-4 at 8B ([arXiv](https://arxiv.org/abs/2510.23038)).

## Limitations admitted by the authors


## Limitations found by others
- Judges text responses, not agent trajectories; the survey 2601.05111 cites it as the training-time optimisation exemplar for agentic judges (added by agent-as-judge-core researcher).

## What it leaves untried
- Retrieval/web tools, multi-file code.
