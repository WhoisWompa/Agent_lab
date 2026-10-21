---
title: "Does a Hosted Decision Model Respect Irrelevant Alternatives? A Pre-Registered Test of Option-Set Dependence in Jev"
authors: Dushyant Rajput et al.
date: 2026-10
arxiv: 2610.16655
url: https://arxiv.org/abs/2610.16655
venue: arXiv
category: llm-judge-foundations
pdf: agent as a judge papers/decision models/open models/evaluations/Does a Hosted Decision Model Respect Irrelevant Alternatives (Rajput 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "evaluations"]
topics: ["decision models", "judge and decision-model audits", "presentation sensitivity"]
---
# Does a Hosted Decision Model Respect Irrelevant Alternatives? A Pre-Registered Test of Option-Set Dependence in Jev

## One line
Shows that the Jev decision model's option probabilities depend on which other options are listed (it violates independence of irrelevant alternatives), so its probabilities are only meaningful relative to the option list, not as fixed properties of each option.

## Method
The problem: callers threshold and compare a decision API's per-option probabilities across calls as if each belonged to the option alone. That holds only under independence of irrelevant alternatives (IIA): the odds P(A)/P(B) between the right answer A and its strongest wrong rival B should not change when an irrelevant option is added. LLM sensitivity to option order and wording is known; set dependence in a calibrated decision model had not been measured.

The idea is a direct, pre-registered measurement of IIA in three pieces:
- **Signal versus noise.** Jev is stochastic (identical calls differ), so a raw change in log-odds L = ln P(A)/P(B) is inflated by noise. Every option set is run twice and the squared change minus half the summed squared repeat differences is used; if each call is truth plus independent noise, its expectation is exactly the squared systematic shift, whatever each set's noise level.
- **A clone test that separates two theories of choice.** Adding a paraphrase B' of the wrong answer: Luce predicts A loses mass (B and B' together take a double share, pooled shift -ln 2); elimination by aspects (EBA) predicts A is untouched and B, B' split B's share (pairwise shift +ln 2).
- **Similar decoys and growing option counts**, to test whether shifts are directional and grow with list size.

It also tests a mitigation: one yes/no question per option, set-independent by construction.

## Evaluated on
- Every added option moves the odds beyond noise: RMS shift 0.20-0.52 nats against run-to-run noise 0.15-0.17 (1.2-3 times), all 10 main cells significant, even for an off-domain option taking at most 0.1% of the mass.
- Shifts follow similarity, not attraction: a decoy similar to the wrong answer moves odds toward gold by +0.099 [0.073, 0.124]; one similar to gold does not detectably hurt it (+0.008, CI spans 0).
- Paraphrases are partial substitutes, between Luce and EBA: gold keeps its mass (0.656 to 0.640, Luce predicted about 0.49), but the clone takes only 0.124 of B's 0.360, about a third rather than EBA's half; pairwise shift is 0.53 of EBA's prediction. A clone flips the top choice in 15% of items.
- Distortion grows with log K, no plateau: about 1.02 nats at 255 off-domain options; off-domain padding turns the shift against gold (-0.31) and drops accuracy 0.853 to 0.814.
- Questions packed in one call are isolated: mean P(A) changes under 0.0006 across all nine conditions.
- Yes/no per option restores invariance (RMS shift under 0.02) but picks the right answer 8.7 points less often (0.693 vs 0.849 at K=128), so the "fix at no cost" hypothesis fails.

## Limitations admitted by the authors
- One model version (jev-1.13.0) and single-label classification with bare label names only; options with rich descriptions, other tasks, or later versions may behave differently.
- No human review: an LLM checked near-decoys and flagged 4 of 300 as plausibly correct, so about 15 unreviewed bad decoys may remain and slightly inflate near-decoy shifts; clone paraphrases were also LLM-written.
- Shift analyses cover only contested items (both A and B at least 0.05), about a quarter of items; effects on confident items are not estimated.
- The mechanism (joint encoding of the option list) is inferred from behaviour, not tested.

## Limitations found by others

## What it leaves untried
- No method that keeps both invariance and accuracy: the authors list calibrating yes/no scores against Choice or averaging Choice over random option subsets but test none, so callers must choose between comparable scores and correct answers.
- No judge setting: everything is intent and topic classification, so whether option-set dependence shifts verdicts when Jev grades candidate answers or rubric levels (where the option list is often edited) is open.

## Topics
[[Topic - decision models]] · [[Topic - judge and decision-model audits]] · [[Topic - presentation sensitivity]]
