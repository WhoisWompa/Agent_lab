---
title: "Benchmarking candidate coverage and rejection policy transfer in typed decision models"
authors: Jiawen Lu et al.
date: 2026-10
arxiv: 2610.03387
url: https://arxiv.org/abs/2610.03387
venue: arXiv
category: agent-evaluation-benchmarks
pdf: agent as a judge papers/decision models/open models/evaluations/Benchmarking Candidate Coverage and Rejection Policy Transfer in Typed Decision Models (Lu 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "evaluations"]
topics: ["decision models", "abstention and fallback", "judge and decision-model audits"]
---
# Benchmarking candidate coverage and rejection policy transfer in typed decision models

## One line
A benchmark showing that the "none of these" rejection thresholds of typed decision models (Laya, Jev, against Qwen2.5-7B) often stop working when moved to another task or candidate setup, and that different sources of missing answers give different tradeoffs.

## Method
- **Problem.** A typed decision model picks one option from a candidate list supplied at request time. When the retriever or caller leaves the right answer out, the model should reject. A p(none) threshold tuned in one setup gets reused elsewhere unchecked.
- **Two rates, kept apart.** Coverage G = 1 when the reference label is in the menu. The benchmark reports detection D = P(reject | missing) and false rejection F = P(reject | covered) side by side, next to selection accuracy. Normalising over the menu does not reveal whether the answer is in it, so selection, score quality and rejection are measured separately. A single D−F number hides very different regimes. In the earlier discovery study, Laya on TREC has D/F 97.2/69.7 and Jev has 24.8/0.0, yet their D−F gaps are nearly equal (27.5 vs 24.8).
- **Transfer test.** A threshold is fitted on 80 source pairs (best detection with calibration F ≤ 5%), then frozen and applied to every other task. It is compared with recalibrating on the target using the same number of labels.
- **Three kinds of missing answer, never pooled:** artificial omission (the right label swapped out of a matched menu), natural retrieval misses (a BM25 top-k menu that happens to leave out the reference), and global out-of-scope queries (intents outside the ontology).
- Assumes public reference labels define coverage correctly.

## Evaluated on
- **Source thresholds often break on a new task:** above 5% target F in 6 of 12 transfers for both Laya and Jev. Jev's DBpedia threshold (τ = 0.06) gives D = 92.2% but F = 69.3% on Emotion. Laya's AG News threshold gives F = 66.7% on TREC.
- **A cautious threshold can switch rejection off.** Jev's Emotion threshold is τ = 1.00, so the strict p(none) > τ rule never fires and every target gets D/F = 0/0.
- **Better retrieval coverage can raise false rejection.** On CLINC150, going from k = 2 to k = 10 lifts coverage from 89.7% to 98.3%. Over the same change Laya's OOS detection rises from 83.0% to 99.0%, but its covered F rises from 15.2% to 48.8%.
- **Equal accuracy, very different rejection.** On DBpedia k = 13, Jev and Qwen select correctly 97.4% and 96.9% of the time but detect 82.4% vs 25.0% of missing answers.
- **Score quality predicts which local policy works.** On DBpedia, Jev's none-score AUROC is 0.987 vs Laya's 0.865, and calibrated D/F is 98.8/3.6 vs 34.0/2.4.
- **Interface wording moves the operating point.** Neutral option IDs cut Qwen's detection by 30.6 points on DBpedia. Task-aligned NONE wording raises Laya's Emotion detection by 25.0 points.

## Limitations admitted by the authors
- Coverage follows public labels. Overlapping class descriptions can leave an acceptable answer in the menu after the label is removed.
- The samples are roughly balanced, unlike real deployment frequencies. Rare classes have few examples: at k = 10 the natural-miss detection rests on only five queries.
- Only one checkpoint per model is tested. A task change mixes distribution shift with rubric shift, so the results describe these interfaces only.
- The 5% calibration constraint gives no population-level risk guarantee. Even target recalibration goes above 5% test F on DBpedia (6.0% Laya, 7.1% Jev).
-- The BM25 scope gate rejects 0% of natural menus by construction, because it shares the retriever's winner. A rejection gate tied to the retriever cannot catch that retriever's misses.

## Limitations found by others

## What it leaves untried
- No remedy is proposed. Nothing is tried to make thresholds transfer, such as conformal or risk-controlled calibration, or recalibrating with fewer labels.
- No retriever-independent rejection gate or second-stage verifier is tested, though the coupling problem is shown.
- Larger natural-miss samples and more models are named as next steps but not done, so the natural-miss and OOS numbers stay thin.

## Topics
[[Topic - decision models]] · [[Topic - abstention and fallback]] · [[Topic - judge and decision-model audits]]
