---
title: "When the Right Answer Is Missing: An Arithmetic-Dependent Rejection Bottleneck in Jev"
authors: Jike Zhong et al.
date: 2026-09
arxiv: 2609.39496
url: https://arxiv.org/abs/2609.39496
venue: arXiv
category: alternative-paradigms
pdf: agent as a judge papers/decision models/open models/evaluations/When the Right Answer Is Missing - Rejection Bottleneck in Jev (Zhong 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "evaluations"]
topics: ["decision models", "abstention and fallback", "judge and decision-model audits"]
---
# When the Right Answer Is Missing: An Arithmetic-Dependent Rejection Bottleneck in Jev

## One line
Shows that the typed decision model Jev picks the right numeric answer from a menu 99% of the time but rejects a menu with no right answer only 7% of the time, even with an explicit NONE option, and repairs most of the gap with a rejection-probability threshold.

## Method
The problem: typed decision models such as Jev return a structured choice from a predefined menu rather than generated text. Real workflows (the paper's example is matching a payment to retrieved invoices) often hand the model a menu where every candidate is wrong. TypeSafe's own guidance is to add an "other" or "none-of-the-above" option. The paper asks whether a model that can select the right answer can also tell when none is offered.

The idea is a paired test. Each problem appears twice, once with exactly one correct candidate and once with none, so the present-minus-absent accuracy gap measures rejection failure directly. The same decision is posed three ways: Menu Choice (A/B/C/NONE), a T/F Choice per candidate through the categorical API, and native Boolean per candidate, which differs from T/F only in the type field. This separates whether Jev can compute the answer from whether the output interface is to blame.

The repair works on scores the API already returns. Answer-absent menus put more probability on NONE than answer-present menus do, even when NONE does not win the argmax. So the rule becomes: reject if P(NONE) ≥ τ, otherwise take the argmax candidate. For per-candidate verification, the acceptance threshold on the truth score is raised above 0.5. τ is picked on 20 separate development problems, then frozen.

## Evaluated on
- Selection does not imply rejection: Menu Choice gets 99% present vs 7% absent on two-operation arithmetic (a+b−c), and 94% vs 24% on purchase totals.
- The model can verify but the categorical interface fails: native Boolean gets 99% exact-match rejection on the same absent arithmetic menus, while T/F Choice with the same questions gets 27%. Supplying the computed result lifts Menu rejection from 7% to 100%.
- The failure appears with very little computation: Menu absent accuracy falls from 66% at one operation to 4% at two. Even single-digit operands give only 56% rejection. Lookup and logic controls are perfect.
- Scores still carry the signal: T/F AUC is .985 on arithmetic, but only 88/200 menus are exact matches at the 0.5 threshold.
- Thresholding recovers most rejection on held-out cases: arithmetic Menu at τ=.03 goes from 7% to 79% rejection while selection drops from 99% to 97%, so balanced accuracy rises from 53% to 88%. Purchase rejection goes from 24% to 79%, but selection drops from 94% to 86%.
- The candidate sets are not the problem: reasoning-enabled Qwen3.5-9B gets 100% present and absent on the arithmetic and purchase menus.

## Limitations admitted by the authors
- Jev is tested only through its hosted API, with no access to weights or activations. The paper therefore describes the bottleneck but cannot say why categorical rejection fails when Boolean verification succeeds.
- The fix trades away selection, and the cost depends on the task. Purchase totals give up 8 present-case successes to gain 55 rejections, and time-calculation T/F selection falls from 61 to 59 of 80.
- Thresholds are fitted separately for each task and interface. τ ranges from .03 to .13 for Menu and from .66 to .90 for verification, so cross-task calibration is left as future work.
- All inputs are synthetic and programmatically generated. Real retrieval settings, where distractors are not fixed offsets of ±1 to ±3, are named as future work.

## Limitations found by others

## What it leaves untried
- One threshold shared across tasks, or chosen without labelled development data. Per-task τ needs 20 labelled paired problems for every new decision type, which a deployed workflow may not have.
- Real retrieved candidate sets. Distractor distance strongly changes Menu rejection (20% at error 1–5 vs 88% at 195–200), so results on fixed small offsets may not hold for real distractors.
- A deterministic compute-then-lookup pipeline as a baseline. The paper itself shows that supplying the result gives 100% rejection, but it does not compare that remedy against thresholding on cost or coverage.

## Topics
[[Topic - decision models]] · [[Topic - abstention and fallback]] · [[Topic - judge and decision-model audits]]
