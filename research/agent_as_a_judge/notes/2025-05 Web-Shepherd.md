---
title: Web-Shepherd: Advancing PRMs for Reinforcing Web Agents
authors: Hyungjoo Chae et al.
date: 2025-05
arxiv: 2505.15277
url: https://arxiv.org/abs/2505.15277
venue: NeurIPS 2025
category: agent-evaluation-benchmarks
---
# Web-Shepherd: Advancing PRMs for Reinforcing Web Agents

## One line
First process reward model for web navigation: scores each step against an instruction-derived checklist of subgoals.

## Method
Checklist generation then step-level reward; trained on WebPRM Collection (40K step-level preference pairs with checklists); meta-evaluated on WebRewardBench.

## Evaluated on
~30 points better accuracy than GPT-4o on WebRewardBench; +10.9 points on WebArena-lite as verifier for a GPT-4o-mini policy, at lower cost (project page says 10.3).

## Limitations admitted by the authors


## Limitations found by others


## What it leaves untried

