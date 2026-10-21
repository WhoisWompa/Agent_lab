---
title: "Overconfidence in LLM-as-a-Judge: Diagnosis and Confidence-Driven Solution"
authors: Zailong Tian et al.
date: 2025-08
arxiv: 2508.06225
url: https://arxiv.org/abs/2508.06225
venue: AAAI 2026
category: llm-judge-foundations
pdf: agent as a judge papers/decision models/Overconfidence in LLM-as-a-Judge - Diagnosis and Confidence-Driven Solution (2025).pdf
folder: ["agent as a judge", "decision models"]
topics: ["calibration", "judge and decision-model audits", "LLM and agent judges", "social choice"]
---
# Overconfidence in LLM-as-a-Judge: Diagnosis and Confidence-Driven Solution

## One line
Shows that pairwise LLM judges state far more confidence than their accuracy earns, proposes TH-Score to measure calibration only in the high- and low-confidence bands where routing decisions are made, and proposes LLM-as-a-Fuser, where one LLM reads several judges' verdicts and rationales and issues a final verdict with a confidence.

## Method
- **Problem.** A judge's confidence is only useful if it tracks correctness: then high-confidence verdicts can be auto-accepted and low-confidence ones sent to humans. The authors argue judge benchmarks score accuracy alone, and that current judges are overconfident: they cluster at 90-100% confidence while being right much less often. GPT-4o: ECE 39.25 with self-reported confidence at 49.71% accuracy, chance on a two-way choice.
- **Confidence sources.** Three ways to get a number: the judge states it (self-confidence), the share of 10 sampled verdicts that agree (multiple prompting), or the softmax over the A/B answer-token logits.
- **TH-Score.** Look only at predictions with confidence above 100−ε or below ε (default ε = 0.1). Score = (e^(acc−0.5) − 1) × coverage, where acc is accuracy inside those bands and coverage is the share of samples in them. ECE averages over all bins; a deployment only cares whether the extremes can be trusted. The score rises when many items sit at the extremes and are mostly right, and goes negative below 0.5 accuracy. At ε = 0.05 most models have almost no data in the bands; at 0.15 strong models stop standing out.
- **LLM-as-a-Fuser.** Voting, and voting weighted by confidence or entropy, throw away the judges' reasoning. In the fuser, one LLM gets the question, both answers, and every judge's JSON (verdict, confidence, explanation). It is told to weigh the explanations over the scores and to output its own verdict and confidence. The assumption: confident errors show up as weak rationales, so a reader checking the reasoning can overrule a confident wrong majority.

## Evaluated on
- **Overconfidence is widespread.** On JudgeBench, most of the 14 judges have a large ECE with self-reported confidence: Mistral-Nemo 74.22 at 20.29% accuracy, GPT-4.1-nano 57.03, Llama-3.3-70B 47.37. The best, Qwen3-235B, is still at 11.78.
- **The fuser beats voting.** With Qwen3-235B as fuser: 86.29% accuracy and ECE 6.42, against 81.71% and 8.48 for the best baseline (entropy-weighted voting) and 77.43% and 11.78 for Qwen judging alone.
- **Weak models gain most as fusers.** Mistral-Nemo goes from 20.29% to 67.43% accuracy and its ECE drops by 53.73. That is mostly the ensemble's verdicts passed through.
- **The fuser does not always help.** DeepSeek-R1 as fuser loses 8.29 points of accuracy and its ECE rises by 9.37. GPT-4o stays at 49.71% and its ECE gets worse. GPT-4o overrules the majority wrongly 112 times and correctly 6 times; Qwen3 does so correctly 34 times and wrongly 12.
- **TH-Score barely moves for the best fuser.** Qwen3 as fuser scores 17.38, against 17.52 for self-confidence in Table 1: the metric misses the headline calibration gain.

## Limitations admitted by the authors
- The cause of overconfidence is not investigated; it is left as future work. So there is no account of why the fuser fixes it beyond that it does on one benchmark.
- They call for "more scalable solutions": every item needs every ensemble judge plus a fuser call, a cost never measured.
- ε is a hyperparameter with no principled value. The recommended way to set it is "choose where most models contribute significant data", which makes the score depend on which models are being compared.

## Limitations found by others

## What it leaves untried
- No test outside JudgeBench (350 pairs, one benchmark), and no held-out split. The fuser's gains and the choice of ε = 0.1 are both read off the same data, so whether either carries over to other tasks is open.
- The fuser is never compared to a cheap post-hoc recalibration (for example, temperature scaling of each judge's confidence) or to a voting ensemble over fewer, stronger judges. Without that, it is unclear whether reading rationales helps, or just more models plus a strong final reader.
- TH-Score is checked against nothing downstream. The quality of data filtered by it, or of human-escalation routing, is never measured, though that is the metric's whole motivation.

## Topics
[[Topic - calibration]] · [[Topic - judge and decision-model audits]] · [[Topic - LLM and agent judges]] · [[Topic - social choice]]
