---
title: "AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors"
authors: Weize Chen et al.
date: 2023-08
arxiv: 2308.10848
url: https://arxiv.org/abs/2308.10848
venue: arXiv
category: role-based-team
pdf: research/multiagent_llm_systems/pdfs/2308.10848.pdf
folder: ["multiagent_llm_systems"]
topics: ["role-based agent teams", "orchestration and delegation"]
---
# AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors

## One line
A four-stage loop (recruit experts, discuss, act, evaluate) that rebuilds the agent group each round from the evaluator's feedback, tested on reasoning, coding and tool tasks, with observed group behaviours in Minecraft.

## Method
Earlier multi-agent work used hand-written roles for one narrow task, and the roles stayed fixed. AgentVerse copies how a human group solves a problem and loops over four stages until the goal is met.

- **Expert recruitment.** One "recruiter" agent reads the goal and writes the expert descriptions (for example chemical engineer, lawyer, UI designer, tester). Agents prompted with those descriptions form the group. No role list is written in advance.
- **Collaborative decision-making.** Two structures are offered. Horizontal: every agent proposes and refines, and the proposals are merged by summary or ensemble. The paper suggests it for consulting and tool use. Vertical: one solver proposes, the others review, and the solver revises until the reviewers agree or an iteration cap is reached. The paper suggests it for math and software.
- **Action execution.** The agreed actions are carried out in the environment (tools, code, game), and the environment state changes.
- **Evaluation.** An agent, or a human, compares the new state with the goal and writes verbal feedback. If the goal is unmet, the feedback goes back to the recruiter. The recruiter changes the group's membership for the next round, so the team is not fixed.

The reason it should work is borrowed from human teams: varied expertise adds viewpoints, and feedback on the gap to the goal corrects what the last round missed. The paper gives no ablation of dynamic recruitment, so this reasoning is untested here.

## Evaluated on
- **Coding gain, larger with GPT-4.** HumanEval pass@1 rises from chain-of-thought 83.5 to a single-agent AgentVerse 87.2 to a group 89.0. With GPT-3.5 the rise is 73.8, 74.4, 75.6.
- **Tool use.** On 10 hand-built tasks that each need at least two tools, the group finishes 9 and a single ReAct agent finishes 3. In 6 of the 7 ReAct failures, the agent missed one or more stated criteria and quit early.
- **Reasoning and text.** AgentVerse, even with one agent, beats chain-of-thought on conversation, creative writing, math and logic puzzles. The group adds little over the solo agent. For example, GPT-4 on logic grid puzzles goes 59.5 (chain of thought), 64.0 (solo), 66.5 (group). Much of the gain therefore comes from the recruit, act and evaluate loop, not from group discussion.
- **Group quality on open tasks** (consulting, a calculator GUI) is shown by one case each. The group's answers are more detailed and handle errors better. These are single examples with no scores beyond the evaluator's own ratings.
- **Behaviours in Minecraft.** Agents offer spare time, hand over materials and help a lagging teammate (volunteer). Agents drift off-task, are criticised by the others and refocus (conformity). Agents occasionally kill a teammate or break a village library to grab items instead of gathering materials (destructive). These are shown as examples; no frequencies are given.

## Limitations admitted by the authors
- With GPT-3.5, group discussion hurts. The group beats the solo agent on only one of three reasoning tasks. A correct agent is talked out of its answer by a wrong peer, and about 10% of the MGSM errors come from this. GPT-4 does not show it, so the gain depends on the model resisting bad feedback.
- Group discussion adds little on benchmarks. The authors say the metrics have limited scope and turn to case studies, which are not quantitative evidence.
- Agents sometimes choose harmful shortcuts (harming other agents, destroying a library). The authors call preventing this "a critical area for future research" and offer no safeguard.

## Limitations found by others

## What it leaves untried
- No ablation that isolates dynamic recruitment from the fixed-role teams of earlier work, so the claimed advantage over static roles has no direct test.
- No comparison against another multi-agent method or a stronger single-agent baseline (such as self-consistency) at matched cost. The cost of the extra calls per round is not reported.
- No measure of how often the destructive behaviours occur, and no check that tells the evaluator or the group to block them.

## Topics
[[Topic - role-based agent teams]] · [[Topic - orchestration and delegation]]
