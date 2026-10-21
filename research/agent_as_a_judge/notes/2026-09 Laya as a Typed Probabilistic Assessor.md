---
title: "Laya as a Typed Probabilistic Assessor: An Independent Reproduction and a Preregistered Study of Calibration and Selective Escalation"
authors: Gowthamkumar Nandakishore
date: 2026-09
arxiv: 2609.33843
url: https://arxiv.org/abs/2609.33843
venue: arXiv
category: trained-judges-reward-models
pdf: agent as a judge papers/decision models/open models/papers/Laya as a Typed Probabilistic Assessor - Independent Reproduction and Calibration Study (Nandakishore 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "papers"]
topics: ["decision models", "judge and decision-model audits", "calibration", "confidence-gated escalation"]
---
# Laya as a Typed Probabilistic Assessor: An Independent Reproduction and a Preregistered Study of Calibration and Selective Escalation

## One line
An independent, preregistered study showing the open 421M Laya typed-decision assessor reproduces its card's accuracy but ships uniformly under-confident, one fitted temperature fixes most of that, and its confidence gate beats random escalation but misses a 10% error target.

## Method
The problem: a small open encoder (ModernBERT-large) returns a label distribution for typed questions over workflow state (agent traces, invoices, security alerts), meant as a cheap first-stage judge that accepts when confident and escalates when unsure. Accuracy says nothing about whether that confidence can drive a gate, and the card admits it is uncalibrated: temperatures fitted on training data, then overridden by an inherited table.

The contribution is a measurement, not a new judge:
- **Direction of miscalibration, not just ECE.** The signed gap (mean confidence minus accuracy) is reported with ECE. An over-confident judge passes errors through a gate; an under-confident one over-escalates and erodes the cost case. Two models with ECE 0.21 can fail in opposite directions.
- **Repair by one scalar.** If the shipped table causes the miscalibration, one temperature fitted on held-out data should remove it without changing the ranking of confidences.
- **Gate = calibrated max-probability ≥ τ**, τ being the smallest threshold with fitting-split accepted error ≤ 0.10. With no strong judge runnable, end-to-end accuracy is an oracle bound, compared with random escalation at the same rate.
- **Two tracks against contamination.** The released model saw all training data, so Track A fits on half the test set and evaluates on the other; Track B retrains from the base on clean splits, which also prices fitting temperatures on trained-on data.

## Evaluated on
- **Headline reproduces, except soft accuracy:** accuracy 0.767 vs. card 0.766; soft accuracy 0.509 vs. reported 0.471, with the interval excluding the card's number.
- **Shipped model is under-confident everywhere:** signed gap −0.214 (confidence 0.553 vs. accuracy 0.767); every reliability bin sits above the diagonal.
- **One temperature fixes it, and the shipped table points the wrong way:** fitted T = 0.469 (sharpening) takes held-out ECE 0.204 → 0.037 and NLL 0.703 → 0.536; the shipped table softens with T = 1.25–1.98.
- **Confidence carries real but limited signal:** the gate adds +6.5 (Track A) and +7.6 (Track B) accepted-set accuracy points over random escalation, but accepted error is 0.140 out of sample against the 0.10 target (0.092 on the fitting split). Calibration barely changes ranking: error-detection AUROC 0.766 → 0.780.
- **Contamination has a price:** fitting temperatures on trained-on items inflates held-out ECE 3.7× (0.024 → 0.087).
- **No out-of-distribution transfer:** on a claim-verification probe accuracy is 0.617 (0.858 in-distribution), a third of unsupported claims are accepted, and no threshold reaches the 10% target.

## Limitations admitted by the authors
- Every score is agreement with a synthetic ~4B teacher, not correctness. The model's 0.767 is above the teacher's own self-agreement ceiling (0.735), which the dataset card reads as learning the teacher's quirks.
- The frozen selection rule picked isotonic regression, which overfit on 200–240 cases on both tracks (Track A held-out NLL 0.774 vs. 0.703 uncalibrated), so the calibration hypothesis fails though every temperature method works.
- The threshold miss comes from fitting calibrator and τ on the same decisions: τ = 0.70 already had a fitting-split upper bound of 0.116, above its target.
- High-confidence errors survive the gate: 26 of 177 accepted security decisions are wrong (14.7%), one at calibrated confidence 1.0 against a unanimous label.
- The human-adjudicated external set was dropped; the OOD probe is small (120 claims) and self-authored, a signal rather than a measurement.
- No escalation target was run and JEV never accessed, so cascade accuracy and cost are only bounds.
- About 0.08 of headline accuracy depends on skewed label priors: reweighting to uniform labels drops accuracy from 0.772 to 0.688.

## Limitations found by others

## What it leaves untried
- Cross-fitting calibrator and threshold, or picking τ by an upper confidence bound: a post-hoc check of the latter gives 0.101 error at coverage 0.534, but it was never tested prospectively.
- Running a real escalation target, to turn the oracle bound and symbolic cost into actual cascade numbers.
- Human labels instead of the teacher, the only way to tell whether beating the teacher ceiling is correctness or imitation.

## Topics
[[Topic - decision models]] · [[Topic - judge and decision-model audits]] · [[Topic - calibration]] · [[Topic - confidence-gated escalation]]
