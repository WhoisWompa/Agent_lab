---
title: The Lessons of Developing Process Reward Models in Mathematical Reasoning
authors: Zhenru Zhang et al.
date: 2025-01
arxiv: 2501.07301
url: https://arxiv.org/abs/2501.07301
venue: ACL 2025 Findings
category: trained-judges-reward-models
---
# The Lessons of Developing Process Reward Models in Mathematical Reasoning

## One line
Qwen team's account of why PRMs disappoint: MC labels are noisy, and Best-of-N evaluation rewards PRMs that have drifted into outcome judges.

## Method
- Compares MC estimation, LLM-as-judge and human labels; proposes consensus filtering (keep steps where MC and an LLM judge agree); releases Qwen2.5-Math-PRM-7B/72B.

## Evaluated on
- Reports better BoN and step-wise error identification (ProcessBench) than open PRMs ([arXiv](https://arxiv.org/abs/2501.07301)).

## Limitations admitted by the authors
- MC estimation yields weaker performance and generalisation than LLM-as-judge and human annotation.
- BoN bias: policies produce correct answers with flawed reasoning; PRMs tolerate them, inflating BoN; many PRMs' minimum scores land on the final-answer step, i.e. they became outcome judges.

## Limitations found by others


## What it leaves untried
- Process supervision outside math.
