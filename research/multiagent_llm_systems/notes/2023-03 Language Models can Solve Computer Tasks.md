---
title: Language Models can Solve Computer Tasks
authors: Geunwoo Kim et al.
date: 2023-03
arxiv: 2303.17491
url: https://arxiv.org/abs/2303.17491
venue: NeurIPS 2023
category: generator-critic-loop
pdf: research/multiagent_llm_systems/pdfs/2303.17491.pdf
folder: ["multiagent_llm_systems"]
topics: ["self-refinement and critique loops"]
---
# Language Models can Solve Computer Tasks

## One line
A single LLM is prompted to criticise and then rewrite its own output (RCI), applied in three stages to turn a task into an executable keyboard and mouse action, and this matches or beats trained agents on MiniWoB++ with a few demonstrations per task.

## Method
The problem: earlier computer-control agents were trained from scratch with supervised learning (SL) or reinforcement learning (RL). That needs tens of thousands of expert demonstrations and a hand-made reward for every task, so it does not carry to new tasks. Raw LLMs prompted to act did worse than those trained agents, because a generated action must satisfy three things at once: it must serve the task, be possible in the current page state, and be in a format the executor accepts.

The idea is Recursive Criticism and Improvement (RCI). There is one model and no second agent. It answers, is prompted to "find problems with your answer", then is prompted to improve the answer given those problems. The loop can stop on environment feedback, an iteration cap or a heuristic. Two forms exist: explicit RCI writes the critique out, and implicit RCI updates the output directly without sampling a critique.

For computer tasks the action is built in three steps, each with its own RCI:
- Task grounding: the model writes a step-by-step plan, and one explicit RCI pass improves it. The plan also acts as memory of which stage the agent is at.
- State grounding: implicit RCI ties abstract references ("email from Bob") to concrete HTML elements in the current page. One pass is enough, since repeating it did not change the success rate.
- Agent grounding: implicit RCI repeats until the action fits the executor's allowed formats, capped at 3 loops, the value the authors found best.

No trained components are added. Everything rests on the LLM critiquing itself, and the harness only enforces the loop cap and executability.

## Evaluated on
- Beats trained agents with far less data on 55 MiniWoB++ tasks. It is 41% above WebN-T5-3B, which was fine-tuned on 12K demonstrations. It is 6% above CC-Net when CC-Net is stripped of dictionary typing (the fair comparison, since this agent generates its text), and 27 to 37 points above the best RL and SL results. It is less than 1 point above the best SL+RL result. The full CC-Net, with dictionary typing, still scores higher.
- Needs 2 to 3 demonstrations per task: 120x fewer samples than WebN-T5-3B and 11,000x fewer than CC-Net (about 23,000 per task).
- Each grounding stage matters about equally. Removing any one lowers success. Without agent grounding, success on simple tasks falls by 60%.
- Language model quality matters. GPT-3 without instruction tuning struggles to finish tasks.
- RCI also helps plain reasoning. Eight arithmetic and commonsense benchmarks all improve over zero-shot. For example GSM8K goes 77.95 to 85.43, and StrategyQA 48.81 to 61.81. It beats zero-shot and few-shot chain of thought (CoT) on four of five arithmetic sets, and combining RCI with CoT scored highest on four of five.

## Limitations admitted by the authors
- Reasoning gains used ground-truth feedback to stop the loop. Without it, RCI produces false-negative critiques that lower accuracy, and in half the benchmarks it only reached zero-shot level. The gains therefore depend on an external signal.
- It costs more than sampling once, since every step takes several calls (no cost figure given).
- It is tested mainly on gpt-3.5-turbo and gpt-4, so transfer to other models is unknown.
- Long HTML pages exceed context length, and pruning them is non-trivial.
- The action space is clicks and typing only, and the agent plans short-term. Failures cluster in long-horizon tasks (guess-number, search-engine), multi-step reasoning (tic-tac-toe) and tasks needing the rendered page (count-shape).
- HTML alone misses details of modern UI components, so other input modalities are needed.
- It still trails task-specific SL+RL training on some tasks.

## Limitations found by others

## What it leaves untried
- Critique without a ground-truth stopping signal. The paper shows the loop hurts without one but offers no self-contained stopping rule.
- Several LLMs exchanging critiques as team members. The discussion mentions this, along with game theory and RL-discovered loop structures, but runs nothing.
- Fine-tuning the LLM on computer tasks, or multimodal input. Both are expected to help, but neither is tried.

## Topics
[[Topic - self-refinement and critique loops]]
