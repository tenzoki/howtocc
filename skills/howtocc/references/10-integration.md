# Chapter 10: Integration into applications and products

From the guide *Apply Claude* by Kai Stalmann, as of November 2026. Numbers in brackets such as (8.3) refer to sections of the guide; the index in SKILL.md says which file holds each chapter.

## 10.1 Claude in productivity applications

Describes working with Claude within Microsoft Office, Google Workspace, Slack and Microsoft Copilot.

Claude and the work application can be integrated in two ways: either an extension brings Claude into the application, or a connector brings the application into Claude (8.4). Both methods are available for Google Workspace.

| Environment| Offering| What it does| Availability
| :---:| :---:| :---:| :---:
| Microsoft 365| Claude for Excel, PowerPoint, Word and Outlook (extensions)| Excel: read and write cells, formulas, pivot tables and charts. PowerPoint: create and edit slides within an existing template. Word: draft and revise documents with tracked changes. Outlook: organise your inbox, draft replies, find appointments| Paid plans. Outlook is in beta and requires one-off approval from the administrator.
| Google Workspace| Connectors for Gmail, Calendar and Drive; Claude for Google Workspace (sidebar in Docs, Sheets and Slides)| Connectors: search for, read, draft emails and send them after asking for confirmation. Create, edit and delete appointments. Search for, share and move files in Drive (6.3). Sidebar: Claude reads the open file and edits it directly.| Connectors: all plans. Sidebar: Beta, paid plans
| Slack| Claude Tag| Anyone who mentions `@Claude` in a channel assigns a task. Claude maintains a checklist in the thread and replies there, visible to everyone.| Public Beta. Team and Enterprise. Billed on a pay-as-you-go basis via the organisation; channels do not require a separate licence per Slack user. Direct messages are routed via the user’s licence.
| Microsoft Copilot| Claude models in Copilot, Researcher and Copilot Studio| The user selects Claude as the model within the Microsoft products.| Operated by Microsoft. Disabled by default in the EU, EFTA and the United Kingdom. A separate setting for Word, Excel and PowerPoint is enabled by default if the tenant (the organisation’s Microsoft 365 environment) was created after 25 March 2026

**Special features**

- **Microsoft 365:** The four add-ins can share their working context. What happens in Excel is subsequently recognised by Claude in PowerPoint. In Team and Enterprise, this setting is disabled by default. Skills and connectors can also be used there.
- **Slack:** Claude Tag is intended for work that the team views collectively. Personal work on individual files remains the domain of Cowork or Claude Code. The owner restricts the user group and spending.
- **Microsoft Copilot:** Anthropic acts here as a sub-processor for Microsoft. Microsoft’s contractual and data protection terms and conditions apply. The Claude models are currently located outside Microsoft’s EU data boundary. On 5 November 2026, Microsoft announced that it would bring processing for organisations in the EU and EFTA within the EU data boundary by the end of 2026. In the EU, EFTA and the United Kingdom, an administrator must manually enable the models. Only the separate settings for Word, Excel and PowerPoint are enabled by default in tenant accounts created after 25 March 2026.

**Selection**

| Situation| Suitable approach
| :---:| :---:
| The work takes place on an open file.| Extension within the application
| Multiple sources contribute to a single result.| Claude with connectors
| The team works together on a task.| Claude Tag in Slack
| The organisation uses Microsoft’s contractual framework.| Claude models in Copilot

The rule set out in 6.3 applies to sending: a human must check the draft before it leaves the organisation.

## 10.2 Programming Interface and Agent Development

Explains how to integrate your own software with Claude via the Messages API, Tool Use, the Agent SDK and Managed Agents.

Your own software integrates Claude via four building blocks. They differ in the extent to which Anthropic takes over the agent loop (the sequence of planning, acting and checking).

| Module| What it provides| Loop run by| Suitable for
| :---:| :---:| :---:| :---:
| Messages API| The core interface accepts messages and returns the model’s response.| Your own application| Individual calls and workflows with full control
| Tool use| Claude requests that a function be called. Your own functions are executed by the application, whilst tools such as web searches and code execution are handled by Anthropic.| Your own application| Access to your own data and actions
| Agent SDK| The library for Python and TypeScript provides tools, the agent loop and context management of Claude Code.| Your own process| Agents on your own infrastructure
| Managed Agents| Anthropic runs the agent in an isolated cloud environment where it reads files, executes commands and uses the web.| Anthropic| Long-running and scheduled tasks. Beta

**Prerequisites:** You’ll need an account on the Claude Console and an API key. Billing is based on tokens used, separate from app subscriptions (2.2).

**Supplementary services**

| Service| Purpose
| :---:| :---:
| Message Batches| Process large volumes on a delayed basis, at half price
| Token Counting| Determine the size of a request before sending it
| Files| Upload files once and use them across multiple calls
| Skills| Create and manage your own skills (9.1)

**Rules**

- **Start small:** A single, well-formulated prompt is often sufficient. Agents are only worthwhile when the steps are unpredictable (9.2).
- **Describe tools precisely:** Claude decides when to call a tool based on the description.
- **Measure first, then refine:** Success criteria and test cases come before working on the prompt (8.2).
- **Consider data retention:** Managed agents retain session histories until they are deleted and are therefore unsuitable for agreements that do not permit data retention (11.1).
- **Operator obligations:** Anyone offering a chat service to customers must disclose the use of AI (6.2). Additional requirements apply to recommendations in high-risk areas (6.4).

## 10.3 MCP and Deployment Methods

Explains your own MCP servers, which provide tools and data, and MCP clients, which utilise them; also covers custom connectors and the choice of procurement channel, either directly from Anthropic or via a cloud provider.

MCP (Model Context Protocol) is an open standard that connects AI applications to external systems, much like a universal plug. Once built, a server works with any application that supports the standard, including, alongside Claude, ChatGPT, Visual Studio Code and Cursor.

| Role| Task| Examples
| :---:| :---:| :---:
| MCP server| Provides tools (actions), data and pre-built workflows| A service provider’s server, or your own server connected to an internal database
| MCP client| Connects to servers and calls their tools| Claude in Chat and Cowork, Claude Code, your own applications via the API’s MCP connector (Beta)

**Custom connectors**

A custom connector connects to a remote MCP server via its web address (8.4).

- **Accessibility:** Claude accesses the server from Anthropic’s cloud, even if the user is using Cowork or the desktop app. The server must be accessible via the public internet. If it is located on a corporate network, Anthropic’s IP addresses must be allowed through the firewall.
- **Login:** The server usually requires login via OAuth (a method for granting access without sharing a password) or fixed login credentials. With fixed, shared login credentials, every user can access whatever these credentials can access.
- **Organisation:** In Team and Enterprise plans, the owner adds such a connector; in Enterprise, a member with the appropriate role can also do so. Afterwards, each member connects independently.
- **Trust:** Anthropic does not verify these servers. Connections are only established with servers originating from a trusted source (11.1).

Local MCP servers, which run as a program on your own computer, are used by Claude Code and the desktop app. They are not available in the browser or on mobile devices; in Cowork, they are only available as part of a plugin.

**Procurement channels**

| Option| Operator| Feature
| :---:| :---:| :---:
| Claude API| Anthropic| New models and features first; billing and support provided by Anthropic
| Claude Platform on AWS| Anthropic, via the AWS account| Billing via AWS
| Amazon Bedrock| AWS| Integrated into AWS billing and rights management
| Claude Models on Google Cloud| Google or Anthropic, depending on the variant| Integrated into Google Cloud
| Microsoft Foundry| Via Azure. Anthropic operates the service in both variants, either on Azure’s infrastructure or on its own| In the Azure variant, inputs and responses remain within Azure. Some features are missing.

The range of features varies depending on the platform. Managed Agents are available via the Claude API, the Claude Platform on AWS and the Anthropic-operated version on Google Cloud. Anthropic recommends the direct approach for new projects and the full range of features, and the cloud provider for existing contracts, specific compliance requirements and consolidated billing. Before making a decision, it is important to check whether every required feature is available via the chosen approach.
