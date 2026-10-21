---
title: "BERT-as-a-Judge: A Robust Alternative to Lexical Methods for Efficient Reference-Based LLM Evaluation"
authors: Hippolyte Gisserot-Boukhlef et al.
date: 2026-04
arxiv: 2604.09497
url: https://arxiv.org/abs/2604.09497
venue: COLM 2026
category: trained-judges-reward-models
pdf: agent as a judge papers/decision models/open models/papers/BERT-as-a-Judge - Efficient Reference-Based LLM Evaluation (Gisserot-Boukhlef 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "papers"]
topics: ["trained judges and reward models", "open decision models"]
---
# BERT-as-a-Judge: A Robust Alternative to Lexical Methods for Efficient Reference-Based LLM Evaluation

## One line
Fine-tunes a 210M-parameter encoder to classify a (question, candidate answer, reference) triplet as correct or incorrect, replacing regex answer matching at a fraction of the cost of an LLM judge.

## Method
The problem: benchmarks with a single right answer are scored by parsing the model's output with a regex and matching it lexically. This scores format compliance as much as ability. Llama-3 70B misformats over 60% of its open-form math answers. Even models that follow the format lose points to verbose answers: Gemma-3 is underestimated by 12 to 31 points on context extraction while its parsing failures are near zero. Leaderboards get reshuffled; Qwen-3 32B drops 18 places on multiple choice. LLM judges fix this but cost a generation per verdict, and their output depends on which judge and prompt are used.

The proposal: correctness against a reference is a classification task, and bidirectional encoders are good at classification. An encoder (EuroBERT 210M) reads the question, the candidate and the reference together and outputs a sigmoid probability of "correct". It is trained with binary cross-entropy on about 1M triplets drawn from 36 models' outputs, labeled by a large LLM judge (Nemotron-Super-v1.5). This is distillation: the encoder learns to imitate the big judge's verdicts, then runs in about 200 ms per sample on a laptop CPU. The assumption is that the teacher stands in for humans; on 3,212 human annotations it agrees 97.5% of the time.

## Evaluated on
- Beats regex across task types: +21.2 points on CoQA, +20.4 on MATH, +10.4 on ARC-Challenge (accuracy against the teacher's labels).
- Matches LLM judges up to 70 times larger: 98.5 vs 98.6 (Qwen-3 14B) on MMLU, 89.3 vs 81.1 on SQuAD-v2. It also beats a Qwen-3 0.6B fine-tuned on the same data with equal training FLOPs (89.3 vs 84.9 on SQuAD-v2). Asking the LLM judges to reason first did not raise their accuracy.
- Holds on tasks it was not trained on (98.6 TruthfulQA, 95.1 ASDiv). Leaving a model family out of training costs at most about three points on that family (worst case LFM-2 0.7B context extraction, 87.4 to 84.4; most cells move by under one).
- 100K training samples (about 2 GPU hours) are enough for multiple choice and math; only context extraction keeps improving with more data.
- Accuracy is flat across a wide range of decision thresholds. Its probabilities are near-calibrated after temperature scaling with τ = 1.75.

## Limitations admitted by the authors
- Only English benchmarks with objectively checkable answers. Open-ended generation (summarization, translation, code, instruction following) is untested, and that is where reference matching is hardest.
- Context extraction is the weak spot: 88 to 91% versus 93 to 99% elsewhere. Without the question in the input it falls further, from 89.2 to 84.2, because judging a span needs the passage.
- Using it only as a fallback when the regex fails recovers little: context extraction rises from 73.0 to 75.2, against 89.2 for the encoder alone. Most regex errors are wrong matches on answers that parsed, not parse failures.
- Training on one answer format and testing on another costs accuracy: context extraction falls from 89.2 to 84.3 when a model trained on formatted answers judges free-form ones.
- Multilingual results are preliminary, MMLU only. English-only training already gets 95.8 to 97.9 across 12 languages.

## Limitations found by others

## What it leaves untried
- Scoring against human labels. Every headline number is agreement with the same teacher that produced the training labels, so above about 97.5% it measures imitation of Nemotron, not truth. The paper's own correction formula, A_H = (2ρ − 1)A_S + 1 − ρ, turns 89.2 on context extraction into roughly 87 against humans (our calculation). It also assumes the encoder's errors are independent of the teacher's, which a distilled student is the least likely judge to satisfy.
- Adversarial or gaming tests. Verbose answers listing several candidates are already 22% of human-teacher disagreements. An encoder that can be fooled cheaply would be dangerous as an RL reward or leaderboard scorer, and this is not tested.
- Using its calibrated probabilities. The paper shows they are calibrated but never routes low-confidence cases to an LLM judge or a human, which would be a better hybrid than the regex fallback.

## Topics
[[Topic - trained judges and reward models]] · [[Topic - open decision models]]
