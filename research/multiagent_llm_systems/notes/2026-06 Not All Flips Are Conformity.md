---
title: Not All Flips Are Conformity: Decomposing Stance Convergence in Multi-Agent LLM Debate
authors: Xiqi Hao et al.
date: 2026-06
arxiv: 2606.00820
url: https://arxiv.org/abs/2606.00820
venue: arXiv
category: failure-analysis-survey
pdf: research/multiagent_llm_systems/pdfs/2606.00820.pdf
folder: ["multiagent_llm_systems"]
topics: ["multi-agent debate and consensus"]
---
# Not All Flips Are Conformity: Decomposing Stance Convergence in Multi-Agent LLM Debate

## One line
Adds a no-peer control to multi-agent debate and shows that answer changes and convergence are not evidence that peers helped, because many flips happen without peers and peer adoption can correct, corrupt, or leave an answer wrong.

## Method
Debate is usually judged by how often agents change answers and how much they converge. The paper argues this cannot show that peers improved anything: an agent may change just because it is asked to reconsider, and a move toward a peer may fix an error, introduce one, or swap one wrong answer for another.

The fix is a matched counterfactual. Five agents answer a multiple-choice question alone (Round 0). On questions where they disagree, each agent is re-asked from the same starting answer under three parallel conditions: self-reflection (no peer information), stance-only (peers' answers shown), and full reasoning (peers' answers plus their reasoning). Changes are then sorted by source:
- Reconsideration instability: the agent changes with no peers.
- Strict conformity: stable under self-reflection, but moves to a peer's answer when stances are shown.
- Reasoning-only peer adoption: stable under both, moves only when peer reasoning is shown.

Each adoption is also labelled by correctness: correct-to-wrong (harmful), wrong-to-correct (beneficial), or wrong-to-wrong. The paper then asks whether harmful adoption can be predicted and suppressed. The labels describe observable patterns, not a proof of why the agent moved.

## Evaluated on
Mainly five GPT-4o agents on MMLU-Pro (1,040 disagreement questions, 5,200 agent-question pairs), with checks on GPQA-Diamond, BBEH, AGIEval, DeepSeek-V4-Flash and Qwen3-Plus.
- A large share of flips need no peers: 36.98% of pairs change under self-reflection alone, against 46.85% with stances and 50.56% with full reasoning. Strict conformity is 29.30% of the self-reflection-stable pairs (960 of 3,277).
- Adoption has no single direction. Strict conformity splits 30.7% correct-to-wrong, 36.4% wrong-to-correct and 32.9% wrong-to-wrong. Reasoning-only adoption splits 34.1% harmful, 30.0% beneficial and 35.9% wrong-to-wrong.
- Correction needs a correct peer to exist. Of wrong, self-reflection-stable agents, 49.2% have no correct peer and 11.3% face a correct-peer majority. Controlled with ground-truth peer answers, accuracy goes 5.6%, 14.0%, 61.2%, 89.2% as correct peers go from 0 to 3 of 4. With support standardized, beneficial adoption exceeds harmful by 8.75 points under stance-only (CI -13.44 to -4.27).
- Individual gains do not become group gains. Individual accuracy rises from 42.17% (self-reflection) to 45.87% (full reasoning), yet majority-vote accuracy is 77.35% for both, with 57% more tokens for full reasoning (paired difference 0.00 points, CI -0.59 to +0.59). Majority-vote accuracy without any round 1 is 76.22%.
- Plausible wrong reasoning is the most persuasive material. In a one-peer test on 500 selected anchors, GPT-4o adopts a constructed wrong answer 64.4% of the time with a stance, 78.2% with generic non-solving text, and 87.0% with question-specific wrong reasoning. The generic-text effect differs across models (DeepSeek-V4-Flash falls 12 points from assertion to generic text), but the specific-wrong-reasoning jump is positive for all three.
- Adoption can be predicted but not usefully mitigated. A Round 0 feature model predicts who will adopt (AUC 0.804) but only weakly predicts who will be harmed (AUC 0.661). An independence prompt aimed at the top 20% by risk cuts harmful, beneficial and wrong-to-wrong adoption alike, with no detectable accuracy gain. With ground-truth correctness used to pick targets, it raises accuracy 14.63 points in the high-risk group, which is not deployable.

## Limitations admitted by the authors
- Primary results use homogeneous GPT-4o agents and one round of peer exposure, so heterogeneous teams and multi-round compounding are untested.
- The direction result is weak outside the primary setting. Wrong-to-correct is at least as frequent as correct-to-wrong in all eight model-benchmark combinations, but only the GPT-4o MMLU-Pro interval excludes 50% (54.2%, CI 50.5 to 57.9).
- Rates are model specific. The self-reflection flip rate is 11.91% for DeepSeek-V4-Flash and 74.07% for Qwen3-Plus, and the ordering of flip rates across conditions fails for Qwen3-Plus.
- The self-reflection baseline depends on wording: a neutral "answer again" changes 8.8% of answers and an explicit "reconsider" changes 16.7%. Strict conformity may also miss adoption when no-peer answers are stochastic.
- The persuasion experiment uses susceptibility-selected anchors, one peer, constructed materials, and assigned priors that match the real Round 0 answer for only 253 of 500 anchors. Its rates are not population estimates, and the materials differ in length (about 100 to 130 tokens) as well as content.
- Only verifiable multiple-choice tasks, so open-ended or subjective debate is untested.

## Limitations found by others

## What it leaves untried
- Verification-guided debate: the paper concludes that a correctness signal or verifier is needed to tell beneficial from harmful adoption, but does not build or test one.
- Heterogeneous model teams and multiple rounds, where correct peers may be more available (49.2% of wrong agents had none here).

## Topics
[[Topic - multi-agent debate and consensus]]
