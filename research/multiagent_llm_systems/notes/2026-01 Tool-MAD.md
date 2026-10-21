---
title: "Tool-MAD: A Multi-Agent Debate Framework for Fact Verification with Diverse Tool Augmentation and Adaptive Retrieval"
authors: Seyeon Jeong et al.
date: 2026-01
arxiv: 2601.04742
url: https://arxiv.org/abs/2601.04742
venue: arXiv
category: debate-cooperative-reasoning
pdf: research/multiagent_llm_systems/pdfs/2601.04742.pdf
folder: ["multiagent_llm_systems"]
topics: ["multi-agent debate and consensus"]
---
# Tool-MAD: A Multi-Agent Debate Framework for Fact Verification with Diverse Tool Augmentation and Adaptive Retrieval

## One line
Two debating LLM agents, one with a Wikipedia RAG tool and one with a live web search API, re-query after every round and fall back on a judge that sees RAGAS faithfulness and answer-relevance scores when they do not agree.

## Method
The problem: debate frameworks answer from the model's internal knowledge (MAD) or from a document pool retrieved once before the debate (MADKE). Both leave the team stuck with the same blind spots, and the evidence cannot follow the arguments as they develop.

Tool-MAD changes three things.
- **Heterogeneous tools.** The two debaters share a prompt but retrieve differently. The RAG agent searches a Wikipedia vector store (Milvus). The Search agent uses the Tavily web API. Each gets the top three documents per query. The claim is that RAG gives precise, curated context and search gives breadth and fresh facts, so their errors overlap less than two agents with the same tool.
- **Adaptive query formulation.** In round 1 each agent queries from the claim alone. From round 2 on, each agent sees the opponent's last answer and its own previous query, then keeps or rewrites the query and retrieves again. The evidence therefore changes with the argument.
- **Stability score as a control signal.** Each round, every answer is scored for faithfulness (the share of its statements supported by the retrieved documents) and answer relevance (embedding similarity between the question and questions generated from the answer). If both agents give the same label and both scores clear 0.7 (faithfulness) and 0.8 (relevance), the debate stops. Otherwise it continues, up to 3 rounds. The thresholds were picked from the observed score distributions: relevance mostly sits above 0.8, and faithfulness spreads around 0.7 to 0.8, so a stricter faithfulness bar would reject reasonable answers.

If no consensus is reached, a Judge agent reads the claim, the debate history and the scores averaged over rounds, and gives the label (SUPPORTS, REFUTES or NOT ENOUGH INFO). The harness enforces stopping and thresholds. The judge only reads the scores as part of its prompt and is not required to follow them.

## Evaluated on
- **Beats debate baselines on four fact-verification sets (200 sampled claims each, exact match).** With GPT-4o-mini, average 71.0 against 68.0 for MADKE and 52.9 for MAD. With Llama-3.3-70B, 74.0 against 56.5 and 45.9.
- **A small model with the framework beats larger bare models.** GPT-4o-mini plus Tool-MAD (71.0) is above GPT-4o (58.9) and DeepSeek-R1 (66.1) on average.
- **Both tools are needed.** RAG+Search reaches 62.0 to 77.5 per dataset, and RAG+RAG or Search+Search gets 55.5 to 68.5 on the same sets. The paper reads this as less redundant retrieval.
- **Query rewriting helps modestly.** +2.0 on FEVER, +2.5 on FEVEROUS, +1.0 on AVERITEC, 0 on FAVIQ.
- **Score-based feedback helps.** It improves every dataset, most on FAVIQ (+4.5). Correct answers score higher than incorrect ones on both metrics in all four datasets.
- **Rounds.** Accuracy rises to round 3 and dips slightly at round 4, which fixes T at 3.
- **Medical QA with swapped tools.** MedQA 77.0 against 74.0 for MADKE. PubMedQA 29.0 against 22.5 for MAD and 21.5 for MADKE.

## Limitations admitted by the authors
- Repeated trials are too expensive, since every query triggers several LLM calls. Only 95% bootstrap intervals for GPT-4o-mini are given (FEVER 0.67 to 0.79). Those intervals are wide enough to cover the 3-point average gap over MADKE.
- Query rewriting does not help where the first query already covers the search space (FAVIQ, 0 gain), so the benefit depends on the dataset.

## Limitations found by others

## What it leaves untried
- No cost or latency comparison: each round is two retrievals, two answers and two RAGAS scorings, and the paper gives no token or call counts against MADKE or a single agent.
- The scores are computed by an LLM against the retrieved documents, so a confidently wrong retrieved page earns high faithfulness. The Fort Myers case (fresh search result contradicting the dataset label) shows retrieval can disagree with the label, but no experiment tests wrong evidence.
- No test of whether the judge actually uses the scores or the score-gated stopping rule beats plain consensus beyond the ablation gaps (2 to 4.5 points on 200 claims). No more than two debaters and two tool types are tried.

## Topics
[[Topic - multi-agent debate and consensus]]
