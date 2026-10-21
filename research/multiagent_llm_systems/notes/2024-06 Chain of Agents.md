---
title: Chain of Agents: Large Language Models Collaborating on Long-Context Tasks
authors: Yusen Zhang et al.
date: 2024-06
arxiv: 2406.02818
url: https://arxiv.org/abs/2406.02818
venue: arXiv (preprint, under review)
category: topology-communication
pdf: research/multiagent_llm_systems/pdfs/2406.02818.pdf
folder: ["multiagent_llm_systems"]
topics: ["orchestration and delegation"]
---
# Chain of Agents: Large Language Models Collaborating on Long-Context Tasks

## One line
Splits a long input into window-sized chunks, has worker LLMs read them in sequence passing a running message along, and has a manager LLM write the final answer from the last message.

## Method
The problem: long inputs break LLMs in two known ways. Input reduction (truncation, RAG) may drop the part that holds the answer, because retrieval is imperfect. Window extension keeps everything but the model loses focus ("lost in the middle").

The idea: keep every agent's context short and still let the system see all n tokens. Workers W1..Wl each get one chunk (under the window limit k), the query, a task instruction, and a "communication unit" (CU) written by the previous worker. Each worker rewrites the CU: evidence for QA, a running summary for summarization, a code summary with function and class names for code completion. The last CU goes to a separate manager agent, which alone writes the answer.

Why sequential: a multi-hop answer often needs a fact from chunk 1 to know what to look for in chunk 3. Parallel workers cannot hand that fact over. The paper's HotpotQA case study shows worker 1 collecting related evidence without being able to answer, worker 2 extending it, and worker 3 completing the chain.

Assumptions: no training, same base model for every worker and the manager unless stated, left-to-right reading order. Cost argument: encoding time O(nk) rather than O(n^2) for full context, the same decoding time. Design notes in a footnote, with no numbers given: letting the last worker answer directly, or giving the manager every CU, lowered performance because conflicting CUs confused it.

## Evaluated on
- Beats full-context and RAG with an 8k window on all eight non-BookSum datasets (QA, summarization, code) across three model families (text-bison, text-unicorn, gemini-ultra). Example: NarrativeQA with text-bison 25.26 vs 11.96 (full-context) and 14.20 (RAG). The paper states "up to 10%" in the abstract, but its own text cites gains of 12-22 points over the full-context baseline, so the abstract understates or uses a different measure; the text does not reconcile this.
- Beats 200k-window Claude 3 using only an 8k window: on NarrativeQA, opus 23.96 vs 6.56; on BookSum, 17.47 vs 14.00. The gain grows with input length and reaches about 100% for inputs over 400k tokens.
- Helps most where RAG misses: when the gold chunk ranks low in RAG's retrieved list, CoA scores far above RAG's trend line.
- Sequential beats parallel multi-agent designs on all eight datasets. The "Merge" (vote over independent workers) and "Hierarchical" (tree to manager) baselines cannot pass information between workers. Merge falls to 33.66 and Hierarchical to 27.96 on RepoBench-P against CoA's 58.25.
- Ablations: removing the manager costs over 10 points on MuSiQue (26.79 vs 37.09). Right-to-left reading is worse on most datasets. Random order is mixed (better on HotpotQA and Qasper, worse on MuSiQue).
- Lost in the middle: the performance spread across gold-answer positions is 4.89 for CoA vs 6.13 for the vanilla model, with standard deviations of 1.91 and 2.17. That is a small gap with overlapping spreads, so "mitigates" is a modest claim.
- Multi-path (several reading orders, then vote or LLM judge) adds more, but the oracle that picks the best path is far above vote or judge. On HotpotQA, five random orders give 75.73 oracle vs 59.17 with a judge.

## Limitations admitted by the authors
- Communication is not tuned: LLMs are aligned to human norms, which the authors say is not optimal for agent-to-agent messages. No test of fine-tuning or in-context examples.
- Only one communication form is tried; debate or richer discussion between workers is not explored.
- Cost and latency are not reduced. The chain is sequential, so latency grows with the number of chunks (about 18.6 agents on average for BookSum). The authors suggest routing cheaper models in for some workers.
- Selecting among multiple paths is unsolved: vote and judge both land well below the oracle, and which one works better depends on the task.

## Limitations found by others

## What it leaves untried
- No cost or wall-clock comparison against RAG. Only an asymptotic argument against full-context is given, yet the chain runs one call per chunk, serially.
- No test of whether a mistake in an early CU is passed on and compounded, or whether a weak worker could be mixed with a strong manager. The paper uses the same model throughout and names this only as future routing.
- The reading order is fixed or random. Nothing lets the manager or a worker choose which chunks to read, which could shorten the chain.

## Topics
[[Topic - orchestration and delegation]]
