---
title: Model Evaluation - Approach, Methodology & Results: Gemini 3 Flash
org: Google DeepMind
date: 2025-12
url: https://storage.googleapis.com/deepmind-media/gemini/gemini_3_flash_model_evaluation.pdf
kind: lab-practice
category: frontier-labs
---
# Model Evaluation - Approach, Methodology & Results: Gemini 3 Flash

## One line
The 'evals methodology' companion to the Gemini 3 Flash model card (Dec 2025; linked from deepmind.google/models/evals-methodology/gemini-3-flash), listing per-benchmark sourcing, harness and grading conventions.

## What they do
- All Gemini scores pass@1 via the Gemini API, default sampling; "single attempt" = no majority voting or parallel test-time compute; smaller benchmarks averaged over multiple trials.
- Non-Gemini numbers are providers' self-reported unless noted; missing ones computed by GDM via provider APIs or taken from third parties (Vals.ai, Artificial Analysis for Grok 4.1 Fast).
- HLE from Scale AI leaderboard or self-reported; ARC-AGI from ARC Prize semi-private set.
- Terminal-Bench 2.0 from public leaderboard with default Terminus-2 harness.
- SWE-bench Verified: providers use different scaffolds; GDM's is single-attempt with a bash tool, file-edit tools and a submit tool, averaged over 5 runs.
- tau2-bench: Sierra framework with prompt adjustment; the simulated user is Gemini 3 Pro with a custom system instruction; adopts Anthropic's Airline-domain fixes from the Claude Opus 4.5 report.
- Toolathlon from benchmark authors / leaderboard; MCP Atlas from Scale AI leaderboard; Vending-Bench 2 from Andon Labs; FACTS Benchmark Suite and SimpleQA Verified from Kaggle leaderboards; MRCR v2 (internal, not public) at 128k cumulative and 1M pointwise.

## Evidence
- The document is explicit that comparison numbers mix scaffolds and sources (e.g. GPT-5.2 ScreenSpot-Pro uses python, "should not be directly comparable").

## Limitations and criticisms
- Cross-lab tables are not apples-to-apples: different scaffolds, reasoning settings, and self-reported vs leaderboard sources.
- Simulated-user model is the lab's own model (Gemini 3 Pro), a potential bias source on tau2.

## Relevance to agent evaluation
Shows the practical reality of reported agent evals: harness choice (Terminus-2, custom SWE scaffold), user simulators and leaderboard-sourced numbers are part of the measurement; labs fix each other's benchmark bugs (Airline domain).
