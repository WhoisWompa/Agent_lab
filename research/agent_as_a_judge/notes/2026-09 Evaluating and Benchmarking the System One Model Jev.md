---
title: "Evaluating and Benchmarking the System One Model Jev"
authors: Tobias Deußer et al.
date: 2026-09
arxiv: 2609.37647
url: https://arxiv.org/abs/2609.37647
venue: arXiv
category: agent-evaluation-benchmarks
pdf: agent as a judge papers/decision models/open models/evaluations/Evaluating and Benchmarking the System One Model Jev (Deusser 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "evaluations"]
topics: ["decision models", "judge and decision-model audits", "calibration"]
---
# Evaluating and Benchmarking the System One Model Jev

## One line
The first independent public-benchmark evaluation of Jev, a commercial non-generative "System One" decision model, checking its accuracy, the vendor's calibration claim, and where it fails, against two open-weight LLMs scored on identical requests.

## Method
The problem: generative LLMs are now used for small pipeline decisions (routing, moderation, grounding checks, rubric scoring), where the answer must be parsed from text and its probability is usually unavailable or unreliable. Jev instead answers typed questions about a state with three primitives: Choice (one of up to 255 options, with a probability per option), Score (a position on a 2 to 10 level rubric, returned as a probability-weighted level), and Noul (P(yes) for a statement). The vendor calls these probabilities calibrated, but no systematic evaluation existed.

The paper's idea is to map 37 public datasets onto these three primitives, with one frozen template per dataset, no prompt tuning and no examples, and to make the comparison fair by giving open LLMs the same interface: each option gets a single-token code, and one forward pass gives the model's exact next-token distribution over the codes, renormalized into option probabilities like Jev's. This turns the open models into a control: if a pattern appears in Jev but not in them on identical requests, it is specific to Jev. That control is used to probe contamination on MMLU, since Jev's training data are not public.

## Evaluated on
- Jev beats a larger open model on most decisions, and does it cheaply: ahead of Qwen3.8-27B on 27 of 37 datasets (11 with non-overlapping 95% intervals, none of Qwen's 9 leads), ahead of Gemma-4-E4B on all 37; 346,009 requests cost US$9.15 at 0.36 s mean latency.
- Choice probabilities are well calibrated: pooled ECE 0.028 vs 0.063 for Qwen and 0.208 for Gemma; residual miscalibration is overconfidence on 20 of 22 datasets and tracks low accuracy (rho = -0.83).
- Confidence supports gating: answering only the most confident 50% lifts Banking77 from 79.7% to 96.3% and SIB-200 from 81.5% to 98.2%.
- Binary probabilities rank well but sit badly against 0.5: prompt-injection recall is 50% at AUROC 0.982; multi-label Nouls predict mean P(yes) 0.209 against an observed 0.041. Thresholds tuned on 1,000 training examples raise UNFAIR-ToS micro-F1 from 0.499 to 0.748.
- As a rubric judge of generated text it is weak and no better than Qwen: SummEval mean rho 0.554, HelpSteer2 0.412, with helpfulness (0.399) and correctness (0.369) lowest; Qwen is higher on 9 of 12 rubric dimensions.
- Possible MMLU contamination: Jev scores calculation-heavy MMLU subjects higher than the rest (94.3% vs 91.3%) while both open models find them harder (Qwen 74.7% vs 83.0%), as do all three on C-Eval. Rotating options leaves it at 94.3%, ruling out shallow memorization only.

## Limitations admitted by the authors
- One untuned template per dataset; weak results such as AGB-DE (F1 0.204) and HelpSteer2 may partly reflect wording.
- The open baselines use prompts written for Jev and no thinking; letting them reason would likely raise their accuracy, so the "Jev beats Qwen" result holds only for single-pass scoring.
- No generative proprietary models are compared, so Jev is placed against only two open-model points; Jev's size, architecture and data are unknown, so gaps cannot be attributed to anything.
- The memorization probes rule out only memorized answer positions and option sets, not memorized question-answer pairs, so the MMLU result stays unexplained and other long-established English benchmarks are to be read with caution.
- Each request ran once; run-to-run variance is unmeasured.

## Limitations found by others

## What it leaves untried
- Perturbing the questions themselves (e.g. changing the numbers in MMLU calculation items), which the authors name as the decisive contamination test; without it, Jev's strongest-looking results cannot be trusted.
- A relevance-judgment task, though Score is a natural fit for graded relevance labels.
- Fixing the multi-label over-prediction at the source, e.g. asking all labels in one Choice or conditioning Nouls on each other, rather than only tuning thresholds, since each Noul is answered in isolation and "has no notion that only one or two of 28 emotions usually apply".

## Topics
[[Topic - decision models]] · [[Topic - judge and decision-model audits]] · [[Topic - calibration]]
