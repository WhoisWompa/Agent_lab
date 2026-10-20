---
title: SWE-Bench+: Enhanced Coding Benchmark for LLMs
authors: Reem Aleithan et al.
date: 2024-10
arxiv: 2410.06992
url: https://arxiv.org/abs/2410.06992
venue: arXiv
category: agent-evaluation-benchmarks
---
# SWE-Bench+: Enhanced Coding Benchmark for LLMs

## One line
Manual audit of SWE-bench passing patches showing solution leakage and weak tests, plus a post-cutoff rebuilt set.

## Method
Manual inspection of SWE-Agent+GPT-4 passing patches.

## Evaluated on
32.67% of successful patches had the solution in the issue or comments; 31.08% passed only because tests were weak; resolution 12.47% -> 3.97% after filtering.

## Limitations admitted by the authors


## Limitations found by others


## What it leaves untried
- Automated leakage detection at scale.
