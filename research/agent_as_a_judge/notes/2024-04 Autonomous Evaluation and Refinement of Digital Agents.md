---
title: Autonomous Evaluation and Refinement of Digital Agents
authors: Jiayi Pan, Yichi Zhang, Nicholas Tomlin, Yifei Zhou, Sergey Levine, Alane Suhr
date: 2024-04
arxiv: 2404.06474
url: https://arxiv.org/abs/2404.06474
venue: COLM 2024
category: agent-evaluation-benchmarks
topics: ["LLM and agent judges", "agent evaluation benchmarks", "judges as reward signals"]
---
# Autonomous Evaluation and Refinement of Digital Agents

## One line
Domain-general VLM/LLM evaluators for web and device-control trajectories, then used as reward for refinement (Reflexion-style and filtered fine-tuning).

## Method
Variants trade cost, modularity and accuracy (end-to-end VLM vs captioner + LLM reasoner); judge sees the instruction, action history and final screenshot(s).

## Evaluated on
74.4% to 92.9% agreement with oracle metrics across benchmarks; +29% relative on WebArena, ~75% relative on device control.

## Limitations admitted by the authors


## Limitations found by others


## What it leaves untried

## Topics
[[Topic - LLM and agent judges]] · [[Topic - agent evaluation benchmarks]] · [[Topic - judges as reward signals]]
