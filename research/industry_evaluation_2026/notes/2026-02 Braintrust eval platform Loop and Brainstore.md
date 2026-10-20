---
title: Braintrust: eval-first platform with Loop agent and Brainstore
org: Braintrust
date: 2026-02
url: https://www.braintrust.dev/docs/loop/index
kind: tooling-product
category: eval-tooling
---
# Braintrust: eval-first platform with Loop agent and Brainstore

## One line
Braintrust is the eval-first commercial platform (experiments, scorers, CI, online scoring) that raised $80M at an $800M valuation in Feb 2026 and ships Loop, an agent that writes and edits prompts, datasets and scorers.

## What they do
- Series B: $80M led by ICONIQ at $800M valuation, Feb 2026 (https://finder.techleap.nl/news/feed/braintrust-raises-80m-to-monitor-ai-models-and-agents-in-production, citing SiliconANGLE).
- Scorers: autoevals library (1,063 stars, MIT), LLM-as-judge, custom code; span scorers and trace scorers (trace scorers get the whole trace). Same scorers run on production via online scoring (https://braintrust.dev/articles/best-hallucination-detection-tools-2026).
- Loop: agent that "can create and update prompts, scorers, facets, preprocessors, datasets, views, and automations, but has no tool to delete them"; docs warn auto-accept can make production changes such as creating an online scoring rule (https://www.braintrust.dev/docs/loop/index).
- Brainstore: trace database (inverted index + columnar on object storage); vendor claims ~80% faster trace queries (unverified).
- Pricing (checked 27 Aug 2026 by beri.net): Pro $249/mo incl. 50k scores, $1.50 per 1k scores over; Starter 10k incl. then $2.50/1k; hybrid/self-host Enterprise-only (https://www.beri.net/article/braintrust-vs-langfuse-vs-promptfoo-llm-eval-regression-gate-2026). Another source lists Pro at $450/mo (conflict).

## Evidence
- beri.net estimate for 600k scores/month: Braintrust Pro ≈ $1,074 vs Langfuse Cloud Core ≈ $115, Opik Cloud ≈ $44, Promptfoo $0.
- CI: eval-action posts a PR summary comment rather than blocking; terminate_on_failure stops on errors not regressions; blocking needs a custom Reporter (beri.net).

## Limitations and criticisms
- "Braintrust meters the thing it wants you to do more of": a 4th scorer raises the bill ~28% (beri.net). Prompts/outputs go to Braintrust cloud on Starter/Pro.
- No built-in measure of judge agreement with human reviewers (beri.net says this of all four tools compared).

## Relevance to agent evaluation
- Loop is an agent that authors scorers — i.e., an agent building the judge. Trace-level scorers are the hook for agent trajectory judging.

