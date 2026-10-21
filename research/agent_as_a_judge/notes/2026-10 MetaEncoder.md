---
title: "MetaEncoder: Exploring the Limit of Bi-Encoders for Multimodal System One Decision Making with Natural Language Interface"
authors: Jianpeng Cheng et al.
date: 2026-10
arxiv: 2610.11316
url: https://arxiv.org/abs/2610.11316
venue: arXiv
category: alternative-paradigms
pdf: agent as a judge papers/decision models/open models/papers/MetaEncoder - Limits of Bi-Encoders for Multimodal System One Decision Making (Cheng 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "papers"]
topics: ["decision models", "open decision models"]
---
# MetaEncoder: Exploring the Limit of Bi-Encoders for Multimodal System One Decision Making with Natural Language Interface

## One line
Turns a 30B multimodal decoder into a cacheable bi-encoder that scores natural-language candidates against a free-form request, for both small-option decisions and million-item retrieval, and finds its ceiling is missing reasoning.

## Method
Problem: System One models (one forward pass, a choice plus a distribution) usually take a rigid per-task schema, and candidate scoring trades off badly. Cross-encoders and constrained decoders let the request see the candidates, so they are accurate, but cannot cache candidates or scale past a context window. Bi-encoders cache and scale to millions, but all interaction goes through one dot product, which fails on fine-grained distinctions and on labels defined only by the prompt's criteria.

Idea: keep the bi-encoder and win back the missing interaction on the request side. Request and candidates are free natural language, optionally with image/video. The representation is the normalised last-token hidden state, which under causal attention sees the whole request. For small closed sets (<256 options) the option list is pasted into the request, giving the request embedding roughly the view of alternatives a constrained decoder has. Scores are cosine similarity, softmaxed with a temperature into a distribution. Training is request-to-candidate InfoNCE; closed and open sets differ only in negatives: the row's other options vs in-batch plus hard negatives. The option list is randomly dropped from some closed-set training prompts so it cannot just string-match options. The assumption: a pointer-like match between a listed option and a candidate carrying the same label and text recovers joint comparison.

## Evaluated on
- Beats retrieval embedders on decisions: JevBench hard 0.7387 vs 0.4865 (WeMM-Embedding-9B) and 0.4324 (Qwen3-VL-Embedding-8B); ImaJev 0.8555 vs 0.8117.
- Trails the full-attention decision model it cannot replace on text decisions: JevBench hard 0.7387 vs 0.7658 for OpenJev-27B, MMLU 0.7767 vs 0.8601; but OpenJev does no retrieval or multimodal input.
- Near but below SOTA on retrieval: MMEB-V3 video 0.6486 vs 0.7431, image 0.7897 vs 0.8099; best on NanoBEIR 0.6634 vs 0.6175.
- Options in the request is the key trick: MMLU 0.5645 to 0.7456, MMMU 0.4875 to 0.5629; candidates rendered as label plus text add another +0.031 on MMLU. A bare letter as candidate still gets 0.6512 on MMLU (chance 0.25), so the model resolves a pointer.
- Order-robust: under 10 option permutations no variant's standard deviation exceeds 0.003.
- Reasoning is the bottleneck: letting the decoder generate freely lifts MMMU from 0.4962 to 0.7202; feeding the decoder's CoT to MetaEncoder lifts it from 0.5730 to 0.7155, and to 0.6871 with the answer label cut out (the full CoT leaks the label 93.7% of the time).

## Limitations admitted by the authors
- No explicit reasoning: both MetaEncoder and a constrained decoder sit about 20 points below an unconstrained decoder on MMMU, so on multi-step tasks a single pass is the ceiling.
- More input does not help hard tasks: going from 8 to 64 video frames raises Perception by 0.127 but Adaptation falls (0.4600 to 0.4367), so extra perception does not buy reasoning.
- The single-vector bottleneck costs accuracy against full attention, shown by the gap to OpenJev-27B on JevBench and MMLU.
- Pointer resolution degrades with set size: the bare-label deficit on MMMU widens from +0.028 at 3 options to -0.1725 at 10, so the "options in prompt" trick weakens as candidate sets grow.
- The CoT fix needs a decoder to generate the reasoning first, giving up the one-pass speed that motivates System One.

## Limitations found by others

## What it leaves untried
- Calibration: the model is pitched as returning a probability distribution, but no calibration measure is reported, only Hit@1/accuracy; for a judge or router the probability is the product; the claim is unsupported.
- Training data and the option-dropout rate are neither described nor ablated, so architecture and task-matched data cannot be separated (the authors credit fine-tuning for beating the decoder).
- An encoder that reasons itself (e.g. generated think-tokens before embedding) is named as the fix in the conclusion but not tried; that is the test of whether a cacheable model can close the 20-point gap without a separate decoder call.

## Topics
[[Topic - decision models]] · [[Topic - open decision models]]
