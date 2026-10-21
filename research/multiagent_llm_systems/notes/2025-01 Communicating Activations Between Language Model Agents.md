---
title: Communicating Activations Between Language Model Agents
authors: Vignav Ramesh et al.
date: 2025-01
arxiv: 2501.14082
url: https://arxiv.org/abs/2501.14082
venue: ICML 2025
category: topology-communication
pdf: research/multiagent_llm_systems/pdfs/2501.14082.pdf
folder: ["multiagent_llm_systems"]
topics: ["communication topology and channels", "multi-agent debate and consensus"]
---
# Communicating Activations Between Language Model Agents

## One line
Two frozen LLMs communicate by overwriting one model's last-token hidden activation with another's mid-layer activation, replacing natural-language messages at under a quarter of the compute.

## Method
Problem: natural-language communication between agents (e.g. debate) costs inference compute that grows with the number of agents and the length and number of messages. Decoding a message also collapses the sender's state to one token, discarding information. The authors cite probing results that mid-network representations hold richer information than the final layers, which are tuned only for next-token prediction.

Idea (called AC): run model B up to layer j and model A up to layer k. Take A's last-token activation and combine it with B's last-token activation through a function f. Then let B finish its forward pass and decode. A only needs a partial forward pass and B a single one. There are no rounds, because one graft is claimed to carry all of A's beliefs about its prompt.

Choices of f:
- sum
- mean
- replace (B's activation is simply overwritten by A's)
- any of these applied after a learned linear map W, trained once per model pair on generic C4 text with an MSE loss. W adds no task-specific parameters or data.

Layers k = j = 26 were picked from a grid search on the two coordination games and then reused for everything else. The authors' reason replace works best is that its output stays inside B's activation space, while sum roughly doubles the norm. This is a hypothesis, not tested directly. Editing only the last token is claimed to be enough because causal attention already folds the whole prompt into it.

The compute argument is analytic FLOP counts, which say the activation route is "in all practical cases" cheaper. The paper gives no formula-level bound.

## Evaluated on
- Replace nearly closes the gap between no communication and a single agent that sees both prompts, in two signalling games. On Countries with 3B models, accuracy goes from 0% to 78%, against 84% for the single agent and 69% for natural language. On Tip Sheets it is 90% against 74% for natural language.
- Beats two-round natural-language debate on seven reasoning sets, using LLaMA-3.2-3B as A and LLaMA-3.1-8B as B. The gain is up to 27.0% over debate across six of the seven. Examples: Public Relations 74 vs 63, Formal Logic 47 vs 37, GSM8k 64 vs 75 (debate wins here).
- Debate does not reliably beat the better single model, while AC beats both single models on every set except GSM8k, where it is 64 vs 60 for the 8B model. Full MMLU: AC matches or beats debate on 48 of 57 subjects, averaging 62.7 vs 60.7.
- More debate rounds do not rescue the baseline. AC still wins on 5 of 7 sets against 3 to 4 rounds, though 3-round debate reaches 79 on GSM8k against AC's 64.
- Works across model families (Qwen, Gemma, LLaMA) without training W. It beats debate in all six pairs, and beats both individual models in 4 of 6 pairs on Biographies and 5 of 6 on GSM8k. Gains track how similar the two activation spaces are, a positive correlation shown in a figure with no number given.
- Learning W on generic text helps on four of seven sets (+2.6 to 50.0%), but hurts on the others. Training W on GSM8k's own train set lifts GSM8k from 66 to 78, which the authors take as evidence of a distribution mismatch.

## Limitations admitted by the authors
- Without the learned map, the two models' activation spaces must be roughly aligned. The generic-text map is inconsistent across tasks (above).
- Needs access to hidden states, so it does not work with black-box APIs.
- Activations are not human-readable, so the interpretability that natural-language messages give is lost. The authors call this a tradeoff and leave it for future work. Their idea of interpreting activations by the beliefs they induce in the listener is only proposed.
- Debate compute for 4 rounds was too high to finish on most sets, so the scaling comparison is incomplete.

## Limitations found by others

## What it leaves untried
- Tests only two-model, one-way grafts on small LLaMA, Qwen and Gemma models (1B to 9B). Larger models and more than two agents, where natural-language costs actually blow up, are not run.
- Does not test harder coordination such as negotiation or Diplomacy-style games, which the authors list as future work. The signalling games here have one informed sender and one receiver.
- The choice of k = j = 26 comes from a grid search on the two games. Whether it holds for other model pairs or sizes is not checked.

## Topics
[[Topic - communication topology and channels]] · [[Topic - multi-agent debate and consensus]]
