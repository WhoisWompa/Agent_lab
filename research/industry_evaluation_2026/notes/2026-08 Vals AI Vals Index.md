---
title: Vals Index and Vals AI domain benchmarks
org: Vals AI
date: 2026-08
url: https://www.vals.ai/benchmarks/vals_index
kind: third-party-evaluator
category: third-party-and-benchmarks
---
# Vals AI: Vals Index and industry benchmarks

## One line
An independent evaluator focused on enterprise domains (finance, law, tax, coding). Its composite index is weighted by GDP, and its benchmarks are partly private.

## What they do
- **Original Vals Index**: GDP-weighted. Weights:
  - Finance: 2.0 (CorpFin plus Finance Agent)
  - Coding: 1.4
  - Law: 0.3 (CaseLaw)
  - The sum is divided by 3.7.
- **Index v2.1** (secondary source): BEA-weighted, (8.0 Finance + 5.6 Coding + 1.2 Legal + 0.5 Tax) / 15.3. Finance here is Finance Agent v2 plus an Excel Modeling Benchmark ([capitalandcompute](https://capitalandcompute.net/ai-benchmarks/vals-index/)).
- Vals also hosts LiveCodeBench runs, among others.

## Evidence
- **v1.2 leaderboard** (11 Aug 2026) ([vals.ai v1.2](https://www.vals.ai/benchmarks/vals_index_v1_2)):
  - Claude Fable 5: 75.14%
  - Claude Opus 5: 74.82%
  - Kimi K3: 74.70%
- **v2.1**: top score 68.90% for Gemini 4 Argon (secondary).
- **Funding**: Vals reportedly raised a $40M Series A led by a16z ([KuCoin blog](https://www.kucoin.com/blog/vals-ai-40m-series-a-real-world-benchmarks)). This is a secondary source, and the date was not confirmed.
- **CorpFin replacement**: the same source says CorpFin was replaced in May 2026 by a harder Excel modelling benchmark. BenchLM still shows CorpFin v2 ([BenchLM](https://benchlm.ai/benchmarks/valscorpfinv2)). The two sources conflict.

## Limitations and criticisms
- Index versions change and are not comparable with each other.
- Private test sets cannot be audited.
- The current version could not be confirmed on vals.ai.

## Relevance to agent evaluation
Vals is the main independent source of finance and legal agent evaluations, such as Finance Agent. Weighting by GDP is one answer to the question "important to whom?" when building composite scores.
