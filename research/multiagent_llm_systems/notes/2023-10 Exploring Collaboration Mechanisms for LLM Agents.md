---
title: Exploring Collaboration Mechanisms for LLM Agents: A Social Psychology View
authors: Jintian Zhang et al.
date: 2023-10
arxiv: 2310.02124
url: https://arxiv.org/abs/2310.02124
venue: arXiv (v3, May 2024)
category: debate-cooperative-reasoning
pdf: research/multiagent_llm_systems/pdfs/2310.02124.pdf
folder: ["multiagent_llm_systems"]
topics: ["multi-agent debate and consensus", "self-refinement and critique loops"]
---
# Exploring Collaboration Mechanisms for LLM Agents: A Social Psychology View

## One line
Builds small "machine societies" of three ChatGPT agents with easy-going or overconfident personas and tests which order of debate and reflection rounds works best, finding that debate-first strategies win and that agents show human-like conformity.

## Method
The problem: multi-agent LLM work (debate, reflection) is mostly tuned by trial, with no account of which collaboration structure helps and why. The paper treats collaboration as a design space with three variables.
- Trait: each agent is prompted to be easy-going (open to persuasion) or overconfident (sticks to its answer). Four 3-agent societies mix the two, from all overconfident to all easy-going.
- Thinking pattern per round: debate (see the other agents' answers and revise) or reflection (review one's own earlier answers and revise).
- Collaborative strategy: the sequence of patterns over rounds. With 3 rounds and all agents using the same pattern each round, this gives 8 strategies (p0p0p0 = continuous debate, p1p1p1 = continuous reflection, and so on).

The authors then read the results through social psychology (conformity, groupthink, consensus reaching). The claim is that small, well-ordered groups beat simply adding agents or rounds. The framing is an interpretation: the paper shows behavioural parallels, not a causal test of the theories.

## Evaluated on
Three tasks (MMLU high-school multiple choice, MATH levels 3-5, chess move validity), 50 questions each, with gpt-3.5-turbo; other LLMs are in the appendix.
- Personas barely matter: accuracy across the four societies under the same strategy is not clearly different (significance tests in the appendix). The authors attribute this to alignment and sycophancy damping overconfidence. Persona does change consensus: all-easy-going societies reach consensus more easily.
- Order of patterns matters a lot: on MMLU in society S4, p0p0p1 scores 65.2 against 34.4 for p1p0p0. Debate-first and debate-dominant strategies generally beat reflection-first ones; on LLaMA2-13B and Qwen-72B debate-initial is better, on LLaMA2-70B and Mixtral debate-dominant is better.
- Some strategies are cheaper at similar accuracy: p0p0p1 uses 3510 tokens against 4364 for continuous debate on MMLU and matches it on MATH (e.g. 52.8 vs 50.4 in S2). This is the basis of the abstract's claim of beating prior top approaches with fewer tokens. The main text does not show a table against other published methods.
- Bigger is not better: three agents is best (odd counts avoid ties; accuracy among odd counts barely varies), and 3 rounds is enough, since 3 to 10 rounds fluctuate without a clear gain.
- Mixing patterns within a round (some agents debate, others reflect) lowers accuracy, so all agents should use the same pattern in a round.
- Conformity is widespread and grows with rounds. It helps on ChatGPT and Qwen-72B and hurts on LLaMA2-13B/70B and Mixtral, and its benefit shrinks as rounds increase. Reflection leaves more distinct answers (harder consensus); debate converges.
- Difficulty and task interact: chess shows only a slight best-to-worst gap, while on the hardest MATH level 5, debate plus continuous reflection (p0p1p1, p1p1p0) does best.

## Limitations admitted by the authors
- Every society uses one underlying LLM; mixing models was not tried for cost reasons, though differing pretraining data could change the social dynamics.
- Strategies were found by exhaustive search, not chosen by the agents; continuous debate is near the ceiling but costs more tokens, and cheaper strategies exist.
- Setup is simple: few trait types and small societies, so claims about "society" are limited to 2 to 10 agents.
- Scoring is manual checking and rule matching, so open-ended or creative tasks (e.g. literary writing) are not covered.

## Limitations found by others

## What it leaves untried
- Letting agents choose their own thinking pattern each round, which would replace the exhaustive search over strategies and the cost it carries.
- Heterogeneous societies of different LLMs, where conformity direction (helpful on some models, harmful on others) could be tested against model diversity.
- Larger test sets: 50 questions per task with large standard deviations (the paper itself introduces a win-tie metric to cope) leaves many strategy gaps near noise.

## Topics
[[Topic - multi-agent debate and consensus]] · [[Topic - self-refinement and critique loops]]
