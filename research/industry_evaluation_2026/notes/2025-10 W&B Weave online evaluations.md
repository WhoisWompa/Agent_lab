---
title: W&B Weave (CoreWeave) online evaluations and monitors
org: Weights & Biases / CoreWeave
date: 2025-10
url: https://site.wandb.ai/online-evaluations
kind: tooling-product
category: eval-tooling
---
# W&B Weave (CoreWeave) online evaluations and monitors

## One line
Weave is W&B's LLM tracing/eval product (Apache-2.0 SDK, 1.1k stars), now under CoreWeave after the May 2025 acquisition, with offline scorers and online monitors sampling production traces.

## What they do
- Online evaluations: sample live traces, score with built-in or custom LLM judges, monitor over time (https://wandb.ai/wandb_fc/product-announcements-fc/reports/Ship-AI-with-confidence-Introducing-W-B-Weave-Online-Evaluations--VmlldzoxMzI2ODEzNg).
- CoreWeave closed W&B acquisition 5 May 2025 (https://investors.coreweave.com/news/news-details/2025/CoreWeave-Completes-Acquisition-of-Weights--Biases/default.aspx); Weave pricing now on CoreWeave Forge page.
- Accepts OTLP; trajectory "partial" (Arize comparison).

## Evidence
- aicoolies review 82/100 (https://aicoolies.com/reviews/wandb-weave-review) — low-quality review site.

## Limitations and criticisms
- Latitude (competitor) argues W&B's training-experiment paradigm fits production LLM reliability poorly (https://latitude.so/blog/best-wb-alternatives-ai-evaluation). Self-managed requires licensed W&B.

## Relevance to agent evaluation
- Standard online-judge monitoring; little agent-specific beyond trace scorers.

