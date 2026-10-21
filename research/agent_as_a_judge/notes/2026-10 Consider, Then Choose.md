---
title: "Consider, Then Choose: Order-Invariant Decisions in System One Models"
authors: Jianguo Huang et al.
date: 2026-10
arxiv: 2610.18233
url: https://arxiv.org/abs/2610.18233
venue: arXiv
category: llm-judge-foundations
pdf: agent as a judge papers/decision models/open models/papers/Consider, Then Choose - Order-Invariant Decisions in System One Models (Huang 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "papers"]
topics: ["decision models", "presentation sensitivity"]
---
# Consider, Then Choose: Order-Invariant Decisions in System One Models

## One line
Runoff, a training-free rule that scores each option alone to keep a few candidates, then compares only those in every rotation of a model-derived ranking, so a single-pass decision model's choice no longer depends on option order.

## Method
The problem: System One decision models (Jev and open copies) read option-letter probabilities from one listing, so the answer depends on option order, more so with more options: for Qwen3-8B, shuffling changes 4.7% of answers at 2 options and 17.0% at 20. Cyclic averaging (AnyJev) leaves 10.3% at 20 options, because the input order still picks which K of the K! listings are averaged, and it costs K².

The diagnosis: scoring each option alone with a yes/no question gives a pointwise distribution blind to order. Flips happen among the top three pointwise options (at least one flip answer is there in over 90% of flips) and when the pointwise top-1 is uncertain: over a third flip below 0.8, 7% at 0.999 and above, while listwise confidence stays at 93% to 99.5%. More options mean more uncertain questions (7% to 24% from K=2 to 20). Shuffling only the ruled-out options changes about as many answers as shuffling the candidates (15.3% vs 14.0%), so distractors add noise by themselves.

The construction, in two steps:
- **Consider**: keep the smallest top set of the pointwise distribution that holds at least α of the probability mass and has at least k_min options (defaults α=0.99, k_min=3). The set grows when the model is unsure.
- **Choose**: rank candidates by pointwise probability, make a listwise decision on each cyclic shift of that ranking so every candidate takes every position once, and average log-probabilities. The set's mass is split by this comparison; outside it, pointwise mass is kept.

Why it is invariant: every request depends only on the option *set* and the model's own scores, never the input order, whatever the model's position bias, provided the model is deterministic and pointwise scores have no ties. Cost is K + m² option slots instead of K²; two forward passes on open models.

## Evaluated on
- Removes order dependence on open models: 0.0% flips on all five datasets for Qwen3-8B and Gemma 4 12B, against 11.6%/7.1% average for AnyJev and 22.8%/14.4% for Listwise.
- Keeps accuracy with many options: 73.8% at 20 options vs 74.5% for AnyJev and 73.0% for Listwise. Average over five datasets is 65.8 vs 66.8 (Qwen) and 72.2 vs 73.8 (Gemma).
- Works as a black-box wrapper: GPT-6 Luna drops from 13.2% native flips to 0.0%, Jev 1.13 from 5.3% to 0.9%, and Mercury Decide from 9.8% to 1.4%. All five fine-tuned decision models drop to 0.0%.
- Cheaper when options are many: 77 ms vs 308 ms per record on 20-option Banking20 (4.0x), but slightly slower at 3–6 options (77 vs 67 ms).
- Helps a chained agent: on 316 OSWorld tasks it solves 27 vs 21 tasks (Qwen3.5-35B-A3B) and 14 vs 9 (Qwen3.5-9B).

## Limitations admitted by the authors
- Invariance assumes identical requests get identical answers. On non-deterministic APIs, flips remain (Jev 1.13 0.9%, Tev1 4B up to 7.3% on MMLU-Pro), because noisy yes/no scores can change the consideration set.
- Fixes only option order, not other biases such as preferring certain option names.
- Trails cyclic averaging on reasoning questions: on MMLU-Pro it is up to 3.6 points behind (Torchcast 12B), because the consideration set misses the gold answer more often. Even at k_min=3, the set contains the gold answer only 90% of the time.
- Accuracy relative to baselines varies: with Gemma 4 12B on Banking20 it falls 0.7–3.3 points behind AnyJev from 8 options on.

## Limitations found by others

## What it leaves untried
- Making the gold answer survive Consider more often (a set size adapted to question type, or a fallback when pointwise scores are flat); the 10% pruning misses drive the reasoning-task losses.
- Using pointwise uncertainty as an abstain or reliability flag: the paper shows listwise confidence hides it (93%+ even when over a third flip) but never acts on it.

## Topics
[[Topic - decision models]] · [[Topic - presentation sensitivity]]
