---
title: WebArena: A Realistic Web Environment for Building Autonomous Agents
authors: Shuyan Zhou et al.
date: 2023-07
arxiv: 2307.13854
url: https://arxiv.org/abs/2307.13854
venue: ICLR 2024
category: agent-evaluation-benchmarks
---
# WebArena: A Realistic Web Environment for Building Autonomous Agents

## One line
Self-hosted websites (shopping, CMS, Reddit-like forum, GitLab, maps) with 812 tasks graded by functional checks on final state or answer.

## Method
Rule-based verifiers: exact/fuzzy string match on answers, programmatic checks of DB/page state. Only the outcome is checked.

## Evaluated on
GPT-4 agent 14.41% vs human 78.24% at release.

## Limitations admitted by the authors


## Limitations found by others
- Rule-based checks under-report success: 83.8% precision but only 55.9% recall vs expert labels (AgentRewardBench, 2504.08942).
- Zhu et al. (2507.02825) report outcome-validity issues in WebArena under the ABC checklist (string matching accepting/rejecting wrong answers).

## What it leaves untried

