---
title: "From Retrieval to Typed Decisions: Calibrated System One Models from Biomedical Sentence Encoders"
authors: Pritam Deka
date: 2026-10
arxiv: 2610.02486
url: https://arxiv.org/abs/2610.02486
venue: arXiv
category: trained-judges-reward-models
pdf: agent as a judge papers/decision models/open models/papers/From Retrieval to Typed Decisions - Calibrated System One Models from Biomedical Sentence Encoders (Deka 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "papers"]
topics: ["decision models", "open decision models", "calibration"]
---
# From Retrieval to Typed Decisions: Calibrated System One Models from Biomedical Sentence Encoders

## One line
Converts biomedical retrieval encoders into calibrated one-pass typed-decision (System One) models, and shows that Laya's open RLCD recipe is a biased, rescaled estimator that loses to plain cross-entropy.

## Method
System One models (Jev, Laya) answer schema-typed questions about a text (choice, ordinal score, true/false "noul") in one forward pass, returning probabilities to threshold for act, defer or escalate. All existing ones start from general-domain checkpoints. The paper asks whether biomedical encoders trained for retrieval are a better start: a typed decision resembles retrieval (does "instruction + option" match the text?), though cosine similarity need not encode negation, ordinal judgement or calibrated truth.

SBERT2S1 offers four conversions: **Z/B**, a scaled cosine between text and hypothesis (frozen or fine-tuned; text embeddings precomputable for corpus screening); **C**, Laya's cross head scoring one [MASK] slot per option; and **PFR**, C's score added to the cosine prior with a zero-initialised last layer, so the untrained model is exactly the zero-shot retriever and training learns a residual on it. Calibration claims are all checked after temperature scaling.

Second idea: RLCD adds to cross-entropy a REINFORCE step on noise-perturbed logits rewarded by proper scores. The paper proves this ascends a noise-smoothed proper score, with two flaws: the baseline (mean of the item's own G=4 draws) includes the draw itself, shrinking the gradient by 3/4; and dividing by the minibatch reward std makes the term grow roughly as 1/sigma while noise is annealed, so the noisy term swamps cross-entropy. The fix, PG-LOO, uses the other draws' mean as baseline and drops the normalisation, giving an unbiased estimate.

## Evaluated on
- Retrieval helps zero-shot only when options differ in content: 15-24 chance-normalised points vs 0-7 for MLM parents. On label-word options (yes/no) cosine gaps are about 1e-3 and no encoder beats chance.
- After fine-tuning the benefit depends on the head: across 15 comparisons retrieval training is significantly better in 10 and worse in 1 with PFR, better in 1 and worse in 5 with C.
- C beats PFR under every objective (+1.3 to +2.4 seen, +3.8 to +10.2 held-out), but PFR is nearly order-invariant: 0.3% of answers flip under option permutation vs 15.7% for C.
- Released RLCD trails cross-entropy by 2.5-3.0 points. Its estimator points the right way (cosine 0.98) but is 3.6x to 15x too large as sigma anneals, so the score term outweighs CE 5-20x instead of 1.3x; PG-LOO recovers 1.5-2.5 points.
- No calibration gain survives scaling: PG has the lowest raw ECE (7.0 vs 9.3), but after scaling all objectives sit at 3.6-4.4 and PG has the worst NLL.
- A base-size BioClinical-ModernBERT cross head reaches 73.1 vs fine-tuned Laya-large 75.0 at a third of the size. Escalating the 20% least confident questions to Gemma-4-31B lifts macro accuracy from 59.5 to 68.4 (budget picked retrospectively on test).

## Limitations admitted by the authors
- The head-by-objective grid uses one encoder and Laya's hyperparameters untuned per objective, so the RLCD verdict may partly reflect the schedule.
- The six parent-retriever pairs share parents, so they are not independent replications.
- MEDLINE-S1 labels are weak: a missing index tag need not mean false, and indexers saw the full article.
- Seen-task calibration does not transfer: several models are poorly calibrated on held-out tasks, and cross-head order flips rise from 3% (seen) to 17% (held-out).
- Fine-tuning ruins the retriever (SciFact nDCG@10 from 67.6 to 24.6-43.3 unless the prior is frozen), which undercuts retrieve-then-decide for long notes. Those stay near chance anyway.
- A few training inputs recur in calibration and test splits. Removing them costs 0.3-0.4 points, but temperatures were not refitted.

## Limitations found by others

## What it leaves untried
- Retraining Laya-large with PG-LOO: the estimator fix is shown only on base-size encoders, while the recipe it critiques ships on the larger model.
- Fixing the label-word blind spot, e.g. an entailment-trained retriever or negation-aware hypotheses, so PFR's prior helps noul questions, a large share of the suite.
- Validating the escalation threshold on held-out data, since the cascade is the deployment argument and is so far only retrospective.

## Topics
[[Topic - decision models]] · [[Topic - open decision models]] · [[Topic - calibration]]
