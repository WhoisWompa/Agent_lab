---
title: Limits to scalable evaluation at the frontier: LLM as Judge won't beat twice the data
authors: Florian E. Dorner, Vivian Y. Nastl, Moritz Hardt
date: 2024-10
arxiv: 2410.13341
url: https://arxiv.org/abs/2410.13341
venue: ICLR 2025
category: alternative-paradigms
---
# Limits to scalable evaluation at the frontier: LLM as Judge won't beat twice the data

## One line
Proves that when the judge is no more accurate than the evaluated model, no debiasing method can cut required ground-truth labels by more than half.

## Method
Theory on debiasing (e.g. prediction-powered inference) with judge labels plus ground-truth labels; empirical check of sample-size savings.

## Evaluated on
Main bound: at most a factor-two saving in labels; empirically savings are smaller than the bound (from abstract).
- (llm-judge-foundations) Upper bound: at most 2x label savings when judge accuracy <= evaluated model; empirical savings even smaller.

## Limitations admitted by the authors
- Bound is about estimating aggregate metrics, not per-instance judgments.
- Bound concerns binary/scalar evaluation estimates; assumes judge no better than evaluatee.

## Limitations found by others
- Feng et al. 2026 'Noisy but Valid' (2601.20913) give conditions under which noisy judge testing beats direct evaluation and quantify an 'oracle gap' for estimated judge TPR/FPR.

## What it leaves untried
- Same analysis for agentic judges whose accuracy may exceed the evaluated agent's in narrow checks (e.g. execution).
- Bounds when the judge has tools or references that make it more accurate than the evaluatee.

