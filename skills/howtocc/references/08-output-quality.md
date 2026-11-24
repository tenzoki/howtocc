# Chapter 8: Managing the Quality of Outcomes

From the guide *Apply Claude* by Kai Stalmann, as of November 2026. Numbers in brackets such as (8.3) refer to sections of the guide; the index in SKILL.md says which file holds each chapter.

## 8.1 Structuring the Work Assignment

Explains the structure of prompts in terms of role, context, task, constraints and format, and demonstrates that they can be written, spoken or supplemented with images and files.

A good instruction explicitly states what is to be produced, for what purpose and in what form. Anthropic recommends, as a test, presenting the instruction to a colleague with no prior knowledge: if she does not understand it, neither will Claude.

| Building block| Key question| Example| Note
| :---:| :---:| :---:| :---:
| Role| From whose perspective does Claude work?| “You are reviewing as an editor at a specialist publishing house.”| One sentence is enough. In current models, a clear brief counts for more than the role.
| Context| Who is the result for, and what is its purpose?| “The letter is addressed to customers without specialist knowledge and explains a price increase.”| Justifying a requirement helps: Claude applies it to similar cases.
| Task| What exactly is to be produced?| “Write three versions of the subject line.”| Start with the action verb. Number several steps.
| Restrictions| What are the limitations?| “No more than 150 words; use only details from the attached price list.”| State what should be included, rather than what shouldn’t. Allow for uncertainty: “Let us know if any details are missing.”
| Format| In what format?| “As a table with the columns: Variant, Subject, Reason.”| An example is the most reliable way to guide the format and tone.

**Rules**

- **Ask for more if more is required:** Claude delivers what the prompt specifies. Depth, completeness or variations must be explicitly requested.
- **Use examples sparingly:** one example is often sufficient. Anthropic recommends three to five different examples to prevent Claude from adopting the randomness of a single pattern.
- **Long material first:** extensive documents should be placed at the beginning, with the question at the end. Anthropic reports that this order yields up to 30 per cent better answers in tests. Furthermore, the prompt helps by citing the relevant sections first (2.1).
- **Keep it short:** A longer prompt is not necessarily better (8.2).

**Input methods**

| Method| Suitability| Limit
| :---:| :---:| :---:
| Writing| Precise prompts that can be checked and reused|
| Speaking| The voice mode (beta, all plans) conducts the conversation verbally, for example for thinking aloud or whilst on the move. Switch between text and voice within the same conversation.| Fable is not available as an option here. Ask multi-part questions one at a time.
| Images| Photos, screenshots and diagrams can be added to the prompt.| Claude has difficulty reading small or blurry images. Anthropic recommends a minimum resolution of 1,000 × 1,000 pixels.
| Files| Documents and spreadsheets provide the material to which the prompt refers.| Formats and size limits are specified in section 3.2.

## 8.2 Iteration and error diagnosis

Shows how results improve step by step and how typical errors in the prompt can be identified.

A poor result usually indicates a gap in the prompt. The quickest way to improve is for each iteration to address exactly one cause.

| Symptom| Probable cause| Correction
| :---:| :---:| :---:
| The answer remains too general.| The task specifies neither details nor requirements.| Add details and an example; explicitly request depth
| The answer misses the mark.| The purpose and target audience are missing.| State what the result is needed for
| The format varies.| The form is merely described.| Include a template
| For large tasks, the result becomes unreliable.| A task requires too many steps at once.| Break down into sub-tasks, each of which accomplishes one thing (9.2)
| Details are made up.| The material is missing, and Claude fills in the gap.| Include material, explicitly allow ‘I don’t know’, request evidence (2.1)
| Claude suggests rather than implementing.| The task is phrased as a question.| “Change the paragraph” instead of “Can you suggest changes?”
| Previous instructions are lost.| The conversation is long; older parts have been summarised (1.1).| Start a new conversation; include permanent information in the project instructions (8.3)

**Procedure**

- **Start simply:** Begin with a concise, clear brief and only add to it if it noticeably improves the result.
- **Give precise feedback:** Specify what should stay the same and what needs to change, rather than simply demanding that it be ‘better’.
- **Start afresh:** After two unsuccessful rounds of corrections, a new discussion with a more precise brief will lead to the desired outcome more quickly. Otherwise, the process will continue to be influenced by previous failed attempts.
- **Ask Claude:** The question “What was unclear about my instruction? Rephrase it” often reveals the missing detail.
- **Secure what works:** An instruction that proves effective belongs in the project instructions (8.3) or in a skill (9.1).
- **Measuring recurring tasks:** Anyone who uses a task frequently or in a custom application should define success criteria and test cases, and check every change made to it (10.2).

## 8.3 Provision of working knowledge

Explains how projects, instructions, Memory and files determine what knowledge is available to the model, and how the context window limits its scope.

Claude only knows what is in the context window about a project (1.1). Several means provide knowledge to the context window, and they differ in their scope.

Figure 8 as text: three nested scopes, all of which must fit inside the limited context window. Account (applies in every conversation): personal instructions (working style, tone; set by the human) and Memory (topics from earlier conversations; created by Claude). Project (applies only there): project instructions (role, goal, rules; set by the human), project knowledge (files for the project) and project memory (created by Claude). Conversation: the prompt (task, files, images) and the history (responses and tool results).

*Figure 8: Scopes of working knowledge. What applies in the account affects every conversation; what is contained in the project applies only there.*

| Means| Content| Note
| :---:| :---:| :---:
| Personal instructions| Working methods, personal terminology, typical tasks, tone| These apply to all conversations within the account.
| Project instructions| Role, objective and rules of a project| Keep it concise: framework, key rules, role.
| Project knowledge| Documents, data and code relating to the project| Up to 30 MB per file; the text is imported. In paid plans, when dealing with large volumes of data, Claude loads only the relevant excerpts (RAG) and can thus hold up to ten times the volume.
| Memory| Role, people, preferences, ongoing work| Claude creates the entries itself or in response to the command ‘Remember this’. They can be viewed and edited. Claude only stores sensitive topics such as health or religion with consent.
| Search in previous chats| Content from previous conversations on request| Paid plans. Within a project, Claude only searches that project’s conversations.

**Rules**

- **Conversations within a project are not linked to one another:** the only thing they have in common is what is contained in the instructions, project knowledge, project memory or the account’s memory. Results that are to remain valid should be included in the project knowledge.
- **Memory is not a set of rules:** Claude decides for itself what to remember. Binding guidelines belong in the instructions.
- **Switch it off where it gets in the way:** Memory can be switched off for an individual conversation before the first message is sent. An incognito chat is also excluded from the history and search function (11.1). It is not available in projects.
- **The organisation has a say:** In Team and Enterprise, Memory is enabled by default for the organisation. The owner can disable it, in which case all members’ memories will be permanently deleted. In organisations created on or after 31 October 2026, Memory is enabled for every member from the outset. In older organisations, each member enables it themselves.

**The context window as a boundary:** All the elements mentioned share the space with the history, tools and the response being drafted (1.1). Three habits help keep it clear: keep project instructions concise, enable only the connectors you need (8.4) and start a new conversation for a new topic.

A new version of projects is being introduced as a beta for selected Pro, Max and Ultra subscribers, initially in Claude Code. There, a project is a single conversation, the work of which Claude distributes across parallel threads. A library collects the files.

## 8.4 Connecting to external data sources

Describes how connectors to services such as Google Drive, Gmail, Notion, Slack or GitHub make existing data usable and allow actions to be performed within these services.

A connector makes a service’s data accessible without uploading it and allows Claude to act within that service. Its scope is limited strictly to the permissions of the logged-in user: anything the user is not authorised to view within the service remains inaccessible to Claude. Shared access credentials (10.3) form an exception to this. In Google Drive, Claude searches for files; in Slack, it sends messages; and in the Linear task management system, it creates tasks. Connectors are available across all plans, in Chat, in Cowork, in the desktop app and in the mobile app.

**In four steps**

1. **Select:** The Directory (Anthropic’s catalogue) lists the intended use as well as the read and write permissions for each connector.
2. **Connect:** The user logs in to the service and confirms the requested permissions.
3. **Enable:** The ‘+’ menu in the conversation determines which services Claude is permitted to use there.
4. **Use:** Claude automatically draws on a connected service if it is relevant to the question.

**Types**

| Type| Feature| Note
| :---:| :---:| :---:
| Connector from the Directory| Listed by Anthropic, with its own page detailing capabilities and availability| Automatically verified by default; additionally verified by a human and labelled ‘Verified’
| Interactive connector| Displays interfaces such as dashboards or task boards directly within the conversation| Marked as ‘Interactive’ in the Directory
| Custom connector| Connects to an MCP server via its web address (10.3)| Not tested by Anthropic. One is permitted on the Free plan.
| Desktop extension| Runs locally within the desktop app| The entries in the Directory have been deprecated (1.2).

**Control**

- **Set action levels:** Each connector’s capability has one of three levels: always allowed, approval required or blocked. In Team and Enterprise, the owner can set the levels for everyone, for example, allowing reading but blocking sending.
- **Activation:** In Team and Enterprise, the owner activates a connector, after which each member signs in themselves (6.3).
- **Save space:** Each connector takes up context. The ‘Auto’ default setting is suitable for most users. From around ten connectors onwards, the ‘On demand’ setting is worth using, whereby Claude only loads a service when it needs it.
- **Note the data location:** The connected service processes data on its own infrastructure and under its own terms and conditions. Changing Claude’s settings regarding the processing location does not alter this.
- **Connect sparingly:** Only connect services that are needed and that you trust. Write permissions carry greater weight than read permissions (11.1).
