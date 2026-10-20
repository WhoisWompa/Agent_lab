---
title: CAISI Evaluation of DeepSeek V4 Pro
org: NIST Center for AI Standards and Innovation (CAISI)
date: 2026-05
url: https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro
kind: third-party-evaluator
category: frontier-labs
---
# CAISI Evaluation of DeepSeek V4 Pro

## One line
US CAISI's 1 May 2026 evaluation of DeepSeek V4 Pro, using 9 benchmarks in 5 domains incl. two held-out ones and an IRT-based aggregate, concluding V4 is the most capable PRC model it has tested and about 8 months behind the US frontier.

## What they do
- Domains/benchmarks: cyber (CTF-Archive-Diamond), software engineering (SWE-Bench Verified, PortBench - CAISI-built, non-public, porting CLI tools across languages), natural sciences (FrontierScience, GPQA-Diamond), abstract reasoning (ARC-AGI-2 semi-private), maths (OTIS-AIME-2025, PUMaC 2024, SMT 2025).
- 1PL Item Response Theory over models x tasks to estimate an Elo-like capability; equal weight per benchmark within domain and per domain; controlled token budgets and agent scaffolding; benchmark suite pre-committed.
- Cost comparison against GPT-5.4 mini.

## Evidence
- IRT Elo: DeepSeek V4 Pro 800 +/- 28 vs GPT-5.5 1260 +/- 28 (per NIST page as fetched; one secondary source quoted 999 +/- 27, so figures conflict - https://letsdatascience.com/news/caisi-evaluates-deepseek-v4-pro-against-frontier-models-c7b2e918).
- DeepSeek's own report puts V4 near Opus 4.6 / GPT-5.4; CAISI's (with non-public benchmarks) puts it near GPT-5.
- Cheaper than GPT-5.4 mini on 5 of 7 benchmarks.

## Limitations and criticisms
- Critics (Decrypt) call the private benchmarks and the cost filter that excluded all US models but GPT-5.4 mini "convenient" (https://decrypt.co/366685/us-says-china-best-ai-models-lag-behind-experts-not-sure?amp=1); fuller IRT write-up promised.
- Not a pre-deployment test; post-release on open weights.

## Relevance to agent evaluation
Government evaluator using held-out agentic SWE tasks and IRT aggregation to correct for self-reported lab numbers; evidence that self-reported vs independent gaps are large for agentic tasks.
