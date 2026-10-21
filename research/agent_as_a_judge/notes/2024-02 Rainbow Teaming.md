---
title: Rainbow Teaming: Open-Ended Generation of Diverse Adversarial Prompts
authors: Mikayel Samvelyan et al.
date: 2024-02
arxiv: 2402.16822
url: https://arxiv.org/abs/2402.16822
venue: NeurIPS 2024
category: self-evolving-tests
topics: ["self-evolving tests"]
---
# Rainbow Teaming: Open-Ended Generation of Diverse Adversarial Prompts

## One line
Quality-diversity (MAP-Elites) search that grows an archive of adversarial prompts, one cell per (risk category x attack style), against one target LLM.

## Method
Archive with predefined feature dimensions (risk category, attack style). Each iteration: sample a parent prompt, a Mutator LLM mutates it toward a target cell, the target responds, a Judge LLM compares the new prompt's response with the incumbent in that cell (pairwise preference) and the more harmful one is kept. Black-box, output-only judging. Also applied to question answering and cybersecurity.

## Evaluated on
Above 90% attack success rate across tested models (incl. Llama 2-chat and Llama 3-Instruct). Fine-tuning the target on generated data improves its safety without hurting general capability, per the authors.

## Limitations admitted by the authors
- Feature descriptors (categories/styles) are hand-chosen, which bounds what can be discovered.
- Relies on an LLM judge for harmfulness, which can misjudge; pairwise comparison reduces but does not remove this.
- The archive is specific to the target model; transfer to other models is partial.

## Limitations found by others


## What it leaves untried
- Let the archive dimensions themselves evolve from what the judge found uncovered.
- Audit and repair the judge using disagreements surfaced during search.

## Topics
[[Topic - self-evolving tests]]
