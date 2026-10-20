---
title: AutoBencher: Towards Declarative Benchmark Construction
authors: Xiang Lisa Li et al.
date: 2024-07
arxiv: 2407.08351
url: https://arxiv.org/abs/2407.08351
venue: ICLR 2025
category: self-evolving-tests
---
# AutoBencher: Towards Declarative Benchmark Construction

## One line
An LM proposes and iteratively refines dataset descriptions to optimise declared benchmark properties (difficulty, novelty, salience, harmfulness), then generates Q/A sets that expose new model weaknesses.

## Method
Benchmark construction as optimisation: a proposer LM (GPT-4) suggests topics/descriptions, a generator writes questions with answers grounded in privileged information (retrieved documents, or a Python tool for math), candidate models are evaluated, and scores feed into the next proposal round. Two modes: capability (hard, novel topics) and safety (unsafe prompts models fail to refuse).

## Evaluated on
Datasets elicit 22% more model errors than existing benchmarks. Found Gemini-Pro knowledge gaps on specific historical/economic topics and GPT-4o failing to refuse some crypto-scam requests. Domains: math, multilingual, knowledge, safety.

## Limitations admitted by the authors
- Answer correctness of generated items depends on retrieval/tool grounding; errors in generated answers inflate measured difficulty.
- Optimising for difficulty can reward obscure, low-salience questions; a salience term is added to counter this.
- One strong model (GPT-4) as generator, inheriting its biases.

## Limitations found by others
- Self-bias work (SILENCER, 2505.20738) reports that LLM-generated benchmarks tend to favour the generator model.

## What it leaves untried
- Target a single system and rewrite the benchmark around that system's failures across rounds.
