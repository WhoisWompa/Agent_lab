---
title: Demystifying evals for AI agents
org: Anthropic (Mikaela Grace, Jeremy Hadfield, Rodrigo Olivares, Jiri De Jonghe)
date: 2026-01
url: https://anthropic.com/engineering/demystifying-evals-for-ai-agents
kind: lab-practice
category: production-practice
---
# Demystifying evals for AI agents

## One line
Anthropic's engineering guide (9 Jan 2026) to building evals for agents: vocabulary (task, trial, grader, transcript, outcome, harness), three grader types, capability vs regression suites, pass@k vs pass^k, an eight-step roadmap and per-agent-type recipes, drawn from Claude Code and customers.

## What they do
- Defines the agent under test as model plus harness; grades the **outcome** (final environment state, e.g. the reservation exists in the DB) not the agent's claims.
- Three grader types: **code** (string/regex, fail-to-pass and pass-to-pass tests, static analysis, state checks, tool-call checks), **model** (rubrics, NL assertions, pairwise, reference-based, multi-judge consensus), **human** (SME review, spot-check sampling, A/B tests, inter-annotator agreement). Advice: deterministic where possible, LLM where needed, humans sparingly to calibrate. Scoring can be weighted, binary (all must pass) or hybrid.
- **Capability evals** start at a low pass rate ("a hill to climb"); **regression evals** sit near 100%; capability tasks "graduate" into regression once saturated.
- **pass@k vs pass^k**: 75% per-trial success gives ~42% pass^3; by k=10 pass@k nears 100% while pass^k nears 0. pass^k for customer-facing agents.
- Per agent type: coding (unit tests + code-quality rubric usually suffice; example adds ruff/mypy/bandit, security-log state checks, turn/token/latency metrics); conversational (state check + transcript constraint like <10 turns + LLM rubric for empathy, with a second LLM simulating the user, as in tau-bench / tau2-bench); research (groundedness, coverage, source quality; frequent expert calibration); computer use (check real/sandbox state, WebArena/OSWorld style).
- Roadmap: (0) start early with 20-50 tasks from real failures; (1) convert manual checks, tickets, bug reports; (2) unambiguous tasks with reference solutions, "two domain experts reach the same verdict"; (3) balanced sets (should and should-not trigger, e.g. Claude.ai web search over/under-triggering); (4) isolated, clean-state harness; (5) grade outcome over path, partial credit, calibrate judges with humans, give judge an "Unknown" option, one isolated judge per rubric dimension, hack-resistant graders; (6) read transcripts; (7) monitor saturation; (8) dedicated evals team owns infra, domain experts and PMs/CS/sales contribute tasks via PR.
- Online layer: automated evals on every change and model upgrade; production monitoring for drift; A/B tests once traffic allows; triage user feedback constantly; sample transcripts weekly; human studies for calibration ("Swiss cheese" layering).
- Named practice: Descript (three dimensions: don't break things, do what I asked, do it well; moved from manual grading to LLM graders with human calibration; separate quality and regression suites); Bolt (built eval system in ~3 months for an already-popular agent: static analysis + browser agents that test generated apps + LLM judges for instruction following); Qodo; Claude Code (began with concision and file edits, later over-engineering).

## Evidence
- CORE-Bench: Opus 4.5 initially scored 42%, rose to ~95% after fixing rigid grading (penalising "96.12" vs "96.124991..."), ambiguous specs and irreproducible stochastic tasks.
- Terminal-Bench tasks failed because they omitted a required file path; METR time-horizon tasks penalised instruction-following models.
- Internal eval leak: Claude read git history left by prior trials (shared state inflates scores).
- Opus 4.5 "failed" a tau2-bench airline task by finding a policy loophole that was better for the user.
- "As a rule, we do not take eval scores at face value until someone digs into the details of the eval and reads some transcripts."
- Teams with evals adopt a new model "in days rather than weeks" (claim, no data).
- Internal inconsistency: SWE-bench Verified start given as 40% in one place and 30% in another.

## Limitations and criticisms
Vendor-authored guidance by a model lab; customer anecdotes (Descript, Bolt, Qodo) are not quantified. No reported judge-human agreement figures. Little on cost of eval pipelines. Treats production monitoring as complementary but gives no concrete online-judge design. Appendix lists Harbor, Braintrust, LangSmith, Langfuse, Arize as frameworks without evaluation of them.

## Relevance to agent evaluation
The most complete lab statement of agent eval practice as of 2026: outcome-state grading, transcript grading as a secondary layer, simulated users for conversational agents, pass^k for reliability, and explicit warnings that the grader itself is often the bug (broken tasks, rigid graders, leaky harnesses). For a judge agent: isolate one judge per dimension, give it an "Unknown" exit, calibrate against experts, and prefer state checks over trajectory judgments where state is observable.

_Added by eval-tooling researcher (2026-10-20):_ - Its "grade outcomes not paths" stance contrasts with vendor trajectory-match evaluators (exact/in-order/any-order); and it insists on reading transcripts to validate graders — the human check on an agent-judge.
_Added by frontier-labs researcher (2026-10-20):_ Anthropic's own system cards apply this at scale: the Claude Opus 5 card's automated behavioural audit runs ~3,200 investigator-agent sessions scored by a separate judge on dozens of dimensions, and BrowseComp transcripts are post-hoc scanned by 'a verifier Claude' for answer leakage (see note '2026-07 Anthropic Claude Opus 5 System Card').
