---
title: Which Agent Causes Task Failures and When? On Automated Failure Attribution of LLM Multi-Agent Systems
authors: Shaokun Zhang et al. (incl. Chi Wang, Qingyun Wu)
date: 2025-05
arxiv: 2505.00212
url: https://arxiv.org/abs/2505.00212
venue: ICML 2025
category: agent-evaluation-benchmarks
---
# Which Agent Causes Task Failures and When? On Automated Failure Attribution of LLM Multi-Agent Systems

## One line
Defines automated failure attribution and the Who&When dataset of failure logs from 127 multi-agent systems, labelled with responsible agent and decisive step.

## Method
Three LLM methods compared: all-at-once, step-by-step, binary search over the log.

## Evaluated on
Best: 53.5% agent-level, 14.2% step-level accuracy; some methods below random; o1 and R1 not practically usable.

## Limitations admitted by the authors
- Task is open; methods each have trade-offs.

## Limitations found by others


## What it leaves untried
- Agentic attribution that replays the system from the suspected step (counterfactual re-execution) instead of reading logs (added by agent-as-judge-core researcher).
