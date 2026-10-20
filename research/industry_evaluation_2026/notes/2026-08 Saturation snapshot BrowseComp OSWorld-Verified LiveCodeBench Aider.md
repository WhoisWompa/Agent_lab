---
title: Saturation snapshot - BrowseComp, OSWorld-Verified, LiveCodeBench, Aider polyglot, LiveBench, HumanEval
org: Various (OpenAI BrowseComp; XLANG OSWorld; LiveCodeBench team; Aider; LiveBench)
date: 2026-08
url: https://benchlm.ai/benchmarks/browse-comp
kind: benchmark
category: third-party-and-benchmarks
---
# Saturation snapshot: BrowseComp, OSWorld-Verified, LiveCodeBench, Aider polyglot, LiveBench

## One line
By mid-2026 most of the agent and coding benchmarks of 2024-25 were bunched at the top. Third-party aggregators show leaders within about 2-6 points of each other.

## What they do
- **BrowseComp** (OpenAI, 2025): hard-to-find facts that require persistent web browsing; the answer is short and verifiable.
- **OSWorld-Verified**: computer-use tasks (see the Epoch OSWorld note).
- **LiveCodeBench**: competitive-programming problems collected continuously after model cutoffs. LiveCodeBench Pro uses Codeforces and ICPC problems ([alphaXiv](https://www.alphaxiv.org/benchmarks/university-of-washington/livecodebench-pro)).
- **Aider polyglot**: code edits in several languages, scored with the diff-edit format.
- **LiveBench**: a general benchmark refreshed monthly.

## Evidence
All figures below are from secondary aggregators and are unverified.
- **BrowseComp**, 22 Aug 2026 ([BenchLM](https://benchlm.ai/benchmarks/browse-comp)): GPT-5.6 Sol 92.2%, Kimi K3 91.2%, Claude Opus 5 90.8%. A July snapshot had the top models within 2.1 points.
- **OSWorld-Verified** ([benchmarklist](https://benchmarklist.com/benchmarks/osworld_verified/)): Claude Mythos Preview leads at 85.4%, and the top 8 are within 6 points.
- **LiveCodeBench**:
  - 20 Aug 2026 ([BenchLM](https://benchlm.ai/benchmarks/liveCodeBench)): DeepSeek-V4-Pro-Max 93.5%, with the top models within about 1.9 points.
  - Vals, April 2026: Gemini 3.1 Pro Preview 88.49%. Models are near-perfect on the easy split ([Vals](https://www.vals.ai/benchmarks/lcb-08-07-2025)).
  - Artificial Analysis dropped LiveCodeBench from its index in v4.0.
- **Aider polyglot**: Claude Opus 4.5 at 89.4% around April 2026 ([Codesota](https://codesota.com/code-generation)). Epoch lists Aider polyglot as an externally run benchmark ([Epoch](https://epoch.ai/benchmarks)). No 2026 frontier results were found.
- **HumanEval**: 96-98%, useless for comparing models.
- **LiveBench**: no 2026 data found.
- **WebVoyager**: browser agents reached 97.1% ([agentmarketcap](https://agentmarketcap.ai/blog/2026/04/13/browser-agent-benchmark-saturation-webvoyager-97-percent-2026)).

## Limitations and criticisms
The aggregators conflict on details and evaluation conditions differ between them. No BrowseComp-Plus data was found.

## Relevance to agent evaluation
These benchmarks still appear in model cards, but they no longer separate frontier agents from one another. Differentiation has moved to long-horizon, economic and interactive evaluations (time horizon, Vending-Bench, ARC-AGI-3, GDPval, AA-Briefcase).
