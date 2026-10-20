---
title: Establishing Best Practices for Building Rigorous Agentic Benchmarks
authors: Yuxuan Zhu et al. (incl. Sayash Kapoor, Percy Liang, Daniel Kang)
date: 2025-07
arxiv: 2507.02825
url: https://arxiv.org/abs/2507.02825
venue: arXiv
category: agent-evaluation-benchmarks
---
# Establishing Best Practices for Building Rigorous Agentic Benchmarks

## One line
Agentic Benchmark Checklist (ABC) for task validity and outcome validity, applied to popular agent benchmarks to expose setup and reward-design flaws.

## Method
Checklist synthesised from builders' experience, a survey of practice and previously reported issues; applied manually to benchmarks.

## Evaluated on
Flaws can under- or overestimate performance by up to 100% relative. Examples: SWE-bench Verified insufficient tests; tau-bench counts empty responses as success. Applying ABC to CVE-Bench cut overestimation by 33%.

## Limitations admitted by the authors
- Checklist is partly qualitative; the 33% fix figure is from one benchmark.

## Limitations found by others


## What it leaves untried
- An automated checker (agent) that applies ABC to a benchmark.
