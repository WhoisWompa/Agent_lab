---
title: All Verdicts are Not Equal: Rethinking LLM Judge Reliability
authors: Vineet Kumar et al.
date: 2026-10
arxiv: 2610.12083
url: https://arxiv.org/abs/2610.12083
venue: AACL-IJCNLP 2026
category: llm-judge-foundations
---
# All Verdicts are Not Equal: Rethinking LLM Judge Reliability

## One line
Reliability audit of six frontier judges showing verdicts change across identical temperature-0 runs, order swaps flip most verdicts on hard tasks, and the most consistent judge is consistently wrong (51% ground-truth agreement).

## Method
Six frontier models x four benchmarks x five prompt formats x two orders x three temperatures x ten repetitions. Introduces the trustworthy verdict rate T (probability a verdict is reproducible, order-invariant and accurate) and an upper bound on accuracy from position bias.

## Evaluated on
Position swaps flip the majority of verdicts on challenging tasks; most deterministic judge 51% agreement with ground truth; reliability is item-specific; holistic rubric scoring improves trustworthiness more than any single prompting intervention on pairwise win rate.

## Limitations admitted by the authors


## Limitations found by others


## What it leaves untried
- Combining rubric scoring with verification tools on the items where T is low.
