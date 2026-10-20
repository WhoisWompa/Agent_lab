---
title: UserProxyBench: Evaluating LLM User Simulators for Agent Benchmarks and Training
authors: Ashish Jain, Armaan Sandhu
date: 2026-09
arxiv: 2609.38043
url: https://arxiv.org/abs/2609.38043
venue: arXiv
category: agent-evaluation-benchmarks
---
# UserProxyBench: Evaluating LLM User Simulators for Agent Benchmarks and Training

## One line
Scores the simulated user (User Fidelity Score, rubric-based) separately from agent success on tau-bench-family tasks.

## Method
Agent fixed (GPT-5.5), user proxy varied across 375 enterprise tasks and seven proxies.

## Evaluated on
Swapping only the user moves mean reward 15.2 points; 24.4% of successful episodes contain a user-spec violation, mostly premature disclosure (1.06 fewer tool calls).

## Limitations admitted by the authors


## Limitations found by others


## What it leaves untried

