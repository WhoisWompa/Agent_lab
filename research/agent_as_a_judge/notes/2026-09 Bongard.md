---
title: "Bongard: Training Machine Intuition. An Open Encoder-Decoder Model for Probabilistic Judgment"
authors: Li Ding et al.
date: 2026-09
arxiv: 2609.39111
url: https://arxiv.org/abs/2609.39111
venue: arXiv (AgentBull technical report)
category: trained-judges-reward-models
pdf: agent as a judge papers/decision models/open models/papers/Bongard - Training Machine Intuition (Ding 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "papers"]
topics: ["decision models", "open decision models", "calibration"]
---
# Bongard: Training Machine Intuition

## One line
An open 4B-4B encoder-decoder decision model that reads a state once, answers many typed questions about it with a trained probability head, and is trained on one GPU through supervised judgments, contrastive alignment and sandbox outcome distributions.

## Method
Problem: open System One models mostly read letter or yes/no token logits from decoder-only LLMs, which depend on the tokeniser, label-word priors and option position. And when several questions concern one state, the state is read causally, so early tokens never see later ones.

Solution, three parts:
- **Architecture.** A T5Gemma 2 encoder reads the state bidirectionally, once. Each question is a separate decoder sequence that cross-attends to the shared state, with no attention between questions, so N questions cost one encoder pass and about N/8 decoder calls. A 1.3M-parameter bilinear head scores each candidate, given in full by name and description, against the end-of-question state; a softmax gives the distribution. In a probe, forcing the encoder to read forward only cut accuracy from 69.8% to 64.6% and raised NLL more than fourfold.
- **Stage 2, JEPA without a next-token anchor.** After supervised stage 1, all decision representations point the same way: raw cosine between unrelated readouts is 0.93-0.996, so cosine alignment has no signal. And the representation did not encode the answer: on questions answered at 99.6%, it sat closer to the wrong option's "no" than the correct option's "yes". The fix subtracts the batch mean, uses InfoNCE against the batch for separately encoded pairs (query/passage, image/content, world+action/next state), and contrasts the correct "yes" with a wrong "no" under the same evidence so their shared template cancels.
- **Stage 3, outcome learning.** Each legal action in a sandbox is labelled with an outcome distribution from rollouts or an exact oracle, and trained on with cross-entropy. The argument: a policy gradient with reward (correct minus q) has the Brier gradient in expectation, so it converges to the true probability, whereas a correctness-only reward pushes the top class to 1. When the environment reveals the outcome, the direct loss gives that gradient without sampling noise.

## Evaluated on
- Accurate and better calibrated than Jev: 78.05% on DecisionBench (23,900 rows, 4th of 61) vs Jev 1.13 at 72.0%; ECE 0.063 vs 0.128, NLL 0.72 vs 2.43.
- Stage 2 makes judgments consistent across rephrasings: held-out re-expressions 75.7% to 85.9%, logical complements 44.8% to 71.1%. A matched short control isolates the alignment terms: question-to-answer retrieval 2.3% to 56.6%.
- Stage 3 helps on held-out sets: frontier-style decisions 45.2% to 73.9%, hard-style 34.9% to 50.5%.
- Knows when nothing favours an option: 0.500 on a fair coin (Jev 0.80); mean KL from uniform 0.0009 vs Jev's 0.769.
- Cheap: 36 ms median per request, 32 questions on one state in 221 ms instead of 1.16 s, about $4.4 per million decisions vs $40 for Jev.
- Mixed against Jev on identical items: leads on 6 of 24 benchmarks (Banking77 93.1 vs 79.8), trails by more than three points on 9.

## Limitations admitted by the authors
- The representation gain is not shown to help decisions: the only control isolating the alignment terms is short and shows reshaped geometry, no decision gain.
- Stage 2 raised overconfidence (ECE 0.12 to 0.15); post-hoc temperatures of 1.2-2.15 are what repair calibration.
- Stage 3 is tracked on a panel from its own environments; judging consequences in unseen environments is untested.
- It tends to accept wrong worked answers as correct, which matches its largest deficit to Jev: JudgeBench 55.4% vs 79.7%, with prompt injection (56.9 vs 75.9) and toxicity (53.5 vs 67.5) also behind.
- Question-aware encoding breaks isolation: an answer can change when other questions' instructions join the request.
- Choice probabilities are not order-invariant, since each candidate sees only earlier ones; rotation averaging exists but is off by default.

## Limitations found by others

## What it leaves untried
- A full-length stage-2 run with the alignment weight at zero, plus a head that reads the reshaped representation; without both, JEPA's effect on decisions is unknown.
- Outcome judgment in environments held out from stage 3, the normal case for a judge.
- A large encoder with a small decoder, which the architecture argument motivates but only the balanced 4B-4B was tried.

## Topics
[[Topic - decision models]] · [[Topic - open decision models]] · [[Topic - calibration]]
