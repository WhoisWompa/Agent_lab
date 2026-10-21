---
title: "Probability Contracts: Accuracy, Coherence, and Decisions Across LLM Interfaces"
authors: Han Chen et al.
date: 2026-09
arxiv: 2609.37470
url: https://arxiv.org/abs/2609.37470
venue: arXiv
category: llm-judge-foundations
pdf: agent as a judge papers/decision models/open models/evaluations/Probability Contracts - Accuracy, Coherence, and Decisions Across LLM Interfaces (Chen 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "evaluations"]
topics: ["decision models", "judge and decision-model audits", "calibration", "presentation sensitivity"]
---
# Probability Contracts: Accuracy, Coherence, and Decisions Across LLM Interfaces

## One line
A benchmark of small synthetic worlds with exact posteriors that scores a model's probability reports on three separate axes (error against the true posterior, coherence across equivalent requests, and the loss of the act-or-defer decision they trigger), and shows the three axes rank models differently.

## Method
The problem: a model can be asked for the same probability in several ways (a direct event question, a two-option choice, a full category distribution), and the answers can disagree while each passes validation. With real data there is only one outcome label per case, so nobody can tell which report was right for that case, or whether agreement means the reports are correct.

The idea is a "probability contract": each request is tied to an explicit event, the evidence shown, a mapping from output options to sets of outcomes, and the identities the reports must satisfy. The worlds are four-cell finite populations with integer counts and evidence likelihoods, so the true posterior is computed exactly. That lets the benchmark separate three questions: accuracy (distance to the true posterior), coherence (ten relations such as p(A)+p(not A)=1, category sums, Frechet bounds, invariance to option order or key names, exact repeats), and decision value (a reject-option controller that answers when its top probability is at least 1-c, else defers at cost c, scored with the exact posterior). Failed or rejected outputs count as deferrals, so cheap fallback cannot hide.

Two pieces of analysis carry the conceptual claims. First, half the gap between two reports of one event is all that disagreement certifies about their error; the rest is shared error that agreement cannot reveal. Second, averaging two reports always lowers the Brier score versus picking one at random (by the squared gap over four), and Brier equals decision loss averaged uniformly over defer costs, so at any single cost averaging can still hurt. Proposition 1 gives the exact per-world penalty by which action regions the reports and their midpoint fall into.

## Evaluated on
- Equivalent requests change decisions: Jev's Event and Choice interfaces give different binary actions on 32.8% of valid pairs at defer cost 0.10 (Kev 14.9%, Qwen Posttrained 34.2%); in the opening example 0.84 vs 0.97 for a true 0.694 turns a 0.10 deferral into a 0.306 expected loss.
- Accuracy and coherence rank models in opposite orders: Kev has lower canonical posterior error than Jev (0.2350 vs 0.2677 total variation) but a complement residual of 0.5055 vs 0.0929; Jev has the larger Event/Choice gap (0.1938 vs 0.0629) yet lower binary error (0.186 vs 0.294). The accuracy ordering also splits 4-4 across the eight strata.
- Disagreement hides most error: half the Event/Choice gap accounts for only 11-52% of mean pair error (Kev 10.7%, Jev 52.2%), and low-disagreement selection beats confidence selection only for Jev.
- Better Brier, not better decisions: on a 99-cost grid the averaging-minus-random loss contrast takes both signs for every model.
- No model passes the contract: all four fail the prespecified criterion (validity at least 0.995 and every relation's pass-rate lower bound at least 0.95); Jev's exact repeats differ, with only 745/1,000 within 0.02.
- Reports barely beat deferring: at c = 0.10 Kev loses 0.1090 and Jev 0.1336 against 0.10 for always defer, while the Qwen models simply always defer.

## Limitations admitted by the authors
- Four-cell worlds with two encodings make exact targets possible, but transfer to open-ended tasks is untested, and that is where judges are actually used.
- The local models all come from the Qwen lineage, and only one Jev revision was tested, so the coherence failures may reflect one family.
- Training, prompts, readout and precision all differ across configurations, so no gap can be traced to a single cause; why Kev and Posttrained sum p(A)+p(not A) to about 1.5 and 1.8 is unresolved.
- The primary worlds offer little room for gains: the oracle beats always defer by only 0.0103 at c = 0.10, which caps how much any decision policy can show.
- The 160-token reasoning arms produced zero valid reports, so the effect of reasoning on accuracy is undefined; a later 16-world diagnostic is too small for conclusions.
- Section 7 (disagreement and averaging) and the 99-cost sweep are post hoc, with pointwise intervals and no multiplicity correction; every small averaging penalty where both policies beat deferral has an interval containing zero.
- Likelihood readouts renormalise over answer tokens that hold little mass (mean 0.011 for Base), so they are not true event posteriors.

## Limitations found by others

## What it leaves untried
- Fixing the incoherence: averaging over two reports is the only reconciliation tried. Projecting all related reports onto the nearest coherent set was explicitly not run, though the paper shows complement residuals near 0.8 that such a step would directly remove.
- Choosing an interface per world. The baseline is a random pick, not a learned or rule-based selector, so whether one can predict which interface to trust stays open.
- Tasks without an exact posterior, for instance judge verdicts with human labels, to test whether the accuracy-coherence reversal holds where judges are deployed.

## Topics
[[Topic - decision models]] · [[Topic - judge and decision-model audits]] · [[Topic - calibration]] · [[Topic - presentation sensitivity]]
