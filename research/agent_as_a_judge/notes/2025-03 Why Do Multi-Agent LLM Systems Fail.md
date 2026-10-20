---
title: Why Do Multi-Agent LLM Systems Fail?
authors: Mert Cemri et al. (incl. Matei Zaharia, Ion Stoica)
date: 2025-03
arxiv: 2503.13657
url: https://arxiv.org/abs/2503.13657
venue: arXiv
category: agent-evaluation-benchmarks
---
# Why Do Multi-Agent LLM Systems Fail?

## One line
MAST: taxonomy of 14 failure modes in 3 categories (system design, inter-agent misalignment, task verification) from multi-agent traces, plus an LLM-as-judge annotator.

## Method
Grounded-theory analysis of 150 traces; MAST-Data of 1,600+ traces from 7 frameworks; LLM-as-a-judge pipeline annotates failure modes.

## Evaluated on
Inter-annotator Cohen kappa 0.88; LLM annotator reported high agreement with humans (figure not retrieved here).

## Limitations admitted by the authors


## Limitations found by others
- Who&When (2505.00212) shows that locating which agent/step caused failure is much harder than naming a failure type.

## What it leaves untried

