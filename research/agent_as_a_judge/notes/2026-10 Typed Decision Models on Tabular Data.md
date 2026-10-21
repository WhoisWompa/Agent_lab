---
title: "Typed Decision Models on Tabular Data"
authors: Baowen Zhang et al.
date: 2026-10
arxiv: 2610.19536
url: https://arxiv.org/abs/2610.19536
venue: arXiv
category: alternative-paradigms
pdf: agent as a judge papers/decision models/open models/papers/Typed Decision Models on Tabular Data (Zhang 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "papers"]
topics: ["decision models", "judge and decision-model audits", "presentation sensitivity"]
---
# Typed Decision Models on Tabular Data

## One line
Tests typed decision models against LLMs on fixed-answer table decisions and finds them cheaper and as accurate, robust to question wording but not to table layout, with their probability marking which decisions will flip.

## Method
The problem: LLMs used for tabular decisions must decode text and map it to an option, costly per decision, and their answers shift with column order, row format and option wording. Typed decision models instead return one probability per fixed option in a single pass, trained for calibration (RLCD for Jev, proper scoring rules for the open-weight Clef and Kev-27B). Whether that interface also brings robustness was untested, since a decision model still reads the table as text.

The idea is a robustness probe built from information-preserving rewrites: 21 types of change that keep every cell and header recoverable (renamed or reordered options, paraphrases; shuffled columns and rows, transposition, other formats such as JSON or Markdown). A decision "flips" if it differs from the original-request decision, and flips are compared against each model's re-send rate (flips from sending the identical request again) so that noise is separated from sensitivity. A decision is "fragile" if any table rewrite flips it.

The confidence argument: a flip happens when a rewrite pushes the margin (log-probability gap between chosen and next-best option) below zero. If rewrites add a small, roughly item-independent shift, only low-margin decisions flip, so the model's own probability should predict fragility, and flips should cancel in accuracy because borderline items are right about as often as wrong.

## Evaluated on
- Practical: decision models match LLMs and lead on two of three tasks (Jev 89.7 TabFact accuracy vs GPT-6 Luna 79.0; Kev-27B 81.2 anomaly AUROC vs 77.3), though GPT-6 Luna leads row classification (62.5 vs 61.2 Macro-F1 for Luna Decisions). Jev runs 0.08 s per row vs 1.62 s for GPT-6 Luna, which costs 1.6 to 8 times as much per decision.
- Robust to question wording: renaming or reordering options flips 2–8% of Jev/Clef/Kev-27B classifications, at most 5.5 points above re-send, vs 14–30% for the open-weight LLMs. GPT-6 Luna Decisions is the exception: reversing options flips 23% of classifications despite a 0.0% re-send rate, and 92–100% of its flips move to the option now listed first.
- Not robust to table organization: other row formats flip 12–21% of every model's classifications, about ten times the open-weight re-send rate; for every model about a third of row decisions flip under some table rewrite (31.7–42.8%), while Macro-F1 moves under a point for some models.
- Confidence predicts fragility: flip AUROC 0.82–0.93 for decision models across tasks; among their top-25% most confident items only 0.1–5% flip (Luna Decisions on TabFact 15.5%) vs about a third overall. LLM ten-draw agreement is weaker, and stated confidence the weakest (e.g. 0.58 flip AUROC for GPT-6 Luna on TabFact).
- Usable: re-querying only the 25% least confident rows in other formats recovers 79–89% of the gain of re-querying all rows, vs 23–44% for random rows.

## Limitations admitted by the authors
- Confidence tracks stability, not correctness: stable-but-wrong decisions carry nearly the same confidence as stable-and-right ones (0.67–0.86 vs 0.76–0.90) and make up 17–23% of decisions in row classification and anomaly detection, so no instability signal can catch them.
- Each model is tested in one version; Jev and GPT-6 Luna Decisions are closed, OpenAI does not document how the Decisions API computes probabilities, and the API was in public beta, so results may not hold across versions.
- Rewrites exclude column renaming and unit conversion, so the paper says little about robustness to those.
- Beyond about 64 labelled rows, TabPFN-3.5 and trained models beat every in-context model, and decision models' shorter context windows limit how many rows they can read.

## Limitations found by others

## What it leaves untried
- Training decision models on table rewrites (e.g. via RLCD) to make them invariant to format and order; the authors name table organization as the main limitation but do not attempt the fix.
- A combined system where the decision model handles most rows and an LLM explains or reviews the least confident ones, proposed but not built.
- Detecting stable-but-wrong decisions, the 17–23% that confidence and flip checks both miss; this matters most for decision models used as judges.

## Topics
[[Topic - decision models]] · [[Topic - judge and decision-model audits]] · [[Topic - presentation sensitivity]]
