---
title: Gemini 3.5 Flash Model Card
org: Google DeepMind
date: 2026-05
url: https://deepmind.google/models/model-cards/gemini-3-5-flash/
kind: lab-practice
category: frontier-labs
---
# Gemini 3.5 Flash Model Card

## One line
Google DeepMind's 19 May 2026 card for Gemini 3.5 Flash, whose benchmark table is now almost entirely agentic and professional-work evals; frontier safety is inferred from Gemini 3.1 Pro testing plus extra cyber testing.

## What they do
- Benchmarks: Terminal-bench 2.1 (Terminus-2) 76.2%, SWE-Bench Pro (Public, single attempt) 55.1%, MCP Atlas 83.6%, Toolathlon 56.5%, OSWorld-Verified 78.4%, Finance Agent v2 57.9%, GDPval-AA 1656 Elo, CharXiv Reasoning 84.2%, MMMU-Pro 83.6%, Blueprint-Bench 2 33.6%, MRCR v2 77.3% @128k / 26.6% @1M, HLE 40.2%, ARC-AGI-2 72.1%. Compared against 3 Flash, 3.1 Pro, Sonnet 4.6, Opus 4.7, GPT-5.5.
- No SWE-bench Verified, GPQA or LiveCodeBench rows (contrast with the 3.1 Pro card three months earlier).
- Safety: automated evals as deltas vs 3 Flash; human red teaming by specialist teams outside the development team; child-safety launch thresholds.
- Frontier safety: evaluated Gemini 3.1 Pro (most capable model), no CCLs; extra cyber testing found 3.5 Flash below the cyber CCL.

## Evidence
- "The evaluation results are for automated evaluations and not human evaluation or red teaming."
- Results "computed with improved evaluations and thus are not directly comparable" with earlier cards (same wording in the 3.7/3.8 Flash cards: https://deepmind.google/models/model-cards/gemini-3-7-flash/).

## Limitations and criticisms
- No external testers named. Frontier safety claim relies on a different model's results.
- No Gemini 3.5 Pro card was found in the DeepMind model-card index at time of research (https://deepmind.google/models/model-cards/).

## Relevance to agent evaluation
Clear marker of the 2026 benchmark turnover: a flagship-family card whose capability section is mostly agent benchmarks (terminal, MCP, computer use, finance agent, GDPval-AA) graded by execution or by third-party rubric/pairwise harnesses.
