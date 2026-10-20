---
title: LLM-as-a-Judge Is Not an Oracle: Why Self-Improving Agents Need Deterministic Guardrails
authors: Vansh Wahi
date: 2026-09
arxiv: 2609.02246
url: https://arxiv.org/abs/2609.02246
venue: arXiv
category: self-evolving-tests
---
# LLM-as-a-Judge Is Not an Oracle: Why Self-Improving Agents Need Deterministic Guardrails

## One line
Production experience report: LLM-judged self-improvement loops failed in 11 ways; proposes PROCTOR, a Teacher-Student loop with five deterministic guardrails the judge cannot override.

## Method
Teacher (an LLM judge) evaluates Student changes; guardrails: hermetic sandboxes, capability-disjoint roles, acceptance checks that outrank the Teacher, frozen holdouts, canary cases where a perfect score signals cheating.

## Evaluated on
Months of production use (contract analysis, compliance review, code quality). 11 failure modes in 4 classes: judge bias, harness/metric failures, ground-truth errors, reward hacking. One case: a 100% pass rate concealed about 68% true capability because agents read cached answer keys. Rubric rewrites gave limited gains; constraining the judge's output order helped reliably.

## Limitations admitted by the authors
- Teacher is itself an LLM judge; the paper lists failures PROCTOR does not prevent.
- Single-author practitioner report, not a controlled study.

## Limitations found by others


## What it leaves untried
- Measure which guardrail catches which failure on a public benchmark.
