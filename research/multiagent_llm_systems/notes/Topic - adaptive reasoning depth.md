---
type: topic
group: Mechanisms
---
# Topic - adaptive reasoning depth

Spending extra compute (looping, partial chain of thought, handing off to a slow reasoner) only on inputs where the fast decision is unsure, and how the switch is decided.

Group: Mechanisms. See [[Topics]]. Same group: [[Topic - confidence-gated escalation]], [[Topic - calibration]], [[Topic - presentation sensitivity]], [[Topic - abstention and fallback]], [[Topic - reasoning prompting]].

## Papers (2)
- [[2023-11 ADaPT]] — A recursive controller lets an LLM executor try a task directly and calls an LLM planner to split it into sub-tasks only when the executor reports failure, repeating at each level. (also: [[Topic - orchestration and delegation]])
- [[2025-02 MaAS]] — MaAS learns a distribution over multi-agent workflows (an "agentic supernet") and samples a different, cheaper-or-richer system for each query, instead of searching for one fixed system. (also: [[Topic - automated pipeline and topology search]])
