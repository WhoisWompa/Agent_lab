---
title: Product Evals in Three Simple Steps
org: Eugene Yan
date: 2025-11
url: https://eugeneyan.com/writing/product-evals/
kind: essay
category: production-practice
---
# Product Evals in Three Simple Steps

## One line
Eugene Yan's Nov 2025 recipe: label a small binary dataset, align one LLM evaluator per dimension to it, and run the harness on every config change, with explicit sample-size arithmetic.

## What they do
- Binary labels (pass/fail for objective; win/lose/tie for subjective). Target "at least 50-100 failures out of 200+ total samples"; prefer organic failures (from production or smaller models) over synthetic defects, which are out of distribution; active learning to surface likely failures.
- Split ~75% dev / 25% test. One evaluator per dimension: of a single "God Evaluator", "I've never seen this work well."
- Pairwise: run both orders, inconsistent verdicts become ties.
- Measure precision, recall (prioritise recall on fail) and Cohen's kappa.
- Harness runs evaluators in parallel and outputs a one-row metrics table.

## Evidence
- Kappa 0.4-0.6 "substantial", >0.7 "excellent"; human-human kappa often only 0.2-0.3 and humans can miss up to 50% of defects.
- Sample-size example: 200 samples with 3% defects vs a 5% bar gives 95% CI ~0.6-5.4% (inconclusive); 400 samples narrows upper bound to ~4.7%; halving margin needs 4x samples.
- Anecdote: a team spent ~4 weeks building evals, then ran dozens of experiments in two weeks.

## Limitations and criticisms
Individual practitioner's guidance; the kappa thresholds are conventions, not validated cutoffs. Human-agreement numbers are general claims, not from a specific study in the post. Single-turn product framing; little on agents.

## Relevance to agent evaluation
Supplies the statistics many teams skip (CIs on pass rates, how many samples to detect a defect-rate difference) and a realistic human ceiling (kappa 0.2-0.3), which matters when deciding whether a judge agent is "good enough".
