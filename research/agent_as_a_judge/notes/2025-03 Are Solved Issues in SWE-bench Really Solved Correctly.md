---
title: Are "Solved Issues" in SWE-bench Really Solved Correctly? An Empirical Study
authors: You Wang, Michael Pradel, Zhongxin Liu
date: 2025-03
arxiv: 2503.15223
url: https://arxiv.org/abs/2503.15223
venue: arXiv (cs.SE)
category: agent-evaluation-benchmarks
topics: ["agent evaluation benchmarks", "alternative evaluation paradigms", "self-evolving tests"]
---
# Are "Solved Issues" in SWE-bench Really Solved Correctly? An Empirical Study

## One line
Shows SWE-bench's PR-test verifier accepts wrong patches, via full developer test suites and differential testing (PatchDiff).

## Method
Run plausible patches against all developer tests; generate differential tests comparing agent patch vs gold patch behaviour; manual inspection.

## Evaluated on
7.8% of 'correct' patches fail the developer suite; 29.6% of plausible patches diverge from gold; 28.6% of divergent ones certainly wrong; resolution inflated by 6.2 pp absolute.

## Limitations admitted by the authors


## Limitations found by others
- (added by alternative-paradigms researcher) PatchDiff differential testing finds about 7.8% of 'correct' SWE-bench Verified patches fail the full developer test suite and 29.6% behave differently from the gold patch, of which 28.6% are certainly incorrect.


## What it leaves untried
- Feeding differential tests back as a standard part of the verifier.

## Topics
[[Topic - agent evaluation benchmarks]] · [[Topic - alternative evaluation paradigms]] · [[Topic - self-evolving tests]]
