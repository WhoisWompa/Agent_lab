---
title: "TypedBench: A Benchmark for Calibration, Framing Sensitivity, and Cost in System One Decision Models"
authors: Rahul Sharma et al.
date: 2026-10
arxiv: 2610.11392
url: https://arxiv.org/abs/2610.11392
venue: arXiv
category: agent-evaluation-benchmarks
pdf: agent as a judge papers/decision models/open models/evaluations/TypedBench - Calibration, Framing Sensitivity, and Cost in System One Decision Models (Sharma 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "evaluations"]
topics: ["decision models", "judge and decision-model audits", "calibration", "presentation sensitivity"]
---
# TypedBench: A Benchmark for Calibration, Framing Sensitivity, and Cost in System One Decision Models

## One line
A contamination-resistant benchmark that tests whether typed decision models (hosted Jev, open Laya encoder, open Kev decoders) give probabilities software can act on, judged by wording stability, calibration against a noise floor, and decision cost.

## Method
System One models take a state and typed questions (choice, ordinal score, yes/no) and return a probability vector in one pass, with no text. Their pitch is calibrated probabilities that software can threshold or route on. Existing evidence does not test this. Jev's own evaluation compares against two frontier LLMs, not ground truth. Laya's results use a checkpoint fine-tuned on the benchmark's training split. Public results sit on pretraining-contaminated datasets.

The idea has three parts:
- **Policy-derived labels.** Seven generators tag each template with facts and compute the label by running the rule stated in the question. Fresh items cannot be memorised, so accuracy measures rule application, not recall. Paired control arms change one thing per item (unknowable context, label noise, distractors, withheld option, surface noise).
- **Calibration against a null.** ECE is divided by the ECE a perfectly calibrated model with the same confidences would show by chance. About 1 to 1.5 means calibrated. This is needed because at n=500 the floor ranges from 0.002 to 0.049, so raw ECE cannot be compared across questions.
- **Judge probabilities by decisions.** Under an asymmetric cost matrix, the cost of taking the top answer (argmax) is compared with the choice that minimises expected cost (Bayes). Accuracy is reported as a range over paraphrases.

## Evaluated on
- **Wording moves the strongest model most.** On ticket priority, Jev's accuracy spans 24 points across friendly rewordings of the same rule (0.708 to 0.946, median 0.874). A paraphrased negation ("Is it safe to treat this message as genuine?") costs Jev 23 points on phishing.
- **No model is calibrated, and the direction varies.** ECE is above its null almost everywhere (Jev: 2.2x on priority, 4.3x on phishing). Jev is under-confident on every core ticket and phishing question (all refitted temperatures below 1). The encoder is over-confident on its errors. Yet Jev still ranks its own errors best (lowest AURC).
- **Confidence is not evidence-driven.** With the tier line removed, two priority levels fit equally well. Jev still puts 0.89 mass on one level, while the decoders split theirs (0.28 to 0.51).
- **Acting on probabilities can cost more.** On priority (under-prioritising costs 2x), Bayes roughly doubles Jev's cost (1,080 to 2,300 per 10^4) and raises Kev-9B's (4,780 to 7,960). It saves cost for weaker models (Kev-4B: 8,980 to 5,000). On phishing, Jev's under-confidence makes Bayes flag 498 of 500 emails.
- **Architectures fail on different axes.** The encoders collapse before 100 options and barely beat the majority prior on priority (0.34 to 0.38 against 0.34). The decoders slow down as questions are added (3.5 s for 9B at 21 questions against 245 ms for Jev).

## Limitations admitted by the authors
- States are templated, not native text. That is why a fine-tuned DistilBERT scores 1.000 on every question, so results may not carry over to real traffic. A human-labelled native-text tier is proposed but not built.
- Separation between strong models rests on one kind of question: rule application, mainly ticket priority. Most other questions are saturated for Jev and the larger decoders. Multi-step rules, numeric conditions, conflicting evidence and graded answers are left for future generators.
- Template spaces are finite (about 590 distinct phishing texts). Jev's phishing cost loss loses significance when whole templates are resampled, because it comes from one template.

## Limitations found by others

## What it leaves untried
- **Recalibration per question.** The paper says calibration must be fixed per model, primitive and question, but never fits a recalibrator and re-runs the cost test. That would show whether Bayes's loss for Jev and Kev-9B disappears, and whether the evidence-blind confidence (0.89 on unknowable items) survives it.
- **Real traffic.** Generated items are never checked against real, human-labelled traffic, so it is unknown whether the 24-point wording range holds on native text.
- **A routing policy that counts request cost.** Escalating a third of answers still sends every request to the hosted model, and a one-question call costs over 40% of a full one. No escalation policy that counts cost per request is tried.

## Topics
[[Topic - decision models]] · [[Topic - judge and decision-model audits]] · [[Topic - calibration]] · [[Topic - presentation sensitivity]]
