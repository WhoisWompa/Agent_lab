---
title: MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering
authors: Jun Shern Chan et al.
date: 2024-10
arxiv: 2410.07095
url: https://arxiv.org/abs/2410.07095
venue: ICLR 2025
category: agent-evaluation-benchmarks
topics: ["agent evaluation benchmarks"]
---
# MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering

## One line
75 Kaggle competitions; agent submissions scored by the competition metric against the human leaderboard (medals).

## Method
Grading by local re-implementation of each competition's metric on held-out test sets.

## Evaluated on
o1-preview with AIDE reached at least a bronze medal in 16.9% of competitions.

## Limitations admitted by the authors
- Contamination risk because Kaggle solutions are public; authors probe it.
- Locally reconstructed test splits differ from the original private leaderboards.

## Limitations found by others


## What it leaves untried

## Topics
[[Topic - agent evaluation benchmarks]]
