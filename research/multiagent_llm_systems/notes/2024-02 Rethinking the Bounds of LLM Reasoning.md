---
title: Rethinking the Bounds of LLM Reasoning: Are Multi-Agent Discussions the Key?
authors: Qineng Wang et al.
date: 2024-02
arxiv: 2402.18272
url: https://arxiv.org/abs/2402.18272
venue: arXiv
category: debate-cooperative-reasoning
pdf: research/multiagent_llm_systems/pdfs/2402.18272.pdf
folder: ["multiagent_llm_systems"]
topics: ["multi-agent debate and consensus", "reasoning prompting"]
---
# Rethinking the Bounds of LLM Reasoning: Are Multi-Agent Discussions the Key?

## One line
Re-tests the claim that multi-agent discussion beats a single LLM on reasoning, and finds that a single agent with a strong prompt (a worked demonstration) matches it, while discussion helps mainly when no demonstration is given.

## Method
The problem: papers on multi-agent discussion (Debate, MAD, ReConcile) report gains over a single agent such as chain-of-thought, but the single-agent baseline is often given a weaker prompt than the discussion agents, which usually get task demonstrations. The paper asks whether the gain comes from the discussion or from the prompt.

The remedy is a controlled comparison. Prompts are split into three components: a detailed question description, an answer-format description, and a hand-written worked demonstration. Each component is switched on or off for both the single agent and the discussion frameworks, so the two sides always get the same prompt.

The paper also adds its own framework, Conquer-and-Merge Discussion (CMD), to cover group discussion, which the existing frameworks do not. Agents are split into groups (three per group). Inside a group, agents see each other's answers and explanations. Across groups they see only answers, which saves tokens as agent count grows. After three rounds, all agents vote with equal weight. A tie goes to a "secretary" agent that reads one explanation per side, or to group representatives who discuss at a higher level. A message-passing algorithm synchronises the agents, including those on different LLMs.

## Evaluated on
Tests on commonsense QA (ECQA), math word problems (GSM8K) and deductive reasoning (FOLIO-wiki), mainly with ChatGPT-3.5, then with Gemini Pro and Bard added.
- A strong single agent matches the best discussion: on FOLIO-wiki with a demonstration, the single agent scores 76.09 and CMD 77.39. Averaged over all three tasks with demonstrations: single agent 75.63, CMD 74.46, Debate (3 agents) 73.88, MAD 70.04.
- Without demonstrations discussion does better: average accuracy is 67.41 for the single agent against 71.67 for Debate and 70.75 for CMD. The authors explain this by other agents supplying new perspectives. This is a hypothesis, not tested.
- With multiple LLMs the pattern holds: without demonstrations, ReConcile 76.11 and CMD 76.93 beat the best single model, Gemini Pro (74.38). With demonstrations, CMD 78.66 against Gemini Pro 78.59 is a tie.
- A stronger LLM lifts weaker ones during discussion: Bard and ChatGPT-3.5 improve over rounds when Gemini Pro is in the group, while Gemini Pro dips slightly in round 2 and recovers (shown in a figure, no numbers given).
- Two discussion-specific errors are named: judge mistake (the tie-breaking judge picks the wrong side) and wrong answer propagation (an agent drops a correct answer to join a wrong consensus). The second is called the most common, "even when most initial answers are correct". Support is a case study, not a count.
- MAD is the weakest framework (average 70.04 with demonstrations against 75.63 for a single agent). The authors suspect that forcing agents to disagree injects irrelevant material.

## Limitations admitted by the authors
- Each agent is a plain LLM session, with no tree-of-thought, tools or knowledge bases. Stronger agents might change the verdict on discussion.
- Only reasoning tasks are tested, so the conclusion does not cover planning or interactive settings.
- Only three LLMs (Bard, Gemini Pro, ChatGPT-3.5) were tried, for cost reasons. Generality to other models is open.

## Limitations found by others

## What it leaves untried
- ECQA and GSM8K use only 100 questions each, and the gaps are often a few points (CMD 83 against single agent 83 on GSM8K with a demonstration), so the "on par" finding rests on small samples. A larger or repeated run would show which differences are real.
- Cost is never compared. Discussion uses several agents and several rounds, so even a tie in accuracy favours the single agent. The paper does not put a number on that.
- The explanations for why discussion helps without demonstrations, and why ECQA gets worse with demonstrations ("overthinking"), are guesses with no ablation behind them.

## Topics
[[Topic - multi-agent debate and consensus]] · [[Topic - reasoning prompting]]
