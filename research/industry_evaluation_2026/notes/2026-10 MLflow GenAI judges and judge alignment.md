---
title: MLflow 3 GenAI evaluation: make_judge and judge alignment (SIMBA/DSPy)
org: Databricks / MLflow
date: 2026-10
url: https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/align-judges
kind: tooling-product
category: eval-tooling
---
# MLflow 3 GenAI evaluation: make_judge and judge alignment (SIMBA/DSPy)

## One line
MLflow 3 (28k stars, Apache-2.0) has custom LLM judges via make_judge() and an automated alignment step that optimises judge instructions against expert feedback using DSPy's SIMBA optimizer.

## What they do
- Workflow: baseline judge assessments → expert corrections logged under the judge's exact name → optimize (default SIMBA). Minimum ~10 traces, 50–100 better.
- Databricks claims alignment improves agreement with humans by 30–50% vs baseline (vendor-stated).
- Not supported for session-level/multi-turn judges (e.g., ConversationCompleteness).
- Version confusion: docs variously require MLflow 3.4.0+ or 3.14.0+; align() signature changed across versions (https://mlflow.org/docs/3.5.1/genai/eval-monitor/scorers/llm-judge/alignment).
- MLflow also has a ConversationSimulator with goal+persona test cases (experimental) (via https://www.lyzr.ai/?p=140045).

## Evidence
- 30–50% figure is Databricks' marketing; no independent replication found.

## Limitations and criticisms
- Alignment only for single-turn judges; API drift.

## Relevance to agent evaluation
- One of very few products that *optimises* a judge against human labels automatically rather than just measuring agreement — the most direct productisation of judge calibration.

