---
title: "More Choices, Fewer Decisions: Ordinal-Scale Bias in JEV-like Direct-Decision Models"
authors: Tianxiang Gao et al.
date: 2026-09
arxiv: 2609.38827
url: https://arxiv.org/abs/2609.38827
venue: arXiv
category: llm-judge-foundations
pdf: agent as a judge papers/decision models/open models/evaluations/More Choices, Fewer Decisions - Ordinal-Scale Bias in JEV-like Models (Gao 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "evaluations"]
topics: ["decision models", "judge and decision-model audits", "presentation sensitivity"]
---
# More Choices, Fewer Decisions: Ordinal-Scale Bias in JEV-like Direct-Decision Models

## One line
Shows that JEV-like direct-decision models (JEV 1.13, KEV, StartLux) squeeze their verdicts onto far fewer levels of a graded rating scale than the gold labels occupy, that finer scales make this worse, and that targeted LoRA post-training can largely undo it on the trained scales.

## Method
Problem: a direct-decision model can score plausible accuracy while using only a small part of the scale it is given. Accuracy scores items one at a time, so it cannot see how the whole population of verdicts is spread. Motivating case: JEV 1.13 on ANLI reaches 74.95% accuracy, yet sends 38.8% of predictions and 51.3% of errors to Neutral, although gold is nearly balanced and Neutral is picked at 37.2-39.6% in every slot.

Idea: a population-level utilization metric. exp(entropy) of a label distribution is its effective number of labels (Hill numbers). D_R is the percentage gap between the effective support of the argmax decisions and that of the gold labels; a shortfall is "candidate-space compression". D_R = 0 means equal size, not the same labels, so TVD is reported next to it. A soft version on the mean probability vector separates spread-out probabilities from spread-out decisions. The paper then rules out rival causes one at a time (gold imbalance, candidate position, candidate count, spacing of neighbouring levels) and argues that compression is tied to ordinal structure and grows as the scale is refined. The fix it tests is BA-LoRA, a bias-aware LoRA objective that adds consistency, diversity and SVD terms to the supervised loss.

## Evaluated on
- Ordinal scales compress, nominal ones mostly do not: across 36 ordinal datasets mean D_R is 25.9-39.5 points, against 1.0-13.4 on four nominal tasks with 7-14 candidates. On a balanced 14-level toxicity task JEV puts 66.2% of predictions on Level 01.
- Position is not the cause: shuffling candidate order lowers ordinal D_R from 35.0-52.5 to 26.1-46.0 points, still far above the 0.4-1.4 for shuffled nominal tasks.
- Finer scales compress more on the same items: JEV's D_R rises from 4.1 at K=2 to 45.6 at K=14, while DBpedia stays below 0.4. KEV-4B/9B keep at least 96% soft utilization as top-1 margins fall from 50-54 to 4-6 points, so the probabilities stay broad while the argmax piles up.
- Accuracy and utilization come apart: wider spacing on Politeness lifts JEV accuracy from 38.2% to 43.6% while D_R rises from 6.1 to 26.8. KEV-4B is more accurate than KEV-0.8B (33.4% vs 28.8%) yet more compressed (32.8 vs 31.1).
- Post-training works in-domain: BA-LoRA cuts D_R from 52.6 to 13.2 (0.8B) and from 53.6 to 14.4 (4B) on held-out items from the trained sources. On 28 unseen ordinal sources the 4B model improves (26.8 to 21.3) but the 0.8B model gets worse (25.0 to 29.9).

## Limitations admitted by the authors
- The ordinal/nominal split is binary, so "semantic coupling" as the cause rests on task type, not a graded measure. Difficulty is also confounded with it: nominal accuracy is 70-85% against 29-38% on ordinal tasks.
- Same-item scaling covers three ordinal sources, and its nominal reference, DBpedia, is near ceiling (at least 98.9% accuracy), so it is not a difficulty-matched control.
- Position results rest on two permutations per item, and all results are point estimates.
- Matching support is not correctness: KEV-0.8B reaches D_R 0.1 at 34.8% accuracy, near the 33.3% chance level.
- Only one hosted JEV version and two open families are tested. SST-5, DBpedia-14 and IMDb are KEV training sources and overlap was not audited, so the DBpedia ceiling may reflect exposure.
- BA-LoRA shows KEV can be changed but says nothing about why JEV compresses, and it hurts the 0.8B model on unseen sources.

## Limitations found by others

## What it leaves untried
- A decoding-side fix. Probabilities stay broad while the argmax concentrates, so reading an expected score or thresholds off the full distribution might restore utilization without training. It is the only option for hosted JEV.
- A link to downstream harm. The paper recommends reporting D_R for rubric judges and cascades, but it never shows that compression changes rankings or cascade decisions.

## Topics
[[Topic - decision models]] · [[Topic - judge and decision-model audits]] · [[Topic - presentation sensitivity]]
