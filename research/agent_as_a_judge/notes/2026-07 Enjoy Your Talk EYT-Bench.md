---
title: "Enjoy Your Talk: A Human-Centered Benchmark for Multi-Turn Dialogue with Decoupled User Simulation, Target Modeling, and Judging"
authors: Jinglan Gong et al.
date: 2026-07
arxiv: 2607.10428
url: https://arxiv.org/abs/2607.10428
venue: arXiv
category: agent-evaluation-benchmarks
pdf: agent as a judge papers/Enjoy Your Talk - EYT-Bench, Decoupled User Simulation and Judging (2026).pdf
folder: ["agent as a judge"]
topics: ["user simulation", "LLM and agent judges"]
---
# Enjoy Your Talk: A Human-Centered Benchmark for Multi-Turn Dialogue with Decoupled User Simulation, Target Modeling, and Judging

## One line
A multi-turn chat benchmark that splits user simulator, target model and LLM judge into separate roles, and adds trajectory metrics (intent drift, final-intent completion) next to rubric scores for empathy, persona fit and human-likeness.

## Method
The problem: multi-turn benchmarks often use one model family as simulator, target and judge, which inflates scores through self-preference, and they score turns one at a time without checking whether the conversation reaches the user's goal. EYT-Bench sets up three roles:
- **Simulator**: plays a human-curated persona (structured demographics or long free-text profiles). Each turn it writes the user message, gold labels (explicit intent, latent intent, emotion) and its progress toward a one-sentence "final intent"; two consecutive "achieved" reports end the dialogue.
- **Target**: first predicts the user's labels with a separate prompt, then writes its reply. The two prompts are kept apart because merging them, by the authors' account, "inflates the subjective interaction scores".
- **Judge**: scores each turn on three dimensions of five sub-criteria each, then decides whether the final intent was met (FICR) and gives a 1-5 satisfaction score.

Intent drift is the mean cosine distance between gold and predicted intent embeddings; an optional warm-up weighting gives the first two turns weight α. The assumption: keeping the roles in different families removes self-preference.

## Evaluated on
- **Subjective scores barely separate models; objective tracking does.** Almost every model's Empathy falls within [3.45, 3.86] out of 5. On the PersonaMem pool, latent-intent accuracy runs from 0.08 to 0.80.
- **Reasoning matters only with long personas.** Switching on thinking in Gemma-4 raises latent-intent accuracy by +0.47 to +0.50 on PersonaMem but only +0.08 to +0.20 on Nemotron. Subjective scores move by |Δ| ≤ 0.10. Their explanation, that Nemotron personas leak the latent label, is untested.
- **The persona pool changes the results.** FICR is ≥ 0.95 for 11 of 13 API models on Nemotron but spreads 0.525 to 0.886 on PersonaMem.
- **Swapping the judge shifts scores but supposedly keeps rankings.** With DeepSeek-V4-Pro as judge, subjective scores drop by 0.55 to 0.66 Likert points and mean satisfaction changes by only 1.8/100. But the per-model Empathy changes run from +31 to -61, and no rank correlation is reported, so the "rankings preserved" claim has no number behind it.
- **The judge roughly tracks humans, with caveats.** Against human ratings, r = 0.87 on Empathy, 0.74 on Persona and 0.58 on Anthropomorphic. The judge rates higher than humans by 5.4 to 9.0/100, and by 16/100 for Claude-Sonnet. Only 59 turn-cells, and annotators could see the judge's scores.

## Limitations admitted by the authors
- **Simulator and judge are the same model** (Gemini-3.1-Pro-Thinking) – the three-way split breaks at its centre. The cross-judge test limits the residual bias to ≤ 0.66 Likert points but does not remove it.
- **FICR is decided by an LLM, not humans.** The human study is only a pilot, with anchoring risk because judge scores were visible.
- **The reasoning result rests on one model family.** Gemma-4 is the only family with paired thinking on/off variants.
- **The cross-judge test is small**: 42 pairs per the limitations, 46 per the table.
- **Small gaps are noise.** At 100 dialogues per pool, differences below ~0.05 (subjective) or ~0.03 (accuracy) are not significant.

## Limitations found by others

## What it leaves untried
- **Gold labels from a model that is not also a target.** The gold labels and the decision to stop come from Gemini, which is also scored as a target, so Gemini may be graded against its own idea of the user. Human gold labels, or a simulator outside every target family, would test whether the 9× objective gap is real.
- **A true warm-up test, and matching prompts and gold labels.** At the main setting (α = 0.10, T = 10) every turn gets weight 0.10, so a full-length dialogue's "warm-up weighted" score equals its unweighted one; only early-stopped dialogues (mean length ≈ 7.8) are reweighted at all. Also, the target's prediction prompt offers only 7 of the 8 latent intents and an older 10-label emotion list, while the gold labels use 15 emotions. Part of the low accuracy may be labels the target cannot output at all. Matching the label sets and choosing α ≠ 1/T would separate these effects.

## Topics
[[Topic - user simulation]] · [[Topic - LLM and agent judges]]
