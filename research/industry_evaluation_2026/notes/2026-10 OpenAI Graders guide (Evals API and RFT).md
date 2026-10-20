---
title: Graders (OpenAI API docs)
org: OpenAI
date: 2026-10
url: https://developers.openai.com/api/docs/guides/graders
kind: tooling-product
category: frontier-labs
---
# Graders (OpenAI API docs)

## One line
OpenAI's developer guide (accessed Oct 2026, publication date unknown) to graders used by the Evals API and reinforcement fine-tuning, which now states that OpenAI is deprecating graders in those workflows.

## What they do
- Grader types: string_check (eq/neq/like/ilike, 0/1), text_similarity (fuzzy_match, bleu, meteor, cosine, ROUGE), score_model (a grader model returns a numeric score in a range from a user prompt; sampling params incl. reasoning effort; pass_threshold), python (grade(sample, item) -> float), and multi (formula combining sub-graders; RFT only). label_model exists in the API reference but is not on this page as fetched.
- Same grader objects serve as eval metrics and as RFT reward functions (score 0-1, partial credit); endpoints /fine_tuning/alpha/graders/run and /validate return reward and sub-rewards.
- Docs recommend Python graders for determinism; model graders "flexible but nondeterministic".

## Evidence
- Deprecation text: "OpenAI is deprecating graders as part of the evals and fine-tuning workflows they support." Points to the deprecations page; no dates or replacement on this page.

## Limitations and criticisms
- Date of the deprecation notice and timeline not verified (deprecations page not read).

## Relevance to agent evaluation
Concrete link between evaluation and training: the identical rubric/model grader is both the eval and the RL reward. The deprecation signals OpenAI moving this surface; anyone building an agent judge on it should check the deprecation timeline.
