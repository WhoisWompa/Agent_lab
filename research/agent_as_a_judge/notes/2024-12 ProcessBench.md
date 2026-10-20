---
title: ProcessBench: Identifying Process Errors in Mathematical Reasoning
authors: Chujie Zheng et al.
date: 2024-12
arxiv: 2412.06559
url: https://arxiv.org/abs/2412.06559
venue: ACL 2025
category: trained-judges-reward-models
---
# ProcessBench: Identifying Process Errors in Mathematical Reasoning

## One line
Benchmark of 3,400 competition-level math solutions with expert-annotated earliest error step; tests whether PRMs and critics can locate the first wrong step.

## Method
- Task: output the index of the earliest erroneous step or declare all correct. Metric: harmonic mean (F1) of accuracy on erroneous and correct samples.

## Evaluated on
- F1 averages: Math-Shepherd-PRM-7B 31.5; RLHFlow-PRM-Mistral-8B 28.4; Skywork-PRM-7B 42.1; Qwen2.5-Math-7B-PRM800K 56.5; GPT-4o 61.9; Qwen2.5-72B-Instruct 61.2; QwQ-32B-Preview 71.5; o1-mini 87.9 ([HTML](https://arxiv.org/html/2412.06559v4)).
- Correct-answer-but-flawed-process share: 3.5% GSM8K, 18.8% MATH, 32.2% OlympiadBench, 51.8% Omni-MATH.

## Limitations admitted by the authors
- Math only; earliest-error framing ignores later errors.

## Limitations found by others


## What it leaves untried
- Process benchmarks for code, agents and proofs.
