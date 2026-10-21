# Role-based multi-agent LLM teams with SOPs (mainly software engineering), 2023 to Oct 2026

Scope: systems that organise LLM agents as a team of named roles (PM, architect, coder, reviewer, tester...) following a fixed procedure. Out of scope and covered by other researchers, mentioned only as pointers: orchestrator-worker systems (e.g. ChatDev's Puppeteer, arXiv 2505.19591, NeurIPS 2025), topology optimisation (MacNet, arXiv 2406.07155), generator-critic loops, debate, failure surveys (MAST is used here only for what it says about ChatDev/MetaGPT/HyperAgent), production frameworks (ChatDev 2.0 "DevAll").

PDFs: all 29 papers below were downloaded to `C:\Users\lione\agents\research\multiagent_llm_systems\pdfs\<arxiv-id>.pdf`; every download returned a valid `%PDF-` file, none failed. PDF URL for every entry is `https://arxiv.org/pdf/<arxiv-id>`.

Status legend: **Published** = a venue was confirmed in a source; **Preprint** = only arXiv found.

## Q0. Which systems belong to this family, and how is each one structured as an incentive-and-information system?

### Takeaway
The family runs from free two-agent role-play (CAMEL, 2023) through SOP pipelines with structured documents (MetaGPT, ChatDev, 2023), to designs that split test-writing from code-writing (AgentCoder, EvoMAC) and to 2025-2026 repository-scale teams (Agyn, AgentForge). The main structural divide is between systems whose loop is closed by **executed tests** and systems closed by an **LLM verdict or a round cap**. In the canonical open-source code (ChatDev 1.0, MetaGPT), most "done" signals are strings the agents emit themselves ("<INFO> Finished", "YES"), bounded by hard round or budget caps.

### Cited Findings

#### MetaGPT (Hong, Zhuge, Chen et al., 15 authors incl. Schmidhuber). arXiv 2308.00352. **Published, ICLR 2024 (oral).** PDF https://arxiv.org/pdf/2308.00352
- Venue: ICLR 2024 oral — [ICLR](https://www.iclr.cc/virtual/2024/oral/19756); arXiv v7 Nov 2024 — [arXiv](https://arxiv.org/abs/2308.00352)
- (1) Roles: the Product Manager writes the PRD (goals, user stories, competitive analysis, requirement pool). The Architect writes the system design (file list, data structures, interfaces, call-flow diagram). The Project Manager writes a task list with one task per code file. The Engineer writes code. The QA Engineer writes and reviews unit tests — [arXiv HTML](https://arxiv.org/html/2308.00352v7)
- (2) Visibility: agents publish structured messages to a **shared message pool** and **subscribe by role profile**, which filters out irrelevant content. For example, the Architect mainly watches PRDs. An agent acts only after all its prerequisite inputs arrive. Communication is through documents and diagrams, not dialogue — [arXiv HTML](https://arxiv.org/html/2308.00352v7)
- (2, code) In the repo, the Engineer loads the system-design doc, the task doc and the existing source file. On bug fixes it receives all source files — [engineer.py](https://raw.githubusercontent.com/geekan/MetaGPT/main/metagpt/roles/engineer.py). The QaEngineer builds a `TestingContext` from the test doc and the **code doc**, loads code from the repo, and uses `msg.instruct_content`. It does **not** read the Engineer's message text or explanation — [qa_engineer.py](https://raw.githubusercontent.com/geekan/MetaGPT/main/metagpt/roles/qa_engineer.py)
- (3) Stopping, paper: executable feedback. The Engineer iterates until the tests pass or **3 retries** are used up — [arXiv HTML](https://arxiv.org/html/2308.00352v7)
- (3) Stopping, code: `Team.run(n_round=3)` loops until the round count is exhausted, all roles are idle, or the budget runs out. `_check_balance()` raises `NoMoneyException` when `total_cost >= max_budget`, the budget being set by `invest()`. The exception is not caught in `run`, so archiving is skipped — [team.py](https://raw.githubusercontent.com/geekan/MetaGPT/main/metagpt/team.py)
- (3, code) The Engineer's "summarize code" loop passes on an **LLM verdict**: `_is_pass` asks "Does the above log indicate anything that needs to be done?" and returns True if the string "YES" appears in the reply. It is capped by `max_auto_summarize_code`. The code comment says -1 means unlimited, but the logic breaks immediately at -1 — [engineer.py](https://raw.githubusercontent.com/geekan/MetaGPT/main/metagpt/roles/engineer.py)
- (3, code) The QaEngineer has `test_round_allowed = 5`. After that it emits "Exceeding 5 rounds of tests, stop." Results of `RunCode` are routed to the Engineer ("Alex"). `DebugError` output is routed back to QA itself — [qa_engineer.py](https://raw.githubusercontent.com/geekan/MetaGPT/main/metagpt/roles/qa_engineer.py)
- (4) Measurable vs judgment work: the paper contradicts itself. Section 3.3 says the Engineer writes and runs unit tests. Section 3.1 and Appendix B give test generation to the QA Engineer — [arXiv HTML](https://arxiv.org/html/2308.00352v7). In code, the QA role writes the tests, from the code — [qa_engineer.py](https://raw.githubusercontent.com/geekan/MetaGPT/main/metagpt/roles/qa_engineer.py)
- (5) Code vs prompt: the SOP is "encoded into prompt sequences", with a schema and format per role output. The paper does not describe schema validation. Executable feedback is the one mechanism clearly in code — [arXiv HTML](https://arxiv.org/html/2308.00352v7). In code: round cap, budget cap, QA round cap, and pub-sub routing via `send_to` — [team.py](https://raw.githubusercontent.com/geekan/MetaGPT/main/metagpt/team.py), [qa_engineer.py](https://raw.githubusercontent.com/geekan/MetaGPT/main/metagpt/roles/qa_engineer.py)
- (6) Failures, self-reported: no UI or front-end coverage; real-world complex requirements remain hard; earlier versions missed errors in review because of hallucination — [arXiv HTML](https://arxiv.org/html/2308.00352v7)
- (7) Results: HumanEval pass@1 85.9%, MBPP 87.7%. Executable feedback adds +4.2 points (HumanEval) and +5.4 points (MBPP). SoftwareDev executability 3.75 vs ChatDev 2.25, human revision cost 0.83 vs 2.5, tokens 31,255 vs 19,292. The full four-agent setup costs $1.385 per project; Engineer-only costs $0.915 with executability 1.0. The text gives running time as 503 s, but Table 1 says 541 s — [arXiv HTML](https://arxiv.org/html/2308.00352v7)

#### ChatDev (Qian, Liu, Liu, Chen, Dang, Li, Yang, Chen, Su, Cong, Xu, Li, Liu, Sun). arXiv 2307.07924. **Published, ACL 2024 (long).** PDF https://arxiv.org/pdf/2307.07924
- Venue: "Accepted to ACL 2024" on the arXiv record — [search summary of arXiv/ACL Anthology](https://arxiv.org/abs/2307.07924v5)
- (1) Roles: CEO, CTO, programmer, reviewer, tester. The chat chain has design, coding (writing, then completion) and testing (static code review, then dynamic system testing). Each subtask is a dual-agent instructor/assistant chat — [arXiv HTML](https://arxiv.org/html/2307.07924v5). The code's role list adds Counselor, CHRO, CPO and CCO — [ChatChainConfig.json (chatdev1.0)](https://raw.githubusercontent.com/OpenBMB/ChatDev/chatdev1.0/CompanyConfig/Default/ChatChainConfig.json)
- (2) Visibility: short-term memory holds the instruction-response pairs within a phase. Across phases, **only the solutions** are passed forward, "rather than the entire communication history" — [arXiv HTML](https://arxiv.org/html/2307.07924v5). The code-review phase env holds `task, modality, ideas, language, codes, images`. There is no programmer-reasoning field, though the in-phase role-play history is present — [phase.py](https://raw.githubusercontent.com/OpenBMB/ChatDev/chatdev1.0/chatdev/phase.py)
- (3) Stopping, paper: a subtask ends after two unchanged code modifications or 10 rounds. On consensus, the assistant prefixes its answer with `<SOLUTION>` — [arXiv HTML](https://arxiv.org/html/2307.07924v5)
- (3) Stopping, code:
  - Each chat runs `for i in range(chat_turn_limit)` (asserted between 1 and 100) and breaks when either agent emits `<INFO>` or a terminated flag — [phase.py](https://raw.githubusercontent.com/OpenBMB/ChatDev/chatdev1.0/chatdev/phase.py)
  - CodeCompleteAll runs up to 10 cycles, until no unimplemented file remains — [ChatChainConfig.json](https://raw.githubusercontent.com/OpenBMB/ChatDev/chatdev1.0/CompanyConfig/Default/ChatChainConfig.json), [composed_phase.py](https://raw.githubusercontent.com/OpenBMB/ChatDev/chatdev1.0/chatdev/composed_phase.py)
  - **CodeReview** runs up to 3 cycles and stops when the string `"<INFO> Finished"` appears in the modification conclusion, a **self-declared done** — same sources
  - **Test** runs up to 3 cycles and stops when `exist_bugs_flag` is False — same sources
  - If the test report contains "ModuleNotFoundError", the test-modification chat is skipped with "nothing need to do" — [phase.py](https://raw.githubusercontent.com/OpenBMB/ChatDev/chatdev1.0/chatdev/phase.py)
- (3, code) How `exist_bugs` decides — [chat_env.py](https://raw.githubusercontent.com/OpenBMB/ChatDev/chatdev1.0/chatdev/chat_env.py):
  - It runs `python main.py`, sleeps 3 s, then kills the process if it is still running.
  - It reports a bug only if stderr contains "Traceback" (case-insensitive).
  - Empty stderr, or stderr without a traceback, counts as **no bug**.
  - The return code is read before `poll()`, so the `returncode == 0` branch is effectively dead.
  - In short, "tests pass" means **no crash with a traceback in the first 3 seconds**.
- (4) Measurable vs judgment work is split by phase. The reviewer does static review (e.g. unimplemented methods, missing imports). The tester relays compiler/runtime errors, which the programmer fixes — [arXiv HTML](https://arxiv.org/html/2307.07924v5). No unit tests are written. The only "measurable" check is the run-for-3-seconds test above.
- (5) Prompt-only: communicative dehallucination, where the assistant asks for details before answering; consensus tokens; role behaviour. Code-enforced: phase order, cycle caps, turn caps, the string-match breaks, and the stderr check — [arXiv HTML](https://arxiv.org/html/2307.07924v5), [composed_phase.py](https://raw.githubusercontent.com/OpenBMB/ChatDev/chatdev1.0/chatdev/composed_phase.py)
- (6) Failures, self-reported: agents implement simple, low-information-density logic and struggle with vague requirements, so the approach suits prototypes. Functionality, robustness and safety are not evaluated. "Method Not Implemented" is 34.85% of review discussions; "ModuleNotFound" is 45.76% of testing errors — [arXiv HTML](https://arxiv.org/html/2307.07924v5)
- (7) Results (SRDD, GPT-3.5): completeness 0.5600, executability 0.8800, consistency 0.8021, quality 0.3953, vs MetaGPT 0.4834 / 0.4145 / 0.7601 / 0.1523. Pairwise win vs MetaGPT is 57.08% with a GPT-4 judge and 88.00% with human judges. Average 22,949 tokens and 148 s per project — [arXiv HTML](https://arxiv.org/html/2307.07924v5)
- (7) Ablations: removing roles drops executability 0.88 to 0.58 and quality to 0.2212. Removing communicative dehallucination drops quality to 0.3094. Stopping after review vs after testing gives identical numbers: the "≤Testing" row equals full ChatDev, so the testing phase adds nothing measurable on these metrics — [arXiv HTML](https://arxiv.org/html/2307.07924v5)
- Repo status: ChatDev 1.x moved to the `chatdev1.0` branch on 7 Jan 2026. `main` is now ChatDev 2.0 (DevAll), a zero-code multi-agent platform. A human-in-the-loop mode (`--config "Human"`, the user acts as reviewer) and an incremental mode exist — [GitHub README](https://github.com/OpenBMB/ChatDev)

#### CAMEL (Li, Hammoud, Itani, Khizbullin, Ghanem). arXiv 2303.17760. **Published, NeurIPS 2023** (per arXiv comments). PDF https://arxiv.org/pdf/2303.17760
- (1) Roles: the AI user (instructs, plans), the AI assistant (executes), a task specifier (turns an idea into a concrete task), and an optional critic, AI or human, that selects among proposals — [arXiv HTML](https://arxiv.org/html/2303.17760v2)
- (2) Visibility: both chat agents see the full message history. The assistant also sees the new instruction. The task specifier sees the role descriptions and the idea — [arXiv HTML](https://arxiv.org/html/2303.17760v2)
- (3) Stopping: the user gives no instruction for 3 rounds; the assistant issues an instruction (role reversal detected); the user emits `<CAMEL_TASK_DONE>` (**self-declared**); a token limit is hit; or a **40-message cap** is reached, set for cost — [arXiv HTML](https://arxiv.org/html/2303.17760v2)
- (5) Prompt-only "inception prompting": "Never flip roles! Never instruct me!", a forced "Solution: ... Next request." format, honest refusal, and the done token. The paper does not say which termination checks are in code — [arXiv HTML](https://arxiv.org/html/2303.17760v2)
- (6) Failures reported: role flipping, the assistant repeating instructions, "flake replies" (vague promises to act), and **infinite loops of meaningless messages** (thanks or goodbyes). No frequencies are given — [arXiv HTML](https://arxiv.org/html/2303.17760v2)
- (7) Results: AI Society human eval, CAMEL wins 76.3% vs gpt-3.5-turbo 10.4%. Code domain, GPT-4 eval, wins 76.0% vs 24.0%. CAMEL-7B fine-tuned on the generated data reaches HumanEval pass@1 14.0% — [arXiv HTML](https://arxiv.org/html/2303.17760v2)

#### AgentVerse (Chen, Su, Zuo et al., 16+ authors, Tsinghua / BUPT / Tencent). arXiv 2308.10848. **Published, ICLR 2024.** PDF https://arxiv.org/pdf/2308.10848
- Venue: ICLR 2024 poster and proceedings — [ICLR proceedings](https://proceedings.iclr.cc/paper_files/paper/2024/hash/578e65cdee35d00c708d4c64bce32971-Abstract-Conference.html)
- (1) Roles: a recruiter generates expert roles. Decision-making is either horizontal (all agents share and refine, then aggregate) or vertical (one solver proposes, reviewers critique). Then action execution and an evaluator — [arXiv HTML](https://arxiv.org/html/2308.10848v3)
- (3) Stopping: in the vertical structure, refinement ends at reviewer consensus or after a set iteration count. If the evaluator judges the goal unmet, its feedback goes back to recruitment. Tool agents are capped at 10 ReAct steps. The **evaluator is an LLM by default**. For HumanEval with GPT-4, an extra agent writes unit tests and the results go to the evaluator — [arXiv HTML](https://arxiv.org/html/2308.10848v3)
- (6) Failures: with GPT-3.5, Group underperformed Solo on 2 of 3 reasoning tasks. Agents were swayed by incorrect feedback, about 10% of MGSM errors. More reviewers produced erroneous critiques, so math used 2 agents. In Minecraft, agents engaged in "destructive behaviours" such as destroying a village library — [arXiv HTML](https://arxiv.org/html/2308.10848v3)
- (7) HumanEval pass@1 (GPT-4): CoT 83.5, Solo 87.2, Group 89.0. GPT-3.5: 73.8 / 74.4 / 75.6. Tool use: 9 of 10 tasks vs 3 for single ReAct — [arXiv HTML](https://arxiv.org/html/2308.10848v3)

#### Self-collaboration code generation (Dong, Jiang, Jin, Li; Peking University). arXiv 2304.07590. **Published, ACM TOSEM** (journal named on the page). PDF https://arxiv.org/pdf/2304.07590
- (1, 2) Roles: the analyst decomposes the task and writes a plan without implementation detail; the coder writes and repairs code; the tester writes a report on functionality, readability and maintainability. They share a **blackboard**. Each prompt contains the role description, the team description and the requirement — [arXiv HTML](https://arxiv.org/html/2304.07590v3)
- (3) Stopping: up to n = 4 rounds, or earlier when the **tester declares no issues remain**, an LLM verdict — [arXiv HTML](https://arxiv.org/html/2304.07590v3)
- (4) The tester **does not execute code**: it "simulates" testing with the LLM. A variant with a compiler running the public HumanEval tests did not beat the three-role team — [arXiv HTML](https://arxiv.org/html/2304.07590v3)
- (6) Failures: tester errors often add exception handling that makes functions raise and fail tests. Iteration sometimes breaks correct edge-case code. Data contamination is suspected on MBPP — [arXiv HTML](https://arxiv.org/html/2304.07590v3)
- (7) GPT-3.5 pass@1: HumanEval 57.3 to 74.4; MBPP 52.2 to 68.2; HumanEval-ET 42.7 to 56.1. GPT-4 HumanEval: 67.7 to 90.2 — [arXiv HTML](https://arxiv.org/html/2304.07590v3)

#### AgentCoder (Huang, Zhang, Luck, Bu, Qing, Cui). arXiv 2312.13010. **Preprint** (no venue found). PDF https://arxiv.org/pdf/2312.13010
- (1, 2) Roles: the programmer (LLM), the test designer (LLM) and the test executor (**a Python script**, not an LLM). The test designer writes tests from the requirements **without seeing the code**, "to keep tests objective and avoid bias from incorrect code" — [arXiv HTML](https://arxiv.org/html/2312.13010v3)
- (3) Stopping: all generated tests pass, or the iteration budget runs out. The budget value is not stated; RQ3 evaluates up to 5 iterations — [arXiv HTML](https://arxiv.org/html/2312.13010v3)
- (4) Split vs merged:
  - Separate agents: tests correct against the canonical solution 87.8% (HumanEval) and 89.9% (MBPP) with GPT-3.5; line coverage 87.5% / 89.5%.
  - **One agent writing both**: test accuracy 61.0% / 51.8%, coverage 72.5% / 75.9%, pass@1 71.3% / 79.4% (vs 79.9% / 89.9% separated).
  - The authors attribute the gap to "tests being biased by the same agent's code" and to task distraction — [arXiv HTML](https://arxiv.org/html/2312.13010v3)
- (7) GPT-4 pass@1: HumanEval 96.3%, MBPP 91.8%. Tokens on HumanEval: 56.9K vs MetaGPT 138.2K, ChatDev 183.7K, AgentVerse 149.2K. Baselines are taken from the original papers, not re-run — [arXiv HTML](https://arxiv.org/html/2312.13010v3)

#### MapCoder (Islam, Ali, Parvez). arXiv 2405.11403. **Published, ACL 2024** (per the project README, a secondary source). PDF https://arxiv.org/pdf/2405.11403
- Venue: README says accepted at ACL 2024 — [search result, gitee mirror of README](https://gitee.com/thomastao/MapCoder)
- (1, 2) Roles and inputs — [arXiv HTML](https://arxiv.org/html/2405.11403v1):
  - Retrieval agent: self-generates k similar problems, plans and tutorials, with no external retriever.
  - Planning agent: writes one plan per exemplar, each with a **self-reported confidence score**.
  - Coding agent: sees the problem and one plan.
  - Debugging agent: sees the code, the sample I/O and the plan.
- (3) Stopping: plans are tried in confidence order. Code that **passes the problem's sample I/O** is returned. Otherwise up to t debug attempts are made, then the next plan; after k plans, the last code is returned. Defaults: k = t = 5 on HumanEval, 3 on the other benchmarks. For MBPP, one MBPP-ET test per problem is held out as sample I/O — [arXiv HTML](https://arxiv.org/html/2405.11403v1)
- (6) Limitations: high token and API-call cost; sample I/O may not cover all cases — [arXiv HTML](https://arxiv.org/html/2405.11403v1)
- (7) pass@1: HumanEval 93.9%, MBPP 83.1%, APPS 22.0%, CodeContests 28.5%, xCodeEval 45.3% — [arXiv HTML](https://arxiv.org/html/2405.11403v1)

#### CodeSim (MapCoder successor; Islam, Ali, Parvez). arXiv 2502.05664. **Published, NAACL 2025 Findings.** PDF https://arxiv.org/pdf/2502.05664
- Planning, coding and debugging agents. The plan is verified by **LLM step-by-step simulation** on sample I/O, and internal debugging uses the same simulation, "without relying on an external compiler". pass@1: HumanEval 95.1%, MBPP 90.7%, APPS 22%, CodeContests 29.1% — [arXiv](https://arxiv.org/abs/2502.05664)

#### Experiential Co-Learning, ECL (Qian, Dang, Li, Liu, Xie, Wang, Chen, Yang, Cong, Che, Liu, Sun). arXiv 2312.17025. **Published, ACL 2024 long (2024.acl-long.305).** PDF https://arxiv.org/pdf/2312.17025
- Venue: [ACL Anthology](https://preview.aclanthology.org/setup/2024.acl-long.305)
- Mechanism — [arXiv HTML](https://arxiv.org/html/2312.17025v3):
  - Co-tracking turns ChatDev trajectories into a task-execution graph, with identical code states merged by MD5.
  - Co-memorizing stores "shortcuts" (non-adjacent nodes whose score gain exceeds ε = 0.90).
  - Co-reasoning retrieves these as few-shot examples: instruction-to-solution pools for the assistant, solution-to-instruction pools for the instructor.
- Experience score: task similarity × solution similarity × a **binary compilation check**. This is a heuristic, not a learned reward. Maximum 5 rounds per phase — [arXiv HTML](https://arxiv.org/html/2312.17025v3)
- (7) Quality 0.7304 vs ChatDev 0.4267; executability 0.9650 vs 0.8800; duration 122.8 s vs 148.2 s. Consistency barely moves (0.7970 vs 0.7909) — [arXiv HTML](https://arxiv.org/html/2312.17025v3)
- (6) Same "simplest logic" problem with vague requirements; no robustness evaluation; the embedding-based consistency metric is coarse — [arXiv HTML](https://arxiv.org/html/2312.17025v3)

#### Iterative Experience Refinement, IER (Qian, Li, Dang et al.). arXiv 2405.04219. **Preprint** (no ACL listing found). PDF https://arxiv.org/pdf/2405.04219
- Successive vs cumulative experience pools, with heuristic elimination by information gain (ε = 0.95) and by use frequency (top 0.95 fractile). 930 of 8,053 experiences are kept, "11.54%" in the paper; the actual ratio is 11.55%. Quality: successive 0.6372, cumulative 0.6337, ECL 0.5775, ChatDev 0.4665. Duration is about 180 s vs 122.8 s for ECL. A bad batch can degrade the whole successive pool, and the hit ratio declines as the cumulative pool grows. One model, one dataset, proxy metrics only — [arXiv HTML](https://arxiv.org/html/2405.04219v1)

#### Cross-Team Collaboration, CTC (Du, Qian, Liu, Xie, Wang, Dang, Chen, Yang). arXiv 2406.08979. **Published, ACL 2025 Findings** (as "Multi-Agent Collaboration via Cross-Team Orchestration"). PDF https://arxiv.org/pdf/2406.08979
- Venue: ACL 2025 Findings per a web search that surfaced the ACL Anthology author listing ([ACL Anthology, Zihao Xie](https://aclanthology.org/people/zihao-xie/)). The anthology ID was not confirmed.
- Mechanism: 8 parallel ChatDev teams sync at key phases. Greedy pruning drops low-quality content, then hierarchical partitioning and greedy aggregation follow, done by a role-assigned agent listing strengths and drawbacks. Maximum 5 rounds per phase — [arXiv HTML](https://arxiv.org/html/2406.08979v1)
- (7) Quality 0.779 to 0.840 vs ChatDev; executability 0.813 to 0.928 — [arXiv HTML](https://arxiv.org/html/2406.08979v1)
- (6) Quality **declines beyond about 4 teams**. Diversity needed mixed temperatures. Pruning by imperfect metrics may discard creative solutions. Some ablations produced "I cannot process this task". Communication overhead grows with the number of teams — [arXiv HTML](https://arxiv.org/html/2406.08979v1)

#### Co-Saving (Qiu, Qian et al.). arXiv 2505.21898. **Preprint.** PDF https://arxiv.org/pdf/2505.21898
- A resource-aware ChatDev successor. "Shortcuts" learned from past successful trajectories skip redundant reasoning steps. Adds an emergency factor and a **forced termination mechanism to prevent resource exhaustion**. Reports -50.85% tokens and +10.06% code quality vs ChatDev on SRDD — [arXiv](https://arxiv.org/pdf/2505.21898)

#### EvoMAC (Hu, Cai, Du, Zhu, Liu, Yu, Hou, Tang, Chen). arXiv 2410.16946. **Published, ICLR 2025.** PDF https://arxiv.org/pdf/2410.16946
- Venue: [ICLR 2025 proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/39af4f2f9399122a14ccf95e2d2e7122-Abstract-Conference.html)
- (1) Teams — [arXiv HTML](https://arxiv.org/html/2410.16946v1):
  - Coding team: an organiser plus coders.
  - **Separate testing team**: writes unit tests, the "target proxy".
  - Updating team: a gradient agent reads the execution logs and judges each agent; an updating agent removes, rewrites or adds agents and rewires the workflow ("textual backpropagation").
  - The compiler runs the code against the tests.
- (3) Fixed K evolving iterations (Algorithm 1). No early-stop criterion is given — [arXiv HTML](https://arxiv.org/html/2410.16946v1)
- (4) Measurable work (tests) and code-writing are held by separate teams. The paper argues objective execution feedback avoids LLM self-critique bias — [arXiv HTML](https://arxiv.org/html/2410.16946v1)
- (7) rSDE-Bench (53 tasks, 616 tests): Website Basic 89.38%, Game Basic 77.54%. HumanEval 94.51% with GPT-4o-mini — [arXiv HTML](https://arxiv.org/html/2410.16946v1)
- (6) Game logic errors persisted across iterations and plateaued; no cost analysis — [arXiv HTML](https://arxiv.org/html/2410.16946v1)

#### AgileCoder (Nguyen, Chau, Nguyen, Bui). arXiv 2406.11912. **Preprint** ("work in progress"). PDF https://arxiv.org/pdf/2406.11912
- (1, 2) Roles and inputs — [arXiv HTML](https://arxiv.org/html/2406.11912v2):
  - Product Manager: writes the backlog and acceptance criteria.
  - Scrum Master: checks feasibility and **decides deliverability**.
  - Developer: sees only the code relevant to the current fix, plus cross-file context from a dynamic code dependency graph.
  - Senior Developer: static review against the backlog and acceptance criteria.
  - Tester: writes test suites, ordered by the graph's topological order.
- (3) Stopping: sprints repeat until the Scrum Master or PM judges the software ready, an **LLM verdict**; tests are not the stop condition. Average 1.64 sprints on ProjectDev — [arXiv HTML](https://arxiv.org/html/2406.11912v2)
- (7) HumanEval with GPT-3.5: 70.53 vs ChatDev 61.79 and MetaGPT 62.80. ProjectDev executability: 57.79% vs 32.79% and 7.73%. Cost about 36.8K tokens and $0.44 per run vs ChatDev $0.12. Removing the test suite costs 8.33 points on HumanEval; removing the graph drops executability to 23.38% and causes 11 context overflows — [arXiv HTML](https://arxiv.org/html/2406.11912v2)

#### MAGIS (Tao, Zhou, Wang, Zhang, Zhang, Cheng). arXiv 2403.17927. **Published, NeurIPS 2024.** PDF https://arxiv.org/pdf/2403.17927
- Roles: Manager, Repository Custodian, Developer, QA Engineer, for GitHub issue resolution. Resolves 13.94% of SWE-bench issues, about 8× direct GPT-4 — [arXiv](https://arxiv.org/abs/2403.17927); NeurIPS 2024 poster — [NeurIPS](https://neurips.cc/virtual/2024/poster/93481). 25.33% on SWE-bench Lite (appendix) — [search summary of arXiv PDF](https://arxiv.org/pdf/2403.17927)
- Gap: the QA agent's visibility and stop rule were not extracted.

#### CodeR (Chen, Lin, Zeng, Zan et al., 17 authors). arXiv 2406.01304. **Preprint.** PDF https://arxiv.org/pdf/2406.01304
- Multi-agent issue resolution with **pre-defined task graphs**. 28.33% on SWE-bench Lite with one submission per issue — [arXiv](https://arxiv.org/abs/2406.01304)

#### HyperAgent (Phan, Nguyen, Nguyen, Bui). arXiv 2409.16299. **Preprint** (v3, Sep 2025). PDF https://arxiv.org/pdf/2409.16299
- Planner, Navigator, Code Editor, Executor; SWE-bench, RepoExec, Defects4J. No numbers on the abstract page — [arXiv](https://arxiv.org/abs/2409.16299). Analysed as a failing system in MAST (see Q4).

#### Smaller and adjacent members
- **SoA**, Self-Organized Agents (Ishibashi, Nishimura). arXiv 2404.02183. Preprint. Agents multiply automatically with problem complexity; +5% pass@1 on HumanEval over a single agent — [arXiv](https://arxiv.org/abs/2404.02183). PDF https://arxiv.org/pdf/2404.02183
- **CodePori**. arXiv 2402.01411. Preprint. Agents for system design, code development, review, verification and test engineering. 89% on HumanEval; manually tested on 20 projects — [arXiv HTML](https://arxiv.org/html/2402.01411v2). PDF https://arxiv.org/pdf/2402.01411
- **CodeCoR**. arXiv 2501.07811. Preprint. Prompt, coding, test and repair agents; each generates several outputs and prunes the low-quality ones. Average pass@1 77.8% — [arXiv](https://arxiv.org/abs/2501.07811v1). PDF https://arxiv.org/pdf/2501.07811
- **PairCoder**. arXiv 2409.05001. Navigator (plans, selects, directs using execution feedback) and Driver (codes, tests, refines) — [awesomepapers summary of arXiv](https://awesomepapers.io/papers/2409.05001). A later ACL 2026 Findings paper of the same name has a different author list and framing: one model writes, the other reviews, roles swap when errors stall — [ACL Anthology preview](https://preview.aclanthology.org/ingest-acl/2026.findings-acl.149/). The relationship between the two is unresolved. PDF https://arxiv.org/pdf/2409.05001
- **ALMAS** (Tawosi, Ramani, Alamir, Liu). arXiv 2510.03463. Vision paper at the ASE 2025 MAS-GAIN workshop. Agents mapped to agile roles, plug-in to developer tools — [arXiv](https://arxiv.org/pdf/2510.03463), [ASE 2025](https://conf.researchr.org/details/ase-2025/mas-gain-2025-papers/3/ALMAS-an-Autonomous-LLM-based-Multi-Agent-Software-Engineering-Framework). PDF https://arxiv.org/pdf/2510.03463

#### 2025-2026 successors and studies
- **Agyn** (Benkovich, Valkov). arXiv 2602.01465. Preprint, Feb 2026. Agents for coordination, research, implementation and **review**, each with an isolated sandbox and structured channels. Methodology: analysis, task spec, PR creation, iterative review, no human. **72.2% on SWE-bench 500** (post hoc); stopping rule not stated — [arXiv](https://arxiv.org/abs/2602.01465). PDF https://arxiv.org/pdf/2602.01465
- **AgentForge** (Kumar, Ali, Ahmed, Ali, Usman). arXiv 2604.13120. Preprint, Apr 2026. Planner, Coder, Tester, Debugger, Critic, with shared memory. **"Every code change must survive sandboxed execution before propagation"** (mandatory Docker). 40.0% on SWE-bench Lite, +26 to 28 points over single agents. Ablations show execution feedback and role decomposition each contribute — [arXiv](https://arxiv.org/abs/2604.13120). PDF https://arxiv.org/pdf/2604.13120. (Not to be confused with AgentForge 2608.04148, a role-playing *learning* platform for humans — [arXiv](https://arxiv.org/abs/2608.04148).)
- **Shen et al., role-based MAS optimised with textual feedback**. arXiv 2505.16086. Preprint, May 2025 (Amazon authors). An AgentVerse-style vertical system: a recruiter draws roles from a ChatDev-derived pool; a Programmer solver; **two reviewers, one review iteration**. Functionality, robustness and coverage are scored by a **GPT-4 judge**; style by pycodestyle. Online group one-pass optimisation: functionality 6.90 to 7.26, coverage 0.32 to 7.81, style violations 6.62 to 3.24. The optimised prompts show the solver had to be told to implement *all* requirements and the reviewer to detail missing functionality — [arXiv HTML](https://arxiv.org/html/2505.16086v2). PDF https://arxiv.org/pdf/2505.16086
- **Ha et al., classical process models as coordination**. arXiv 2509.13942. Preprint. Waterfall, V-Model and Agile; 11 projects × 4 GPT variants = 132 runs. Waterfall was most efficient, V-Model most verbose, Agile highest quality at the highest cost — [arXiv](https://arxiv.org/abs/2509.13942). PDF https://arxiv.org/pdf/2509.13942
- **Shafin et al., process models for class-level generation**. arXiv 2511.09794. Preprint. Waterfall-style Requirement → Design → Implementation → Testing on ClassEval (100 tasks). It **reduced functional correctness by 37.8% (GPT-4o-mini) and 39.8% (DeepSeek-Chat)** but improved Claude-3.5-Haiku by 9.5%. Structural errors fell; semantic and validation errors rose; the Testing stage had the strongest effect, including new reasoning failures — [arXiv](https://arxiv.org/abs/2511.09794). PDF https://arxiv.org/pdf/2511.09794
- **Donato et al., role-based generation at repository scale**. arXiv 2607.04212. **Published, IEEE Software 2026** (special issue on engineering agentic systems). 12 Java repositories, GPT-5. Compile rates: LLM-only 31%, sequential agentic 22%, reflexive agentic (ChatDev 2.0) 40%. Outputs were partial skeletons covering about 1 to 25% of the original. The reflexive loop "uses no compiler, stderr, or test feedback". Role assignments vary between runs because the planner defines them dynamically — [arXiv HTML](https://arxiv.org/html/2607.04212v1). PDF https://arxiv.org/pdf/2607.04212
- Surveys (pointers): He, Treude, Lo, LLM-based MAS for SE, arXiv 2404.04834 — [arXiv](https://arxiv.org/pdf/2404.04834). Design-patterns study, arXiv 2511.08475: Role-Based Cooperation is the most used of 16 patterns — [arXiv](https://arxiv.org/abs/2511.08475). Multi-vocal review of MAS for code generation, arXiv 2604.16321 — [arXiv](https://arxiv.org/pdf/2604.16321). Not downloaded; outside "systems".

### Inferences
- The family's information design converges on **artifact-only hand-offs**. MetaGPT passes structured docs via subscription; ChatDev passes only solutions across phases; AgileCoder passes graph-selected code slices. History-stripping is the norm across phases, but within a phase dialogue history is fully shared, as in ChatDev's role-play chats and CAMEL.
- Read as contract theory, the stronger systems make the "principal's signal" an executed test written by a party that never saw the code (AgentCoder, EvoMAC, AgentForge). The weaker ones let the producer's counterpart issue a cheap-talk verdict ("<INFO> Finished", "YES", "no issues remain").

### Gaps
- ChatDev 2.0 (DevAll) internals and stop rules were not inspected.
- MAGIS, CodeR, HyperAgent and Agyn reviewer visibility and stop rules were not extracted from full text.
- No sensitivity numbers on round caps were found for any system.

## Q1. In each system, what is the actual stopping rule, in code? Is it a test, a reviewer, a round count, or a self-declared "done"?

### Takeaway
Almost every system has a **hard round or budget cap** as the backstop. The "early" exit is a self-declared or LLM-judged signal more often than a real test. Only AgentCoder, MapCoder (sample I/O), EvoMAC (fixed K with tests as feedback, not as stop) and AgentForge (sandbox gate) tie progress to executed code. ChatDev's "test pass" is "no Traceback in stderr within 3 s".

### Cited Findings
| System | Early exit | Hard backstop | Source |
|---|---|---|---|
| CAMEL | `<CAMEL_TASK_DONE>` from AI user (self-declared); also no instruction for 3 rounds, or role reversal | 40 messages; token limit | [arXiv HTML](https://arxiv.org/html/2303.17760v2) |
| MetaGPT (code) | all roles idle; Engineer summary passes if LLM reply contains "YES"; QA loop on run results | `n_round` (default 3); `NoMoneyException` at budget; QA `test_round_allowed=5`; paper: 3 debug retries | [team.py](https://raw.githubusercontent.com/geekan/MetaGPT/main/metagpt/team.py), [engineer.py](https://raw.githubusercontent.com/geekan/MetaGPT/main/metagpt/roles/engineer.py), [qa_engineer.py](https://raw.githubusercontent.com/geekan/MetaGPT/main/metagpt/roles/qa_engineer.py), [paper](https://arxiv.org/html/2308.00352v7) |
| ChatDev 1.0 (code) | chat: `<INFO>` token; review: `"<INFO> Finished"` in conclusion (self-declared); test: `exist_bugs` False (no "Traceback" in stderr after 3 s run); completion: no unimplemented file | `chat_turn_limit` (≤100); CodeComplete 10 cycles; CodeReview 3; Test 3; paper: 10 rounds or 2 unchanged modifications | [phase.py](https://raw.githubusercontent.com/OpenBMB/ChatDev/chatdev1.0/chatdev/phase.py), [composed_phase.py](https://raw.githubusercontent.com/OpenBMB/ChatDev/chatdev1.0/chatdev/composed_phase.py), [chat_env.py](https://raw.githubusercontent.com/OpenBMB/ChatDev/chatdev1.0/chatdev/chat_env.py), [ChatChainConfig](https://raw.githubusercontent.com/OpenBMB/ChatDev/chatdev1.0/CompanyConfig/Default/ChatChainConfig.json) |
| ECL / IER / CTC | inherits ChatDev | 5 rounds per phase | [ECL](https://arxiv.org/html/2312.17025v3), [CTC](https://arxiv.org/html/2406.08979v1) |
| Co-Saving | shortcuts | "forced termination mechanism to prevent resource exhaustion" | [arXiv](https://arxiv.org/pdf/2505.21898) |
| AgentVerse | reviewer consensus; LLM evaluator judges goal met | set iteration count; 10 ReAct steps for tools | [arXiv HTML](https://arxiv.org/html/2308.10848v3) |
| Self-collaboration | tester (LLM, no execution) says no issues | n = 4 rounds | [arXiv HTML](https://arxiv.org/html/2304.07590v3) |
| AgentCoder | all independently written tests pass (script executor) | iteration budget (up to 5 evaluated) | [arXiv HTML](https://arxiv.org/html/2312.13010v3) |
| MapCoder | sample I/O passes | k plans × t debug rounds (5×5 or 3×3) | [arXiv HTML](https://arxiv.org/html/2405.11403v1) |
| CodeSim | LLM-simulated I/O trace | not extracted | [arXiv](https://arxiv.org/abs/2502.05664) |
| EvoMAC | none stated | fixed K evolving iterations | [arXiv HTML](https://arxiv.org/html/2410.16946v1) |
| AgileCoder | Scrum Master / PM judge deliverable (LLM) | conversation exchange limit; no fixed sprint count (mean 1.64) | [arXiv HTML](https://arxiv.org/html/2406.11912v2) |
| Shen et al. 2025 | — | one review iteration, 2 reviewers | [arXiv HTML](https://arxiv.org/html/2505.16086v2) |
| AgentForge 2026 | change must pass sandboxed execution before propagating | not stated | [arXiv](https://arxiv.org/abs/2604.13120) |
| Donato 2026 (ChatDev 2.0 reflexive) | — | 6 to 10 iterations observed; no compiler or test feedback | [arXiv HTML](https://arxiv.org/html/2607.04212v1) |

- ChatDev's `exist_bugs` treats a still-running process, empty stderr, or non-traceback stderr as "no bugs". The return-code check is dead code — [chat_env.py](https://raw.githubusercontent.com/OpenBMB/ChatDev/chatdev1.0/chatdev/chat_env.py)
- ChatDev's own ablation: stopping after review ("≤Review") vs the full pipeline changes quality 0.3717 to 0.3953. "≤Testing" equals the full system exactly — [arXiv HTML](https://arxiv.org/html/2307.07924v5)
- MetaGPT's budget exception propagates uncaught and skips `env.archive` — [team.py](https://raw.githubusercontent.com/geekan/MetaGPT/main/metagpt/team.py)

### Inferences
- ChatDev's executed check is weak: it is a 3-second smoke run, and GUI or long-running programs pass by default. Combined with self-declared review completion, this matches MAST's ChatDev chess example, where the system "passed verification" while accepting invalid moves (see Q4).
- MetaGPT's `_is_pass` substring check would also count a reply containing "YES" anywhere, e.g. in a quoted to-do list, as a pass. This is a fragile parse of an LLM verdict. It is inferred from the described code, not from a reported incident.

### Gaps
- Default `chat_turn_limit` per phase in ChatDev's PhaseConfig.json was not fetched.
- MetaGPT's current-release defaults for `use_code_review` and `max_auto_summarize_code` were not confirmed.
- CodeSim's and HyperAgent's stop logic in code was not inspected.

## Q2. Where a reviewer or critic agent exists, does it see the builder's explanation or only the artifact?

### Takeaway
Mixed. MetaGPT's QA reads the code document and structured fields, not the Engineer's message text. ChatDev's reviewer is given the codes plus task and ideas, but reviews inside a dialogue with the programmer, so it sees the programmer's turns. AgentCoder's test designer is the cleanest case: it sees only the requirement, never the code. No paper explicitly studies hiding the builder's explanation from the reviewer.

### Cited Findings
- MetaGPT QA uses `code_doc` and `msg.instruct_content` and loads code from the repo. It does not use the Engineer's message content — [qa_engineer.py](https://raw.githubusercontent.com/geekan/MetaGPT/main/metagpt/roles/qa_engineer.py). The paper's subscription filter restricts each role to role-relevant documents — [arXiv HTML](https://arxiv.org/html/2308.00352v7)
- ChatDev CodeReviewComment gets `task, modality, ideas, language, codes, images`, with no programmer-reasoning field. The dialogue runs through `RolePlaying`, so prior turns are in the exchange — [phase.py](https://raw.githubusercontent.com/OpenBMB/ChatDev/chatdev1.0/chatdev/phase.py). Across phases only solutions pass forward — [arXiv HTML](https://arxiv.org/html/2307.07924v5)
- CAMEL: both agents see the full message history — [arXiv HTML](https://arxiv.org/html/2303.17760v2)
- Self-collaboration: all roles share a blackboard — [arXiv HTML](https://arxiv.org/html/2304.07590v3)
- AgentCoder: the test designer works from the requirements "without seeing the whole code snippet" — [arXiv HTML](https://arxiv.org/html/2312.13010v3)
- AgileCoder's Senior Developer sees the code plus the backlog and acceptance criteria — [arXiv HTML](https://arxiv.org/html/2406.11912v2)
- MapCoder's debugger sees the code, the sample I/O **and the plan**, i.e. the builder's rationale — [arXiv HTML](https://arxiv.org/html/2405.11403v1)
- EvoMAC's gradient agent reads execution logs and per-agent subtask assignments — [arXiv HTML](https://arxiv.org/html/2410.16946v1)
- AgentVerse's evaluator receives the initial problem and the group's decisions — [arXiv HTML](https://arxiv.org/html/2308.10848v3)

### Inferences
- MetaGPT's document-only routing is the closest the family gets to an "artifact-only" reviewer by design. ChatDev's dual-agent chat structurally exposes the reviewer to the builder's persuasion within the phase.

### Gaps
- No ablation was found that compares a reviewer that sees the explanation against one that sees only the artifact, in any of these systems.

## Q3. Which systems let the same agent write and judge, and did that cause reported problems?

### Takeaway
Same-agent write-and-judge appears in MetaGPT's paper text (the Engineer writes and runs its own tests), in AgentCoder's single-agent ablation, and implicitly in every self-declared "done". The clearest quantified harm comes from AgentCoder: when one agent writes both code and tests, test accuracy falls from about 88-90% to 51-61% and pass@1 drops about 9-10 points. Self-collaboration and Shafin et al. show the reverse risk: an LLM tester that judges without execution, or a testing stage, adds new reasoning failures.

### Cited Findings
- AgentCoder RQ6, one agent writing code and tests: test accuracy 61.0% / 51.8% and pass@1 71.3% / 79.4%, vs 87.8% / 89.9% accuracy and 79.9% / 89.9% pass@1 when split. Blamed on tests "biased by the same agent's code" — [arXiv HTML](https://arxiv.org/html/2312.13010v3)
- MetaGPT's paper places test writing and execution in the Engineer (Section 3.3) and also in the QA Engineer (Section 3.1); in code, QA writes them — [arXiv HTML](https://arxiv.org/html/2308.00352v7), [qa_engineer.py](https://raw.githubusercontent.com/geekan/MetaGPT/main/metagpt/roles/qa_engineer.py). MetaGPT-generated tests were 79.3% accurate on HumanEval vs AgentCoder's 89.6% (GPT-4) — [AgentCoder HTML](https://arxiv.org/html/2312.13010v3)
- ChatDev review completion is declared by the review/modification chat itself (`"<INFO> Finished"`) — [composed_phase.py](https://raw.githubusercontent.com/OpenBMB/ChatDev/chatdev1.0/chatdev/composed_phase.py)
- In CAMEL, the AI user, who directs the work, declares `<CAMEL_TASK_DONE>` — [arXiv HTML](https://arxiv.org/html/2303.17760v2)
- Self-collaboration's non-executing LLM tester introduced errors (added exception handling that fails tests) and broke correct edge cases — [arXiv HTML](https://arxiv.org/html/2304.07590v3)
- EvoMAC explicitly separates the testing team from the coding team, arguing that objective execution feedback avoids self-critique bias — [arXiv HTML](https://arxiv.org/html/2410.16946v1)
- AgentVerse's agents were swayed by incorrect reviewer feedback (about 10% of MGSM errors); more reviewers produced more erroneous critiques — [arXiv HTML](https://arxiv.org/html/2308.10848v3)

### Inferences
- The evidence favours splitting *measurable* work: tests written by an agent blind to the code, and executed by a script. Splitting *judgment* work, an LLM reviewer or tester without execution, gives weaker and sometimes negative returns (Self-collaboration, AgentVerse GPT-3.5, Shafin et al.).

### Gaps
- No paper in this family measured reward hacking such as weakening tests or deleting asserts by a coder that can edit tests. Whether the coder can modify the tests was not checked for MetaGPT or AgileCoder.

## Q4. What do the follow-up and failure-analysis papers say went wrong in these systems?

### Takeaway
The independent evidence is negative. ChatDev reaches only about 33% correctness on ProgramDev, and its verifier passes programs that violate the spec. Process-heavy waterfall pipelines can cut correctness by about 38-40% on class-level tasks for some models. At repository scale, role teams produce partial skeletons with low compile rates. Prompt or role fixes give single-digit gains, and adding a real objective-level verifier gives the largest one (+15.6 points). Cost blow-ups and loop pathologies are reported in the systems' own papers.

### Cited Findings
- MAST (Cemri, Pan, Yang et al.), arXiv 2503.13657, **published at NeurIPS 2025** ([NeurIPS](https://neurips.cc/virtual/2025/poster/121528)). It annotated traces of MetaGPT, ChatDev, HyperAgent, AppWorld and AG2 — [arXiv HTML](https://arxiv.org/html/2503.13657v2):
  - ChatDev is about 33.33% correct on ProgramDev.
  - Failure categories: specification issues 41.77%, inter-agent misalignment 36.94%, task verification 21.30%.
  - Selected modes: step repetition 17.14%; reasoning-action mismatch 13.98%; fail to ask for clarification 11.65%; unaware of termination conditions 9.82%; premature termination 7.82%; no or incomplete verification 6.82%; incorrect verification 6.66%; role-spec disobedience 0.5%.
  - ChatDev chess example: the program passed all verification rounds yet accepted invalid moves, because the verifier checked only compilation and comments.
  - HyperAgent: the Navigator acted without telling the Planner, and the Planner repeated responses.
  - Interventions on ChatDev with GPT-4o: role-spec fixes +9.4%; adding a high-level objective verification step +15.6 points. The authors conclude simple fixes are insufficient.
  - PDF https://arxiv.org/pdf/2503.13657 (downloaded as a pointer; the failure-survey area belongs to another researcher)
- CAMEL itself reports role flipping, instruction repetition, flake replies and infinite loops of thanks or goodbyes — [arXiv HTML](https://arxiv.org/html/2303.17760v2)
- Cost:
  - Token use per HumanEval run: ChatDev 183.7K, MetaGPT 138.2K, AgentVerse 149.2K, AgentCoder 56.9K — [AgentCoder](https://arxiv.org/html/2312.13010v3)
  - MapCoder's own limitation is a "large number of tokens" — [MapCoder](https://arxiv.org/html/2405.11403v1)
  - AgileCoder costs $0.44 per run vs ChatDev $0.12 — [AgileCoder](https://arxiv.org/html/2406.11912v2)
  - Co-Saving exists to cut ChatDev tokens by 50.85% — [Co-Saving](https://arxiv.org/pdf/2505.21898)
  - CTC quality drops beyond about 4 teams — [CTC](https://arxiv.org/html/2406.08979v1)
- "Simplest logic" / hollow completion: ChatDev, ECL and CTC all report that agents implement minimal logic under vague requirements, e.g. rectangles for sprites or hard-coded data — [ChatDev](https://arxiv.org/html/2307.07924v5), [ECL](https://arxiv.org/html/2312.17025v3), [CTC](https://arxiv.org/html/2406.08979v1). "Method Not Implemented" is 34.85% of ChatDev review discussions — [ChatDev](https://arxiv.org/html/2307.07924v5)
- Shafin et al. 2025: a Waterfall multi-agent process cut ClassEval correctness 37.8% (GPT-4o-mini) and 39.8% (DeepSeek-Chat) and raised semantic and validation errors. Testing introduced new reasoning failures — [arXiv](https://arxiv.org/abs/2511.09794)
- Donato et al. 2026: on 12 Java repositories, outputs were partial skeletons; compile rates were 22% (sequential agentic) and 40% (ChatDev 2.0 reflexive) vs 31% LLM-only. There was over-engineering on simple projects and missing error handling and security. The reflexive loop had no compiler or test feedback — [arXiv HTML](https://arxiv.org/html/2607.04212v1)
- Ha et al. 2025: process choice trades quality against cost; Agile is highest quality but most expensive — [arXiv](https://arxiv.org/abs/2509.13942)
- Shen et al. 2025: unoptimised role prompts under-implement requirements, and reviewers under-report missing functionality. Fixing them needed per-agent prompt rewriting from failure explanations — [arXiv HTML](https://arxiv.org/html/2505.16086v2)
- Evaluation weakness: EvoMAC reports that ChatDev-style consistency and quality metrics correlate only 0.2583 and 0.3041 with human judgement, vs 0.9922 for its test-based accuracy — [arXiv HTML](https://arxiv.org/html/2410.16946v1). AgentCoder's baselines are copied from original papers, not re-run — [arXiv HTML](https://arxiv.org/html/2312.13010v3)

### Inferences
- The recurring failure is **hallucinated completion passing a weak gate**. Self-declared "Finished", LLM "YES" verdicts and 3-second smoke runs all let skeletal code through. MAST's largest single intervention gain (+15.6) came from adding an objective-level verifier, which is consistent with this.
- Headline numbers for the SRDD-era systems (ChatDev, ECL, IER, CTC, Co-Saving) rest on proxy metrics that a later paper found poorly correlated with humans. They are weak evidence of functional correctness.

### Gaps
- No independent reproduction of MetaGPT's or ChatDev's headline numbers was found.
- No paper reports gaming in the strict sense (e.g. a coder editing tests to pass) for this family. Every "gaming-like" evidence found is verifier weakness, not adversarial manipulation.
- The MAST per-system failure-rate figure (Figure 1 and Figure 4 numbers for MetaGPT and HyperAgent) was not in the extracted text.
