---
title: "Confident Rankings with Fewer Items: Adaptive LLM Evaluation with Continuous Scores"
authors: Esma Balkır et al.
date: 2026-01
arxiv: 2601.13885
url: https://arxiv.org/abs/2601.13885
venue: arXiv
category: agent-evaluation-benchmarks
pdf: agent as a judge papers/stopping rules/Confident Rankings with Fewer Items - Adaptive LLM Evaluation with Continuous Scores (Balkir 2026).pdf
folder: ["agent as a judge", "stopping rules"]
topics: ["stopping rules"]
---
# Confident Rankings with Fewer Items: Adaptive LLM Evaluation with Continuous Scores

## One line
Extends IRT-based computerized adaptive testing from right/wrong items to continuous scores (ROUGE, BLEU, LLM-as-judge) and adds a multi-model ranker that stops as soon as every adjacent pair of models is confidently ordered or declared a tie.

## Method
Problem: adaptive testing already cuts LLM evaluation cost, but prior methods assume binary correct/incorrect answers, so continuously scored generation tasks could not use it. And standard CAT tests each model to a fixed precision even when the only question is "which model is better".

Idea 1, continuous CAT. Keep the 1PL logistic mean, µ = logistic(θ − b), but replace the Bernoulli outcome with a normal whose variance mimics Bernoulli: σ² = k·µ(1−µ). One noise parameter k per dataset-metric plays the role of 1/a² (discrimination). Variance peaks at µ = 0.5 and shrinks at the edges, keeping most mass inside [0,1]. Fisher information becomes µ(1−µ)/k, so the item-selection and Bayesian-update machinery of binary CAT is reused unchanged. A dropped second information term only makes standard errors conservative and leaves item order unchanged whenever a > √2. Item difficulties b and k are fitted once from a calibration population of models; items whose scores anti-correlate with ability are discarded.

Idea 2, adaptive ranker. Run one CAT estimator per model, compute P(θi > θj) = Φ((θ̂i − θ̂j)/√(SEi² + SEj²)) for adjacent pairs in the current ranking, and keep testing only models in pairs not yet resolved at confidence γ. Among candidates, the next item goes to the model with the highest SE²/((n+1)·cost), so cheaper models absorb the extra testing. Stop when all adjacent pairs are confident, or report remaining pairs as ties when the budget runs out.

## Evaluated on
- Better rankings than random sampling at equal cost: mean Kendall τ 0.75 vs 0.62 using about 2% of items, winning on 7 of 9 dataset-metric pairs; on the LLM-judge metric (TruthfulQA) 0.637 vs 0.417.
- Confident verdicts are almost always right: 99% accuracy on non-tie pairs, and 94% recall of ground-truth ties; worst case GovReport ROUGE-L at 0.94 accuracy.
- The stopping rule is close to free: versus fixed-length CAT given strictly more items, it saves 32% of items and 39% of cost for 0.03 lower τ (0.75 vs 0.78), with the loss concentrated in FLORES COMET (+0.20 for fixed).
- Transfers to unseen model families: calibrated on OpenAI, Llama and Gemini only, it averages τ 0.76 vs 0.63 for a static most-discriminative subset and 0.58 random; the static subset ranks the held-out families in near-reverse order on TruthfulQA (−0.27, −0.33) with no warning.
- Fit of the variance assumption does not drive results: the best-ranking metric has conformance R² = −8.2; low discrimination (Nemotron F1, a = 1.39) predicts failure.

## Limitations admitted by the authors
- Cold start: item parameters need exhaustive runs of calibration models (17 models × 4 temperatures, equal to 68 full evaluations), which only pays back after roughly 70 new-model evaluations on that dataset.
- Parameters must be refitted for every metric separately, adding overhead for multi-metric evaluation.
- Each adjacent pair is tested independently at α = 0.05, so family-wise error is uncontrolled: about 18% chance of at least one misordered pair for five models; Holm-Bonferroni would fix it but might erase the efficiency gain.
- The tie detector is very conservative: it reports 51% ties against 26% in ground truth (tie precision 0.45), and 61% vs 7% on Nemotron.
- The LLM judge (GPT-4.1-nano) shares a family with several evaluated models, possibly biasing calibration toward them.

## Limitations found by others

## What it leaves untried
- Item-specific discrimination (2PL) instead of one global k; named as future work, it matters most where the method loses to random.
- Testing with an LLM judge as the main or only scorer, with judge noise and bias modelled: only one of nine settings uses a judge, and its ranking accuracy (0.637) is among the weakest.
- A family-wise-corrected or sequentially valid stopping rule, to see how much of the 32% item saving survives once the 18% misordering risk is controlled.

## Topics
[[Topic - stopping rules]]
