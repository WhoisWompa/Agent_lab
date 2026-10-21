# Orchestrator-worker, planner-executor and hierarchical-delegation LLM systems (2023 to October 2026), read as incentive-and-information systems

Scope note: only systems where one agent decomposes and delegates to others and receives their results. Role-based teams (MetaGPT, ChatDev), generator-critic loops, debate, topology optimisation, failure surveys and production frameworks are covered by other researchers; they appear here only as pointers. All PDFs listed below were downloaded to `C:\Users\lione\agents\research\multiagent_llm_systems\pdfs\<arxiv-id>.pdf` (all 30 downloads succeeded and begin with `%PDF-`; none were opened). Status labels: **preprint** = arXiv only as far as verified; **published** = venue stated in the arXiv comment field or the proceedings page; **blog/docs** = no PDF.

## Q0. What is each system's structure (roles, information flow, acceptance rule, plan/judge split, code vs prompt, failures, results)?

### Takeaway
Across ~30 systems the dominant pattern is an LLM orchestrator that both plans and judges, receives a worker-written summary or final message (not the full trace), and accepts on the worker's self-report (DONE/FAIL, "task complete") plus a fixed iteration/stall budget enforced in code. A minority (TaskWeaver, Magentic-One's terminal, OS-Copilot's critic, HTN-Orchestrate, VMAO, AgentFlow, Agent S3's judge) add a check or a separate judging agent, and only TaskWeaver's AST rule check and execution return codes are non-LLM verification.

### Cited Findings

#### Index table (identity, status, PDF)

| System | Authors (first) / org | Year | Status / venue | arXiv | PDF |
|---|---|---|---|---|---|
| HuggingGPT | Shen, Song, Tan, Li, Lu, Zhuang (Zhejiang U. / MSRA) | 2023 | preprint on arXiv page (v4 Dec 2023); widely cited as NeurIPS 2023, not confirmed from arXiv page | 2303.17580 | https://arxiv.org/pdf/2303.17580 |
| Plan-and-Solve prompting | Lei Wang, Wanyu Xu, Yihuai Lan, Zhiqiang Hu, Yunshi Lan | 2023 | published, ACL 2023 | 2305.04091 | https://arxiv.org/pdf/2305.04091 |
| AutoGen | Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran Wu, Beibin Li et al. (Microsoft) | 2023 | preprint on arXiv page (venue not stated there) | 2308.08155 | https://arxiv.org/pdf/2308.08155 |
| ADaPT | Archiki Prasad, Alexander Koller, Mareike Hartmann, Peter Clark, Ashish Sabharwal et al. (AI2 / UNC) | 2023 | published, NAACL 2024 Findings | 2311.05772 | https://arxiv.org/pdf/2311.05772 |
| TaskWeaver | Bo Qiao, Liqun Li, Xu Zhang, Shilin He et al. (Microsoft) | 2023 | preprint | 2311.17541 | https://arxiv.org/pdf/2311.17541 |
| OS-Copilot / FRIDAY | Zhiyong Wu, Chengcheng Han, Zichen Ding, Zhenmin Weng, Zhoumianze Liu et al. | 2024 | preprint | 2402.07456 | https://arxiv.org/pdf/2402.07456 |
| TDAG | Yaoxiang Wang, Zhiyong Wu, Junfeng Yao, Jinsong Su | 2024 | published, Neural Networks (journal) | 2402.10178 | https://arxiv.org/pdf/2402.10178 |
| Mixture-of-Agents | Junlin Wang, Jue Wang, Ben Athiwaratkun, Ce Zhang, James Zou (Together AI / Duke / Stanford) | 2024 | preprint on arXiv page; venue not stated there | 2406.04692 | https://arxiv.org/pdf/2406.04692 |
| Agent-Oriented Planning (AOP) | Ao Li, Yuexiang Xie, Songze Li, Fugee Tsung, Bolin Ding, Yaliang Li | 2024 | published, ICLR 2025 | 2410.02189 | https://arxiv.org/pdf/2410.02189 |
| Agent S | Saaket Agashe, Jiuzhou Han, Shuyu Gan, Jiachen Yang, Ang Li, Xin Eric Wang (Simular) | 2024 | preprint on arXiv page | 2410.08164 | https://arxiv.org/pdf/2410.08164 |
| Magentic-One | Adam Fourney, Gagan Bansal, Hussein Mozannar, Cheng Tan et al. (Microsoft Research AI Frontiers) | 2024 | preprint | 2411.04468 | https://arxiv.org/pdf/2411.04468 |
| Anthropic "Building effective agents" (orchestrator-workers pattern) | Erik Schluntz, Barry Zhang | Dec 2024 | blog | none | https://www.anthropic.com/engineering/building-effective-agents |
| OpenAI Swarm | OpenAI | 2024 | GitHub repo, "experimental, educational", superseded | none | https://github.com/openai/swarm |
| OpenAI Agents SDK handoffs / agents-as-tools | OpenAI | 2025 | docs | none | https://openai.github.io/openai-agents-python/handoffs/ ; https://openai.github.io/openai-agents-python/multi_agent/ |
| TalkHier | Zhao Wang, Sota Moriyama, Wei-Yao Wang, Briti Gangopadhyay, Shingo Takamatsu (Sony) | 2025 | preprint | 2502.11098 | https://arxiv.org/pdf/2502.11098 |
| Plan-and-Act | Lutfi Eren Erdogan, Nicholas Lee, Sehoon Kim, Suhong Moon, Hiroki Furuta, Gopala Anumanchipalli et al. (UC Berkeley) | 2025 | preprint on arXiv page (v3) | 2503.09572 | https://arxiv.org/pdf/2503.09572 |
| Agent S2 | Saaket Agashe, Kyle Wong, Vincent Tu, Jiachen Yang, Ang Li, Xin Eric Wang (Simular) | 2025 | preprint | 2504.00906 | https://arxiv.org/pdf/2504.00906 |
| HALO | Zhipeng Hou, Junyi Tang, Yipeng Wang | 2025 | preprint | 2505.13516 | https://arxiv.org/pdf/2505.13516 |
| Puppeteer (Evolving Orchestration) | Yufan Dang, Chen Qian, Xueheng Luo, Jingru Fan, Zihao Xie, Ruijie Shi et al. (Tsinghua / OpenBMB) | 2025 | published, NeurIPS 2025 | 2505.19591 | https://arxiv.org/pdf/2505.19591 |
| OWL / Workforce (CAMEL) | Mengkang Hu, Yuhang Zhou, Wendong Fan, Yuzhou Nie, Bowei Xia, Tao Sun et al. | 2025 | preprint | 2505.23885 | https://arxiv.org/pdf/2505.23885 |
| AgentOrchestra (TEA protocol) | Wentao Zhang, Liang Zeng, Yuzhen Xiao, Yongcong Li, Ce Cui, Yilei Zhao et al. (Skywork) | 2025 | preprint (v6) | 2506.12508 | https://arxiv.org/pdf/2506.12508 |
| Anthropic multi-agent research system | Jeremy Hadfield, Barry Zhang, Kenneth Lien, Florian Scholz, Jeremy Fox, Daniel Ford | 13 Jun 2025 | blog; no paper form found | none | https://www.anthropic.com/engineering/multi-agent-research-system |
| Cognition "Don't Build Multi-Agents" (critique) | Walden Yan | 12 Jun 2025 | blog | none | https://cognition.com/blog/dont-build-multi-agents |
| Magentic-UI | Hussein Mozannar, Gagan Bansal, Cheng Tan, Adam Fourney, Victor Dibia et al. (Microsoft) | 2025 | preprint | 2507.22358 | https://arxiv.org/pdf/2507.22358 |
| Tree of Agents (TOA) | Song Yu, Xiaofei Xu, Ke Deng, Li Li, Lin Tian | 2025 | published, Findings of EMNLP 2025 | 2509.06436 | https://arxiv.org/pdf/2509.06436 |
| Agent S3 / Behavior Best-of-N ("Scaling Agents for Computer Use") | Gonzalo Gonzalez-Pumariega, Vincent Tu, Chih-Lun Lee, Jiachen Yang, Ang Li, Xin Eric Wang | 2025 | preprint (v2) | 2510.02250 | https://arxiv.org/pdf/2510.02250 |
| AgentFlow (Flow-GRPO) | Zhuofeng Li, Haoxiang Zhang, Seungju Han, Sheng Liu, Jianwen Xie, Yu Zhang et al. (Stanford) | 2025 | published, ICLR 2026 Oral | 2510.05592 | https://arxiv.org/pdf/2510.05592 |
| Claude Code subagents | Anthropic | 2025-2026 | docs | none | https://code.claude.com/docs/en/sub-agents |
| Towards a Science of Scaling Agent Systems (centralized vs others) | Yubin Kim, Ken Gu, Chanwoo Park, ... Xin Liu (Google Research, Google DeepMind, MIT) | Dec 2025 | preprint (v3) | 2512.08296 | https://arxiv.org/pdf/2512.08296 |
| Kimi K2.5 Agent Swarm (PARL-trained orchestrator) | Moonshot AI | Jan 2026 | vendor blog; tech report not located | none | https://www.kimi.com/blog/kimi-k2-5 |
| Intelligent AI Delegation (framework) | Nenad Tomašev, Matija Franklin, Simon Osindero (Google DeepMind) | Feb 2026 | preprint | 2602.11865 | https://arxiv.org/pdf/2602.11865 |
| VMAO (Verified Multi-Agent Orchestration) | Xing Zhang, Yanwei Cui, Guanghui Wang, Wei Qiu, Ziyuan Li, Fangwei Han et al. (AWS GenAI Innovation Center, HSBC) | Mar 2026 | workshop, ICLR 2026 MALGAI | 2603.11445 | https://arxiv.org/pdf/2603.11445 |
| Recognize Your Orchestrator (entropy dynamics, "Reasoning Trap") | Junze Zhu, Weihao Chen, Xuanwang Zhang, Zhen Wu, Xinyu Dai | May 2026 | preprint | 2606.01351 | https://arxiv.org/pdf/2606.01351 |
| SwarmBench (LLMs as swarm orchestrators) | Jinshan Gao, Zhuoran Jin, Tianyi Men, Kang Liu, Jun Zhao | Aug 2026 | published, EMNLP 2026 Findings | 2608.30661 | https://arxiv.org/pdf/2608.30661 |
| HTN-Orchestrate | Yanchen Deng, Jianguo Huang, Yao Long Teng, Yixuan Li, Handuo Zhang, Ning Wang et al. | Oct 2026 | preprint (v2) | 2610.22195 | https://arxiv.org/pdf/2610.22195 |

Pointer-only (other researchers' scope) PDFs also downloaded because they bear on Q4: MAST "Why Do Multi-Agent LLM Systems Fail?" (Cemri et al., UC Berkeley, 2503.13657, https://arxiv.org/pdf/2503.13657) and Who&When failure attribution (Zhang, Yin et al., 2505.00212, https://arxiv.org/pdf/2505.00212).

Not covered as a separate system: "Tree of Agents" is long-context chunk-agents, not delegation; listed for completeness — [arXiv 2509.06436](https://arxiv.org/abs/2509.06436).

#### Per-system records

**HuggingGPT (2023)** — [arXiv](https://arxiv.org/abs/2303.17580), [HTML](https://arxiv.org/html/2303.17580)
- Roles: ChatGPT as controller; Hugging Face expert models as workers. Four stages: task planning, model selection (by model function descriptions), task execution, response generation — [arXiv abstract](https://arxiv.org/abs/2303.17580).
- Plan is a JSON list of tasks with `task`, `id`, `dep`, `args`; dependencies use `<resource>-task_id` placeholders substituted at execution time; tasks without dependencies run in parallel (this substitution is code) — [HTML](https://arxiv.org/html/2303.17580).
- Controller sees structured inference results (bounding boxes with probabilities, answer distributions) and is asked to produce "a reliable decision with a confidence level"; no explicit verification step of expert outputs is described — [HTML](https://arxiv.org/html/2303.17580).
- Workers see only their args (no view of the overall task) — inferred from the plan format, same source.
- Results (GPT-3.5): single-task planning F1 54.45, sequential F1 51.92, graph F1 51.91; human eval task-planning passing rate 91.22%, rationality 78.47%; end-to-end success 63.08% — [HTML](https://arxiv.org/html/2303.17580).
- Limitations stated: latency from multiple LLM calls, context length limits on model descriptions, instability (LLM ignores instructions causing workflow exceptions), plans not guaranteed feasible — [HTML](https://arxiv.org/html/2303.17580).

**Plan-and-Solve prompting (ACL 2023)** — single-model prompting precursor: "devise a plan to divide the entire task into smaller subtasks, and then carry out the subtasks"; targets missing-step errors of Zero-shot-CoT; on GPT-3 it outperforms Zero-shot-CoT on all ten datasets and is comparable to 8-shot CoT on math — [arXiv](https://arxiv.org/abs/2305.04091). No separate agents, no verification; relevant only as the planner/executor split inside one context.

**AutoGen (2023), hierarchical / GroupChatManager modes** — [arXiv](https://arxiv.org/abs/2308.08155)
- Framework of "conversable" agents combining LLMs, humans and tools; conversation patterns programmed in natural language or code — [arXiv abstract](https://arxiv.org/abs/2308.08155).
- GroupChat: a `speaker_selection_method` may be a custom Python function returning the next Agent, or `'auto'`, `'manual'`, `'random'`, `'round_robin'`; returning `None` ends the chat; `max_round` caps rounds (example 20); the selection function receives `groupchat.messages` (the shared history); `allowed_speaker_transitions_dict` constrains transitions — [AutoGen 0.2 docs](https://microsoft.github.io/autogen/0.2/docs/topics/groupchat/customized_speaker_selection/). Code-enforced: speaker choice when a function is supplied, termination on `None`, round cap. In `'auto'` mode the manager is an LLM choosing speakers (the doc page does not describe its internals).
- Magentic-One is shipped on top of AutoGen (see below) — [Magentic-One HTML](https://arxiv.org/html/2411.04468).

**ADaPT (NAACL Findings 2024)** — [arXiv](https://arxiv.org/abs/2311.05772)
- Planner decomposes a sub-task only "when the LLM is unable to execute" it, recursively, so decomposition depth adapts to executor capability. Results: up to +28.3% success on ALFWorld, +27% WebShop, +33% TextCraft over baselines — [arXiv abstract](https://arxiv.org/abs/2311.05772).
- Acceptance trigger is executor failure (executor self-report of success/failure); I did not fetch the full text to confirm how failure is detected (gap).

**TaskWeaver (2023)** — [HTML](https://arxiv.org/html/2311.17541)
- Roles: Planner (talks to user, decomposes, reports); Code Interpreter = Code Generator + Code Executor; plugins as Python functions whose YAML schemas go into the CG prompt.
- What the Planner sees: the executor's return code, logs (stdout/stderr, plugin logs), cell output and artifacts (files, images); on failure the raw error can be passed to the CG instead of an LLM summary.
- What the worker sees: the Planner's subtask, plugin definitions, examples; its history keeps prior failed code and errors; the paper does not say whether the CG sees the full user request.
- Code-enforced verification: generated code is parsed to an AST and checked against configurable rules; violation → regenerate; persistent violation → failure reported to Planner; a plugin-only mode denies all non-plugin code; sessions run in their own Jupyter process / Docker container; regeneration capped at three. The paper motivates this with "LLMs may ignore prompt instructions."
- Completion: ReAct-style loop until the plan is done; no formal completion criterion.
- Results (GPT-4 / GPT-3.5 normalised): Eval-Cases 0.87/0.42, DS-1000 0.60/0.40, InfiAgent-DABench 0.88/0.70, DSEval 0.72/0.36 (text gives 0.85 for GPT-4 Eval-Cases, inconsistent with table 0.87).
- All from [TaskWeaver HTML](https://arxiv.org/html/2311.17541).

**OS-Copilot / FRIDAY (2024)** — [HTML](https://arxiv.org/html/2402.07456)
- Roles: Planner (DAG of subtasks typed API/Code/QA); Configurator (declarative, procedural=tool repository, working memory); Actor = Executor + Critic (+ Refiner).
- Planner sees system version, task, action list, API list, working directory and files — so it plans at the right granularity.
- Acceptance: the Critic, an LLM, judges subtask completion from execution results and before/after system state; Refiner retries up to three attempts. The Critic also scores generated tools 0-10; tools scoring >8 are saved. Authors admit no ground truth and LLM/rule-based state comparison can be inaccurate.
- Results (GPT-4-Turbo): GAIA test Level 1/2/3 = 40.86/20.13/6.12% vs prior best 30.30% L1 (the "35%" relative claim); SheetCopilot 60% pass@1 after self-directed learning vs 55% SheetCopilot.
- Limitations: heavy prompt engineering, model changes shift behaviour; read-only web browsing.
- All from [OS-Copilot HTML](https://arxiv.org/html/2402.07456).

**TDAG (Neural Networks)** — dynamic decomposition with a *generated* subagent per subtask, motivated by "error propagation and limited adaptability"; introduces ItineraryBench — [arXiv](https://arxiv.org/abs/2402.10178). Full text not read (gap on verification mechanics and numbers).

**Mixture-of-Agents (2024), layered aggregation** — [HTML](https://arxiv.org/html/2406.04692)
- Layers of proposers; each agent in layer k sees all outputs of layer k-1; final aggregator (default Qwen1.5-110B-Chat, 6 open-source proposers, 3 layers).
- Aggregator prompt tells it responses "may be biased or incorrect" and asks it to synthesise, not copy; an LLM-ranker (select-one) baseline did significantly worse.
- No worker sees a success criterion beyond the user prompt; no verification other than the aggregator's own judgement.
- Results: AlpacaEval 2.0 LC 65.1% (65.7% with GPT-4o aggregator; MoA-Lite 59.3%) vs GPT-4o 57.5%; MT-Bench 9.25 vs 9.19; intro cites 65.8% (inconsistency).
- Cost: high time-to-first-token since the first token waits for the last layer.
- All from [MoA HTML](https://arxiv.org/html/2406.04692).

**Agent-Oriented Planning, AOP (ICLR 2025)** — [HTML](https://arxiv.org/html/2410.02189)
- Meta-agent decomposes and allocates (JSON plan: task, agent, reasoning, deps); principles: solvability, completeness, non-redundancy.
- Pre-execution checks: a learned reward model (MiniLM embeddings → MLP) predicts how well an agent can solve a subtask *without calling it*, trained on LLM-scored (or human-scored) pairs mapped to 1-8; low score → reassign or replan. An LLM "detector" checks completeness and redundancy; >15% of queries had such issues early on.
- The paper does not describe runtime judging of sub-agent answers; the feedback loop updates each agent's "representative works" after resolution.
- Results: Husky-QA 43.7% vs HUSKY 39.6%, ReAct 37.6%, GPT-4o 33.3%; DROP 34.0 vs 28.0; IIRC 41.5 vs 36.5. Ablations: no detector 36.6%, no reward model 38.7%.
- Cost: ~1.12M prompt + 0.38M completion tokens vs ~0.02M/0.09M for single-agent GPT-4o over the test set.

**Agent S (2024)** — [HTML](https://arxiv.org/html/2410.08164)
- Manager (plan from task + initial observation + web knowledge + narrative memory) → ordered subtasks with context; Worker executes each with episodic memory and a Trajectory Reflector; Self-Evaluator summarises experiences into memory.
- Acceptance: the Worker emits DONE when *it* judges the subtask complete, or FAIL; on FAIL the Manager replans from current environment state. No independent check is described.
- Results (GPT-4o): OSWorld 20.58% vs 11.21% baseline (+83.6% relative).
- Error analysis of failed tasks: planning error 34.69%, grounding 53.06%, execution 79.59% (overlapping); 46% of execution errors were caused by planning or grounding errors.

**Agent S2 (2025)** — [HTML](https://arxiv.org/html/2504.00906)
- Manager revises the remaining subgoals after *every* completed subgoal ("Proactive Hierarchical Planning"), using latest observation, prior subgoals and original instruction; Worker returns SUCCESS/FAILURE via `done`/`fail` actions; Mixture-of-Grounding routes each action to visual (UI-TARS-72B-DPO), textual (Tesseract OCR) or structural (UNO spreadsheet) experts.
- Results (Claude-3.7-Sonnet): OSWorld 27.0% (15-step), 34.5% (50-step); proactive beats reactive planning by +4.62 / +6.15 pts.
- Error analysis: planning failures most frequent; fails to recognise infeasible tasks.

**Agent S3 / bBoN (2025)** — [arXiv](https://arxiv.org/abs/2510.02250)
- Runs multiple full rollouts, converts each to a "behavior narrative", and a Behavior Judge (separate selection step) compares them. OSWorld 72.6% vs human 72.36% (abstract v2). Earlier coverage reported 69.9% (with bBoN) from 62.6% single run — [LessWrong summary](https://www.lesswrong.com/posts/rft2jio6CzvmsvTua/behavior-best-of-n-achieves-near-human-performance-on); conflicting figures across versions, trust the arXiv v2 abstract.

**Magentic-One (2024)** — [HTML](https://arxiv.org/html/2411.04468)
- Roles: Orchestrator (lead) + WebSurfer (screenshot + text description of new page state), FileSurfer (markdown file previewer), Coder (LLM writes Python), ComputerTerminal (deterministic code/shell execution, no LLM, returns results and errors).
- Task ledger (outer loop): given/verified facts, facts to look up, facts to derive, educated guesses, plan. Progress ledger (inner loop) asks each step: Is the request fully satisfied? Are we looping? Is progress being made? Who speaks next? What instruction to give?
- Stall counter; when it exceeds a threshold (≤2 in experiments) the Orchestrator reflects, rewrites the ledger and plan; agents' contexts are reset after each plan update (context deliberately not carried across replans).
- Termination: task judged complete by the Orchestrator, or a code limit (max attempts / time); then it reviews transcript and ledger and outputs final answer or best guess. No independent artifact check of completion is described.
- Results: GAIA test 32.33±5.3 (GPT-4o), 38.00±5.5 (GPT-4o+o1); AssistantBench accuracy 25.3 / 27.7; WebArena 32.8±3.2. Ablation: removing ledgers −31% on GAIA validation.
- Error analysis (automated coding of logs): most common "persistent-inefficient-actions"; second "insufficient-verification-steps" (tasks marked complete without adequate validation); third "inefficient-navigation-attempts".
- Risks observed: agents repeatedly tried to log in to a misconfigured site until the account was suspended, then attempted a password reset; accepted ToS/cookie prompts; tried to recruit humans (social posts, emailing textbook authors).
- Cost: "perhaps several US dollars, and tens of minutes per task"; not formally evaluated.

**Magentic-UI (2025)** — human-in-the-loop successor; co-planning, co-tasking, action guards, long-term memory; built on the same multi-agent architecture — [arXiv](https://arxiv.org/abs/2507.22358). Here the human is the verifier/approver for irreversible actions (action guards).

**Anthropic "Building effective agents" (Dec 2024)** — [blog](https://www.anthropic.com/engineering/building-effective-agents)
- Orchestrator-workers: central LLM breaks down a task, assigns to workers, synthesises; used when subtasks cannot be predicted in advance (coding across multiple files, multi-source search).
- Evaluator-optimizer is presented as a separate pattern where a *separate* LLM call evaluates — i.e., judging is not part of orchestrator-workers by default.
- Agents should obtain "ground truth" from the environment at each step (tool results, code execution); common stopping condition is a maximum number of iterations.

**Anthropic multi-agent research system (June 2025)** — [blog](https://www.anthropic.com/engineering/multi-agent-research-system)
- Roles: LeadResearcher (plans, saves plan to memory, spawns subagents, synthesises, decides whether more research is needed); subagents (own context, search tools, interleaved thinking); CitationAgent (attributes claims to sources after the report is written).
- Worker brief: objective, output format, guidance on tools/sources, clear task boundaries. Vague briefs caused duplicated work (one subagent on 2021 chip crisis while two others both researched 2025 supply chains).
- Hand-back: condensed findings (subagents "act as filters"); an appendix pattern has subagents write artifacts to external storage and return lightweight references.
- Acceptance: the lead's own judgement on synthesised results; criteria not specified. Separate judge only in *evaluation* (LLM-as-judge rubric: factual accuracy, citation accuracy, completeness, source quality, tool efficiency; 0.0-1.0 + pass/fail), not in the runtime loop.
- Code vs prompt: prompts carry effort-scaling rules (simple: 1 agent, 3-10 tool calls; comparisons: 2-4 subagents, 10-15 calls each; complex: >10 subagents), delegation format, source-quality heuristics; code carries durable execution with checkpoint/resume, retries, tracing, rainbow deploys. Whether subagent count limits are code-enforced is not stated.
- Execution is synchronous: lead waits for each batch; cannot steer subagents mid-run.
- Failures: spawning 50 subagents for simple queries; endless searching for nonexistent sources; subagents distracting each other with excessive updates; SEO content farms preferred over authoritative sources; continuing after results sufficient.
- Numbers: multi-agent (Opus 4 lead, Sonnet 4 subagents) beat single-agent Opus 4 by 90.2% on internal research eval; token usage explains 80% of BrowseComp variance (95% with tool calls and model choice); agents use ~4x chat tokens, multi-agent ~15x; parallelism cut research time up to 90%; 3-5 subagents in parallel.
- No paper form located (gap).

**OpenAI Swarm (2024) and Agents SDK (2025)**
- Swarm: two primitives, Agents and handoffs; "An Agent can hand off to another Agent by returning it in a function"; on handoff "the system prompt will change, but the chat history will not" (receiver sees the full history); stateless between calls; labelled "experimental, educational" and superseded by the Agents SDK — [GitHub](https://github.com/openai/swarm).
- Agents SDK handoffs: exposed to the LLM as a tool `transfer_to_<agent>`; by default the receiver sees the full prior conversation and takes over; `input_filter` can strip history (e.g., `remove_all_tools`); `nest_handoff_history` (beta, off by default) condenses history into summaries; `input_type` gives a schema validated by the SDK; `on_handoff` can raise to block a transfer; input guardrails run only on the first agent, output guardrails only on the agent producing the final output — [handoffs docs](https://openai.github.io/openai-agents-python/handoffs/).
- Agents-as-tools (`Agent.as_tool()`): the manager keeps control and "owns the final answer", combining specialists and enforcing guardrails in one place; code-driven alternatives include structured outputs, chaining, a `while` loop with an evaluator agent "until criteria are met", and `asyncio.gather` — [multi-agent docs](https://openai.github.io/openai-agents-python/multi_agent/). The page does not state exactly what the manager receives from an as_tool call (gap; commonly the sub-agent's final output).

**Claude Code subagents (docs, 2025-2026)** — [docs](https://code.claude.com/docs/en/sub-agents)
- Defined as Markdown with YAML frontmatter (`name`, `description` required; `tools`, `disallowedTools`, `model`, `permissionMode`, `maxTurns`, `hooks`, `isolation: worktree`, etc.).
- Worker sees: its system prompt, the task message the parent writes, CLAUDE.md, a git status snapshot, preloaded skills; *not* the parent conversation (except "fork" subagents, which inherit the full conversation).
- Hand-back: the subagent returns only its summary/final report; verbose output stays out of the parent context; `maxTurns` exhaustion marks output partial. Under auto mode a classifier reviews the subagent's work and report before delivery; reports are scanned for imitated markup but "the scan doesn't judge content".
- Code-enforced: tool allowlist/denylist, certain tools always removed, nesting depth limit (default three layers, env var configurable), concurrency cap (default 20), `PreToolUse` hooks that can block (exit code 2), `SubagentStop` hooks.
- Delegation is decided by the parent matching tasks against `description`.
- Cognition notes Claude Code subagents are generally limited to answering well-defined questions and generally don't write code, keeping investigation out of the main history — [Cognition](https://cognition.com/blog/dont-build-multi-agents).

**TalkHier (2025)** — structured communication protocol plus "hierarchical refinement" to address incorrect outputs, falsehoods and biases; beats o1, AgentVerse and majority voting on open-domain QA, selective questioning and ad-text generation — [arXiv](https://arxiv.org/abs/2502.11098). Full text not read (gap on whether refinement uses separate evaluators; my recollection is that it uses a hierarchy of evaluator agents, unverified).

**Plan-and-Act (2025)** — separate Planner model (structured high-level plan) and Executor model (environment actions); planner trained on synthetic plans annotated onto ground-truth trajectories; WebArena-Lite 57.58%, WebVoyager 81.36% (text-only) — [arXiv](https://arxiv.org/abs/2503.09572).

**HALO (2025)** — three levels: high-level planning agent, mid-level role-design agents that instantiate agents per subtask, low-level inference agents; execution as MCTS workflow search; +14.4% average over baselines on HumanEval/MMLU/MATH — [arXiv](https://arxiv.org/abs/2505.13516).

**Puppeteer (NeurIPS 2025)** — a centralised orchestrator trained with RL to sequence "puppet" agents by evolving task state; improvements stem from "more compact, cyclic reasoning structures" with reduced cost — [arXiv](https://arxiv.org/abs/2505.19591).

**OWL / Workforce (2025)** — [HTML](https://arxiv.org/html/2505.23885)
- Planner (decomposes using a worker capability registry, synthesises final answer), Coordinator (assigns, manages dependencies, integrates), Workers (Web, Document, Reasoning/Coding).
- Hand-back: workers post only final results to a shared task channel; tool-call detail stays isolated; each worker sees only its subtask and concise prior results.
- Acceptance: worker self-assesses failure and posts failure info; Planner replans up to K=2 (code-tracked counter). No separate Coordinator check described.
- Results: GAIA validation 69.70% (Claude-3.7-Sonnet), 60.61% (GPT-4o) vs single agent 37.58%; OWL-trained Qwen2.5-32B planner 52.73% (+16.37) — the "RL" stage is described as DPO. Planner-only training 45.45%, worker-only 31.51%.
- Error analysis: limited tool capability 32.69%, planner errors 21.15%, model capability 19.23%. Inconsistency: OpenAI Deep Research cited as 67.36% in table and 55.15% in intro.

**AgentOrchestra (2025)** — [HTML](https://arxiv.org/html/2506.12508)
- Central planner + Deep Researcher, Browser Use, Deep Analyzer, Tool Generator, Reporter; "automatic replanning under environment shifts or execution failures"; no separate verification step described; accept/retry criteria and what the planner receives are not described in the portion read.
- Self-evolution via TextGrad/self-reflection on prompts, code and solutions with versioning (TEA protocol) for rollback.
- Results: GAIA test 89.04% (L1 98.92, L2 85.53, L3 81.63); validation 93.33% evolved vs 89.70% vanilla; HLE 59.6 vs 55.2.
- Cost estimates: simple ~30 s/5k tokens, complex ~10 min/100k tokens.

**AgentFlow (ICLR 2026 Oral)** — four modules: planner, executor, verifier, generator, coordinated through evolving memory; only the planner is trained (Flow-GRPO) with a single verifiable trajectory-level outcome broadcast to every turn; 7B backbone gains +14.9% search, +14.0% agentic, +14.5% math, +4.1% science, surpassing GPT-4o — [arXiv](https://arxiv.org/abs/2510.05592). Notable as an explicit plan/verify split.

**Towards a Science of Scaling Agent Systems (Google, Dec 2025)** — [HTML](https://arxiv.org/html/2512.08296)
- 260 configurations, 6 benchmarks, 5 architectures. Independent: aggregator concatenates outputs "without cross-validation or majority voting". Centralized: orchestrator decomposes, monitors, coordinates; sub-agents talk only to it; it is the only verification point.
- Trace-level error amplification: Independent 17.2x, Decentralized 7.8x, Hybrid 5.1x, Centralized 4.4x (single agent 1.0); but the error-amplification main effect was non-significant in regression (p=0.658).
- Overhead: Centralized 285%, success 0.463 vs single agent 0.466; Hybrid 515%.
- Capability saturation: above ~45% single-agent performance, adding agents has negative returns (β=−0.236, p=0.004).
- Centralized vs single agent: Finance-Agent +80.8%, BrowseComp-Plus +0.2%, SWE-bench Verified −3.1%, Terminal-Bench −19.2%, PlanCraft −50.3%; the −70% PlanCraft figure in the abstract is for Independent.

**Kimi K2.5 Agent Swarm (Jan 2026)** — trainable orchestrator (PARL) decomposes into parallel subtasks run by frozen subagent copies; reported failure "serial collapse" (orchestrator defaults to single-agent execution), countered with staged reward shaping; vendor reports up to 100 subagents and 80% runtime reduction — [Kimi blog](https://www.kimi.com/blog/kimi-k2-5) via search summary; vendor claims, not independently verified; tech report PDF not located.

**Intelligent AI Delegation (DeepMind, Feb 2026)** — conceptual framework: delegation as task allocation plus "transfer of authority, responsibility, accountability, clear specifications regarding roles and boundaries, clarity of intent, and mechanisms for establishing trust"; argues existing decomposition/delegation "rely on simple heuristics" and cannot "robustly handle unexpected failures" — [arXiv](https://arxiv.org/abs/2602.11865). Secondary coverage says it discusses monitoring from status signalling to cryptographic verification / zero-knowledge proofs — [ArXivIQ](https://arxiviq.substack.com/p/intelligent-ai-delegation) (not checked against full text). Closest to a principal-agent framing in this family.

**VMAO (ICLR 2026 workshop)** — [HTML](https://arxiv.org/html/2603.11445)
- QueryPlanner → DAG of sub-questions each with agent type, dependencies, priority and *verification criteria*; DAGExecutor runs batches of 3; domain agents; ResultVerifier (Claude Opus 4.5) as a separate judge; AdaptiveReplanner; Synthesizer.
- Verifier sees sub-question, criteria, agent result and dependency results — not raw sources; it "can confirm that a claim is present and sourced" but not its truth. Verdict: complete/partial/incomplete, completeness 0-1, missing aspects, contradictions, accept/retry/escalate, confidence.
- Stop rules: completeness ≥0.8; 75% confidence with 50% completeness; <5% improvement; 1M-token budget; max 3 iterations. >75% of queries ended on resource-based stops. Whether workers receive the criteria is not stated.
- Results (25 queries): completeness 3.1→4.2, source quality 2.6→4.1 vs single agent; ~850K vs 100K tokens (~8.5x), 900 s vs 165 s.
- Limits: completeness ≠ accuracy; a misframed sub-question lets the verifier accept a well-sourced but irrelevant answer; judge and executor are the same model family.

**Recognize Your Orchestrator (May 2026)** — [HTML](https://arxiv.org/html/2606.01351)
- Global context initialised with the query and appended with selected executors' outputs each step (accumulating "verbose logs"); max 20 steps.
- Orchestrators caused 67.7% of failures vs 32.3% executors; orchestrators "often lose track of task state, causing loops or early termination".
- "Reasoning Trap": reasoning-heavy models are poor orchestrators (DeepSeek-R1 lowest average 48.96; GPT-5 64.18); GPT-5 High→Low reasoning cut tokens ~69% and raised Step-SR 0.251→0.302; Claude-4.5-Sonnet had best Step-SR 60.83.

**SwarmBench (EMNLP 2026 Findings)** — benchmark of LLMs as swarm orchestrators measuring accuracy, efficiency, cost and process quality; finds substantial differences between models; proposes SwarmExp (experience extraction/replay) — [arXiv](https://arxiv.org/abs/2608.30661). Full text not read.

**HTN-Orchestrate (Oct 2026)** — [HTML](https://arxiv.org/html/2610.22195)
- Planner maintains a hierarchical task network, deferring decomposition until prerequisites resolve; one Orchestrator per leaf dispatches workers (researchers *and verifiers*), waits or terminates; Synthesizers; Recovery extracts supported facts for the next epoch.
- Planner sees only completed precursor summaries and completion outcome (`resolved` / `exhausted_unresolved`), budgeted at 24,000 characters (6,000 per summary).
- Leaf acceptance: terminate when reports contain a complete answer *and a verifier has confirmed it* (CONFIRMED / NEEDS CORRECTION / INCOMPLETE), or when no distinct evidence route remains (keep best candidate, list gaps).
- Code-enforced: atomic plan assembly with coverage and acyclicity checks, depth/branching limits, rounds, worker capacity, time budgets (7,200 s per leaf, 28,800 s per question, 12 orchestrator decisions per leaf per epoch, 70 ReAct turns per worker). Prompt-only: planning action choice, dispatch/terminate rules, verifier phases, synthesis.
- Results (DeepSeek-V4.1-Flash): BrowseComp 89.73% vs Agent Team 87.28, DeepSeek Harness 80.33, ReAct 73.93; SUPERChem 73.44 vs 68.75. Rebuilds occurred on 50% of incorrect questions vs 14.7% of correct ones. No token costs reported.

**Cognition "Don't Build Multi-Agents" (June 2025, critique)** — principles "Share context, and share full agent traces, not just individual messages" and "Actions carry implicit decisions, and conflicting decisions carry bad results"; Flappy Bird example: one subagent built a Super Mario-style background, the other a bird mismatched to the assets; recommends single-threaded linear agent plus a context-compression model — [Cognition](https://cognition.com/blog/dont-build-multi-agents).

### Inferences
- The family splits cleanly by *what the orchestrator conditions acceptance on*: (a) worker self-report (Agent S/S2 DONE/FAIL, OWL failure posts, ADaPT executor failure, Anthropic research lead, Claude Code report); (b) environment ground truth (TaskWeaver return codes/AST rules, Magentic-One ComputerTerminal, OS-Copilot before/after state); (c) a separate LLM judge (VMAO verifier, HTN-Orchestrate verifier workers, OS-Copilot Critic, AgentFlow verifier, Agent S3 Behavior Judge); (d) pre-execution prediction (AOP reward model). For a contract-theory reading, (a) is pure cheap talk, (b) is verifiable output, (c) is costly monitoring by a possibly correlated monitor.
- Fixed budgets (stall counters, max iterations, token caps, time caps, K replans) are the one control almost every system enforces in code; acceptance criteria are almost always prompt-level.

### Gaps
- No paper form of Anthropic's research-system post was found.
- Venues for HuggingGPT, AutoGen, Agent S and MoA could not be confirmed from arXiv pages (commonly cited as NeurIPS 2023, COLM 2024, ICLR 2025, ICLR 2025 respectively — unverified here).
- Full texts of TDAG, TalkHier, HALO, Puppeteer, SwarmBench, Plan-and-Act and ADaPT were not read; their acceptance mechanics are not recorded.
- Kimi K2.5/PARL tech report not located; claims are vendor-only.
- Google ADK, LangGraph supervisor, CrewAI hierarchical process are production frameworks (other researcher's scope); not covered.

## Q1. Does the orchestrator verify, or trust? Where it verifies, with what?

### Takeaway
Most orchestrators trust: they accept the worker's own DONE/success report or synthesised summary, bounded by a code-enforced budget. Verification, where present, is mostly another LLM (critic/verifier/judge); only execution feedback (return codes, errors, AST rule checks, environment state) is non-LLM, and even explicit verifiers check completeness/sourcing rather than truth.

### Cited Findings
- Agent S: Worker emits DONE when it judges the subtask complete; Manager replans only on FAIL — [Agent S HTML](https://arxiv.org/html/2410.08164). Agent S2 same `done`/`fail` signals, but the Manager replans after every subgoal — [Agent S2 HTML](https://arxiv.org/html/2504.00906).
- OWL Workforce: failure detection is worker-driven self-assessment; planner replans up to K=2 — [OWL HTML](https://arxiv.org/html/2505.23885).
- Magentic-One: completion is the Orchestrator's own judgement via the progress-ledger question "is the request fully satisfied?"; no independent artifact check; "insufficient-verification-steps" is its second most common error — [Magentic-One HTML](https://arxiv.org/html/2411.04468).
- Anthropic research system: lead decides whether more research is needed; LLM-as-judge used for evaluation, not as a runtime gate — [Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system).
- TaskWeaver: code-level AST rule verification, return codes and logs drive regeneration (max 3) — [TaskWeaver HTML](https://arxiv.org/html/2311.17541).
- OS-Copilot: LLM Critic compares before/after system state; authors note it lacks ground truth and can be inaccurate — [OS-Copilot HTML](https://arxiv.org/html/2402.07456).
- VMAO: separate LLM verifier (Claude Opus 4.5) scores completeness 0-1; "can confirm that a claim is present and sourced" but not its truth — [VMAO HTML](https://arxiv.org/html/2603.11445).
- HTN-Orchestrate: leaf terminates only when a verifier worker has confirmed the answer (CONFIRMED / NEEDS CORRECTION / INCOMPLETE) — [HTN-Orchestrate HTML](https://arxiv.org/html/2610.22195).
- AgentFlow has an explicit verifier module distinct from the trained planner — [AgentFlow arXiv](https://arxiv.org/abs/2510.05592).
- Agent S3: a Behavior Judge compares multiple rollouts' narratives instead of trusting one — [arXiv](https://arxiv.org/abs/2510.02250).
- AOP verifies *before* execution: a reward model predicts subtask solvability per agent; LLM detector checks completeness/redundancy — [AOP HTML](https://arxiv.org/html/2410.02189).
- MoA: aggregator is warned inputs "may be biased or incorrect" — verification is the aggregator's own judgement — [MoA HTML](https://arxiv.org/html/2406.04692).
- Claude Code: a classifier reviews subagent work under auto mode (a safety check), and the report scan "doesn't judge content" — [Claude Code docs](https://code.claude.com/docs/en/sub-agents).
- Cross-system: centralized orchestration as "the only verification point" yields 4.4x error amplification vs 17.2x for independent agents whose aggregator concatenates "without cross-validation" — but the effect was non-significant in regression (p=0.658) — [Scaling Agent Systems](https://arxiv.org/html/2512.08296).
- MAST: many existing verifiers do superficial checks "such as confirming that code compiles" despite being prompted to verify thoroughly; adding high-level task-objective verification gave +15.6% on ProgramDev (ChatDev) — [MAST HTML](https://arxiv.org/html/2503.13657).
- Anthropic guidance: agents should get "ground truth" from the environment each step — [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents).

### Inferences
- For a harness designer: verification by the same model family that produced the work (VMAO notes judge and executor share a family) is a correlated monitor; the only uncorrelated signals in this literature are environment outputs (execution, state diffs) and multiple independent rollouts (Agent S3).
- A verifier given only the worker's text (VMAO) checks the report, not the world; HTN-Orchestrate's verifier is itself a worker with tools, which moves verification closer to the artifact.

### Gaps
- No system in this family reports an ablation isolating "orchestrator verifies artifact" vs "orchestrator trusts report" under fixed budget, except partial evidence from MAST's +15.6% intervention and VMAO's non-ablated comparison.

## Q2. What does a worker's hand-back actually contain, and is the orchestrator's decision made on the worker's words or on the artifact?

### Takeaway
Hand-backs are overwhelmingly worker-written text: a summary/final message (Claude Code, Anthropic research, OWL, HTN-Orchestrate summaries capped at 6,000 chars), sometimes plus an artifact reference. Only TaskWeaver (return code, logs, output, files), Magentic-One's WebSurfer/Terminal (screenshot, execution result) and HuggingGPT (structured model outputs with probabilities) hand back machine-produced evidence. Decisions are therefore mostly made on the worker's words.

### Cited Findings
- Claude Code: subagent returns only its summary; verbose output stays in the subagent's context — [Claude Code docs](https://code.claude.com/docs/en/sub-agents).
- Anthropic research: subagents return condensed findings ("act as filters"); optional pattern of writing artifacts to storage and passing references — [Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system).
- OWL: workers post only final results; tool-call context isolated — [OWL HTML](https://arxiv.org/html/2505.23885).
- HTN-Orchestrate: Planner receives only precursor summaries and a resolved/exhausted flag, 24,000-char budget (6,000 per summary) — [HTN HTML](https://arxiv.org/html/2610.22195).
- TaskWeaver: return code, stdout/stderr, cell output, artifacts; raw error can be forwarded unsummarised — [TaskWeaver HTML](https://arxiv.org/html/2311.17541).
- Magentic-One: WebSurfer returns screenshot plus written description; ComputerTerminal returns execution results and errors deterministically — [Magentic-One HTML](https://arxiv.org/html/2411.04468).
- HuggingGPT: structured inference results (bounding boxes with probabilities, answer distributions) — [HuggingGPT HTML](https://arxiv.org/html/2303.17580).
- Agent S/S2: worker returns a DONE/FAIL signal; manager re-observes the environment (latest screenshot) when replanning — [Agent S2 HTML](https://arxiv.org/html/2504.00906).
- OpenAI handoffs pass the whole conversation to the receiver (no hand-back: control moves); agents-as-tools keeps the manager in control — [handoffs](https://openai.github.io/openai-agents-python/handoffs/), [multi-agent](https://openai.github.io/openai-agents-python/multi_agent/); Swarm likewise keeps full chat history across handoffs — [Swarm](https://github.com/openai/swarm).
- Recognize Your Orchestrator: orchestrator context accumulates executors' outputs each step ("verbose logs") — [HTML](https://arxiv.org/html/2606.01351).
- Cognition argues summaries are insufficient: "share full agent traces, not just individual messages" — [Cognition](https://cognition.com/blog/dont-build-multi-agents).

### Inferences
- There is a design tension between Cognition (send full traces) and Claude Code / Anthropic / OWL / HTN (send summaries to save context); the "Reasoning Trap"/context-squeezing result and Anthropic's 200K truncation note support the summary side, while Flappy-Bird-style misinterpretation supports the trace side.
- Agent S2's choice to re-read the screen after each subgoal is the cleanest example of deciding on the artifact (environment state) rather than the worker's words.

### Gaps
- None of the papers measures how often a worker's summary misstates what its trace or artifact shows.

## Q3. Is the worker told the success criterion, part of it, or none of it?

### Takeaway
Workers usually get a subtask description and, at best, an output format and boundaries; the global success criterion stays with the orchestrator. Only VMAO attaches explicit per-subtask verification criteria (and does not say workers see them); Claude Code and Anthropic's research briefs include objective/format/boundaries; HuggingGPT/OWL/Agent S workers see only their slice.

### Cited Findings
- Anthropic research: brief = objective, output format, tool/source guidance, task boundaries — [Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system).
- Claude Code: a non-fork subagent gets its system prompt and the task message Claude writes, not the conversation history — [docs](https://code.claude.com/docs/en/sub-agents).
- OWL: each worker sees only its current subtask and concise results from earlier subtasks — [OWL HTML](https://arxiv.org/html/2505.23885).
- TaskWeaver: the paper does not say whether the Code Generator sees the full user request — [TaskWeaver HTML](https://arxiv.org/html/2311.17541).
- Agent S: worker's retrieval keyed on user task, subtask and its context — so it receives the user task string — [Agent S HTML](https://arxiv.org/html/2410.08164). Agent S2 Manager gets the original instruction; worker works on the top subgoal — [Agent S2 HTML](https://arxiv.org/html/2504.00906).
- VMAO: sub-questions carry `verification_criteria`; whether workers receive them is not stated — [VMAO HTML](https://arxiv.org/html/2603.11445).
- HTN-Orchestrate: an instruction generator writes each worker's assignment (contents not detailed in the portion read) — [HTN HTML](https://arxiv.org/html/2610.22195).
- Magentic-One: agents' contexts are reset after each plan update; the Orchestrator issues per-step instructions via the progress ledger — [Magentic-One HTML](https://arxiv.org/html/2411.04468).
- Cognition: sharing only the original task was not enough for subagents to interpret subtasks consistently (Flappy Bird) — [Cognition](https://cognition.com/blog/dont-build-multi-agents).
- Intelligent AI Delegation lists "clear specifications regarding roles and boundaries" and "clarity of intent" as required parts of delegation — [arXiv](https://arxiv.org/abs/2602.11865).

### Inferences
- In information-design terms, almost every system withholds the acceptance rule from the worker; the worker cannot target the judge's criterion, which limits gaming but also causes the misinterpretation failures Anthropic and Cognition report.

### Gaps
- No paper found that varies how much of the success criterion is disclosed to workers and measures the effect.

## Q4. Which systems report the orchestrator was fooled by confident worker reports, or that context was lost at the handoff?

### Takeaway
Direct reports of "orchestrator fooled by a worker's confident claim" are rare and indirect: Magentic-One's "insufficient-verification-steps" (tasks marked complete without validation), MAST's premature termination / no or incorrect verification, VMAO's verifier accepting well-sourced but irrelevant answers. Context loss at handoff is reported more directly by Cognition, Anthropic (duplication, misread tasks), and is a structural cause in Recognize Your Orchestrator (orchestrator loses task state; 67.7% of failures).

### Cited Findings
- Magentic-One: "insufficient-verification-steps" (second most common): tasks marked complete without adequate validation — [Magentic-One HTML](https://arxiv.org/html/2411.04468).
- MAST (pointer; covers Magentic-One and others): premature termination 6.2%, no or incomplete verification 8.2%, incorrect verification 9.1%; reasoning-action mismatch 13.2%, task derailment 7.4%, information withholding 0.85%, ignored other agent's input 1.9% — [MAST HTML](https://arxiv.org/html/2503.13657).
- VMAO: verifier may miss factual errors; a misframed sub-question lets it accept a well-sourced but irrelevant answer — [VMAO HTML](https://arxiv.org/html/2603.11445).
- Anthropic: vague briefs → duplicated work; subagents searched endlessly for nonexistent sources; spawning 50 subagents for simple queries; lead cannot steer subagents mid-run (synchronous) — [Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system).
- Cognition: subagents misinterpreted subtasks and produced incompatible pieces; "conflicting decisions carry bad results" — [Cognition](https://cognition.com/blog/dont-build-multi-agents).
- Recognize Your Orchestrator: orchestrators caused 67.7% of failures; often lose track of task state causing loops or early termination; reasoning models suffer "context squeezing" — [HTML](https://arxiv.org/html/2606.01351).
- Agent S: 46% of execution errors were caused by upstream planning or grounding errors (error propagation across levels) — [Agent S HTML](https://arxiv.org/html/2410.08164).
- OWL: planner errors 21.15% of failures — [OWL HTML](https://arxiv.org/html/2505.23885).
- HuggingGPT: LLM may not follow instructions, causing workflow exceptions; plans not guaranteed feasible — [HuggingGPT HTML](https://arxiv.org/html/2303.17580).
- Kimi K2.5: "serial collapse" — orchestrator stops delegating — [Kimi blog](https://www.kimi.com/blog/kimi-k2-5) (vendor).
- Who&When: failure attribution in MAS logs is hard — best method 53.5% accuracy for the responsible agent, 14.2% for the decisive step — [arXiv](https://arxiv.org/abs/2505.00212).
- Cost: multi-agent ~15x chat tokens (Anthropic); VMAO ~8.5x single-agent tokens; AOP ~1.5M tokens vs ~0.1M; Magentic-One "several US dollars, tens of minutes per task"; centralized overhead 285% (Scaling Agent Systems) — sources as above.

### Inferences
- The literature reports "orchestrator accepted an unverified completion" mostly as an aggregate category from log analysis, not as a measured rate of false worker claims; a harness that logs worker claim vs ground-truth artifact would fill a real gap.
- Systems that deliberately reset context (Magentic-One after replans) or cap summaries (HTN 6,000 chars) trade context loss for orchestrator attention, consistent with the context-squeezing finding.

### Gaps
- I found no paper that specifically measures sycophantic or confident-but-false worker reports deceiving an orchestrator (e.g., a worker claiming tests pass when they don't) within this family; the closest evidence is MAST's verification categories and Magentic-One's error coding.
- Claude Code / Agents SDK docs do not report failure statistics.
