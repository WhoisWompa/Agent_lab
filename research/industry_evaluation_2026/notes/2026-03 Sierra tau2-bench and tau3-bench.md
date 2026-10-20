---
title: tau2-bench / tau3-bench (tool-agent-user benchmark)
org: Sierra Research
date: 2026-03
url: https://hub.harborframework.com/datasets/sierra-research/tau3-bench
kind: benchmark
category: third-party-and-benchmarks
---
# tau2-bench / tau3-bench (Sierra)

## One line
Sierra's benchmark for customer-service agents. The agent talks to an LLM-simulated user and works with domain tools and policies. It is now in its third generation (tau3), maintained in the tau2-bench repo, and the telecom domain is near saturated.

## What they do
- **Task**: the agent must follow a domain policy and use tools while an LLM plays the user.
- **Scoring**: database end-state plus pass^k over repeated trials.
- **Domains**:
  - tau2 added a telecom domain (network, plan, billing, troubleshooting) in which the user also acts on their own device.
  - tau3 reportedly has 375 tasks across airline, retail, telecom and banking knowledge ([benchmarkingagents](https://benchmarkingagents.com/tau3-bench)). This is unverified.
- The official leaderboard typically uses gpt-4.1-2025-04-14 as the user simulator ([evalscope docs](https://evalscope.readthedocs.io/en/latest/third_party/tau2_bench.html)).

## Evidence
- Snapshot from March 2026 (secondary, [BenchLM](https://benchlm.ai/benchmarks/tau2Bench)): on tau2 telecom, GPT-5.4 scored 98.9%, GPT-5.4 mini 93.4% and GPT-5.4 nano 92.5%. Only four models were listed.

## Limitations and criticisms
- Results depend on which model simulates the user.
- Telecom is close to saturated.
- No official tau3 rankings by domain were found.
- HAL's reliability work shows large drops from pass@1 to pass^8 on tau-bench (see the HAL note).

## Relevance to agent evaluation
- This is the standard benchmark for agents that follow policy in conversation.
- The user simulator is itself an LLM, so the quality of simulation is a hidden variable.
- pass^k is the right reliability metric for deployed agents.
