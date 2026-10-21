---
title: "System Switch: When Should a Fast Decision Model Stop and Think?"
authors: Gianluca Bailo
date: 2026-10
arxiv: 2610.09683
url: https://arxiv.org/abs/2610.09683
venue: arXiv
category: alternative-paradigms
pdf: agent as a judge papers/decision models/open models/evaluations/System Switch - When Should a Fast Decision Model Stop and Think (Bailo 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "evaluations"]
topics: ["decision models", "confidence-gated escalation", "adaptive reasoning depth"]
---
# System Switch: When Should a Fast Decision Model Stop and Think?

## One line
A fast one-pass "System One" decision model takes every decision in real-time Doom and hands control to a slow vision reasoner only when a gate on its confidence or on lack of progress opens, and the paper measures what that deferral buys offline and in closed loop.

## Method
The problem: real-time dual-process agents run the slow model continuously, and event-gated ones are turn-based. Here a one-forward-pass typed-decision actor (Laya, Kev, Strands) answers every 0.5s, and a reasoning VLM is called asynchronously while the game runs, so a 12s thought costs 12s of play.

The gate opens on uncertainty (top probability below a threshold three decisions running) or on lack of progress (stuck, failing commands, repetition, no new area). The reasoner then writes a thought and a command that overrides the actor; variants add Doom knowledge to its prompt or commit to its plan until done, failed, damage or 45s.

The central claim: a confidence gate needs sensitivity (AUROC of confidence for right vs. wrong answers), not calibration. Sensitivity can be coarse (which kinds of situation the actor fails) or fine (which answers within a kind). When accuracy varies widely across kinds, coarse is what pays, so the actor should be picked by this AUROC, not by accuracy or ECE.

## Evaluated on
- Accuracy, calibration and sensitivity come apart: five zero-shot actors sit at 0.54-0.60 accuracy, yet their AUROC ranges from 0.60 to 0.89. The best-calibrated (ECE 0.10) rank mid-table on AUROC.
- Deferral gain tracks sensitivity: deferring the 30% least confident decisions beats random deferral by +0.15 for the 0.89-AUROC actor and by about zero for the 0.60-0.61 ones (rank correlation 0.87 over 18 actor-order pairs). With actor and rate picked on held-out games, the gain is +0.13 [0.08, 0.18] in the fixed option order and +0.08 [0.02, 0.14] shuffled.
- The combination matches the reasoner, it does not beat it: 0.75 at 30% deferral vs. 0.69 for the reasoner alone (+0.06 [-0.02, 0.11]). Held-out, the edge over the better of the two parts is +0.05 [-0.12, 0.11].
- Reasoning carries about half the gain: without it, gain over random falls from +0.15 to +0.07.
- In closed loop (33 games), no variant reaches the exit. A fixed "explore" rule behind the same gate covers as much ground (83 cells, 9.7 doors) as the committed reasoner but dies about twice as often (2.7 vs. 1.3 deaths per game). So commitment, not thought content, drives coverage.

## Limitations admitted by the authors
- "Accuracy" means agreement with a rule-based oracle that never labels explore, retreat or wait. Offline scores therefore cannot reward the move the reasoner most often recommends in play, and the two measures diverge.
- The fixed option order inflates results: the correct answer is first in 41% of questions. Shuffling drops Strands from 0.59 to 0.38 and narrows the AUROC spread to 0.52-0.77, and the thinkers were only tested in fixed order.
- Headline numbers choose the actor and rate on the test set. The held-out selection gives the smaller, more honest figures above.
- The closed loop is tiny: three seeds per variant, one map, no successes, so differences in deaths may be noise.
- Latency undercuts real-time use: 9-29s median per thought, plans applied to frames that old, the reasoner busy 38-70% of the game; the offline 30% deferral is impossible live at a median 1,300 tokens per decision.
- Thought faithfulness to game state was only spot-checked. Told that doors can need keys, the reasoner judged ordinary doors locked in 17 of 25 failures, because the state cannot say whether a door is locked.

## Limitations found by others

## What it leaves untried
- One model in two modes (no reasoning by default, reasoning when gated) vs. two models; the authors say their data do not test this.
- A gate that also catches wrong answers within a situation kind: the best actor is at chance there (AUROC 0.52).
- A state that says whether a door is locked. The paper traces the closed-loop failure to this gap but never fills it to see if thoughts then yield progress.

## Topics
[[Topic - decision models]] · [[Topic - confidence-gated escalation]] · [[Topic - adaptive reasoning depth]]
