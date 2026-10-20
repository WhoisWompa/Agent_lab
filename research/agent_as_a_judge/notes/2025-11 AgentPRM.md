---
title: AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress
authors: Zhiheng Xi et al.
date: 2025-11
arxiv: 2511.08325
url: https://arxiv.org/abs/2511.08325
venue: arXiv
category: agent-evaluation-benchmarks
---
# AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress

## One line
Process reward model for multi-turn agents scoring steps by promise (chance of reaching goal) and progress (dependence between steps), not step correctness.

## Method
Labels from TD estimation with GAE instead of Monte Carlo rollouts.

## Evaluated on
Over 8x more compute-efficient than baselines; robust gains when scaling test-time compute; also used for RL. Tasks: web shopping, browser navigation.

## Limitations admitted by the authors


## Limitations found by others


## What it leaves untried

