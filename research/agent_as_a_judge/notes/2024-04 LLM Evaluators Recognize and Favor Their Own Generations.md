---
title: LLM Evaluators Recognize and Favor Their Own Generations
authors: Arjun Panickssery et al.
date: 2024-04
arxiv: 2404.13076
url: https://arxiv.org/abs/2404.13076
venue: NeurIPS 2024
category: llm-judge-foundations
topics: ["judge and decision-model audits", "LLM and agent judges"]
---
# LLM Evaluators Recognize and Favor Their Own Generations

## One line
Shows self-preference is linked to self-recognition: GPT-4 and Llama 2 can tell their own outputs apart, and fine-tuning that raises self-recognition linearly raises self-preference.

## Method
Summarisation tasks; measure self-recognition (pick own vs other summary) and self-preference (score own higher) out of the box and after fine-tuning on recognition; controlled experiments for confounders.

## Evaluated on
Non-trivial out-of-box self-recognition for GPT-4 and Llama 2; linear correlation between recognition and self-preference after fine-tuning; causal link resists straightforward confounders.

## Limitations admitted by the authors
- Summarisation only; quality of own vs other outputs judged equal by humans is the reference.

## Limitations found by others
- Chen et al. 2025 (2504.03846): on verifiable tasks much of stronger models' self-preference is legitimate (their answers are better); harmful self-preference concentrates where the judge was itself wrong.
- Wataoka et al. 2024 (2410.21819): self-preference may be a familiarity (low-perplexity) effect, not self-recognition per se.

## What it leaves untried
- Testing whether blinding (paraphrasing outputs to strip style) removes the bias.

## Topics
[[Topic - judge and decision-model audits]] · [[Topic - LLM and agent judges]]
