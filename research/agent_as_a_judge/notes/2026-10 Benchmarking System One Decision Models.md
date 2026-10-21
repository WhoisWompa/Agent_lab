---
title: "Benchmarking System One decision models against trained classifiers and language models for automated decision gates"
authors: Amir Rafe et al.
date: 2026-10
arxiv: 2610.00346
url: https://arxiv.org/abs/2610.00346
venue: arXiv (preprint submitted to Elsevier)
category: alternative-paradigms
pdf: agent as a judge papers/decision models/open models/evaluations/Benchmarking System One Decision Models Against Trained Classifiers and LMs (Rafe 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "evaluations"]
topics: ["decision models", "judge and decision-model audits", "confidence-gated escalation"]
---
# Benchmarking System One decision models against trained classifiers and language models for automated decision gates

## One line
One harness sends the same typed requests to hosted and open decision models (Jev and five open families), open generative LMs and trained classifiers, then turns accuracy, calibration, option-naming robustness, selective risk and cascade cost into condition-dependent rules for automated decision gates.

## Method
Problem: a program that hands a branch (escalate, pay/hold/reject, route) to a model needs a declared option plus a probability it can threshold. Decision models ("System One") return one distribution per typed question in a forward pass without generating text. But each published evaluation uses its own prompts, option texts and scoring, so numbers cannot be compared, and none scored several decision models against a classifier trained on the same items.

The contribution is an evaluation design, not a model:
- **Identical requests, one condition varied at a time.** Every model gets the same state, questions and rubrics, with neutral option identifiers (o1..oK) so names carry no cue. Labels, readout, option count, names and second stage are then changed singly. Generative models are read both from stated JSON probabilities and from option-key likelihoods, separating model from readout.
- **Three identities computed from recorded answers.** A served temperature T is undone by raising probabilities to T/T' and renormalising. Domain-then-intent accuracy is the mean of the product of both stages' correctness. Cascade accuracy = A1 + e(τ)·Δesc(τ): escalation helps only if the second stage is better on escalated items, and beats it only if the first stage is better on kept items.
- **Gate measures beyond accuracy:** held-out threshold coverage, Learn-then-Test guaranteed coverage, out-of-scope false acceptance, and flips under a yes/no swap.

## Evaluated on
- **Labels decide the ranking.** With labels, fine-tuned DeBERTa-v3-large wins every labeled task but one: 0.793 vs Jev 0.732 on workflows, 0.953 vs 0.913 on CLINC-150. Without labels, no decision model significantly beats Jev; Gemma-4-31B leads by 2.8 points on CLINC-150 (p=0.004) at 0.2893 vs 0.1095 USD per thousand.
- **Name swaps split the classes.** Swapping yes/no flips 50.5 answers per hundred for Jev (retest floor 1.3), 91.3 for Laya, at least 16.8 for generative models, but 4.2 to 6.5 for four decoder-head checkpoints, whose backbones flip far more.
- **Guarantees cost coverage; in-scope thresholds miss unknowns.** A 5% risk guarantee leaves Jev 0.528 of intent decisions vs 0.93 under a plain held-out threshold, which still accepts 0.310 of out-of-scope requests despite AUROC 0.921.
- **Stored temperatures do not transfer.** Kev-9B's calibration error goes from 0.051 at T=1 to 0.377 as shipped with 150 options.
- **Cascades pay only when stages differ.** this-that-model-1.0 escalating 0.30 to Gemma-4-31B reaches Gemma's 0.942 at 0.108 USD per thousand, about Jev's price.

## Limitations admitted by the authors
- Accuracy is agreement with references, not truth: workflow labels are a ~4B teacher's consensus (self-agreement 0.735) and emotion labels are hashtags. Rater-labeled GoEmotions gave the same class ranking.
- Public benchmarks stand in for operating gates; no deployed logs were used, so the rules are untested on real traffic.
- Jev's and Laya's training data are unreleased, so exposure cannot be checked, and it matters: decider-2b's 0.803 vs 0.504 on emotion comes from training on that corpus and vanishes on GoEmotions.
- Jev can change without notice; pinning 1.13.0 documents but does not prevent drift.
- Adapter rendering moves results: options without keys raised this-that-model-1.0 by 6.8 points on CLINC-150, level with Jev.
- Held-out thresholds are not guarantees: the risk upper bound exceeds 5% for every model but one.

## Limitations found by others

## What it leaves untried
- Running the rules on a live gate's logs with human-adjudicated labels, since every threshold and saving here rests on partly synthetic benchmark labels.
- Gating on more than top-label probability (learned deferral, a separate out-of-scope threshold); on social-science tasks errors reach a fifth by a tenth of coverage, so confidence alone buys little.
- Multi-step or trajectory judgments; every task is single-shot classification.

## Topics
[[Topic - decision models]] · [[Topic - judge and decision-model audits]] · [[Topic - confidence-gated escalation]]
