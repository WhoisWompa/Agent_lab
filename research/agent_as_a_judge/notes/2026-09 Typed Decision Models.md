---
title: "Typed Decision Models: An Early Evidence Audit and Evaluation Checklist"
authors: Lijuan Tang et al.
date: 2026-09
arxiv: 2609.32160
url: https://arxiv.org/abs/2609.32160
venue: arXiv
category: llm-judge-foundations
pdf: agent as a judge papers/decision models/open models/evaluations/Typed Decision Models - An Early Evidence Audit and Evaluation Checklist (Tang 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "evaluations"]
topics: ["decision models", "judge and decision-model audits"]
---
# Typed Decision Models: An Early Evidence Audit and Evaluation Checklist

## One line
Audits the 28 papers that appeared in the first nine days after Jev's release, finds that the typed readout itself has shown no accuracy advantage over ordinary label-probability readouts, and turns the corpus's recurring flaws into a 14-item evaluation checklist.

## Method
The problem: a burst of papers claimed Jev (a hosted "typed decision model" that returns a probability distribution over caller-declared options, no text) matches or replaces LLMs, but nobody had asked which gains come from the interface and which from the model, the test, or the serving setup. The paper defines a TDM by three properties: support closed at request time over caller-supplied options, many isolated questions answered about one state in one pass, and the probability as the product meant to be thresholded or routed on. It then traces every component to an ancestor (label-probability classification, constrained decoding, yes/no rerankers, rubric judges, reject options and cascades). The claim is that what is new is the packaging, not the mechanism, so the right test of any TDM gain is a matched label-log-probability baseline on the same backbone. Applications are sorted by role (step replacement, controller, judge/screener, measurement instrument) and by where low-confidence cases go, because that decides the right baseline: a classifier if nowhere, a cheap generative cascade if to a stronger model, held-out calibration plus a review budget if to humans.

## Evaluated on
- The typed readout adds no accuracy where tested: 21 of 27 model-evaluating papers have no label-probability baseline; in those that do, a typed head and a plain LM head both give .761 macro accuracy, and AUROC is .974 vs .950 (not significant); restricted option logits equal greedy generation whenever generation is valid.
- Parity claims sit on saturated tests (100/100 on 20 items, 63/63 contract checks), while on discriminating tests Jev trails stronger models: 14.6 points on JudgeBench, 19.8 on hard RM-Bench, a median 11.6 macro-F1 in social-science annotation.
- Cost and latency gains are real but conditional: fees tens to hundreds of times lower, yet caching shrinks one latency advantage to under 1 ms, and the same group reports Jev 70% cheaper in one paper and 1.7x more expensive in another.
- Calibration is workload-specific: pooled ECE 0.047 hides a median per-benchmark ECE of 0.168; one study finds calibration slope 1.63 and recalibration cuts error 3.3x; wrong tool calls carry mean confidence .778.
- Escalation is bounded by shared errors: LLM judges repeat Jev's wrong answer in 96% of its most confident errors, so a cascade gains at most 1.5 points over the best single judge; against a cheap generative cascade on external tau2-bench, the TDM cascade is more expensive and not more accurate.
- Checklist compliance is low: 5/26 include a label-probability baseline, 1/5 a cheap generative cascade, 1/27 an option-name swap test, 3/20 latency with and without caching.

## Limitations admitted by the authors
- The corpus covers nine days and essentially one hosted version (jev-1.13), so nothing can be said about cross-version stability or the model class at large.
- Jev is closed, so mechanism claims rest on open replications that may not describe the hosted model.
- arXiv-only keyword search underrepresents industrial experience and may miss similar interfaces not named after Jev.
- Five of the 14 checklist items (e.g. post-hoc design choices, data provenance, model version) could not be scored reliably and are left blank, so the compliance picture is partial.
- Extraction was LLM-assisted; a blind second pass found two factual errors, which were corrected, but residual error is possible.

## Limitations found by others

## What it leaves untried
- The matched-cost ablation it proposes but does not run: same open backbone with no task training, ordinary label-probability fine-tuning, and calibration-oriented decision training, which would finally separate RLCD from data and scale.
- A shared non-saturated benchmark varying option count, questions per state, share of easy items and fallback cost, to say when a TDM cascade beats a cheap generative one; currently one study answers this, and its answer flips across benchmarks.
- Testing the vendor's two-stage procedure for high-cardinality choices (up to 255 options), which no corpus paper measures.

## Topics
[[Topic - decision models]] · [[Topic - judge and decision-model audits]]
