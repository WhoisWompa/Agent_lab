---
title: trajectory-judge: What Outcome-Only LLM Judges Miss on Agent Trajectories
authors: Hadi Mohammadi (Utrecht University)
date: 2026-09
arxiv: 2609.00038
url: https://arxiv.org/abs/2609.00038
venue: arXiv (workshop paper on verifying agents)
category: agent-as-judge
topics: ["LLM and agent judges", "agent evaluation benchmarks"]
---
# trajectory-judge: What Outcome-Only LLM Judges Miss on Agent Trajectories

## One line
Injects single-step faults into correct customer-support agent runs and shows that judges seeing only the final reply cannot detect faults that leave the reply unchanged, while step-level trajectory judges can; proposes paired discrimination as the metric.

## Method
- Deterministic support-desk environment with scripted oracle; injector creates six fault types; each fault paired with its clean parent.
- Judges: 8-rule engine; outcome-only judge (Qwen2.5 14B, request + final reply); step judge (same model, full trajectory, check each step; also Llama 3.1 8B); self-consistency of 3 samples.
- Metric: paired discrimination = flag rate on faults minus flag rate on clean parents. Not an agentic judge; cites Agent-as-a-Judge in related work only.

## Evaluated on
- 400 trajectories (100 clean, 175 silent faults, 125 loud).
- Outcome judge: loud recall 0.84, silent 0.45, false alarm 0.33; paired discrimination +0.163, and **zero** on the four reply-unchanged fault types.
- Step judge 14B: silent recall 0.77, 0/100 false alarms, flags every reply-unchanged fault; paired discrimination +1.00 when asked to check each step.
- 8B judge flags 397/400 - high recall, no discrimination. Majority vote of 3 triples cost with no gain. Detecting vs typing faults are separate: 257/300 detected, 74 mistyped.

## Limitations admitted by the authors
- One environment; injected single-step faults unlike real failures; two local models; faults are 75% of data so precision/F1 not deployment values; small clean set.

## Limitations found by others


## What it leaves untried
- Same paired-fault protocol applied to tool-using agentic judges and to multi-step / compounding faults.

## Topics
[[Topic - LLM and agent judges]] · [[Topic - agent evaluation benchmarks]]
