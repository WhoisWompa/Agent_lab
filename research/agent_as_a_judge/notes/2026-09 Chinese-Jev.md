---
title: "Chinese-Jev: Bringing System One Model to Chinese-Language Tasks"
authors: Zexiao Wang et al.
date: 2026-09
arxiv: 2609.36965
url: https://arxiv.org/abs/2609.36965
venue: arXiv
category: alternative-paradigms
pdf: agent as a judge papers/decision models/open models/papers/Chinese-Jev - Bringing System One Model to Chinese-Language Tasks (Wang 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "papers"]
topics: ["decision models", "open decision models", "calibration"]
---
# Chinese-Jev: Bringing System One Model to Chinese-Language Tasks

## One line
A 322M-parameter encoder-only Jev-style decision model trained on 10 million Chinese decisions, then fine-tuned separately for medicine, law and finance, that matches or beats the hosted Jev on general Chinese tasks at a fraction of the latency.

## Method
The problem: Jev-style "System One" models return a typed decision (choice among options, noul true/false on a proposition, ordinal score) with probabilities in one forward pass, but existing ones are weak in Chinese, and Chinese supervision is scattered across datasets with incompatible label formats.

The idea has two parts. First, a single conversion that turns any Chinese annotation into "context, instruction, type, candidate list, target probability distribution": single-answer questions become one-hot choice targets, yes/no labels become noul, ratings become score, and multiple-answer questions are split into one noul per option ("should option C be selected?"). When several human ratings exist, the target is a soft distribution that keeps both the mean rating and the rater disagreement. Exact duplicates are fingerprinted with choice options sorted, so a reordered question is recognised as the same decision; groups with conflicting labels are dropped entirely, and items sharing a source passage go to the same split to limit leakage.

Second, the model: an mmBERT encoder reads type, instruction, all candidates and context together; a type embedding and a small decision Transformer condition on the decision type; a shared scorer gives one logit per candidate marker, softmaxed. Score readout is the expected level. Training adds to cross-entropy a policy-gradient term (Laya's RLCD) that perturbs logits and rewards proper scoring rules (log, spherical, plus ranked probability score for ordinal decisions), which should push toward calibrated distributions, not just correct argmax. Training runs general-first, then per domain, with one interface throughout.

## Evaluated on
- Chinese training alone fixes the multilingual starting model: general accuracy 40.22% to 69.20% and ECE 23.04% to 3.78% at unchanged 14 ms latency.
- Slightly beats the hosted Jev on general tasks and is much better calibrated: 69.20% vs 68.35% accuracy (0.85 points, the "1.24%" headline is relative), ECE 3.78% vs 11.45%.
- Domain fine-tuning is necessary: the general model averages 37.97% on the three domains, specialists 70.82%; on finance general training even falls below the initialisation (35.39% vs 38.31%).
- Beats Jev only in medicine: 87.65% vs 84.29%. Law 60.10% vs 68.35% and finance 64.72% vs 78.39% stay well behind; "92% of Jev's average accuracy" summarises this.
- Fast and local: 15 ms per decision on an H200, about 17x to 20.3x below Jev's client-observed latency; an INT8 version runs in an iPhone browser at about 1 s per decision.

## Limitations admitted by the authors
- Law and finance remain below Jev, by 8.25 and 13.67 points; the specialists there were trained on only 24,000 decisions each versus 3,000,000 for medicine, so the domain claim rests mostly on medicine.
- Calibration gains from specialisation are uneven: legal ECE rises from 15.37% to 17.45% despite higher accuracy, and specialist average ECE is 12.08% vs Jev's 5.57%. The general-model calibration advantage does not carry over to the domains.
- The speedup over Jev includes network round-trip time, so it measures end-to-end response, not model inference speed; the 20.3x is not a like-for-like comparison.
- Near-duplicate screening against held-out text is not exhaustive; paraphrases across the training corpus are not merged, so some leakage cannot be ruled out.
- Several legal and financial sources (ClaimGen-CN, AppealCase, CFLUE) carry noncommercial licenses, limiting use of the specialists.

## Limitations found by others

## What it leaves untried
- Testing on Chinese benchmarks built outside its own pipeline. CJ-Bench is the held-out split of the same sources Chinese-Jev trained on, while every baseline sees it zero-shot, so the general-domain win over Jev may be largely in-distribution advantage.
- Post-hoc calibration: the paper builds separate calibration partitions for every corpus but applies no calibration, which is exactly what the legal and finance specialists' 11.55% to 17.45% ECE calls for.
- Checking forgetting and judge use: specialists are never re-scored on the general subset, and no result shows the model judging agent or LLM outputs, the use case typed decision models are pitched for.

## Topics
[[Topic - decision models]] · [[Topic - open decision models]] · [[Topic - calibration]]
