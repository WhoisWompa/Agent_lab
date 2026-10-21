---
title: Optimizing LLM-Based Multi-Agent System with Textual Feedback: A Case Study on Software Development
authors: Ming Shen et al.
date: 2025-05
arxiv: 2505.16086
url: https://arxiv.org/abs/2505.16086
venue: AI Agents: Capabilities and Safety Workshop @ COLM 2025
category: role-based-team
pdf: research/multiagent_llm_systems/pdfs/2505.16086.pdf
folder: ["multiagent_llm_systems"]
topics: ["automated pipeline and topology search", "role-based agent teams"]
---
# Optimizing LLM-Based Multi-Agent System with Textual Feedback: A Case Study on Software Development

## One line
Improves a role-based software-development agent team by having an LLM locate which agents caused a critic's negative feedback and then rewrite only those agents' system prompts.

## Method
Problem: prompt optimizers such as TextGrad and DSPy have not been shown to work on a real role-based team, where each agent has a different job, and global feedback on the final output does not say which agent to change. Workflow-search methods (GPTSwarm, DyLAN) prune edges and assume agents are interchangeable voters, which fails when information flow is fixed and roles differ.

The team is a vertical solver-plus-reviewers structure (one programmer, two reviewers, one review round, roles drawn from a ChatDev-style pool). The topology is held fixed and only the system prompts change. For each of five dimensions (functionality, robustness, test coverage, documentation, PEP 8 style violations) a critic returns a score and a natural-language explanation. GPT-4 is the critic for the first three. Documentation uses GPT-4 text and a comment-line count. Style uses the pycodestyle tool, which is rule-based.

Step one, the locator: an LLM reads the task, the critic feedback, the role descriptions and the full agent conversation, then names the underperforming agents and writes a failure explanation for each. This turns one global complaint into per-agent signals. Step two, the optimizer: an LLM rewrites only the marked part of each flagged agent's prompt to mitigate its explanation, asked to generalize beyond the current task. No ground-truth labels are used, and only 5 training tasks with 5 optimization steps.

The paper also compares settings. Online means feedback comes from the current optimized prompts. Offline means feedback is gathered once from the default prompts. Individual means one random flagged agent is updated per step, and group means all flagged agents are updated. For group, one-pass rewrites all agents in one LLM call and multi-pass uses one call per agent.

## Evaluated on
- Beats a TextGrad-style baseline that skips the locator: the full pipeline always outperforms it. Direct optimization raised style violations from 6.62 to 6.90, and functionality barely moved (6.90 to 6.74).
- Beats one-shot demonstration in 22 of 30 dimension-setting cases. One-shot lowered functionality (6.90 to 6.66).
- Best setting is online group one-pass: functionality 7.26 vs 6.90 unoptimized, coverage 7.81 vs 0.32, documentation 20.33 vs 3.80, violations 3.24 vs 6.62.
- Group beats individual in most cases. The authors guess that a prompt-only system is too simple to overfit.
- Offline is only worse than online on 2 of 5 dimensions, so feedback gathered once from a few annotated examples can suffice. One-pass versus multi-pass shows no consistent gap, so one-pass saves calls.
- Starting from near-empty prompts reaches similar scores (functionality 7.06, robustness 7.77, violations 4.61 vs 3.24).

## Limitations admitted by the authors
- Optimized prompts sometimes leak instance-specific content from training tasks (for example "consider the lifecycle of any temporary files"), so generalization is not assured.
- The model-based critics (the first three dimensions) give noisier training curves that oscillate more than the rule-based ones. Offline training curves for style violations also oscillate more than online ones.
- Test sets are 100 tasks and curves use 30 dev examples, both due to budget, so small gaps (0.1 on functionality) are hard to read.
- Training and dev curves rise together, but training curves are less stable than dev ones, which the authors attribute to sparse training data.
- DSPy could not be compared because it needs numeric metrics rather than text feedback.

## Limitations found by others

## What it leaves untried
- No ablation of the locator against random or all-agent selection beyond the TextGrad-style baseline, and no check of whether its attributions are correct. The paper does not test whether the identified agent was really at fault.
- Everything runs on one model (GPT-4), one team shape and one task family (SRDD), so transfer to other roles, models or non-code tasks is unsupported.
- Human-written feedback for offline optimization is proposed as promising but left as future work.

## Topics
[[Topic - automated pipeline and topology search]] · [[Topic - role-based agent teams]]
