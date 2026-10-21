---
title: MetaGPT: Meta Programming for a Multi-Agent Collaborative Framework
authors: Sirui Hong et al.
date: 2023-08
arxiv: 2308.00352
url: https://arxiv.org/abs/2308.00352
venue: ICLR 2024
category: role-based-team
pdf: research/multiagent_llm_systems/pdfs/2308.00352.pdf
folder: ["multiagent_llm_systems"]
topics: ["role-based agent teams", "self-refinement and critique loops", "communication topology and channels"]
---
# MetaGPT: Meta Programming for a Multi-Agent Collaborative Framework

## One line
Encodes a software company's standard operating procedures into a fixed pipeline of five LLM roles that hand each other structured documents instead of chat, plus a run-and-debug loop for the code.

## Method
The problem: chat-based multi-agent systems (CAMEL, ChatDev) pass free-form dialogue between agents. On long tasks the information distorts like a telephone game, and hallucinations cascade from one agent to the next. The authors' fix is to copy human practice.

- **Roles and a fixed workflow.** Five roles (Product Manager, Architect, Project Manager, Engineer, QA Engineer), each with a profile, goal and constraints. They run in a set order. The PM writes a requirements document, the Architect turns it into file lists, data structures and interface definitions, the Project Manager splits tasks, the Engineer writes code, and QA writes tests.
- **Structured outputs as the only hand-off.** Each role must produce a schema-bound document or diagram, not conversation. The claim is that this removes idle chatter and missing content. The paper offers no direct test of that claim. It is supported only indirectly, by the comparison with ChatDev.
- **Shared message pool with subscription.** Agents publish to a global pool and subscribe by role. An agent acts only once its prerequisite messages exist. This avoids one-to-one message webs and limits information overload.
- **Executable feedback.** The Engineer writes and runs unit tests, keeps its debugging history, and retries up to 3 times. The authors added it because their first versions missed errors in review, which they attribute to hallucination. Execution gives a check that does not depend on the model's own judgment.

What it assumes: the task fits a waterfall-style software SOP, and the roles and their order are hand-designed.

## Evaluated on
- **Code generation beats single-model baselines.** Pass@1 is 85.9% on HumanEval and 87.7% on MBPP, against 67.0% for GPT-4 alone as quoted from its technical report. The authors' own reruns of GPT-4 reach about 72% to 81% depending on prompt and parsing, so the gap is smaller than the headline. The appendix shows GPT-4 is sensitive to prompt and post-processing.
- **Executable feedback adds measurable gain.** Pass@1 rises 4.2% on HumanEval and 5.4% on MBPP. On SoftwareDev, human revisions fall from 2.25 to 0.83 per task, and executability moves only from 3.67 to 3.75.
- **Beats ChatDev on whole-project tasks.** On the authors' SoftwareDev benchmark (7 tasks in the main comparison), executability is 3.75 against 2.25 for ChatDev. The code is larger, 251 lines against 78. Tokens per code line are 124 against 249. Total tokens are higher, 31,255 against 19,292. AutoGPT, LangChain and AgentVerse all score 1.0, meaning non-functional.
- **Each role earns its cost.** Adding Product Manager, Architect and Project Manager to a lone Engineer lifts executability from 1.0 to 4.0 and cuts revisions from 10 to 2.5. Expense rises from $0.915 to $1.385.
- **The backend matters.** On five tasks, executability is 3.8 with GPT-4, 2.8 with GPT-3.5 and 1.4 with Deepseek Coder 33B. The open model also takes 1186 s against 553 s.

## Limitations admitted by the authors
- No UI, front-end or multimodal agents, so such tasks are not served. Even with the most generated code among compared frameworks, diverse real-world requirements remain hard.
- A user cannot easily interrupt an agent mid-run or set a checkpoint for one.
- Each project runs independently. The self-improvement mechanism in the appendix, where agents rewrite their constraint prompts from past feedback, is only an initial version. It changes role constraints but not the communication interfaces, and no results are reported for it.

## Limitations found by others

## What it leaves untried
- No ablation isolates structured documents from the fixed role order or the message pool, so which part of the SOP drives the gain is unknown. The role ablation only adds roles.
- Human executability scores come from a 1 to 4 rubric on 7 tasks, with no reported number of raters or agreement. The 70-task averages are given only for the version without feedback.
- No test on non-software tasks, or on tasks where the fixed waterfall order does not fit. The dynamic, self-organising SOP is only sketched in the outlook.

## Topics
[[Topic - role-based agent teams]] · [[Topic - self-refinement and critique loops]] · [[Topic - communication topology and channels]]
