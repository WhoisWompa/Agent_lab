---
title: "Recalibrating Many Questions with Few Labels: Minimax Rates and Identification Limits"
authors: Xiaoyu Li et al.
date: 2026-10
arxiv: 2610.18488
url: https://arxiv.org/abs/2610.18488
venue: arXiv
category: llm-judge-foundations
pdf: agent as a judge papers/decision models/open models/evaluations/Recalibrating Many Questions with Few Labels - Minimax Rates and Identification Limits (Li 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "evaluations"]
topics: ["calibration", "decision models"]
---
# Recalibrating Many Questions with Few Labels: Minimax Rates and Identification Limits

## One line
A theory paper on recalibrating a probability-returning model (such as the decision model Jev) per question when there are many questions but few labels each: what pooling across questions recovers, and what no amount of pooling can.

## Method
Calibration on average says nothing about one question. Each question j has its own map g_j(p) = P(Y=1 | P=p), assumed nondecreasing (the model ranks cases correctly within a question). The target is the average excess Brier score over the true maps, with m questions and n labels each.

**Fixed effects (what can be shared).** If every map lies within sup-distance τ and total variation V of one shared monotone shape, the minimax risk is (mn)^-2/3 + min{τ², 1/n} + min{τ², V², (V/n)^2/3}, up to universal constants. The shape is learned from all mn labels; each question learns or ignores its own offset and wiggle, whichever costs less. The estimator that reaches this rate is a pooled isotonic fit plus a per-question bounded-variation correction. The size of that correction is chosen once for all questions, on held-out labels pooled across questions, so τ and V need not be known. Tuning each question on its own labels cannot adapt. Under constant shifts with large m²/n it loses a factor of order min{n, log(m²/n)}, because n labels cannot tell a small shift from none.

**Random effects (what is necessary for decisions).** If the maps are drawn from an unknown prior, the target is the Bayes risk, which can be far lower: a prior picking constant 1/4 or 3/4 has Bayes risk at most e^(-n/8)/4. But n labels identify only the prior's moments up to order n, and the Bayes rule needs moment n+1. The paper's "identification regret" is the excess one rule must accept against all priors that produce the same data. It equals a squared Chebyshev radius of the unidentified top moments. A new lemma on sorted vectors confines that moment to an interval of length 4^-n, so the regret is at most 2^-n.

## Evaluated on
- Not knowing the prior costs little past a few labels: at most 2^-n (under 10^-3 for n≥10), and at least β⋆^-n/(72√n), β⋆≈3.583, for every finite m, so more questions cannot remove it.
- At one to three labels it can equal the Bayes risk itself: the ratio is 1, 1/2, 1/5 for n = 1, 2, 3 (arcsine prior).
- For constant maps (an uninformative predictor) the exponential base is exactly β⋆, not the 4 the moment range suggests.
- Pooling pays: at m=300 and n=16, one question alone resolves its map at about 0.16, while the pool resolves the shape at about 0.0035.
- In simulation, per-question cross-validation costs up to 14.6x (median 2.5) over the best fixed estimator. Tuning once across questions stays within 1.40x (median 1.05), but this rule was added post hoc.

## Limitations admitted by the authors
- The bounds are on Brier risk, not calibration error. The lower bounds do not transfer, because predicting the pooled label mean already has calibration error at most 1/(4mn).
- The rate assumes continuous outputs. Deployed models often report a coarse grid, where the pooled mean reaches 1/(4mn), and that case is open.
- The paper assumes one shared output distribution and monotone maps. Without monotonicity the 4^-n confinement fails: a counterexample at n=1 gives a gap of 1/2.
- The 2^-n bound assumes infinitely many questions. No finite-m procedure is given, and rare label patterns amplify estimation error.
- Constants are not explicit, so no concrete m and n are given at which per-question tuning provably loses.
- For monotone maps the base is known only to lie in [2, β⋆]. The hard cases are uninformative predictors, so it is unknown whether useful predictors are easier.

## Limitations found by others

## What it leaves untried
- No real Jev data. The motivating use is never tested, and real outputs are likely discrete and differ across questions, which breaks two assumptions.
- A finite-m empirical-Bayes procedure (for example, a nonparametric maximum-likelihood prior), which a practitioner needs to reach the near-Bayes target.
- Per-question tuning around a pooled shape, the rule most practitioners would use. The lower bound does not cover it, and the simulations hint it loses.

## Topics
[[Topic - calibration]] · [[Topic - decision models]]
