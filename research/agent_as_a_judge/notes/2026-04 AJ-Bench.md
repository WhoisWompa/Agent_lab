---
title: AJ-Bench: Benchmarking Agent-as-a-Judge for Environment-Aware Evaluation
authors: Wentao Shi et al. (USTC, NUS, Meituan)
date: 2026-04
arxiv: 2604.18240
url: https://arxiv.org/abs/2604.18240
venue: ACL 2026 Findings
category: agent-as-judge
---
# AJ-Bench: Benchmarking Agent-as-a-Judge for Environment-Aware Evaluation

## One line
Benchmark that tests whether LLM agents can judge other agents' trajectories by actively using tools and live environments (search, databases/filesystem, Office GUIs), against the same models without tools.

## Method
- Judges built on the MCPMark framework; 60 tools. Data-system environments (filesystem, Postgres from MCPMark) replayed locally so the judge can inspect the final state; GUI environments (PowerPoint/Word/Excel from OSWorld) on isolated AWS instances with accessibility tree + screenshots; Search tasks (Mind2Web2, WideSearch) judged against the live web, long pages summarised by the same model.
- Binary success/failure verdicts; metric F1.

## Evaluated on
- 155 tasks, 516 annotated trajectories, 3 domains.
- Tool use gives ~13 F1 points on average: gpt-5-mini-low 59.00 (LLM-judge) -> 72.41 (agent-judge); deepseek-v3.2 64.49 -> 77.34. Best LLM-as-judge (gemini-3-pro-preview) 75.05. Average agent-judge F1 ~0.72.
- Higher reasoning effort not consistently helpful (deepseek-v3.2 thinking < non-thinking); more interaction turns help, mostly at small budgets; multimodal input helps unevenly across GUI subdomains.
- Failure modes: not calling a needed tool, calling wrong tools, misreading tool outputs (most common in Search and DS), wrong reasoning despite correct evidence; one case of verdict contradicting reasoning (FAIL reasoning, PASS output).

## Limitations admitted by the authors
- Most tasks adapted from existing benchmarks.
- Search domain depends on live web connectivity/stability.
- Plans to build tasks independently and scale.

## Limitations found by others
- AgentHorizon (2610.11050) finds tool access does not consistently help: some open models do better as direct judges than agentic ones, and harness choice shifts accuracy by several points.

## What it leaves untried
- Measuring run-to-run variance and cost per verdict for agent judges.
- Judges that re-execute or replay actions to test counterfactuals rather than only inspect final state.
