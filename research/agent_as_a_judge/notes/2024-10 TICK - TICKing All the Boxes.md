---
title: TICKing All the Boxes: Generated Checklists Improve LLM Evaluation and Generation
authors: Jonathan Cook et al.
date: 2024-10
arxiv: 2410.03608
url: https://arxiv.org/abs/2410.03608
venue: arXiv
category: agent-evaluation-benchmarks
topics: ["LLM and agent judges"]
---
# TICKing All the Boxes: Generated Checklists Improve LLM Evaluation and Generation

## One line
LLM generates an instruction-specific YES/NO checklist, then a judge scores the response against it; used for evaluation and self-refinement.

## Method


## Evaluated on
Raises exact agreement between LLM judgements and human preferences (reported 46.4% -> 52.2%).

## Limitations admitted by the authors
- Agreement remains about half; checklist quality depends on the generator.

## Limitations found by others


## What it leaves untried
- Not applied to agent trajectories (applied to instruction following); Web-Shepherd (2505.15277) carries the checklist idea to web agents.

## Topics
[[Topic - LLM and agent judges]]
