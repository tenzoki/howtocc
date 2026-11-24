---
name: howtocc
description: What Claude can and cannot do, and which feature, plan or working method fits a task. Use for questions about Claude, Cowork, Claude Code, skills, connectors, plans, limits, data protection.
---

# howtocc

This skill answers questions about using Claude: what it can do, where it becomes unreliable, which building block fits a task, what a plan includes, and how to work with it well. The knowledge comes from the guide *Apply Claude: Fundamentals, fields of application, and working models* by Kai Stalmann (qantr GmbH, November 2026), stored chapter by chapter in `references/`.

Use it when someone asks, for example:

- "Can Claude do X?" or "Why can't Claude do X?"
- "Should I use a project, a skill, a connector, Cowork or Claude Code for this?"
- "Which plan do I need?" or "What does Pro include?"
- "How do I get better results?" or "Why is the answer so generic?"
- "Is it safe to let Claude do X?" or "What happens to my data?"
- "How do I install Claude Code?" or "How do I share a skill with my team?"

## How to answer

1. **Find the chapter.** Use the index below to pick the one or two reference files that cover the question, and read them before answering. Read only what the question needs; the files are long. Do not answer from memory when a file covers the question, because the guide is more specific and more recent than training knowledge on these products.
2. **Answer the question that was asked.** Lead with the answer: yes, no, or which option. Then give the condition that matters most (plan, platform, beta status, a setting that must be on). Reply in the language the person wrote in; the reference files are in English.
3. **Name the limit along with the capability.** The guide pairs almost every capability with a limit or a check. Where one applies, pass it on. A person who learns that Claude summarises web sources should also learn that the sources need opening before the information is reused.
4. **Recommend one building block.** For "what should I use" questions, name one building block and the reason, and mention an alternative only if the choice depends on something the person has not said.
5. **Cite the section.** Give the section number, such as "(section 8.3)", so the person can read further in the guide.
6. **Say when the guide is silent.** If no file covers the question, say so, and then answer from other knowledge or a web search, marked as not from the guide.

## Dates and changing facts

The guide describes the state of November 2026 (Claude Code 2.1.319). Two kinds of content age differently:

- **Durable:** how the model works, the limits of reliability, how deeply to check a result, how to write a prompt, how to restrict an agent. These can be stated plainly.
- **Changing:** prices, usage limits, plan contents, model versions, beta and preview labels, regional availability, announced dates. State these with "as of November 2026". If a decision depends on one of them (buying a plan, choosing a deployment path, relying on a retention rule) and a web search or documentation tool is available, check the current Anthropic page first. If the current source disagrees with the guide, use the current source and say that the guide is out of date on this point.

What the running environment shows also outranks the guide. If the model answering is newer than the versions the guide lists, or a feature is visibly present or absent in this session, say what is true here.

## Index of the reference files

| File | Sections | Read it for |
|---|---|---|
| `references/00-getting-started.md` | 0.1, 0.2 | Where to find Claude, creating an account, the Free plan, paying, installing Claude Code on macOS, Windows and Linux, Claude as an installation helper |
| `references/01-fundamentals.md` | 1.1 to 1.3 | How the model works, the context window, what Claude is good at, the full list of building blocks with their status, which building block fits which requirement |
| `references/02-deployment-decision.md` | 2.1, 2.2 | Types of error and countermeasures, how deeply to check a result, what media Claude can and cannot produce, plans and prices, usage limits, model series and effort levels, interfaces, basic settings, regional availability |
| `references/03-knowledge-generation.md` | 3.1 to 3.5 | Web search and Research, summarising with evidence, analysing data and documents, file formats and size limits, charts and dashboards, comparing options for a decision, learning and teaching, academic research and Claude Science |
| `references/04-content-creation.md` | 4.1 to 4.3 | The path from idea to publication, drafting, proofreading, style, literary and advertising texts, watermarking and labelling, Claude Docs, Slides, Design and Motion, artifact or file, sharing artifacts |
| `references/05-software-development.md` | 5.1 to 5.3 | Claude Code interfaces and permission modes, exploring a codebase, bug fixes, features and refactoring, tests, `/code-review`, Claude Security, CLAUDE.md, hooks and their limits, sandbox, managed settings, CI, script mode, worktrees |
| `references/06-operational-processes.md` | 6.1 to 6.4 | Strategy, marketing and sales, customer service with benchmark figures and protection rules, office work (mail, calendar, minutes, data maintenance), industry offerings, the Usage Policy requirements for high-risk recommendations |
| `references/07-personal-matters.md` | 7.1, 7.2 | Personal advice on health, career, relationships and money, when a professional is needed, excessive agreement (sycophancy), dependence, warning signs, crisis support |
| `references/08-output-quality.md` | 8.1 to 8.4 | Structure of a prompt, examples, voice, images and files as input, diagnosing a poor result, iteration, personal and project instructions, project knowledge, Memory, search in past chats, connectors and how to control them |
| `references/09-standardisation-delegation.md` | 9.1 to 9.4 | Prompt templates, skills and plugins, chains, agents, sub-agents and agent teams, scheduled tasks and `/loop`, Cowork, Claude in Chrome, Computer Use, Claude Duet, approval modes |
| `references/10-integration.md` | 10.1 to 10.3 | Claude in Microsoft 365, Google Workspace, Slack (Claude Tag) and Microsoft Copilot, Messages API, tool use, Agent SDK, Managed Agents, MCP servers and clients, custom connectors, cloud providers |
| `references/11-responsibility-organisation.md` | 11.1 to 11.3 | Model training and retention, administration (SSO, roles, audit), prompt injection and safeguards for agents, sharing conversations, projects, skills and plugins, learning path and courses, EU AI Act Article 4, announced product changes |

Numbers in brackets inside the files, such as (8.3), are cross-references to these sections.

## Where to look by kind of question

| Question | Start with |
|---|---|
| Can Claude do X at all? | 1.2 for the building block and its status, 2.1 for limits and media |
| Which building block for my task? | 1.3, then the chapter of the building block |
| Which plan, what does it cost, why did I hit a limit? | 2.2, and 0.1 for the Free plan and payment |
| Can I trust this result? How much should I check? | 2.1 |
| Why is my result poor? | 8.2, then 8.1 |
| How does Claude know about my project or my preferences? | 8.3 |
| How do I connect a service? | 8.4, and 10.3 for a custom connector |
| How do I make a task repeatable or automatic? | 9.1 for skills, 9.3 for schedules, 9.2 for agents |
| How do I let Claude act on my computer or in the browser? | 9.4, and 11.1 for the risks |
| How do I work with code? | Chapter 5, and 0.2 for installation |
| How do I build Claude into my own software? | 10.2, 10.3 |
| What happens to my data? What can an administrator control? | 11.1 |
| How do we share work in a team? | 11.2 |
| A field of work (research, writing, sales, support, office, an industry) | The matching section in chapters 3, 4 and 6 |
| Health, money, relationships, emotional strain | Chapter 7, and 6.4 if a recommendation affects another person |

## The core in brief

These points hold across the guide and can be used without opening a file.

**Two sources of knowledge.** Claude draws on fixed training knowledge and on the context window. It cannot know anything that is in neither. Current and private information has to be put into the context window: as a file, through a web search, or through a connector. Every conversation starts empty unless a project, Memory or personal instructions add content.

**The text is probable, not verified.** Wrong information sounds as certain as correct information. Facts, figures and quotations need a source or a cross-check. Claude may also report an action as done that did not happen, so check the result where it was meant to land.

**When a task is suitable.** A task suits Claude if it is work on text, code or data, if the material is in the training knowledge or fits in the context window, and if the result can be checked.

**How deeply to check.** Ask two things: is an error noticed, and what does it cost?

| | Error noticed at once | Error hardly noticed |
|---|---|---|
| **Error costs a lot** | Use, and check the result in full: testable code, analyses that can be recalculated, texts read before sending | Only with evidence and expert review: legal, health and financial questions in individual cases, facts and quotations without a source to hand |
| **Error costs little** | Use freely: ideas, outlines, drafts, rewording, first explanations | Use, and check samples: summaries of long documents, research overviews, sorting and tagging |

If the expert review is missing in the costly, hard-to-notice case, the task is not suitable for Claude.

**Choosing a building block.**

| Requirement | Building block |
|---|---|
| Include material once | File in the chat |
| Knowledge and rules for one undertaking | Project |
| Preferences for all conversations | Personal instructions (written by the person), Memory (created by Claude) |
| Current information | Web search, or Research for in-depth questions |
| Data from a service, or acting in it | Connector |
| The same procedure every time | Skill |
| Share skills and connectors as a bundle | Plugin |
| A result to edit or share | Artifact, or a file for Office programs |
| A multi-step task | Cowork |
| A task on a schedule | Scheduled task |
| Work on source code | Claude Code |

A prompt that is repeated becomes a skill. What applies to a project permanently goes into the project. A skill that runs reliably can be delegated.

**Keep the context window clear.** Accuracy drops as the window fills. Include only relevant material, enable only the connectors that are needed, and start a new conversation for a new topic. After two failed corrections, a new conversation with a more precise brief works better than a third attempt.

**What Claude does not produce.** Photos, illustrations, realistic video and voice clones. It produces diagrams, vector graphics, layouts and code-based animations.

**Agreement is a risk.** Claude knows only the questioner's account and tends to agree with it. Asking for the strongest objections, in a new conversation, gives a better check than asking for confirmation.

**Acting agents.** Prompt injection needs two things at once: Claude reads third-party content, and Claude can take far-reaching action. Limit one of them. Sending, paying and deleting stay subject to approval.
