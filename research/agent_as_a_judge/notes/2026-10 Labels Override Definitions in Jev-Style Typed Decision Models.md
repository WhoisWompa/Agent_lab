---
title: Labels Override Definitions in Jev-Style Typed Decision Models
authors: Seyedarmin Azizi et al.
date: 2026-10
arxiv: 2610.02586
url: https://arxiv.org/abs/2610.02586
venue: arXiv
category: llm-judge-foundations
pdf: agent as a judge papers/decision models/open models/evaluations/Labels Override Definitions in Jev-Style Typed Decision Models (Azizi 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "evaluations"]
topics: ["decision models", "judge and decision-model audits", "presentation sensitivity"]
---
# Labels Override Definitions in Jev-Style Typed Decision Models

## One line
Shows that open Jev-style typed decision models (and LLMs scoring label strings) decide from the option's name rather than the caller's written definition, and traces this to one line of prompt rendering that writes "{label}: {definition}" into the input.

## Method
A typed decision model returns a probability per caller-defined option in one forward pass; each option has a short label and a definition, and the definition is the only place to state the actual rule. The interface implies a posterior over definitions, with labels as identifiers. The paper tests that implication by treating label and definition as two independent channels and varying them separately: meaningful labels, arbitrary labels (A/B), labels swapped onto the wrong definition, labels only, or neither. A definition-following model should be indifferent to the label; preference for the label is "option-label bias", distinct from the input-independent prior that contextual calibration removes.

PolicyBench makes the label carry zero information: synthetic tickets whose route is a boolean rule stated only in one definition. Its controlled version (XF) gives the false branch an explicit negation, because with "none of the above" it mostly measured a preference for the more specific definition.

The key causal move is a patch in both directions with weights untouched: delete the label from LAYA's rendering, and add it to VON's (which already passes only definitions). This yields a two-call test: ask twice changing only labels; if distributions differ, labels drive the decision. No gold labels or weights needed.

## Evaluated on
- Definitions are ignored when a label is present: deleting all definitions leaves LAYA-TD accuracy unchanged (0.8559 vs 0.8487), though definitions alone support 0.7971 vs a 0.5690 no-information control; a label contradicting its definition drops accuracy to 0.1357, below chance.
- Meaningful names hurt when the rule lives in definitions: renaming options to A/B raises LAYA-TD by +0.1511 [+0.1377, +0.1646] on PolicyBench-XF; LAYA-EN falls to 0.5297 under misleading names (chance 0.5).
- The cause is rendering, not the decision head: removing the label makes all three LAYA checkpoints exactly invariant (+0.0000); adding it to VON drops its accuracy from 0.8511 to 0.2281 under contradicting labels.
- Plain LLMs show it too, contradicting Sun et al.'s attribution to the constrained head: Qwen2.5-7B gains +0.1203 and Mistral-7B +0.1531 from A/B labels.
- Confidence gating fails under the bias: LAYA-TD's confidence AUROC goes from 0.8123 to 0.2433 under contradicting labels, so a confidence threshold would accept the wrong decisions and escalate the right ones.
- Polarity is not read: "Is it false that" flips 0.9656 to 0.9825 of LAYA decisions and 0.9711 of VON's. Mitigations: A/B labels +0.1511; null-state prior correction +0.0391 for LAYA-TD but drives VON to 0.5000; an "ignore the labels" instruction only +0.0138.

## Limitations admitted by the authors
- Hosted Jev is not measured; the mechanism claim covers only the two open code bases.
- PolicyBench is synthetic and templated, buying exact ground truth at the cost of naturalness, so +0.1511 may not transfer to real routing rules.
- The misleading condition is arguably an under-specified request, so the argument is rested on arbitrary vs aligned and arbitrary vs exchanged contrasts, where nothing is contradictory.
- The definitions are the authors' own wording; different phrasing would move the absolute numbers.
- LAYA-ML, Qwen2.5-1.5B and Llama-3.1-8B sit near chance on PolicyBench (Llama answers one class on 98.6% of items), so their small contrasts are not evidence of robustness.
- Removing the label is not free: where class names are informative, LAYA-TD drops from 0.8487 to 0.8067; VON with missing definitions returns uniform.
- Latency and cost, the stated case for typed models, are not measured.

## Limitations found by others

## What it leaves untried
- No fix for the negation failure, present in every typed model and unmoved by an explicit warning (0.3546).
- No training with label/definition conflicts, which could keep an informative label's benefit without letting it override definitions, avoiding the 0.8487 to 0.8067 trade.
- The two-call test is never run on hosted Jev, though it needs no weights; that would show whether the closed model shares the cause.

## Topics
[[Topic - decision models]] · [[Topic - judge and decision-model audits]] · [[Topic - presentation sensitivity]]
