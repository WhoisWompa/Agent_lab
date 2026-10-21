---
title: Does a Tool Result Carry More Authority Than Plain Text? Three Prospective Studies of False-Claim Adoption in a Synthetic Assignment Task with Claude Opus 5
authors: Justin Bronder et al.
date: 2026-08
arxiv: 2608.14992
url: https://arxiv.org/abs/2608.14992
venue: arXiv
category: failure-analysis-survey
pdf: research/multiagent_llm_systems/pdfs/2608.14992.pdf
folder: ["multiagent_llm_systems"]
topics: ["judge and decision-model audits", "presentation sensitivity", "abstention and fallback"]
---
# Does a Tool Result Carry More Authority Than Plain Text?

## One line
Three preregistered studies on one model ask whether an unsupported claim is adopted more often when it arrives as a native tool result than as plain text, and find the apparent tool-result advantage disappears once the text comparator is made active.

## Method
The concern: agents read from stores they also write to, so a claim written earlier without checking can come back as a tool result with an ID and timestamp. Nothing new is known, only the packaging changed. If packaging alone moves the answer, write-then-read-back manufactures false corroboration, and provenance fields become safety controls.

The test is a synthetic lookup. Claude Opus 5 is asked for the assigned code of a named item (AMBER, ORCHID, SABLE) or ABSTAIN. The correct code is never visible; a wrong "planted" code appears in one message. The endpoint is false-code adoption, an output measure, not evidence of belief.

- Studies 1 and 2 (inter-turn): the planted claim sits in a no-claim control, a prior assistant assertion, a tool-result record, or a tool-result record inside a ten-field metadata wrapper marked `support_status: unchecked`.
- Study 3 (same turn): both records are announced in advance and placed in the final user turn, and target binding is swapped between the linked tool result and an inline JSON record. This replaces the earlier assistant-assertion comparator, which sat at the same floor as the no-claim control.

The paper's own point is that a native tool result differs from text in role, serialization, linkage, forced position and fulfilling the "retrieve" instruction, so package contrasts cannot isolate channel authority.

## Evaluated on
- Tool result beats assistant assertion between turns: 14/24 vs 0/22 scorable in Study 1 (no-claim 0/24), then 7/24 vs 0/24 in a fresh preregistered run, one-sided Fisher p = 0.0047.
- The model reads the record, not a fixed bias toward a token: tool-result arm picked the record's code in 11/12 supported trials, but false adoption varied by planted token (8/8 SABLE, 4/8 ORCHID, 2/8 AMBER in Study 1).
- The rate is unstable across days: 14/24 on Aug 9 fell to 7/24 on Aug 13 (post hoc p = 0.080 unstratified, 0.021 stratified); the cause is unidentified.
- The headline reverses with an active text control: inline announced text gave 60/60 adoption, tool result 57/60, so the registered superiority criterion failed (p = 1, a ceiling artifact, not equivalence).
- The metadata wrapper is not a mitigation: versus the raw tool result, 15/24 vs 14/24 adoption, seven more abstentions, eight fewer correct supported answers.
- Abstention gates answering: no-claim and assistant-assertion arms abstained on 36/36 and 34/34 scorable trials; the tool-result arm abstained 11/36.
- A free, reliable verifier tool, called in 144/144 conversations, gave 0/96 false adoption, but that run was nonconcurrent and changed several components, so it is not a causal estimate.

## Limitations admitted by the authors
- External validity is narrow: one model alias, one API, one synthetic template with opaque IDs and three color tokens. The setup may evoke benchmark compliance more than natural memory use.
- Treatments are bundled message packages (role, linkage, serialization, forced first position, retrieval fulfillment), so no channel effect is isolated.
- Adoption may be competent compliance: the model had no way to tell the planted record was false, so it does not show gullibility.
- The comparators were badly placed: the assistant arm sat at the no-claim floor (non-detection is not equivalence), and the inline arm hit the ceiling at 60/60, leaving no room to detect a difference.
- Study 3 changed the system prompt and conversation graph, so its rates cannot be pooled with Studies 1 and 2.
- Run-to-run drift (14/24 to 7/24) occurred with no checkpoint identifier; provider cybersecurity refusals also hit other runs (34/36 in one portfolio), so the instrument interacts with provider classification.
- Live save, retrieval and persistence were not exercised; a proposed third same-turn arm separating groundedness from native provenance was not run.

## Limitations found by others

## What it leaves untried
- A same-turn arm that separates task-sanctioned groundedness from native provenance, the only way to tell whether any channel effect exists once linkage and position are bundled.
- Other models, vendors and task templates; the paper argues these would add breadth without fixing the underidentified mechanism.
- The operational question the authors name as next: whether a fixed evidence-checking or provenance policy lowers uptake of unsupported records while keeping correct use of supported ones, with concurrent controls.

## Topics
[[Topic - judge and decision-model audits]] · [[Topic - presentation sensitivity]] · [[Topic - abstention and fallback]]
