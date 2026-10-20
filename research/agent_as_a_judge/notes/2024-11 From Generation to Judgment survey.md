---
title: From Generation to Judgment: Opportunities and Challenges of LLM-as-a-judge
authors: Dawei Li et al.
date: 2024-11
arxiv: 2411.16594
url: https://arxiv.org/abs/2411.16594
venue: EMNLP 2025
category: llm-judge-foundations
---
# From Generation to Judgment: Opportunities and Challenges of LLM-as-a-judge

## One line
Survey defining LLM-as-a-judge by input (point/pair/list) and output (score/rank/select) and organising the field into what to judge, how to judge and how to benchmark.

## Method
Taxonomy: what to judge (helpfulness, safety and security, reliability, relevance, logic, overall quality); how to judge (tuning: data and techniques; prompting: swap, rule augmentation, multi-agent, demonstrations, multi-turn, comparison acceleration); how to benchmark (general, bias quantification, challenging tasks, domain-specific).

## Evaluated on
Survey; no new experiments. Companion list github.com/llm-as-a-judge/Awesome-LLM-as-a-judge.

## Limitations admitted by the authors
- Open problems: bias and vulnerability (length, format, self-preference; prompt injection; adversarial phrases), calling for principles, calibration and root-cause study.
- Scaling judgment at inference time (long CoT, sampling, search) costs compute, can overthink, and widens the attack surface.
- Dynamic and complex judging (LLM-as-examiner, debate, agentic pipelines) is immature.
- Human-LLM co-judgement is little studied; proposes judges choosing which samples go to humans.

## Limitations found by others


## What it leaves untried
- Its own author group's Preference Leakage paper (2502.01534) shows a contamination bias the taxonomy does not yet cover: judges favour students distilled from them.
