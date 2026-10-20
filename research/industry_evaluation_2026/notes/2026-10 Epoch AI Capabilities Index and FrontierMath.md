---
title: Epoch Capabilities Index (ECI), Benchmarking Hub and FrontierMath
org: Epoch AI
date: 2026-10
url: https://epoch.ai/benchmarks
kind: third-party-evaluator
category: third-party-and-benchmarks
---
# Epoch Capabilities Index, Benchmarking Hub and FrontierMath

## One line
Epoch runs its own evaluations on about 90 tracked benchmarks. It combines them into one capability scale using item response theory (the ECI), and it owns FrontierMath, which needed a major correction in 2026.

## What they do
- **ECI**: models performance as sigmoid(slope × (capability − difficulty)). Benchmark difficulty is inferred from overlapping results rather than set by hand.
  - The general index uses more than 50 benchmarks scored from 0 to 1, so Elo-style arenas are excluded ([Epoch ECI methodology](https://epoch.ai/data/eci-documentation/methodology); [eci-public](https://github.com/epoch-research/eci-public)).
  - The underlying paper is "A Rosetta Stone for AI Benchmarks", funded by Google DeepMind.
- **Benchmarks Epoch runs itself**:
  - GPQA Diamond, MATH L5, Mock AIME, SWE-bench Verified;
  - FrontierMath and its Open Problems and Erdős sets;
  - MirrorCode (with METR) and others.
  - SWE-Lancer and SimpleQA are planned ([Epoch](https://epoch.ai/benchmarks)).

## Evidence
- **ECI, as of 1 Oct 2026**:
  - Claude Opus 5.5 at 167, narrowly ahead of GPT-6 Astra.
  - Claude Sonnet 5.5 is about level with Claude Fable 5.1 at 165.
- **FrontierMath Tiers 1-3**: GPT-5.4 Pro scored 50% in March 2026 ([Epoch Brief](https://epochai.substack.com/p/the-epoch-brief-march-2026)).
- **FrontierMath audit**:
  - An AI-assisted review found fatal errors in about 33% of problems, up from earlier estimates of 7-10% ([Crypto Briefing](https://cryptobriefing.com/frontiermath-benchmark-audit-errors/)).
  - The benchmark was reissued after fixing 42% of problems, and corrected scores are not comparable with the originals ([OWID](https://ourworldindata.org/grapher/ai-frontiermath-over-time)).
  - The two figures conflict.
- **FrontierMath Erdős**: 68 open problems. Only GPT-6 Astra solved any, 2 of 68 ([Epoch](https://epoch.ai/latest/announcing-frontiermath-erdos)).
- **Epoch's own caveats**:
  - Contamination, especially on MATH L5.
  - Sensitivity to prompts.
  - Its GPQA results for Claude 3.5 Sonnet were 0.55 ± 0.03, against Anthropic's reported 65%.
  - Runs are not yet pinned to git revisions.

## Limitations and criticisms
- The ECI inherits errors from its component benchmarks, many of which Epoch has itself labelled Flawed.
- FrontierMath was funded by OpenAI, which had access to much of the dataset. This was the 2025 controversy, not re-verified here.

## Relevance to agent evaluation
- IRT stitching lets agents be compared across benchmarks they never shared.
- Epoch's own benchmark needing a 33-42% correction shows that even careful benchmark makers need a separate audit layer.
