---
title: "Calibrated Decisions at Scale: Converting Police Crash Narratives into Probabilistic Crash Variables with a System One Model (Jev)"
authors: Amir Rafe et al.
date: 2026-09
arxiv: 2609.24052
url: https://arxiv.org/abs/2609.24052
venue: arXiv (preprint submitted to Elsevier)
category: llm-judge-foundations
pdf: agent as a judge papers/decision models/Calibrated Decisions at Scale - Crash Narratives with a System One Model, Jev (2026).pdf
folder: ["agent as a judge", "decision models"]
topics: ["decision models", "judge and decision-model audits", "calibration", "confidence-gated escalation"]
---
# Calibrated Decisions at Scale: Converting Police Crash Narratives into Probabilistic Crash Variables with a System One Model (Jev)

## One line
An independent audit of Jev, a typed decision model that returns probabilities and no text, coding Texas crash narratives at population scale: its probabilities rank well but overstate prevalence until a two-parameter map fitted on a few thousand human labels fixes them, and the calibrated probabilities become a per-variable human-review budget.

## Method
**Problem.** Coding narratives with frontier LLMs costs too much at corpus scale, needs output parsing, and gives verbalized confidence that is generated text rather than a measured probability, so nothing says how much output a person must check.

**Idea.** Code each narrative as 27 typed questions in one call, with detail questions read only when their presence question exceeds 0.5. A frozen System One model answers with probabilities, so no answer is invalid. The probabilities are audited, not trusted, and the only fitted object is a per-variable Platt map (intercept and slope). Three constructions carry the audit:
- **Resolution floor (Prop. 1).** On a discrete grid whose smallest positive value is δ, with no mass on zero, a variable with base rate ρ < δ cannot be calibrated: mean probability overstates prevalence and ECE ≥ δ−ρ, whatever the ranking. Jev's grid is 0.01 to 1.00 and it returned zero 0 times in 2.4M answers.
- **One-sided reference noise (Lemma 2).** If coded fields only omit factors, the reliability curve against them lies at or below the true one.
- **Review budget over flags.** With rare positives a flag-nothing rule already has risk ρ, below a 5% target, so accuracy-based selective risk certifies no review. The budget H(π*) is instead the share of flagged records that cannot be auto-accepted at target precision π*, cross-fitted (threshold chosen on one half, certified on the other).

## Evaluated on
- **Cheap, since cost tracks schema size (122 tokens per question vs about 89 per median narrative):** 195,857 narratives for $30.22 ($0.154 per 1,000); $774 projected for 5.0M, against about $39,875 for a mid-tier frontier model at list price (52x).
- **Accurate, not calibrated:** F1 0.908 against 2,416 human labels, but mean probability 4.8% against a 2.7% base rate, slope 1.63, Spiegelhalter z −5.3.
- **Recalibration fixes it:** out-of-fold ECE 0.0231 to 0.0069 (3.3x), slope to 0.97.
- **Coded fields understate agreement, not calibration:** κ against them is lower than against humans on 9 of 9 variables by a median 0.26 (drugs 0.48 vs 0.96), while the ECE ratio between references has median 1.0.
- **Calibration is per model:** one frontier arm is more accurate (F1 0.967) but worse calibrated (slope 2.55); the other is calibrated (ECE 0.0027) but no more accurate (F1 0.885).
- **Budget:** held-out H(0.90) is 0.8% of flags at delivered precision 0.906; against coded fields it saturates at 100% for 8 of 9 variables.

## Limitations admitted by the authors
- Four variables fail (F1 < 0.70) and threshold retuning gains under 0.05 on every stable variable; frontier arms recover three of them, so the fault is this model with this schema.
- The human reference covers only clear cases; counting the 49 dropped pairs as errors lowers F1 to 0.875 and raises the budget to 6.9%.
- Some rare variables have only 5 positive labels, so their thresholds are noise and 5 variables cannot get their own map.
- Weights come from a greedy draw with no known inclusion probabilities, valid only if labeling is uninformative within a cell.
- Jev is closed and vendor-versioned, so the audit is perishable; a map fitted at one base rate must be refit, not transported.
- Option-order and wording effects were not tested; the claim is output validity only.

## Limitations found by others

## What it leaves untried
- Distribution-free risk control (conformal risk control, Learn-then-Test) for the threshold: named but not applied, so the budget is an estimate with an interval, not a guaranteed precision.
- Rewritten criteria for the four failing variables, scored on a fresh reference set, the direct test of the model-schema explanation.
- Repeating the audit across Jev versions and against frontier logit probabilities rather than verbalized ones, to separate interface from model.

## Topics
[[Topic - decision models]] · [[Topic - judge and decision-model audits]] · [[Topic - calibration]] · [[Topic - confidence-gated escalation]]
