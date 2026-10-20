---
title: Terminal-Bench 2.0 and the Harbor framework
org: Laude Institute / Stanford (Terminal-Bench team)
date: 2025-11
url: https://www.tbench.ai/leaderboard/terminal-bench/2.0
kind: benchmark
category: third-party-and-benchmarks
---
# Terminal-Bench 2.0 and Harbor

## One line
A benchmark of 89 Docker-containerised command-line tasks for agent-plus-model combinations, run with the Harbor framework. It was the most cited terminal or agentic coding benchmark in 2026 model cards.

## What they do
- **Tasks**: 89 tasks scored by tests inside containers. Submissions are agent-plus-model pairs.
- **Leaderboard**: tbench.ai lists audited entries with viewable trajectories ([HF README](https://huggingface.co/datasets/harborframework/terminal-bench-2.0/blob/main/README.md)).
- **Harbor**: the runtime that scales evaluations across cloud containers (`harbor run -d terminal-bench@2.0`) ([Harbor docs](https://harborframework.com/docs/running-tbench); [VentureBeat](https://venturebeat.com/ai/terminal-bench-2-0-launches-alongside-harbor-a-new-framework-for-testing)).
- **Harbor hub**: also hosts other benchmarks, including tau3-bench and SWE-rebench.
- **Later versions**: Artificial Analysis uses Terminal-Bench 4.0 ([AA v4.3](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-3)). A Terminal-Bench 4.0 release page was not fetched.

## Evidence
- Snapshot of 9 Mar 2026 (secondary, [Morph](https://www.morphllm.com/terminal-bench-2)):
  - Forge Code + Gemini 3.1 Pro: 78.4%
  - Droid + GPT-5.3-Codex: 77.3%
  - Simple Codex + GPT-5.3-Codex: 75.1%
- Snorkel's view shows 142 entries with a median of 44% ([Snorkel](https://snorkel.ai/leaderboard/terminal-bench-2-0/)).
- No standings for October 2026 were confirmed.

## Limitations and criticisms
- Epoch labelled Terminal-Bench 4.0.0 Flawed on 4 Sep 2026 ([Epoch registry](https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks)).
- A contributor replied that the flaws affect fewer than 3% of runs and stay within the confidence intervals ([Digg](https://digg.com/ai/5lxkqram)).
- Vendor-submitted agent scaffolds allow selection of the best configuration.

## Relevance to agent evaluation
- Scores are reported for the harness and model together, which is the right unit for agents.
- Trajectories are public, so an agent judge can audit them.
