---
title: Evaluate agent workflows / Trace grading (OpenAI API docs)
org: OpenAI
date: 2026
url: https://developers.openai.com/api/docs/guides/agent-evals
kind: tooling-product
category: production-practice
---
# Evaluate agent workflows / Trace grading (OpenAI API docs)

## One line
OpenAI's platform guidance: start agent evaluation from traces, grade traces, then move to datasets and eval runs.

_Added by eval-tooling researcher (2026-10-20):_ OpenAI's docs describe trace grading (scoring a whole agent trace with a grader) plus datasets/eval runs and a grader zoo (string_check, text_similarity, score_model, python, multi), now caught up in the Evals deprecation.

## What they do
Workflow: inspect traces (model calls, tool calls, guardrails, handoffs) -> trace grading against structured criteria (right tool? handoff when expected? instruction/safety violations?) -> datasets and eval runs for repeatability -> Evals API for large batches. Trace grading page: https://developers.openai.com/api/docs/guides/trace-grading. Points to a cookbook on an "evaluation flywheel" for resilient prompts.

_Added by eval-tooling researcher (2026-10-20):_ - Trace grading: open Logs > Traces, inspect a trace (from Agents-SDK apps, or Agent Builder workflows "during the transition window"), create a grader, run it on selected traces, refine prompts/tools/routing/guardrails. Suggested questions: right tool chosen? handoff when it should? instruction/safety policy broken? did a change improve end-to-end behaviour? (https://developers.openai.com/api/docs/guides/agent-evals ; https://developers.openai.com/api/docs/guides/trace-grading)
- Graders (https://developers.openai.com/api/docs/guides/graders): string_check (eq/ne/like/ilike → 0/1); text_similarity (fuzzy_match, BLEU, GLEU, METEOR, ROUGE, cosine — cosine Evals only); score_model (grader model returns numeric score in range + reasoning; used in Evals and reinforcement fine-tuning); python (user grade(sample,item) → float, errors score 0); multi (formula combining sub-graders; RFT only). label_model and endpoint graders exist but not covered on that page.
- Third-party guides (2025-26) describe AgentKit Evals as dataset builder + trace grading + prompt optimizer (https://futureagi.com/blog/openai-agentkit-future-agi-2025/ — secondary).

## Evidence
Docs; no date shown; no numbers.

_Added by eval-tooling researcher (2026-10-20):_ - Graders doc reliability guidance: watch for "grader hacking" (high model-grader scores with poor expert human evaluations); "observability for this is planned" but doesn't exist yet; validate a model grader with a meta-eval of ground-truth grades and check it ranks answers in expert order; use few-shot strong/fair/weak examples; non-numeric outputs default to 0; reasoning models don't accept temperature.
- No agreement or accuracy figures are published for any OpenAI grader.

## Limitations and criticisms
Page does not cover grader calibration against humans. Undated.

_Added by eval-tooling researcher (2026-10-20):_ - All Evals-hosted graders are being deprecated (see 2026-06 deprecation note). One OpenAI nav page lists trace grading under "Legacy APIs" (search summary, unverified).

## Relevance to agent evaluation
Platform-level endorsement of trajectory (trace) grading as the starting point for agents.

_Added by eval-tooling researcher (2026-10-20):_ - Trace grading = judging the full trajectory, the core primitive for an agent-judges-agent setup. OpenAI's "meta-eval the grader against human ground truth" and "grader hacking" warnings are directly applicable when a judge's scores are used as an RL or optimisation signal.

