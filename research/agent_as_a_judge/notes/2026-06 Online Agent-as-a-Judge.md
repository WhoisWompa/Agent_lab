---
title: Online Agent-as-a-Judge: Situation-Generating Evaluation for Interactive Agents
authors: Hyogon Ryu et al.
date: 2026-06
arxiv: 2606.08200
url: https://arxiv.org/abs/2606.08200
venue: ICML 2026 Workshop (Trustworthy AI for Good)
category: self-evolving-tests
---
# Online Agent-as-a-Judge: Situation-Generating Evaluation for Interactive Agents

## One line
An in-world evaluator agent interacts with the target through the environment's own dialogue/action interface and creates situations tied to evaluation criteria, instead of scoring a free-running trajectory afterward.

## Method
Judge is an agent inside the environment; given criteria, it provokes situations (e.g. conflicts) that would otherwise not arise, then collects evidence on immediate and later behaviour. Criteria are designer-authored.

## Evaluated on
Life-simulation environment with 32 designer-authored social criteria; improves criteria coverage and agreement with human labels over post-hoc trajectory scoring (abstract gives no values).

## Limitations admitted by the authors
- Single environment (life simulation); generalisation not addressed in the abstract.
- Criteria fixed and human-authored.

## Limitations found by others


## What it leaves untried
- Persist the situations as a test set and refine them across rounds based on which criteria went unobserved or were misjudged.
