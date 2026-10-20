---
title: Who Validates the Validators? Aligning LLM-Assisted Evaluation of LLM Outputs with Human Preferences
org: Shreya Shankar, J.D. Zamfirescu-Pereira, Bjoern Hartmann, Aditya Parameswaran, Ian Arawjo (UIST 2024)
date: 2024-04
url: https://arxiv.org/abs/2404.12272
kind: essay
category: production-practice
---
# Who Validates the Validators? Aligning LLM-Assisted Evaluation of LLM Outputs with Human Preferences

## One line
UIST 2024 paper introducing EvalGen and naming "criteria drift": users need criteria to grade outputs, but grading outputs is how they define criteria. Pre-window, but the intellectual root of 2025-26 practitioner advice.

## What they do
EvalGen proposes candidate assertions (Python functions and LLM grader prompts), asks the user to grade a subset of outputs, and keeps the assertions that align with those grades. Qualitative study with 9 industry practitioners.

## Evidence
Users' criteria changed as they saw outputs; some criteria were output-dependent. Secondary summary (emergentmind) says no participant's initial criteria matched their final labels (unverified). Follow-on: PROMPTEVALS (NAACL 2025), 2,087 pipeline prompts with 12,623 assertion criteria.

## Limitations and criticisms
Small qualitative study; prototype tool.

## Relevance to agent evaluation
Justifies "look at data before writing rubrics" and re-validating judges as criteria evolve; any judge agent's rubric is a moving target.
