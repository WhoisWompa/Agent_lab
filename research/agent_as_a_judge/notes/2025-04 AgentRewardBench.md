---
title: AgentRewardBench: Evaluating Automatic Evaluations of Web Agent Trajectories
authors: Xing Han Lù et al. (incl. Siva Reddy)
date: 2025-04
arxiv: 2504.08942
url: https://arxiv.org/abs/2504.08942
venue: arXiv
category: agent-evaluation-benchmarks
---
# AgentRewardBench: Evaluating Automatic Evaluations of Web Agent Trajectories

## One line
Meta-benchmark of 1,302 expert-labelled web-agent trajectories (5 benchmarks, 4 agent LLMs) for testing LLM judges on success, side effects and repetition.

## Method
Experts label each trajectory for success, side effects, repetitiveness; 12 LLM judges compared, plus a simplified judge with screenshot and/or accessibility-tree input.

## Evaluated on
Best judge (simplified, GPT-4o, accessibility tree): precision 69.8%, recall 83.1%; no judge above 70% precision. Official rule-based checks: precision 83.8%, recall 55.9%. Input ablation (GPT-4o-mini): screenshot only 64.5 P / 78.3 R; a11y tree only 61.5 / 86.1; both 62.1 / 81.7 (extra input distracted); neither 60.7 / 73.9. Failure modes: grounding mismatch, being misled by the agent's own claim of success, missed instruction details (found the product, never bought it), missing that the agent wrongly declared a task infeasible. Inter-annotator agreement 89.3% on success (one agent, WebArena).

## Limitations admitted by the authors
- 4 agent backbones, 5 benchmarks; AssistantBench split only 33 tasks.
- Ambiguity resolved by discussion with a lenient default.
- No single judge best everywhere.

## Limitations found by others
- MobileJudgeBench (2608.11434) found the AgentRewardBench-style judge not consistently better than a simple screenshot-sampling baseline on mobile.

## What it leaves untried
- Judges that can query the environment's final state instead of reading the trajectory.
