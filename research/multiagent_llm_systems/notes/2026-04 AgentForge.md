---
title: "AgentForge: Execution-Grounded Multi-Agent LLM Framework for Autonomous Software Engineering"
authors: Rajesh Kumar et al.
date: 2026-04
arxiv: 2604.13120
url: https://arxiv.org/abs/2604.13120
venue: arXiv
category: role-based-team
pdf: research/multiagent_llm_systems/pdfs/2604.13120.pdf
folder: ["multiagent_llm_systems"]
topics: ["role-based agent teams", "self-refinement and critique loops"]
---
# AgentForge: Execution-Grounded Multi-Agent LLM Framework for Autonomous Software Engineering

## One line
A five-agent pipeline (Planner, Coder, Tester, Debugger, Critic) that runs every generated patch in a mandatory Docker sandbox and reaches 40.0% on SWE-bench Lite with GPT-4o.

## Method
The problem: LLMs write plausible code but cannot check it. Existing multi-agent coding systems either simulate execution or make it optional, so errors pass from one agent to the next unchecked. The paper's principle is that no code change moves on until it has survived real execution.

The pipeline is fixed and sequential. Before planning, an orchestrator retrieves the five most similar solved tasks (episodic memory) and the five most relevant repository files from a vector store. The Planner turns the task and this context into a JSON list of steps, each assigned to an agent. The Coder writes a new file or a minimal unified diff. The Tester writes pytest cases for that code. The code and tests run in a network-isolated sandbox (512 MB RAM, 0.5 CPU). On failure, the Debugger gets the code plus the raw stderr/stdout and rewrites it, up to 3 retries. The Critic returns a binary PASS/FAIL on the whole result; a PASS stores the task and patch in episodic memory for later tasks.

The authors frame this as a finite-horizon MDP over repository states with a 0/1 reward from the real test suite. They add three propositions. (1) Execution is a lower-variance correctness signal than model likelihood, so a 7B model with execution feedback should beat a 70B one without. (2) Splitting into n agents multiplies success probabilities, so it helps only if specialization cuts each agent's error enough: the summed per-agent gains must exceed p(n-1), where p is the monolithic failure probability. (3) Diffs cost O(k) tokens against O(L) for full files, so they should be less error-prone. The propositions are justified by argument only. The 7B-vs-70B and diff-vs-full-file predictions are never tested.

## Evaluated on
- Beats single-agent baselines on SWE-bench Lite (300 tasks): 40.0% resolved against 14.0% for single-call GPT-4o, 12.0% for a ReAct GPT-4o agent and 18.1% for published SWE-agent (different base model).
- Every role matters in a 100-task ablation: the full pipeline gets 42.0%. Removing the Critic gives 38.0%, the Debugger 31.0%, the Tester 28.0% (27.0% in the figure) and the Planner 19.0%. The single-agent baseline gets 14.0%. The authors conclude the Tester-Debugger loop is the largest contributor.
- Retries saturate: gains flatten after about 2 retries, though the default is 3.
- Cost is 2.7x the single call: $0.1445 against $0.054 per task, about $43 for all 300 tasks.
- Failures in 30 sampled tasks: 40% faulty localization, 26.7% wrong or partial patches, 20% "cognitive deadlock" (the Debugger keeps editing the same function with near-identical stderr), 13.3% sandbox or tooling.

## Limitations admitted by the authors
- Works at file level and struggles with multi-file coordination. Localization is the top failure at 40%, and in 52% of those cases the right patch needed edits across several files.
- The Tester's tests can be brittle, which weakens the execution signal the design relies on. In 34% of wrong-patch failures the tests overfit the observed failure or depend on names the patch changes.
- The Debugger gets stuck: 20% of failures are repeated near-identical attempts, so more retries do not help.
- The metric is binary resolve/not-resolve and misses partial correctness and regressions. All results use GPT-4o only.
- Execution-grounded agents can produce incorrect or insecure code, and the authors say deployment needs human oversight, static analysis and audit.

## Limitations found by others

## What it leaves untried
- No ablation isolates execution from decomposition. Every row removes an agent, so the claim that execution feedback independently drives the gain is not separated from the effect of having more LLM calls. A sandbox-off run with the same five roles would test it. The cost comparison (2.7x) also leaves compute unmatched.
- The propositions' own predictions (small model with execution beats large model without; diff beats full-file above 200 lines) are stated as testable but never tested.
- No comparison to other multi-agent or test-time-scaling systems under the same model (Trae Agent is only discussed in a note). The ablation covers 100 tasks and the main result is a single run on 300, so the 42.0% vs 40.0% gap is not examined.

## Topics
[[Topic - role-based agent teams]] · [[Topic - self-refinement and critique loops]]
