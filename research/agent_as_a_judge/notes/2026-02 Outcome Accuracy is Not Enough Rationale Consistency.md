---
title: Outcome Accuracy is Not Enough: Aligning the Reasoning Process of Reward Models
authors: Binghai Wang et al.
date: 2026-02
arxiv: 2602.04649
url: https://arxiv.org/abs/2602.04649
venue: arXiv
category: trained-judges-reward-models
topics: ["trained judges and reward models", "preference learning"]
---
# Outcome Accuracy is Not Enough: Aligning the Reasoning Process of Reward Models

## One line
Shows GenRMs/LLM judges trained on outcome accuracy reach right verdicts for wrong reasons, and trains with a hybrid rationale-consistency + outcome reward.

## Method
- Rationale Consistency metric: agreement of the judge's reasoning with human reasoning.

## Evaluated on
- RM-Bench 87.1, JudgeBench 82.0; about 5% average gain over outcome-only baselines; +7% Arena Hard v2 creative writing when used for RLHF ([arXiv](https://arxiv.org/abs/2602.04649)).

## Limitations admitted by the authors
- Outcome-only training lowers rationale consistency over training.

## Limitations found by others


## What it leaves untried

## Topics
[[Topic - trained judges and reward models]] · [[Topic - preference learning]]
