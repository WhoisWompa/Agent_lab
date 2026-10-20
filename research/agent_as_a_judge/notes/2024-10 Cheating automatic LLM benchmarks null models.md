---
title: Cheating Automatic LLM Benchmarks: Null Models Achieve High Win Rates
authors: Xiaosen Zheng et al.
date: 2024-10
arxiv: 2410.07137
url: https://arxiv.org/abs/2410.07137
venue: ICLR 2025
category: alternative-paradigms
---
# Cheating Automatic LLM Benchmarks: Null Models Achieve High Win Rates

## One line
A constant, input-independent output crafted against the judge prompt achieves top win rates on AlpacaEval 2.0 (86.5% LC), Arena-Hard-Auto (83.0) and MT-Bench (9.55) (as recalled).

## Method


## Evaluated on
- (llm-judge-foundations) AlpacaEval 2.0: 86.5% LC win rate; Arena-Hard-Auto: 83.0; MT-Bench: 9.55. Tests defences: template paraphrasing and perplexity filters do not stop it reliably; length control and style disentanglement do not either.

## Limitations admitted by the authors
- Attack assumes access to the judge template; defenses not fully explored.
- Proof-of-concept; an adversary could use LLMs to make cheating outputs less detectable.
- Calls for anti-cheating mechanisms rather than providing one.

## Limitations found by others
- Zhao et al. 2025 (2507.08794) show that even trivial 'master key' tokens (':' or 'Thought process:') fool reference-based judges, a weaker-attacker version of the same failure.

## What it leaves untried
- A certified or detection-based defence; judging inside a structured-output protocol where candidate text cannot rewrite the template.

