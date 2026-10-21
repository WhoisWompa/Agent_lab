---
title: Self-Taught Evaluators
authors: Tianlu Wang et al.
date: 2024-08
arxiv: 2408.02666
url: https://arxiv.org/abs/2408.02666
venue: arXiv (Meta)
category: trained-judges-reward-models
topics: ["trained judges and reward models", "self-evolving tests"]
---
# Self-Taught Evaluators

## One line
Trains an LLM judge with no human preference labels by generating contrasting response pairs where one is known to be worse, then iteratively training on the judge's own correct reasoning traces.

## Method
- From unlabeled instructions, the model writes a response to a modified instruction to produce a plausibly worse answer; judge samples reasoning + verdicts, keeps those agreeing with the known label, fine-tunes; repeat.

## Evaluated on
- Llama3-70B-Instruct: RewardBench 75.4 to 88.3 (88.7 with majority vote), above GPT-4 judges and matching top labelled RMs at the time ([arXiv](https://arxiv.org/abs/2408.02666)).
- (llm-judge-foundations) RewardBench 75.4 -> 88.3 (88.7 majority vote), above GPT-4 as judge at the time.

## Limitations admitted by the authors
- (self-evolving-tests slice) Single base model, RewardBench-centred evaluation.
- (self-evolving-tests slice) Synthetic 'worse' responses may not reflect the subtle errors real judging requires (construction bias).
- Synthetic 'worse' responses may be easier to distinguish than natural errors.
- Evaluated mostly on RewardBench, now saturated.
- Synthetic-only data; quality bounded by how the 'worse' responses are generated.

## Limitations found by others
- RewardBench 2 (arXiv:2506.01937) shows RewardBench-1 scores overstate ability by about 20 points.
- Tan et al. 2024 JudgeBench (2410.12784): RewardBench-style gains do not imply accuracy on hard objective pairs.

## What it leaves untried
- Hard pairs where both answers look plausible; tool-based checks.

## Topics
[[Topic - trained judges and reward models]] · [[Topic - self-evolving tests]]
