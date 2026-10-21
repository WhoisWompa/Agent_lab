---
type: topic
group: Agent systems
---
# Topic - self-refinement and critique loops

A model critiques and revises its own output, or is critiqued by a second model, over one or more rounds (Self-Refine, Reflexion, RCI, generator-critic loops). The subject is what the loop changes, when it helps or hurts, and what stops it. The critique is a step in producing the answer, not a judgment of someone else's output.

Group: Agent systems. See [[Topics]]. Same group: [[Topic - orchestration and delegation]], [[Topic - role-based agent teams]], [[Topic - strategic play among LLM agents]], [[Topic - multi-agent debate and consensus]], [[Topic - automated pipeline and topology search]], [[Topic - communication topology and channels]], [[Topic - agent system failure analysis]].

## Papers (2)
- [[2023-10 Large language models cannot self-correct reasoning yet]] — Shows intrinsic self-correction without external feedback often fails to improve and can degrade reasoning accuracy. (also: [[Topic - judge and decision-model audits]], [[Topic - LLM and agent judges]])
- [[2024-07 Spontaneous Reward Hacking in Self-Refinement]] — When a generator iteratively optimises against an LLM evaluator (especially the same model with shared context), evaluator scores rise while human-judged quality stalls or drops. (also: [[Topic - judge and decision-model audits]], [[Topic - judges as reward signals]])
