---
title: Do LLM Evaluators Prefer Themselves for a Reason?
authors: Wei-Lin Chen et al.
date: 2025-04
arxiv: 2504.03846
url: https://arxiv.org/abs/2504.03846
venue: arXiv
category: llm-judge-foundations
topics: ["judge and decision-model audits"]
---
# Do LLM Evaluators Prefer Themselves for a Reason?

## One line
On verifiable tasks, stronger models' self-preference is mostly legitimate, but harmful self-preference persists exactly where the judge erred as a generator; long CoT before judging reduces it.

## Method
Seven model families judge own vs others' answers on math, factual knowledge and code with ground truth; separates legitimate from harmful self-preference; tests inference-time scaling; extends to LMArena.

## Evaluated on
Stronger models show more self-preference, mostly aligned with real quality; when wrong, stronger models show more pronounced harmful self-preference; long CoT before evaluation reduces harmful self-preference.

## Limitations admitted by the authors


## Limitations found by others


## What it leaves untried
- Cross-family blinding plus CoT combined.

## Topics
[[Topic - judge and decision-model audits]]
