---
title: CodeT: Code Generation with Generated Tests
authors: Bei Chen et al.
date: 2022-07
arxiv: 2207.10397
url: https://arxiv.org/abs/2207.10397
venue: ICLR 2023
category: alternative-paradigms
pdf: research/multiagent_llm_systems/pdfs/2207.10397.pdf
folder: ["multiagent_llm_systems"]
topics: ["alternative evaluation paradigms", "self-evolving tests"]
---
# CodeT: Code Generation with Generated Tests

## One line
Model generates both code and tests; dual execution agreement ranks candidate solutions without reference tests.

## Method


## Evaluated on


## Limitations admitted by the authors
- (self-evolving-tests slice) Generated tests can be wrong; agreement replaces correctness, so a consistent-but-wrong cluster can win.
- Generated tests can share the code's misconceptions, rewarding consistently wrong solutions.

## Limitations found by others


## What it leaves untried

## Topics
[[Topic - alternative evaluation paradigms]] · [[Topic - self-evolving tests]]
