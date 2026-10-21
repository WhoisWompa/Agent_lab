---
title: Memory Reward Inflation in Self-Improving LLM Agents
authors: Mohammad Asadolahi et al.
date: 2026-06
arxiv: 2608.00017
url: https://arxiv.org/abs/2608.00017
venue: arXiv
category: self-evolving-tests
topics: ["judge and decision-model audits", "LLM and agent judges"]
---
# Memory Reward Inflation in Self-Improving LLM Agents

## One line
Shows that LLM-judged scores stored in an agent's memory inflate on wrong episodes (the 'Echo Gap') and compound, and proposes an answer-free de-inflation method (LUCID).

## Method
Treats stored episode scores as proxy rewards; formalises an Error-Independence Assumption (a correcting signal must track truth with errors independent of the memory's self-grading bias) and proves inflation compounds under score-based and plain similarity retrieval.

## Evaluated on
BIRD text-to-SQL execution accuracy: LUCID 56.9% vs. Memento-style self-graded memory 54.0% vs. memory-less 52.4%.

## Limitations admitted by the authors
- Single benchmark (BIRD).

## Limitations found by others


## What it leaves untried
- Apply the EIA test to a judge that keeps memory of its own past verdicts.

## Topics
[[Topic - judge and decision-model audits]] · [[Topic - LLM and agent judges]]
