---
title: "Koa-decision: Fast and Consistent Structured Decision Making with Generative LLMs"
authors: Shenghong Dai et al.
date: 2026-09
arxiv: 2609.36115
url: https://arxiv.org/abs/2609.36115
venue: arXiv
category: alternative-paradigms
pdf: agent as a judge papers/decision models/open models/papers/Koa-decision - Fast and Consistent Structured Decision Making with Generative LLMs (Dai 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "papers"]
topics: ["decision models", "open decision models"]
---
# Koa-decision: Fast and Consistent Structured Decision Making with Generative LLMs

## One line
Fine-tunes an open LLM or VLM to answer any classification-style decision with one reserved control token, read off in a single decode step, so it matches frontier models on accuracy at about 0.53 s per request whatever the task.

## Method
The problem: prompted LLM classifiers give verbose multi-token answers, and constrained decoding still spells labels token by token, so latency grows with label length and varies. Encoder classifiers are fast but tied to one fixed label set.

The idea is to make each decision a single typed token. The vocabulary gets a pool of up to 500 reserved control tokens ([control_1] ... [control_500]) with trainable embeddings. As special tokens they never split or appear in the input. The system prompt lists the active labels in plain language, each tied to a control token. Fine-tuning puts cross-entropy only on the one assistant position, with a softmax limited to the active control tokens. Inference is one argmax over those tokens, so decoding is O(1).

What is new compared with SALSA, the closest concurrent work: the label-to-token mapping is **shuffled at random across training instances**. A token's identity then carries no meaning, so the model has to read the label descriptions in the prompt. Any new mapping works at inference, which makes adding, merging or retiring labels a prompt edit instead of retraining. Without the shuffle, the authors report, the models overfit to token IDs and failed on new mappings (no number given). Multi-label output trains toward a soft target spread over all the relevant tokens and keeps every label above a threshold, still in one pass.

## Evaluated on
- **Frontier-level accuracy on production routing:** 85.5% on a private intent-routing set whose labels change over time, against 87.7% for Claude-4.8-Opus, 87.1% for Gemini-Pro-3.1 and 84.0% for GPT-5. All are zero-shot on that set.
- **Several-fold lower latency, flat tail:** 0.53 s median and 0.63 s P95, which is about 1.9x to 7.5x faster than frontier models at the median and 2.4x to 9.0x at P95. P95 minus P50 is about 0.10 s, while frontier models widen by 0.5 to 1.7 s.
- **Latency does not depend on the task:** medians of 0.529 s, 0.526 s and 0.527 s on intent routing, SST-2 and voice endpointing. Jev/TypeSafe, another single-token system, is essentially tied at 0.55 s, so the speedup comes from the formulation itself, not from engineering.
- **Multimodal:** Gemma-3-27B reaches 62.7% on MIntRec 2.0 (30 intents, with video). That beats Gemini-Pro-3.1 at 55.9% and the task-trained encoders MAG-BERT and MulT at about 60.6%.
- **Mapping invariance:** across ten fresh random token permutations on MIntRec 2.0, accuracy is 61.62 ± 1.11, against 62.72 with the fixed mapping.

## Limitations admitted by the authors
- **Multilingual weakness:** fine-tuning used only English. On MTOP the best backbone averages 73.7, against 77.7 for GPT-4o and 78.4 for the base Mistral it was tuned from. The Mistral fine-tune falls to 59.3 on Thai.
- **Multi-label is asserted, not shown:** the target distribution and the selection rule are left out, and no multi-label results are reported, so the claimed edge over Jev is unsupported in the paper.
- **The O(1) claim covers decoding only:** prefill still grows with prompt length, and the prompt lists every label with its description.
- **Production data cannot be released:** the headline intent-routing numbers can only be reported in aggregate and cannot be reproduced.

## Limitations found by others

## What it leaves untried
- **Calibration and abstention:** the restricted softmax gives a full distribution over labels, but the paper reports only argmax accuracy. Whether a 0.6 means anything, which a router needs to defer, is untested.
- **A matched-training control:** Koa is fine-tuned while frontier models run zero-shot. No experiment separates the single-token interface from the effect of supervised fine-tuning, for example a model fine-tuned to emit label strings.
- **Large or open-ended label sets and agent-trace judging:** the hardest tests use 77 classes (Banking77) and 30 classes (MIntRec 2.0), far below the 500-token pool. It is also untested as a judge of long trajectories, where prefill rather than decoding dominates latency.

## Topics
[[Topic - decision models]] · [[Topic - open decision models]]
