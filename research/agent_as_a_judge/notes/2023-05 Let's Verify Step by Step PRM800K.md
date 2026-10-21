---
title: Let's Verify Step by Step (PRM800K)
authors: Hunter Lightman et al.
date: 2023-05
arxiv: 2305.20050
url: https://arxiv.org/abs/2305.20050
venue: ICLR 2024
category: trained-judges-reward-models
topics: ["trained judges and reward models"]
---
# Let's Verify Step by Step (PRM800K)

## One line
Shows process supervision (human labels on every reasoning step) trains better math verifiers than outcome supervision; releases PRM800K.

## Method
- Human labellers marked about 800K steps (positive/negative/neutral) on about 75K GPT-4 solutions to 12K MATH problems; active learning picked convincing wrong-answer solutions.
- PRM scores a solution as the product of step-correctness probabilities; used for best-of-N.

## Evaluated on
- PRM solves 78.2% of a representative MATH test subset (best-of-1860), above ORM and majority voting; active learning about 2.6x more data-efficient (paper abstract).

## Limitations admitted by the authors
- Math only; human step labels expensive.
- Test-set contamination risk with MATH discussed.
- Only used for reranking, not RL.

## Limitations found by others
- ProcessBench (arXiv:2412.06559): a Qwen2.5-Math-7B PRM trained on PRM800K gets 56.5 average F1 at locating the first error, and drops from 68.2 (GSM8K) to 44.3 (Omni-MATH).

## What it leaves untried
- RL against the PRM and its hackability.

## Topics
[[Topic - trained judges and reward models]]
