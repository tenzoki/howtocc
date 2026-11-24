# Chapter 11: Responsibility and Organisation

From the guide *Apply Claude* by Kai Stalmann, as of November 2026. Numbers in brackets such as (8.3) refer to sections of the guide; the index in SKILL.md says which file holds each chapter.

## 11.1 Data Protection, Administration and Risks Associated with Agents Acting Independently

Covers data protection, access rights, retention periods and audit trails, as well as safeguards for agents acting autonomously.

Three questions determine responsible use: What happens to the data, who is authorised to do what, and how is an acting agent restricted?

**Data Protection**

| Question| Individual plans (Free, Pro, Max, Ultra)| Team, Enterprise and API
| :---:| :---:| :---:
| Model training| When the model improvement setting is enabled, for conversations flagged for security review, and following explicit consent elsewhere. Incognito chats remain exempt even when this setting is enabled.| Not enabled by default
| Deletion| A deleted conversation disappears immediately from the history and from the systems within 30 days.| API: Inputs and outputs are deleted within 30 days. Uploaded files and sessions from Managed Agents remain until they are deleted. In the apps, the organisation’s retention policy applies.
| Extended storage| Where use for training is permitted, data is retained for up to 5 years in de-identified form.| For the API, a ‘zero data retention’ agreement can be requested. This does not cover every feature or every model; Fable, for example, is not included.

The following applies to all plans: Anthropic stores feedback via the thumbs buttons, along with the conversation, for up to 5 years and may use it for training. Content flagged as a breach of the Usage Policy remains stored for up to 2 years, whilst security check classification scores are retained for up to 7 years. Incognito chats are retained for 30 days by default and appear in the owner’s data exports for Team and Enterprise plans. Raw data from connectors is not used for training. Connected services process data in accordance with their own terms and conditions (8.4). The organisation itself is responsible for verifying whether compliance with the GDPR is sufficient.

**Administration**

| Means| Purpose| Plan
| :---:| :---:| :---:
| Centralised login (SSO), automatic account management (SCIM)| Centrally assign and revoke accounts| SSO from the Team plan onwards, SCIM in Enterprise
| Roles and permissions| Define who is permitted to use and share functions| Enterprise
| Permissions per function| Connectors (8.4), Memory (8.3), Skills and Plugins (11.2), Cowork and Claude in Chrome (9.4)| Team and Enterprise
| Retention rules| Set the retention period for conversations and files| Enterprise
| Audit trail| Audit logs and the Compliance API record activities. Events from Cowork can be forwarded to your own monitoring system.| Enterprise, monitoring of Cowork from the Team plan onwards

The managed settings (5.3) also apply to Claude Code.

**Risks posed by active agents**

Figure 10 as text: prompt injection becomes a risk where two conditions meet. Condition 1: Claude reads third-party content (web pages, emails, third-party files). Condition 2: Claude can take far-reaching action (send, pay, delete, change). Countermeasure for 1, limit reading: only trusted sources and extensions. Countermeasure for 2, limit action: approval before far-reaching actions.

*Figure 10: Two conditions for a successful attack via third-party content. If either is missing, the attack becomes difficult.*

The greatest risk is prompt injection: instructions hidden within third-party content cause Claude to perform an unintended action. According to Anthropic, such an attack requires both conditions to be met simultaneously.

- **Establish a trust boundary:** Define which sources are considered safe, and do not grant Claude write access to anything else.
- **Restrict permissions:** A dedicated working folder with a backup copy replaces access to all files.
- **Confirm actions with significant consequences:** Sending, paying and deleting remain subject to approval (9.4).
- **Limit unattended operations:** Scheduled tasks must not handle confidential data or perform actions that are difficult to reverse. Their results are checked after each run (9.3).
- **Check extensions:** Skills, plugins and MCP servers must only come from trusted sources (9.1, 10.3).

Anthropic trains the models to defend against such attacks and checks incoming content and outgoing actions. For Claude in Chrome, it cites a success rate for known attacks of less than 0.08 per cent in its own tests of the entire protection configuration using the Opus 4.8 model, whilst emphasising that the risk is not zero.

## 11.2 Collaboration, Distribution and Maintenance of Shared Resources

Describes how teams share, organise and archive results and projects, and how skills are released within the organisation or submitted as plugins to the Directory.

Working collaboratively with Claude requires three things: shared results, shared workspaces and shared procedures. There is a separate tool for each, with its own set of permissions.

| Subject| Path| Permissions and restrictions
| :---:| :---:| :---:
| Conversation| A link shows a snapshot. Subsequent messages remain private.| In Team and Enterprise, only within the organisation. Attached files and raw data from connectors are not included.
| Project| Sharing with individual users or the entire organisation| Team and Enterprise. Two levels: view or edit. The owner can disable sharing. Connectors only work in private projects.
| Skill| Share with individuals; in Enterprise, also with groups. Publish to the organisation’s library| Shared skills are read-only. Changes will be reflected for recipients the next time the skill is used. The organisation may require a review prior to publication.
| Plugin| The owner specifies the following for each plugin: not available, available for installation, installed by default, or mandatory.| Team and Enterprise. Custom catalogues (Marketplaces) are synchronised from a repository on GitHub or GitLab.
| Entry in the directory| Submission via the developer portal| Paid plan; in Team and Enterprise, submitted by the owner. Anthropic automatically reviews every version, with new plugins additionally reviewed by a human.

**Organising and archiving**

- **Assign:** Individual conversations can be moved to a project at a later date.
- **Highlight:** A star keeps important projects within easy reach.
- **Archive:** An archived project remains viewable and retains its members and permissions. It can only be deleted after it has been restored.
- **Revoke access:** Archiving does not revoke access. To do this, members must be removed in the sharing settings.

**Maintaining shared assets**

- **Assigning responsibility:** Every shared project and every published skill has a designated person in charge.
- **Managing versions:** Plugins from a repository carry their version history with them. Bugs are fixed there and the plugins are resynchronised.
- **Pruning the collection:** Outdated files in the project knowledge base take up space in the context window and lead to incorrect answers (8.3).
- **Review shared links:** In individual plans, the ‘Shared chats’ setting lists all shared links and allows you to remove them if desired.
- **Note departures:** Access to shared skills automatically ends when a user leaves the organisation.

## 11.3 Skills development and outlook

Outlines a step-by-step learning path from the basics to advanced use and identifies foreseeable product changes.

Using Claude can be learnt in four stages. Each stage adds a new skill whilst also requiring more scrutiny.

| Level| Skills| Chapter| Free courses from Anthropic
| :---:| :---:| :---:| :---:
| 1 Basics| Understanding how it works and its limitations, clarifying tasks, verifying results| 1, 2, 8.1, 8.2| “Claude 101”, “AI capabilities and limitations”, ‘AI Fluency: Framework and foundations’
| 2 Specialist application| Using Claude in your own field, providing knowledge, integrating services| 3 to 7, 8.3, 8.4| ‘AI Fluency’ for teachers, students, non-profit organisations and small businesses
| 3 Continuity| Documenting workflows as skills, planning tasks, handing over work to Cowork| 9| ‘Introduction to agent skills’, ‘Introduction to Claude Cowork’
| 4 Development and operation| Working with Claude Code, integrating Claude into your own software, managing and securing its use| 5, 10, 11| ‘Claude Code 101’, ‘Building with the Claude API’, MCP courses

The courses are available on the Claude Academy (academy.claude.com) and are free of charge. You can start them without an account. You only need to register if you wish to save your progress.

**Four competencies:** Anthropic’s course summarises the skilful use of AI in four terms, based on a framework by Rick Dakan and Joseph Feller.

| Competence| Meaning| In the document
| :---:| :---:| :---:
| Delegation| Deciding whether and how to use AI for a task| 2.1, 9.2
| Description| Describing objectives in such a way as to produce useful results| 8.1
| Discernment| Accurately assessing the results and behaviour of AI| 2.1, 8.2
| Diligence| Taking responsibility for the use of AI and its consequences| 11.1

**Duty of competence:** Article 4 of the EU AI Act has applied since 2 February 2025. In its amended form, it requires providers and deployers of AI systems to implement measures that support the development of their staff’s AI competence. They are not required to guarantee a specific level of competence.

**Foreseeable changes**

| Change| Status as of November 2026| Consequence
| :---:| :---:| :---:
| Chat and Cowork are merging.| Roll-out in Pro, Max and Ultra; beta in Team; available in Enterprise following activation| Approval modes and scheduled tasks are available in every conversation (9.3, 9.4).
| Projects are getting a revamp.| Beta for selected Pro, Max and Ultra subscribers, initially in Claude Code| A project becomes a conversation with parallel work streams (8.3).
| Claude Duet| Research Preview in the US; Team and Enterprise announced| An assistant that takes the initiative (9.4)
| Model change| Sonnet 4.5 will be discontinued on 30 November 2026. Older models that are still selectable will follow: Opus 4.5 on 24 November 2026 at the earliest, Opus 4.6 and Sonnet 4.6 in February 2027 at the earliest. The latest generation will run until at least September 2027.| Custom applications require a plan for the model change (10.2).
| Desktop extensions| Entries in the directory have been deprecated| Users of such extensions should consider replacing them with connectors or plugins (8.4).

Pricing, availability and designations such as ‘Beta’ in this document reflect the status as at November 2026. These should be checked in the source before making a decision. The principles set out in Part I are more durable: operating principle, limits of reliability and verification of results.
