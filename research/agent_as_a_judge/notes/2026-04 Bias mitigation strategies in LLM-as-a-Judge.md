---
title: Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines
authors: Sadman Kabir Soumik
date: 2026-04
arxiv: 2604.23178
url: https://arxiv.org/abs/2604.23178
venue: TMLR 2026
category: llm-judge-foundations
topics: ["judge and decision-model audits", "LLM and agent judges", "presentation sensitivity"]
---
# Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines

## One line
Head-to-head test of nine debiasing strategies on five 2025-26 judges: style (markdown) bias dominates, position bias is now small, and a debiased mid-tier judge beats frontier judges at 1/15 the cost.

## Method
Five judges from Google, Anthropic, OpenAI, Meta; three benchmarks (MT-Bench n=400, LLMBar n=200, custom controlled n=375); four bias types; nine strategies including a combined budget strategy; Holm-Bonferroni correction.

## Evaluated on
Best: Gemini 2.5 Flash + Combined Budget 71.0% agreement (kappa 0.549) at ~$0.001/eval vs Claude Sonnet 4 69.5% at ~$0.015. Style bias 0.10-0.76 (favouring markdown) vs position bias <=0.04. Length-aware verbosity: Gemini Pro/Flash/Llama prefer longer (+0.24 to +0.44), Claude prefers concise (-0.12), GPT-4o neutral (-0.04); all pick complete over truncated (0.88-1.00). Significant debiasing gains: Claude S8 +11.5 pp, Flash S8 +7.5 pp, Claude S5 +7.3 pp, Flash S1 +4.7, Llama S8 +4.5.

## Limitations admitted by the authors
- Agreement ceilings near 70% even with best strategy; single author; benchmarks are preference-based.

## Limitations found by others


## What it leaves untried
- Testing whether the gains hold on objective-correctness sets (JudgeBench, RewardBench 2).

## Topics
[[Topic - judge and decision-model audits]] · [[Topic - LLM and agent judges]] · [[Topic - presentation sensitivity]]
