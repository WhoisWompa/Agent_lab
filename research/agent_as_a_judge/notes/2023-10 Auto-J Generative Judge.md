---
title: Generative Judge for Evaluating Alignment (Auto-J)
authors: Junlong Li et al.
date: 2023-10
arxiv: 2310.05470
url: https://arxiv.org/abs/2310.05470
venue: ICLR 2024
category: trained-judges-reward-models
---
# Generative Judge for Evaluating Alignment (Auto-J)

## One line
A 13B generative judge for 58 real-world scenarios that does pairwise comparison and single-response critique-with-rating.

## Method
- Data: real user queries across 58 scenarios, responses from many LLMs, judgments written by GPT-4 and filtered (about 3.4K pairwise and about 1K single-response training samples, recalled from the paper).
- Output: a critique naming strengths/weaknesses, then a verdict or a 1-10 rating.

## Evaluated on
- Paper reports Auto-J beats open judges and ChatGPT on pairwise agreement with human labels and on critique quality in its own eval set.

## Limitations admitted by the authors
- Scenario taxonomy is fixed; out-of-scenario behaviour untested.
- GPT-4 is the label source.
- Scenario coverage defined by authors.

## Limitations found by others
- Huang et al. (arXiv:2403.02839) evaluate Auto-J as one of the fine-tuned judges that generalise poorly.
- JudgeBench (2410.12784): 36.6%.

## What it leaves untried
- Judging correctness of reasoning, code or math.
