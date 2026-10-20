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
- Module details (added by agent-as-judge-core researcher): graph (file/dependency graph, chunks code), locate (finds file a requirement refers to), read (multimodal: code, images, video, docs), search (code snippets, hidden deps), retrieve (segments of long texts such as the trajectory), ask (decides satisfied/not), memory (past judgments), planning. Search was dropped as useless on workspaces of hundreds of lines. No numbers given for dropping search/memory/planning.
- Incremental ablation on OpenHands: ask only 65.03% -> +graph 75.95% -> +read 82.24% -> +locate 90.44% -> +retrieve 90.16% (retrieve no gain on OpenHands, said to help MetaGPT/GPT-Pilot).
- Reads files but does not execute the generated code as a test harness; the "ask" module queries the LLM, it does not question the judged agent. Backbone GPT-4o.

## Evaluated on
DevAI: 55 AI-dev tasks, 365 requirements, agents MetaGPT, GPT-Pilot, OpenHands. Alignment with human consensus, gray-box: 92.07 / 86.61 / 90.16% vs LLM-as-a-Judge 68.86 / 71.85 / 70.76%. Black-box: 88.52 / 83.88 / 90.44% vs 84.15 / 65.30 / 60.38%. Cost $30.58 and 118 min vs ~$1,297.50 human: 97.64% cost and 97.72% time saved.
- Additional numbers (added by agent-as-judge-core researcher): humans ~86.5 h (58 h + 28.5 h consensus); LLM-as-a-Judge cost $29.63 and 10.99 min - i.e. Agent-as-a-Judge costs about the same as an LLM judge in dollars but ~11x the wall-clock time. Individual humans averaged 84.88-89.34% alignment; 3-human majority vote 93.98-95.08%. The intro (97.64% cost / 97.72% time) and Sec 4.4 numbers imply the two percentages are swapped. Human-judged requirement satisfaction: MetaGPT 22.13%, GPT-Pilot 44.80%, OpenHands 42.89%; task solve rate 0 / 1.81 / 1.81% (one task solved). Agent judge reported GPT-Pilot solve rate 5.45% vs humans 1.81%.

## Limitations admitted by the authors
- (self-evolving-tests slice) Judge and requirement set are fixed; no test refinement across rounds; one domain (AI development tasks).
- Proof of concept; memory errors cascade; planning unstable.
- Human consensus may not be ground truth.
- Class imbalance makes alignment rates misleading (PR curves added).
- Only 55 tasks; small workspaces so search gave little.
- Human judges disagreed 10-30% of the time; gray-box trajectories are "nearly inaccessible in practical situations"; a larger expert panel would be more reliable but costly (added by agent-as-judge-core researcher).

## Limitations found by others
- AJ-Bench (2604.18240) classifies the DevAI judge as not environment-aware (it inspects the workspace but does not interact with an environment) (added by agent-as-judge-core researcher).
- Survey on LLM-as-a-Judge for SE (2510.24367) notes DevAI checks execution/format of requirements, not overall engineering quality.
- Gaming the Judge (2601.14691) shows trajectory-reading judges are fooled by manipulated agent reasoning (up to +90% false positives) - a direct risk for the gray-box setting.
- AgentHorizon (2610.11050) finds tool access/harnesses do not consistently help judges (Qwen 3.6 27B better direct than agentic), contradicting a blanket "agentic > LLM judge" reading.
- Only 3 human judges, 3 developer agents, one backbone; no run-to-run variance reported (own reading).

## What it leaves untried
- Using its intermediate feedback as a process reward for agent training (named as future work).
- Self-play between judge and evaluated agents (named as future work).
- Testing on tasks with side effects outside a code workspace.
- Executing the generated code/tests in a sandbox as part of judging; interactive questioning of the judged agent; re-testing memory/planning/search on large repositories; run-to-run variance (added by agent-as-judge-core researcher).
