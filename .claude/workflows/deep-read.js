export const meta = {
  name: 'deep-read-run',
  description: 'Deep read of one paper: the deep reader reads it in full and names its references, the librarian checks which exist, searchers find the missing ones, readers summarise them, the deep reader writes the report',
  whenToUse: 'Launched by the deep-read skill with args {paper, date}. paper is the paper note path, e.g. notes/Paper - Reflexion.md.',
  phases: [
    { title: 'Paper', detail: 'full text, note upgraded, references' },
    { title: 'Vault', detail: 'which references already have notes' },
    { title: 'Search', detail: 'missing references found on arXiv' },
    { title: 'Read', detail: 'reference abstracts into notes' },
    { title: 'Report', detail: 'Cites and the report' },
    { title: 'File', detail: 'research note and indexes' },
  ],
}

if (!args || !args.paper || !args.date) throw new Error('args.paper and args.date are required')
if (args.dryRun) return { status: 'dry-run' }

const BATCH = 5
const paper = args.paper
const date = args.date

const REF = { type: 'object', properties: {
  title: { type: 'string' }, authors: { type: 'string' }, year: { type: 'string' },
  arxiv_id: { type: 'string', description: 'Empty if the reference gives none' },
  why: { type: 'string', description: 'Why the paper needs it' },
}, required: ['title', 'authors', 'year', 'arxiv_id', 'why'] }

const DEEP1 = {
  type: 'object',
  properties: { note: { type: 'string' }, title: { type: 'string' }, references: { type: 'array', items: REF } },
  required: ['note', 'title', 'references'],
}

const CHECK = {
  type: 'object',
  properties: {
    found: { type: 'array', items: { type: 'object', properties: {
      title: { type: 'string' }, path: { type: 'string' }, sentence: { type: 'string' },
    }, required: ['title', 'path', 'sentence'] } },
    missing: { type: 'array', items: REF },
  },
  required: ['found', 'missing'],
}

const SEARCH = {
  type: 'object',
  properties: { candidates: { type: 'array', items: { type: 'object', properties: {
    kind: { type: 'string', enum: ['paper', 'repo'] }, title: { type: 'string' }, url: { type: 'string' }, why: { type: 'string' },
  }, required: ['kind', 'title', 'url', 'why'] } } },
  required: ['candidates'],
}

const READ = {
  type: 'object',
  properties: { items: { type: 'array', items: { type: 'object', properties: {
    kind: { type: 'string', enum: ['paper', 'repo'] }, title: { type: 'string' }, url: { type: 'string' },
    note: { type: 'string' }, summary: { type: 'string' }, relevance: { type: 'string' },
  }, required: ['kind', 'title', 'url', 'note', 'summary', 'relevance'] } } },
  required: ['items'],
}

const DEEP2 = {
  type: 'object',
  properties: { report: { type: 'string' }, opened: { type: 'array', items: { type: 'string' } } },
  required: ['report', 'opened'],
}

const chunk = (xs, n) => Array.from({ length: Math.ceil(xs.length / n) }, (_, i) => xs.slice(i * n, i * n + n))

// --- Call 1: the paper -----------------------------------------------------
phase('Paper')
const deep = await agent(
  `Call 1. Paper note: ${paper}\nDate: ${date}`,
  { agentType: 'deep-reader', schema: DEEP1, label: 'deep: paper' },
)
if (!deep) throw new Error('deep reader returned nothing')
const paperTitle = deep.note.replace(/^.*Paper - /, '').replace(/\.md$/, '')
log(`${deep.references.length} references kept`)

// --- Vault: which references exist ------------------------------------------
phase('Vault')
const check = await agent(
  `Job 2: check.\n\nReferences:\n${JSON.stringify(deep.references, null, 2)}`,
  { agentType: 'research-librarian', schema: CHECK, label: 'librarian: check' },
)
if (!check) throw new Error('librarian returned nothing')
log(`${check.found.length} in the vault, ${check.missing.length} missing`)

// --- Search and read the missing ones ---------------------------------------
const located = (await parallel(check.missing.map((r, i) => () => agent(
  `Find one paper by title.\nTitle: ${r.title}\nAuthors: ${r.authors}\nYear: ${r.year}${r.arxiv_id ? `\narXiv id: ${r.arxiv_id}` : ''}\n\nReturn that paper as the only candidate if you find it on arXiv, else an empty list.`,
  { agentType: 'research-searcher', schema: SEARCH, phase: 'Search', label: `find ${i + 1}` },
)))).filter(Boolean).flatMap((r) => r.candidates.slice(0, 1))
const unresolved = check.missing.filter((r) => !located.some((c) => c.title.toLowerCase().includes(r.title.toLowerCase().slice(0, 30))))
if (unresolved.length) log(`${unresolved.length} references not found on arXiv`)

const read = (await parallel(chunk(located, BATCH).map((batch, i) => () => agent(
  `Problem: these are references of a deep read of [[Paper - ${paperTitle}]]. Judge relevance to that paper. Add a Cited by line linking it.\n\nDate: ${date}\nResearch note: Research - Deep read of ${paperTitle}\n\nCandidates:\n${JSON.stringify(batch, null, 2)}`,
  { agentType: 'research-reader', schema: READ, phase: 'Read', label: `read ${i + 1}` },
)))).filter(Boolean).flatMap((r) => r.items)

// --- Call 2: the report ------------------------------------------------------
phase('Report')
const refs = [
  ...check.found.map((f) => `- ${f.path} — ${f.sentence}`),
  ...read.filter((r) => r.note).map((r) => `- ${r.note} — ${r.summary}`),
  ...unresolved.map((r) => `- (no note) ${r.title}, ${r.authors}, ${r.year}`),
].join('\n')
const report = await agent(
  `Call 2. Paper note: ${deep.note}\n\nReference notes:\n${refs || '(none)'}`,
  { agentType: 'deep-reader', schema: DEEP2, label: 'deep: report' },
)
if (!report) throw new Error('deep reader returned nothing')

// --- File ------------------------------------------------------------------
phase('File')
await agent(
  [
    'Job 3: file. This is a deep read: kind: deep, one wave, verdict stop.',
    `Research note: Research - Deep read of ${paperTitle}\nProblem: a deep read of [[Paper - ${paperTitle}]]\nDate: ${date}\nRound: 1`,
    `References already in the vault:\n${JSON.stringify(check.found, null, 2)}`,
    `Items read:\n${JSON.stringify(read, null, 2)}`,
    `Not found on arXiv:\n${JSON.stringify(unresolved, null, 2)}`,
    'Question list: (none; a deep read has no question list)',
    `Lead verdict: stop\nReasoning: the report is written.\nQuestion to the user: (none)\nSynthesis:\n${report.report}`,
    `Also: the paper note was upgraded to depth full; update its index line in Papers Index and its topic notes if its summary changed.`,
  ].join('\n\n'),
  { agentType: 'research-librarian', label: 'file' },
)

return {
  status: 'stop',
  note: `Research - Deep read of ${paperTitle}`,
  references: { found: check.found.length, read: read.length, unresolved: unresolved.length },
  report: report.report,
}
