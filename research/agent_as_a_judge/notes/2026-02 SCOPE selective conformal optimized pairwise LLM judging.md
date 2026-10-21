---
title: SCOPE: Selective Conformal Optimized Pairwise LLM Judging
authors: Sher Badshah, Ali Emami, Hassan Sajjad
date: 2026-02
arxiv: 2602.13110
url: https://arxiv.org/abs/2602.13110
venue: ICML 2026
category: alternative-paradigms
topics: ["LLM and agent judges", "abstention and fallback", "presentation sensitivity"]
---
# SCOPE: Selective Conformal Optimized Pairwise LLM Judging

## One line
Selective conformal risk control for pairwise judges; Bidirectional Preference Entropy (query both orders) as the uncertainty score.

## Method
Calibrate an acceptance threshold so the error rate on non-abstained judgments is at most alpha.

## Evaluated on
At alpha = 0.10 empirical FDR 0.097-0.099; up to 2.4x more judgments accepted than baselines at the same risk (from abstract).

## Limitations admitted by the authors
- Exchangeability assumption; pairwise only.

## Limitations found by others


## What it leaves untried
- Extension to graded/rubric judgments of agent runs.

## Topics
[[Topic - LLM and agent judges]] · [[Topic - abstention and fallback]] · [[Topic - presentation sensitivity]]
