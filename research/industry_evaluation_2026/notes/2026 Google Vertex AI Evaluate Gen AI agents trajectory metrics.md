---
title: Evaluate Gen AI agents (Vertex AI / Gemini Enterprise Agent Platform docs)
org: Google Cloud
date: 2026
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/evaluation-agents
kind: tooling-product
category: production-practice
---
# Evaluate Gen AI agents (Vertex AI / Gemini Enterprise Agent Platform docs)

## One line
Google's agent evaluation docs defining reference-trajectory metrics alongside final-response evaluation.

## What they do
trajectory_exact_match (identical tool calls, same order), trajectory_in_order_match (reference calls in order, extras allowed), trajectory_any_order_match (all reference calls, any order), plus precision/recall-style variants and final-response judging; custom agents return response + trajectory dict.

## Evidence
Docs; no data.

## Limitations and criticisms
Reference-trajectory matching penalises valid alternative paths, which Anthropic explicitly warns against ("grade the outcome more than the path").

## Relevance to agent evaluation
Shows the cloud-vendor default is reference-trajectory comparison, a contrast with outcome-state grading favoured by practitioners.
