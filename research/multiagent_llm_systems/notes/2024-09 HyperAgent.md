---
title: "HyperAgent: Generalist Software Engineering Agents to Solve Coding Tasks at Scale"
authors: Huy N. Phan et al.
date: 2024-09
arxiv: 2409.16299
url: https://arxiv.org/abs/2409.16299
venue: arXiv
category: orchestrator-worker
pdf: research/multiagent_llm_systems/pdfs/2409.16299.pdf
folder: ["multiagent_llm_systems"]
topics: ["orchestration and delegation", "role-based agent teams"]
---
# HyperAgent: Generalist Software Engineering Agents to Solve Coding Tasks at Scale

## One line
A Planner agent delegates to Navigator, Editor and Executor child agents over a message queue, so one system handles issue resolution, repo-level code generation and fault localization/repair without task-specific rebuilding.

## Method
The problem: most coding agents are built for one task (SWE-bench issues, or generating a project from requirements), so claims of general software engineering are overstated. The paper copies the developer loop (analyse and plan, localize the feature, edit, execute and verify, repeat) and gives each phase to an agent.

- The Planner holds all the hard reasoning. It reads the task, writes a plan, sends requests, and loops on feedback until it is done or hits an iteration limit.
- Child agents do the "heavy but simpler" work. The Navigator searches the repo with IDE-like tools (trigram code search, go-to-definition). The Editor writes patches, applied through an auto-repair editor that fixes syntax and indentation. The Executor keeps a persistent bash shell, reproduces the issue and runs tests.
- Messages carry two fields, Context (background and rationale) and Request (the instruction). Children read from queues asynchronously. Several Navigators can search in parallel, failed tasks are requeued, and the Planner is decoupled from workers.
- A small LLM summarizer (Llama-3.1-8B) condenses each child's execution log before it returns to the Planner. This keeps the Planner's context short, so the cost is paid once, in the strong model.
- Models are chosen per role: a strong model for Planner and Editor, cheaper and faster ones for Navigator and Executor.
- Adapting to a task means filling a task template (issue text, or an error trace). For tasks that need no code change (fault localization), the Editor is simply dropped.
- Tool design is treated as part of the method. For example, go-to-definition needs exact line and column numbers, which LLMs get wrong, so a proximity search lets the agent give approximate positions.

## Evaluated on
- Competitive on GitHub issue resolution, but not clearly ahead on the harder split. On SWE-bench Verified the best configuration resolves 33.0%, against 33.6% for SWE-Agent with Claude 3.5 Sonnet and 33.2% for Agentless with GPT-4o. On Lite it resolves 26.0% against 24.3% for Agentless.
- Cheap configuration is fast: HyperAgent-Lite-1 averages 106 s and $0.45 per issue, against 720 s and $0.68 for AutoCodeRover. The strongest configuration costs more ($1.82) than Agentless ($0.34) for roughly the same Verified score.
- On RepoExec without gold context, it reaches 53.33% pass@5, above every baseline including CodeLlama-34b given full context (49.54%). Its pass@1 of 38.33% is below that model's 42.93%.
- Fault localization on Defects4J: 59.70% Acc@1 against 51.00% for AutoFL, the next best.
- Program repair: 82 correct fixes (20.8%) on Defects4J v1.2 against 74 for RepairAgent, and 110 (25.0%) on v2 against 90.
- Roles matter: with each child agent replaced by the Planner using its tools, cost rises in every case. Removing the Navigator drops Full-1 resolve rate from 27% to 19%, removing the Editor to 12%, and removing the Executor to 22%. This is on a 100-instance subset.

## Limitations admitted by the authors
- Information is lost between agents. The Planner relies on summaries, so it can hallucinate that the task is solved and exit early. The paper names early exit and exit timeout as remaining failure types, but gives no rates for them.
- Results depend heavily on the model mix. Full-3 reaches only 18.33% on Verified and Lite-2 only 16.00%, against 33.00% for Full-1. The generalist claim holds only with a strong Planner.
- Tool interfaces are fragile. Small models such as Claude Haiku scroll files until the context overflows, and go-to-definition fails until proximity search is added (9% to 15% on the ablation subset). Each fix is a hand-tuned patch for one failure.
- Planner and Editor replacing a Navigator or Editor need long context, because those roles interact with the environment continuously. The decoupling is therefore a requirement, not just a saving.

## Limitations found by others

## What it leaves untried
- The scalability claim (parallel Navigators, dynamic load balancing) is never measured. Results report time and cost per issue, but no throughput or speed-up from adding agents.
- Early exit is traced to lossy summaries but the summarizer is not varied or ablated, and no independent check of the Planner's "solved" belief (beyond the Executor) is tried.
- The generalist claim rests on three Python and Java benchmarks. No unseen SE task or language is tried, so "off-the-shelf" generality is untested.

## Topics
[[Topic - orchestration and delegation]] · [[Topic - role-based agent teams]]
