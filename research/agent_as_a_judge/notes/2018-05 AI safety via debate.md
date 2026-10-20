---
title: AI safety via debate
authors: Geoffrey Irving et al.
date: 2018-05
arxiv: 1805.00899
url: https://arxiv.org/abs/1805.00899
venue: arXiv
category: alternative-paradigms
---
# AI safety via debate

## One line
Proposes training agents via a zero-sum debate game judged by a human, arguing that optimal play in debate can let a polynomial-time judge answer questions in PSPACE.

## Method
Two agents alternate statements about a question; a judge (human, or in the toy experiment a sparse classifier) sees the transcript and picks the winner. The judge never sees the full evidence, only what debaters reveal. Theory: complexity-theoretic analogy (debate with a poly-time judge ~ PSPACE). No execution or verification; judge sees the argument transcript only.

## Evaluated on
MNIST toy experiment: debaters reveal pixels to a sparse classifier judge that sees only 6 pixels; debate raised the judge's accuracy from 59.4% to 88.9% (as recalled from the abstract). Also small human pilot experiments on images.

## Limitations admitted by the authors
- The approach relies on honesty being the winning strategy at equilibrium, which is assumed, not shown, for real ML training.
- Human judges may be biased, persuadable or fooled by rhetoric; the paper names this as the central open question.
- The MNIST experiment is a toy and does not involve natural language.

## Limitations found by others
- Obfuscated arguments problem: a dishonest debater can force the honest one into an intractable sub-problem (named and addressed by Brown-Cohen et al. 2025, arXiv 2506.13609).
- Single- and two-turn human debate did not help humans on hard reading comprehension (Parrish et al. 2022, arXiv 2204.05212; arXiv 2210.10860).
- Recchia et al. 2025 (arXiv 2507.19486): simple protocols showed no overall advantage over deferring to the model; evaluator confirmation bias.

## What it leaves untried
- Debate where the judge is an agent with tools (can run code, check sources) rather than a passive reader of a transcript.
- Debate as a protocol for evaluating agent trajectories rather than answers to questions.
