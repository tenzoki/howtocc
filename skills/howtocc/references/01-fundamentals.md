# Chapter 1: Fundamentals and Core Components

From the guide *Apply Claude* by Kai Stalmann, as of November 2026. Numbers in brackets such as (8.3) refer to sections of the guide; the index in SKILL.md says which file holds each chapter.

## 1.1 Operating Principle and Performance Profile

Explains how the language model works and its context window (the amount of text it takes into account at any one time), and uses this to determine the types of tasks for which Claude is suitable.

**Operating Principle**

The name Claude refers to two things: a family of language models (currently the Haiku, Sonnet, Opus and Fable series) and the assistant as which these models operate within Anthropic’s applications. You can choose which model responds (2.2). The model generates each response token by token (a token is a word or part of a word) as a probable continuation of the text so far. In doing so, it draws on two sources: the fixed training knowledge and the content of the context window.

Figure 1 as text: the language model draws on two sources. (a) Training knowledge: fixed, cannot be changed, as of June 2026, no internal data. (b) The context window: working memory, controllable, around 1 million tokens. The context window holds instructions (personal, in the project, from skills), knowledge provided (files, project knowledge, Memory), tool results (web search, connectors, code execution), the conversation history and the current prompt. The response is generated token by token and becomes part of the conversation history.

*Figure 1: The two sources of knowledge for a response. Claude cannot know anything that is not contained in either the training knowledge or the context window.*

| Feature| Implications for use
| :---:| :---:
| The generated text is probable, but has not been verified.| Incorrect information sounds just as certain as correct information. Facts, figures and quotations require a source or cross-checking (2.1).
| Training knowledge ends in June 2026 and does not contain any internal data.| Current and personal information must be added to the context window: as a file, via a web search or via a connector.
| Claude can only see what is in the context window.| Every conversation starts empty, unless projects, Memory or personal instructions insert content (8.3).
| The continuation is selected, not calculated deterministically.| The same question yields answers phrased differently. Consistent results require specifications to be defined in templates or skills (9.1).
| Before responding, the model reflects in intermediate steps (Thinking); the level of effort is adjustable.| Challenging tasks benefit from a higher level of effort, though this consumes time and usage quotas (2.2).

**Context window**

- **Size:** Current models can handle up to 1 million tokens, roughly 2,000 pages of text.
- **Content:** Everything is included: instructions, files, images, tool outputs, the entire history and the resulting response, including the thought process. Tools and connectors take up a particularly large amount of space.
- **Filling:** As the amount of content grows, accuracy and recall decrease. When approaching the limit, Claude automatically summarises previous messages (in paid plans with code execution enabled), though details may be lost.

Hence the working rule: only include relevant material and start a new conversation for a new topic.

**Performance profile**

A task is suitable if it can be defined as work on text, code or data; if the necessary material is contained in the training knowledge or fits within the context window; and if the result can be verified.

| Strength| Typical tasks| Explored in depth in
| :---:| :---:| :---:
| Understanding and summarising| summarising, explaining, answering questions about documents, extracting information| 3.1, 3.2
| Weighing up| comparing, evaluating, formulating counter-arguments| 3.3
| Drafting and reworking| drafting texts and outlines, translating, adapting tone and format| Chapter 4
| Programming| reading, writing and checking code| Chapter 5
| Working with tools| researching, creating files, executing processes| Chapter 9

Where reliability ends is covered in 2.1.

## 1.2 List of core modules

Defines each core module and lists the sub-sections that provide further detail (as at 04/11/2026). The ‘Status’ column indicates pre-release versions and unconfirmed items; an empty field means that no restriction is documented. Section 2.2 covers which tariff includes which module.

| Module| Function| Status| In-depth
| :---:| :---:| :---:| :---:
| **A. Model**| | |
| Model series| Haiku, Sonnet, Opus and Fable differ in performance, speed and cost. Fable is the generally available version of Mythos, which is reserved for verified organisations.| | 1.1, 2.2
| Cognitive effort and thinking| Two separate settings determine how thoroughly the model thinks before responding; greater effort consumes time and usage quotas.| | 1.1, 2.2
| Context window| This limits the amount of text the model considers at any one time.| | 1.1, 8.3
| Input and output formats| The model accepts text and images and outputs text; other formats are generated via tools such as code execution.| |  2.1, 8.1
| **B. Commands and Control**| | |
| Prompt| A prompt is a single command issued to the model.| | 8.1
| Personal Instructions| These apply permanently to all conversations within an account.| | 8.3
| Memory| Claude remembers topics from previous conversations; the entries can be edited individually.| | 8.3
| Styles| They define tone and format as selectable presets.| No longer documented in the help pages| 4.2
| Learning mode| Claude guides you like a tutor by asking follow-up questions.| Documented only for Claude for Education| 3.4
| Incognito chats| These conversations are not saved in the history or in Memory.| | 11.1
| **C. Knowledge and Information**| | |
| Projects| They bring together knowledge, instructions and files for a specific task.| | 8.3
| File and image analysis| Claude reads uploaded documents, spreadsheets and images.| | 3.2
| Web search| Claude bases its answers on current web sources.| | 3.1
| Research| Claude conducts research across multiple sources in several steps.| | 3.1
| Searching in previous chats| Claude retrieves content from previous conversations.| | 8.3
| **D. Integration**| | |
| Connectors| They connect Claude to external services and their data.| | 8.4
| MCP (Model Context Protocol)| This open standard governs how models integrate with tools and data; connectors are based on it.| Integration via the API (MCP connector): Beta| 8.4, 10.3
| Directory| Anthropic’s catalogue lists connectors and plugins for adding.| | 8.4, 11.2
| Interactive apps (MCP apps)| Third-party applications can be used directly within the chat.| | 8.4
| Desktop extensions| These provide local MCP packages for the desktop app.| Deprecated directory entries| 8.4
| **E. Results**| | |
| Code execution and file creation| Claude executes code in a sandboxed environment to create or edit files.| | 4.3
| Artifacts| Results appear as standalone objects in a panel next to the chat.| | 4.3
| Claude Docs, Slides and Design| These artefact templates are used for documents, presentations and visual designs.| |  4.3
| Charts and diagrams| Visualisations appear interactively in the chat and in Cowork.| Beta| 3.2
| Dashboards| They display live data from sources such as BigQuery or Salesforce.| Beta| 3.2
| Claude Motion| It generates animations from code and is not a video model.| Beta| 4.3
| **F. Reuse and extension**| | |
| Skills| They store instructions for recurring tasks.| | 9.1
| Plugins| They bundle skills, connectors, commands, agents (systems that carry out sub-steps autonomously) and hooks (automatically triggered processes). Agents and hooks from a plugin remain inactive in chat.| | 9.1, 11.2
| **G. Action and Delegation**| | |
| Cowork| Claude carries out multi-step tasks autonomously using files and applications.| Web and mobile: in Team Beta, in Enterprise upon approval| 9.4
| Scheduled tasks| Tasks run on a timed and recurring basis.| | 9.3
| Computer Use| Claude operates the screen and programs.| Desktop app: Beta; Claude Code: Research Preview| 9.4
| Claude in Chrome| Claude acts as an agent within the Chrome browser.| | 9.4
| Claude Duet| This agent takes action on its own initiative, for example with a morning briefing and regular checks.| Research Preview, USA only| 9.4
| Claude Code| Claude works directly on the source code: in the terminal, in the IDE (integrated development environment), in the desktop app or in the cloud.| | 5.1
| CLAUDE.md and Hooks| The CLAUDE.md file defines project rules; hooks are custom actions that Claude Code automatically executes when certain events occur.| |  5.3
| Code Review| Multiple agents review code changes before they are committed.| | 5.2
| Subagents, Agent Teams, Dynamic Workflows| They distribute work across multiple agents running in parallel.| Agent Teams: experimental| 9.2
| **H. Access and integration methods**| | |
| Web, desktop and mobile| The Claude app is used directly via these interfaces.| Linux: Beta| 2.2
| Voice mode| The conversation is conducted verbally; Claude responds with pre-recorded voices.| Beta| 8.1
| Office add-ins| Claude works in Excel, PowerPoint, Word and Outlook.| Outlook: Beta| 10.1
| Claude for Google Workspace| Claude works in Docs, Sheets and Slides.| Beta| 10.1
| Claude Tag| Teams can address Claude via @mentions, initially in Slack; the organisation manages access.| Public Beta| 10.1
| Claude in Microsoft Copilot| Microsoft uses Claude models in Copilot and operates this integration itself.| Disabled by default in the EU, EFTA and the UK; enabled in Word, Excel and PowerPoint depending on the tenant| 10.1
| Messages API and Tool Use| Your own software uses Claude via the programming interface; Claude calls functions of this software via Tool Use.| | 10.2
| Platform Services| Additional API functions reduce costs and control output, including batch processing, caching of recurring prompt sections (Prompt Caching) and structured outputs.| Stable; availability varies by platform| 10.2
| Agent SDK| Claude Code’s agent technology is available as a program library.| | 10.2
| Managed Agents| Agents run on an infrastructure managed by Anthropic.| Beta| 10.2
| Cloud deployment| Claude is also available via Amazon Bedrock, Claude Platform on AWS, Google Cloud and Microsoft Foundry.| | 10.3
| **I. Organisation and product offerings**| | |
| Pricing plans| Free, Pro, Max, Ultra, Team, Enterprise, Education and Government define the scope of features and usage limits.| | 2.2
| Administration| Roles and permissions, single sign-on (SSO), audit logs and retention policies govern operations within organisations.| | 11.1
| Claude Science| This working environment is intended for research, including clinical and medical research, but not for clinical or diagnostic use.| Beta| 3.5
| Claude Security| It continuously scans code for security vulnerabilities.| Public Beta| 5.2
| Industry-specific packages| There are dedicated packages for finance, legal, healthcare, life sciences, public sector and charitable organisations.| varies by package| 6.4

## 1.3 Interplay of the building blocks

Shows how task, knowledge, integration, result, reuse and delegation interlock, and which building block suits which task.

The building blocks fulfil six functions within a workflow: three determine what the model encounters, one determines the form of the result, and two make the process repeatable and autonomous.

Figure 2 as text: Task (prompt, instructions), Knowledge (projects, files, Memory, web search) and Integration (connectors to services and data) feed the language model, which reads the context window. The Result is a response in the chat, an artefact or file, or an action in a service or program. Reuse (skills, plugins, templates) captures what works (proven tasks, procedures and integrations) and is loaded for a matching task. Delegation (Cowork, scheduled tasks, agents) means Claude carries out the process itself, in several steps or on a schedule.

*Figure 2: Interaction of the six building block groups. The groups correspond to sections B to G of the list in 1.2.*

**Selection of the building block**

| Requirement| Building block| Note
| :---:| :---:| :---:
| Include material once| File in chat| This applies only to this conversation.
| Provide knowledge and rules for a project| Project| Applies to all conversations within the project.
| Set preferences for all conversations| Personal instructions, Memory| You write the instructions yourself; Memory is created by Claude.
| Retrieve up-to-date information| Web search; for in-depth questions, use Research| Training knowledge ends in June 2026 (1.1).
| Use data from a service or interact with it| Connector| This saves you from having to upload data repeatedly.
| Perform a task in the same way every time| Skill| A skill describes a procedure; a project describes the background to an undertaking. Claude only loads it when the task is suitable.
| Share skills and connectors as a bundle| Plugin| It contains skills, but does not replace them.
| Edit or share a result| Artifact| For Word, Excel or PowerPoint, Claude generates a file.
| Assign a multi-step task| Cowork| Claude takes action itself, rather than just replying.
| Have a task carried out regularly| Scheduled task| It runs hourly, daily, weekly or on weekdays.
| Work on source code| Claude Code| It reads and modifies the files of a software project directly.

**Typical expansion**

The building blocks build on one another. A prompt that is repeated becomes a skill. Anything that applies to a project on a permanent basis is incorporated into the project. A skill that runs reliably can be delegated (Chapters 8 and 9).
