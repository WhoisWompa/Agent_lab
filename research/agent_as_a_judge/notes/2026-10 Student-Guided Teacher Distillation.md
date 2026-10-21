---
title: "Student-Guided Teacher Distillation for Efficient LLM Task Routing: Positioning Against Jev-Style System-1 Classifiers"
authors: Haifeng Wu et al.
date: 2026-10
arxiv: 2610.02516
url: https://arxiv.org/abs/2610.02516
venue: arXiv
category: alternative-paradigms
pdf: agent as a judge papers/decision models/open models/papers/Student-Guided Teacher Distillation for LLM Task Routing vs Jev-Style Classifiers (Wu 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "papers"]
topics: ["open decision models"]
---
# Student-Guided Teacher Distillation for Efficient LLM Task Routing

## One line
A compact ModernBERT router, distilled from a DeBERTa-v3 zero-shot NLI teacher, also proposes the top-k candidate labels the teacher scores, so each labeling round gets cheaper and the student sharper, for routing requests into a fixed 60-category task taxonomy.

## Method
The problem is labeling cost. A zero-shot NLI classifier scores one premise-hypothesis pair per label, so with 60 task categories, every request costs 60 teacher passes, and over hundreds of thousands of requests that pairwise scoring is the main cost of building a dataset.

The idea: use the student *before* teacher inference. Its softmax gives a ranking that knows the task, so the teacher reranks only the student's top-k labels. The teacher's labels retrain the student, the better student proposes sharper candidate sets, and k shrinks (top-8 to top-4, say) only once measured coverage at the smaller k holds up. What is new, by the authors' account: the first stage is a real classifier trained end to end on the target taxonomy and is the same model served in production. In extreme multi-label classification (XMC), the shortlist comes from embedding similarity or clustered label trees instead. In self-training, the teacher always scores the full label space. It assumes the teacher's top-1 label nearly always falls in the student's top-k; if it doesn't, it can never be recovered.

The second idea is about what counts as a valid target. Scoring k labels and setting the rest to zero gives a vector that is *not* a 60-class soft target for KL distillation. Soft-label distillation gets its value from the probabilities on non-top classes (Hinton's "dark knowledge"), and zeroing classes that were never scored biases the student toward overconfidence instead of approximating the distribution sparsely. So truncated top-k scores supply only hard pseudo-labels (cross-entropy terms), and the KL term is kept for examples the teacher scored over all 60 labels.

Jev and Laya appear only as context: System-1 decision models with no published training method.

## Evaluated on
- Student imitates teacher moderately: best checkpoint 77.5% teacher agreement (155/200), deployed v4 76.5%, up from 62.82% (v2) and 69.5% (v3).
- More teacher data did not help by itself: v5-full60, with an order of magnitude more teacher-scored examples, fell to 71.5%. Only a 1-epoch, low-learning-rate fine-tune from v4 reached 77.5%.
- Top-k keeps most of the teacher's top-1: Coverage@16 of 91.3% (in-sample seed set, n=300) and 100% (fresh SWE holdout, n=40). Coverage@4 is 74.3% / 80.0%, so it degrades gradually instead of collapsing.
- Agreement depends heavily on distribution: 39.0% on the in-sample seed set (19.0% against human gold) and 62.5% on the fresh holdout, both well below the 76.5% headline.
- Fast in serving: about 5,200 requests/s on four GPUs.

## Limitations admitted by the authors
- The central claim is unproven. The paper has no full-60-teacher GPU throughput number, so no ratio of labeling-cost reduction can be reported; the only full-60 teacher timings are local CPU runs that don't represent real cost.
- The coverage samples are convenience samples, not the certified held-out set. One sample was likely in the training data, and the other is "best-effort" disjoint because the training row range was not recorded.
- Teacher agreement measures imitation, not correctness. The only human-gold figure (19.0% on the seed set) is very low.
- No embedding-retrieval baseline and no comparison against non-iterative distillation, so it is unshown whether the student-guided shortlist beats a generic retriever.
- Early runs used invalid truncated KL targets; low-confidence pseudo-labels and duplicates are named risks.

## Limitations found by others

## What it leaves untried
- A calibration check on the student's confidence. The router thresholds on confidence, and the paper positions itself against "calibrated" System-1 models, yet it reports no calibration measure, so its confidence scores cannot be compared with Jev-style claims.
- Filling unscored classes with something better than zero (for example the student's own probabilities, renormalised) so truncated rounds can still feed the KL term.
- A per-example adaptive k driven by student uncertainty instead of one global k, which would target teacher cost at the inputs where coverage fails.

## Topics
[[Topic - open decision models]]
