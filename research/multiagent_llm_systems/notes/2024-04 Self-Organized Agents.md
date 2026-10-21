---
title: Self-Organized Agents: A LLM Multi-Agent Framework toward Ultra Large-Scale Code Generation and Optimization
authors: Yoichi Ishibashi et al.
date: 2024-04
arxiv: 2404.02183
url: https://arxiv.org/abs/2404.02183
venue: arXiv
category: orchestrator-worker
pdf: research/multiagent_llm_systems/pdfs/2404.02183.pdf
folder: ["multiagent_llm_systems"]
topics: ["orchestration and delegation", "self-refinement and critique loops"]
---
# Self-Organized Agents: A LLM Multi-Agent Framework toward Ultra Large-Scale Code Generation and Optimization

## One line
A tree of code agents in which each "Mother" agent writes a function skeleton and spawns new agents for the sub-functions, so each agent holds a small, constant amount of code while the total codebase grows with the number of agents.

## Method
The problem: a single code agent must keep the whole codebase in its context while generating and debugging. LLM performance drops as input tokens grow (the paper cites prior work for this and does not measure it), so one agent cannot scale to large projects.

The solution is a hierarchy of two agent types, both an LLM plus a memory of its own code and unit tests.
- **Mother agent.** Given a docstring and unit tests, it writes the function with its sub-functions left unimplemented. It also writes a docstring and unit tests for each sub-function. It hands each sub-function to a freshly spawned agent. The number and kind of sub-functions are chosen by the LLM according to problem difficulty, so the agent count grows with complexity. Children of one Mother run asynchronously and never see the Mother's code internals.
- **Child agent.** A leaf at a preset tree depth. It implements one function from its docstring.

Modification runs after generation. All pieces are combined and tested against the root's unit tests. Feedback then flows down the tree. Each agent sees its Mother's feedback, old code and new code, adds the results of its own unit tests, writes its own self-feedback, and revises. It also passes its state to its own children. The loop repeats up to a fixed iteration count. The claim is that the parent's feedback tells a child something a bare test failure does not (for example "ignore negative numbers"). No ablation tests this claim.

Roles are not occupational (programmer, tester, manager as in MetaGPT or ChatDev). Agents are split by code function. The authors call this "micro", versus the "macro" project-management view of role-based teams, and call the two complementary.

## Evaluated on
- **Beats a single-agent baseline on HumanEval Pass@1.** 71.4 for SoA against 66.5 for Reflexion, the same GPT-3.5-turbo with self-debugging. SoA also beats Self-Edit (62.2), plain ChatGPT (57.3) and CoT (44.6). Gemini Pro scores 67.7.
- **Each agent handles less code, the total is larger.** Averaged over HumanEval, average characters and tokens per function (per agent) are lower than Reflexion's. The code per final solution, summed over all agents, is higher. Only a bar chart is given and no exact figures are in the text.
- **Unequal test budgets.** SoA used 1 unit test and Reflexion used 6, which the authors present as making the gain more surprising. Tree depth was 2 and there were 8 modification iterations.

## Limitations admitted by the authors
- Performance depends on the LLM chosen and on the quality of the generated unit tests. Tests are the only signal driving the loop, and wrong tests give wrong feedback.
- Evaluated only on a limited set of programming tasks. Real, complex software projects are untested.
- Communication and collaboration between agents is not optimized for efficiency or fault tolerance.
- GPT-4 was not used because of experimental cost, so the result is for one weaker model.

## Limitations found by others

## What it leaves untried
- The headline claim (scaling "indefinitely", with constant code per agent) is never tested on a large project. HumanEval has single short functions, so the scale-up is argued, not shown. A multi-file benchmark would test whether interface mismatches between independently written sub-functions break the build.
- No ablation separates the gain from parent-to-child feedback from the gain from decomposition alone. Nor is cost reported (agent count, token spend) against the single agent, so it is unknown whether 5 points is worth the extra calls.
- Mothers see no child code, so a wrong skeleton or wrong sub-function test cannot be repaired from below. Nothing tests how often this happens, or whether children should be able to push back.

## Topics
[[Topic - orchestration and delegation]] · [[Topic - self-refinement and critique loops]]
