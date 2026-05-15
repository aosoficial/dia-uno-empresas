# Tools — what a Company Brain needs

This repo explains tool categories, not a single mandatory stack.

You can implement Company Brain System with many tools. The important part is the role each tool plays.

## 1. Memory / knowledge graph

Role: store durable company knowledge and relationships.

Examples of what it stores:

- people;
- projects;
- decisions;
- risks;
- processes;
- entities;
- relationships;
- source references.

Public concept: **Company Memory**.

Implementation options:

- graph database;
- markdown vault;
- vector-aware knowledge base;
- custom internal memory layer.

## 2. Structured database

Role: store operational records with clear fields.

Examples:

- tasks;
- customers;
- receipts;
- decisions;
- agent runs;
- approvals;
- metrics.

Implementation options:

- Supabase;
- Postgres;
- Airtable;
- Notion database;
- internal app database.

## 3. Semantic search / embeddings

Role: find relevant context by meaning, not just exact keywords.

Examples:

- retrieve similar decisions;
- find related customer problems;
- surface prior receipts;
- connect repeated issues.

Implementation options:

- Voyage;
- OpenAI embeddings;
- local embeddings;
- hosted vector database.

## 4. Execution board / control plane

Role: coordinate work between humans and agents.

Examples:

- tasks;
- owners;
- states;
- approvals;
- comments;
- evidence;
- review queue.

Implementation options:

- Paperclip-like control plane;
- Linear;
- GitHub Issues;
- Trello;
- Jira;
- custom internal app.

## 5. Agent runtime

Role: define how an agent behaves.

It should include:

- identity;
- mission;
- permissions;
- tools;
- memory policy;
- handoff rules;
- receipt rules;
- escalation rules.

## 6. Document/source repository

Role: keep the method versioned and reviewable.

Implementation options:

- GitHub repo;
- GitLab repo;
- internal git server;
- versioned document system.

## Tool selection rule

Do not start by buying tools.

Start by answering:

1. What must the company remember?
2. What must agents be allowed to do?
3. What actions need human approval?
4. What evidence must exist after work?
5. What review cadence will improve the system?

If you need help choosing or connecting tools, follow [`docs/08-get-help-from-libera.md`](08-get-help-from-libera.md).
