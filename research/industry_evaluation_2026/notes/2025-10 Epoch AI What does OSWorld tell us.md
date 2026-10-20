---
title: What does OSWorld tell us about AI's ability to use computers?
org: Epoch AI
date: 2025-10
url: https://epoch.ai/publications/what-does-osworld-tell-us-about-ais-ability-to-use-computers
kind: third-party-evaluator
category: third-party-and-benchmarks
---
# What does OSWorld tell us about AI's ability to use computers?

## One line
Epoch's audit of OSWorld (30 Oct 2025) found that many "computer-use" tasks barely need a GUI, that about 10% are invalid, and that the benchmark changes over time.

## What they do
Manual review of OSWorld's 361 tasks, covering:
- whether a task really needs a GUI;
- task validity;
- changes to instructions over time;
- dependence on the live web;
- how strict the verifiers are;
- how many steps a task takes.

## Evidence
- **GUI need**: about 15% of tasks can be done with a terminal alone. Another 30% or so can swap terminal and Python for most of the GUI work, so about 45% need little or no GUI.
- **Validity**:
  - About 10% of tasks have serious errors: wrong gold answers, evaluation functions that are too strict or too lax, or tasks that ask for no action.
  - About 8% are designed to be infeasible.
- **Drift**:
  - A July 2025 update (OSWorld-Verified) changed most instructions and evaluation functions, and about 10% more have changed since.
  - About 10% of tasks rely on live internet data.
- **Verifiers**: they check only the final machine state.
  - Some are too strict, such as requiring a specific time of day.
  - Some are too lax, such as checking only that zoom decreased.
  - Some are tied to fragile absolute XPaths.
- **Task length**:
  - Most tasks take fewer than 10 atomic steps.
  - About 12% take more than 20, and about 5% more than 50.
  - About one third involve more than one application.
- **Human baseline**: 72%.
- **2026 status** (secondary sources, unverified):
  - Aggregators show top OSWorld-Verified scores around 85%, with the top eight within 6 points ([benchmarklist](https://benchmarklist.com/benchmarks/osworld_verified/)).
  - A successor, "OSWorld 2", appears in vendor and aggregator listings ([datalearner](https://www.datalearner.com/en/benchmarks/osworld-2-offline-20260808)).

## Limitations and criticisms
- Epoch's estimate that ambiguity affects at most 28% of tasks is a rough inference from the human baseline.
- OSWorld is not in the 2026 Benchmark Reviews registry, so it has no formal verdict.

## Relevance to agent evaluation
- Checking only the final state misses how the agent got there. A judge that reads the trajectory would catch terminal shortcuts and could assess how the agent interpreted the intent.
- Benchmark versions drift, so comparing computer-use agents across time is unreliable.
