---
title: Introducing SWE-bench Verified
authors: OpenAI Preparedness (Neil Chowdhury et al.)
date: 2024-08
arxiv: none
url: https://openai.com/index/introducing-swe-bench-verified/
venue: OpenAI blog
category: agent-evaluation-benchmarks
topics: ["agent evaluation benchmarks"]
---
# Introducing SWE-bench Verified

## One line
Human-screened 500-task subset of SWE-bench meant to remove underspecified issues and unfair tests.

## Method
Professional developers annotated sampled SWE-bench tasks for issue clarity and test validity; tasks flagged as underspecified or with unfair tests were dropped. Grading stays test-based.

## Evaluated on


## Limitations admitted by the authors
- Screening was done once, by humans, on a fixed snapshot; contamination was not addressed.

## Limitations found by others
- OpenAI itself (2026-02-23, 'Why we no longer evaluate SWE-bench Verified') audited 138 hard tasks and found 59.4% with material problems in tests or descriptions (tests demanding unspecified names/details), plus evidence that GPT-5.2, Claude Opus 4.5 and Gemini 3 Flash reproduce original fixes from memory; stopped reporting it and recommended SWE-bench Pro.
- Zhu et al. (2507.02825) list Verified's insufficient test cases as an ABC violation.
- UTBoost (2506.09289): 24.4% of Verified leaderboard entries affected by insufficient tests, 11 ranking changes.
- PAIChecker (2607.28587, per secondary source): 13.6% of Verified instances show PR-issue misalignment.
- METR (2026-03-10): ~50% of passing PRs not mergeable, ~24 pp overstatement.

## What it leaves untried
- Continuous re-screening or freshness (time-split tasks) instead of a one-off filtered set.

## Topics
[[Topic - agent evaluation benchmarks]]
