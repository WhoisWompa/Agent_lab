---
title: Announcing Evals and Releases: Evaluate Fin before, during, and after you go live
org: Intercom (Brian Donohue)
date: 2026-08
url: https://www.intercom.com/blog/announcing-evals-and-releases/
kind: tooling-product
category: production-practice
---
# Announcing Evals and Releases: Evaluate Fin before, during, and after you go live

## One line
Intercom's 13 Aug 2026 launch of "eval-driven delivery" for its Fin agent: simulated multi-turn Evals before launch, staged Releases with A/B tests during, and Monitors that judge every live conversation after.

## What they do
- **Evals** = named groups of **Simulations** (multi-turn conversations with a simulated customer, the data/tools Fin can access, and judge criteria). Built manually, uploaded from existing conversations, or generated from real inbox conversations.
- Scoring: "Scoring combines deterministic checks with an LLM judge, and if any single criterion fails, the Simulation fails." Criteria include whether Fin replied, what it needed to say, whether the right Procedure triggered, whether a data connector was called. Results show transcript, event log, outcome (answered / handed to team / handed to workflow).
- **Releases** bundle content, Procedures and Guidance changes; Evals run against a Release before publishing; rollout to all, gradual ramp, or A/B test vs current config, reporting resolution rate, escalation rate, CSAT; pause/fix/re-test or one-step rollback.
- **Monitors** review every live conversation against quality standards and flag failures; flagged conversations become new Simulations.
- Operator (Intercom's ops agent) drafts content changes, builds Evals and Releases as proposals for human approval.
- Help centre: https://www.intercom.com/help/en/articles/15899411-fin-evals-beta (Evals in closed beta).

## Evidence
No performance numbers; illustrative claim that a 1% regression could hit thousands of conversations a day. Product announcement.

## Limitations and criticisms
Marketing; judge validation against humans is not described. Closed beta at time of writing.

## Relevance to agent evaluation
A complete productised loop (sim -> gated release -> online judge on 100% of traffic -> failures back into sims) and an example of an agent (Operator) authoring evals for another agent, with human approval.
