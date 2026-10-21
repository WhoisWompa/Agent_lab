---
title: "StartLux-Decision: AutoThink Decision Models with Reinforcement Learning for Calibrated Deliberative Decisions"
authors: Xialie Zhuang et al.
date: 2026-10
arxiv: 2610.17309
url: https://arxiv.org/abs/2610.17309
venue: arXiv
category: trained-judges-reward-models
pdf: agent as a judge papers/decision models/open models/papers/StartLux-Decision - AutoThink Decision Models with RL for Calibrated Deliberative Decisions (Zhuang 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "papers"]
topics: ["decision models", "open decision models", "adaptive reasoning depth", "calibration"]
---
# StartLux-Decision: AutoThink Decision Models with Reinforcement Learning for Calibrated Deliberative Decisions

## One line
A family of open decision models (0.8B to 27B) that answer typed questions in one forward pass and stop to reason only when unsure. Reasoning is trained with RLCD 2, which rewards the gain in proper-score quality of the decision probability and penalizes overlong traces.

## Method
- **Problem.** Open decision models (routers, verifiers, tool-call checkers) read option probabilities from logits in one pass. That is fast, but it fails on decisions that need computation, such as arithmetic, schedules or rule exceptions. The authors also find that decision training damages reasoning. Prompted to reason, their 4B model writes little or nothing on about 40% of questions, and their 9B model runs to the length limit on about 70%.
- **Instant.** Single-pass readout over option letters, with bidirectional attention in the full-attention layers. Earlier prompt tokens can then see the question and options that come after them. In a controlled comparison this adds up to 2.4 DI points, at four of five scales.
- **AutoThink (Read-or-Think).** The model first reads a probability p0. If the top probability is at least 0.9, it answers at once. Otherwise it reasons for up to 4,096 tokens, reads p1, and returns 0.25·p0 + 0.75·p1. The 0.75 weight was picked to minimize Brier score on held-out data, not to maximize accuracy.
- **RLCD 2.** The reward for a reasoning trace is S(p1) − S(p0) − λ·max(0, |τ| − B). A frozen copy of the starting model produces both p0 and p1. S is a strictly proper, decision-weighted score whose weight is a mix of uniform and Beta(8,2), so it focuses on errors at high confidence. The idea is to reward reasoning for how much it improves the probability, not just for getting the answer right. The soft budget B (3,072 at release) pushes against runaway loops without cutting traces off hard. Training uses only questions below the 0.9 gate, matching how the model is used at inference.
- **Policy-aware calibration.** Selection and routing change what a confidence number means. Choosing the best of N candidates favors scores that came out high by chance, the optimizer's curse. The paper proves that accuracy at a fixed score cannot rise with N. The fix is to fit calibration maps on the outputs the deployed policy actually returns, conditioned on the routing or selection statistics, and to certify thresholds separately for each route.

## Evaluated on
- **RLCD 2 fixes termination without losing accuracy.** At 9B, termination rises from 45.9% to 93.9% and mean trace length drops 65% (2,494 to 868 tokens). Held-out accuracy moves from 80.38 to 80.48. On DecisionPivot, 9B pair accuracy rises from 53.3% to 59.9%.
- **The length penalty drives termination, the proper score drives calibration.** With the predictive reward replaced by random noise, the length penalty still gets nearly every trace to terminate. Proper-score rewards beat accuracy-only rewards on calibration.
- **Reasoning pays on computation.** On DecisionPivot, AutoThink beats Instant by 11.5 to 18.4 pair-accuracy points, and the 27B model reaches 86.9% against GLM-5.3's 82.2%. On the items routed to reasoning, 27B accuracy rises from 57% to 93%, with 1,783 errors fixed and 94 new ones introduced.
- **Strong DI results, but the public DI subset was the development set.** Instant beats the best model of the same size by 7.4 to 16.9 points on the public DI 0.3 subset.
- **Policy-aware calibration works.** Across 184 pipeline settings, signed gaps shrink from [−11.7, +20.5] to [−2.7, +2.1] points. Thresholds certified on single predictions miss the 5% error target in 44 of 67 best-of-16 pairs. Thresholds certified on the policy's outputs miss it in 0.

## Limitations admitted by the authors
- The public DI subset steered data recipes, attention choice and seed averaging. DI scores therefore "reflect model selection and are not independent test results". Only DecisionPivot is independent, and it comes from the same authors.
- Gains stay within task families seen in training. Stage 2 data lifts the matching tasks by 8.6 points and the others by 0.3.
- A tight budget hurts long computations. With a 2,048 budget, 4B loses 5.9 points on items that used 2,048 to 4,095 tokens before RL. At the released 3,072 budget it still loses 4.2.
- Policy-aware maps do not survive distribution shift: up to 6.1 points of residual overconfidence on unseen datasets. Any change in N, routing rate, generator or task family needs recalibration.
- After reasoning the model is overconfident. The 4B post-reasoning readout is 4.0 points overconfident even though its single-pass readout is well calibrated. At a 5% error target only 2% of its default answers can be accepted.
- The 0.9 gate is fixed. The paper's own Proposition 5 says the optimal gate is "reason when expected score gain exceeds cost", and it states the fixed threshold is not shown to be optimal.
- AutoThink can be worse than Instant: 11.8 points lower on MuSR at 27B. The paper partly attributes this to causal attention.

## Limitations found by others

## What it leaves untried
- **A learned gate.** Proposition 5 already defines the gate as expected score gain minus reasoning cost. Training a head to predict that value would replace the fixed 0.9 threshold. That threshold sends 61% of DecisionPivot items to reasoning based on confidence alone, with no estimate of whether reasoning will help.
- **Rewards from a moving scorer.** p0 and p1 come from a frozen starting model, so the reasoning policy is tuned to a scorer it never updates. A scorer that is trained jointly or refreshed periodically is not tested.
- **An outside benchmark.** The authors built both the development set and the only independent test (DecisionPivot), so an external benchmark is needed before the gains can be trusted beyond the authors' own benchmark families.

## Topics
[[Topic - decision models]] · [[Topic - open decision models]] · [[Topic - adaptive reasoning depth]] · [[Topic - calibration]]
