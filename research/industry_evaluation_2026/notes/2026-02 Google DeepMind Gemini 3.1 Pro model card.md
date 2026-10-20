---
title: Gemini 3.1 Pro Model Card
org: Google DeepMind
date: 2026-02
url: https://deepmind.google/models/model-cards/gemini-3-1-pro/
kind: lab-practice
category: frontier-labs
---
# Gemini 3.1 Pro Model Card

## One line
Google DeepMind's 19 Feb 2026 model card for Gemini 3.1 Pro: a benchmark table across reasoning, agentic tool use, coding, multimodal and long context, automated content-safety deltas plus internal red teaming, and Frontier Safety Framework (FSF) results across five risk domains.

## What they do
- Benchmarks: HLE 44.4% (51.4% with search+code), ARC-AGI-2 77.1% (ARC Prize Verified), GPQA Diamond 94.3%, Terminal-Bench 2.0 68.5%, SWE-Bench Verified 80.6%, SWE-Bench Pro 54.2%, LiveCodeBench Pro 2887 Elo, BrowseComp 85.9%, tau2-bench (Retail 90.8, Telecom 99.3), MCP Atlas 69.2%, MMMU-Pro 80.5%, MMMLU 92.6%, MRCR v2 84.9% @128k / 26.3% @1M; GDPval-AA Elo also reported.
- Methodology details are on a separate evals-methodology page (see the Gemini 3 Flash methodology note for the format).
- Content safety: automated evals (text, multilingual, image-to-text, tone, unjustified refusals) as deltas against the previous model; human red teaming by specialist teams "who sit outside of the model development team".
- FSF: CBRN (Uplift Level 1 CCL not reached), Cyber (alert threshold reached, as for Gemini 3 Pro; CCL not reached; tested with and without Deep Think), Harmful manipulation (Level 1 not reached; max odds ratio 3.6x), ML R&D (acceleration/automation Level 1 not reached though one RE-Bench task doubled the human baseline), Misalignment exploratory (instrumental reasoning Levels 1-2 not reached; stealth flat; situational awareness stronger but inconsistent).

## Evidence
- Card states safety results "are for automated evaluations and not human evaluation or red teaming"; manual review found flagged losses mostly false positives or not egregious.
- Evaluation methods refined, so results are "not directly comparable" with earlier cards.

## Limitations and criticisms
- No explicit external/third-party safety testing named in the card (third-party only for the ARC Prize-verified number). Commentators criticised the Gemini 3 FSF report for thin detail and absent third-party reports (https://thezvi.substack.com/p/gemini-3-model-card-and-safety-framework).
- Competitor numbers are a mix of self-reported and leaderboard values.
- A third-party analysis notes only the standard Terminus-2 harness score was published for Terminal-Bench (https://smartscope.blog/en/generative-ai/google-gemini/gemini-3-1-pro-benchmark-analysis-2026/).

## Relevance to agent evaluation
Google's FSF includes situational-awareness and stealth evaluations (an eval-awareness proxy) and agentic benchmarks graded by execution (Terminal-Bench, SWE-Bench) or simulated users (tau2). Little is disclosed about LLM judges.
