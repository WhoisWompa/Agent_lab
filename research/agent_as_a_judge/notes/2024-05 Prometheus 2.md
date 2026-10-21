---
title: Prometheus 2: An Open Source Language Model Specialized in Evaluating Other Language Models
authors: Seungone Kim et al.
date: 2024-05
arxiv: 2405.01535
url: https://arxiv.org/abs/2405.01535
venue: EMNLP 2024
category: trained-judges-reward-models
topics: ["trained judges and reward models", "LLM and agent judges"]
---
# Prometheus 2: An Open Source Language Model Specialized in Evaluating Other Language Models

## One line
Open 7B and 8x7B judges that do both direct (1-5) assessment and pairwise ranking under user-defined criteria, built by merging the weights of two single-format judges.

## Method
- Data: Feedback Collection (pointwise, from Prometheus 1) plus the new Preference Collection (about 200K pairwise judgments with feedback, GPT-4-generated), both synthetic.
- Trains one Mistral-7B / Mixtral-8x7B judge per format, then linearly merges weights; reported that merging beats joint multi-task training.
- Output: verbal feedback then score or preferred response.

## Evaluated on
- Four direct-assessment benchmarks (Vicuna Bench, MT Bench, FLASK, Feedback Bench) and four pairwise ones (HHH Alignment, MT Bench Human Judgment, Auto-J Eval, Preference Bench). Abstract claims the highest correlation and agreement with humans and proprietary judges among open evaluator LMs at the time ([arXiv](https://arxiv.org/abs/2405.01535)).

## Limitations admitted by the authors
- Still trails GPT-4 / Claude-3-Opus on some benchmarks.
- English only; synthetic GPT-4 labels.
- Correlation targets are human/GPT-4 preferences, not objective correctness.

## Limitations found by others
- JudgeBench (arXiv:2410.12784) and RM-Bench (arXiv:2410.16184) show such judges fail when the pair differs in correctness rather than style.
- Huang et al. (arXiv:2403.02839): fine-tuned judges are not a general substitute for GPT-4.
- JudgeBench (2410.12784): 34.9-40.3% accuracy.

## What it leaves untried
- Reasoning before the verdict trained with RL (taken up by J1, JudgeLRM, RM-R1).

## Topics
[[Topic - trained judges and reward models]] · [[Topic - LLM and agent judges]]
