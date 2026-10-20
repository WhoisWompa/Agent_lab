---
title: Coding Agents Index: GitHub Copilot coding agent
org: amplifying.ai
date: 2026-08
url: https://amplifying.ai/coding-agents/github-copilot
kind: third-party-evaluator
category: production-practice
---
# Coding Agents Index: GitHub Copilot coding agent

## One line
Third-party tracker estimating merge rates of agent-authored public PRs on GitHub.

## What they do
Counts agent-created public PRs and their merge and human-review status over 8-week windows.

## Evidence
Copilot coding agent: 80.5% merged (260,778/323,847, Apr-Jun 2026) then 68.4% (87,128/127,335, Jun-Aug 2026); 78.3% of merged PRs had human review in significant repos. Academic comparison (Polytechnique Montreal, 9,428 agent PRs in 489 Python repos): Copilot 68.1%. GitHub added official agent-PR merge fields to its usage-metrics API (https://github.blog/changelog/2026-04-08-copilot-reviewed-pull-request-merge-metrics-now-in-the-usage-metrics-api).

## Limitations and criticisms
Public repos only; tracker says estimates can swing 30-40% between runs; "a high merge rate with a low review rate means the agent self-merges, not that a human signed off."

## Relevance to agent evaluation
Merge rate is now the de facto external metric for coding agents, but self-merge and task selection make it a weak quality signal.
