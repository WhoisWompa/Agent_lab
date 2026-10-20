---
title: UTBoost: Rigorous Evaluation of Coding Agents on SWE-Bench
authors: Boxi Yu, Yuxuan Zhu, Pinjia He, Daniel Kang
date: 2025-06
arxiv: 2506.09289
url: https://arxiv.org/abs/2506.09289
venue: ACL 2025
category: agent-evaluation-benchmarks
---
# UTBoost: Rigorous Evaluation of Coding Agents on SWE-Bench

## One line
LLM-driven test-case augmentation finds SWE-bench tasks whose tests let wrong patches pass and re-ranks the leaderboards.

## Method
LLM generates extra unit tests from the codebase and gold patch; patches that pass original but fail augmented tests are flagged and checked.

## Evaluated on
36 instances with insufficient tests; 345 erroneous patches marked passing; 40.9% of Lite and 24.4% of Verified leaderboard entries affected; 18 / 11 ranking changes.

## Limitations admitted by the authors


## Limitations found by others


## What it leaves untried

