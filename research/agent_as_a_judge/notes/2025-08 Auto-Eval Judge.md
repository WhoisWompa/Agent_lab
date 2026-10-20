---
title: Auto-Eval Judge: Towards a General Agentic Framework for Task Completion Evaluation
authors: Roshita Bhonsle et al.
date: 2025-08
arxiv: 2508.05508
url: https://arxiv.org/abs/2508.05508
venue: arXiv
category: agent-as-judge
---
# Auto-Eval Judge: Towards a General Agentic Framework for Task Completion Evaluation

## One line
Domain-independent judge agent that decomposes a task into sub-tasks and checks each step of the actor agent's trajectory before aggregating a completion verdict.

## Method
- Modular: each module handles one aspect (task decomposition, step validation using the actor's output and reasoning, aggregation). Reads the trajectory, not only the final output. Module/tool details not in the abstract.

## Evaluated on
- Actor: Magentic-One on GAIA and BigCodeBench. Vs GPT-4o LLM-as-a-Judge: +4.76% alignment accuracy with humans on GAIA, +10.52% on BigCodeBench.

## Limitations admitted by the authors
- No limitations section visible at abstract level; one actor agent, two benchmarks.

## Limitations found by others


## What it leaves untried
- Testing generality across many actor agents and domains; reporting cost and variance.
