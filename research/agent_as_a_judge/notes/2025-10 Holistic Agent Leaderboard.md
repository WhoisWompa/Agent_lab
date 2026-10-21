---
title: Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation
authors: Sayash Kapoor et al.
date: 2025-10
arxiv: 2510.11977
url: https://arxiv.org/abs/2510.11977
venue: arXiv
category: agent-evaluation-benchmarks
topics: ["agent evaluation benchmarks"]
---
# Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation

## One line
Standardised harness and leaderboard (HAL) running 21,730 rollouts over 9 models x 9 benchmarks, with LLM-aided log inspection.

## Method
Common harness across hundreds of VMs; cost tracked; ~2.5B tokens of logs released; LLM-aided analysis of logs.

## Evaluated on
About $40,000 total. Higher reasoning effort reduced accuracy in most runs. Log inspection found agents searching HuggingFace for the benchmark instead of solving the task, and misusing credit cards in flight booking: behaviours invisible to outcome scores.

## Limitations admitted by the authors


## Limitations found by others


## What it leaves untried
- Turning log inspection into a scored, validated trajectory judge.

## Topics
[[Topic - agent evaluation benchmarks]]
