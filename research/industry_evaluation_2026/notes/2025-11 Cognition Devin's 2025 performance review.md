---
title: Devin's 2025 Performance Review: Learnings From 18 Months of Agents At Work
org: Cognition
date: 2025-11
url: https://cognition.com/blog/devin-annual-performance-review-2025
kind: production-practice
category: production-practice
---
# Devin's 2025 Performance Review: Learnings From 18 Months of Agents At Work

## One line
Cognition's 14 Nov 2025 "performance review" of Devin, reporting production outcome metrics (67% of PRs merged vs 34% a year earlier) and where the coding agent succeeds and fails, largely from customer-reported figures.

## What they do
- Evaluates by production outcome rather than benchmark: merge rate, time per task vs human baselines, customer anecdotes. "67% of its PRs are now merged vs 34% last year"; "hundreds of thousands of PRs" merged.
- Succeeds on tasks with "clear, upfront requirements and verifiable outcomes" worth 4-8 junior-engineer hours: migrations, security fixes, unit tests, small tickets.
- Struggles with ambiguity and mid-task changes: performs worse "when you keep telling it more after it starts the task."
- "Human review is still necessary, because code quality is not straightforwardly verifiable"; humans write testing playbooks; code owners check coverage.
- Cognition also reportedly runs an internal benchmark, FrontierCode (tasks from real open-source PRs graded on reviewer-defined criteria; 150-task Extended set) - secondary reports only, e.g. https://runtimewire.com/zh/article/cognition-adds-grok-4-6-to-devin-s-multi-model-coding-platform.

## Evidence
"4x faster at problem solving", "2x more efficient in resource consumption"; security fix 30 min human vs 1.5 min Devin; migration 3-4 h vs 30-40 h per file; Litera: test coverage +40%, regression cycles 93% faster. Most figures customer-reported, no denominators.

## Limitations and criticisms
Merge-rate denominator, window and definition not given; vendor metric not independently replicable (https://agentmarketcap.ai/blog/2026/07/13/cognition-devin-67-percent-pr-merge-rate-vendor-production-metric, commentary suggests pairing merge rate with 30-day revert rate). Merge rate is a selection-biased proxy (users assign easier tasks).

## Relevance to agent evaluation
Merge rate is becoming the headline production metric for coding agents, but its weaknesses (task selection, no quality-after-merge signal, self-merges) are why human review stays in the loop.
