---
title: Agents' Room: Narrative Generation through Multi-Step Collaboration
authors: Fantine Huot et al.
date: 2024-10
arxiv: 2410.02603
url: https://arxiv.org/abs/2410.02603
venue: ICLR 2025
category: orchestrator-worker
pdf: research/multiagent_llm_systems/pdfs/2410.02603.pdf
folder: ["multiagent_llm_systems"]
topics: ["role-based agent teams", "orchestration and delegation"]
---
# Agents' Room: Narrative Generation through Multi-Step Collaboration

## One line
A fixed pipeline of specialised planning agents and section-writing agents, sharing one scratchpad, writes long stories that expert readers prefer over single-call baselines.

## Method
The problem: one LLM call asked for a long story produces text that is too short, generic and repetitive, and long detailed prompts are brittle. The paper treats long-form writing as a collaboration problem and splits it by narrative theory.

- Two kinds of agent. Planning agents (conflict, character, setting, plot) write only to a shared scratchpad. Writing agents (exposition, rising action, climax, falling action, resolution) each write one section of the final story and also post it to the scratchpad. The story is the concatenation of the writing agents' outputs.
- The scratchpad starts as the writing prompt and grows by one labelled entry per agent call. Each agent sees the whole scratchpad; its own prompt template reformats it, so the scratchpad stays free of prompts.
- A central orchestrator picks the next agent. Here it is deterministic (conflict, character, setting, plot, then the five sections in order), justified only by the "strong narrative theory prior". The framework allows learned orchestrators, but none is tried.
- Why it should work: each call has a narrow job, the sections are generated piecemeal so length is not capped by one call, and later agents read earlier decisions instead of re-inventing them.
- Agents are either zero-shot prompted or LoRA-fine-tuned. Because the dataset has no plan or section annotations, a larger teacher model reverse-engineers them from human stories (distilled backtranslation), and the small model is trained on those.

The same Gemini 1.5 Flash backbone serves every system. Baselines include one-shot zero-shot or fine-tuned writing, one-shot with plan or reflection instructions, and a two-call plan-then-write chain.

## Evaluated on
A new 123-story training set plus 52 validation and 55 test prompts (TELL ME A STORY, written by professional-level writers; stories average about 1,500 tokens), judged on plot, creativity, development and language.

- Writing agents beat every baseline: expert raters preferred the stories from the variants with writing agents (best: fine-tuned write and plan+write) over all single-call and two-stage baselines on every dimension (Figure 3; no numeric margin in the text).
- Fine-tuned agents beat zero-shot agents, which the authors read as evidence that backtranslated synthetic data works.
- Length: variants with writing agents give about 3,000 words against about 1,100 to 1,200 for one-shot baselines and 1,439 for humans.
- Planning alone does not help: the plan-only variant ranks poorly, which the authors attribute to its single simple finalizer agent being unable to use the plan (a guess, not tested).
- Humans still win: human-written stories are preferred overall, across all dimensions, with the smallest gap on language use. Raters preferred the longer story only 0.51 of the time, so length does not explain this.
- An LLM judge (Gemini 1.5 Pro, pairwise) tracks humans: system-level Spearman 0.62, item-level 0.41. It picks the same story 90.2% of the time when order is swapped. Human inter-annotator agreement is Fleiss kappa 0.46.

## Limitations admitted by the authors
- The orchestrator is deterministic and the agent set is hand-picked for one narrative structure, so the work cannot show that dynamic orchestration or other structures help. It is left for future work.
- The dataset is small (123 training stories), so it cannot train a model from scratch. Only LoRA on a small model is possible.
- Machine stories remain more repetitive than human ones: the longest systems have the highest repetition (inter-story trigram repetition about 42 to 44 against 19 for humans), and unique-word ratio is about 46 to 47 percent against 15.5 percent. More length costs diversity. Machine stories also start sentences with an article or pronoun more often than humans.
- Agreement is modest: kappa 0.46 between humans, and item-level LLM-human correlation only 0.41, so the automatic judge is not a safe stand-in for single stories.
- Generated stories may carry biases from training data.

## Limitations found by others

## What it leaves untried
- A learned orchestrator that chooses or skips agents per prompt. The fixed order makes it impossible to tell whether the gain comes from the collaboration or simply from the section split and the longer output.
- An ablation against one model doing the same section-by-section writing with the same plan. No such control is reported, so "multi-agent" versus "multi-call" is not separated.
- Agents that critique or revise earlier scratchpad entries, and human-in-the-loop editing. Both are mentioned as possible but not run.

## Topics
[[Topic - role-based agent teams]] · [[Topic - orchestration and delegation]]
