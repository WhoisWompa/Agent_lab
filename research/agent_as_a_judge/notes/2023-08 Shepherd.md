---
title: Shepherd: A Critic for Language Model Generation
authors: Tianlu Wang et al.
date: 2023-08
arxiv: 2308.04592
url: https://arxiv.org/abs/2308.04592
venue: arXiv
category: trained-judges-reward-models
---
# Shepherd: A Critic for Language Model Generation

## One line
A 7B LLaMA critic that writes natural-language critiques and suggested refinements of model answers.

## Method
- Data: community critiques mined from Stack Exchange and Reddit (feedback on answers) plus a smaller set of human-annotated critiques on model outputs. Human, not GPT-4-labelled.
- Output: free-form critique; no score.

## Evaluated on
- Evaluated by GPT-4 and human preference comparisons against Alpaca, SteamSHP and ChatGPT critiques; reported competitive or better win rates vs ChatGPT.

## Limitations admitted by the authors
- Evaluation of critique quality itself relies partly on GPT-4.
- Critiques do not always identify the actual error.

## Limitations found by others
- CriticBench (Lin et al., arXiv:2402.14809) and later critic studies find small critics often fail to locate errors in reasoning.

## What it leaves untried
- Measuring whether the critique helps a human or a model fix the answer.
