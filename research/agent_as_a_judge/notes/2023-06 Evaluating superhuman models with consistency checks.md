---
title: Evaluating Superhuman Models with Consistency Checks
authors: Lukas Fluri, Daniel Paleka, Florian Tramer
date: 2023-06
arxiv: 2306.09983
url: https://arxiv.org/abs/2306.09983
venue: SaTML 2024 (as recalled)
category: alternative-paradigms
---
# Evaluating Superhuman Models with Consistency Checks

## One line
Evaluates models that may exceed humans by checking logical consistency rules (e.g. equivalent chess positions should get the same score, forecasts should be monotone).

## Method
Defines metamorphic/logical relations per domain; finds violations in chess engines, GPT-4 forecasting and legal judgment prediction.

## Evaluated on
Found inconsistencies in all three domains (e.g. opposing evaluations of equivalent chess positions; non-monotone forecasts of sports records).

## Limitations admitted by the authors
- Consistency is necessary, not sufficient: a consistently wrong model passes.

## Limitations found by others


## What it leaves untried
- Consistency relations over agent trajectories (e.g. equivalent environment states should yield equivalent actions).
