# Discussion summary, 2026-10-20: judge agent design

What was discussed in the session after the two research runs. Not a plan.

## Research done

- `research/agent_as_a_judge/` : the academic literature on agent-as-a-judge, LLM-as-a-judge, trained judges, agent evaluation, alternative paradigms, self-evolving tests. 300 paper notes, six slice summaries, `report.md`.
- `research/industry_evaluation_2026/` : what labs, tool vendors, independent evaluators and deploying companies do for evaluation as of October 2026. 133 source notes, four slice summaries, `report.md`.

## What the research says, in one paragraph each

**Academic.** Nobody has built a judge that is pointed at one target agent, talks to it, keeps its own test set, and refines both its tests and its own verdicts each round. The pieces exist separately. Every evaluation method that holds up does so by changing what evidence the judge sees (execution, state, trace, references, a small human-labelled anchor), not by better prompting. The thing that breaks first is always the grader, not the model. Label-free judge self-repair raises judge-judge agreement without raising agreement with humans. An agent's narration can raise judge false positives by up to 90% while its actions are unchanged.

**Industry.** Everyone uses AI to grade AI. Labs grade capability by execution and safety by LLM judges, and run auditor-agent-plus-judge loops (Anthropic's Petri pattern, adopted by xAI and Meta). Deployers run simulated-user suites as release gates and fold failures back as new tests. Almost nobody publishes how often the AI judge agrees with a human. Nobody runs the two-loop design above.

## Design points agreed in discussion

1. **The reasoning text is out of the score.** It is model-specific noise and the main place faking lives. Keep it for diagnosis only.
2. **Score on what the agent cannot alter.** The base-written trace in `logs/` (tool calls and results), the state of the world after the run (files, `data/`, outputs), and checks the judge runs itself. Tool-call arguments are still agent-written text, so call names and results are the hard facts, payloads are not.
3. **Action trajectory for hard rules.** Forbidden tool, looping, claiming success before a tool returned, writing outside its folder. Yes/no facts from the harness.
4. **Two judges with different views of the same run.** One reads the full span (reasoning included), one reads only actions and state. Disagreement is the signal: full-span passes and actions-only fails means the narration carried the verdict. The disagreement set is the labelling queue; cases the user decides become the frozen anchor set. The size of the disagreement set over rounds is a drift metric for the builder-judge loop. Not found in the literature.

## Things to watch, not blockers

- Agreement between the two judges is not a pass. Same-family judges share blind spots. Never tune one judge toward the other.
- The judge-to-builder loop is a Goodhart loop: whatever the judge rewards, the builder produces. Shopify's judge was gamed once it became the reward.
- Judges flip about one in seven verdicts on re-run. Sample more than once or make the actions-only side rule-based.
- Judge drift on model upgrade: pin the judge's model and prompt version, re-measure against the anchor set on every change.
- Eval awareness: a frontier-model target can recognise a test style. Keep a held-out slice the builder never sees.

## What the user flagged about the session

Answers were front-loading caveats on every idea, including good ones. Agreed to push back only on actual disagreement and to stop hedging ideas that are cheap to try.
