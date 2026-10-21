---
title: τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains
authors: Shunyu Yao et al.
date: 2024-06
arxiv: 2406.12045
url: https://arxiv.org/abs/2406.12045
venue: arXiv / ICLR 2025
category: agent-evaluation-benchmarks
pdf: agent as a judge papers/tau-bench - A Benchmark for Tool-Agent-User Interaction (Yao 2024).pdf
folder: ["agent as a judge"]
topics: ["agent evaluation benchmarks", "user simulation"]
---
# τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

## One line
Customer-service agent (retail, airline) talks to an LLM-simulated user and calls APIs under a policy; graded by comparing final database state to the goal state, with pass^k for reliability.

## Method
User simulated by an LLM given a hidden scenario; verifier = final DB state match plus required outputs. Introduces pass^k (all k trials succeed).

## Evaluated on
GPT-4o function-calling agent under 50% in retail at release, pass^8 below 25%.

## Limitations admitted by the authors
- (self-evolving-tests slice) User simulator can be inconsistent; tasks are static.
- Simulated users can make errors or be inconsistent.

## Limitations found by others
- (added by alternative-paradigms researcher) Seshadri et al. 2026 (arXiv 2601.17087): simulated users shift agent success by up to 9 points depending on user LLM and are miscalibrated vs real users.
- (added by alternative-paradigms researcher) Zhu et al. 2025 (arXiv 2507.02825) report outcome-validity issues in tau-bench (as recalled).
- Zhu et al. (2507.02825): tau-bench counts empty responses as success on some tasks.
- Sim2Real (2603.11245): 451 humans vs 31 simulators; simulators are over-cooperative and inflate agent success.
- Lost in Simulation (2601.17087): success shifts up to 9 pp depending on user LLM.
- UserProxyBench (2609.38043): swapping only the user proxy moves mean reward 15.2 pts; 24.4% of successful episodes have a user-spec violation.
- Decision-fidelity paper (2606.20708): simulator always pursues the goal, cannot walk away.

## What it leaves untried

## Topics
[[Topic - agent evaluation benchmarks]] · [[Topic - user simulation]]
