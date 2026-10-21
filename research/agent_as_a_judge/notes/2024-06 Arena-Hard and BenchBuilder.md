---
title: From Crowdsourced Data to High-Quality Benchmarks: Arena-Hard and BenchBuilder Pipeline
authors: Tianle Li et al.
date: 2024-06
arxiv: 2406.11939
url: https://arxiv.org/abs/2406.11939
venue: arXiv
category: alternative-paradigms
topics: ["LLM and agent judges", "alternative evaluation paradigms"]
---
# From Crowdsourced Data to High-Quality Benchmarks: Arena-Hard and BenchBuilder Pipeline

## One line
Pipeline that filters crowdsourced Arena prompts into a hard static set (Arena-Hard-Auto) judged by an LLM, designed to separate models and agree with Arena rankings.

## Method


## Evaluated on
- (llm-judge-foundations) Arena-Hard-Auto: 3x higher model separation than MT-Bench, 98.6% correlation with human preference rankings, about $20 per evaluation run.

## Limitations admitted by the authors
- Inherits LLM-judge biases (length, style, self-preference); the target is agreement with Arena, which itself has the biases above.
- LLM judge bias (self-preference toward judge's family, length/style) acknowledged; style control added later.
- Prompt pool drawn from Arena users, so distribution follows Arena traffic.

## Limitations found by others
- Zheng et al. 2024 (arXiv 2410.07137): a constant 'null model' output gets 83.0 on Arena-Hard-Auto (as recalled).
- Zheng et al. 2024 (2410.07137): a null model scores 83.0 on Arena-Hard-Auto.
- Tan et al. 2024 JudgeBench (2410.12784): the Arena-Hard judge prompt with GPT-4o reaches only 56.6% on objectively labelled hard pairs, so high ranking correlation does not mean per-item correctness.
- Singh et al. 2025 'Leaderboard Illusion' (2504.20879): the human Arena that Arena-Hard is validated against is itself distorted by private testing and sampling asymmetries.

## What it leaves untried
- Correctness-checked judging (execution/verification) for the coding and math share of prompts.

## Topics
[[Topic - LLM and agent judges]] · [[Topic - alternative evaluation paradigms]]
