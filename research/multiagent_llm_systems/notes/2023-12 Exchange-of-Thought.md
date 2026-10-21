---
title: Exchange-of-Thought: Enhancing Large Language Model Capabilities through Cross-Model Communication
authors: Zhangyue Yin et al.
date: 2023-12
arxiv: 2312.01823
url: https://arxiv.org/abs/2312.01823
venue: arXiv (cs.CL)
category: debate-cooperative-reasoning
pdf: research/multiagent_llm_systems/pdfs/2312.01823.pdf
folder: ["multiagent_llm_systems"]
topics: ["multi-agent debate and consensus", "communication topology and channels"]
---
# Exchange-of-Thought: Enhancing Large Language Model Capabilities through Cross-Model Communication

## One line
Three LLMs share their reasoning chains over several rounds, in one of four fixed communication layouts, and stop on a majority answer, with each model's confidence measured by how often its own answer changed.

## Method
The problem: chain-of-thought and self-correction use only a model's own view, and LLMs struggle to revise answers without external feedback. Sampling many chains and voting (self-consistency) helps, but on hard questions most samples are wrong. The authors' pilot (three reasoning datasets) found that among the questions a model gets wrong, most still have the correct answer somewhere in its samples. So the right reasoning exists and needs to be spread, the way a correct minority can win through persuasion.

The solution, Exchange-of-Thought (EoT): the first round is ordinary chain-of-thought from each model. In later rounds each model sees the previous-round rationale and answer of some other models and answers again. Which models it sees is set by four layouts borrowed from network topology:
- Memory (bus): everyone sees everyone's log. Fastest spread, highest volume (n^2 messages).
- Report (star): one central model sees all, the others see only the centre. The centre needs the most processing capacity.
- Relay (ring): each model sees only its predecessor. Lowest load per node (2n messages), slowest spread.
- Debate (tree): leaf models see each other, the parent only receives. Volume 7(n-1)/2, between the others.

Two stopping rules: a model leaves when its answer repeats from the last round (individual), or everyone stops when a majority agrees (global). The final answer is the majority answer.

Confidence evaluation guards against spreading wrong chains. A model's confidence is the share of its rounds that gave its most frequent answer (a model that gives three different answers in three rounds has low confidence). Recipients are told this, so they can discount unsure senders. The reasoning: answers that flip are more often wrong, as in self-consistency work. This is a heuristic with no learned component and no external verifier.

## Evaluated on
Main setup: three GPT-3.5 models, 10 datasets (six math, two commonsense, two symbolic), five runs.
- Beats the strongest baseline on math: the four layouts average 87.20 to 87.50 against 84.16 for progressive-hint prompting (PHP), about 3 points up; roughly equal to self-consistency with 10 samples (86.59).
- Three GPT-3.5 beat a single GPT-4 with chain-of-thought on MultiArith and SingleEQ, but not on the other math sets (GPT-4 averages 90.51).
- On StrategyQA, gains over chain-of-thought are 8.06 to 8.67 points across layouts; on Penguins about 2 points over self-consistency with 3 samples.
- Majority-consensus stopping beats stopping on repeated own answer by 4.01 to 7.56 points on AQuA; the authors attribute the loss to models exiting early through degeneration.
- Confidence evaluation adds 2.92 points on average on GSM8K.
- Cheaper: 20% lower cost and 3% higher accuracy than self-consistency with 5 samples; matches ComplexCoT self-consistency with 10 samples at one-seventh of the cost. Most questions settle within three rounds.
- Model mix: putting GPT-4 as hub (Report) or parent (Debate) adds 1 point or 0.9; a GPT-3.5, GPT-4, Claude-2 mix comes close to or beats two GPT-4 plus one GPT-3.5, taken as evidence for diversity. Gains over self-consistency with 5 samples are smaller for stronger models (3.2 on GPT-3.5, 1.0 on GPT-4, 1.4 on Claude-2).

## Limitations admitted by the authors
- Only commercial models (GPT-3.5, GPT-4, Claude-2) were used; open-source models were left out because of weak communication ability and high compute cost, so the method is untested there.
- Context length caps how many models can join, since every round packs other models' full rationales into the prompt. Only three models were used by default.

## Limitations found by others

## What it leaves untried
- No ablation of agent count beyond three. The cost and gain curve as models are added is not shown, though message volume grows as n^2 for Memory.
- The four layouts give near-identical averages (87.20 to 87.50), and the paper gives no rule for choosing one beyond "different scenarios suit different layouts". No per-question choice of layout.
- Confidence by answer stability is not compared with calibrated or verifier-based confidence, and the case where several models are confidently wrong together is not examined. Majority rule can also lock in a shared error; the paper does not measure how often.

## Topics
[[Topic - multi-agent debate and consensus]] · [[Topic - communication topology and channels]]
