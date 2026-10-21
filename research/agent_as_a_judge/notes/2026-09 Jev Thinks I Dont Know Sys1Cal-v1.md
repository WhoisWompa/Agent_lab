---
title: "Jev thinks \"I don't know\", but doesn't say it: Introducing Sys1Cal-v1 Dataset for Probability Calibration"
authors: Riccardo Porcedda
date: 2026-09
arxiv: 2609.35342
url: https://arxiv.org/abs/2609.35342
venue: arXiv
category: llm-judge-foundations
pdf: agent as a judge papers/decision models/open models/evaluations/Jev Thinks I Dont Know But Doesnt Say It - Sys1Cal-v1 Dataset (Porcedda 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "evaluations"]
topics: ["decision models", "judge and decision-model audits", "calibration"]
---
# Jev thinks "I don't know", but doesn't say it: Introducing Sys1Cal-v1 Dataset for Probability Calibration

## One line
Builds a True/False benchmark with exactly known probabilities to test whether the System One decision model Jev returns probabilities that mean what they say, and finds that its Choice answers act as if a hidden "uncertain" mass had been dropped and the rest renormalised.

## Method
The problem: Jev's selling point is calibrated probabilities from three primitives (Noul for binary, Choice for categorical, Score for ordinal scales). The paper says no public test backs that claim. Existing benchmarks such as JevBench check only top-label confidence (ECE), not whether each option probability is right or whether the three primitives agree. That matters because expected-utility decisions downstream use the whole distribution.

The benchmark idea: generate propositions whose true P(A) is fixed by construction across six families from explicit probabilities to sequential Bayesian updates, then render each in several equivalent forms. Because the target is a distribution and not a single label, the score can be distance-based: OVL = 1 - |p_hat - p*|, a "soft accuracy". Score answers become a probability through their expectation over 10 levels. Pairwise distance between equivalent renderings measures representation sensitivity.

The second idea is a latent three-valued model. Score and Noul agree with each other and with ground truth, but Choice relates to Score through a non-linear curve. The paper's explanation: Jev holds a latent T/U/F split, takes T from the Score expectation, models the uncertain mass as U = lambda * mu^alpha * (1-mu)^beta, and Choice reports T/(T+F), throwing U away. This yields two tools: an inverse map that turns a raw Choice answer into a calibrated binary probability, and an interval P(A) in [T, T+U] for uncertainty-aware decisions (act, defer, escalate). The paper assumes Score carries no hidden uncertainty, and its only reason is that Score is already well calibrated.

## Evaluated on
- Choice is the weak primitive: mean OVL is 0.764 for Jev-Choice, against 0.918 for Noul and 0.886 for Score. The open SemIf Choice baseline is worse at 0.629.
- The uncertain component is real in the data: the fit gives alpha = 0.530, beta = 1.011 and R^2 = 0.834 against Choice probabilities. The global lambda is 0.978 (CI 0.789 to 1.000), and adding U cuts absolute error by 0.110 on average, with a 95% CI that excludes zero.
- Inverting the map fixes Choice after the fact: mean/median OVL goes from 0.764/0.771 to 0.880/0.903.
- The T/U/F interval reaches mean OVL 0.931 and median 0.978, but the mean interval width is 0.292, so this score is far more lenient than binary OVL.
- Choice is less stable across equivalent renderings: mean pairwise TV is 0.0998, more than twice Noul's 0.0441.
- In a worked cost example, one raw Choice output of 0.632 gives three different actions: act True raw, act False corrected (0.400), defer under T/U/F.

## Limitations admitted by the authors
- The items are synthetic and templated, with little ecological coverage: no rich paraphrase, adversarial wording or domain decisions. So the findings may not hold on the free-form inputs a judge sees.
- Score is reduced to one number, its expectation. The full 10-level distribution may hold structure this throws away, and the whole U model is built on that summary.
- The three-truth-value account only describes the outputs; it is not a claim about Jev's internals. Choice behaves "as if" a richer state were collapsed, which the authors say indicates but does not prove a hidden third value.

## Limitations found by others

## What it leaves untried
- Testing the correction on held-out problems. The fit and the inverse map seem to be estimated on the same 92 problems they are scored on, so the jump from 0.764 to 0.880 is in-sample. Transfer to new items is unknown.
- Adding an explicit "Uncertain" option to Choice, or comparing U with Noul's spread, would test the hidden-third-value hypothesis directly instead of inferring it from the shape of a curve.
- Measuring whether the T/U/F deferral actually lowers cost on real judge decisions. The case for it rests on one hand-built example with chosen costs (100 for an error, 45 for deferring).

## Topics
[[Topic - decision models]] · [[Topic - judge and decision-model audits]] · [[Topic - calibration]]
