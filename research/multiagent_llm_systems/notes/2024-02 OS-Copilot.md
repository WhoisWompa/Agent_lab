---
title: "OS-Copilot: Towards Generalist Computer Agents with Self-Improvement"
authors: Zhiyong Wu et al.
date: 2024-02
arxiv: 2402.07456
url: https://arxiv.org/abs/2402.07456
venue: ICLR 2024
category: framework-production
pdf: research/multiagent_llm_systems/pdfs/2402.07456.pdf
folder: ["multiagent_llm_systems"]
topics: ["orchestration and delegation", "self-refinement and critique loops"]
---
# OS-Copilot: Towards Generalist Computer Agents with Self-Improvement

## One line
A planner, configurator, actor and critic framework gives one LLM agent (FRIDAY) a single interface to the whole operating system, and lets it write and keep its own tools so it can learn applications it has never seen.

## Method
The problem: most computer agents are built for one application (a browser, a terminal, a spreadsheet). An OS holds hundreds of applications, and hand-writing a control mechanism, tools and prompts for each one does not scale.

OS-Copilot answers with two ideas.

**1. A universal interface and a four-part loop.**
- The interface covers a Python interpreter, a bash terminal, API calls and mouse/keyboard control.
- A **planner** splits the request into subtasks. The authors propose a directed acyclic graph planner, so independent subtasks can run in parallel in separate subagents, each with its own configurator and actor.
- A **configurator** is the memory hub. It follows a human-memory analogy:
  - Declarative memory holds the user profile (a concept only, with no benchmark) and semantic knowledge such as OS version and working directory.
  - Procedural memory is the tool repository.
  - Working memory retrieves what is relevant, using dense retrieval, and assembles the prompt for the actor.
- The **actor** has an executor that writes and runs the action. A critic then judges the outcome with an LLM, using system information gathered before and after. It checks whether the subtask is done, gives an error analysis when it is not, and says whether the plan needs restructuring. A refiner applies the correction, with at most three attempts.

**2. Self-improvement through tool accumulation.**
- If retrieval finds no tool above a similarity threshold, a tool generator writes a new Python class.
- After success the critic scores the tool from 0 to 10 for reuse, and tools scoring above 8 enter the repository.
- With a stated learning objective such as "master spreadsheets", FRIDAY proposes its own easy-to-hard task curriculum and keeps the tools it builds while solving it.
- Why it should work: new skills become reusable code rather than longer prompts, and the critic supplies feedback where there is no ground truth. The authors say none of the planner, critic or refiner is new; the contribution is how they are combined.

## Evaluated on
- **GAIA, level 1.** FRIDAY scores 40.86% against 30.3% for GPT-4 with hand-picked plugins, a 35% relative gain. AutoGPT-4 scores 15.05%. The plugin baseline needs a human to choose the plugins; FRIDAY does not.
- **GAIA, levels 2 and 3.** 20.13% against 9.70% at level 2. At level 3 FRIDAY scores 6.12% where every baseline scores 0.
- **Self-directed learning on GAIA.** Learning on the dev set added 9 tools. Level 1 rises from 36.56% to 40.86% and level 2 from 17.61% to 20.13%. Level 3 does not move. Most of the gain over baselines is therefore in the architecture, not the learning.
- **Spreadsheets (SheetCopilot-20).** Without learning FRIDAY solves 0%; the authors say it reached for pandas and matplotlib instead of an Excel library. After self-generating 10 tasks and 8 tools it solves 60%, against 55% for a GPT-4 SheetCopilot whose tools are hand-built. That is 12 of 20 tasks against 11.
- **Time.** Level 1 averages 118 s against 456 s for AutoGPT-4. GPT-4 with plugins takes 39 s, but that figure leaves out the human's plugin selection.

## Limitations admitted by the authors
- **Prompt-dependent.** FRIDAY is built by prompting, so performance can shift sharply when the underlying LLM changes. Fine-tuning would need large trajectory datasets, which are hard to collect.
- **Closed-source and GUI-only software.** Code and language alone cannot control it. Screenshot-to-action and visual grounding are not built.
- **Weak on web and multimodal tasks.** FRIDAY only reads from websites and cannot click. Multimodal tasks need local models such as speech-to-text, which are hard to deploy. The authors give a per-capability breakdown.
- **Unreliable critic.** Subtasks have no ground truth, and judging them means comparing system states with hard-coded rules or an LLM. This is hard to scale and possibly inaccurate. The critic also gates which tools are kept.
- **Safety and interpretability.** Actions on a real OS can be harmful. The authors flag this as unstudied and do not test it.
- **Concept-only parts.** The user profile module has no benchmark.

## Limitations found by others


## What it leaves untried
- No ablation of the critic, the refiner or the DAG planner. The claim that they "elevate" the agent rests on comparison with different systems (AutoGPT-4, plugins), not on removing each part.
- Learning is tested on one 20-task spreadsheet set, where the margin over the baseline is one task, plus one qualitative PowerPoint case. The paper gives no check that learned tools stay correct or do not clutter retrieval as the repository grows.
- Only GPT-4-turbo is used, because of budget. The paper never tests the prompt-dependence it admits.

## Topics
[[Topic - orchestration and delegation]] · [[Topic - self-refinement and critique loops]]
