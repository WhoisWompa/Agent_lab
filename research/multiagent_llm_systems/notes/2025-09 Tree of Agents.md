---
title: "Tree of Agents: Improving Long-Context Capabilities of Large Language Models through Multi-Perspective Reasoning"
authors: Song Yu et al.
date: 2025-09
arxiv: 2509.06436
url: https://arxiv.org/abs/2509.06436
venue: arXiv
category: topology-communication
pdf: research/multiagent_llm_systems/pdfs/2509.06436.pdf
folder: ["multiagent_llm_systems"]
topics: ["communication topology and channels", "multi-agent debate and consensus"]
---
# Tree of Agents: Improving Long-Context Capabilities of Large Language Models through Multi-Perspective Reasoning

## One line
Splits a long document across several agents that share summaries, then re-read each other's chunks in many different orders and vote, so an 8B model comes close to much larger long-context models on long-document QA.

## Method
The problem: on long inputs, models under-use the middle ("lost in the middle"), input reduction (retrieval, compression) can drop the key clue, and prior multi-agent methods read in one fixed order. Chain of Agents passes messages one way along a chain, so errors amplify. LongAgent depends on a leader that decomposes the task, and it needs fine-tuning.

Tree of Agents (TOA) has three phases.
- **Chunk perception.** Each of N agents gets one chunk (N=5 in the main runs). It returns evidence and a tentative answer for the query, which is its "cognition".
- **Multi-perspective reasoning.** Each agent reads the others' cognitions (not their chunks) and picks which other chunks it wants. It then tries every ordering of those chunks. The orderings form a tree, and the agent updates its cognition after each chunk. The claim is that reading order changes interpretation, so different paths can fill the gaps of a path that missed a clue. The paper supports this with a toy example (appendix) and the gains below, with no direct measurement of order effects.
- **Consensus.** Each agent keeps the cognition from its longest path, on the assumption that more context reduces local bias (cited, not tested here). It answers from that cognition, and a majority vote across agents decides. Agents may answer "none". A tie goes to an extra agent.

Cost control, since orderings grow factorially:
- Prefix-hash cache: paths sharing a prefix reuse the stored state.
- Adaptive pruning: if the agent marks a chunk "useless" at some point on a path, the rest of that path is dropped. The agent itself makes this judgment.

It is training-free and plug-and-play.

## Evaluated on
- Highest accuracy among the methods built on the same base model: with LLaMA3.1-8B, 54.3% on DetectiveQA and 45.0% on NovelQA. With DeepSeek-V3 it gets 57.3% and 47.3% (NovelQA is not the top score there: Chain of Agents has 48.0%). These figures are from 100 sampled questions per dataset, averaged over three runs.
- Close to commercial long-context models. GPT-4o scores 56.0% and 48.7%, and Gemini 1.5-pro 55.7% and 45.7%. The 8B TOA is slightly below both on each dataset (for example 45.0% vs 45.7% for Gemini on NovelQA). DeepSeek-V3 TOA is above them on DetectiveQA only.
- Far fewer "none" answers: 1.7% on DetectiveQA and 4.3% on NovelQA, against 37.0% and 16.0% for Chain of Agents with the same 8B model. The authors read this as less hallucination. The paper does not separately measure hallucination, and a low none-rate could also mean overconfident wrong answers.
- Needle-in-a-haystack (1K to 128K, 8B model): average score 9.38 (single needle) and 7.77 (two needles), against 8.31 and 4.07 for Chain of Agents. It stays steady at middle depths, where Sequential and Vote drop.
- Stable on inputs up to 100K tokens, while Chain of Agents falls sharply beyond 64K.
- Five agents is best, which the authors attribute to chunk-size balance. DetectiveQA accuracy is 46.0% at 3 agents, 54.3% at 5 and 51.0% at 7. NovelQA is 25.0%, 45.0% and 28.0%.
- Caching and pruning cut phase-2 API calls from 2103 to 1034 (50.8%) with DeepSeek-V3. The whole pipeline still uses 2534 calls against 2287 for Chain of Agents.

## Limitations admitted by the authors
- Extra compute from probing many orders, growing with the number of chunks. Even with caching and pruning, inference is slower than the simple baselines, and the authors say this is a problem for large-scale deployment.
- Pruning depends on the base model's own judgment. The appendix says its effect is small on small models. Token savings with LLaMA3.1-8B are 5%, against 59% on NovelQA and 33% on DetectiveQA with DeepSeek-V3.
- Token use stays well above Chain of Agents: with DeepSeek-V3 on NovelQA, 12.8M tokens against 10.2M even after caching and pruning.

## Limitations found by others

## What it leaves untried
- No ablation of the order probing, the longest-path rule or the majority vote on their own. The paper never shows that multiple orderings, rather than just more agent passes, produce the gain.
- Only multiple-choice QA on novels and needle retrieval, with 100 samples per dataset. Summarisation and other tasks that need global understanding are untested.
- All orderings are tried (there is no sampling of orders), so cost scales factorially with chunk count. Selecting a few orders would be the obvious fix.

## Topics
[[Topic - communication topology and channels]] · [[Topic - multi-agent debate and consensus]]
