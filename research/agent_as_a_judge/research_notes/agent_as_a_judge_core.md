# Agent-as-a-Judge: the original paper, its descendants, its critics (through Oct 2026)

Per-paper notes are in `research/agent_as_a_judge/notes/`. Notes this researcher wrote or extended: 2024-10 Agent-as-a-Judge (extended), 2026-01 A Survey on Agent-as-a-Judge, 2026-04 AJ-Bench, 2025-06 Mind2Web 2, 2026-10 AgentHorizon, 2026-01 Gaming the Judge, 2026-09 trajectory-judge, 2025-04 AgentRewardBench (extended), 2025-08 Auto-Eval Judge, 2026-05 An Empirical Study of Automating Agent Evaluation, 2026-08 Benchmarking LLM Judges for Mobile Agent Evaluation (extended), 2026-08 AgentJudgeBench, plus short notes: When AIs Judge AIs, VAGEN, Agentic Rubrics, CodeVisionary, FinResearchBench, NarrativeFactScore, Sentient Agent as a Judge, AI Agents-as-Judge Enterprise Documents, MAJ-Eval, ARM-Thinker, DREAM, Scaling Agentic Verifier for Competitive Coding, GAUGE, BabelJudge, Model or Harness, EvalAgent Implicit Criteria, Evaluation Agent visual. Five of my notes duplicated ones that other researchers had written moments earlier (Online-Mind2Web, Who&When, TIR-Judge, AgentV-RL, MobileJudgeBench). I deleted my copies and added my facts to theirs.

## Q1. What does the original Agent-as-a-Judge do, which modules were ablated, what were the numbers, and what limitations did the authors admit?

### Takeaway
Agent-as-a-Judge (Zhuge et al., arXiv 2410.10934, Oct 2024, ICML 2025) is a GPT-4o judge built from five kept modules: graph, locate, read, retrieve, ask. It checks each requirement of a DevAI task against the developer agent's workspace, and in the gray-box setting also against its trajectory. It agrees with a 3-human consensus about 90% of the time, against about 60-84% for LLM-as-a-Judge. It costs about 2.3% of human evaluation. Memory and planning were dropped as harmful or unstable, and search was dropped as useless. The judge never executes the code and never questions the agent it is judging.

### Cited Findings
- **Modules.** Eight modules were proposed: graph, locate, read (multimodal), search, retrieve, ask, memory, planning. The final configuration is graph+locate+read+retrieve+ask. The other three were dropped for these reasons, with no numbers reported:
  - memory "proved detrimental" because early errors cascade;
  - planning was "unstable";
  - search did not help on workspaces of only hundreds of lines.
  — [arXiv HTML 2410.10934](https://arxiv.org/html/2410.10934)
- **Incremental ablation on OpenHands** (alignment with human consensus): ask alone 65.03%, +graph 75.95%, +read 82.24%, +locate 90.44%, +retrieve 90.16%. Retrieve brought no gain on OpenHands. — [arXiv HTML](https://arxiv.org/html/2410.10934)
- **DevAI** has 55 tasks, 365 hierarchical requirements forming a DAG, and 125 preferences. The developer agents were MetaGPT, GPT-Pilot and OpenHands, running on gpt-4o-2024-05-13 with a 1,800 s limit. As judged by humans:
  - requirements met: 22.13%, 44.80%, 42.89%;
  - task solve rates: 0%, 1.81%, 1.81% (one task solved in total).
  — [arXiv HTML](https://arxiv.org/html/2410.10934)
- **Alignment with human consensus** (MetaGPT / GPT-Pilot / OpenHands):

  | Judge | Setting | MetaGPT | GPT-Pilot | OpenHands |
  |---|---|---|---|---|
  | Agent-as-a-Judge | gray-box | 92.07% | 86.61% | 90.16% |
  | Agent-as-a-Judge | black-box | 88.52% | 83.88% | 90.44% |
  | LLM-as-a-Judge | gray-box | 68.86% | 71.85% | 70.76% |
  | LLM-as-a-Judge | black-box | 84.15% | 65.30% | 60.38% |

  Individual humans scored 84.88-89.34%. A majority vote of the 3 humans scored 93.98-95.08%. — [arXiv HTML](https://arxiv.org/html/2410.10934)
- **Cost and time:**

  | Evaluator | Cost | Time |
  |---|---|---|
  | Humans | ~$1,297.50 | ~86.5 h |
  | Agent-as-a-Judge | $30.58 | 118.43 min |
  | LLM-as-a-Judge | $29.63 | 10.99 min |

  The 97.64% / 97.72% savings figures are given inconsistently between the introduction and Section 4.4. — [arXiv HTML](https://arxiv.org/html/2410.10934)
- **Limitations the authors admit:**
  - it is a proof of concept;
  - tasks are small and workspaces are hundreds of lines;
  - the human consensus "may not represent the absolute ground truth", and humans disagreed with each other 10-30% of the time;
  - gray-box trajectories are "nearly inaccessible in practical situations";
  - class imbalance makes the alignment rate misleading, so PR curves are reported as well;
  - a larger expert panel would have been better but was too costly.
  — [arXiv HTML](https://arxiv.org/html/2410.10934)
- The paper was published at ICML 2025 (PMLR v267). — [PMLR](https://proceedings.mlr.press/v267/zhuge25a.html); [ICML poster](https://icml.cc/virtual/2025/poster/45485)

### Inferences
- Measured against an LLM judge, the cost advantage disappears. Agent-as-a-Judge costs about the same in dollars ($30.58 vs $29.63) and takes about 11x longer. The headline "97% savings" is a comparison with humans only.
- Agent-as-a-Judge counted 5.45% of GPT-Pilot's tasks as solved where humans counted 1.81%. The judge appears more lenient on whole-task success than on single requirements.
- The study used one backbone, three agents and three humans, and reported no run-to-run variance. Robustness to the choice of backbone and to repeated runs was never tested.
- The judge "verifies" only by reading files. It does not run the code, does not use tests, and does not interact with the agent. Each of these is an obvious axis left untried.

### Gaps
- No numeric ablations were published for memory, planning or search. The "harmful" verdicts are qualitative.
- I found no independent replication of DevAI's human-agreement numbers with a different judge backbone or with more annotators.

## Q2. Which later papers extend it: new domains, trajectory-level judging, interactive judges, judges with tools or sandboxes?

### Takeaway
The extensions fall into four families:
- **Rubric-tree judges for agentic search.** Mind2Web 2 is the best example.
- **Environment-aware tool-using judges.** AJ-Bench, VAGEN and AgentHorizon's harness judges inspect the live state.
- **Trajectory and step-level judges.** Auto-Eval Judge and trajectory-judge check each step, and Who&When attributes failures to an agent and step.
- **Trained tool-using judges and verifiers.** TIR-Judge, ARM-Thinker, AgentV-RL and Agentic Rubrics.

Few of these judges interact with the agent under test. The exceptions are social and dialogue judges such as Sentient Agent as a Judge.

### Cited Findings
- **Mind2Web 2** (2506.21506, Jun 2025, NeurIPS 2025): 130 agentic-search tasks, each with a task-specific judge script.
  - The rubric tree averages ~50 nodes (max 603, depth up to 6), with critical, non-critical and sequential nodes aggregated by gate-then-average.
  - An Extractor tool and a Verifier tool check claims against the cited page's text and screenshot. The judge LLM is o4-mini; scripts were drafted by Claude-3.7-Sonnet and reviewed by humans.
  - Reported verifier correctness is 99.03%. Of 35 human-judge discrepancies, 27 were human errors.
  - Admitted limitations: cited pages are assumed truthful, hidden content may be unreachable, live sites drift, and 120 of the 130 tasks are private.
  - The best agent, OpenAI Deep Research, reaches 50-70% of human performance.
  — [arXiv abs](https://arxiv.org/abs/2506.21506); [HTML](https://arxiv.org/html/2506.21506v2)
- **AJ-Bench** (2604.18240, Apr 2026, ACL 2026 Findings): 155 tasks, 516 trajectories, 60 tools, across three domains: Search (Mind2Web2, WideSearch), data systems (filesystem and Postgres from MCPMark) and GUI (Office apps from OSWorld). Judges inspect environment state through MCP tools.
  - Tool use adds about 13 F1 points: gpt-5-mini 59.00 → 72.41, deepseek-v3.2 64.49 → 77.34. Average agent-judge F1 is about 0.72.
  - More reasoning effort does not reliably help. More interaction turns do help.
  - Failure modes: missing tool calls, wrong tools, misreading tool output (the most common), and correct evidence followed by wrong reasoning.
  — [arXiv HTML](https://arxiv.org/html/2604.18240); [ACL Anthology](https://aclanthology.org/2026.findings-acl.1269/)
- **AgentHorizon** (2610.11050, Oct 2026): 1,373 human-recorded computer-use trajectories in success/near-miss pairs. The agentic judges are LLMs inside the Codex, Claude Code, Gemini CLI, OpenCode and OpenHands harnesses.
  - Best balanced accuracy is 80.9% (GPT-5.5 + Codex). GPT-5.5 scores 68.6% as a direct judge.
  - Qwen 3.6 27B scores 77.6% as a direct judge but 70.4% as an agentic judge.
  - Recall on Bad Side Effects is at most 24.1%.
  - Cost is $0.10-0.66 per trajectory.
  — [arXiv HTML](https://arxiv.org/html/2610.11050v1)
- **VAGEN** (2602.00575, Jan 2026): a GUI verifier agent. It first extracts evidence from the trajectory, then actively probes the live environment for latent state, moving from cheap to expensive checks. Tested on OSWorld-Verified and AndroidWorld. The abstract gives no numbers. — [arXiv abs](https://arxiv.org/abs/2602.00575)
- **Auto-Eval Judge** (2508.05508, Aug 2025): a modular judge that decomposes the task and checks each step of the trajectory. Against a GPT-4o LLM judge it adds +4.76% human alignment on GAIA and +10.52% on BigCodeBench. The actor was Magentic-One only. — [arXiv abs](https://arxiv.org/abs/2508.05508)
- **Agentic Rubrics** (2601.04171, Jan 2026): an agent explores the repository, writes a rubric grounded in that codebase, and scores SWE patches without executing tests. It reaches 54.2% on SWE-Bench Verified best-of-N (Qwen3-Coder-30B-A3B), at least 3.5 points above the baselines. — [arXiv abs](https://arxiv.org/abs/2601.04171)
- **TIR-Judge** (2510.23038, ICLR 2026): an 8B judge trained with RL to call a code executor. It gains up to +6.4% pointwise and +7.7% pairwise. — [arXiv abs](https://arxiv.org/abs/2510.23038)
- **CodeVisionary** (2504.13472, ASE 2025): an agent judge for code. Its correlation with humans is +0.217 Pearson over the best baseline on 363 samples. — [arXiv abs](https://arxiv.org/abs/2504.13472)
- **FinResearchBench** (2507.16248, ICAIF 2025): a logic-tree Agent-as-a-Judge for financial research agents, with 70 questions. — [arXiv abs](https://arxiv.org/abs/2507.16248)
- **Who&When** (2505.00212, ICML 2025): failure attribution in multi-agent systems. The best method is 53.5% accurate at the agent level and 14.2% at the step level. — [arXiv abs](https://arxiv.org/abs/2505.00212)
- **EvalAgent** (2605.11378, AWS, May/Sep 2026): a coding agent that writes the whole evaluation (criteria, code, report) from the agent's source and traces, and sets itself against Agent-as-a-Judge.
  - Experts preferred it 79.5% of the time.
  - Its first-run executability (Eval@1) is about 65%.
  - The agentic meta-judge reached 76.3% three-way agreement across three runs.
  — [arXiv HTML](https://arxiv.org/html/2605.11378)
- **Other domain applications** listed in the Awesome-Agent-as-a-Judge repo: NarrativeFactScore (2501.09993), enterprise documents (2506.22485), Sentient Agent as a Judge (2505.02847, a judge that converses with the model under test), MAJ-Eval (2507.21028), DREAM for deep research (2602.18940), AgentV-RL (2604.16004), Scaling Agentic Verifier for Competitive Coding (2602.04254), ARM-Thinker (2512.05111). — [Awesome-Agent-as-a-Judge](https://github.com/ModalityDance/Awesome-Agent-as-a-Judge)

### Inferences
- The richest descendants keep the original's per-requirement decomposition (rubric trees, logic trees, checklists) and replace "read the workspace" with domain tools: page fetch and screenshots in Mind2Web 2, MCP/DB/GUI state in AJ-Bench, live probing in VAGEN.
- None of the descendants I found makes the judge run new tests against the artifact, i.e. generate and execute adversarial checks. None interrogates the developer agent about its claims. Agentic Rubrics explicitly avoids execution.
- Per-task judge construction does not scale: Mind2Web 2 required over 1,000 human hours plus per-script review. Automatic judge or rubric synthesis that does not need human review is still open.

### Gaps
- Exact numbers were not verified for VAGEN, DREAM, ARM-Thinker, AgentV-RL, NarrativeFactScore or MAJ-Eval; I read their abstracts or listing entries only.
- I found no DevAI-specific follow-up that runs code in a sandbox. AJ-Bench is the nearest equivalent.
- "Model or Harness?" (2607.28802) and DAREBench (2609.06059) appeared in search results only and were not read.

## Q3. Which papers criticise or measure the weaknesses of agentic and trajectory judges?

### Takeaway
The criticism so far is mostly empirical.
- **Gaming.** Judges that read trajectories can be gamed by the agent's own narrated reasoning (up to +90% false positives).
- **Tools.** Tools help some models and hurt others, and the harness alone moves accuracy by several points.
- **Side effects.** Judges largely miss side effects (recall ≤24%).
- **Silent faults.** Judges that see only outcomes cannot see faults that leave the reply unchanged.
- **Hard ceiling.** Judge accuracy plateaus at 77-82% on hard tool-calling cases regardless of size.
- **Rankings.** Choice of judge reshuffles agent rankings by up to 13 places.

I found no paper that directly measures self-preference or run-to-run variance for Agent-as-a-Judge itself.

### Cited Findings
- **Gaming the Judge** (2601.14691, Jan 2026): rewrites only the CoT of 800 web-agent trajectories, leaving actions and screenshots unchanged.
  - False positive rate rises by up to 90%.
  - Progress Fabrication adds 20-30 FPR points on GPT-4o and GLM-4.1V. Qwen-2.5-72B and GLM-4.1V exceed 50% absolute FPR.
  - Prompting, voting and extended thinking reduce the effect but do not remove it, and each costs recall.
  - The authors suggest grounding claims against observations, but do not test it.
  — [arXiv HTML](https://arxiv.org/html/2601.14691)
- **AgentHorizon** (2610.11050):
  - Tools do not help consistently: Qwen 3.6 27B scores 77.6% direct vs 70.4% agentic.
  - Swapping the harness shifts accuracy by about 3.7 points.
  - Bad-side-effect recall is at most 24.1%.
  - Without the instruction, Qwen called 98.9% of trajectories successful.
  - Judges also reject valid work over trivial deviations.
  — [arXiv HTML](https://arxiv.org/html/2610.11050v1)
- **trajectory-judge** (2609.00038, Sep 2026):
  - The outcome-only judge has zero paired discrimination on faults that leave the reply unchanged. The step judge reaches +1.00.
  - Raw recall overstates detection: an 8B judge flags 397 of 400 trajectories.
  - A 3-sample majority vote triples the cost with no gain.
  — [arXiv HTML](https://arxiv.org/html/2609.00038v2)
- **MobileJudgeBench** (2608.11434, Aug 2026):
  - Judges misclassify 9-24% of mobile trajectories. The backbone shifts a judge by 5.6-10.5 points, and rankings shift by up to 13 positions.
  - GPT judges anchor on the last frame. Qwen judges accept partial completion.
  - RL with judge rewards underperforms RL with a rule reward (≤45.4% vs 54.6%).
  — [arXiv HTML](https://arxiv.org/html/2608.11434v1)
- **AgentJudgeBench** (2608.26623, Aug 2026, EMNLP 2026):
  - On hard queries without ground truth, all six judges fall in a 77-82% band regardless of scale.
  - Giving ground truth can lower alignment (by 1.5-3.9 points) through over-anchoring.
  - CoT and temperature have negligible effect.
  — [arXiv abs](https://arxiv.org/abs/2608.26623)
- **AgentRewardBench** (2504.08942): 12 LLM judges on 1,302 web trajectories. No judge excels across all benchmarks, and rule-based checks under-report success. — [arXiv abs](https://arxiv.org/abs/2504.08942). The figure "no judge above 70% precision" appears in a search summary. The best judge's precision is 69.8%, per another researcher's note in `notes/2025-04 AgentRewardBench.md`.
- **AJ-Bench** reports one judge whose reasoning concluded FAIL while its output said PASS. The most common failure is misreading tool outputs. — [arXiv HTML](https://arxiv.org/html/2604.18240)
- **EvalAgent study** (2605.11378) on unconstrained agentic evaluators:
  - they over-engineer, writing 2.4-6.6x more code;
  - 35-75% fall back to keyword heuristics;
  - plans and code drift apart;
  - the agentic meta-judge is non-deterministic, with 76.3% three-run agreement.
  — [arXiv HTML](https://arxiv.org/html/2605.11378)
- **GAUGE** (2609.12191, EMNLP 2026 Industry): in user-simulated evaluation, judge-rated satisfaction carries essentially no information about task success. 57.5% of conversations rated satisfied failed the task, and judges disagree 31% of the time on close pairs. — [arXiv abs](https://arxiv.org/abs/2609.12191). A secondary search summary also claimed GAUGE measured self-preference of an Anthropic judge for Claude agents. It is not in the abstract and is **unverified**.
- **Cost.** Practitioner sources say an agent evaluator can cost more per record than the run it evaluates. This is a blog claim, not a paper. — [search summary of Arize/LangChain blogs](https://arize.com/glossary/agents-that-evaluate-agents/)

### Inferences
- The judged agent's narration is an attack surface, and the gray-box mode of the original paper is most exposed to it. A judge that ignores CoT and verifies claims against environment state is suggested but untested (Gaming the Judge).
- Side effects (actions nobody asked for) are the clearest blind spot of current judges, agentic or not. Diffing environment state before and after the run is an untried remedy in these papers.
- Tool access is not a free win. It depends on the model and the harness (AJ-Bench +13 vs AgentHorizon mixed). Tool-use errors, such as misreading outputs, become a new failure class.

### Gaps
- I found no study measuring the run-to-run variance of an Agent-as-a-Judge verdict on DevAI.
- I found no study of self-preference where the judge agent shares a backbone with the agent under test. Only the unverified GAUGE claim exists.
- I found no adversarial study in which the judged agent deliberately shapes its workspace (rather than its CoT) to fool a tool-using judge.

## Q4. Are there surveys (2025-2026) that cover agent-as-a-judge as a category, and what taxonomy and open problems do they list?

### Takeaway
There are two surveys. **"A Survey on Agent-as-a-Judge"** (You, Cai et al., 2601.05111, Jan 2026) is the main one. It classifies judges by stage (procedural, reactive, self-evolving) and by capability (multi-agent collaboration, planning, tool integration, memory/personalisation, optimisation). It lists cost, latency, safety and privacy as challenges. **"When AIs Judge AIs"** (Yu, 2508.02994, Aug 2025) is a shorter review. It names bias, robustness and meta-evaluation as open problems.

### Cited Findings
- **2601.05111 stages:**
  - Procedural: fixed workflows (ChatEval, M-MAD, GEMA-Score, CAFES).
  - Reactive: adaptive routing and tool calls in a fixed decision space (Evaluation Agent, AGENT-X, MAJ-Eval, Agentic Reward Modeling).
  - Self-evolving: online rubric and memory updates (EvalAgent 2504.15219).
  — [arXiv HTML 2601.05111](https://arxiv.org/html/2601.05111v1)
- **2601.05111 capability axes:**
  - collaboration: consensus vs decomposition;
  - planning: orchestration vs rubric discovery;
  - tools: evidence collection (Agent-as-a-Judge, CodeVisionary, ARM-Thinker) vs correctness verification (HERMES, VerifiAgent, Agentic RM);
  - memory and personalisation;
  - optimisation: training-time (TIR-Judge, ARM-Thinker) vs inference-time.
  — [arXiv HTML](https://arxiv.org/html/2601.05111v1)
- **2601.05111 challenges:**
  - cost: RL training on long tool trajectories, multi-step inference;
  - latency, which clashes with RL reward loops;
  - safety: prompt injection and tool misuse, errors propagating across agents, judge bias reinforced when the judge serves as a reward;
  - privacy of memory.
- **2601.05111 future directions:** proactive personalisation, on-the-fly rubric generation, adaptive granularity, judges that probe the environment and escalate edge cases, human-agent collaborative calibration, RL-internalised planning and tool use, jointly trained multi-agent judges.
- **2601.05111 self-critique:** there is no consensus definition of an "evaluation agent", and many included systems are prompt role-play.

  — [arXiv HTML](https://arxiv.org/html/2601.05111v1)
- **Survey companion list:** the GitHub repository Awesome-Agent-as-a-Judge (~106 entries). — [GitHub](https://github.com/ModalityDance/Awesome-Agent-as-a-Judge)
- **2508.02994:** a single-author review covering the move from single-model judges to multi-agent debate, and deployments in medicine, law, finance and education. It names bias, robustness and meta-evaluation as open problems and argues that agent judges should complement human oversight. — [arXiv abs](https://arxiv.org/abs/2508.02994)
- **2508.07407**, a survey of self-evolving agents, describes the agent judge as evaluating whole trajectories and cites DevAI. — [arXiv PDF](https://arxiv.org/pdf/2508.07407)
- **2510.24367**, a survey of LLM-as-a-Judge for software engineering, places Agent-as-a-Judge among pointwise code evaluators. — [search summary, arXiv PDF](https://arxiv.org/pdf/2510.24367)

### Inferences
- The 2601.05111 taxonomy is organised by how a judge is built. It has no axis for **what evidence the judge trusts**: narration vs artifacts vs live environment state. It also has no axis for **adversarial robustness to the judged agent**. The 2026 empirical papers (Gaming the Judge, AgentHorizon, trajectory-judge) show that evidence source is what decides failure. A taxonomy built on evidence source and adversarial robustness is missing.
- Both surveys omit non-determinism and variance across runs.

### Gaps
- I did not read the full text of 2508.02994, so its detailed taxonomy, if any, is not captured.
- Other researchers' notes exist for nearby work I did not verify myself: JEV-as-a-Judge (2026-09), OSReward (2026-07), AgentPRM (2025-11), Autonomous Evaluation and Refinement of Digital Agents (2024-04), Web-Shepherd (2025-05). Check `notes/` for their details.
