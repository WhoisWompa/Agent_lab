---
title: Learning to Plan & Reason for Evaluation with Thinking-LLM-as-a-Judge (EvalPlanner)
authors: Swarnadeep Saha et al.
date: 2025-01
arxiv: 2501.18099
url: https://arxiv.org/abs/2501.18099
venue: ICML 2025
category: trained-judges-reward-models
topics: ["trained judges and reward models", "LLM and agent judges"]
---
# Learning to Plan & Reason for Evaluation with Thinking-LLM-as-a-Judge (EvalPlanner)

## One line
Judge first writes an unconstrained evaluation plan, then executes it, then gives the verdict; plans and executions are optimised by iterative self-training on synthetic pairs.

## Method
- Synthetic preference pairs (WildChat and MATH prompts); sample many plan+execution traces; DPO on correct vs incorrect verdict traces; iterate.

## Evaluated on
- J1 paper's table: EvalPlanner-Llama-70B 73.2 overall (PPE 67.9, RewardBench 93.8, RM-Bench 82.1, JudgeBench 56.6, FollowBenchEval 65.4); 8B much weaker (JudgeBench 30.2) ([J1 HTML](https://arxiv.org/html/2505.10320v3)).
- (llm-judge-foundations) RewardBench 93.9; gains on RM-Bench, JudgeBench, FollowBenchEval.

## Limitations admitted by the authors
- (self-evolving-tests slice) Synthetic training signal; RewardBench-centred evaluation.
- Relies on synthetic pairs; offline DPO rather than online RL.

## Limitations found by others
- J1 (arXiv:2505.10320) beats it with online RL on the same data family.

## What it leaves untried
- Tool use inside the plan.

## Topics
[[Topic - trained judges and reward models]] · [[Topic - LLM and agent judges]]
