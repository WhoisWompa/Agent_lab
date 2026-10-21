---
title: ALI-Agent: Assessing LLMs' Alignment with Human Values via Agent-based Evaluation
authors: Jingnan Zheng et al.
date: 2024-05
arxiv: 2405.14125
url: https://arxiv.org/abs/2405.14125
venue: NeurIPS 2024
category: self-evolving-tests
topics: ["self-evolving tests", "LLM and agent judges"]
---
# ALI-Agent: Assessing LLMs' Alignment with Human Values via Agent-based Evaluation

## One line
An evaluator agent with memory emulates realistic misconduct scenarios and iteratively refines them against a target LLM to surface long-tail misalignment.

## Method
Two stages. Emulation: retrieve similar past successful test records from a memory module and generate a realistic scenario from a misconduct seed. Refinement: if the target behaves well, the agent rewrites the scenario (more subtle or contextual) and re-tests, for several iterations. A tool-using evaluator module judges target responses. Memory keeps test scenarios that worked across evaluations.

## Evaluated on
Three value dimensions: stereotypes, morality, legality, seeded from existing datasets. Reports finding more misalignment than static benchmarks across many target LLMs; generated scenarios judged realistic by humans (numbers in paper).

## Limitations admitted by the authors
- Judging of target responses relies on LLM-based evaluators that can err.
- Refined scenarios may drift from the original misconduct (validity of refined tests), checked only by sampling/human study.
- Single-turn, text LLM targets only.

## Limitations found by others


## What it leaves untried
- Use memory to fix the judge, not only to reuse successful attacks.
- Apply to tool-using agents over their native channel.

## Topics
[[Topic - self-evolving tests]] · [[Topic - LLM and agent judges]]
