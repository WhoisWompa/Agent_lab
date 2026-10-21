---
title: "Selective Reasoning for Typed Decision Models: When to Start, Read, and Stop"
authors: Bin Zheng et al.
date: 2026-10
arxiv: 2610.19644
url: https://arxiv.org/abs/2610.19644
venue: arXiv
category: alternative-paradigms
pdf: agent as a judge papers/decision models/open models/papers/Selective Reasoning for Typed Decision Models - When to Start, Read, and Stop (Zheng 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "papers"]
topics: ["decision models", "open decision models", "adaptive reasoning depth"]
---
# Selective Reasoning for Typed Decision Models: When to Start, Read, and Stop

## One line
A single trained candidate-answer head on a frozen Qwen3.5-4B returns a typed choice either at once or from a partial chain of thought, with three small controllers deciding whether to start reasoning, when to query an answer, and when to accept it and cancel generation.

## Method
Problem: a typed decision model (Kev-style: picks one of the supplied candidates, no explanation) is fast but sometimes wrong. Reasoning fixes some errors, costs time, and can also break correct answers. The paper wants one interface that keeps the typed output whether or not reasoning ran, and spends reasoning only where it pays.

- **Shared reader.** One 10,240-parameter linear head reads candidate probabilities from the backbone state at a forced `</think><FINAL>` cue. Trained on empty and partial reasoning prefixes (128 to 1,024 tokens), the same head gives both the direct answer and every intermediate answer. Reading from the existing hidden states without the cue works much worse (41-52% vs 79% at 1,024 tokens), so every read needs its own backbone query.
- **When to start.** Two logistic models estimate, from the initial read's confidence features, the chance that reasoning *corrects* the answer and the chance that it *breaks* it. Reasoning starts when the difference clears a threshold set to route about 75% of questions.
- **When to read.** Reads cost input processing, so a cheap logistic trigger on the hidden state already produced during decoding (plus position) decides at every fourth sentence boundary whether a read is likely to find a correct, concentrated answer.
- **When to stop.** Accept a read if its normalised entropy certainty is at least 0.70, then cancel generation. If nothing is accepted, a terminal read answers. The authors note certainty measures concentration, not probability of being correct.

## Evaluated on
- Selective reasoning recovers most of the gain from reasoning: 84.38% vs 70.96% for direct reading over 768 ProofWriter, LogiQA 2.0 and ARC questions (+13.41 pp, CI 10.42 to 16.28).
- It beats a fixed budget at equal output: +7.29 pp over 512-token terminal reading with 2.25% more output tokens.
- It is faster than a 1,024-token budget at almost the same accuracy: 46.30% less time, a -1.17 pp difference (CI -2.60 to +0.26).
- The early-exit saving is real interruption: 34.09% less time than no-stop on identical token prefixes, 652 vs 654 correct. Only 2 of 25 wrong exits would have been fixed by continuing.
- The learned trigger cuts queries by 40.88% compared with reading every eight sentences, but time goes *up* by 0.406 s: sparser reads let generation run longer before acceptance.

## Limitations admitted by the authors
- One backbone (Qwen3.5-4B), with components fitted only on ProofWriter and LogiQA. ARC is the only transfer test, and there the benefit gate spends calls badly: 107 of the 108 ARC questions only it selects end up with the same correctness either way.
- The benefit gate does not beat simple margin routing: -0.39 pp (CI -1.56 to +0.78), and the factorial study cannot separate them either. The paper's correction-minus-regression idea is therefore unsupported as an improvement.
- Trigger supervision (correct with certainty at least 0.85) does not match online acceptance (0.70). 104 of 577 routed questions never get an intermediate read. Revised schedules save 15% of time but move accuracy by -1.17 pp.
- Independent greedy runs differ: the same policy scores 648 vs 652, and 638 vs 648 in another series. Differences of a few answers are within run noise.
- Energy and serving throughput are unmeasured, and the follow-up policies were tuned on the evaluation questions.

## Limitations found by others

## What it leaves untried
- Calibrating the acceptance rule to correctness. Entropy concentration is not a probability of being right, and the paper's ethics note says unequal error costs need task-specific criteria, yet it tests no calibrated or risk-bounded stop.
- Other backbones and open-ended judging tasks. All three tasks are multiple choice, so transfer to judge-style verdicts on agent outputs is unknown.
- Batched serving. Only one question runs at a time; whether concurrent reads still pay off on a shared GPU is open.

## Topics
[[Topic - decision models]] · [[Topic - open decision models]] · [[Topic - adaptive reasoning depth]]
