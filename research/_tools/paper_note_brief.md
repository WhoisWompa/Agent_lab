# Paper note brief

You write one paper note for a research vault. Read the template and the paper text, then write one markdown file. Do nothing else: no searching, no other files, no edits elsewhere.

Template (the exact shape, headings fixed): the `_TEMPLATE.md` in the notes folder you were given.

Write the note to: <the notes folder you were given>\<YYYY-MM> <short title>.md
- YYYY-MM is the paper's date, from the arXiv id or dateline in the text. If only a year is findable, use YYYY alone.
- <short title> is the paper's title shortened to its main name, no colon, no subtitle, like the other files in that folder (e.g. "2023-06 Judging LLM-as-a-judge with MT-Bench and Chatbot Arena.md").
- If a file with that name already exists, add " (2)" before ".md" rather than overwrite.

Frontmatter: all the template's fields, plus three after `category`:
  pdf: <the Source PDF path you were given, as given>
  folder: [<the folder chain you were given, as given>]
  topics: [<every topic from research/topics.md whose definition the paper satisfies>]
`category` is one of the six listed in the template; pick the best fit. Topics follow the rules in `research/topics.md`: the definition decides, two or three is normal, and a new topic is proposed (not written) only when none fits.

WHO READS THIS AND WHY. The reader will never open the paper. They want two things: the paper's main idea (the problem it attacks and the solution it proposes) and its limitations. They do NOT want to know how the experiments were conducted: no dataset construction, no request counts, no prompt formats, no statistical-test machinery, no per-model result tables. But every judgment in the note must carry its reason or number right next to it. "The argument is weak" is useless; "a 0.60 confidence from the model is close to a coin flip, and 30% of such verdicts flip under a cosmetic cue" is what is wanted. If the paper gives the reason, state it; if it gives the number, quote it; if it gives neither, say the claim is unsupported in the paper.

Sections, keep the template's headings exactly, fill them like this:
- One line: what it does, one sentence.
- Method: the problem the paper attacks, and the idea or solution it proposes: what is new, what it assumes, and why it should work. The mechanism, not the procedure. If the method itself is a statistical or algorithmic construction, explain that construction, since that is the idea.
- Evaluated on: short. Only the results that carry the paper's claims, written as claim then evidence (e.g. "Stops with a third of the samples at the same error rate: X vs Y on Z"). Three to six bullets. No setup description.
- Limitations admitted by the authors: each bullet is one limitation plus why it matters or what evidence shows it, in one or two sentences. Skip boilerplate limitations that do not touch the claims.
- Limitations found by others: leave the heading with nothing under it (you have only this paper).
- What it leaves untried: one to three bullets, the obvious next step the paper does not take, and why it matters.

End the body with `## Topics` and one `[[Topic - <name>]]` link per topic in `topics:`, in order.

Length: 400 to 700 words in the body. Do not invent numbers. If a number is not in the text, do not write it. If the text is long, read it in parts with offset/limit until the end; do not stop after the first part. When done, reply with only: the file path you wrote, and the first-line summary.
