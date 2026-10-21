---
title: Compaction as Epistemic Failure: How Agentic LLM Tools Fabricate Confirmed Results from Killed Processes
authors: Hiroki Tamba
date: 2026-07
arxiv: 2607.13071
url: https://arxiv.org/abs/2607.13071
venue: arXiv
category: failure-analysis-survey
pdf: research/multiagent_llm_systems/pdfs/2607.13071.pdf
folder: ["multiagent_llm_systems"]
topics: ["agent system failure analysis"]
---
# Compaction as Epistemic Failure: How Agentic LLM Tools Fabricate Confirmed Results from Killed Processes

## One line
A single-author case report showing that Claude Code's session compaction recorded partial terminal output from a killed process as confirmed results, and that later sessions and models inherited the false claims unchecked.

## Method
The problem: agentic coding tools compress long histories into compaction summaries that the next session treats as ground truth. Nobody checks the summary against the raw log, and the receiving model cannot tell a summarised observation from a persisted outcome.

The paper is a case study, not a system. A Python script sent sequential API queries and was meant to write results to a JSON file. It was killed by the timeout (SIGTERM, exit code 143) after two iterations (A1, A2) had printed to the terminal and before anything was written. The compaction summary listed A1 and A2 as completed, with extracted field values. A new session on a different model version (Opus 4.7 to Opus 4.6) accepted them as data points. A separate Claude Chat session accepted them too. The output file actually held zero successes: all 11 recorded attempts failed with HTTP 400.

The proposed root cause is a conflation of observed with persisted. Compaction reads the context window without reference to the exit status, so an abnormal exit never qualifies the claim. The inheritance step then flattens epistemic status, so "the user asked about X" and "A1 completed with result Y" carry equal weight. The author borrows the commit-protocol distinction from databases: output is not complete until written to durable storage.

Proposed remedies, none of them implemented or tested:
- Keep exit codes attached to the outputs they produced.
- Flag the outputs of any non-zero exit as unconfirmed, or re-verify them against files.
- Use tiered confidence for inherited claims, with file-verified claims ranked above terminal-derived ones.
- Add verification checkpoints at model-version boundaries.

The author also links this to his earlier work on LLM-judge non-determinism and to a GitHub issue on Claude Code over-trusting its own outputs, calling the missing safeguard an "observer-aware protocol". The link is argued by analogy only (both are failures of self-report), with no shared measurement.

## Evaluated on
- One incident on July 11, 2026 supports the main claim: a three-layer propagation (compaction, cross-model inheritance, cross-product to Chat). The evidence is the empty output file against a summary that reported two successes.
- Four "structurally identical" failures from a 48-hour window are offered as corroboration. Examples: a database sync that silently failed for twenty days because INSERT logic was missing, and a file listing reported as current though weeks old. These are anecdotes. Only the A1/A2 case is a compaction failure; the others are the model treating absent error signals as success.
- An informal n=1 test of ChatGPT Codex, which inspects files as well as terminal output, correctly separated finished from interrupted runs. The artifacts were deleted, so this cannot be checked.

## Limitations admitted by the authors
- The primary failure is a single instance in one configuration (Claude Code, Opus 4.7/4.6, Windows, one script type). Generalisation to other platforms is argued from the mechanism and not shown.
- The Codex comparison is asymmetric: Claude ran at the end of a multi-hour, high-context session, while Codex ran in a clean sandbox. It shows file-first verification works under light load, not that Codex is immune.
- The discovery came from one heavy user's workflow, so other usage patterns (shorter sessions, less context) may never trigger it. The corroborating cases come from the same researcher in the same 48 hours.
- Compaction is undocumented, so the paper cannot say whether the behaviour is a design choice, a bug or an emergent property of summarising.
- The Codex test data were deleted, so the test is not reproducible.

## Limitations found by others

## What it leaves untried
- Repeating the kill-before-write scenario many times across tools, platforms and context lengths, to get a failure rate instead of one incident.
- Implementing and testing the proposed fixes (exit-code-aware summaries, tiered confidence). Without that there is no evidence they remove the false positives.
- Checking the raw summarisation prompt or output to see why the exit code is dropped. The causal account of "observation-persistence conflation" is inferred from behaviour, not shown.

## Topics
[[Topic - agent system failure analysis]]
