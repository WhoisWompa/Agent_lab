---
title: Talk Structurally, Act Hierarchically: A Collaborative Framework for LLM Multi-Agent Systems
authors: Zhao Wang et al.
date: 2025-02
arxiv: 2502.11098
url: https://arxiv.org/abs/2502.11098
venue: arXiv
category: topology-communication
pdf: research/multiagent_llm_systems/pdfs/2502.11098.pdf
folder: ["multiagent_llm_systems"]
topics: ["communication topology and channels", "self-refinement and critique loops", "orchestration and delegation"]
---
# Talk Structurally, Act Hierarchically: A Collaborative Framework for LLM Multi-Agent Systems

## One line
TalkHier makes agents exchange a fixed three-part message (instruction, background, intermediate output) and routes feedback through a nested evaluator team whose supervisor summarises it before the generator's answer is revised.

## Method
The paper names two faults in multi-agent LLM systems. First, agents talk in long free text, so a receiving agent loses the task context or the required output format. Second, refinement uses sequential or flat evaluators, so feedback is not summarised, the evaluators are not balanced against each other, and results depend on the order in which feedback arrives. The paper cites other work for both faults and does not measure them itself.

Two changes address them.

- **Structured communication.** Every message between agents has three fields: the message (the subtask and its format), the background (the problem's core details and decisions so far), and the intermediate output (the sender's work product). Background is left out on member-to-supervisor edges. Each agent also keeps its own persistent memory instead of a shared pool.
- **Hierarchical refinement.**
  - Teams are nested: a member of one team can be the supervisor of another.
  - A main supervisor asks an evaluation supervisor to score the current answer.
  - The evaluation supervisor hands one criterion to each evaluator, for example intent, responsibility and well-being for moral questions, or truth tables for logic.
  - It collects the verdicts and summarises them into one report.
  - The main supervisor checks the report against a quality threshold. If it passes, the answer is returned. If not, a revisor rewrites the answer, up to a maximum number of rounds.

Summarising before the generator sees feedback is meant to remove the order bias and the dropped opinions of a flat evaluator chain. The graph of agents is fixed, and the supervisor chooses who speaks next at run time. The threshold is only described in the prompt as "ensuring correctness" or "achieving high relevance".

## Evaluated on
All systems use GPT-4o. The o1 baseline is a different model.
- Beats multi-agent baselines on five MMLU subjects. TalkHier scores 88.38% average accuracy, against AgentVerse at 83.66%, AgentPrune at 83.60%, and GPT-4o with 7-run majority vote at 71.15%.
- Roughly ties o1-preview, which scores 87.56%. That is 0.82 points ahead, and the authors say the comparison is not like-for-like.
- Leads on WikiQA: ROUGE-1 0.3461 against AutoGPT's 0.3286, and BERTScore 0.6079 against 0.5885.
- On Japanese ad headlines (Camera), BERTScore is 0.91 against 0.73 for OKG. Faithfulness is 8.6 against 6.3. The character-count violation rate is 4%, the same as OKG, against 16-17% for GPT-4o and ReAct. Attractiveness is 6.2, below ReAct at 7.0 and GPT-4o at 6.5.
- Ablation (three MMLU subjects, full system 87.21%):
  - Removing the evaluation team drops it to 76.15%.
  - Removing the evaluation supervisor drops it to 81.86%.
  - Replacing the structured protocol with plain text drops it to 84.43%.
  - Single-agent ReAct scores 67.33%.
  - So hierarchy matters more than protocol.
- Protocol fields: dropping background alone gives 78.30%, and dropping intermediate output alone gives 82.55%.
- The automatic ratings agree only weakly with people. On 10 headlines, Pearson correlation with the mean of four human raters is 0.67, but agreement with an individual rater (ICC 0.23) is poor.

## Limitations admitted by the authors
- Cost is high. Each question uses about 36,000-65,000 tokens ($0.13-0.23). Final runs cost about $2,100, and failed attempts probably tripled that. This limits who can reproduce the work.
- The human check of the evaluators is small and weak: 10 headlines, ICC(2,1) of 0.23, and no confidence intervals. The refinement loop depends on these ratings, so the authors only call the feedback "relatively meaningful".
- Baselines were hard to set up for ad text, so only three were run. AutoGPT, AgentVerse and GPTSwarm were left out because they needed heavy customisation. The Camera gain (17.63% mean) is measured against one specialised baseline, OKG.

## Limitations found by others

## What it leaves untried
- A comparison at equal compute. Majority voting uses 3-7 calls and TalkHier about 40,000+ tokens per question, so how much of the gain comes from spending more is unmeasured.
- Separate ablations of the order bias and of summarisation. The paper claims hierarchy removes order bias but never shuffles evaluator order or tests a flat team that also summarises.
- A test of the agent-specific memory. It is presented as a contribution, but the ablations never remove it. Table 4 also shows that dropping both background and intermediate output (82.25%) beats dropping background alone (78.30%), and the paper does not explain this.

## Topics
[[Topic - communication topology and channels]] · [[Topic - self-refinement and critique loops]] · [[Topic - orchestration and delegation]]
