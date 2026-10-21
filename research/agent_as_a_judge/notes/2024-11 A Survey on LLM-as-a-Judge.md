---
title: A Survey on LLM-as-a-Judge
authors: Jiawei Gu et al.
date: 2024-11
arxiv: 2411.15594
url: https://arxiv.org/abs/2411.15594
venue: arXiv (revised through Oct 2025)
category: llm-judge-foundations
topics: ["LLM and agent judges", "judge and decision-model audits"]
---
# A Survey on LLM-as-a-Judge

## One line
Survey organised around 'how to build reliable LLM-as-a-judge systems', with strategies for consistency and debiasing plus a proposed reliability meta-evaluation benchmark.

## Method
Literature survey. Covers in-context design, model choice, post-processing (swap, multiple rounds, multi-judge voting, cascaded selective evaluation), and evaluation of judges.

## Evaluated on
Proposes a reliability-oriented meta-evaluation benchmark (results in its Section 4.4; not extracted here).

## Limitations admitted by the authors
- Challenges listed: reliability (ICL sensitivity, overconfidence, self-enhancement, weak cross-model generalisation); robustness (adversarial attacks, input sensitivity, jailbreaks, brittle scoring); backbone limits; interpretability; meta-evaluation and temporal consistency; ethical/social effects (bias amplification, accountability, homogenisation of creative output).
- Future directions listed: reasoning-centric judgment and self-evolving judges; theoretically grounded evaluation; more reliable judges; MLLM-as-a-judge; better meta-benchmarks; data annotation; scaling; embodied intelligence; LLM optimisation; domain-specific reliable applications.

## Limitations found by others


## What it leaves untried
- A quantitative ranking of which mitigation fixes which bias at what cost (partly done later by Soumik 2026, 2604.23178).

## Topics
[[Topic - LLM and agent judges]] · [[Topic - judge and decision-model audits]]
