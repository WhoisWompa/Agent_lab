---
title: "Fast Models, Slow Evidence: A Paired and Self-Audited Evaluation of System-1 Decision Models for LLM Agent Harnesses"
authors: Jiawei Li
date: 2026-10
arxiv: 2610.02267
url: https://arxiv.org/abs/2610.02267
venue: arXiv
category: alternative-paradigms
pdf: agent as a judge papers/decision models/open models/evaluations/Fast Models, Slow Evidence - Evaluation of System-1 Decision Models for LLM Agent Harnesses (Li 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "evaluations"]
topics: ["decision models", "judge and decision-model audits", "confidence-gated escalation"]
---
# Fast Models, Slow Evidence: A Paired and Self-Audited Evaluation of System-1 Decision Models for LLM Agent Harnesses

## One line
Compares the open-weight LAYA and hosted JEV System-1 decision models on 11 agent-harness decision points, then audits its own first draft and finds that errors in cost, quality and threshold accounting, not in scored predictions, had changed the deployment advice.

## Method
The problem: an agent harness makes many small typed decisions (which model, which tool, is this context relevant, is this an injection), usually by prompting the working LLM, which spends a full generation on a one-label answer. System-1 models return a class distribution for a typed question in one non-autoregressive pass, and vendors claim LLM-level accuracy at a fraction of the cost. The paper asks where that holds, how stable it is, and what such a model saves as a gate in front of an LLM.

Two parts. First, a paired comparison: identical inputs to both models, confidence read the same way (max class probability; LAYA's own "confidence" field differs from it by 0.299 on average, which would silently break any threshold), differences counted on disagreements. Second, what is new: a self-audit that re-derives every headline number from raw outputs and runs a control for each suspected confound. It targets a rarely discussed failure class: errors in deployment accounting (cost, end-to-end quality, threshold choice) downstream of correctly scored predictions. A gate is judged by the share of traffic still sent to the expensive path and the held-out share of needed cases it skipped.

## Evaluated on
- JEV wins 9 of 11 decision points by +10.8 to +46.0 pp, largest on 60-77-label intent sets (81.0% vs 35.0%).
- Neither model can route between LLMs zero-shot: JEV answers "cheap" 99.5% of the time (50.0%, the constant baseline) and LAYA has AUROC 0.48. RAG relevance is a tie, 61.0% vs 60.5%.
- LAYA is structurally fragile: reversing option order changes 30.3% of its decisions (JEV 1.8%); with 50 nearest-neighbour tool decoys it falls to 31.3%, since its code leaves each option about four tokens. JEV keeps 98.9% where one tool is correct.
- Gates save less than they look: the JEV safety pre-screen cuts review cost by 4.3%, not the 23.9% first reported, because its own tokens were omitted; at a lower threshold it costs 4.7% more. The lasting gain is latency, 34-41% of requests released in about 0.3 s.
- Thresholds picked in-sample for a 5% miss target reach 10-17% misses at the 95th percentile held-out on tracks with 100-200 positives, and exceed the target in about half of splits.
- A "tool-output channel" effect on injection false positives was an artifact: with passages native to tool outputs, JEV stays at 0% in both channels.

## Limitations admitted by the authors
- One version each, zero-shot only; LAYA's fine-tuning path, its main selling point, is untested, so the gap may not hold for adapted LAYA.
- Any single accuracy carries a ±5 pp wording band (rewording moves tracks 5-15 pp), so only rankings, not absolute numbers, are firm; on routing and RAG even the ranking sign flips across wordings.
- Label noise: a blind LLM judge agrees with the dataset on only 12.7% of items both models got wrong, so RAG and safety accuracies are understated.
- Routing labels rest on single runs of a 7B model on mostly multiple-choice items, so the attainable routing accuracy is unknown; the result says zero-shot routing fails on these labels, not that routing is impossible.
- JEV's training data is unknown, so near-perfect scores on public tool and injection sets may partly reflect exposure.
- Gate savings depend on production base rates the study does not observe; the class mixes are synthetic.

## Limitations found by others

## What it leaves untried
- Fine-tuned or per-domain-recalibrated LAYA in the same paired setup; Platt scaling alone cut LAYA's RAG calibration error from 0.22 to 0.027, so the zero-shot verdict may be the wrong one for the open model.
- Gates on real traffic: the savings ceiling (58% for a perfect RAG gate here) comes from synthetic base rates.
- Voting over option permutations for LAYA is recommended but never tested, so whether it repairs the 30% order sensitivity is unknown.

## Topics
[[Topic - decision models]] · [[Topic - judge and decision-model audits]] · [[Topic - confidence-gated escalation]]
