---
title: "Chinese Decision: A Family of Language Models for Single-Pass Probabilistic Decision-Making"
authors: yanqiang (single author)
date: 2026-10
arxiv: 2610.23170
url: https://arxiv.org/abs/2610.23170
venue: arXiv (technical report)
category: trained-judges-reward-models
pdf: agent as a judge papers/decision models/open models/papers/Chinese Decision - A Family of LMs for Single-Pass Probabilistic Decision-Making (Yan 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "papers"]
topics: ["decision models", "open decision models"]
---
# Chinese Decision: A Family of Language Models for Single-Pass Probabilistic Decision-Making

## One line
Fine-tunes small Qwen3.5 causal LMs (0.8B, preliminary 2B) with LoRA into an open Chinese decision model that returns a calibrated probability distribution over supplied candidates from one forward pass, with one checkpoint serving general, medical, legal and financial decisions.

## Method
- **Problem:** triage, moderation and tool routing need a probability over a few known options, not free text that must be parsed, and a bare label carries no uncertainty.
- **Interface:** context, instruction and up to 26 candidates (key plus description) are compiled into one fixed Chinese prompt with letters A to Z. The logits for those letters at the final position are softmaxed over the valid candidates only. Nothing is generated. The distribution serves Boolean (p(true)), categorical (argmax key) and ordinal score (expected level index) questions.
- **What is new:** little, by the author's own account: the letter readout (from "hmm"), backbone and data (CJ-Bench, from Chinese-Jev) are borrowed. The contribution is one causal-LM checkpoint trained jointly across domains (Chinese-Jev used encoder specialists), one prompt compiler shared by training, eval and serving, and a GGUF/Q8 deployment path.
- **Training:** cross-entropy on soft or hard targets; categorical candidates are shuffled with their targets to reduce position dependence. The 2B run adds RLCD: Gaussian logit perturbations rewarded by a clipped log, spherical and ranked probability score, which the author does not claim is strictly proper because of the clipping.
- **Calibration:** the checkpoint is chosen by validation NLL. A single temperature (T = 1.108) is fitted on a held-out validation bucket for deployment. The API's "sharpness" field is explicitly not a probability of being correct.

## Evaluated on
- **One small model matches hosted Jev on professional domains:** the 0.8B averages 76.98% across medicine, law and finance against Jev's 77.01% (imported number). It beats Chinese-Jev's three specialists by 1.21, 7.76 and 9.50 points, and trails Jev by 4.17 points in finance.
- **General domain above prior baselines:** 72.24% accuracy and 3.03% ECE, against Chinese-Jev General at 69.20% / 3.78% and Jev at 68.35% / 11.45%.
- **Low aggregate calibration error, uneven by domain:** micro ECE is 1.07% raw and 0.27% after temperature scaling. Legal ECE is 5.70%, compared with 0.17% in medicine.
- **Boolean is easy, ordinal is hard:** 94.95% on Boolean, 78.33% on categorical, 56.47% on score questions.
- **Q8 keeps the aggregates but not every answer:** ECE 0.2696% vs 0.2706%, yet top-1 agreement with the full-precision model is only 98.92% (96.72% on score questions). 1,185 correct predictions turn wrong and 1,240 wrong ones turn right.
- **Bigger is not yet better:** 2B at 40% of an epoch gets 72.56% general but 74.22% professional, below the 0.8B.

## Limitations admitted by the authors
- Baselines are copied from Chinese-Jev, not rerun, and the 0.8B is larger than the roughly 322M-parameter Chinese-Jev encoders, so "beats Chinese-Jev" is not like-for-like.
- Single runs, no seeds, no confidence intervals. Many decisions share a parent document (for example 2,048 parents behind 4,300 legal items), so the effective sample is far smaller than 307,900. The 0.03-point tie with Jev is descriptive only.
- 0.8B vs 2B changes size, objective, batch and data seen at once, so nothing isolates scale or RLCD.
- Calibration is non-monotonic. Legal ECE rises from 2.30% to 5.70% between steps 5000 and 10000 while accuracy improves, so a low micro ECE hides subgroup miscalibration.
- No robustness tests (reordering, paraphrase, distractors, injection, out-of-distribution). A documented failure: the spoiler detector fires on "please don't post spoilers".
- With no "none of the above" option, the softmax puts all probability on the supplied candidates even when the right answer is missing.
- Labels are inherited: a medical "match" label measures the source task, not verified medical correctness; contamination is not ruled out.

## Limitations found by others

## What it leaves untried
- A matched ablation: 2B with cross-entropy only vs 2B with RLCD, at equal data. Without it the paper cannot say whether the proper-scoring RL objective helps at all.
- Testing whether the claimed position independence holds by reordering candidates at test time. Training shuffles them but the test never does, which matters for any judge use where option order is arbitrary.
- An abstain or "none of the above" candidate plus risk-coverage curves. A judge needs to know when its 0.9 means something, and the paper reports only aggregate ECE.

## Topics
[[Topic - decision models]] · [[Topic - open decision models]]
