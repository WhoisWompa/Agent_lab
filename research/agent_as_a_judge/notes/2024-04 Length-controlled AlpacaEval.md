---
title: Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators
authors: Yann Dubois et al.
date: 2024-04
arxiv: 2404.04475
url: https://arxiv.org/abs/2404.04475
venue: COLM 2024
category: alternative-paradigms
---
# Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators

## One line
Regression-based length control for AlpacaEval raised Spearman correlation with Chatbot Arena from 0.94 to 0.98 (as recalled).

## Method


## Evaluated on
- (llm-judge-foundations) AlpacaEval 2.0 (805 instructions). Spearman correlation with LMSYS Chatbot Arena rises from 0.94 to 0.98. Claims improved robustness to prompting models to be more or less verbose.

## Limitations admitted by the authors
- Controls only for length; other style cues remain.
- Only controls the biases it explicitly models (length); other confounders remain.
- Correlation target is Chatbot Arena, itself a human-preference proxy with its own style biases.

## Limitations found by others
- Zheng et al. 2024 (2410.07137): a null model with a constant crafted response reaches 86.5% LC win rate on AlpacaEval 2.0, so length control does not stop judge gaming.
- Feuer et al. 2024 (2409.15268): LLM-judge preferences on such benchmarks do not correlate with concrete measures of safety, knowledge or instruction following; style dominates.
- Soumik 2026 (2604.23178): style (markdown) bias is the dominant bias (0.10-0.76) and length-aware verbosity bias varies in sign across judges, so a single length regression is not a general debiasing method.

## What it leaves untried
- Regression control for style/markdown features (Chatbot Arena later added style control) and for self-preference is not attempted here.

