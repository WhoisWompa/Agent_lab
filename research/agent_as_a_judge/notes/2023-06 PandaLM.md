---
title: PandaLM: An Automatic Evaluation Benchmark for LLM Instruction Tuning Optimization
authors: Yidong Wang et al.
date: 2023-06
arxiv: 2306.05087
url: https://arxiv.org/abs/2306.05087
venue: ICLR 2024
category: trained-judges-reward-models
topics: ["trained judges and reward models", "LLM and agent judges"]
---
# PandaLM: An Automatic Evaluation Benchmark for LLM Instruction Tuning Optimization

## One line
A 7B LLaMA pairwise judge for choosing instruction-tuning hyperparameters, trained on GPT-3.5 labels.

## Method
- Data: about 300K pairwise samples labelled by GPT-3.5 (synthetic, filtered).
- Output: win/tie/lose plus a short reason and a reference answer.

## Evaluated on
- On a 1K human-annotated test set, reported F1 reaching about 94% of GPT-3.5's and about 88% of GPT-4's (paper abstract).

## Limitations admitted by the authors
- Teacher is GPT-3.5, which caps quality.
- Focus is relative ranking of models during tuning, not absolute grading.
- Small judge; subjective criteria.

## Limitations found by others
- Huang et al. (arXiv:2403.02839) include PandaLM among fine-tuned judges that do not transfer across formats/benchmarks.
- JudgeBench (2410.12784): 13.1%.

## What it leaves untried
- Multi-domain or reasoning-heavy evaluation.

## Topics
[[Topic - trained judges and reward models]] · [[Topic - LLM and agent judges]]
