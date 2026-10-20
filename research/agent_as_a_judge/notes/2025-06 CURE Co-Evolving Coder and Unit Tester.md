---
title: Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning (CURE)
authors: Yinjie Wang et al.
date: 2025-06
arxiv: 2506.03136
url: https://arxiv.org/abs/2506.03136
venue: NeurIPS 2025
category: self-evolving-tests
---
# Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning (CURE)

## One line
RL framework that trains a code generator and a unit-test generator together from their interaction outcomes, without ground-truth code, so the tester learns from the coder's mistakes.

## Method
Coder samples solutions, tester samples tests; execution gives a pass/fail matrix. Tester reward favours tests that separate correct from incorrect solutions (penalising tests that reject correct code or pass wrong code). Coder is rewarded for passing tests.

## Evaluated on
ReasonFlux-Coder models improve code generation and unit-test accuracy over base Qwen2.5 models and serve as reward models / for test-time scaling (numbers in paper).

## Limitations admitted by the authors
- Paper shows generated tests can be wrong (hallucinated expected outputs) or correct-but-naive (pass incomplete code); the reward design must penalise both.

## Limitations found by others
- Code-A1 (2603.15611) argues single-model self-play with white-box access causes self-collusion (trivial tests), while black-box testers write generic tests; it separates the two roles into opposing models.

## What it leaves untried
- Apply the tester-reward idea to a judge of agents: reward tests that discriminate known-good from known-bad agent behaviour.
