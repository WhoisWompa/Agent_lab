---
title: "LLM-as-Jev: LLMs Are Already Jev-Style Decision Models, When and How to Fine-Tune Them"
authors: Yinheng Li et al.
date: 2026-10
arxiv: 2610.02076
url: https://arxiv.org/abs/2610.02076
venue: arXiv
category: alternative-paradigms
pdf: agent as a judge papers/decision models/open models/papers/LLM-as-Jev - LLMs Are Already Jev-Style Decision Models, When and How to Fine-Tune Them (Li 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "papers"]
topics: ["decision models", "open decision models"]
---
# LLM-as-Jev: LLMs Are Already Jev-Style Decision Models, When and How to Fine-Tune Them

## One line
Shows that an unmodified causal LLM, read through a numbered-option prompt and a prefix-free scoring trick, already works as a calibrated Jev-style decision model, and gives a KL-anchored fine-tuning recipe for the cases where training helps.

## Method
Problem: Jev returns a probability distribution over fixed options instead of text, but is proprietary. Community copies add custom heads (retrained per backbone) or read option-letter logits (capped at 26 options), and it was unclear when fine-tuning pays: fine-tuned reflex 4B (79.7%) trailed frozen SemIf on the same backbone (80.5%).

Idea, training-free: list options as `[1] … [K]`, prefill the reply with `Best answer: [`, and score each option as the summed log-probability of its suffix `k]`, softmaxed over all K. The closing bracket makes suffixes prefix-free (`1]` is not a prefix of `12]`), so K is unlimited, and the shallow trie lets one prefill plus 1 to 3 parallel steps score even 151 options. Options are compared jointly in one prompt; isolated scoring trails by about 5 points (76.2% vs 81.4%). With no architecture change it carries over to images and to native thinking ("Thinking Jev": think to a hard token budget, then score).

Idea, fine-tuning: a listwise loss renormalised over legal tokens at each trie node, computed along the gold path only. It ignores illegal tokens and positions outside the answer, so the model can drift there; three KL anchors to the frozen model (legal vs illegal mass, ranking of illegal tokens, full distribution at reply start and after the bracket) pin those down. The assumption: tuning should only reorder options.

## Evaluated on
- A frozen 4B model is already competitive: 81.4% on public JevBench, versus 80.5% for SemIf and 79.7% for fine-tuned reflex on the same backbone; ECE 0.057 with no post-hoc scaling, versus 0.061 and 0.070.
- Scales past letter readouts: 69.0% zero-shot on 77-way Banking77; 82.4% on MMBench, 15.2% without the image.
- Fine-tuning helps where the model is weak, not broadly: 0.6B Banking77 goes 22.2% to 60.5%; no full-parameter 4B run beats the frozen 4B on JevBench (74.9% to 81.4%). MMLU and TriviaQA stay flat, so training does not add knowledge.
- Anchors matter though scores hide it: without them the 4B model writes past the answer on 69 of 231 items and 176 0.6B answers hit the length limit, at nearly unchanged accuracy; λ=1 cuts this to 0 and 1. LoRA with anchors is the best 4B: 84.0%, ECE 0.050.
- Budgeted thinking closes the gap to a frontier model: 94.8% at 4,096 thinking tokens versus 94.4% for GPT-5.6 Sol, at an estimated $450 per million decisions against $2,477; budgets up to 256 tokens give no gain because the model spends them restating the task.

## Limitations admitted by the authors
- Training mixtures were revised after error analysis on public JevBench items, so fine-tuned JevBench results are labelled exploratory.
- One seed per configuration; the authors call 1 to 2 point shifts noise, the size of many reported fine-tuning effects.
- Mismatched training data backfires: intent-only training raises "yes" answers from 36 to 49 (35 are correct) and ECE from 0.057 to 0.134, cutting JevBench to 74.9%; more short-context data drops long items from 23 to 17 correct.
- Options 1 and 10 share a first token; anchored training shifts MMLU-Pro answers from 10 to 1 and loses 15 questions net, unexplained.
- The FP32 code is slow (194 ms at 4B vs 46 ms for SemIf), so cost claims rest on FLOP-based estimates, not measured serving.
- Thinking at 1,024 to 4,096 tokens multiplies price by 6.5 to 15 and replaces 2 forward passes with up to 1,824.

## Limitations found by others

## What it leaves untried
- No sealed JevBench score is reported for the authors' own models, while community models score far lower there (for example 86.1 public vs 37.0 sealed). Without it, the claim that frozen models generalise as well as tuned ones is untested on unseen items.
- Only two Qwen backbones are tested, though any causal LLM is claimed; Phi-4 and Llama 2 checks cover trie shape, not accuracy.
- Option-order bias is handled only by shuffling during training; the training-free recipe, the paper's main recommendation, is left exposed to position bias, and it is never measured.

## Topics
[[Topic - decision models]] · [[Topic - open decision models]]
