---
title: Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference
authors: Wei-Lin Chiang et al.
date: 2024-03
arxiv: 2403.04132
url: https://arxiv.org/abs/2403.04132
venue: ICML 2024
category: alternative-paradigms
topics: ["alternative evaluation paradigms", "preference learning", "social choice"]
---
# Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference

## One line
Crowdsourced pairwise blind battles between anonymous models, ranked with Bradley-Terry, as a live leaderboard of human preference.

## Method
Users submit their own prompts, see two anonymous responses, vote. Bradley-Terry coefficients with confidence intervals; active sampling of pairs; vote-quality checks. Later added style control (regressing out length and markdown).

## Evaluated on
Over 240K votes at the time of the paper (as recalled); reported prompts diverse and crowd votes in good agreement with expert raters.

## Limitations admitted by the authors
- Users are self-selected and prompts skew toward certain uses; votes can reflect style; no ground truth.
- Crowd votes are style-sensitive; private testing and sampling asymmetries distort scores (Singh et al. 2025, 2504.20879).

## Limitations found by others
- Singh et al. 2025 'The Leaderboard Illusion' (arXiv 2504.20879): undisclosed private testing with selective disclosure (Meta tested 27 private variants before Llama-4), unequal data access (Google ~19.2%, OpenAI ~20.4% of data vs 29.7% for 83 open-weight models combined), silent deprecation hurting open models; extra Arena data gives up to 112% relative gain on the Arena distribution.
- Huang et al. 2025 (arXiv 2501.07493): an attacker can de-anonymise the model behind a reply with >95% accuracy and vote for or against a target.
- Min et al. 2025 (arXiv 2501.17858): a few hundred rigged votes can shift rankings.
- arXiv 2508.11847: dropping a handful of preferences can change top rankings.

## What it leaves untried
- Arena-style human preference over agent trajectories (not single replies).

## Topics
[[Topic - alternative evaluation paradigms]] · [[Topic - preference learning]] · [[Topic - social choice]]
