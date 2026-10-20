---
title: JudgeBench: A Benchmark for Evaluating LLM-based Judges
authors: Sijun Tan et al.
date: 2024-10
arxiv: 2410.12784
url: https://arxiv.org/abs/2410.12784
venue: ICLR 2025
category: trained-judges-reward-models
---
# JudgeBench: A Benchmark for Evaluating LLM-based Judges

## One line
Benchmark of hard response pairs whose correctness is objectively verifiable (knowledge, reasoning, math, code), to test judges on correctness instead of style.

## Method
- Pairs built from the same strong model's responses; labels from ground truth; position-consistent scoring.

## Evaluated on
- GPT-4o only slightly better than random ([arXiv](https://arxiv.org/abs/2410.12784)). Later: J1-Qwen-32B 71.4, DeepSeek-R1 68.9, o1-mini 64.2 (J1 paper); 'Outcome Accuracy is Not Enough' GenRM 82.0 (arXiv:2602.04649); one Sept 2026 paper reports a GPT-6 judge at 93.1% on a JudgeBench subset (arXiv:2609.26550).

## Limitations admitted by the authors
- Labels require objective ground truth, so subjective quality is out of scope.

## Limitations found by others


## What it leaves untried

