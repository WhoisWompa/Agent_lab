---
title: Amazon Bedrock AgentCore Evaluations
org: Amazon Web Services
date: 2026-03
url: https://aws.amazon.com/blogs/machine-learning/build-reliable-ai-agents-with-amazon-bedrock-agentcore-evaluations
kind: tooling-product
category: eval-tooling
---
# Amazon Bedrock AgentCore Evaluations

## One line
AWS's managed agent-evaluation service (preview at re:Invent Dec 2025, GA by 31 Mar 2026) with built-in LLM-judge evaluators at session, trace and tool level, ground-truth trajectory matchers, custom LLM judges and Lambda code evaluators, run online on sampled production traffic or on demand in CI.

## What they do
- Preview announcement Dec 2025 (https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-bedrock-agentcore-policy-evaluations-preview): "13 built-in evaluators".
- GA blog (31 Mar 2026) lists: Session — Goal Success Rate; Trace — Helpfulness, Correctness, Coherence, Conciseness, Faithfulness, Harmfulness, Instruction Following, Response Relevance, Context Relevance, Refusal, Stereotyping; Tool — Tool Selection Accuracy, Tool Parameter Accuracy; plus ground-truth Trajectory Exact Order / In-Order / Any Order Match.
- Ground truth inputs: expected_response (Correctness), expected_trajectory (trajectory evaluators), assertions = natural-language outcome statements (GoalSuccessRate).
- Judges: built-in judge reasons before scoring, with fixed prompts/models/criteria "to keep results consistent"; judge model not named; managed capacity with cross-Region inference. Custom LLM judges (own model, instructions, scoring schema). Code evaluators = AWS Lambda receiving OpenTelemetry spans.
- Online mode samples a % of production traces, up to 10 evaluators per config, results in CloudWatch. On-demand API for CI (max 10 evaluations per call). "Same evaluators" in CI and production.
- Third-party evaluators: DeepEval and AutoEval libraries offered (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/third-party-evaluators.html). Custom code-based evaluators blog: https://aws.amazon.com/blogs/machine-learning/build-custom-code-based-evaluators-in-amazon-bedrock-agentcore/

## Evidence
- The blog says 13 evaluators but lists 14 (count inconsistency). No pricing in post. No agreement-with-human statistics.
- Reliability advice in the post: calibrate custom evaluators with SMEs; if inconsistent, make instructions specific, make score levels distinct, lower temperature; LLM judges are unreliable for exact-match checks — use code.

## Limitations and criticisms
- Built-in judge model is opaque (not named). Judges are fixed by AWS, so users can't inspect or tune them beyond writing custom ones.

## Relevance to agent evaluation
- GoalSuccessRate with natural-language assertions is the closest cloud analogue to "agent judges whether the goal was met". The OTel-span-in, score-out Lambda contract is a clean pattern for deterministic side-effect checks.

