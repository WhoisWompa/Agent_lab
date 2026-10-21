---
title: RM-Bench: Benchmarking Reward Models of Language Models with Subtlety and Style
authors: Yantao Liu et al.
date: 2024-10
arxiv: 2410.16184
url: https://arxiv.org/abs/2410.16184
venue: ICLR 2025
category: trained-judges-reward-models
topics: ["judge and decision-model audits", "trained judges and reward models"]
---
# RM-Bench: Benchmarking Reward Models of Language Models with Subtlety and Style

## One line
Benchmark pairing responses that differ by subtle content errors while varying style (length, markdown) to expose style bias in RMs.

## Method
- Chat, code, math, safety; easy/normal/hard by style interference.

## Evaluated on
- Best RMs averaged only 46.6% in the hard setting, below chance ([arXiv](https://arxiv.org/abs/2410.16184)). Later: J1-Qwen-32B 90.3, RM-R1-32B 83.9, rationale-consistency GenRM 87.1 overall (arXiv:2602.04649).
- (llm-judge-foundations) Nearly 40 RMs. State of the art averages only 46.6% under style-bias interference (Hard), below random (50%). Claims strong correlation with downstream policy performance.

## Limitations admitted by the authors
- Focus on chat, safety, math, code domains; content errors are synthetic (injected).

## Limitations found by others
- Saha et al. 2025 EvalPlanner (2501.18099) and later thinking judges report gains on RM-Bench, suggesting reasoning partly offsets style bias.

## What it leaves untried
- Testing generative LLM judges with explicit rubrics on the Hard split as a style-bias mitigation.

## Topics
[[Topic - judge and decision-model audits]] · [[Topic - trained judges and reward models]]
