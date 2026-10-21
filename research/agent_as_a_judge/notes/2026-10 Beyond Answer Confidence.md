---
title: "Beyond Answer Confidence: A Controlled Audit of Self-Knowledge in a Black-Box Decision Model"
authors: Sharath M Shankaranarayana et al.
date: 2026-10
arxiv: 2610.01006
url: https://arxiv.org/abs/2610.01006
venue: arXiv
category: llm-judge-foundations
pdf: agent as a judge papers/decision models/open models/evaluations/Beyond Answer Confidence - Controlled Audit of Self-Knowledge in a Black-Box Decision Model (Shankaranarayana 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "evaluations"]
topics: ["decision models", "judge and decision-model audits", "calibration"]
---
# Beyond Answer Confidence: A Controlled Audit of Self-Knowledge in a Black-Box Decision Model

## One line
Shows the decision model Jev's calibrated confidence does not signal missing knowledge, while yes/no questions about the case (settled? enough evidence?) do and "do you know?" mostly reads surface cues.

## Method
The problem: decision models like Jev return probabilities meant for routing and abstention, and the vendor claims confidence predicts accuracy. But a calibrated 0.5 can mean a fair coin or an unknown fact, and one output distribution cannot be split into aleatoric and epistemic parts, so calibration does not show whether confidence falls when the model is out of its depth.

The idea: test it behaviourally. Hold an item fixed and vary only what the model is told, or probe a knowledge boundary (made-up entities, news after an observed accuracy break). Uncertainty that reports missing knowledge should pass five checks: evidence lowers entropy, no information gives near-uniform output, irrelevant text changes nothing, calibration holds at every knowledge level, and some separate query tells missing knowledge from chance (C5). For C5, each call also asks three yes/no follow-ups: `settled` (is the outcome already fixed?), `enough` (does the context suffice?) and `known` (do you know the answer for certain?). The key addition is surface-cue controls (text-only classifiers, realistic look-alike names, date removal), so a follow-up that "detects" a gap is not just reading the wording. Failing a check shows a limitation; passing proves no internal epistemic state.

## Evaluated on
- Confidence is calibrated on familiar closed-choice tasks: SmoothECE 0.015-0.025 on CLINC150 with examples or names, 0.016 on MMLU-Redux.
- With no information it backs a salient guess instead of being uniform: 0.80 on "one" for a fair die in every option order, 0.52 on one option for fabricated entities (uniform reference 0.25); the open GLiNER2.5-Decide is nearly uniform on the same inputs.
- Past the knowledge boundary confidence rises (0.75 to 0.82) while accuracy falls to chance; Jev answers "no" to 92% of post-boundary news against a true 51.5%, and recalibrating on earlier months still leaves 0.19-0.23 overconfidence.
- Case questions work: `settled` separates fixed-unknown facts from future draws at AUROC 1.00; `enough` detects incomplete evidence at 0.95 vs 0.85 for confidence, and keeps 0.95 within length strata where length drops to 0.48.
- `known` looks strong (0.91 on fabricated entities and post-boundary news) but collapses under cue controls: text alone separates pseudo-words at 1.00 and periods by date at 0.997; with look-alike names `known` falls to 0.74 (answer uncertainty 0.76), with dates removed to 0.58 (vs 0.56).
- For stated odds, Choice puts 0.98 on a 40% outcome; asking one yes/no per outcome lands within 0.030 of stated chance, 0.012 after rescaling to sum to one.

## Limitations admitted by the authors
- One version of one closed model; no other system ran the full protocol.
- The knowledge boundary is an accuracy change point in news (around late 2024), not a verified training cutoff.
- Date removal can change the proposition or lose which event is meant: in a 240-pair sample, 30 of 112 "yes" questions lost event identity (single AI annotator), so only response changes are reported.
- A text classifier at chance does not certify that no cue remains, and `enough` was checked against length features only.
- Follow-up answers are validated as rankings, not calibrated probabilities; absolute levels vary across fourteen rewordings, so thresholds must be set per wording.
- The "not known" option's value depends on prevalence: +0.05 accuracy when half the questions are past the boundary, -0.03 at 5%, and a rule skipping the most recently dated questions trails it by only 0.01-0.02.
- Cue controls and the equivalence margin were added after the main studies and not confirmed on a fresh panel.

## Limitations found by others

## What it leaves untried
- Running the same protocol on other decision models and judge LLMs; GLiNER2.5-Decide already behaves differently with no information.
- Testing the follow-ups in an actual judge or routing pipeline with costs and realistic prevalence; on ordinary questions `enough` filtering is 2-6 points less accurate than confidence at equal coverage.
- A self-knowledge probe that survives cue controls; beyond `known` and a second-look check, none is tried.

## Topics
[[Topic - decision models]] · [[Topic - judge and decision-model audits]] · [[Topic - calibration]]
