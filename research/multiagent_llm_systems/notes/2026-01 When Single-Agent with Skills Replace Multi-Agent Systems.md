---
title: When Single-Agent with Skills Replace Multi-Agent Systems and When They Fail
authors: Xiaoxiao Li
date: 2026-01
arxiv: 2601.04748
url: https://arxiv.org/abs/2601.04748
venue: arXiv
category: topology-communication
pdf: research/multiagent_llm_systems/pdfs/2601.04748.pdf
folder: ["multiagent_llm_systems"]
topics: ["communication topology and channels", "orchestration and delegation"]
---
# When Single-Agent with Skills Replace Multi-Agent Systems and When They Fail

## One line
Compiles a multi-agent pipeline into one LLM call that picks among "skills", then shows that skill selection collapses as the skill library grows and that two-stage routing partly repairs it.

## Method
The problem: multi-agent systems pay for repeated context exchange and several sequential calls. The proposal is to treat each agent as a skill (a descriptor used for selection, an execution policy, an optional tool backend) and "compile" the agent graph into a single agent that selects and runs skills in one shared context. Communication edges become input/output constraints written into the skills. Cost then moves from message passing to a selection overhead that grows with library size.

The paper states when compilation is possible: communication can be put in a sequence, agents see only shared history, and all agents use the same backbone model. Debate, parallel best-of-n sampling and private-information agents are declared not compilable. This is asserted as an "if and only if" with no proof in the text.

The second half asks how selection accuracy scales with library size |S|. Borrowing from cognitive science (Hick's law, working-memory limits, similarity interference, chunking), it fits a capacity law, accuracy ≈ α / (1 + (|S|/κ)^γ), where κ is the size at which accuracy halves, plus a hypothesized confusability penalty. The prediction is that confusable skills hurt more than library size alone, and that grouping skills into coarse-then-fine choices keeps each decision below capacity.

## Evaluated on
- Compiled single agent matches the multi-agent original while cutting cost: accuracy change from -2.0 to +4.0 points (average +0.7), tokens down 53.7% and latency down 49.5% on average. This is GSM8K (3 agents to 1 call), HumanEval (3 to 1) and HotpotQA (4 to 1), all on GPT-4o-mini. HotpotQA latency fell 60.9%; GSM8K only 28.7%, because the arithmetic itself dominates.
- Flat selection degrades with library size: above 90% accuracy at |S| of 20 or fewer, about 20% at 200. The fitted law gives κ of 91.8 (GPT-4o-mini) and 83.5 (GPT-4o), R² above 0.97. GPT-4o has the lower κ, which the author cannot explain.
- Confusability, not size alone, causes errors: with no look-alike skills, accuracy stays 100% at |S| = 20, against about 95% for mixed libraries of that size. One look-alike per skill costs 7-30%, two cost 17-63%. At 10 base skills with two look-alikes each, GPT-4o scores 70% and GPT-4o-mini 37%.
- Two-stage routing helps at large sizes (|S| of 60 or more): GPT-4o-mini rises from about 45% to 83-85%, GPT-4o from about 63% to 72%. Stronger models gain less.
- Longer execution policies in the selection prompt did not lower capacity; the curves overlap within standard error. The author's hypothesis here failed.

## Limitations admitted by the authors
- The skill libraries are synthetic, so real skill distributions may behave differently.
- Only selection accuracy is measured at scale, not end-to-end task success, so the cost of a wrong selection is unknown.
- Only two OpenAI models are tested; the κ values may not transfer, and the GPT-4o versus GPT-4o-mini ordering is unexplained, possibly fitting variance with few points.
- The hierarchies are simple, and the naive and confusability-aware versions score about the same because the test design already aligns domains with look-alike clusters. So the benefit of confusability-aware grouping is not isolated.
- Compilation gains were tested only with 3-4 skills, and the author notes smaller benefit for very long outputs near context limits. When compilation fails to help even though compilable is "not explored in depth".
- The null result on policy complexity may just mean the policy templates were not hard enough.

## Limitations found by others

## What it leaves untried
- The two halves are never joined: no compiled system with 10 or more agents is run to see whether selection error erodes the 54% token saving. The efficiency condition (selection overhead below communication overhead) is stated but not measured against library size.
- Compilation is compared against a pipeline, an iterative loop and a router on one cheap model, all single-call. Heterogeneous backbones or tool-backed (externalized) skills, which the paper excludes, are where multi-agent systems are most often used.
- The closing guideline suggests that multi-agent systems with specialized routers may beat a monolithic agent for large libraries, but this is not tested against the hierarchical single agent.

## Topics
[[Topic - communication topology and channels]] · [[Topic - orchestration and delegation]]
