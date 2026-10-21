---
title: Scalable AI Safety via Doubly-Efficient Debate
authors: Jonah Brown-Cohen, Geoffrey Irving, Georgios Piliouras
date: 2023-11
arxiv: 2311.14125
url: https://arxiv.org/abs/2311.14125
venue: ICML 2024
category: alternative-paradigms
topics: ["alternative evaluation paradigms"]
---
# Scalable AI Safety via Doubly-Efficient Debate

## One line
Gives debate protocols where the honest debater wins using polynomially many steps of simulation, even against a dishonest debater with unbounded compute, with a judge who checks only a constant number of steps.

## Method
Theoretical: models the task as a computation (possibly stochastic) that a human oracle can check at single steps; designs debate protocols with efficiency on both the honest prover and the verifier side.

## Evaluated on
No empirical evaluation; theorems only.

## Limitations admitted by the authors
- Assumes the problem is decomposable into human-checkable steps and that the human oracle is reliable at each step.

## Limitations found by others
- Brown-Cohen et al. 2025 (arXiv 2506.13609) note recursive protocols remain open to the obfuscated-arguments problem, which motivated prover-estimator debate.

## What it leaves untried
- Empirical test with LLM debaters.

## Topics
[[Topic - alternative evaluation paradigms]]
