---
title: Becoming Experienced Judges: Selective Test-Time Learning for Evaluators
authors: Seungyeon Jwa et al.
date: 2025-12
arxiv: 2512.06751
url: https://arxiv.org/abs/2512.06751
venue: arXiv
category: self-evolving-tests
topics: ["self-evolving tests", "LLM and agent judges"]
---
# Becoming Experienced Judges: Selective Test-Time Learning for Evaluators

## One line
Learning While Evaluating (LWE): a judge keeps an evolving meta-prompt that writes per-sample evaluation instructions and refines itself from self-generated feedback as it judges a stream of cases; Selective LWE updates only when the judge is self-inconsistent.

## Method
No training or validation set. For each sample the meta-prompt generates sample-specific criteria; the judge decides; self-feedback revises the meta-prompt. The selective variant uses self-inconsistency as the 'missed' signal deciding when to update, cutting cost.

## Evaluated on
Two pairwise comparison benchmarks; Selective LWE beats strong baselines (numbers in paper).

## Limitations admitted by the authors
- Learning signal is self-generated; no external ground truth during learning.
- Pairwise preference only; not interactive or agentic evaluation.

## Limitations found by others


## What it leaves untried
- Use disagreement with a human or execution oracle, not only self-inconsistency, as the trigger.
- Carry the learned meta-prompt across evaluations of one specific target.

## Topics
[[Topic - self-evolving tests]] · [[Topic - LLM and agent judges]]
