---
title: "Qwen-Audio-Jev: A Unified Interface for Audio Decisions"
authors: Ying Fang et al.
date: 2026-10
arxiv: 2610.21614
url: https://arxiv.org/abs/2610.21614
venue: arXiv (preprint, Alibaba Token Foundry)
category: alternative-paradigms
pdf: agent as a judge papers/decision models/open models/papers/Qwen-Audio-Jev - A Unified Interface for Audio Decisions (Fang 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "papers"]
topics: ["decision models", "open decision models"]
---
# Qwen-Audio-Jev: A Unified Interface for Audio Decisions

## One line
Adds a typed decision head (CHOICE, NOUL, SCORE) to the Qwen-Audio-3.1-ASR-Flash-Next audio LLM so that selection, yes/no judgment and rating are read out of one hidden state instead of generated as text,, about 20x faster than the original.

## Method
- **Problem.** Many audio jobs (screening, speaker verification, quality scoring) need a bounded answer. Generating it as text costs latency, and the text still has to be parsed and validated.
- **Idea.** Keep the audio encoder, adaptor and MoE decoder. Put the question and an explicit answer specification (candidate descriptions, the binary proposition, or ordered rating levels with criteria) into the prompt, and take the decoder's hidden state at the last prefix token, before any answer token. Three small linear projections read that one state. CHOICE gives a softmax over up to 64 supplied candidates. NOUL gives a sigmoid probability that the proposition is true. SCORE gives a softmax over up to 10 ordered levels, and the rating is the expected level. The output slots have no fixed meaning: the answer specification defines them for each question, so one head covers scenes, emotions or instruments without a fixed class vocabulary. This follows Jev's typed decision primitives.
- **Why it should work.** The backbone already understands audio given a question, and one forward pass gives the decision. Heterogeneous datasets can be mixed because each example trains only the primitive its labels support. Missing labels add no loss.
- **Training.** Supervised fine-tuning first, with cross-entropy for CHOICE (candidate order shuffled so the model can't learn answer positions), binary cross-entropy for NOUL, and for SCORE a mix of cross-entropy, a CDF term that penalises answers far from the right level, and a loss on the expected rating. An optional second stage (RLCD) treats each decision as a one-step bandit. It samples 32 actions and uses a group reward whose expectation equals the negative Brier score, plus a ranked-probability term for SCORE. The aim is calibrated probabilities, not only right answers.

## Evaluated on
- **One head covers all three answer types.** 18 setups: 8 CHOICE, 4 NOUL, 6 SCORE. Headline results: 78.70% on MMAU-mini, 84.06% on MMSU, 6.50% EER on VoxCeleb1-O, NISQA overall normalised MAE 0.1062 with Pearson 0.821.
- **Quality varies a lot by task.** CHOICE runs from 100% on gender and 92.7% on non-speech sounds down to 57.3% on MELD emotion and 69.9% on MMAR complex QA.
- **Good probability ranking can hide a bad default threshold.** Clotho-AQA and In-the-Wild deepfake detection have nearly equal AUC (0.879 vs 0.876), yet at the 0.5 threshold In-the-Wild misses 57.3% of positives against 24.5% for Clotho-AQA.
- **Speed.** About 20x faster inference than the original backbone. The paper gives no setup, hardware or latency figures behind this number.

## Limitations admitted by the authors
- **Calibration is not shown.** The authors say probabilities do not by themselves establish calibration. They report Brier scores only for NOUL. They give no calibration-error measure and don't evaluate the RLCD stage on its own, so the calibration motive behind RLCD goes untested.
- **Comparative gains, generalisation and deployment efficiency "require further evaluation".** No baseline appears in any results table, not even the generating backbone, so it is unknown whether the head gains or loses accuracy against generating the answer.
- **Several questions about one clip still need one forward pass each.** So the speedup does not extend to asking many questions of one clip.
- **Weak spots they name.** Emotion (MELD 57.3%), complex QA (MMAR 69.9%), deepfake misses (57.3% FNR at 0.5), and synthetic-speech MOS error (VoiceMOS MAE 0.813, worse than every NISQA dimension).

## Limitations found by others

## What it leaves untried
- **A same-backbone comparison.** Score accuracy and calibration of the generating Qwen-Audio model against the head, with and without RLCD. Without it, the claim that 20x speed costs nothing is unsupported.
- **Calibration measures for CHOICE and SCORE.** Reliability diagrams or ECE for all three primitives would show whether the probabilities can drive thresholds and abstention.
- **One pass for many questions.** Reading several questions from one encoded clip would extend the speed gain to the screening workloads the paper targets.

## Topics
[[Topic - decision models]] · [[Topic - open decision models]]
