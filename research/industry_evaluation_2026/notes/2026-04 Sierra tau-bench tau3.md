---
title: τ-bench / τ²-bench / τ³-bench (Sierra)
org: Sierra Research
date: 2026-04
url: https://github.com/sierra-research/tau2-bench
kind: benchmark
category: eval-tooling
---
# τ-bench / τ²-bench / τ³-bench (Sierra)

## One line
Sierra's τ-bench family evaluates tool-using agents against an LLM-simulated user and checks final database state; the repo now hosts τ³-bench (375 tasks across airline, retail, telecom, banking-knowledge, with full-duplex voice).

## What they do
Simulated user (LLM) converses with agent under domain policy; success = final DB state matches goal; pass^k reliability metric; τ² added dual-control (user also acts); τ³ adds banking RAG domain, full-duplex voice eval, 75+ task-quality fixes (secondary: https://benchmarkingagents.com/tau3-bench ; Harbor listing published 25 Apr 2026: https://hub.harborframework.com/datasets/sierra-research/tau3-bench/latest).

## Evidence
GitHub 2,264 stars, MIT, active (GitHub API 2026-10-20). BenchLM tracks provider-reported τ³ scores (not controlled) (https://benchlm.ai/benchmarks/tau3-bench).

## Limitations and criticisms
Voice details not verified from official source; user simulator itself is an LLM whose errors confound scores.

## Relevance to agent evaluation
The reference design for simulated-user agent evaluation with outcome (state) grading rather than LLM judging.

