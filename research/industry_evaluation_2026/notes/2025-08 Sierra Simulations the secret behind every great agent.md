---
title: Simulations: the secret behind every great agent
org: Sierra (Sachi Shah)
date: 2025-08
url: https://sierra.ai/blog/simulations-the-secret-behind-every-great-agent
kind: production-practice
category: production-practice
---
# Simulations: the secret behind every great agent

## One line
Sierra's 19 Aug 2025 post describing how its customer-service agents are tested with simulated personas graded by an independent judge agent, auto-generated from customer SOPs, and gated in CI.

## What they do
- Mock personas vary language, technical comfort, tone; preset context (logged in, email on file) mirrors real conditions; edge cases such as spelling an email letter by letter.
- A separate judge agent grades each simulated conversation: did the user reach their goal, did the agent follow SOPs, stay on brand, give accurate, helpful, clear answers.
- Each simulation can be run multiple times and all runs graded (no k given).
- Test cases auto-generated from SOPs, knowledge bases, historical coaching transcripts and conversation flows; persisted and re-run after each update.
- CX teams run sims alongside Journeys in Agent Studio before publishing; developers run them via GitHub Actions or CLI and can **gate releases** on specific simulations like unit tests.
- Follow-on: Voice Sims (Sep 2025) simulate callers with different languages, accents, emotional states, sharing the same eval infrastructure.

## Evidence
Customers run "over 35,000 tests (and growing) each day"; claims resolution rates up to 90% and CSAT above 4.5/5. These are marketing figures; no judge accuracy, simulator fidelity or failure rates are reported, and test volume is not linked to outcomes.

## Limitations and criticisms
Vendor blog. Silent on how the judge agent is validated against humans and on simulator realism (simulated users are known to be easier or differently distributed than real ones). No pass^k number despite Sierra authoring tau-bench.

## Relevance to agent evaluation
The clearest public description of the simulated-user + judge-agent pattern used in production customer-service agents: an agent (judge) evaluates another agent (the CS agent) talking to a third (the simulated user), with results used as release gates.
