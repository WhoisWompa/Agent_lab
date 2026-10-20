---
title: Evals FAQ: Should I use 'ready-to-use' evaluation metrics?
org: Hamel Husain
date: 2026-01
url: https://hamel.dev/blog/posts/evals-faq/should-i-use-ready-to-use-evaluation-metrics.html
kind: essay
category: eval-tooling
---
# Evals FAQ: Should I use 'ready-to-use' evaluation metrics?

## One line
The most-cited practitioner critique of eval tooling: generic prebuilt metrics (helpfulness, coherence, hallucination scores) waste time and create false confidence; do error analysis, define binary failure modes, and validate custom judges against human labels.

## What they do
Recommends error analysis → binary failure modes → custom evaluators validated against human judgment; treat the judge as a classifier (label ~100 outputs pass/fail) (talk deck: https://hamel.dev/blog/posts/revenge/images/The_Revenge_of_the_Data_Scientist.pdf). Simon Willison quotes: off-the-shelf tools rarely address domain needs (https://simonwillison.net/tags/hamel-husain/).

## Evidence
Practitioner opinion; widely echoed by vendors (even Future AGI says off-the-shelf metric lists are the wrong thing to shop on).

## Limitations and criticisms
Date of FAQ entry approximate (2025-26 series).

## Relevance to agent evaluation
Directly undercuts vendor 'prebuilt agent evaluator' catalogues; argues an agent-judge must be task-specific and measured against human labels.

