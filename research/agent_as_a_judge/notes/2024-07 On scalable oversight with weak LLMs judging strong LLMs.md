---
title: On scalable oversight with weak LLMs judging strong LLMs
authors: Zachary Kenton et al.
date: 2024-07
arxiv: 2407.04622
url: https://arxiv.org/abs/2407.04622
venue: NeurIPS 2024
category: alternative-paradigms
topics: ["alternative evaluation paradigms", "LLM and agent judges"]
---
# On scalable oversight with weak LLMs judging strong LLMs

## One line
Large DeepMind study comparing debate, consultancy and direct QA with weaker LLM judges across extractive QA, math, coding, logic and multimodal tasks.

## Method
Strong LLM agents (Gemini family) as debaters/consultants, weaker LLMs as judges. Protocols: assigned-side debate and consultancy, open debate/consultancy where the agent picks its side, and direct QA by the judge alone. Judge sees only the transcript (and the task where no info asymmetry).

## Evaluated on
Debate outperforms consultancy across all tasks when sides are assigned. Debate beats direct QA only on extractive QA with information asymmetry; mixed elsewhere. In open protocols, judges are less often convinced of the wrong answer in debate than consultancy. Stronger debaters raise judge accuracy, but more modestly than earlier work suggested.

## Limitations admitted by the authors
- Judges and debaters are LLMs; no human judges in most settings.
- No training of debaters; inference-time prompting only.
- Gains over direct QA are task-dependent and absent where the judge already has the information.
- LLMs as proxies for human judges.

## Limitations found by others
- Recchia et al. 2025 (arXiv 2507.19486) and arXiv 2504.03731 question accuracy as the metric and the baselines used.

## What it leaves untried
- Debate training (RL) on the same suite; agentic tasks with tools.

## Topics
[[Topic - alternative evaluation paradigms]] · [[Topic - LLM and agent judges]]
