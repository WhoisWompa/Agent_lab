---
title: Calibration and Risk-Budgeted Decisions with System One Models
authors: Soundouss Messoudi et al.
date: 2026-10
arxiv: 2610.19811
url: https://arxiv.org/abs/2610.19811
venue: arXiv
category: llm-judge-foundations
pdf: agent as a judge papers/decision models/open models/papers/Calibration and Risk-Budgeted Decisions with System One Models (Messoudi 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "papers"]
topics: ["decision models", "calibration"]
---
# Calibration and Risk-Budgeted Decisions with System One Models

## One line
Shows that the "calibrated probability" scores of System One decision models (Jev and others) cannot simply be thresholded for allow/block or keep/discard decisions, and replaces naive thresholding with Learn Then Test certification that bounds the error rate among the inputs the system lets through.

## Method
The problem: agents make forced binary decisions (allow or block an input, discard or retain a document) with no human to defer to. One action is the conservative fallback (block, retain); the other is the useful one (allow, discard), and the critical error is taking the useful action when the input was actually positive. The risk that matters is therefore the False Omission Rate, P(Y=1 | score < τ): contamination among the inputs the system allowed. The goal is to make the allowed set as large as possible while keeping that rate under a budget α; uncertain inputs fall to the fallback rather than to abstention.

The tempting shortcut is to set τ = α, trusting the vendor's calibration claim. A calibration-policy identity shows why this fails: FOR(τ) = E[S | S < τ] + E[m(S) − S | S < τ], where m is the true positive rate at a given score. Under exact calibration the second term is zero and FOR ≤ τ. But what matters is the miscalibration inside the low-score region only, which a global metric like ECE does not measure, and its sign can push risk either way.

The fix is Learn Then Test. Candidate thresholds are fixed in order from a separate fit split. On a held-out calibration set, each threshold's count of allowed items and positives among them gives a binomial p-value for "this threshold's FOR exceeds α". Thresholds are tested in sequence and testing stops at the first failure; the largest certified threshold is deployed. With probability at least 1 − δ no certified threshold breaks the budget. If none certifies, the system deploys nothing and always takes the fallback. It assumes calibration and deployment data are i.i.d. from the same distribution; it does not assume the scores are calibrated.

## Evaluated on
- Calibration varies by task, so vendor claims do not carry over: Jev's ECE is 0.034 on WildGuardMix and 0.29 on SciDocs.
- Low ECE does not mean a usable policy: on StackOverflow, Kev-base has better ECE than Kev-ft (0.051 vs 0.16) but much worse separation (AUROC 0.599 vs 0.81).
- Naive and empirical thresholds often break the budget, LTT rarely does: test FOR exceeds α in 42.0% of settings for Naive (mean excess 7.09 points, max 73.26), 51.7% for Empirical (mean 1.17), and 7.8% for LTT (mean 0.10). The worst case: Span-01 on Aegis at α = 0.15 lets through 95.3% of benign inputs, but 60.9% of what it allows is harmful.
- Naive thresholds can also be needlessly cautious: on WildGuardMix at α = 0.15, Jev's naive policy accepts 68.7% of benign inputs at 3.3% risk, while LTT accepts 96.8% at 12.8% risk.
- The price is availability. LTT certifies only 21.3% of policies at α = 0.05 and 76.6% at α = 0.5. Fine-tuning a small open model helps: Kev-ft certifies 31/36 settings vs 13/36 for Kev-base, at about $0.003 per 1,000 examples and about 98 ms per example.

## Limitations admitted by the authors
- The guarantee needs calibration and deployment data drawn i.i.d. from the same distribution. The six English benchmarks say nothing about deployment or adversarial shift, which would need periodic recalibration.
- Exact binomial certification has a minimum sample size. Even with zero observed errors, a threshold needs ⌈log δ / log(1 − α)⌉ allowed calibration examples: 45 at α = 0.05 and 22 at α = 0.10, with δ = 0.10. Strict budgets or small calibration sets therefore often end in non-deployment.
- The fine-tuning route that recovers certified policies needs labelled data and local training compute, which a cold-start deployment may not have.
- ATBench is scored on truncated trajectories after the fact, and the reranking tasks use a constructed document mix rather than a real retrieval pipeline. Both change what the measured FOR means.
- The guarantee holds over draws of the calibration set, not for each test estimate, so a single run can still exceed the budget (12 of 153 LTT policies did).

## Limitations found by others

## What it leaves untried
- Certifying multi-model cascades, for example a cheap local scorer that escalates to an API model, with one risk budget for the whole chain. The authors name this but do not try it, and it is where the cost-latency trade-off would be decided.
- Risk control under distribution shift (weighted or online LTT). Moderation and prompt-injection inputs are adversarial by nature, so the i.i.d. assumption is the weakest part of the guarantee.
- Studying how the size of the calibration set affects availability. The authors raise this as future work; it would show how many labels a deployer needs before LTT stops returning non-deployment.

## Topics
[[Topic - decision models]] · [[Topic - calibration]]
