# AI Engineering
## Vision[](https://handbook.gitlab.com/handbook/engineering/ai/#vision)
**Our goal is not merely to launch features, but to ensure they land successfully and provide real value to our customers.** We strive to develop a best-in-class product that exceeds expectations across all user groups by meeting high-quality standards while ensuring reliability and maintaining an ease of operation and scalability to meet diverse customer needs. All team members should remain mindful of our target customers and the multiple platforms we support in everything we do.
Ensure our product excels in all aspects especially for our primary customer [organization archetypes](https://handbook.gitlab.com/handbook/product/personas/organization-archetype/) of large enterprises. This includes scalability, adaptability, and seamless upgrade paths. When designing and implementing features, always keep in mind compatibility for all our deployment options: self-managed, dedicated and Software as a Service (SaaS).
Develop our technical, diverse and global team to drive results that support our product and customer growth, while maintaining [our values](https://handbook.gitlab.com/handbook/values/) and [unique way of working](https://handbook.gitlab.com/handbook/company/culture/all-remote/guide/).
## Mission[](https://handbook.gitlab.com/handbook/engineering/ai/#mission)
GitLab’s unique way of working asynchronously, handbook first method, utilization of the product we develop and clear focus on our values enables very high productivity. We focus on constantly improving quality, usability and reliability of our product to reach maximum customer satisfaction. Community contributions and customer interactions rely on efficient and effective communication. We are a data-driven, customer experience first, open core organization delivering one secure, reliable, world leading DevSecOps platform. Join us in setting new standards, driving innovation, pushing the boundaries of DevSecOps, and consistently delivering exceptional results for our customers.
## Organizational Structure[](https://handbook.gitlab.com/handbook/engineering/ai/#organizational-structure)
![](https://www.plantuml.com/plantuml/svg/FK_D3e8m3Bxp53tlAJ08XfCc7ZmNDc5njARhWlhqZlbpw_UVrb5HT1rYPM3NGqkJ9-V4qrGP0wtroXAXVQYZw9dYncPVm_PhoQ0JNDpASjlmFZ4qCshH9aSA7IUogB_q9HklWLTeK35mAJa47Z30sQ6CSqaIXkVBvTF0ITYcKJ-S-Z4Mze-WfwYIbZnLHefwlAjVV2we7TdjkpS0)
## AI Engineering stakeholders[](https://handbook.gitlab.com/handbook/engineering/ai/#ai-engineering-stakeholders)
This section provides an overview of all teams invested in implementing and maintaining AI features. Our Duo initiative is a cross-category effort.
These are the stakeholders:
Team | Responsible For  
---|---  
[Agent Foundations](https://handbook.gitlab.com/handbook/engineering/ai/agent-foundations/) | Agentic observability / Reusable Agentic components / Duo workflow service  
[AI Coding](https://handbook.gitlab.com/handbook/engineering/ai/ai-coding/) | Code Suggestions, Duo Code Review, code-related slash commands (/explain, /refactor, /tests, /fix), Semantic Indexing, Duo Context Exclusion, Repository X-Ray  
[AI Framework](https://handbook.gitlab.com/handbook/engineering/ai/ai-framework/) | Abstraction Layer / AI Gateway for LLM integration to the application (GitLab Chat, Code Suggestions and other AI capabilities)  
[AI Framework](https://handbook.gitlab.com/handbook/engineering/ai/ai-framework/) (formerly Model Validation) | Custom feature evaluators, evaluation support, automated evaluation tooling  
[Cloud Connector](https://handbook.gitlab.com/handbook/engineering/infrastructure/team/cloud-connector/) (`@mkaeppler`, `@nmilojevic1`) | Supports access to Duo for Self-Managed: Cloud Connector, Unit Primitives  
[Duo Chat](https://handbook.gitlab.com/handbook/engineering/ai/duo-chat/) | GitLab Chat for VS Code and WebIDE  
[Editor Extensions: VS Code](https://handbook.gitlab.com/handbook/engineering/ai/editor-extensions-vscode/) | Maintains the GitLab Workflow VS Code Extension ([maintainers](https://gitlab-org.gitlab.io/gitlab-roulette/?currentProject=gitlab-vscode-extension&mode=show&hidden=reviewer)) & [Web IDE](https://gitlab.com/gitlab-org/gitlab-web-ide) extensions and the [language server](https://gitlab.com/groups/gitlab-org/-/epics/2431). Also contributes with UX improvements for Code Suggestions within GitLab Workflow.  
[Editor Extensions: Multi-Platform](https://handbook.gitlab.com/handbook/engineering/ai/editor-extensions-multi-platform/) | 
  * [JetBrains](https://gitlab.com/gitlab-org/editor-extensions/gitlab-jetbrains-plugin), [Neovim](https://gitlab.com/gitlab-org/editor-extensions/gitlab.vim) & [Visual Studio](https://gitlab.com/gitlab-org/editor-extensions/gitlab-visual-studio-extension) editor extensions
  * Co-owns [Language Server](https://gitlab.com/gitlab-org/editor-extensions/gitlab-lsp) with [Editor Extensions: VS Code](https://handbook.gitlab.com/handbook/engineering/ai/editor-extensions-vscode/)
  * Duo CLI (Ideation/MVC phase)

  
[Global Search](https://handbook.gitlab.com/handbook/engineering/ai/search/) | Abstraction Layer / Vector Storage / Semantic  
[Infrastructure Platforms - Runway](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/gitlab-delivery/runway/) | AI Gateway Scalability / Runway infrastructure  
[Workflow Catalog](https://handbook.gitlab.com/handbook/engineering/ai/workflow-catalog/) | AI Catalog / Custom Agents / Custom Flows  
## Counterparts[](https://handbook.gitlab.com/handbook/engineering/ai/#counterparts)
The AI department engineering structure is different from the Product structure. To read about how we collaborate and who are the counterparts, you can check the [AI product’s page](https://handbook.gitlab.com/handbook/product/ai/).
## ClickHouse Datastore usage[](https://handbook.gitlab.com/handbook/engineering/ai/#clickhouse-datastore-usage)
[ClickHouse usage by Analytics:Platform Insights group](https://handbook.gitlab.com/handbook/engineering/data-engineering/analytics/platform-insights/#clickhouse-datastore)
## Operating Principles[](https://handbook.gitlab.com/handbook/engineering/ai/#operating-principles)
[Operating Principles for the AI Engineering Groups](https://handbook.gitlab.com/handbook/engineering/ai/operating-principles/)
## AI Experimentation[](https://handbook.gitlab.com/handbook/engineering/ai/#ai-experimentation)
We strongly encourage team members to experiment and develop AI-related projects as part of their exploration and learning journey. These experimental initiatives help accelerate our work and allow AI teams to embrace emerging challenges and opportunities.
Existing projects may be reviewed by product and engineering teams on a case-by-case basis for potential migration into GitLab-managed projects.
To protect GitLab’s brand while maintaining our commitment to transparency, all experimental AI projects must prominently display the following disclaimer at the top of their README:
“⚠️ This is an unofficial project. It is not endorsed or supported by GitLab Inc. and is not recommended for use in production environments.”
* * *
#####  [Agent Foundations Group](https://handbook.gitlab.com/handbook/engineering/ai/agent-foundations/)
The Agent Foundations group is focused on developing GitLab Duo Workflow, an AI system to automate tasks and help increase productivity in your development workflow.
#####  [AI Coding Group](https://handbook.gitlab.com/handbook/engineering/ai/ai-coding/)
The AI Coding Group is part of the AI Engineering organization focused on user-facing AI-powered coding features.
#####  [AI Framework Group](https://handbook.gitlab.com/handbook/engineering/ai/ai-framework/)
The AI Framework group is focused on how to support other product groups at GitLab with the AI Abstraction Layer, and GitLab AI feature development.
#####  [Context Systems Group](https://handbook.gitlab.com/handbook/engineering/ai/context-systems/)
The Context Systems Group is part of the AI Engineering organization focused on context gathering tools used to power our AI systems
#####  [Custom Models Group](https://handbook.gitlab.com/handbook/engineering/ai/custom-models/)
The Custom Models group focuses on additional, custom models that power GitLab Duo functionality in support of our customers unique data and use-cases.
#####  [Duo Chat Group](https://handbook.gitlab.com/handbook/engineering/ai/duo-chat/)
We are dedicated to enhancing DevSecOps productivity by building an AI natural language interface to GitLab's Platform.
#####  [Editor Extensions: Multi-Platform Group](https://handbook.gitlab.com/handbook/engineering/ai/editor-extensions-multi-platform/)
We own and maintain code editor extensions for JetBrains, Visual Studio, Neovim & Eclipse IDEs, as well as contributing to the Language Server bringing GitLab's core features and AI capabilities directly into developer workflows.
#####  [Editor Extensions: VS Code Group](https://handbook.gitlab.com/handbook/engineering/ai/editor-extensions-vscode/)
We own and maintain code editor extensions for VS Code, WebIDE as well as contributing to the Language Server bringing GitLab’s core features and AI capabilities directly into developer workflows.
#####  [Global Search Group](https://handbook.gitlab.com/handbook/engineering/ai/search/)
The Global Search team is focused on bringing world class search functionality to GitLab.com and self-managed instances.
#####  [Operating Principles](https://handbook.gitlab.com/handbook/engineering/ai/operating-principles/)
The Operating Principles for the AI Engineering groups. These principles define how we work together to deliver reliable features under tight timelines without sacrificing long-term maintainability.
#####  [Workflow Catalog Group](https://handbook.gitlab.com/handbook/engineering/ai/workflow-catalog/)
The Workflow Catalog Group is focused on developing Workflow Catalog, a catalog of Agents, tools, and flows that can be created, curated, and shared across organizations, groups, and projects.
Last modified February 2, 2026: [Combine Context Systems and AI Coding (`96cbbb33`)](https://gitlab.com/gitlab-com/content-sites/handbook/commit/96cbbb33)
[ ](https://gitlab.com/gitlab-com/content-sites/handbook/blob/main/content/handbook/engineering/ai/_index.md) - [ ](https://gitlab.com/-/ide/project/gitlab-com/content-sites/handbook/edit/main/-/content/handbook/engineering/ai/_index.md) - please [contribute](https://handbook.gitlab.com/handbook/about/contributing/). [ ![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-sa/4.0/)