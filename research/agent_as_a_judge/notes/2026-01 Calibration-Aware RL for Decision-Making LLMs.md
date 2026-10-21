---
title: Balancing Classification and Calibration Performance in Decision-Making LLMs via Calibration Aware Reinforcement Learning
authors: Duygu Nur Yaldiz et al.
date: 2026-01
arxiv: 2601.13284
url: https://arxiv.org/abs/2601.13284
venue: arXiv
category: trained-judges-reward-models
pdf: agent as a judge papers/decision models/open models/papers/Calibration-Aware RL for Decision-Making LLMs (2026).pdf
folder: ["agent as a judge", "decision models", "open models", "papers"]
topics: ["calibration", "open decision models", "judges as reward signals"]
---
# Balancing Classification and Calibration Performance in Decision-Making LLMs via Calibration Aware Reinforcement Learning

## One line
Shows that RL with verifiable rewards leaves reasoning classifiers near-certain on every verdict because the final decision token only copies the reasoning's conclusion, and fixes it by training that one token with a cross-entropy loss toward one-hot when right and uniform when wrong.

## Method
The problem: a model that reasons and then emits one decision token (A/B/C, Safe/Unsafe) is used as a classifier or guard, with confidence read off that token's probability in one pass. To route doubtful cases to a human or bigger model, that probability must be calibrated. The paper finds the two usual fine-tuning routes split: SFT on the label calibrates, while GRPO-style RLVR raises accuracy more but leaves almost every prediction near confidence 1, so the score carries little signal.

The diagnosis has two parts. First, RL can only upweight behaviour the base model already samples, and there are no calibrated rollouts to upweight: 94.6% to 99.9% of sampled trajectories end with a decision-token probability above 0.99, correct or not. Second, the decision token is an extraction step, not an assessment: when the model's own reasoning is replaced with reasoning for the opposite label, the answer flips in 92% to 100% of cases and the flipped answer still gets probability near 1. So the token measures how clearly the trace points at a label, not whether the label is true.

GRPO's advantage is zeroed on the decision token and kept for all reasoning tokens; the decision token instead gets a cross-entropy loss, weighted by λ, whose target is one-hot on the right label when the rollout is correct and uniform over the options when it is wrong. The uniform target is the floor on purpose: pushing a wrong answer's probability below 1/|C| would flip the greedy output away from what the reasoning concluded, breaking reasoning-decision consistency and the RL reward.

## Evaluated on
- RLVR gains accuracy but not calibration: GRPO averages about 3 points more accuracy than SFT, yet its ECE stays high (Qwen3-1.7B on CommonsenseQA: 24.39 vs SFT 7.36); its confidence histogram stays like the base model's.
- The method keeps GRPO accuracy and cuts ECE: on CommonsenseQA ECE goes 24.39 to 15.97 (1.7B), 16.98 to 12.91 (4B), 14.80 to 10.55 (8B), with accuracy within a point except 4B (81.84 to 79.16).
- It holds out of distribution, sometimes beating SFT: OpenBookQA ECE 1.91 and 1.83 (4B, 8B) vs SFT 4.76 and 4.29; XSTest 8B 6.41 vs SFT 6.84 at higher accuracy (88.67 vs 86.78).
- It does not reach SFT in-domain: OpenAI Moderation ECE 7.11 vs SFT 5.26 (4B) and 3.91 (8B).
- Post-hoc calibration stacks on top: isotonic regression after the method gives the lowest ECE in most cells (OpenAI 4B: 2.8 vs 4.85 for isotonic on GRPO), though not all (XSTest 8B: 3.52 vs 1.62 for GRPO plus isotonic).

## Limitations admitted by the authors
- Only the Qwen3 family up to 8B was tested, for legal and compute reasons; the claim that the extraction effect is structural and not model-specific is argued, not shown.
- Confidence is defined as one decision token's probability; open-ended generation, where there is no single verdict token, is out of scope, and the proposed extension to a dedicated correctness token needs claim extraction they did not build.
- Whether RLVR would also miscalibrate a well-calibrated base model is untested; the argument is only that reward pushes any correct 0.7 toward 1.
- Better-calibrated scores are dual-use: they can show an attacker where the decision boundary is, so they suggest keeping them internal for routing.

## Limitations found by others

## What it leaves untried
- Putting uncertainty into the reasoning itself: the fix makes the final token hedge while the trace still argues one way with full conviction, so confidence and stated reasoning can disagree; rewarding traces that weigh both labels was not tried.
- A sweep of λ and a held-out checkpoint choice: λ is fixed at 0.001 and the best checkpoint is picked on the test set, so how robust the accuracy-calibration balance is remains unknown.
- Use as a judge of agent outputs, where verdicts follow long traces and the extraction effect should be strongest.

## Topics
[[Topic - calibration]] · [[Topic - open decision models]] · [[Topic - judges as reward signals]]
