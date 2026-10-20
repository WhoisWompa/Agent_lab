---
title: Replacing Judges with Juries: Evaluating LLM Generations with a Panel of Diverse Models
authors: Pat Verga et al.
date: 2024-04
arxiv: 2404.18796
url: https://arxiv.org/abs/2404.18796
venue: arXiv (Cohere)
category: alternative-paradigms
---
# Replacing Judges with Juries: Evaluating LLM Generations with a Panel of Diverse Models

## One line
Panel of LLM evaluators (PoLL) from disjoint model families, aggregated by voting, beats a single large judge and is over seven times cheaper.

## Method
Three smaller judges from different families (as recalled: Command R, Claude 3 Haiku, GPT-3.5) score independently; max/average voting. No deliberation, no tools. Sees outputs only.

## Evaluated on
Three judge settings and six datasets (single-hop QA, multi-hop QA, Chatbot Arena-style pairwise). Higher correlation with human judgements than GPT-4 alone, less intra-model bias, over 7x cheaper (from abstract).
- (llm-judge-foundations) Cohen's kappa vs humans, GPT-4 vs PoLL: NQ 0.627 vs 0.763, TriviaQA 0.841 vs 0.906, HotpotQA 0.830 vs 0.867. Arena Hard rank correlation: Pearson 0.817 vs 0.917, Kendall 0.667 vs 0.778. Cost $1.25/$4.25 per M tokens vs $10/$30 for GPT-4 Turbo (7-8x cheaper). Each judge scores its own family highest; panel has smallest spread vs humans (sd 2.2 vs 6.1 for GPT-3.5).

## Limitations admitted by the authors
- Tasks are mostly QA with references and Arena-style pairs; not tested on long-form or agentic outputs.
- Panel composition chosen by hand.
- Only three settings and one panel composition; math and reasoning not studied.
- Panel selection left open.
- GPT-4's kappa varied 0.518-0.725 on NQ with prompt wording, so the baseline is prompt-sensitive.

## Limitations found by others
- Goel et al. 2025 (arXiv 2502.04313): correlated errors across models grow with capability, which limits the independence a panel relies on.
- Chen et al. 2025 'Safer or Luckier' (2503.09347): juries improve robustness and human alignment for safety judging but artifact sensitivity (apologetic phrasing skews up to 98%) persists even with the best jury.
- Tan et al. 2024 JudgeBench (2410.12784): ChatEval-style multi-agent debate scores 34.0%, worse than single GPT-4o, on objective hard pairs; panels help on reference-backed QA but not when no member can solve the problem.

## What it leaves untried
- A panel of agentic judges; panels with selective abstention when members disagree.
- Panels on hard objective tasks without references; correlated errors when all members share a training-data blind spot.

