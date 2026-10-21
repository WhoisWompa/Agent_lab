---
title: "Releasing the Inner Jev: A Simple Recipe for Open Decision Models"
authors: Jonathan Geuter et al.
date: 2026-10
arxiv: 2610.17205
url: https://arxiv.org/abs/2610.17205
venue: arXiv
category: trained-judges-reward-models
pdf: agent as a judge papers/decision models/open models/papers/Releasing the Inner Jev - A Simple Recipe for Open Decision Models (Geuter 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "papers"]
topics: ["decision models", "open decision models", "calibration"]
---
# Releasing the Inner Jev: A Simple Recipe for Open Decision Models

## One line
Shows that an off-the-shelf instruction-tuned open LLM, read out from its answer-letter logits in one forward pass and temperature-scaled, already matches the closed decision model Jev, and that a short LoRA run on top beats it.

## Method
The problem: Jev-style "System One" decision models (state + question + K options in, one probability per option out, no generation) are said to need a special architecture and an RL method for calibrated decisions (RLCD), none of it public. The paper asks whether that is necessary.

The idea is that the capability is already inside instruction-tuned models. The options are labelled A, B, C...; after one forward pass the logits of those letter tokens at the last position are softmaxed over the K real options. Little is thrown away: every backbone puts over 99.4% of next-token mass on the letters. The raw probabilities are overconfident (fitted temperatures of 6.0 for choice and 7.2 for yes/no on Gemma 4 31B), so one temperature per question type is fitted on held-out data; this changes confidence, never the answer.

The training recipe keeps that readout as its starting point: the decision head is the LM-head rows for the letters plus a learned correction initialised at zero, so the untrained model is exactly the zero-shot readout. LoRA adapters and the correction are trained with cross-entropy for 400 steps (about five GPU-hours) on public and LLM-labelled questions. No RL, no reward model.

## Evaluated on
- Zero-shot already matches Jev: Gemma 4 31B scores 79.6 Capability on OpenDecisions (the authors' own 2,352-question validation set) against Jev's 80.1; Qwen3.6-27B scores 79.0. Temperature scaling alone lifts Gemma from 72.9 to 79.6.
- A short LoRA run beats Jev: Gemma 4 31B goes to 84.4 (+4.8 ± 2.0), 4.3 ± 2.5 above Jev, with the best calibration of all systems (92.3). On the official JevBench v1.7 leaderboard it scores 81.5, second, against Jev's 77.1.
- The gain carries to held-out public decision sets, but is smaller: 89.0 macro accuracy against Jev's 88.0 over 9,212 items, with lower calibration error (ECE 0.047 vs 0.066).
- LoRA does the work, not the head: training only the head on a frozen backbone gives 78.9 (no gain over 79.6); LoRA with the head frozen gives 84.9, the same as joint training.

## Limitations admitted by the authors
- OpenDecisions was used to choose the recipe, so it is a development set, not an independent test; the headline 84.4 is optimistic for that reason, and the held-out margin over Jev shrinks to about one accuracy point.
- The recipe does not transfer down the size range: with the same settings Qwen3.6-27B gains 2.2 ± 2.2, Gemma 4 12B loses 0.4 ± 1.8, and Qwen3.5-4B gains nothing until three extra changes, also tuned on OpenDecisions.
- Training lowers calibration for the three smaller models (27B −0.6, 12B −2.2, 4B −0.8), cancelling part of the accuracy gain.
- Possible bias in the labels: Qwen3.6-27B supplies training labels while the related Qwen3.8-27B sits on the evaluation labelling panel; most OpenDecisions items are LLM-written.
- Jev stays ahead on knowledge-heavy multiple choice by 4.0 ± 0.8 points (92.9 vs 88.8), mostly MMLU-Pro, MMLU and WinoGrande, so the claim holds for reading a supplied state, not for knowledge.
- The letter answer depends on option order: after training, the 4B model still flips on about 6% of choice and yes/no questions when the options are reversed.

## Limitations found by others

## What it leaves untried
- Calibration is only post-hoc temperature scaling fitted on a different distribution; putting calibration into the training loss is named but not tried, and matters because fitted temperatures already fail to transfer for the trained Qwen models.
- No abstention: the readout always returns a distribution over the options, and the model was seen answering "None" on items whose options do not fit the state; a learned reject option would matter for judge use where the right answer may be missing.

## Topics
[[Topic - decision models]] · [[Topic - open decision models]] · [[Topic - calibration]]
