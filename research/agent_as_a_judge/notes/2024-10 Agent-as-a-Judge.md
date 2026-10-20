---
title: Agent-as-a-Judge: Evaluate Agents with Agents
authors: Mingchen Zhuge et al. (incl. Jürgen Schmidhuber)
date: 2024-10
arxiv: 2410.10934
url: https://arxiv.org/abs/2410.10934
venue: ICML 2025
category: agent-evaluation-benchmarks
---
# Agent-as-a-Judge: Evaluate Agents with Agents

## One line
An agentic judge that explores the evaluated agent's workspace (and optionally trajectory) to check each of a task's hierarchical requirements; introduced with DevAI.

## Method
Modules: graph, locate, read, search, retrieve, ask, memory, planning. Best combo: graph+locate+read+retrieve+ask; memory and planning hurt or were unstable. Gray-box (with trajectory) and black-box (workspace only) settings. Judges per requirement, so gives intermediate feedback.

## Evaluated on
DevAI: 55 AI-dev tasks, 365 requirements, agents MetaGPT, GPT-Pilot, OpenHands. Alignment with human consensus, gray-box: 92.07 / 86.61 / 90.16% vs LLM-as-a-Judge 68.86 / 71.85 / 70.76%. Black-box: 88.52 / 83.88 / 90.44% vs 84.15 / 65.30 / 60.38%. Cost $30.58 and 118 min vs ~$1,297.50 human: 97.64% cost and 97.72% time saved.

## Limitations admitted by the authors
- Proof of concept; memory errors cascade; planning unstable.
- Human consensus may not be ground truth.
- Class imbalance makes alignment rates misleading (PR curves added).
- Only 55 tasks; small workspaces so search gave little.

## Limitations found by others


## What it leaves untried
- Using its intermediate feedback as a process reward for agent training (named as future work).
- Self-play between judge and evaluated agents (named as future work).
- Testing on tasks with side effects outside a code workspace.
