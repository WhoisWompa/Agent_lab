---
title: Prover-Verifier Games improve legibility of LLM outputs
authors: Jan Hendrik Kirchner et al.
date: 2024-07
arxiv: 2407.13692
url: https://arxiv.org/abs/2407.13692
venue: arXiv (OpenAI)
category: alternative-paradigms
---
# Prover-Verifier Games improve legibility of LLM outputs

## One line
Trains small verifiers against helpful and sneaky provers on grade-school math so that strong-model solutions become checkable by weak verifiers and by time-limited humans.

## Method
Iterative game: a small verifier is trained to predict solution correctness; a helpful prover is rewarded for correct solutions the verifier accepts; a sneaky prover is rewarded for incorrect solutions the verifier accepts. Verifier sees only the final chain-of-thought text. Correctness ground truth is available (GSM-style math).

## Evaluated on
Optimising only for correctness makes solutions less legible (the legibility trade-off, often called the 'legibility tax'). Over training, time-constrained humans' accuracy rose on helpful-prover solutions and fell on sneaky-prover solutions, i.e. sneaky provers learn subtler errors (from abstract).

## Limitations admitted by the authors
- Requires ground-truth labels for correctness; demonstrated on one math domain.
- Legibility costs some accuracy relative to correctness-only training.

## Limitations found by others


## What it leaves untried
- Use the trained verifier as an evaluator for agent outputs in domains without labels.
- Combine with debate: prover and sneaky prover as debaters.
