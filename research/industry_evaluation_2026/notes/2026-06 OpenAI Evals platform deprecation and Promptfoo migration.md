---
title: OpenAI Evals platform deprecation and migration to Promptfoo
org: OpenAI
date: 2026-06
url: https://developers.openai.com/api/docs/deprecations
kind: tooling-product
category: eval-tooling
---
# OpenAI Evals platform deprecation and migration to Promptfoo

## One line
On 3 June 2026 OpenAI announced it is shutting down its hosted Evals platform (dashboard + API) and Agent Builder on 30 Nov 2026, and points users to Promptfoo, which it acquired in March 2026.

## What they do
- Deprecations page: Evals deprecated (notice 3 Jun 2026); existing evals read-only from 31 Oct 2026; Evals dashboard and API shut down 30 Nov 2026. "Graders documented for eval workflows are part of this transition." Agent Builder also shuts 30 Nov 2026 (migrate to Agents SDK or ChatGPT Workspace Agents); reusable prompts / v1/prompts API also shut 30 Nov 2026.
- Migration path: OpenAI cookbook "Moving from OpenAI Evals to Promptfoo" (dated 3 Jun 2026) https://developers.openai.com/cookbook/examples/evaluation/moving-from-openai-evals-to-promptfoo — says supported evals can be exported as runnable Promptfoo configs; workflow shifts from dashboard to config file + CLI, local or CI.
- Community thread: https://community.openai.com/t/deprecation-notice-evals-will-be-shut-down-on-november-30th-2026/1385537

## Evidence
- Dates and wording quoted from the official deprecations page (fetched 2026-10-20).
- A community forum user reported they could not find the "export as runnable Promptfoo config" button (per search summary of the thread; not independently verified).
- Graders doc (https://developers.openai.com/api/docs/guides/graders) itself says "OpenAI is deprecating graders" in evals and fine-tuning workflows, with no separate date.

## Limitations and criticisms
- Lock-in lesson: hosted evals built in a vendor dashboard became read-only with ~5 months' notice. Teams lose the hosted eval history unless exported.
- Neutrality question: the replacement (Promptfoo) is now OpenAI-owned; a third-party comparison flagged neutrality concerns (https://qaskills.sh/compare/promptfoo-vs-openai-evals, secondary).
- No date given for trace grading; the agent-evals guide still documents it (see separate note).

## Relevance to agent evaluation
- The biggest frontier lab is retreating from hosting its own eval product and pushing evals into an open-source CLI that lives in the user's repo. This is strong evidence that "eval definitions in version control" beats dashboard-hosted evals for durability.
- An agent-judging-agent design should not depend on a provider-hosted grader API; keep grader prompts and rubrics in-repo.

