---
title: Anthropic: Console Evaluation tool and Managed Agents 'Outcomes' rubric grader
org: Anthropic
date: 2026-05
url: https://platform.claude.com/docs/en/managed-agents/define-outcomes
kind: tooling-product
category: eval-tooling
---
# Anthropic: Console Evaluation tool and Managed Agents 'Outcomes' rubric grader

## One line
Anthropic's first-party eval surface is thin (Console prompt-eval tool since July 2024) but in 2026 it added an in-harness rubric grader for Managed Agents ('Outcomes') that grades the agent's output in a separate context and feeds failures back for retry.

## What they do
- Console Evaluate tab (launched July 2024, https://www.anthropic.com/news/evaluate-prompts; docs https://platform.claude.com/docs/en/test-and-evaluate/eval-tool): prompts with {{variables}}; add test cases manually, CSV import, or Claude-generated; run all; side-by-side comparison of prompt versions; SME grading on a 5-point scale.
- Managed Agents Outcomes (public beta; launched 6 May 2026 at Code with Claude per third-party write-ups, e.g. https://inventivehq.com/blog/claude-agents-outcomes-rubric-grading): harness provisions a grader that checks output against a user rubric; grader runs in its own context window "so the main agent's choices don't bias it"; reports which criteria passed/failed; agent iterates (third-party: default 3 iterations, max 20). Cookbook: https://platform.claude.com/cookbook/managed-agents-cma-verify-with-outcome-grader (stateless grader fetches every URL and checks every quote).
- Anthropic Humanloop team acqui-hire (Aug 2025): https://techcrunch.com/2025/08/13/anthropic-nabs-humanloop-team-as-competition-for-enterprise-ai-talent-heats-up/

## Evidence
- No dedicated hosted eval/observability product comparable to Foundry/AgentCore/Vertex found as of Oct 2026 (searched; gap, not proof of absence).
- Outcomes defaults and launch date from secondary sources; official doc confirms mechanism.

## Limitations and criticisms
- Console eval tool is single-turn prompt evaluation, not agent/trajectory evaluation. Rubric quality determines grader reliability (third-party guide notes loosely worded criteria lead to unreliable grading).

## Relevance to agent evaluation
- Outcomes is literally "an agent that judges another agent" built into a lab's runtime: separate-context grader, rubric, feedback loop. It's verification-in-the-loop rather than offline evaluation.

