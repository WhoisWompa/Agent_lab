---
title: "VideoJev: System One Model for Video Understanding and Interaction"
authors: Yuhan Zhu et al.
date: 2026-10
arxiv: 2610.18615
url: https://arxiv.org/abs/2610.18615
venue: arXiv
category: alternative-paradigms
pdf: agent as a judge papers/decision models/open models/papers/VideoJev - System One Model for Video Understanding and Interaction (Zhu 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "papers"]
topics: ["decision models", "open decision models"]
---
# VideoJev: System One Model for Video Understanding and Interaction

## One line
VideoJev swaps a video MLLM's text-generating head for a shared scoring head that rates candidate time intervals or answer options against the video, so one encoded video can answer many grounding and multiple-choice questions in a single forward pass, at the accuracy of reasoning models and over 100x faster.

## Method
- **Problem.** Visual agents ask many small, structured questions about the same footage ("has the ingredient been added?", "when did X happen?"). Video MLLMs answer each by generating timestamps or answer text token by token, which is slow and wasteful when the output is a compact decision. The premise: open-ended agent behaviour can be built from structured visual judgments, without open-ended generation at every step.
- **Candidate scoring instead of decoding.** The model (built on Qwen3.5-4B and Qwen3.6-35B-A3B) sees the video, then a task instruction, a query and a list of candidates, each closed by a new `<|option_end|>` token, with a `<|decide|>` token at the end. The final MLP and language head are removed. The candidate and decision hidden states are projected, normalised, and compared by cosine similarity to give a logit per candidate. The same head serves both tasks; only the candidates and the output rule differ.
- **Temporal grounding as interval membership.** The timeline is cut into one interval per frame pair, and each interval's timestamp text is a candidate. A sigmoid gives the probability that the interval belongs to the event. Training uses per-interval BCE plus a duration-weighted soft IoU loss, so the model is rewarded for covering the whole event and not just flagging single frames. Decoding takes the contiguous run with the largest sum of threshold-adjusted logits (Kadane's algorithm, linear time, fixed threshold 0.25), giving exactly one span.
- **Video QA as option selection.** A softmax over option logits, trained with cross-entropy. Options are shuffled during training to break position shortcuts.
- **Reusing the video.** Causal attention means the video prefix does not depend on later queries, so it is encoded once. *Cached inference* branches each new query off the cached prefix. *Joint inference* puts many queries after one prefix and reads every `<|decide|>` in one forward pass. Later queries can see earlier query text but no answers. Training uses the same multi-query layout.
- **Why it should work.** The readout is supervised on the exact decision the task needs, and pre-MLP features already carry semantic similarity.

## Evaluated on
- **Better grounding than generative models, about 3x faster.** Mean mIoU over three benchmarks is 65.3 (4B) and 67.7 (35B-A3B), +6.7 and +10.8 over the backbones, and 3.3 above TimeLens2-4B. Latency per query is 0.276s vs 0.763s for the 4B backbone.
- **QA matches Thinking mode at 1/100 the time.** The 4B mean is 74.3 vs 74.9 for Qwen3.5-4B Thinking (1.123s vs 144.9s). The 35B-A3B mean is 79.5 vs 78.8 for Qwen3.6 Thinking (1.493s vs 149.8s). Thinking still wins on Video-MME and MLVU.
- **The gain comes from the head, not only the data.** On identical training data, an autoregressive fine-tune trails VideoJev-4B by 1.3 mIoU and 1.9 QA points.
- **Extra queries are almost free.** Going from 1 to 10 joint queries adds 55ms for grounding and 31ms for QA, and accuracy does not drop: Joint beats Cached in 13 of 14 comparisons.
- **Confidence carries signal.** On LVBench, 35B-A3B's predictions with confidence of at least 99% are 95.8% correct (591 of them), against 73.4% overall.

## Limitations admitted by the authors
- **Overconfident probabilities.** Mean ECE over four benchmarks is 8.65 (4B) and 8.13 (35B-A3B) percentage points, and up to 11.8 on LVBench. There is no calibration training, unlike Jev, which uses RL for it. So the scores cannot yet be used as-is to decide when to defer.
- **Closed-set only.** The model scores candidates someone else supplies. It covers grounding (one contiguous span) and multiple-choice QA, and leaves action recognition, state checks and open-ended goals to future work. An agent still needs a planner to propose the candidates.
- **No streaming.** The prefix is a fixed, fully encoded video. Live streams would need incremental encoding and memory management.
- **Joint inference leaks query text.** Later queries attend to earlier questions. The authors checked that no answers leak, but did not isolate the effect. The small gain over Cached is attributed, without proof, to matching the training layout.
- **Thinking still wins some reasoning-heavy benchmarks.** It keeps an edge on Video-MME and MLVU, and both models fail a small-object counting case.

## Limitations found by others

## What it leaves untried
- **Calibration.** Temperature scaling or calibration-aware training on held-out data. The paper proposes it but does not run it, though the system-one/system-two hand-off it pitches depends on trustworthy confidence.
- **A real agent loop.** It never wires VideoJev under a planner that generates candidates, so the claim that structured judgments compose into open-ended workflows is untested. Every result is on benchmark candidates written by humans.
- **Joint vs Cached consistency.** No test of whether a query's answer changes depending on which other queries share its forward pass. That matters if a judge's verdict should not depend on what it was asked alongside.

## Topics
[[Topic - decision models]] · [[Topic - open decision models]]
