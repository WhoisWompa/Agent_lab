---
title: Comet Opik: open-source tracing, evals and agent optimizer
org: Comet
date: 2026-10
url: https://www.comet.com/docs/opik/agent_optimization/opik_optimizer/concepts
kind: tooling-product
category: eval-tooling
---
# Comet Opik: open-source tracing, evals and agent optimizer

## One line
Opik is Comet's Apache-2.0 tracing/eval platform (22.8k stars) distinguished by an Agent Optimizer SDK (evolutionary, few-shot, meta-prompt, GEPA strategies) and low cloud pricing.

## What they do
- Optimizer: all optimizers implement optimize_prompt(); tunes prompts, tools, agent workflows using logged datasets/metrics/traces.
- Metrics include "Agent task completion" and "Agent tool correctness"; online evaluation; Opik Guardrails.
- Pricing (beri.net Aug 2026): Pro $19/mo incl. 100k spans, $5/100k after; retention >60 days $29/100k; free cloud tier capped at 10 members. Estimated ≈$44/mo for the 600k-score workload.
- GitHub: comet-ml/opik 22,756 stars, Apache-2.0 (GitHub API).

## Evidence
- Feature info from Comet docs; trajectory support "partial" per Arize comparison.

## Limitations and criticisms
- Long retention expensive; pytest integration requires you to write thresholds.

## Relevance to agent evaluation
- Joins the 2026 trend of optimisers closing the loop from judge scores to prompt changes — which magnifies any judge bias (Goodhart).

