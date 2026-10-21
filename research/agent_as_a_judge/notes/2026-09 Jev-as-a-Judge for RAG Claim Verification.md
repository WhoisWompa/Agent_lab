---
title: "Jev-as-a-Judge for RAG Claim Verification: Confidence-Gated Cascading Between a Non-Generative Verifier and a Frontier LLM"
authors: Alden Do Rosario et al.
date: 2026-09
arxiv: 2610.20634
url: https://arxiv.org/abs/2610.20634
venue: arXiv
category: alternative-paradigms
pdf: agent as a judge papers/decision models/open models/evaluations/Jev-as-a-Judge for RAG Claim Verification - Confidence-Gated Cascading (Do Rosario 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "evaluations"]
topics: ["decision models", "LLM and agent judges", "confidence-gated escalation"]
---
# Jev-as-a-Judge for RAG Claim Verification: Confidence-Gated Cascading Between a Non-Generative Verifier and a Frontier LLM

## One line
Pits a non-generative decision model (jev-1.13.0: typed verdict plus native probability, no text) against a frontier LLM judge on RAG claim verification, finds an accuracy tie at 187x lower cost but different errors, and tests a cheap-first confidence-gated cascade.

## Method
Problem: RAG verification needs one bit per claim, yet pipelines buy it at generation prices. Proposal: a decision model returning one member of a declared enumeration (supported / not_supported) with a probability over it, nothing to parse.

- **Judge the guard on its guard metric.** Rejecting a supported claim costs a retry; passing an unsupported one ships a hallucination with an approval stamp. So the false-verification rate (share of gold-unsupported claims passed) is reported on its own, since balanced accuracy averages it in at half weight and can hide a large gap.
- **Probability provenance.** Probabilities are native, logprob-derived, or none (verbal self-reports excluded). Ranking claims (AUROC against gold) is separated from ranking the model's own errors (selective AUROC of max(p, 1-p) against correctness); only the second justifies routing.
- **Cheap-first cascade, evaluated honestly.** Jev answers every claim; below a confidence threshold the claim escalates to the frontier LLM (frontier-first is impossible: its API returns no logprobs). The threshold is cross-fitted and checked against random escalation at the same budget and an oracle escalating exactly Jev's errors.

## Evaluated on
- Accuracy tie at 187x cost: 73.27 vs 73.83 macro balanced accuracy, difference -0.56, CI [-5.6, 4.5]; $0.048 vs $8.93 per 1k claims.
- The tie hides different errors: 15.2% disagreement (41 vs 34 discordant), and Jev passes 23.2% of unsupported claims vs 14.1%, a 9.1-point gap, CI [4.55, 13.64], Holm-adjusted p = 0.005, the one robust result.
- Jev ranks claims well (AUROC 0.868) but its own errors only moderately (selective AUROC 0.722). Gating alone at 35.2% coverage gives 97.1% verified precision and 2.1% false verification.
- Cascade is 3.06x cheaper at unresolved accuracy: 74.10 at $2.92 vs 73.83 at $8.93 (CI [-3.85, 4.15]). Random escalation at the same budget does as well ($2.81), so the saving is the escalation share, not the signal.
- In-sample tuning inflates the score by 1.72 points (75.82) and understates cost ($1.62 vs $2.92). The oracle reaches 82.9.

## Limitations admitted by the authors
- No equivalence claimed: one flip in the thinnest class (4 claims) moves the macro average more than the whole gap.
- The cascade is the more permissive guard: 19.22% vs 14.14% false verification (adjusted p = 0.057), and 6.09 points worse than high-effort frontier (adjusted p = 0.005).
- Against Jev alone it costs 61x more for +0.83 points (CI [-3.36, 4.86]): it replaces the frontier, not the cheap tier.
- Run-to-run noise exceeds the gap: a second Jev pass flipped 7 verdicts (72.44 vs 73.27), and a prompt-parity fix moved the frontier from 73.06 to 73.83, reversing the sign.
- The threshold is not identifiable: fold-fits split between 0.80 (669 of 1000) and the top grid value (253), regimes escalating 17.2% vs 64.8%; the cascade falls below the frontier in 68 of 200 repeats.
- Calibration has one participant, since the frontier exposes no probability. Jev is off where routing trusts it: claims given 0.05 are supported 29% of the time.
- 187x is a one-day list-price ratio and Jev's free output tokens are vendor policy; the cascade is an offline replay with no latency or second hop measured.
- Harness validity is unconfirmed: their MiniCheck port scored 61.6 against a published 75.0.
- Conflict of interest: the authors sell claim verification, and the first author earlier published the in-sample figure corrected here.

## Limitations found by others

## What it leaves untried
- A better routing signal: the oracle sits 8.8 points above the cascade and selective AUROC (0.722) is the bottleneck; training the decision model to rank its own errors is the obvious step.
- A guard-priced objective: the threshold maximises balanced accuracy, which lands on a permissive point; choosing it out of fold to minimise false verification at a given cost is untested.
- Transfer: their contamination-resistant holdout, the test split and other yes/no tasks are untested.

## Topics
[[Topic - decision models]] · [[Topic - LLM and agent judges]] · [[Topic - confidence-gated escalation]]
