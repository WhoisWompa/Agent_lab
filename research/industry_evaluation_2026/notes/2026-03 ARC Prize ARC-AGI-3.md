---
title: ARC-AGI-3 and ARC Prize 2026 (with ARC-AGI-2 status)
org: ARC Prize Foundation
date: 2026-03
url: https://arcprize.org/competitions/2026/arc-agi-3
kind: benchmark
category: third-party-and-benchmarks
---
# ARC-AGI-3 and ARC Prize 2026

## One line
ARC-AGI-3 launched on 25 Mar 2026 as an interactive, game-like benchmark for agentic skill acquisition. Humans solve 100% of its environments, and frontier LLMs scored under 0.4% at launch. ARC-AGI-2 is now close to saturated by frontier models.

## What they do
- **ARC-AGI-3**: interactive environments in which an agent must explore, infer the goal and the rules, and act. It is scored on efficiency of skill acquisition relative to humans ([arXiv 2603.24621](https://arxiv.org/pdf/2603.24621)).
- **ARC Prize 2026**: a Kaggle competition under compute limits ([Kaggle leaderboard](https://www.kaggle.com/competitions/arc-prize-2026-arc-agi-3/leaderboard)).
  - Milestone prizes on 30 Jun and 30 Sep 2026: $25K for 1st, $10K for 2nd, $2.5K for 3rd.
  - Results are announced on 4 Dec (secondary source).
- **Verified testing of frontier models**: ARC Prize runs frontier models itself on a semi-private set, using a standard harness or a provider adapter harness, and publishes cost per task.

## Evidence
- **Launch**: the best frontier LLMs scored under 0.4% in the 30-day developer preview. The best purpose-built preview agent scored 12.58% ([Medium summary](https://medium.com/@AdithyaGiridharan/arc-agi-3-dropped-and-frontier-ai-scored-less-than-1-90cd70e65a61), secondary).
- **Competition progress**, from ARC Prize posts on X:
  - Tufa Labs scored 11.04% early.
  - Yi-Chia Chen reached 28.34% around 28 Sep ([X](https://x.com/arcprize/status/2104590501915787290)).
  - Tufa Labs reached 68.91% around 13 Oct, up from 56% ([X](https://x.com/arcprize/status/2110031207601979715)).
  - The Kaggle leaderboard shows Tufa 68.91, Yi-Chia Chen 67.49 and Team Turducken 52.82.
- **Verified frontier results on ARC-AGI-3** (mid-October 2026, via search summary, not confirmed on an official results page):
  - Gemini 4 Argon: 97.5% with the provider adapter harness, 49.8% with the standard harness.
  - Haiku 5.5: 2.8% and 0.5%.
  - DeepSeek V4.1 Flash: 3.3% and 0.9%.
- **ARC-AGI-2**:
  - GPT-6 Astra: 95.0% at maximum reasoning, on ARC Prize's verified page dated 2 Sep 2026 (search summary).
  - GPT-5.6 Sol: 92.5% at $1.44 per task; Claude Opus 5: 90.4% ([capitalandcompute](https://capitalandcompute.net/ai-benchmarks/arc-agi-2/), secondary).
  - Thinking Machines' Inkling Small: 40.1% at $0.23 per task ([ARC Prize result page](https://arcprize.org/results/thinky-inkling-small)).

## Limitations and criticisms
- Scores depend heavily on the harness: the provider adapter and the standard harness differ by about 48 points for Gemini 4 Argon. The sources do not explain the adapter.
- Within 18 months of launch, ARC-AGI-2 went from hard to over 90% for frontier models.

## Relevance to agent evaluation
- ARC-AGI-3 is one of the few benchmarks that is natively agentic and interactive, with a human baseline built in and cost per task reported.
- The gap between harnesses shows that, for agents, the scaffold is part of what gets measured. Leaderboards must state the harness.
