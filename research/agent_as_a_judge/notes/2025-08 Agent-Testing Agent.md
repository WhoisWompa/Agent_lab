---
title: Agent-Testing Agent: A Meta-Agent for Automated Testing and Evaluation of Conversational AI Agents
authors: Sameer Komoravolu, Khalil Mrini
date: 2025-08
arxiv: 2508.17393
url: https://arxiv.org/abs/2508.17393
venue: arXiv
category: self-evolving-tests
---
# Agent-Testing Agent: A Meta-Agent for Automated Testing and Evaluation of Conversational AI Agents

## One line
A meta-agent that reads a target conversational agent's code, interviews its designer, mines literature, then runs persona-driven adversarial dialogues whose difficulty adapts to judge feedback to hunt the target's weakest capabilities.

## Method
Inputs: target source (static code analysis), designer interview, web/literature search. Generates personas and test dialogues; talks to the target over its conversational interface; each dialogue is scored by an LLM-as-a-Judge rubric; a weakness-planning step keeps difficulty estimates and steers later tests toward low-scoring capabilities. Outputs metrics plus bug reports. Open-source.

## Evaluated on
Two targets: a travel planner and a Wikipedia-writing agent. Found more diverse and more severe failures than expert annotators while matching their severity ratings; 20-30 minutes vs. days for 10-annotator rounds. Ablation: removing code analysis and web search increased variance and miscalibration.

## Limitations admitted by the authors
- Two target agents only.
- Judge rubric is an LLM; its calibration is compared with annotators but not improved during the loop.

## Limitations found by others


## What it leaves untried
- Track where the judge's scores disagree with humans and refine rubric and tests from that, not only from target weakness.
