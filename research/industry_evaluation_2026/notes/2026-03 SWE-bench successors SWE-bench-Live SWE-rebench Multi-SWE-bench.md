---
title: SWE-bench successors - SWE-bench-Live, SWE-rebench, Multi-SWE-bench, SWE-Bench Pro Verified
org: Microsoft Research et al. (SWE-bench-Live); Nebius (SWE-rebench); ByteDance (Multi-SWE-bench); various
date: 2026-03
url: https://arxiv.org/html/2505.23419v2
kind: benchmark
category: third-party-and-benchmarks
---
# SWE-bench successors: live and refreshed coding-agent benchmarks

## One line
These benchmarks answer SWE-bench Verified's contamination problem in three ways: refreshing tasks continuously from GitHub activity after model cutoffs, extending to more languages, or repairing known-broken tasks.

## What they do
- **SWE-bench-Live** (Microsoft et al.): 1,319 tasks from GitHub issues created since 2024, across 93 repos, with a community leaderboard at swe-bench-live.github.io ([arXiv 2505.23419](https://arxiv.org/html/2505.23419v2)). It reports a substantial performance gap compared with static SWE-bench.
- **SWE-rebench** (Nebius): continuously collects issue-PR pairs created after training cutoffs, filters them for quality and reproducibility, and adds monthly splits. The current set has 860 Python tasks ([Harbor hub](https://hub.harborframework.com/datasets/swe-rebench/swe-rebench-leaderboard/latest?page=107)).
- **Multi-SWE-bench** (ByteDance): extends to multiple languages, with 1,632 tasks across 39 repos curated by hand. No 2026 results were found.
- **SWE-Bench Pro Verified**: an arXiv paper (2609.08149) that repairs broken SWE-Bench Pro instances based on external audits ([arXiv](https://arxiv.org/pdf/2609.08149)).
- **PAIChecker** (arXiv 2607.28587): a tool for detecting PRs that do not match their issue in SWE-bench-like benchmarks ([arXiv](https://arxiv.org/pdf/2607.28587)).

## Evidence
- **SWE-rebench, March 2026**: Claude Opus 4.6 led at 65.3%, ahead of GLM-5 and Gemini 3.1 Pro ([BenchLM](https://benchlm.ai/benchmarks/sweRebench), secondary).
- **SWE-rebench, March-May 2026 release**: a later report says GPT-5.5 leads at 88.7% ([AI Weekly](https://aiweekly.co/alerts/swe-rebench-puts-gpt-55-first-on-clean-coding-leaderboard)). This is unverified, and the report's description of the data source conflicts with the official one.

## Limitations and criticisms
- Live sets are smaller, mostly Python, and still verified by unit tests, so METR's mergeability gap still applies.
- Monthly splits make comparisons across time noisy.

## Relevance to agent evaluation
Refreshed task sets are the main defence against contamination for coding agents. Verifier quality is still the weak point, and that is where a review layer by an agent judge would help.
