---
title: "EvoFlow: Evolving Diverse Agentic Workflows On The Fly"
authors: Guibin Zhang et al.
date: 2025-02
arxiv: 2502.07373
url: https://arxiv.org/abs/2502.07373
venue: arXiv
category: topology-communication
pdf: research/multiagent_llm_systems/pdfs/2502.07373.pdf
folder: ["multiagent_llm_systems"]
topics: ["automated pipeline and topology search"]
---
# EvoFlow: Evolving Diverse Agentic Workflows On The Fly

## One line
A niching evolutionary search that keeps a population of cheap-to-expensive, mixed-LLM agentic workflows on a cost-performance Pareto front, instead of one expensive workflow for every query.

## Method
Problem: automated workflow search (AFlow, ADAS, AgentSquare, GPTSwarm) optimizes one metric and fixes one LLM for every agent. The result is a single complex workflow applied to easy and hard queries alike, and weaker, cheaper models are never used. The authors cite routing studies for the claim that models are complementary, not nested, but they do not test that claim separately.

Idea: treat the search as two-objective, maximizing performance and minimizing cost, and return a Pareto set of workflows. The search space has three levels. An invoking node is an LLM call (model, prompt, temperature). An operator node is a small graph of invoking nodes, such as CoT, debate, self-refine, ensemble, ReAct or self-consistency. A workflow is a graph of operator nodes. Putting the model choice inside the search space is the new part.

Loop, driven query by query:
- Initialize 15 random workflows, each tagged by an LLM with five domain/utility tags.
- For each incoming query, retrieve the top 3 workflows by cosine similarity between query and tag embeddings (MiniLM). This keeps evolution from collapsing onto one domain or one level of complexity.
- An LLM performs crossover on the parents. Three LLM-driven mutations follow: swap the model of a node (guided by a pool of per-model performance history), rewrite a prompt (guided by workflow experience), and add or delete operators and rewire them.
- Niching selection: only the 5 existing workflows closest to the offspring in cost and tag similarity compete with it. Each is run on the query, running averages of cost and performance are updated, and the worst by a Pareto-dominance fitness is removed. Local competition stops cheap simple workflows from being eliminated by expensive strong ones.

At inference the system retrieves a workflow from the population that fits the query's domain and complexity. The reason it should work is that diversity is protected structurally, by niches, rather than hoped for.

## Evaluated on
- Beats hand-made and automated baselines with a single GPT-4o-mini backbone: average 82.55 over six benchmarks (math, code, ALFWorld) against 78.40 for AFlow and 78.14 for AgentSquare. MATH is 57.70 vs 51.28 for AFlow.
- With four open-source models combined, it reaches 72.90% on MATH against 70.20% for o1-preview, at 12.4% of its overall cost (overall cost 972.58 vs 7840.51, in units of 10^-3 dollars). The best single model, Qwen-2.5-72b, gets 63.80%.
- It is cheaper than AFlow on Qwen: 37.5% of the training cost and 19.5% of the inference cost on MATH. The authors attribute this to routing some nodes to cheaper Llama or Hermes models.
- Joint training on MATH and MBPP helps EvoFlow (MBPP 87.62 to 88.35) but hurts GPTSwarm, DyLAN and AFlow (GPTSwarm on MATH falls to 39.18 from a gain of +4.19 when trained alone). The authors credit population optimization, which is a plausible reading but not tested directly.
- The learned population spans a simple I/O plus self-refine workflow (38.7% accuracy, $0.00018 per query) up to debate plus iterative generation and ensembling (72.57%, $0.0037). The paper presents this as evidence of query-aware selection, but no per-query routing analysis is given.
- Ablations: removing tag retrieval or LLM mutation lowers performance and raises variance. Removing operator mutation costs 3.5 to 7.3 points.

## Limitations admitted by the authors
- The paper has no limitations section. The only trade-off it states is population size: going from N=5 to N=25 adds 3.1 points but raises per-query cost from 8e-4 to 2e-3 dollars, so N=15 was chosen as a compromise.
- Parent count K is sensitive in both directions. A small K reduces offspring diversity, and a large K strains the LLM's ability to merge many workflows. Both lower performance.

## Limitations found by others

## What it leaves untried
- Heterogeneity is tested on only MATH and MBPP, and there EvoFlow falls short of o1-preview on MBPP (87.62 vs 89.65). There is no test of the cost claim against stronger closed models, or with a model pool larger than four 70B-class open models.
- Routing at inference rests on tag-embedding similarity to a query. The paper never measures how often the selected workflow is the right complexity level, so the claim of query-adaptive spending is shown only by the population plot.
- On MBPP EvoFlow uses 8.19M overall tokens against AFlow-Qwen's 2.26M while costing less in dollars (565 vs 1598). The paper does not discuss this gap, so the dollar saving depends on the cheap models' prices, not on fewer tokens.

## Topics
[[Topic - automated pipeline and topology search]]
