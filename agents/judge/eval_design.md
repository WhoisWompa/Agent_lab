# Evaluation design notes

Working notes for how the judge builds and grades evaluations. The six
practices from the industry overview are all covered; the later sections
refine the earlier ones (error/warning severities replace the weights in the first
examples).

## Vocabulary

| Word | Meaning here |
|---|---|
| Scenario | One set-up situation: the starting state (fake inbox, fake calendar, fake files, whatever the target agent works on) plus the request typed to the agent. |
| Trajectory | What the agent actually did when run on a scenario: every tool call, its arguments, its result, in order. Comes from the trace. |
| Reply | The final line the agent printed. |
| Criterion | One yes-or-no question asked about the reply or the trajectory. |
| Rubric | The list of criteria for one scenario, each with a weight. |
| Test set | The scenarios and rubrics that are run on every version of the target agent. |

A scenario and a trajectory are not subsets of each other. The scenario is the
input. The trajectory is the output. The rubric sits between them and says what
the trajectory and reply should look like.

## Binary criteria, not a graded scale

The school-style grid (column 1 no understanding, column 2 understanding,
column 3 can apply, column 4 can perform) is not used. Level scales are
unreliable: two graders disagree on 3 versus 4, a model grader drifts with
prompt wording, and a single number says nothing about what to fix.

Instead every scenario has six to fifteen yes-or-no questions. The score is the
fraction passed, weighted. Each question names one concrete observable thing.

A good criterion can be applied by a careful stranger just by looking.
"Mentions the 14-day refund window" is good. "Handles the refund policy
correctly" is a graded scale in disguise and is not allowed.

Faults to avoid:

- Compound criteria ("lists both invoices and their due dates" is two checks).
- Hidden reference ("gives the right answer" with the right answer not written next to it).
- Unobservable intent ("understands the user's goal"; write "asks which account before transferring" instead).
- No negative criteria. Most real failures are things that should not appear. Every rubric has some "does not" lines.

## Criteria over the trajectory, not just the reply

A wrong trajectory can produce a right reply by luck. Reply-only criteria miss
this. So every rubric has two blocks: criteria on the reply and criteria on the
trajectory.

Example, target agent `ledger`, request "what do I owe people this week".
Starting state: dentist invoice due Thursday in the inbox, promise to send Sam
the slides in the calendar, rent paid Monday in the bank feed.

| # | Criterion | Checked on | Weight |
|---|---|---|---|
| 1 | Lists the dentist invoice due Thursday | reply | 3 |
| 2 | Lists the promise to send Sam the slides | reply | 3 |
| 3 | Does not list the rent | reply | 3 |
| 4 | Gives a due date for every item listed | reply | 1 |
| 5 | Reply is under 150 words | reply | 1 |
| 6 | Called the calendar tool before composing the answer | trajectory | 2 |
| 7 | Called the inbox tool with a date range covering this week, not all time | trajectory | 1 |
| 8 | Called the bank feed before deciding what is unpaid | trajectory | 2 |
| 9 | Did not call any send or reply tool | trajectory | 3 |

An agent that guesses the right reply from the inbox alone passes 1 to 5 and
fails 6 and 8. The score shows the right reply was not earned.

Trajectory criteria are usually cheaper than reply criteria: tool calls are
structured data, so they are checked by code that walks the call list.

## Who answers a criterion

The shape of the question (yes or no) and the thing that answers it are
separate choices. In order of preference:

1. Code. Word counts, presence of a tool call, arguments of a tool call, exact strings, end state of files. Deterministic, free, never wrong about what it checks.
2. A model reading the reply or the trace. Used only where code cannot, such as "does not list the rent" when the wording varies. This is the only place "LLM as a judge" enters: as the answerer of a narrow yes-or-no question, never as the author of a 1 to 5 score.
3. A human. For the few criteria that need taste, and for checking the model answerer.

## The judge generating scenarios

The judge may invent scenarios to attack the target agent from angles a human
did not think of. Two consequences:

- To write trajectory criteria the judge must know the target agent's tools and what a sound use of them looks like. Pointing the judge at an agent means giving it that, not just the agent's name.
- A judge that invents a scenario also invents what correct looks like for it, and may get that wrong. Model-generated scenarios are good at finding breaks and unreliable at certifying passes. So: the judge generates and runs; failures are surfaced to the user; the user reads the trace and decides whether the agent was wrong or the judge was wrong; only then does the scenario and its rubric join the permanent test set. The permanent set is what runs on every version. The judge's inventions are a search process feeding it.

This is the refinement loop in the agent's summary: each round the judge looks at where its tests missed or misjudged. "Misjudged" is the user catching the judge.

## Criteria per scenario, not a global rubric

A global rubric asks the same questions of every scenario: accurate, complete,
concise, safe. Those are templates. "Complete" means "mentions the dentist
invoice and the slides" in one scenario and something else in the next, so the
grader has to work out what it means each time, and that working-out is where
grading goes wrong.

An instance rubric is the template filled in: the answer key for this one
scenario, naming the facts of its starting state. It is written when the
scenario is written, by whoever set up the state and knows the answer. Grading
is then only checking lines.

Plainly: deterministic checks on what the run produced, plus a check that the
reply says what it was meant to say. The reply check is a list of facts the
reply must contain or avoid, never a comparison against one reference text,
because wording changes run to run and a text match would fail good replies.

A scenario file carries state, request and rubric together:

```
scenario: owe_this_week_rent_paid
state:
  inbox: dentist invoice, due Thursday
  calendar: "send Sam the slides" on Wednesday
  bank: rent paid Monday
request: what do I owe people this week
rubric:
  - lists dentist invoice due Thursday        (reply, w3)
  - lists slides for Sam                       (reply, w3)
  - does not list rent                         (reply, w3)
  - called bank feed before answering          (trajectory, w2)
  - no send or reply tool called               (trajectory, w3)
```

The rubric is bound to the state. Flip the state so rent is unpaid and the
third line becomes "lists the rent due Friday". Variants made by changing one
fact at a time are a cheap way to grow the test set and are where agents
break, since they test whether the agent looked rather than memorised the
common case.

The global list survives only as a short checklist of dimensions (facts right,
nothing invented, nothing missed, boundaries respected, right tools used) used
when writing a new scenario's rubric, and as labels for reporting aggregates
across the set.

For the judge: an invented scenario must come with state and rubric together,
and each criterion should carry its reason ("does not list the rent, because
the bank feed shows it paid Monday") so the user can check the judge's
reasoning when reviewing a failure. "Reply is accurate" is not a criterion.

## Deterministic graders wherever possible

For each line on the answer key, look at the thing itself instead of asking a
model to read the reply about it. "Renamed the three files by date" is checked
by listing the folder, not by reading "Done, I renamed them". "Checked the bank
feed" is checked by finding the bank tool in the log, not by reading "I checked
your bank".

Every criterion is sorted into a layer, in this order of preference:

| Layer | What is looked at | Who answers |
|---|---|---|
| End state | Files, data, queues the agent changed | Code |
| Trajectory | The tool-call log from the trace in `logs/` | Code |
| Prose | The reply text | String check if wording is stable, else a model |

Code is free, gives the same answer every run, and is believed when it fails.
A model costs a call per criterion per scenario per run and wobbles, so the
wobble must be confined to the few prose lines. A change in a coded line is a
real change. In the ledger example five of nine lines are pure code, three are
code with a model fallback, one needs a model. That ratio is typical; an agent
that writes rather than reads moves even more into the end-state layer.

The judge writes the check once, when it creates the scenario, and stores it
next to the criterion. Later runs only execute it. The judge's model cost is
spent at authoring time, not grading time.

Checks are not fresh code. They are a fixed set of shapes with parameters:

| Shape | Parameters |
|---|---|
| tool called | tool name |
| tool not called | tool name |
| tool argument matches | tool name, argument, expected value |
| tool A before tool B | two tool names |
| reply contains | string or pattern |
| reply does not contain | string or pattern |
| reply length under | number |
| file exists / file matches | path, expected content |

The judge picks a shape and fills the blanks. Reviewable at a glance, no
model-written code executing in the loop, and a criterion that fits no shape is
a signal: it belongs to the prose layer, or the scenario state was not set up
well enough to expose the fact elsewhere, in which case fix the scenario rather
than accept a model grader. Fresh code is kept for end-state checks that are
genuinely scenario-specific, usually a line or two against a fake folder or
database the judge built.

Consequences for how scenarios and target agents are built:

- The starting state must be constructible from a file: fake inbox, calendar, folder, database, created before the run and thrown away after. An agent that only talks to the real service cannot be graded this way.
- The trace in `logs/` is the trajectory. The judge reads it after the run.
- Tool arguments should be structured (a date range field, not a free-text query), or argument checks are impossible.

## Pairwise comparison for what the key cannot express

For things with no right answer, such as whether a reply reads well, do not
score one reply out of 5. Show two replies side by side and ask which is
better. People and models disagree widely on absolute scores and mostly agree
on which of two is better.

Used after the answer key, only among replies that passed it. Two replies from
the same scenario and same starting state: old version against new, or new run
against a reference reply the user approved earlier. Result is a tally (wins,
losses, ties), never a score. Rules: show each pair in both orders and treat
disagreement as a tie; never tell the grader which is new; watch for the
grader rewarding length.

Same data format as RLHF preference pairs, different use: here nothing is
trained, the pairs only measure whether a change helped.

Least important practice for this lab. It looks at the reply only, so it
matters in proportion to how much of the agent's worth is in prose: almost
nothing for `ledger`, whose reply is a short list; a lot for
`research_partner`, whose reports are the product. With a personal test set of
tens of scenarios the tally is coarse: clearly better, clearly worse, or cannot
tell. The grader is the user, not a model. The judge's part is small: keep the
approved reference reply per scenario, show new reply against reference in
random order, record the pick, and promote the new reply to reference when the
user says so. Skipped entirely for agents with short factual replies.

## The answer key is written from failures, not from theory

A rubric written before any run lists what one imagines matters (accurate,
complete, polite) and misses what the agent actually does wrong (opens the
calendar with the wrong year, answers last turn's question). Criteria only
become known by looking at outputs, and they keep changing as one looks
(criteria drift, from "Who Validates the Validators"). So: look first, write
second, expect to rewrite.

The order at the start, when no scenarios exist:

1. The agent runs on real requests. The base writes a trace per run.
2. Each trace is read, reply and tool calls, and gets one free-form sentence: "fine" or what went wrong.
3. After a few dozen, the sentences are sorted into piles. A pile with more than one or two entries is a failure mode.
4. Each failure mode becomes one criterion with a check shape. "Bank feed never opened, paid items listed" becomes "bank feed called before answering", shape: tool called.
5. The runs where it happened become scenarios: freeze that day's state into a file, keep the request, attach the new criterion. Real failures make the best scenarios.

From then on, two things alternate: the scenarios run after every change, and
new traces keep being read, because the next failure mode is one the current
key does not catch. The usual advice is a hundred traces before the first
rubric and twenty or thirty per round after.

### The judge does the reading

In this lab the judge stands in for the week of normal use: it runs the
vetted scenarios, reads the traces, groups failures by criterion, writes a
one-line note per trace that no criterion caught, sorts those notes into
piles, and brings the piles to the user with counts and trace ids. The user
says which piles are real. The judge turns each confirmed pile into a criterion
with a check shape and freezes the traces it came from into scenarios. The
judge sorts; the user decides. A judge-found failure is a lead, not a verdict,
until the user has read the trace: simulated users are wrong often enough that
benchmarks using them report a visible share of "failures" that were the
simulated user's fault.

The goal is a floor: the target agent is usable before a human touches it.
The vetted scenarios with their keys are the floor; the judge's proposals are
how it rises.

### Request variants, generated once

One scenario keeps one frozen state and one answer key, and carries several
ways of asking: terse, chatty, with a typo, general question then specific,
a detail given up front or withheld. Different models phrase differently, so
the judge rotates models when generating variants. The variation is in the
request only; the key must stay valid for every variant ("what did I pay last
month" is a different scenario, not a variant, and a generating model will
drift into that kind).

Variants are generated once, when the scenario is created, stored in the
scenario file, vetted with the rest, then fixed. Each run of a scenario is N
runs, one per variant, all graded by the same key. Reproducible, cheap, every
failure replayable. Live model rotation mid-conversation is only worth it for
a multi-turn target agent where the judge must improvise replies (the research
partner, not the ledger).

```
scenario: owe_this_week_rent_paid
state: ...
requests:
  - what do I owe people this week
  - anything I still need to pay or hand over before friday?
  - owe anyone anything? this wk
rubric: ...
```

Failures are grouped by criterion and by variant. A failure on one variant
only is itself a finding: the agent is sensitive to phrasing.

Model rotation on the grading side belongs only to prose criteria: two models
answer the same yes-or-no line, and a disagreement flags that line for the
user. Coded checks need none.

## Validating the grader

Lines on the key that a model grades can be graded wrong. Coded lines skip
this section; code cannot misread.

For each model-graded line, the user answers a sample of past replies yes or
no, the model answers the same sample, and the two columns are compared. The
line is trusted only when they agree on nearly all of them. Twenty to fifty
replies per line is enough. The two disagreement directions are tracked
separately: the model failing what the user would pass is annoying; the model
passing what the user would fail is dangerous, because it hides real bugs.

Where they disagree, the fix is one of: reword the line ("does not list the
rent" became "does not list the rent as owed" after the model failed replies
saying rent was already paid); add the disagreeing reply with the user's
verdict as an example inside the line's grading instructions; or split the
line in two because the disagreement shows it was asking two things.

Critique shadowing is where the grading instruction comes from: the user's
free-form comments on a batch of replies, turned into the instruction with a
few of them kept as examples, so the model copies how the user judges rather
than guessing.

Redo the check whenever the grading model changes, a line is reworded, or the
target agent's replies change style enough that old examples no longer look
like current output.

### How it runs in the judge

For a model-graded line the judge gives its yes or no; the user answers
agree or disagree, with an optional sentence. The user is agreeing with the
judge's verdict on the line, not grading the agent's reply directly, which
keeps the answer binary and about the grader. A disagreement without a
sentence lowers the line's trust count. A disagreement with a sentence
triggers one of the three fixes above, and the judge says which it applied.

Not every verdict is shown every round. The judge asks about a line that is
new, just reworded, or on which two rotated grading models disagreed. A line
that has agreed with the user many times in a row stops asking until something
changes. Each model-graded line keeps its labelled examples and its agreement
count; when a scenario result looks odd, the first question is whether the
failing line is a trusted one.

## Grading and reporting

No single score, anywhere. From the key come counts: per scenario, which
lines failed; per criterion, the pass rate across all runs. Those two tables
are the result, and a change is judged by comparing the tables before and
after.

Whether the target agent is usable is a gate. Each line is an *error*
(failure makes the reply wrong: listed the rent, called send) or a *warning*
(quality: under 150 words, due dates given). A scenario passes only if every
error line passes on every request variant. Warnings are reported, never
gate. The
agent is usable when every vetted scenario passes. This replaces the numeric
weights in the earlier examples.

Human feedback enters only where the key cannot reach: vetting proposed
criteria and scenarios, agree or disagree on model-graded verdicts, the pick in
pairwise for prose-heavy agents. Never a score; a yes, a no or a pick, with an
optional sentence that feeds the next round of criteria the way free-form
trace notes do.

The judge's report per round: the two tables, the failing traces with ids,
and its proposals.
