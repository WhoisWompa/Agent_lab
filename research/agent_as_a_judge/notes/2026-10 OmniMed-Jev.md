---
title: "OmniMed-Jev: Calibrating LVLM Confidence for Trustworthy Medical Multimodal Decisions via System One"
authors: Luyao Tang et al.
date: 2026-10
arxiv: 2610.00381
url: https://arxiv.org/abs/2610.00381
venue: arXiv
category: trained-judges-reward-models
pdf: agent as a judge papers/decision models/open models/papers/OmniMed-Jev - Calibrating LVLM Confidence for Medical Multimodal Decisions (Tang 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "papers"]
topics: ["decision models", "open decision models", "calibration"]
---
# OmniMed-Jev: Calibrating LVLM Confidence for Trustworthy Medical Multimodal Decisions via System One

## One line
Fine-tunes MedGemma-1.5-4B to return a distribution over a runtime candidate set instead of answer text, and shows its reported confidence tracks correctness far better than a matched generative baseline at similar accuracy.

## Method
- **Problem.** Medical multimodal models serialise diagnoses, findings, counts and measurements as text, so their probability is about the next token, not the decision. Recovering a decision probability is an extra inference step the model was never trained for; the cited medical literature finds such confidence overstates accuracy and breaks deferral policies.
- **Idea.** Every output is a typed decision over explicit candidates: Choice (one class, e.g. differential diagnosis), Noul (yes/no per finding), Score (distribution over an ordered value grid, point estimate = expectation).
- **Mechanism.** Question and candidates are written into the context, each candidate ending in a marker token; one shared head scores the hidden state at each marker with the state representation, softmax over candidates, no vocabulary projection. Because candidate text is input, the model must read the option rather than learn label positions (Choice/Noul options shuffled each epoch; Score grids fixed since position is value). One image is encoded once and all its decisions come out in one pass, trained with cross-entropy per decision.
- **Why it should work.** The decision distribution is the training objective, so calibration is trained and measured directly rather than repaired post hoc. The interface adds no information; it changes what the model is trained to report.
- **Assumes** enumerable candidate sets; free-text reports and boxes are out of scope.

## Evaluated on
- **Calibration much better on the same backbone, data and schedule.** ECE baseline vs OmniMed-Jev: 0.26 vs 0.08 classification, 0.30 vs 0.01 multi-label, 0.42 vs 0.04 counting, 0.13 vs 0.09 regression (3x to 26x).
- **Reliability error falls 9x, 44x, 126x in three families, only 1.3x in regression.** The baseline's reliability error exceeds its resolution in three families: it ranks usefully but its numbers are wrong.
- **Confidence finds errors.** Multi-label AURC 0.2474 to 0.0126 (20x); regression unchanged (0.228 vs 0.227).
- **No accuracy gain.** Classification balanced accuracy 0.69 vs 0.65, paired 95% interval [-0.02, +0.11], McNemar p = 1.00; multi-label and regression intervals include zero too. The only significant gap favours the baseline: counting MAE 2.14 vs 2.52.
- **Reads option meaning, not position.** Shuffling candidates leaves classification answers 0.90 unchanged; two-option restriction scores 0.87 against 0.50 chance.

## Limitations admitted by the authors
- **Interface effect is confounded with denser supervision and the extra head.** Factorising annotations gives 155,729 targets from the same 23,558 images the baseline sees as 23,558 answers; the separating ablation was not run.
- **Baseline probabilities are a reconstruction.** Candidate log-likelihoods normalised after the fact; asking the baseline to state a probability parsed in 0 of 726 rows. On counting its top candidate is never correct (0 of 126), forcing AURC to 1.0, so that gap partly measures the reconstruction.
- **Counting accuracy suffers.** The grid expectation pulls extreme counts to the centre (mean prediction 1.13 below gold). Headline counting calibration includes 75 near-deterministic cell-type decisions; total-count top-1 accuracy alone is 0.15, not 0.32.
- **Retrospective, same-source test.** 726 states from the training sources; per-class, per-source and out-of-distribution calibration unmeasured, so nothing shows it holds under shift. Not evidence of clinical readiness.
- **The "none" option is inverted.** An added "none" candidate gets more mass on correct decisions (0.40) than wrong ones (0.17), error-detection AUC 0.13; unexplained.
- **Checkpoint picked on OmniMed-Jev's validation.** Regression ECE worsens to 0.19 by the final step, and the baseline's calibration was measured only at that one step.

## Limitations found by others

## What it leaves untried
- **Downsample multi-label decisions to the baseline's count** to see whether the calibration gain comes from the interface or from about 6.6x more targets, the paper's main confound.
- **Compare against temperature scaling or a calibration-aware generative objective.** Called complementary, but untested, so it is unknown whether a cheap fix closes most of the ECE gap.
- **Calibration under shift and per subgroup**, where its own related work says medical calibration breaks (class-dependent miscalibration harming abstention).

## Topics
[[Topic - decision models]] · [[Topic - open decision models]] · [[Topic - calibration]]
