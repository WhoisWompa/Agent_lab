---
title: One Token to Fool LLM-as-a-Judge
authors: Yulai Zhao et al.
date: 2025-07
arxiv: 2507.08794
url: https://arxiv.org/abs/2507.08794
venue: NeurIPS 2025
category: llm-judge-foundations
---
# One Token to Fool LLM-as-a-Judge

## One line
Reference-based generative reward models (used in RLVR) give positive rewards to 'master key' answers such as ':' or 'Thought process:' with no content.

## Method
Probe generative RMs/judges that compare a response to a reference answer with content-free responses; propose Master-RM trained with truncated outputs as adversarial negatives.

## Evaluated on
Widespread false positives across open models and proprietary GPT-o1, Claude-4; punctuation-only responses up to ~35% FPR on GPT-4o and 'Thought process:' 60-90% on some open models (per paper's tables, figures vary by model/benchmark). Master-RM near 0% FPR while keeping standard performance. Inference-time strategies (CoT, majority voting) do not reliably fix it.

## Limitations admitted by the authors
- Augmentation covers the found master keys; unseen keys may exist.

## Limitations found by others


## What it leaves untried
- Systematic search for new master keys against Master-RM (adaptive attacker).
