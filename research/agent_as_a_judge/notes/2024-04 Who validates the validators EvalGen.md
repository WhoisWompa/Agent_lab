---
title: Who Validates the Validators? Aligning LLM-Assisted Evaluation of LLM Outputs with Human Preferences
authors: Shreya Shankar et al.
date: 2024-04
arxiv: 2404.12272
url: https://arxiv.org/abs/2404.12272
venue: UIST 2024
category: alternative-paradigms
topics: ["LLM and agent judges", "alternative evaluation paradigms"]
---
# Who Validates the Validators? Aligning LLM-Assisted Evaluation of LLM Outputs with Human Preferences

## One line
EvalGen: mixed-initiative interface where users grade a subset of outputs and the system selects LLM or code assertions that agree with those grades; documents 'criteria drift'.

## Method
LLM proposes criteria and candidate assertion implementations (prompts or Python); user grades outputs; implementations chosen by alignment with grades. Sees outputs only.

## Evaluated on
Qualitative user study with practitioners (participant count not re-verified); users supported the approach but alignment proved subjective and iterative.

## Limitations admitted by the authors
- (self-evolving-tests slice) Small user study (9 participants).
- (self-evolving-tests slice) Assertions selected on a small graded sample may overfit it.
- (self-evolving-tests slice) Criteria drift means evaluations are never final; the tool exposes it but does not resolve it.
- Criteria drift: users need criteria to grade outputs, but grading outputs defines the criteria; some criteria depend on outputs seen.
- Small qualitative study.

## Limitations found by others


## What it leaves untried
- Applying EvalGen-style alignment to agent-trajectory judges.

## Topics
[[Topic - LLM and agent judges]] · [[Topic - alternative evaluation paradigms]]
