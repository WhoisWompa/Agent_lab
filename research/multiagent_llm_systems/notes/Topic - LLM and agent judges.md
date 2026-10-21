---
type: topic
group: Judging and evaluation
---
# Topic - LLM and agent judges

Using an LLM or an agent to evaluate agents or model outputs. Judge designs and prompting, agentic judges that inspect trajectories or run code, reference-based and reference-free judging, methods that make a judge more accurate or less biased. The paper's subject is the judge or the act of judging.

Group: Judging and evaluation. See [[Topics]]. Same group: [[Topic - judge and decision-model audits]], [[Topic - trained judges and reward models]], [[Topic - agent evaluation benchmarks]], [[Topic - user simulation]], [[Topic - alternative evaluation paradigms]], [[Topic - self-evolving tests]], [[Topic - judges as reward signals]], [[Topic - stopping rules]].

## Papers (7)
- [[2022-12 Constitutional AI]] — Trains a harmless but non-evasive assistant with no human harmlessness labels, using a short list of written principles that a model applies to critique its own answers and to judge answer pairs, then distilling those judgments into a reward for RL. (also: [[Topic - judges as reward signals]], [[Topic - trained judges and reward models]], [[Topic - self-refinement and critique loops]])
- [[2025-03 Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation]] — A prompted weaker LLM that reads a frontier agent's chain-of-thought catches reward hacking far better than one that sees only actions, but training the agent against that monitor teaches it to hide its intent. (also: [[Topic - judges as reward signals]])
- [[2025-10 Scaling Agents for Computer Use]] — Runs many independent computer-use agent rollouts and picks the best with Behavior Judge (BJudge), a VLM judge that compares short "behavior narratives" instead of raw screenshot trajectories, reaching 72.6% on OSWorld.
- [[2026-03 Beyond Task Completion]] — Scores agents on how they reach an outcome (policy, grounding, honesty of statements) and disqualifies "corrupt successes", finding that 27-78% of tau-bench successes hide violations. (also: [[Topic - agent evaluation benchmarks]], [[Topic - agent system failure analysis]])
- [[2026-04 Evaluating LLM Agents on Automated Software Analysis Tasks]] — A benchmark of 35 tool-project setup tasks plus a staged single agent (AnalysisAgent) that reaches 94% manually verified success where the best existing agent reaches 77%. (also: [[Topic - agent evaluation benchmarks]])
- [[2026-06 From Confident Closing to Silent Failure]] — Agents often claim a task is done when the environment state says it is not, LLM judges cannot catch this (AUROC at most 0.65), and a TF-IDF classifier catches it far better. (also: [[Topic - judge and decision-model audits]], [[Topic - agent system failure analysis]])
- [[2026-06 The Verification Horizon]] — Qwen's experience report argues that every reward for coding agents is a proxy for user intent that the policy eventually exploits, so the verifier must be rebuilt as the generator improves, and shows four verifier designs that do this. (also: [[Topic - judges as reward signals]])
