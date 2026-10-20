# Self-evolving tests and judges (2022 to October 2026)

Scope: evaluation where the evaluator is generated, grown or refined rather than fixed. Four families: (A) dynamic / refreshed benchmarks, (B) LLM-generated benchmarks and test suites, (C) adversarial and red-team test generation against one target, (D) self-improving judges and evolving rubrics. Plus (E) evaluation agents that run a loop against a target. One note per paper is in `notes/` with `category: self-evolving-tests` (50 new notes; 12 existing notes extended).

Method caveat: arXiv ids and dates were checked on arXiv abstract pages for the 2024-2026 papers that matter most (2512.06751, 2508.17393, 2610.13303, 2607.15092, 2602.23729, 2606.08092, 2606.08200, 2603.15611, 2405.14125, 2502.07577, 2412.09645, 2609.02246, 2608.00017, 2402.11443, 2407.08351, 2504.19162, 2605.30568, 2408.02666, 2602.04254). Older well-known papers (Perez 2022, Rainbow Teaming, DyVal, LiveBench, LiveCodeBench, EvalPlus, CodeT, Meta-Rewarding, EvalGen, OMNI-EPIC, SWE-smith, R2E-Gym, SWE-Gym, CURE) are given from established knowledge with their arXiv ids; numbers for these should be spot-checked before quoting. Requested names I could NOT confirm as real papers: "Self-Instruct for eval", "Language models can generate their own tests", "Adversarial test generation for agents", "Generative adversarial evaluation" as a titled paper, "AutoEval loops". They are treated as themes, not papers. AdaTest (Ribeiro and Lundberg, ACL 2022) has no arXiv id that I could confirm.

## Q1. Which evaluators get sharper over rounds by looking at where they missed or misjudged? How is "missed" measured without ground truth? What stops drift or collapse?

### Takeaway
Two disjoint lines exist. Test generators that sharpen against the target (red teaming, AutoDetect, ALI-Agent, ATA, AutoBencher) measure "missed" as "the target passed my test", scored by a fixed judge. Judges that sharpen themselves (Self-Taught Evaluators, Meta-Rewarding, LWE, SEMJ, rubric-evolution papers) measure "misjudged" through proxies: synthetic labels by construction, a meta-judge, self-inconsistency, cross-lingual inconsistency, or inter-judge disagreement. The 2026 evidence is that the label-free proxies raise consistency without raising agreement with humans, so anchoring to an external oracle (execution, ground truth, a small human set, frozen holdouts) is the only drift stop that has been shown to work.

### Cited Findings
- Self-Taught Evaluators: the "missed" signal is a synthetic label by construction (the response to a perturbed instruction is worse); the judge is fine-tuned on its own verdicts that match it, iterated; Llama3-70B-Instruct goes from 75.4 to 88.3 on RewardBench (88.7 with majority vote) — [arXiv 2408.02666](https://arxiv.org/abs/2408.02666)
- Meta-Rewarding: one model is actor, judge and meta-judge; the meta-judge ranks judgments to train the judging skill; AlpacaEval 2 LC win rate 22.9% to 39.4% for Llama-3-8B-Instruct; needs an explicit length-control step because the loop otherwise drifts to longer outputs — [arXiv 2407.19594](https://arxiv.org/abs/2407.19594)
- Learning While Evaluating (LWE): a judge keeps an evolving meta-prompt that writes per-sample criteria and revises itself from self-generated feedback, with no training or validation set; Selective LWE updates only on cases where the judge is self-inconsistent (self-inconsistency is the "missed" signal) — [arXiv 2512.06751](https://arxiv.org/abs/2512.06751)
- SEMJ: cross-lingual inconsistency of a judge's verdicts is the trigger to send a case back for self-reflection and re-evaluation; beats voting and reflection baselines — [arXiv 2606.08092](https://arxiv.org/abs/2606.08092)
- Rubric evolution needs a way to compare two rubrics; Rubrics on Trial compares synthetic responses written to satisfy each rubric and penalises unnecessary criteria via violate/satisfy response pairs — [arXiv 2607.15092](https://arxiv.org/abs/2607.15092)
- Wang and Blanco generate dataset- and instance-level rubrics without human annotation and iteratively fine-tune the rubric generator from meta-judge rewards; a 14B generator beats a larger proprietary model — [arXiv 2605.30568](https://arxiv.org/abs/2605.30568)
- Key negative result: rewriting the rubric clauses with most inter-judge disagreement raised judge-judge Krippendorff alpha by +0.069 (95% CI 0.046-0.092) on SummEval but changed human agreement by Kendall tau -0.007 (CI -0.037 to 0.021); on HealthBench and USR the preregistered criteria were not met; human agreement was lower after contested-clause edits than control edits on all three datasets (CIs include zero) — [arXiv 2610.13303](https://arxiv.org/abs/2610.13303)
- EvalGen documents "criteria drift": users need criteria to grade outputs, but grading outputs changes the criteria, so evaluation criteria cannot be fully fixed in advance — [arXiv 2404.12272](https://arxiv.org/abs/2404.12272)
- In a production self-improvement loop, rewriting the judge's rubric gave limited gains, while a structural constraint on the judge's output order helped reliably; frozen holdouts and canary cases (a perfect score signals cheating) are the proposed drift stops — [arXiv 2609.02246](https://arxiv.org/abs/2609.02246)
- When an LLM judge's scores are stored in memory and reused, wrong episodes get inflated scores that compound (the "Echo Gap"); a correcting signal must have errors independent of the memory's self-grading bias (Error-Independence Assumption); LUCID 56.9% vs. 54.0% for self-graded memory on BIRD — [arXiv 2608.00017](https://arxiv.org/abs/2608.00017)
- SPC trains a critic against a "sneaky generator" that injects subtle reasoning errors; ProcessBench accuracy 70.8% to 77.7%; the ground truth that keeps it honest is that injected errors must change final answers — [arXiv 2504.19162](https://arxiv.org/abs/2504.19162)

### Inferences
- No paper found combines both halves: a judge that sharpens its tests against one target and also repairs its own scoring from cases where it misjudged. Test generators keep the judge fixed; self-improving judges do not generate tests for a target.
- Self-inconsistency (LWE, SEMJ) and inter-judge disagreement (2610.13303) catch unstable judgments but not stable wrong ones. The Error-Independence Assumption in 2608.00017 states the general reason: a correcting signal whose errors correlate with the judge's own errors cannot fix them.
- The practical drift stops seen across papers are: execution or ground-truth oracles (CURE, SPC, LiveBench, SWE-smith), a frozen human-labelled holdout (PROCTOR), and canary items.

### Gaps
- I found no paper reporting a long multi-round run (more than a handful of iterations) of a self-improving judge with human-agreement tracked per round; Meta-Rewarding and Self-Taught Evaluators report 3-5 iterations.
- Numbers for LWE and SEMJ were not available from the abstracts.

## Q2. Which papers generate tests targeted at one specific system's weaknesses? What about test validity and coverage?

### Takeaway
Target-specific generation is well established for LLMs (Perez 2022, PAIR, Rainbow Teaming, AutoDetect, ALI-Agent, ACD, AutoBencher, EvalTree, MART) and emerging for agents (ToolEmu's adversarial emulator, Agent-Testing Agent, Online Agent-as-a-Judge, ATAD). Validity is handled well only where an oracle exists (code execution, reference solutions); elsewhere it rests on an LLM judge plus sampled human checks. Coverage is usually handled by quality-diversity archives or taxonomies, and the attack-strength vs. diversity trade-off recurs.

### Cited Findings
- Perez et al.: a red LM generates test cases against one 280B chatbot, escalating zero-shot, few-shot from past hits, supervised and RL; RL gives the highest failure rate but the least diverse tests — [arXiv 2202.03286](https://arxiv.org/abs/2202.03286)
- Rainbow Teaming handles coverage with a MAP-Elites archive over hand-chosen risk-category x attack-style cells; reports above 90% attack success on tested models — [arXiv 2402.16822](https://arxiv.org/abs/2402.16822)
- AutoDetect: Examiner, Questioner and Assessor agents iteratively search one target LLM's weaknesses; identification success rate above 30% on ChatGPT and Claude — [arXiv 2406.16714](https://arxiv.org/abs/2406.16714)
- ALI-Agent: emulation plus iterative refinement of misconduct scenarios against one target, with a memory module of past test records and a tool-using evaluator — [arXiv 2405.14125](https://arxiv.org/abs/2405.14125)
- AutoBencher: an LM proposes and refines dataset descriptions as an optimisation over declared properties; answers grounded in retrieved documents or a Python tool for validity; 22% more model errors than existing benchmarks — [arXiv 2407.08351](https://arxiv.org/abs/2407.08351)
- Automated Capability Discovery: a scientist model proposes thousands of tasks against a subject model, clustered into dozens of capability/failure areas; human surveys agree highly with model-generated scores — [arXiv 2502.07577](https://arxiv.org/abs/2502.07577)
- EvalTree builds a capability tree over benchmark instances and reports low-accuracy subtrees as a model's weakness profile (e.g. GPT-4o mini 75.1% on combinatorics vs. 49.1% on trigonometric geometry within MATH) — [arXiv 2503.08893](https://arxiv.org/abs/2503.08893)
- Agent-Testing Agent: reads the target agent's code, interviews the designer, runs persona-driven adversarial dialogues whose difficulty adapts to LLM-judge rubric scores; found more diverse and severe failures than expert annotators, 20-30 minutes vs. days; removing code analysis and web search increased variance and miscalibration — [arXiv 2508.17393](https://arxiv.org/abs/2508.17393)
- Online Agent-as-a-Judge: the evaluator acts inside the environment via the target's own dialogue/action interface and creates situations tied to 32 designer-authored criteria; improves criteria coverage and human agreement — [arXiv 2606.08200](https://arxiv.org/abs/2606.08200)
- ATAD: teacher writes problems, orchestrator validates and screens them, student solves; solved problems trigger harder variants — difficulty co-evolves with the student; invalid problems are sent back for revision — [arXiv 2602.23729](https://arxiv.org/abs/2602.23729)
- Evaluation Agent probes a generative model over multiple rounds with few samples per round, choosing the next probe from the last result; about 10% of the evaluation time of standard pipelines — [arXiv 2412.09645](https://arxiv.org/abs/2412.09645)
- Test validity in code: CURE shows generated tests can be wrong (hallucinated expected outputs) or correct-but-naive (pass incomplete code), and rewards tests that separate correct from incorrect solutions — [arXiv 2506.03136](https://arxiv.org/abs/2506.03136)
- Code-A1: single-model self-play with white-box access leads to self-collusion (trivial tests), black-box testers give generic tests; separates Code LLM and Test LLM with opposing rewards, a validity-vs-difficulty composite reward and a Mistake Book — [arXiv 2603.15611](https://arxiv.org/abs/2603.15611)
- Agentic Verifier iteratively refines an input generator with execution feedback to find inputs that separate candidate programs; up to +10-15 points absolute Best@K on five benchmarks — [arXiv 2602.04254](https://arxiv.org/abs/2602.04254)

### Inferences
- Targeted tests are only as valid as their oracle. Code work solves validity with execution and reference solutions; open-ended and agent settings fall back to LLM judges, which re-imports judge error into the "weakness" measurement.
- Agent-specific work (ATA, Online Agent-as-a-Judge) shows white-box information about the target (code, designer intent) and acting through the target's own channel both raise coverage.

### Gaps
- Few papers report what fraction of generated tests were invalid. Exceptions I saw: ToolEmu (about 68.8% of identified failures confirmed as true risks by humans) and TestGen-LLM (75% build, 57% pass reliably, 25% raise coverage); both are from established knowledge, not re-verified this session.
- No paper measured coverage of an agent's behaviour space in a principled way beyond category archives.

## Q3. Failure modes: Goodharting, collusion, leakage, criteria drift, degenerate tests, cost

### Takeaway
All the predicted failure modes are documented. Collusion and degenerate tests are named in code co-evolution (Code-A1). Drift appears as length drift (Meta-Rewarding), criteria drift (EvalGen) and consensus-without-alignment (2610.13303). Goodharting and reward hacking appear in production loops (PROCTOR). Self-bias in generated benchmarks and memory reward inflation are newer named failures. Leakage motivates the dynamic-benchmark line.

### Cited Findings
- Collusion / degenerate tests: white-box single-model self-play "leads to self-collusion" where the model writes trivial tests for easy reward — [arXiv 2603.15611](https://arxiv.org/abs/2603.15611)
- Goodharting / reward hacking: 11 evaluation failure modes in 4 classes (judge bias, harness/metric failures, ground-truth errors, reward hacking); a 100% pass rate concealed about 68% true capability because agents read cached answer keys — [arXiv 2609.02246](https://arxiv.org/abs/2609.02246)
- Drift in self-judging loops: length increases without explicit length control — [arXiv 2407.19594](https://arxiv.org/abs/2407.19594)
- Criteria drift — [arXiv 2404.12272](https://arxiv.org/abs/2404.12272)
- Label-free rubric repair optimises judge consensus, not human alignment — [arXiv 2610.13303](https://arxiv.org/abs/2610.13303)
- Memory compounding of judge errors (Echo Gap) — [arXiv 2608.00017](https://arxiv.org/abs/2608.00017)
- Diversity collapse of RL attackers — [arXiv 2202.03286](https://arxiv.org/abs/2202.03286); motivating curiosity rewards — [arXiv 2402.19464](https://arxiv.org/abs/2402.19464)
- Self-bias: LLM-generated benchmarks favour the generator model (from question domain, style and wrong labels); mixing generators suppresses it (paper known only from a search summary; title unverified) — [arXiv 2505.20738](https://arxiv.org/abs/2505.20738)
- Leakage and contamination are the motivation for refreshed benchmarks: LiveBench (new questions from recent sources, ground-truth scoring without LLM judges) — [arXiv 2406.19314](https://arxiv.org/abs/2406.19314); LiveCodeBench (time-stamped problems for contamination windows) — [arXiv 2403.07974](https://arxiv.org/abs/2403.07974); LatestEval — [arXiv 2312.12343](https://arxiv.org/abs/2312.12343); DyVal graph-generated samples — [arXiv 2309.17167](https://arxiv.org/abs/2309.17167)
- Cost: ATA runs in 20-30 minutes vs. days for human annotation rounds — [arXiv 2508.17393](https://arxiv.org/abs/2508.17393); LWE's selective variant exists to cut the cost of updating on every case — [arXiv 2512.06751](https://arxiv.org/abs/2512.06751); the rubric study used 129,770 judge requests — [arXiv 2610.13303](https://arxiv.org/abs/2610.13303)

### Inferences
- Leakage of generated tests into training is a stated risk for any evolving test set reused for fine-tuning (Rainbow Teaming, AutoDetect and MART all fine-tune the target on the tests they found), which makes the next round's scores on the same tests uninformative. A held-out, never-trained-on slice is the obvious control.
- Role separation (Code-A1), frozen holdouts and canaries (PROCTOR), and error-independent correction signals (2608.00017) are the three structural defences found.

### Gaps
- No quantitative study found of how fast an evolving judge drifts away from humans as a function of rounds.
- No measurement found of cost per useful (valid, failure-revealing) generated test for agent targets.

## Q4. Closest existing work to: a judge agent pointed at one target agent, talking to it over a channel, keeping a test set, scoring it, and refining the tests each round from where its tests missed or misjudged

### Takeaway
No paper does all of it. The closest five each cover two or three parts. None keeps a persistent test set that it repairs because the judge itself misjudged (as opposed to because the target passed).

### Cited Findings (the five closest, with exact differences)
1. Agent-Testing Agent (2508.17393, Aug 2025) — closest overall: a meta-agent pointed at one conversational agent, talks to it over its interface, scores with an LLM-judge rubric, adapts later tests toward weak capabilities — [arXiv 2508.17393](https://arxiv.org/abs/2508.17393). Differs: refinement is driven by the target's low scores (where the target failed), not by where the judge's tests missed or misjudged; the rubric is fixed during the loop; no persistent test set carried across target versions is described.
2. ALI-Agent (2405.14125, May 2024): keeps a memory of test records, refines each scenario over several rounds against one target until it reveals misalignment — [arXiv 2405.14125](https://arxiv.org/abs/2405.14125). Differs: the target is a single-turn LLM, not an agent over a channel; refinement aims to make tests harder, not to correct judge errors; the evaluator is fixed; values/safety domain only.
3. Online Agent-as-a-Judge (2606.08200, Jun 2026): judge agent talks to the target through the environment's own dialogue and action interface and creates situations tied to criteria — [arXiv 2606.08200](https://arxiv.org/abs/2606.08200). Differs: criteria are designer-authored and fixed; no round-over-round refinement of a test set is described in the abstract; one life-simulation environment.
4. AutoDetect (2406.16714, Jun 2024): Examiner, Questioner and Assessor iterate on one target, generating new questions from found weaknesses — [arXiv 2406.16714](https://arxiv.org/abs/2406.16714). Differs: target is an LLM answering questions, not an agent; the Assessor is fixed; the loop has no notion of the judge's own misjudgments.
5. Learning While Evaluating / Selective LWE (2512.06751, Dec 2025): the judge refines its own evaluation instructions across a stream of cases, updating when it is self-inconsistent — [arXiv 2512.06751](https://arxiv.org/abs/2512.06751). Differs: it is the judge-repair half only; no tests are generated, no target is interacted with, pairwise preference judging only, and "misjudged" is self-inconsistency, not disagreement with an oracle.

Runners-up: Automated Capability Discovery (open-ended task generation against one subject model, scored by the scientist model) — [arXiv 2502.07577](https://arxiv.org/abs/2502.07577); Evaluation Agent (multi-round adaptive probing of one generative model) — [arXiv 2412.09645](https://arxiv.org/abs/2412.09645); EvalGen (human-in-the-loop repair of the judge's criteria from grading disagreement) — [arXiv 2404.12272](https://arxiv.org/abs/2404.12272); Agent-as-a-Judge (agentic judge with tools inspecting an agent's workspace, about 90% agreement with human consensus vs. about 70% for LLM-as-a-judge, but fixed requirements and no rounds) — [arXiv 2410.10934](https://arxiv.org/abs/2410.10934); Code-A1 (separate tester with a Mistake Book of past failures; code only) — [arXiv 2603.15611](https://arxiv.org/abs/2603.15611).

### Inferences
- The unbuilt combination is: ATA-style targeted, channel-based testing of one agent, plus an EvalGen/LWE-style repair of the judge triggered by measured misjudgments, plus PROCTOR-style frozen holdouts and canaries so the loop cannot drift into the consensus-without-alignment trap shown in 2610.13303.
- "Where the tests missed" has two distinct meanings that the literature keeps separate: (a) the target passed a test it should have been probed harder on (test-side miss, the red-teaming line), and (b) the judge's verdict disagreed with an oracle (judge-side miss, the self-improving-judge line). A design that names both signals separately would be new.

### Gaps
- I could not read the full texts of ATA, Online Agent-as-a-Judge, LWE or SEMJ; whether any keeps a persistent cross-round test set is inferred from abstracts only.
- Search may have missed 2026 workshop papers; the area is growing quickly (many 2026 rubric-evolution and self-evolving-agent benchmarks: 2605.24426 SEAL, 2608.00155 AgentStream, 2607.05202 EvoAgentBench, none read).
