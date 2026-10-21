---
title: "AgileCoder: Dynamic Collaborative Agents for Software Development based on Agile Methodology"
authors: Minh Huynh Nguyen et al.
date: 2024-06
arxiv: 2406.11912
url: https://arxiv.org/abs/2406.11912
venue: arXiv
category: role-based-team
pdf: research/multiagent_llm_systems/pdfs/2406.11912.pdf
folder: ["multiagent_llm_systems"]
topics: ["role-based agent teams", "self-refinement and critique loops"]
---
# AgileCoder: Dynamic Collaborative Agents for Software Development based on Agile Methodology

## One line
A multi-agent software team that follows Agile sprints instead of a waterfall and uses a dependency graph of code files to decide what to test and what context to show the agents.

## Method
Problem: ChatDev and MetaGPT follow a one-pass waterfall plan, and they load the whole codebase into the prompt. The authors say this does not match real development (they cite about 70% of professional teams using Agile) and breaks once the repository exceeds the context window.

Roles: Product Manager (writes a backlog of tasks with acceptance criteria), Scrum Master (checks that the backlog is feasible, picks tasks for each sprint, writes final docs), Developer, Senior Developer (reviewer), Tester.

Sprint loop: each sprint has Planning, Development, Testing and Review. The PM drafts a sprint backlog and the SM critiques it. The Developer writes code with docstrings. The Senior Developer reviews it statically in three steps (basic checks such as empty methods and missing imports, then backlog compliance, then acceptance criteria and bugs). The Tester writes tests and runs them, and the Developer fixes failures from the tracebacks. At the end the PM compares the accumulated test report against the backlog and acceptance criteria. If tasks remain, the next sprint starts from the inherited code. If not, the PM ends the run. The stop decision is therefore an LLM judgment, not a harness rule.

Dynamic Code Graph Generator (DCGG): a static-analysis module that keeps a graph of code files, with import relations as edges, and updates it as code changes. It does two jobs. First, after a change it retests only the changed files and their ancestors, in reverse topological order, so dependencies are tested first. Second, on a runtime error it traces the traceback to the files involved and fetches only their cross-file context.

Communication: every phase is a two-party instructor/assistant dialogue in free natural language. A shared message pool stores outputs and task status, and each conversation reads only the part it needs.

The measurable parts (execution, tracebacks, graph, test ordering) are done by code. Judgment (backlog, review, done or not) is by prompted LLM roles.

## Evaluated on
- Beats the other agent frameworks on HumanEval and MBPP pass@1 with GPT-3.5 Turbo: 70.53 and 80.92, against MetaGPT 62.80 and 74.73 and ChatDev 61.79 and 74.80. With Claude 3 Haiku it gets 79.27 and 84.31. With GPT-4 it gets 90.85 on HumanEval against MetaGPT's 85.9 (no MBPP number given).
- Produces more working programs on ProjectDev, the authors' 14 multi-file software tasks, scored by hand: executability 57.79 against ChatDev 32.79 and MetaGPT 7.73. It had 0 failing-to-run errors against 6 and 32.
- The dependency graph is the biggest lever on real projects. Without it, executability falls from 57.50 to 23.38, and 11 runs exceed the context length (none with it).
- Test generation matters most on the benchmarks. Removing it costs 8.33 points on HumanEval with GPT-3.5. Removing code review costs 1.63 there but 5.51 on MBPP. Removing sprints costs 1.02 and 2.47.
- The three-step review beats a single-step review by 2.85 points on HumanEval with GPT-3.5 (3.66 with Haiku).

## Limitations admitted by the authors
- It depends on LLM code generation and LLM decisions, so output can still be suboptimal or miss requirements. The graph reduces this but does not remove it.
- Scalability is open: for large repositories, keeping the graph up to date may become too expensive.
- It models only the technical side of Agile (code, tests). Team dynamics, communication and project management are left out.
- It costs much more: 36,818 tokens, 444 s and 0.44 USD per ProjectDev task, against ChatDev's 7,440 tokens, 120 s and 0.12 USD and MetaGPT's 3,029 tokens, 48 s and 0.02 USD. The authors accept this as the price of the Scrum process.
- HumanEval and MBPP are simple function-level problems and poor tests of a project-level team (the authors say so). The ProjectDev result is the real evidence, but it is only 14 tasks, scored by hand, with GPT-3.5 only. The comparison systems' own benchmarks are not public.

## Limitations found by others

## What it leaves untried
- No controlled test of whether Agile is what helps. The ablations remove sprints, tests and review, but the paper never runs the same roles in one waterfall pass with the same test and graph tooling. The cost gap (about 5 times ChatDev's tokens) may come from extra tooling and rounds rather than from Agile.
- The graph holds import edges only. Calls, inheritance and shared data are not modelled, and the paper does not test how often this misses the true cause of an error.
- Termination is decided by the PM agent reading its own report. The paper does not measure early or late stops, such as the 1.64 sprints average hiding a stop that was too early.

## Topics
[[Topic - role-based agent teams]] · [[Topic - self-refinement and critique loops]]
