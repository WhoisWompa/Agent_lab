---
title: Improving Multi-Agent Debate with Sparse Communication Topology
authors: Yunxuan Li et al.
date: 2024-06
arxiv: 2406.11776
url: https://arxiv.org/abs/2406.11776
venue: arXiv
category: topology-communication
pdf: research/multiagent_llm_systems/pdfs/2406.11776.pdf
folder: ["multiagent_llm_systems"]
topics: ["multi-agent debate and consensus", "communication topology and channels"]
---
# Improving Multi-Agent Debate with Sparse Communication Topology

## One line
Letting each debating LLM agent see only a few peers' answers instead of all of them matches or beats fully-connected debate while cutting input-token cost by roughly 30 to 50%.

## Method
The problem: standard multi-agent debate (MAD) is fully connected, so every agent reads every other agent's previous-round answer. Input context grows with agents times rounds, which makes debate expensive.

The idea: treat the debate as a graph over agents and make it sparse. Density D is the fraction of possible edges present. Six agents are used, in regular graphs of D = 1, 4/5, 3/5 and 2/5. The sparsest is a ring where each agent sees only its two neighbours. Each agent answers alone in round 1, then revises using only its connected peers' round-1 answers, and a majority vote settles any remaining disagreement. The graphs are static.

Why it should work, from a small case study (three GSM8K questions, 100 Monte Carlo runs each). On easy questions, where most references are correct, more visible references raise the chance of a correct answer. On hard questions, where most references are wrong, more references drag the agent toward wrong answers and sharply lower that chance. Dense debate therefore amplifies a wrong majority. A second observation: once all agents agree they almost never change their minds. Sparse graphs take longer to reach consensus, so they keep more rounds of real debate. The authors tie this to earlier findings that longer reasoning helps.

Extensions. With mixed models, the strong model's position matters. The authors put one GPT-3.5 among five Mistral 7B agents on harmlessness labeling. At high centrality (seen by all five) the team scored 67.0 against 64.0 for self-consistency. At low centrality (seen by one) it scored 65.8. A central strong agent reaches the weak ones in one round instead of two, so less is lost on the way. They also apply debate to alignment labeling (choosing the better of two responses, as in RLAIF), where the argument is that better labels give better reward signals. This claim is not tested by training anything.

## Evaluated on
- Sparse debate is cheaper at the same accuracy on math. GPT-3.5 on MATH: the D = 2/5 ring scores 66.0 against 64.0 for fully connected, with 41.5% lower input cost. On GSM8K it ties at 84.5 with 43.6% lower cost.
- All debate variants beat single-model baselines. On MATH, fully connected debate is 4.0 points above self-consistency (64.0 vs 60.0). Sparse variants range from +3.0 to +7.5.
- It carries over to multimodal reasoning. GPT-4o on MathVista: D = 2/5 scores 59.4 against 58.2 fully connected and 53.0 self-consistency, with 33.1% lower total token cost.
- Alignment labeling shows the same pattern. Harmlessness with GPT-3.5: 68.5 (D = 2/5) against 67.5 fully connected, at 53.3% lower cost. Helpfulness with Mistral 7B: 66.6 against 65.5, at 53.5% lower cost.
- The benefit is not monotone in sparsity. Accuracy at D = 3/5 is sometimes the lowest of the sparse settings (63.0 on MATH, 57.0 on helpfulness), so the claim is "no loss", not "sparser is always better".
- A probabilistic variant (each agent sees any reference with probability D) gives 84.5 / 83.5 / 84.0 on GSM8K at 14 to 47% lower cost.

## Limitations admitted by the authors
- No theory explains why sparsity helps. The "wrong majority" argument rests on three questions, so the mechanism is a hypothesis.
- There is no method for choosing the best topology. Only regular graphs, static graphs and six agents (a four-agent check in the appendix) were tried.
- The scale is small and mostly zero-shot: 100 examples per GPT experiment and 500 for Mistral. Gains of 1 to 2 points sit close to the reported standard deviations (for example 67.5 ± 2.0 and 63.0 ± 1.8 on MATH). Only a subset of datasets and a few models (GPT-3.5, GPT-4o, Mistral 7B) were used, which limits generalisation.
- Debate can spread misinformation, and it costs substantial compute.

## Limitations found by others

## What it leaves untried
- Choosing or learning the graph per question or per agent set. Dynamic graphs were only explored in the appendix as a random variant, with no comparison against fixed sparsity.
- Larger teams with irregular graphs, and measuring whether the savings and accuracy hold as agent count grows.
- Testing whether debate-derived labels improve a trained policy. The RLAIF motivation is never closed with a training run.

## Topics
[[Topic - multi-agent debate and consensus]] · [[Topic - communication topology and channels]]
