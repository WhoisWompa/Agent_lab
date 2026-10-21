---
title: Do as We Do, Not as You Think: The Conformity of Large Language Models
authors: Zhiyuan Weng et al.
date: 2025-01
arxiv: 2501.13381
url: https://arxiv.org/abs/2501.13381
venue: ICLR 2025
category: failure-analysis-survey
pdf: research/multiagent_llm_systems/pdfs/2501.13381.pdf
folder: ["multiagent_llm_systems"]
topics: ["multi-agent debate and consensus"]
---
# Do as We Do, Not as You Think: The Conformity of Large Language Models

## One line
Measures how often an LLM drops a correct answer to match peer agents, using a new benchmark (BenchForm) built on Asch-style protocols, and tests two prompt fixes.

## Method
The problem: multi-agent systems are built on the assumption that agents add to each other, but humans in groups conform and herd, and nobody had measured whether LLM agents do the same. Earlier work only noticed conformity as a by-product in a few showcases and tested short interactions.

The paper copies the Asch conformity experiment. One subject agent answers multiple-choice reasoning questions (from BIG-Bench Hard) after six scripted peer agents have spoken. The subject always answers last and never learns whether it was right. Five protocols vary the peers:
- Raw: no peers (the baseline).
- Correct Guidance and Wrong Guidance: one round in which all peers give the right or the wrong answer.
- Trust: earlier rounds where peers were right, then a final round where they are wrong.
- Doubt: the inverse, earlier rounds wrong, then a final round right.

Trust and Doubt test whether a history of peer accuracy or inaccuracy changes how much the subject defers.

Two metrics. Conformity rate (CR) is the share of questions the subject got right alone and gets wrong under the protocol. Independence rate (IR) is the share it gets right alone and still gets right under both Trust and Doubt.

The paper then varies the number of prior rounds and the size of the agreeing majority. It asks the subject to explain its switches. It tests two prompt fixes: a system prompt that makes it an independent thinker, and a user turn that asks it to double-check.

## Evaluated on
- Every one of 11 models shows conformity, none is immune. Across five model series the average CR is 23.5% under Wrong Guidance, 31.3% under Trust and 47.2% under Doubt.
- A history of peer behaviour matters, and doubt is formed more easily than trust. The Doubt protocol misleads most: the models stop accepting a peer answer that is now correct. Llama3.1-405B resists Correct Guidance (accuracy shift 1.0 points) but loses 30.2 points under Doubt.
- Larger models are more independent. Qwen2 IR rises from 19.6% (7B) to 57.6% (72B). Llama3.1-405B reaches 56.1%. Behaviour still differs by model: Qwen2-7B accepts the group almost always (CR 98.7% under Correct Guidance) and so is the least misled by Doubt (27.5%).
- Majority size matters more than interaction time. For Llama3-70B, cutting the majority from 6 to 3 drops CR under Doubt from 69.9% to 32.6%, while cutting prior rounds from 5 to 1 only drops it to 62.7%. A single dissenter helps in one model but not in another: Qwen2-72B's CR under Trust rose from 30.0% to 39.9% when one dissenter appeared.
- Models rationalise differently. Llama3-70B admitted influence and changed its answer in 129 of 254 conforming cases, and sometimes reasoned correctly yet still chose the wrong answer. Qwen2-72B almost never admitted it (1 case) and stuck with its answer in 222 of 259 cases where it denied influence (its conforming set).
- Both fixes help, but unevenly. The persona prompt lifts IR from 28.6% to 40.0% (Llama3-70B) and from 57.6% to 68.6% (Qwen2-72B). Reflection cuts Llama3-70B CR under Doubt from 69.9% to 35.2% and lifts its IR from 28.6% to 68.5%, but raises Qwen2-72B CR under Trust from 30.5% to 45.0%, because it discards its first answer and aligns with the majority.

## Limitations admitted by the authors
- The benchmark is necessary but not sufficient evidence of conformity. In real systems agents often answer without seeing peers' answers first, so the Asch setup may not transfer.
- Multiple-choice reasoning questions simplify real use, which limits how far the findings generalise.
- Causes are speculation. Differences between models likely come from training data and alignment, but those are undisclosed, so the Llama3 to Llama3.1 gap is only attributed, not shown.
- The prompt fixes do not generalise. One prompt cannot suit both a credulous model (Qwen2-7B) and a suspicious one (Llama3 series), and over-calibrated skepticism is a risk.
- Conformity is not always bad; it also yields consensus, and the paper does not separate useful from harmful conformity beyond the Correct Guidance case.

## Limitations found by others

## What it leaves untried
- Free-form group discussion, argument and reasoning as a group: peers here only announce a choice, never give reasons, so how persuasive explanations interact with conformity is unmeasured.
- Chain-of-thought as a fix: the authors note that reflection triggers chain of thought and suggest it, but do not test it.
- Training-side remedies (more data, awareness-oriented alignment) are only suggested from a Llama3 vs Llama3.1 comparison, not tested.

## Topics
[[Topic - multi-agent debate and consensus]]
