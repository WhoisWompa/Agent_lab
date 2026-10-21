---
title: Debate or Vote: Which Yields Better Decisions in Multi-Agent Large Language Models?
authors: Hyeong Kyu Choi, Xiaojin Zhu, Sharon Li
date: 2025-08
arxiv: 2508.17536
url: https://arxiv.org/abs/2508.17536
venue: NeurIPS 2025 spotlight
category: alternative-paradigms
pdf: research/multiagent_llm_systems/pdfs/2508.17536.pdf
folder: ["multiagent_llm_systems"]
topics: ["alternative evaluation paradigms", "social choice", "multi-agent debate and consensus"]
---
# Debate or Vote: Which Yields Better Decisions in Multi-Agent Large Language Models?

## One line
Decomposes multi-agent debate into majority voting and inter-agent debate and shows voting accounts for most of the reported gains.

## Method
Experiments on seven NLP benchmarks comparing MAD variants to plain majority voting; theoretical model of debate as a stochastic process over agent beliefs.

## Evaluated on
Majority voting alone explains most MAD gains; debate induces a martingale over beliefs, so it does not raise expected correctness; biasing updates toward correction helps.

## Limitations admitted by the authors
- Analysis covers reasoning/QA tasks, not evaluation-specific debate panels directly.

## Limitations found by others


## What it leaves untried
- Same decomposition for judge panels (ChatEval-style) and agent-judges.

## Topics
[[Topic - alternative evaluation paradigms]] · [[Topic - social choice]] · [[Topic - multi-agent debate and consensus]]
