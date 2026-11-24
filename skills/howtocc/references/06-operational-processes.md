# Chapter 6: Operational Processes

From the guide *Apply Claude* by Kai Stalmann, as of November 2026. Numbers in brackets such as (8.3) refer to sections of the guide; the index in SKILL.md says which file holds each chapter.

## 6.1 Strategy, Positioning and Customer Acquisition

Covers everything from problem definition through to the offering and target audience, right up to customer acquisition.

| Step| Key question| Contribution by Claude| Human review
| :---:| :---:| :---:| :---:
| 1 Problem| What is the problem, who is affected, and how often does it occur?| Research the market and competition using sources (3.1); summarise customer feedback from interviews, enquiries and surveys (3.2)| Check the figures in the source
| 2 Target group| Who is most affected by the problem, and who makes the purchasing decisions?| Create and describe segments based on your own customer data| Flag profiles without a data basis as assumptions
| 3 Offering| What is being promised, and how does it differ from the competition?| Formulate variations of the value proposition; compare competitors against each criterion (3.3)| Seek out counter-arguments, as Claude tends to agree too readily (7.1)
| 4 Marketing| Through which channels and with what content?| Plan a campaign with objectives, channels, an editorial plan and key performance indicators; draft content in line with the brand’s tone and check it against the style guide (4.2)| Check statements and rights before publication (4.1)
| 5 Acquisition| Which customers, for what purpose, at what stage?| Research companies and contacts, prepare meetings, draft outreach messages, transfer meeting notes into follow-up actions and fields in the CRM (customer database), prepare open sales opportunities and forecasts| Read and send every message yourself

**Building blocks:** Anthropic publishes plugins for this work, organised by role (9.1). ‘Marketing’ contains commands for campaign planning, brand analysis, competitor analysis and performance reporting. ‘Sales’ contains company research, meeting preparation, meeting summaries, review of open sales opportunities and forecasting. Both utilise web searches and proprietary material. ‘Sales’ accesses CRM, email and calendar systems via connectors, such as Salesforce or HubSpot, whilst ‘Marketing’ accesses services such as Canva, Figma and HubSpot (8.4). Recurring tasks, such as a morning briefing on the day’s appointments, run as scheduled tasks (9.3).

**Limitations**

- **Assumptions remain assumptions:** Claude provides market size, willingness to pay and prices as reasoned estimates. These are only validated by market testing.
- **In-house knowledge is lacking:** Claude’s understanding of customers and the market is based solely on the material it receives. The more complete your own data, the more robust the segments.
- **Communication is regulated:** promotional messages are subject to advertising and data protection laws. The responsibility for verification lies with the company (11.1).

## 6.2 Customer service and support

Describes how Claude responds to customer enquiries, drafts replies for staff and maintains the knowledge base.

Claude takes on three roles in customer service: it answers routine enquiries itself, prepares complex cases for staff, and transfers resolved cases to the knowledge base.

Figure 6 as text: a customer enquiry (chat, email, form) is 1 classified by Claude (topic, urgency, responsibility). Routine questions are 2 answered directly, backed by the knowledge base; the response carries its source and is in the language of the enquiry. If uncertain, Claude 3 prepares the case (summary and draft reply) and 4 staff check, decide and reply. The knowledge base holds policies, product knowledge and articles from resolved cases.

*Figure 6: The customer enquiry workflow. Claude answers routine questions using the knowledge base; all other cases are prepared for staff. Resolved cases are transferred back as articles.*

**Two ways to use it**

| Path| Function| Prerequisite
| :---:| :---:| :---:
| Assistant for the service team| The ‘Customer Support’ plugin sorts enquiries by category and urgency (`/triage`), searches for answers in the connected systems (`/research`), drafts the response (`/draft-response`), bundles a case for the technical team (`/escalate`) and writes help articles from resolved cases (`/kb-article`).| Paid plan. Chat, Cowork or Claude Code. Connectors to the ticketing system, CRM and knowledge base
| Dedicated customer channel| A chat system built via the API responds directly to customers, retrieves customer and order data, and carries out actions (10.2).| Development, testing and ongoing monitoring

According to Anthropic, the solution is worthwhile for large volumes of similar enquiries, for round-the-clock support where required, during peak periods and for multilingual customer bases.

**Anthropic’s benchmark figures for a customer chat**

| Key metric| Benchmark
| :---:| :---:
| Correct identification of enquiries| at least 95%
| Correct company and product details| 100%
| Cases correctly escalated to humans| at least 95%
| Enquiries resolved without human intervention| 70 to 80%
| Customer satisfaction| at least 4 out of 5

**Protection rules**

- **Disclose AI use:** Anthropic’s Usage Policy (version valid from 12 November 2026) requires that a chat with customers be identifiable as AI at the start or within the interface.
- **Respond only with verified information:** Claude responds from the knowledge base and cites the source. If there is no basis for a response, it escalates the case (2.1).
- **No commitments:** Decisions on refunds, goodwill gestures and contract amendments are made by a human.
- **Protecting data:** Personal data appears in replies only where necessary and permissible.
- **Staying on topic:** The chatbot redirects questions outside its area of expertise; inputs are checked for misuse.

## 6.3 Office and Administration

Covers support for internal processes such as correspondence, scheduling, minutes and data maintenance.

Office and administrative tasks account for 8% of conversations on Claude.ai in the Anthropic Economic Index and 15% of usage via the programming interface (report from January 2026, sample from November 2025).

| Task| Support| Building block| Monitoring
| :---:| :---:| :---:| :---:
| Correspondence| Organise your inbox, summarise long threads on decisions and outstanding issues, draft replies in your own tone| Claude for Outlook (Beta, Pro and above), Gmail connector (all plans)| In Outlook, the reply is saved as an unsent draft. Via Gmail, Claude asks for confirmation before each send.
| Scheduling| Find mutually available times, prepare invitations using the Outlook form, create and amend appointments via Google Calendar, prepare meetings with a brief briefing| Claude for Outlook, Google Calendar connector| Check invitations before sending
| Minutes| Extract decisions, outstanding items and responsible parties from meeting transcripts or notes, draft a follow-up message| Chat, Claude Docs (4.3)| Cross-check decisions and names against the transcript
| Data maintenance| Clean up and standardise lists, find duplicates, create tables with formulas| Code execution (3.2), Claude for Excel| Take samples, save a copy beforehand
| Recurring tasks| Daily overview, weekly report, to-do list| Scheduled tasks (9.3). Use the ‘Productivity’ plugin for the to-do list| Monitor the first runs

**Draft before sending:** By default, the user must confirm every action that Claude carries out on their behalf. In Team and Enterprise plans, the owner (organisation administrator) decides whether members may authorise individual actions without confirmation. For anything leaving the organisation, confirmation should remain mandatory.

**Limitations**

- **Attachments and images:** The Gmail connector only reads key data from attachments, not the content. From files in Google Drive, Claude only reads the text.
- **Outlook:** The add-in runs on the web, on Windows and on Mac with Microsoft 365. The mobile Outlook apps and self-hosted Exchange servers are excluded.
- **Activation:** In Team and Enterprise plans, the owner must approve connectors before individual users can connect to them.

Integration with Microsoft 365 and Google Workspace is covered in section 10.1.

## 6.4 Industry-specific use

Covers finance, law, healthcare, life sciences, public administration and charitable organisations, including their specialist offerings and requirements.

| Sector| Typical tasks| Specialist services
| :---:| :---:| :---:
| Finance| Presentations for transactions, credit proposals, portfolio reports, verification of actuarial tables in Excel and PowerPoint| Connectors to data providers such as LSEG, FactSet, S&amp;P Global and Morningstar; agent templates for loan applications, customer due diligence (KYC) and fund accounting; dedicated offering for financial advisers
| Legal| Check contracts against your own negotiation guidelines, with tracked changes in Word; review numerous contracts in tabular form; compare legal situations across countries; keep track of deadlines and mandates| Ready-made artefact templates, plugins and connectors to iManage, NetDocuments, Ironclad and Bloomberg Law
| Healthcare| Review applications for cost coverage, prepare appeals against rejections, sort patient records| Connectors to coding and service databases (ICD-10, CMS, NPI) and PubMed; support for the FHIR data standard; infrastructure compliant with the US Health Insurance Portability and Accountability Act (HIPAA)
| Life Sciences| Bioinformatics, literature reviews, study protocols, regulatory submissions| Claude Science (3.5); connectors to PubMed, bioRxiv, ClinicalTrials.gov and Benchling; Team plan for verified academic and non-profit research groups, free to start with, promotional price for 12 months
| Public administration| Document review, research, drafting, case management, replacement of legacy software, public enquiries with handover to case officers| Claude for Government in an environment with US FedRAMP High security certification; access also via Amazon Bedrock and Google Cloud
| Charities| Finding funding, writing applications and reports, planning campaigns, recruiting staff| Discounted Team and Enterprise plans; pre-installed ‘Claude for Nonprofits’ plugin; connectors to Blackbaud, Benevity and Candid

Several services are tailored to the US: the health databases, HIPAA and FedRAMP. Claude Enterprise itself does not hold FedRAMP authorisation. Claude for Education is covered in 3.4.

**Requirements for high-risk use:** Anthropic’s Usage Policy (version valid from 12 November 2026) sets out two conditions whenever a recommendation from Claude concerns a person’s health, rights, finances, work, housing, education or access to services.

- **Professional review:** A qualified person must review the recommendation before it is passed on as advice or implemented as a decision. They may amend it and remain responsible. If the law requires a licence to practise, the person must hold one.
- **Disclosure:** The person concerned is informed that AI was involved.

| Area| Recommendations covered (selection)
| :---:| :---:
| Law and legal status| Advice on rights and obligations in individual cases, documents for signing or submission, outcomes of civil, administrative and arbitration proceedings, residence, asylum and citizenship status
| Medicine| Diagnosis, treatment and dosage, interpretation of symptoms and test results
| Finance, credit, insurance| Personal investment advice, tax advice, credit decisions, premium calculations, decisions on claims
| Work, housing, education| Candidate selection and performance appraisal, tenancy and purchase applications, admission and examination assessment
| Access to healthcare| Priority in triage and on waiting lists, admission to, refusal of or termination of treatment
| Public benefits| Entitlement to benefits and the level of benefits

Internal drafts, research and summaries are not covered, provided they do not themselves constitute the recommendation. Where permitted by law, the professional review is waived in the case of four decisions that are entirely in the person’s favour: payment of an insurance claim, approval of a medically prescribed benefit, authorisation for a healthcare service and approval of a public benefit. The policy completely prohibits decisions relating to criminal prosecution and the criminal justice system. It does not supersede local law: stricter provisions take precedence (11.1).
