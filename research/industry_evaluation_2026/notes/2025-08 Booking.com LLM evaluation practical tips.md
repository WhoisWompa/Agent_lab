---
title: LLM Evaluation: Practical Tips at Booking.com
org: Booking.com (George Chouliaras, Antonio Castelli, Zeno Belligoli)
date: 2025-08
url: https://booking.ai/llm-evaluation-practical-tips-at-booking-com-1b038a0d6662
kind: production-practice
category: production-practice
---
# LLM Evaluation: Practical Tips at Booking.com

## One line
Booking.com's 2025 lessons from a year of judge-LLM development (booking.ai, Aug 2025; reposted MLOps Community 9 Sep 2025): golden datasets with explicit annotation protocols, judges validated as classifiers, strong judge in development and a cheaper distilled judge for production monitoring.

## What they do
- Golden data must match production distribution; low inter-annotator agreement means an ambiguous metric definition.
- Prefer binary or few-class metrics; bin continuous scores.
- Basic protocol: define metric with business owner, ~50-example pilot, annotate 500-1,000; SME reviews ~10% and annotation is redone if >10% wrong. Advanced: 3+ annotators, aggregate by min/max/mean/majority; handle disagreement via a "not sure" class, vote-share weighting, or discarding.
- Validation/test split (50/50 default); start with a strong model (GPT-4.1 or Claude 4.0 Sonnet) as ceiling; few-shot examples never from golden set; macro-F1 for classification, MSE for continuous; iterate until a stakeholder-agreed threshold; never tune on test.
- **Strong judge for development, weak judge for production monitoring**, re-engineered to match the strong judge; dashboard with automated anomaly alerts to app owners.
- Automated prompt optimisation inspired by OPRO, with human review of final prompt for leakage.

## Evidence
Effort: prompt engineering ~1 day to 1 week; annotation days to weeks. No agreement numbers or thresholds published. Mirror: https://mlops.community/blog/llm-evaluation-practical-tips-at-bookingcom.

## Limitations and criticisms
Explicitly excludes agent evaluation ("a topic on its own"). No numbers on judge accuracy or cost.

## Relevance to agent evaluation
Provides a concrete annotation protocol and the strong/weak judge cascade pattern for cost-controlled online monitoring, reusable for trajectory judges.
