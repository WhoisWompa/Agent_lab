---
title: Meta-Rewarding Language Models: Self-Improving Alignment with LLM-as-a-Meta-Judge
authors: Tianhao Wu et al.
date: 2024-07
arxiv: 2407.19594
url: https://arxiv.org/abs/2407.19594
venue: arXiv (Meta)
category: trained-judges-reward-models
topics: ["trained judges and reward models", "self-evolving tests", "preference learning", "judges as reward signals"]
---
# Meta-Rewarding Language Models: Self-Improving Alignment with LLM-as-a-Meta-Judge

## One line
Adds a meta-judge role that judges the model's own judgments, so the judge skill is trained too, not only the policy.

## Method
- Same model plays actor, judge, meta-judge. Meta-judge compares pairs of judgments to build preference data for the judge role; DPO on both. Includes a length-control step.
- Self-generated labels only.

## Evaluated on
- Llama-3-8B-Instruct: AlpacaEval 2 length-controlled win rate 22.9% to 39.4%; Arena-Hard 20.6% to 29.1% (paper abstract).

## Limitations admitted by the authors
- (self-evolving-tests slice) Length bias: without explicit length control the loop drifts to longer responses.
- (self-evolving-tests slice) Judge scores saturate (many ties on the 5-point scale), limiting further gains.
- (self-evolving-tests slice) No human labels: the meta-judge's own bias can be amplified.
- Judge score distribution concentrates (ties, saturation near top scores).
- Positional bias in meta-judge.
- No human labels, so errors can self-reinforce.

## Limitations found by others


## What it leaves untried
- Grounding the meta-judge in verifiable outcomes.

## Topics
[[Topic - trained judges and reward models]] · [[Topic - self-evolving tests]] · [[Topic - preference learning]] · [[Topic - judges as reward signals]]
