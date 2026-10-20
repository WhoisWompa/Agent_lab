---
title: Cursor AI support bot invents login policy
org: Cursor / Anysphere (reported by Fortune, eWeek, AIID)
date: 2025-04
url: https://incidentdatabase.ai/cite/1039/
kind: production-practice
category: production-practice
---
# Cursor AI support bot invents login policy

## One line
April 2025 incident (AIID #1039) where Cursor's AI support agent "Sam" told users device logouts were an intended policy; no such policy existed, and users cancelled subscriptions.

## What they do
Users logged out when switching devices received an email from "Sam" claiming a one-device policy; co-founder Michael Truell denied it on Reddit. Coverage: https://fortune.com/article/customer-support-ai-cursor-went-rogue and https://www.eweek.com/news/cursor-ai-chatbot-hallucination-fake-policy/ (eWeek 22 Apr 2025).

## Evidence
Well documented across outlets; dated 2025-04-19 in AIID.

## Limitations and criticisms
No post-mortem from Cursor on what evaluation or guardrail was missing.

## Relevance to agent evaluation
Illustrates a failure class (confident policy fabrication in an unsupervised customer-facing agent) that groundedness/policy-adherence judges and simulation suites aim to catch, and why vendors now gate on procedure adherence.
