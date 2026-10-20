---
title: Using LLM-as-a-Judge For Evaluation: A Complete Guide (Critique Shadowing)
org: Hamel Husain
date: 2024-10
url: https://hamel.dev/blog/posts/llm-judge/
kind: essay
category: production-practice
---
# Using LLM-as-a-Judge For Evaluation: A Complete Guide (Critique Shadowing)

## One line
Husain's "critique shadowing" method for building an LLM judge from one domain expert's binary verdicts and written critiques (Oct 2024, updated Sep 2026); pre-window but the basis of 2025-26 practice.

## What they do
Seven steps: find the principal domain expert; build a diverse dataset across features, scenarios, personas; expert gives pass/fail plus a written critique; fix obvious errors; build the judge with critiques as few-shot examples and iterate until it agrees with the expert; run error analysis on unseen data; build specialised judges only where needed.

## Evidence
Honeycomb query assistant: "It took us only three iterations to achieve > 90% agreement between the LLM and Phillip [Carter]"; dataset ~50% failures, so raw agreement was meaningful there. Updated guidance: ~100 examples per failure mode; "Below 60 examples, the confidence intervals are often too wide."

## Limitations and criticisms
Raw agreement misleads on imbalanced data; report TPR and TNR separately. Single-expert anchoring risks idiosyncratic standards. Husain himself says the main value is forcing people to look at data.

## Relevance to agent evaluation
Gives a concrete, reproducible judge-calibration loop and one of the few published agreement numbers (>90% after three iterations, single expert, balanced data).
