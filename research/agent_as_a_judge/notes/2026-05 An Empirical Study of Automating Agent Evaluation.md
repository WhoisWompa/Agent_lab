---
title: An Empirical Study of Automating Agent Evaluation
authors: Kang Zhou, Sangmin Woo, Haibo Ding et al. (AWS AI Labs)
date: 2026-05
arxiv: 2605.11378
url: https://arxiv.org/abs/2605.11378
venue: arXiv (v3 Sep 2026)
category: agent-as-judge
---
# An Empirical Study of Automating Agent Evaluation

## One line
EvalAgent: a coding-assistant agent that writes a whole evaluation (criteria, executable code, report) for a target agent from its source code and traces, using 'evaluation skills'; positions itself against Agent-as-a-Judge, which judges directly.

## Method
- Baselines: single-prompt LLM; agentic with source only; agentic with code + traces; plan-then-implement; EvalAgent = plan-then-implement + skills. Meta-evaluator: Claude Opus 4.5 with tools, pairwise. AgentEvalBench of 20 agents.

## Evaluated on
- Experts preferred EvalAgent in 79.5% (10.5% ties), Fleiss kappa 0.923. Meta-evaluator matched the human-majority winner 39/40, per-judgment 75% (AC1 0.687). Opus vs Sonnet agreement 86.6%; three Opus runs 76.3% three-way agreement (run-to-run non-determinism of the agentic meta-judge).
- Eval@1 62.5% (Haiku), 65% (Sonnet); baselines 15-60%. Context7 docs: Sonnet 20% -> 65%. ~31% fewer tokens, ~58% less time than plan-then-implement.
- Weaknesses of unconstrained agentic evaluators: code 2.4-6.6x longer, fallback to keyword heuristics in 35-75% of agents, traces improved relevance but reduced executability, plan-code drift (semantic rubrics planned, shallow checks implemented).

## Limitations admitted by the authors
- 20 agents only; Claude models only; ~1/3 of generated evaluations still need manual debugging; evaluation quality is subjective.

## Limitations found by others


## What it leaves untried
- Cross-model-family evaluators to rule out self-preference; checking whether generated evals catch injected faults.
