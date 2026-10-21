---
title: HTN-Orchestrate: A Hierarchical Task Network Framework for Multi-Agent Orchestration
authors: Yanchen Deng et al.
date: 2026-10
arxiv: 2610.22195
url: https://arxiv.org/abs/2610.22195
venue: arXiv
category: orchestrator-worker
pdf: research/multiagent_llm_systems/pdfs/2610.22195.pdf
folder: ["multiagent_llm_systems"]
topics: ["orchestration and delegation"]
---
# HTN-Orchestrate: A Hierarchical Task Network Framework for Multi-Agent Orchestration

## One line
A two-layer orchestrator in which a Planner grows a hierarchical task network only as prerequisite results arrive, and a per-leaf Orchestrator runs the workers, beating a flat agent team on five benchmarks with the same open-weight backbone.

## Method
The problem: orchestration must reconcile global planning (a structured decomposition with dependencies) with local execution that reacts to findings. Predefined workflows fix the decomposition before any result exists. Dynamic-dispatch "agent teams" keep decomposition, dispatch and synthesis inside one orchestrator and do not model subtask hierarchy or precedence between siblings.

The solution splits the roles.
- **Planner (upper layer).** Holds a task network: a tree of parent-child decompositions plus acyclic precedence edges between siblings. A leaf is "ready" only when its prerequisites are complete. A dependent subtask is decomposed only after its prerequisites return, so its internal structure can use their findings. Each proposed decomposition is checked for coverage of the parent and for acyclicity. Depth and branching are capped.
- **Orchestrator (lower layer).** One instance per executable leaf. It sees the original task, the leaf goal, ancestors and prerequisite summaries, and repeatedly chooses to dispatch workers (researcher, verifier), wait, or finish. Reports are collected as they arrive, so a gap or disputed claim triggers a focused follow-up while other workers still run. The leaf returns a summary, a resolved or unresolved outcome, and evidence references.
- **AND synthesis.** A parent synthesizes its result only after all children complete, recursively up to the root.
- **Rebuilding.** If execution fails or no plausible answer exists under the current network, the Planner extracts supported findings from completed and partial reports into an evidence summary and builds a new network from the original task. The evidence is context only; no new subtask is marked done. Rebuilds are bounded. When budgets run out, it reports the evidence it has and the unresolved requirements rather than presenting a stop as success.

## Evaluated on
All methods use DeepSeek-V4.1-Flash; baselines are ReAct, Agent Team and DeepSeek Harness.
- Best of the controlled systems on all five benchmarks. BrowseComp 89.73% vs 87.28% for Agent Team and 73.93% for ReAct; SUPERChem 73.44% vs 68.75% (Agent Team); PRL-Bench 46.00 vs 35.81 (the largest gain, 10.19 points).
- Competitive with frontier proprietary models: SUPERChem is 0.16 points below GPT-5.6 Sol (73.60%). On BrowseComp three frontier models still score higher (91.50, 91.20, 90.40).
- Ablations on a 200-question BrowseComp subset (full system 92.0%): upfront decomposition 90.5%, single-agent leaf 89.5%, no rebuilding 89.5%. Upfront decomposition also raises median completion time from 25.23 to 30.02 minutes and the rebuild rate from 17.5% to 22.5%.
- Single-agent leaves push work onto the Planner: executed leaves rise from 4.67 to 6.15 per question and rebuilds from 17.5% to 32.0%.
- Where both systems are correct (165 questions), HTN finishes faster on 112 (67.9%), median time ratio 0.699 to Agent Team, with average worker concurrency 2.47 vs 1.70 overall.
- Dependent decomposition occurred 79 times across 57 of 200 questions; rebuilding occurred on 35, of which 27 ended correct.

## Limitations admitted by the authors
- Network depth is capped at two with at most four children per node. The authors name deeper decomposition hierarchies as future work, so tasks needing them are untested.
- Only one backbone (DeepSeek-V4.1-Flash) is used. They list other backbones as future work, so the gain over flat teams is not shown to hold elsewhere.

## Limitations found by others

## What it leaves untried
- The ablations run only on BrowseComp (200 questions). The paper does not show which component matters on the science and research benchmarks, where the gains over Agent Team are larger.
- The gain over Agent Team on BrowseComp is 2.45 points, and the ablation gaps are 1.5 to 2.5 points (3 to 5 questions of 200). The paper reports no repeated runs or variance, so whether these gaps are stable is unsupported.
- Total cost is not compared with the baselines. Incorrect answers use 47.50 worker invocations vs 21.04 for correct ones, and 50.0% of incorrect runs rebuilt vs 14.7%. Using that as an early-abandon or escalation signal is not tried.

## Topics
[[Topic - orchestration and delegation]]
