---
title: Promptfoo (open-source eval and red-team CLI), acquired by OpenAI
org: Promptfoo / OpenAI
date: 2026-03
url: https://openai.com/index/openai-to-acquire-promptfoo/
kind: tooling-product
category: eval-tooling
---
# Promptfoo (open-source eval and red-team CLI), acquired by OpenAI

## One line
Promptfoo, the MIT-licensed config-file/CLI eval and red-teaming tool (26k stars), was acquired by OpenAI (announced 9 Mar 2026) for integration into OpenAI Frontier, and is now OpenAI's recommended replacement for its own Evals platform.

## What they do
- Announcement 9 Mar 2026, undisclosed terms; tech to be integrated into OpenAI Frontier (enterprise agent platform); OpenAI says it will keep building the open-source project; founders say it stays open source and supports non-OpenAI models (https://www.promptfoo.dev/blog/promptfoo-joining-openai/ ; https://techinformed.com/openai-moves-to-bring-promptfoo-into-frontier/ ; https://www.sdxcentral.com/news/openai-acquires-ai-testing-firm-to-beef-up-agentic-security/).
- OpenAI claims Promptfoo is used by >25% of Fortune 500 (Futurum, https://futurumgroup.com/?p=87434).
- Features: YAML test configs, assertions (deterministic + LLM rubric), provider comparisons, red-team plugins (prompt injection, data leakage, jailbreaks, agent attacks). CI: `eval` returns exit code 100 on any failure (default 100% threshold) — the only tool of four compared that fails the build by default (beri.net).
- GitHub: 26,164 stars, MIT, active (GitHub API 2026-10-20).

## Evidence
- beri.net: no production trace store or live sampling; paid tiers contact-sales; Node CLI may frustrate notebook-first teams.

## Limitations and criticisms
- Neutrality concerns now that it's owned by a model vendor (https://qaskills.sh/compare/promptfoo-vs-openai-evals — secondary). Unverified deal price estimates ($100–150M) circulate in blogs.

## Relevance to agent evaluation
- Promptfoo's red-team plugins for agents and its CI-gate default make it the de facto open-source test runner; an agent-judge can be plugged in as an llm-rubric assertion.

