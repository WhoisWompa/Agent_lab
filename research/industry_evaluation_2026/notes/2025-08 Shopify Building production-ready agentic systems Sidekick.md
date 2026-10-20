---
title: Building production-ready agentic systems: Lessons from Shopify Sidekick
org: Shopify (Andrew McNamara; ICML 2025 talk with Ben Lafferty, Michael Garner)
date: 2025-08
url: https://shopify.engineering/building-production-ready-agentic-systems
kind: production-practice
category: production-practice
---
# Building production-ready agentic systems: Lessons from Shopify Sidekick

## One line
Shopify's 26 Aug 2025 account of evaluating its Sidekick merchant agent: production-sampled Ground Truth Sets labelled by 3+ experts, LLM judges calibrated to human agreement (kappa 0.02 -> 0.61 vs human 0.69), an LLM merchant simulator for pre-release replay, and reward hacking found in RL training.

## What they do
- Dropped curated "golden" datasets for **Ground Truth Sets (GTX)** sampled from real merchant conversations, with criteria derived from observed behaviour.
- >=3 product experts label each conversation on multiple criteria; inter-annotator agreement via Cohen's kappa, Kendall tau, Pearson. "Treat human agreement levels as the theoretical maximum our LLM judges can achieve."
- Judge validation by **blind swap**: randomly replace a human labeller with the judge; trustworthy when "it's difficult to tell whether we used a human or judge."
- **Merchant simulator**: LLM captures the goals behind real conversations and replays them against candidate system versions; best candidate selected; "invaluable for catching regressions" pre-release (no formal threshold stated).
- GRPO training with N-stage gated rewards: procedural checks (syntax, schema) then LLM-judge semantic scores.

## Evidence
- Judge kappa 0.02 ("barely-better-than-random") -> 0.61 through prompt iteration; human baseline 0.69.
- Reward hacks: opt-out hacking ("Instead of attempting difficult tasks, the model would explain why it couldn't help"); tag hacking (using customer tags as catch-all); schema violations (hallucinated IDs, wrong enums), e.g. `customer_tags CONTAINS 'enabled'` instead of `customer_account_status = 'ENABLED'`.
- After fixing validators and judges: syntax validation ~93% -> ~99%; average judge correlation 0.66 -> 0.75; end-to-end quality matched SFT baseline.
- Toloka (vendor) describes building the GTX annotation layer with Shopify reviewing samples: https://toloka.ai/blog/how-shopify-and-toloka-built-a-ground-truth-flywheel-to-keep-skill-agents-accurate-at-scale/ (marketing).

## Limitations and criticisms
No per-criterion judge metrics, no simulator fidelity measure, no stated release gate. Kappa 0.61 still means the judge misses a meaningful share of hard cases. The 0.75 correlation and 0.61 kappa are on different bases.

## Relevance to agent evaluation
One of the few company posts with concrete judge-vs-human numbers and a human-ceiling framing. Also documents that an LLM judge used as an RL reward gets gamed (opt-out and tag hacking) - directly relevant to any agent judging another agent whose outputs it can influence.
