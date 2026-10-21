---
title: "OpenJev-RLCD: A Working RLCD Implementation"
authors: Zhimin Gao et al.
date: 2026-09
arxiv: 2609.38850
url: https://arxiv.org/abs/2609.38850
venue: arXiv
category: trained-judges-reward-models
pdf: agent as a judge papers/decision models/open models/papers/OpenJev-RLCD - A Working RLCD Implementation (Gao 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "papers"]
topics: ["decision models", "open decision models", "calibration", "judges as reward signals"]
---
# OpenJev-RLCD: A Working RLCD Implementation

## One line
An open recipe for "reinforcement learning for calibrated decisions": it scores the answer distribution a reasoning model reads out after each of its own rationales with a proper scoring rule, calibrating that readout first and then reinforcing the reasoning with the same score.

## Method
The problem: a decision model (like TypeSafe AI's Jev, whose algorithm is undisclosed) is useful only if its confidence can decide which decisions to automate. Open copies use SFT plus temperature scaling; RLVR's correct-answer reward is not a proper score of anything the model reports, so it makes reasoning models confidently wrong.

The idea: after a sampled rationale ending in "Answer:", the distribution u(r) over option tokens is read out, not sampled, and scored by a strictly proper rule (Brier or log).

Why per rationale: for the Brier score, scoring the mixture of samples equals the average per-rationale score plus the variance of u across rationales. So group or mixture rewards pay a bonus for rationales that disagree, whether or not the disagreement has any basis. With sampled one-hot answers the same identity shows RLVR is the mixture objective minus its Gini-diversity term, so its optimum is the mode, not the true distribution. The per-rationale objective has the unique optimum u(r) = q(x) for every rationale, so a single query is calibrated, provided the outcome does not depend on the model's own rationale.

Optimised naively it fails twice. It switches reasoning off: hedging after an empty rationale is learned faster, and on MMLU-Pro all rationales go empty within about 100 steps, unless a KL anchor is added. And the policy-gradient term, 7 to 12 times larger than the readout gradient, drowns the useful signal in Adam. Hence "calibrate, then reinforce": stage 1 trains only the readout on the model's own on-policy rationales; stage 2 reinforces the rationales with the same proper score as reward, a down-weighted policy-gradient term and a KL anchor to the stage-1 model.

## Evaluated on
- Same accuracy as GRPO, much better ranking of confidence: on GSM8K answer verification, 92.2% vs 91.8% (not significant), but AURC 0.034 vs 0.061, and at a 5% error budget a single query decides 81% of items vs 19% for GRPO. GRPO and RFT need a fitted temperature around 7, RLCD 1.4.
- On knowledge-heavy MMLU-Pro, +5.3 accuracy points over SFT+TS and +5.2 over GRPO+TS. At a 20% error budget it decides 28% of items, vs 16% for SFT+TS and none for any reasoning baseline.
- Stage 1 alone carries most of the gain.
- The stage-2 reward must be proper: continuing with GRPO's correctness reward re-inflates confidence on MMLU-Pro (T from 1.4 to 3.8). RLCD-RL beats it by +1.8 points and -0.035 Brier.
- Under annotator disagreement (ChaosNLI), the per-rationale objective turns reasoning off and only matches cross-entropy (JSD 0.075 vs 0.074). The mixture objective makes rationales random and runs them to the length limit, as the identity predicts.

## Limitations admitted by the authors
- Only a 1.7B model, 400 to 800 steps and three seeds. Larger models or longer training could shift the balance between the two stages.
- GSM8K-Verify is built by the authors with a 0.6B proposer; the 81% coverage figure comes from it.
- Jev is compared only behaviourally. Nothing is claimed about its internal algorithm, so "working RLCD" means a recipe that works, not a reproduction.
- Stage 2 helps where reasoning is computation and is neutral on MMLU-Pro (+0.002 Brier, sign varies by seed). Its benefit cannot be predicted without running it.
- When uncertainty is aleatoric, RL provably cannot beat cross-entropy.

## Limitations found by others

## What it leaves untried
- Agent-state questions: every task is a single-turn QA or verification item. Judging agent trajectories, which is the Jev use case, is never tested.
- Outcomes that depend on the model's own rationale: the calibration guarantee assumes the outcome is independent of the rationale. Decisions that feed back into the world break that assumption, and this is not studied.
- A predictor of when stage 2 pays off (e.g. the gap between direct and reasoned accuracy, 56% vs 87% on GSM8K-Verify), so the RL stage can be skipped where it adds nothing.

## Topics
[[Topic - decision models]] · [[Topic - open decision models]] · [[Topic - calibration]] · [[Topic - judges as reward signals]]
