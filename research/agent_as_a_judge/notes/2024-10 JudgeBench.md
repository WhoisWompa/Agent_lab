---
title: JudgeBench: A Benchmark for Evaluating LLM-based Judges
authors: Sijun Tan et al.
date: 2024-10
arxiv: 2410.12784
url: https://arxiv.org/abs/2410.12784
venue: ICLR 2025
category: trained-judges-reward-models
topics: ["judge and decision-model audits"]
---
# JudgeBench: A Benchmark for Evaluating LLM-based Judges

## One line
Benchmark of hard response pairs whose correctness is objectively verifiable (knowledge, reasoning, math, code), to test judges on correctness instead of style.

## Method
- Pairs built from the same strong model's responses; labels from ground truth; position-consistent scoring.

## Evaluated on
- GPT-4o only slightly better than random ([arXiv](https://arxiv.org/abs/2410.12784)). Later: J1-Qwen-32B 71.4, DeepSeek-R1 68.9, o1-mini 64.2 (J1 paper); 'Outcome Accuracy is Not Enough' GenRM 82.0 (arXiv:2602.04649); one Sept 2026 paper reports a GPT-6 judge at 93.1% on a JudgeBench subset (arXiv:2609.26550).
- (llm-judge-foundations) Overall accuracy (random = 50): GPT-4o vanilla 50.9, GPT-4o with Arena-Hard judge prompt 56.6, Gemini-1.5-pro (Vertex) 44.6, Claude-3.5-Sonnet 64.3, o1-preview 75.4, o1-mini 65.7, o3-mini-high 80.9, Llama-3.1-405B 56.9. Fine-tuned judges: PandaLM 13.1, Prometheus2 34.9-40.3, JudgeLM 25.1-35.7, Auto-J 36.6, Skywork-Critic-70B 57.4. ChatEval multi-agent debate 34.0. Reward models: Skywork-Reward-Gemma-2-27B 64.3, InternLM2-20B 63.4.

## Limitations admitted by the authors
- Labels require objective ground truth, so subjective quality is out of scope.
- 350 pairs (GPT-4o split) is small for fine-grained analysis.
- Pairs generated mainly with GPT-4o, biasing against GPT-4o as judge (Claude-generated split shows similar pattern).
- Some fine-tuned judges limited to 2048 tokens and truncated; many emitted ties/invalid outputs.
- Results depend on prompt and greedy decoding.

## Limitations found by others
- (added by alternative-paradigms researcher) Benchmark of hard response pairs (knowledge, reasoning, math, coding) labelled by objective correctness to test judges; strong judges including GPT-4o barely beat random.
- Lai et al. 2026 BiasScope (2602.09383): automatically discovered biases yield JudgeBench-Pro, on which strong LLM evaluators exceed 50% error.
- Norman et al. 2026 (2606.19544): judge rankings shift by up to 14 positions between JudgeBench, MT-Bench and RewardBench, so one benchmark does not rank judges.

## What it leaves untried
- Letting the judge execute code or check math with tools; the benchmark measures text-only judging.

## Topics
[[Topic - judge and decision-model audits]]
