---
title: ChatDev: Communicative Agents for Software Development
authors: Chen Qian et al.
date: 2023-07
arxiv: 2307.07924
url: https://arxiv.org/abs/2307.07924
venue: arXiv
category: role-based-team
pdf: research/multiagent_llm_systems/pdfs/2307.07924.pdf
folder: ["multiagent_llm_systems"]
topics: ["role-based agent teams", "self-refinement and critique loops"]
---
# ChatDev: Communicative Agents for Software Development

## One line
A virtual software company of role-playing LLM agents (CEO, CTO, programmer, reviewer, tester) builds an app through a fixed design, coding, testing chain of two-agent chats, with a mechanism that makes the assistant ask for details before it answers.

## Method
The problem: earlier deep-learning work improved single phases of the waterfall model, each with its own design, so the pipeline was fragmented. A single LLM asked for a whole program in one step also produces "coding hallucinations": placeholder code, unexecutable code, code that misses the requirements. ChatDev answers with language as the common interface for every phase.

- **Chat chain.** The task is cut into phases (design, coding, testing) and subtasks (code writing, code completion, code review, system testing; five subtasks in all). Each subtask is a dialogue between exactly two agents, an instructor and an assistant, that ends when two successive code modifications are unchanged or after 10 rounds. The authors chose two-agent dialogue over richer topologies to make consensus simple. This fixed workflow tells agents what to talk about.
- **Role prompts.** Inception prompting (from CAMEL) gives each agent its role, subtask goal, tools, termination condition and rules against role flipping, instruction repeating and fake replies. Prompting happens only at the start of a subtask; after that the two agents loop on their own.
- **Memory.** Within a phase an agent sees the full dialogue (short-term). Across phases only the extracted solution is passed on (long-term), not the chat history, so context stays small and focused.
- **Communicative dehallucination.** Vague instructions cause incomplete code. So the assistant briefly reverses roles and asks the instructor for specifics (for example the exact name of a dependency) before giving its answer. It is active in code completion, review and testing.
- The tester runs the code in a Python environment, so the testing phase receives real interpreter errors as feedback. Other judgments (what to improve) come from the reviewer agent's prose.

## Evaluated on
Setup: ChatGPT-3.5, 1,200 self-built software task prompts, compared with GPT-Engineer (single agent) and MetaGPT (fixed roles, human-written procedures).

- Higher quality than both baselines. Quality is completeness x executability x consistency: 0.3953 vs 0.1523 (MetaGPT) and 0.1419 (GPT-Engineer). Executability is 0.88 vs 0.41 and 0.36.
- Preferred in pairwise comparison: against MetaGPT, humans pick ChatDev 88.00% vs 7.92%, but GPT-4 only 57.08% vs 37.50%. The two judges agree on direction but not on margin.
- Role prompts matter most: removing roles from the system prompts drops quality 0.3953 to 0.2212 and executability 0.88 to 0.58. Without a "prefer GUI" role the programmer writes command-line-only programs. Without a "careful reviewer" role feedback stays high-level.
- Removing communicative dehallucination lowers quality to 0.3094 (completeness 0.56 to 0.47). Each added phase raises quality (coding only: 0.2512).
- Cost: about 148 s and 22,949 tokens per program, against 15.6 s and 7,183 tokens for GPT-Engineer, for 144 lines vs 70.
- Dialogue analysis: the most common reviewer complaint is "Method Not Implemented" (34.85%); the most common test error is ModuleNotFound (45.76%). Errors rarely return after a successful compile.

## Limitations admitted by the authors
- Agents write simple logic with low information density. With vague requirements a Snake game is basic and a data system uses static key-value placeholders instead of a database; suited to prototypes, not real applications.
- Evaluation is limited: no test cases exist for whole programs, so the metrics measure only completeness, executability and embedding similarity to the requirement. Functionality, robustness, safety and usability are not measured.
- The multi-agent design costs about 3x the tokens and 10x the time of a single agent, which adds computation and environmental load.

## Limitations found by others

## What it leaves untried
- Ablating the chain structure against a free-form conversation. The ablations remove phases, roles and dehallucination, so the claim that the chat chain itself helps rests only on the gain over baselines that also differ in other ways.
- Using real test suites or functional checks. The consistency score (embedding similarity) can reward code that merely resembles the requirement, and the paper does not test it against correctness.
- A stronger model than ChatGPT-3.5, or fewer-round variants that keep the quality gain at lower cost.

## Topics
[[Topic - role-based agent teams]] · [[Topic - self-refinement and critique loops]]
