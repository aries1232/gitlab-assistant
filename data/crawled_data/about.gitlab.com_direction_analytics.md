#  Stage Direction - Analytics 
  1. You are here:
  2. [GitLab Direction](https://about.gitlab.com/direction/)
  3. Stage Direction - Analytics


The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
  * [What we do](https://about.gitlab.com/direction/analytics/#what-we-do)
    * [Vision](https://about.gitlab.com/direction/analytics/#vision)
    * [Common User Questions We Address](https://about.gitlab.com/direction/analytics/#common-user-questions-we-address)
  * [Composition](https://about.gitlab.com/direction/analytics/#composition)
    * [Platform Insights Group](https://about.gitlab.com/direction/analytics/#platform-insights-group)
    * [Optimize Group](https://about.gitlab.com/direction/analytics/#optimize-group)
    * [Analytics Instrumentation Group](https://about.gitlab.com/direction/analytics/#analytics-instrumentation-group)
  * [Cross-stage Vision for GitLab Usage Analytics](https://about.gitlab.com/direction/analytics/#cross-stage-vision-for-gitlab-usage-analytics)
  * [How we do it](https://about.gitlab.com/direction/analytics/#how-we-do-it)
    * [Personas](https://about.gitlab.com/direction/analytics/#personas)
  * [Right to Win](https://about.gitlab.com/direction/analytics/#right-to-win)
  * [Product Principles](https://about.gitlab.com/direction/analytics/#product-principles)
  * [Where we're going](https://about.gitlab.com/direction/analytics/#where-were-going)
    * [Thematic Direction](https://about.gitlab.com/direction/analytics/#thematic-direction)
    * [1 Year Plan](https://about.gitlab.com/direction/analytics/#1-year-plan)
    * [Competitive Strategy](https://about.gitlab.com/direction/analytics/#competitive-strategy)
  * [Deployment Approaches](https://about.gitlab.com/direction/analytics/#deployment-approaches)
  * [Handbook Pages](https://about.gitlab.com/direction/analytics/#handbook-pages)


## What we do[](https://about.gitlab.com/direction/analytics/#what-we-do)
### Vision[](https://about.gitlab.com/direction/analytics/#vision)
Our vision is to make GitLab the definitive platform for understanding software delivery performance and AI-powered development in the modern era. The Analytics Section closes the DevSecOps loop by providing comprehensive insights into how teams build, ship, and improve software—from SDLC metrics and Value Stream Analytics to AI usage intelligence and developer productivity.
We are uniquely positioned at the intersection of three critical industry trends:
  * The shift to AI-assisted software development and the need to measure its impact
  * Growing demand for engineering intelligence and developer productivity insights
  * The evolution of platform engineering and the need for data-driven DevSecOps decisions


This positions us to compete directly with GitHub Copilot's usage analytics, the Atlassian DX platform acquisition, and standalone engineering intelligence platforms. Our competitive advantage lies in native data ownership, real-time processing through the Data Insights Platform, and seamless integration with GitLab's complete SDLC data.
We will deliver value by:
  * Providing unified visibility into software delivery performance with modern DORA metrics and beyond
  * Enabling teams to measure and optimize AI-assisted development
  * Offering actionable insights from GitLab's unique position as a complete DevSecOps platform
  * Building the foundational data infrastructure that makes advanced analytics possible across GitLab


### Common User Questions We Address[](https://about.gitlab.com/direction/analytics/#common-user-questions-we-address)
When talking with users, we consistently hear:
  * How are my teams actually using GitLab and our AI tools?
  * What's the ROI of our AI coding assistant investments?
  * How do we measure developer productivity without creating perverse incentives?
  * Where are the bottlenecks in our software delivery process?
  * How can we benchmark our performance against industry standards?
  * What data does GitLab collect and how can we leverage it for our own insights?
  * How do I create custom reports that answer my specific business questions?
  * How can we move from reactive metrics to predictive intelligence?


## Composition[](https://about.gitlab.com/direction/analytics/#composition)
The Analytics Section is comprised of a single Stage: the Analytics stage. This stage has three groups:
### Platform Insights Group[](https://about.gitlab.com/direction/analytics/#platform-insights-group)
[Platform Insights](https://about.gitlab.com/direction/analytics/platform-insights) focuses on enabling users to analyze and visualize data to uncover insights about software delivery and platform usage.
**Categories:**
  * Custom Dashboards Foundation - Infrastructure for building and displaying dashboards across GitLab 
    * [Dashboard Customization Framework](https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/dashboard_customization_framework/)
    * [Dashboard Layout Framework](https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/dashboard_layout_framework/)
    * [GitLab Data Exploration](https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/gitlab_data_exploration/)
  * Data Insights Platform - Modern data processing infrastructure built on ClickHouse that powers real-time analytics across GitLab 
    * [Data Insights Platform Architecture](https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/data_insights_platform/)
    * [Siphon Architecture](https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/siphon/)
    * [Analytics with Siphon and Data Insights Platform](https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/analytics_with_siphon_data_insights_platform/)


**Key Initiatives:**
  * **Data Insights Platform** : Sub-second query performance for SDLC metrics and usage analytics, enabling real-time dashboards and immediate feedback loops. This ClickHouse-based infrastructure serves as the foundation for all analytics capabilities across GitLab, providing unified data ingestion, processing, persistence, and querying for analytical data streams.
  * **Developer Productivity Intelligence** : Comprehensive platform for measuring AI usage, code quality trends, and engineering effectiveness with features including: 
    * AI usage analytics and code generation metrics
    * Code review efficiency and cycle time tracking
    * Deployment patterns and release health monitoring
    * Custom metric definitions and business-specific KPIs
  * **SDLC Trends Dashboard** : Executive and team-level visibility into software delivery patterns, deployment frequency, lead times, and change failure rates


### Optimize Group[](https://about.gitlab.com/direction/analytics/#optimize-group)
The Optimize group owns all DevSecOps reporting and metrics across GitLab, focusing on Value Stream Analytics and helping teams identify and eliminate waste in their software delivery process.
**Categories:**
  * Value Stream Analytics - End-to-end visibility and measurement of software delivery flow
  * DORA Metrics - Four key metrics (deployment frequency, lead time for changes, change failure rate, mean time to recovery) plus reliability
  * DevOps Reports - Comprehensive reporting across the software delivery lifecycle


**Key Reports & Capabilities:**
  * Value Stream Analytics dashboards and flow metrics
  * DORA metrics with modern extensions for AI-era development
  * [Issue Analytics](https://docs.gitlab.com/ee/user/group/#issues-analytics) - Project and group-level issue tracking insights
  * [Release Metrics](https://docs.gitlab.com/ee/user/project/releases/#release-metrics) - Release performance and deployment tracking
  * [CI/CD Analytics](https://docs.gitlab.com/ee/user/analytics/ci_cd_analytics.html) - Pipeline performance and build metrics
  * Contributor Analytics - Code contribution patterns and team productivity
  * Duo Agent Platform reports - AI agent performance and usage analytics
  * Value stream mapping and bottleneck identification
  * Cross-project and portfolio-level insights


**Strategic Direction:**
  * Evolution toward predictive analytics and proactive bottleneck detection
  * Integration with Platform Insights' Data Insights Platform for enhanced performance
  * Support for AI-amplified development patterns identified in 2025 DORA research
  * Unified DevOps reporting experience across all delivery metrics


### Analytics Instrumentation Group[](https://about.gitlab.com/direction/analytics/#analytics-instrumentation-group)
[Analytics Instrumentation](https://about.gitlab.com/direction/analytics/analytics-instrumentation) focuses on data collection, processing, and unification efforts.
**Categories:**
  * Service Ping - Aggregated usage data collection for GitLab instances
  * Application Instrumentation - SDKs and frameworks for event tracking


**Key Responsibilities:**
  * Internal event tracking framework for seamless instrumentation
  * Data unification across GitLab's architecture through the [Data Unification Steering Committee](https://gitlab.com/groups/gitlab-org/architecture/gitlab-data-analytics/-/epics/3)
  * Service Ping infrastructure and reliability
  * Event-level instrumentation support
  * Data quality, governance, and compliance


**Current Focus:**
  * Modernizing analytics infrastructure to support real-time data processing
  * Establishing single source of truth for product usage data
  * Enabling self-service instrumentation for product teams
  * Supporting migration to unified data models


The Analytics section works closely with other product groups to:
  * Provide shared infrastructure through the Data Insights Platform
  * Ensure consistent user experiences for visualization and reporting
  * Enable cross-feature data correlations and insights
  * Support the data unification vision


## Cross-stage Vision for GitLab Usage Analytics[](https://about.gitlab.com/direction/analytics/#cross-stage-vision-for-gitlab-usage-analytics)
Multiple groups and teams within GitLab produce and consume analytics data, currently through various approaches. Our long-term vision is to establish a Single Source of Truth for:
  * **How to collect data** : Unified instrumentation methods that work consistently across all features
  * **How to store data** : Centralized data architecture through the Data Insights Platform
  * **How to present data** : Shared visualization and dashboard framework
  * **How to access data** : Consistent APIs and query interfaces


This vision is being realized through:
  * The Data Unification Steering Committee's architectural decisions
  * Migration to the Data Insights Platform for real-time processing
  * Adoption of internal event tracking across product teams
  * Shared dashboard infrastructure for consistent user experiences


## How we do it[](https://about.gitlab.com/direction/analytics/#how-we-do-it)
### Personas[](https://about.gitlab.com/direction/analytics/#personas)
The primary personas we address, in priority order:
  1. **[Sasha - Software Developer](https://handbook.gitlab.com/handbook/product/personas/#sasha-software-developer)** - We address Sasha in the analytics context, focusing on adding instrumentation, debugging data collection, and supporting analytics efforts for their team.
  2. **[Parker - Product Manager](https://handbook.gitlab.com/handbook/product/personas/#parker-product-manager)** - Parker needs to understand product usage, make data-driven decisions, and report on outcomes.
  3. **[Devon - DevOps Engineer](https://handbook.gitlab.com/handbook/product/personas/#devon-devops-engineer)** - Devon needs visibility into deployment patterns, DORA metrics, and infrastructure performance.
  4. **[Cameron - Compliance Manager](https://handbook.gitlab.com/handbook/product/personas/#cameron-compliance-manager)** - Cameron needs audit trails, compliance reporting, and governance visibility.


Both internal GitLab team members and external customers share these personas and use cases. We dogfood extensively while remaining mindful that we must validate with external users, adhering to our [you're not the customer](https://handbook.gitlab.com/handbook/product/product-principles/#:~:text=You%E2%80%99re%20not%20the%20customer.) product principle.
## Right to Win[](https://about.gitlab.com/direction/analytics/#right-to-win)
We have the right to win in this Section because:
  * **Native Data Advantage** - GitLab uniquely owns the complete SDLC dataset—source code, issues, CI/CD events, deployments, security scans, and AI interactions. No standalone analytics tool has this comprehensive context, enabling correlations and insights impossible elsewhere.
  * **AI-Era Timing** - The 2025 DORA Report confirms AI is amplifying both strengths and dysfunctions in development teams. Organizations need new metrics and visibility into AI usage. We're positioned to deliver this at the moment of maximum market need.
  * **Platform Engineering Momentum** - Platform engineering is the dominant DevOps trend, and data observability is a core platform capability. We can embed analytics directly into the platform teams are building, not as a separate tool.
  * **Real-Time Processing Capability** - Our Data Insights Platform built on ClickHouse delivers sub-second query performance at scale, enabling real-time dashboards and immediate feedback loops that batch-processing competitors cannot match.
  * **Developer Trust and Distribution** - Developers trust GitLab with their code. Extending that trust to usage analytics, combined with our bottom-up adoption model, creates a natural expansion path without displacement.
  * **Competitive Gaps** - GitHub's Copilot metrics are limited to AI usage. Atlassian's DX acquisition lacks integrated SDLC data. We can deliver both AI intelligence and complete software delivery insights in one platform.
  * **Single DevOps Platform** - Our integrated platform enables unique technical capabilities: correlating code changes with deployment outcomes, linking security findings to fix times, measuring AI impact on actual delivery metrics, not just code generation.


## Product Principles[](https://about.gitlab.com/direction/analytics/#product-principles)
We will pursue this opportunity with the following principles:
  * **[Focus on Developers](https://handbook.gitlab.com/handbook/product/product-principles/#developer-first)** - Developers are key to bottom-up adoption and our dual flywheel strategy.
  * **[Works by Default](https://handbook.gitlab.com/handbook/product/product-principles/#configuration-principles)** - Basic SDLC metrics and dashboards should be available out-of-the-box in every GitLab instance.
  * **Start with the problem, not the solution** - We will identify real user needs before building. The temptation to collect all possible metrics must be resisted unless we understand who needs it and why.
  * **[Dogfood Everything](https://handbook.gitlab.com/handbook/product/product-processes/#dogfood-everything)** - We must be our own first customer, using our analytics to drive GitLab's product development.
  * **Build Foundations for Others** - Invest in shared infrastructure that enables product teams across GitLab to quickly deliver analytics features for their domains.
  * **Real-Time When Possible, Historical When Needed** - Prioritize real-time insights for operational decisions while maintaining historical depth for trends and benchmarking.
  * **Compete Through Integration** - Our differentiation comes from seamless integration with GitLab's SDLC data, not from building isolated best-of-breed analytics features.


## Where we're going[](https://about.gitlab.com/direction/analytics/#where-were-going)
### Thematic Direction[](https://about.gitlab.com/direction/analytics/#thematic-direction)
Our strategy centers on three interconnected themes:
**1. Data Completeness & Quality**
  * Unifying product usage data architecture across GitLab
  * Ensuring comprehensive instrumentation of AI-assisted development activities
  * Establishing data quality standards and monitoring
  * Enabling customer access to their usage data


**2. Intelligence & Insights**
  * Delivering modern DORA metrics with AI-era extensions
  * Providing AI usage analytics and ROI measurement
  * Building predictive capabilities for bottleneck identification
  * Creating benchmarking frameworks for industry comparison


**3. Platform & Experience**
  * Establishing shared visualization and dashboard infrastructure
  * Migrating capabilities to the Data Insights Platform for real-time performance
  * Providing consistent, intuitive experiences across all analytics features
  * Enabling self-service for common analytics needs


### 1 Year Plan[](https://about.gitlab.com/direction/analytics/#1-year-plan)
**Data Infrastructure & Unification**
  * Complete migration of core dashboards to the Data Insights Platform
  * Establish Data Insights Platform as the standard for new analytics features across GitLab
  * Drive adoption of unified instrumentation (internal event tracking) across product teams
  * Support the Data Unification Steering Committee's architectural decisions
  * Improve data quality monitoring and validation


**Developer Productivity & AI Intelligence**
  * Launch comprehensive AI usage analytics (code generation metrics, acceptance rates, usage patterns)
  * Deliver SDLC trends dashboard with deployment, lead time, and cycle time insights
  * Build engineering intelligence platform features for code review efficiency and quality trends
  * Establish SECURE metrics framework as evolution beyond DORA for AI-era development
  * Enable custom metrics and KPIs for business-specific needs


**Value Stream & Flow Metrics**
  * Integrate Value Stream Analytics with Data Insights Platform for performance improvements
  * Extend DORA metrics with modern additions (Rework Rate, Reliability)
  * Build predictive analytics for bottleneck detection
  * Create portfolio-level insights across projects
  * Support AI-amplified development workflow measurement


**Platform & Foundations**
  * Establish shared dashboard framework for consistent experiences across GitLab
  * Provide dashboard creation and management APIs for other teams
  * Build self-service data exploration capabilities
  * Enable customers to access and export their usage data
  * Create governance and compliance reporting capabilities


**Dogfooding & Internal Use**
  * Use our own analytics to measure GitLab development team productivity
  * Apply AI usage analytics to GitLab Duo adoption and effectiveness
  * Leverage SDLC trends for release planning and improvement
  * Use Value Stream Analytics to identify GitLab's own delivery bottlenecks


**Operational Excellence**
  * Maintain reliability and scalability of Service Ping and Snowplow infrastructure
  * Address technical debt in analytics instrumentation
  * Ensure data privacy and compliance across all analytics features
  * Support internal teams using analytics data for product decisions


### Competitive Strategy[](https://about.gitlab.com/direction/analytics/#competitive-strategy)
**Against GitHub Copilot Metrics:**
  * Deliver broader context beyond AI code generation
  * Show impact on actual DORA metrics and delivery performance
  * Leverage native GitLab data for deeper insights


**Against Atlassian's DX Acquisition:**
  * Provide integrated SDLC analytics, not survey-based insights
  * Offer real-time data, not periodic assessments
  * Include both AI intelligence and traditional productivity metrics


**Against Standalone Engineering Intelligence Platforms (Jellyfish, LinearB, Pluralsight Flow):**
  * Native integration eliminates data pipeline complexity
  * Access to complete GitLab SDLC context
  * No separate tool to purchase and integrate
  * Real-time processing with Data Insights Platform


## Deployment Approaches[](https://about.gitlab.com/direction/analytics/#deployment-approaches)
The Data Insights Platform (built on ClickHouse) provides the foundation for analytics capabilities. Deployment considerations:
  * **GitLab SaaS** : Fully managed, no customer deployment required
  * **GitLab Self-Managed** : Data Insights Platform components can be bundled with GitLab or deployed separately depending on [data unification architecture decisions](https://gitlab.com/groups/gitlab-org/architecture/gitlab-data-analytics/-/epics/3)
  * **Hybrid Options** : Some organizations may choose to process sensitive data on-premises while sending aggregated insights to SaaS


As the data unification work progresses, deployment will become more streamlined and these options will be refined based on customer needs and architectural decisions.
## Handbook Pages[](https://about.gitlab.com/direction/analytics/#handbook-pages)
  * [Analytics Instrumentation Group Engineering](https://handbook.gitlab.com/handbook/engineering/development/analytics/analytics-instrumentation/)
  * [Platform Insights Group Engineering](https://handbook.gitlab.com/handbook/engineering/development/analytics/platform-insights/)
  * [Optimize Group Engineering](https://handbook.gitlab.com/handbook/engineering/development/dev/manage-optimize/)
  * [Data Unification Steering Committee](https://internal.gitlab.com/handbook/product-usage-data-architecture/)


[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/analytics/template.html.md.erb) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/analytics/template.html.md.erb)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fanalytics%2F&_biz_t=1773331641670&_biz_i=%0AStage%20Direction%20-%20Analytics%0A%7C%0AGitLab%0A&_biz_n=24&rnd=778974&cdn_o=a&_biz_z=1773331641796)
suggested results