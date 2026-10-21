---
title: Benchmarking LLM Judges for Mobile Agent Evaluation
authors: Ziqiang Wang et al.
date: 2026-08
arxiv: 2608.11434
url: https://arxiv.org/abs/2608.11434
venue: arXiv
category: agent-evaluation-benchmarks
pdf: agent as a judge papers/Benchmarking LLM Judges for Mobile Agent Evaluation - MobileJudgeBench (2026).pdf
folder: ["agent as a judge"]
topics: ["judge and decision-model audits", "agent evaluation benchmarks"]
---
# Benchmarking LLM Judges for Mobile Agent Evaluation

## One line
MobileJudgeBench: 931 human-annotated mobile-agent trajectories (6 benchmarks, 4 agents, 68 apps) to compare LLM-judge methods.

## Method
- Six judge methods (SPA-Bench, A3 final-state / essential-states, AndroidArena, AgentRewardBench, simple baseline) x five backends (Qwen2.5-VL-72B, GPT-5-mini, Gemini 3 Flash, GLM-4.6V, Claude Sonnet 4.5). All single-pass over recorded screenshots/actions/UI trees/reasoning; none interacts with the device (added by agent-as-judge-core researcher).

## Evaluated on
Simple sampled-screenshot baseline matches or beats purpose-built judges; the backbone LLM matters most; two backbones show opposite (conservative vs permissive) failure profiles; judge-benchmark scores predict usefulness as RL reward.
- Numbers (added by agent-as-judge-core researcher): 931 trajectories, 289 tasks; human pairwise agreement 88.4%; accuracy 76.4%-90.9% (best simple baseline + Gemini 3 Flash), i.e. 9-24% misclassified; backend shifts one method by 5.6-10.5 pts; agent rankings move up to 13 places; balanced accuracy/F1 predict ranking reliability, precision does not. RL with judge rewards (45.4/42.6/39.9%) underperformed rule reward (54.6%). GPT judges: false negatives via last-frame anchoring; Qwen judges: false positives on partial completion; surface UI similarity fools all.

## Limitations admitted by the authors
- Binary labels only; training study on AndroidWorld with one judge; root-cause coding subjective (kappa 0.957 on 30) (added by agent-as-judge-core researcher).

## Limitations found by others


## What it leaves untried
- Agentic judges that query device state after the run instead of trusting the last frame (added by agent-as-judge-core researcher).

## Topics
[[Topic - judge and decision-model audits]] · [[Topic - agent evaluation benchmarks]]
