---
title: Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation
authors: Tuhina Tripathi et al.
date: 2025-04
arxiv: 2504.14716
url: https://arxiv.org/abs/2504.14716
venue: COLM 2025
category: llm-judge-foundations
---
# Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation

## One line
Shows pairwise judging is more exploitable by distractor features than absolute scoring: preferences flip in ~35% of cases vs 9% for absolute scores.

## Method
Inject spurious attributes favoured by the judge (distractors) into lower-quality outputs; compare pairwise preference vs absolute scoring.

## Evaluated on
Pairwise preferences flip ~35% of the time, absolute scores ~9%. Recommends choosing protocol by dataset and objective.

## Limitations admitted by the authors


## Limitations found by others
- Landesberg 2026 (2603.12520): for best-of-N selection pointwise scoring creates ties in 67% of comparisons and recovers only 21% of the possible gain; explicit pairwise judging recovers 61% - so pointwise is more robust but less discriminative.
- Raina et al. 2024 (2402.14016) found the opposite direction for adversarial universal phrases: absolute scoring is more susceptible than comparative assessment.

## What it leaves untried
- Hybrid protocols (pointwise screening, pairwise for close calls).
