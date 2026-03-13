#  Category Direction - GitLab.com 
  1. You are here:
  2. [GitLab Direction](https://about.gitlab.com/direction/)
  3. [Product Section Direction - Core Platform](https://about.gitlab.com/direction/core_platform/)
  4. Category Direction - GitLab.com


The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
  * [Overview](https://about.gitlab.com/direction/core_platform/dotcom/#overview)
  * [Market Opportunity](https://about.gitlab.com/direction/core_platform/dotcom/#market-opportunity)
  * [Competitive Landscape](https://about.gitlab.com/direction/core_platform/dotcom/#competitive-landscape)
  * [Challenges](https://about.gitlab.com/direction/core_platform/dotcom/#challenges)
  * [Target Customer](https://about.gitlab.com/direction/core_platform/dotcom/#target-customer)
  * [Top Customer Success/Sales issues](https://about.gitlab.com/direction/core_platform/dotcom/#top-customer-successsales-issues)
  * [Top user issues](https://about.gitlab.com/direction/core_platform/dotcom/#top-user-issues)
  * [Top Strategy Items](https://about.gitlab.com/direction/core_platform/dotcom/#top-strategy-items)
  * [1-Year Plan](https://about.gitlab.com/direction/core_platform/dotcom/#1-year-plan)
    * [Improved Usability for Admins](https://about.gitlab.com/direction/core_platform/dotcom/#improved-usability-for-admins)
    * [Availability and Performance](https://about.gitlab.com/direction/core_platform/dotcom/#availability-and-performance)
    * [Enterprise-Grade Security and Compliance](https://about.gitlab.com/direction/core_platform/dotcom/#enterprise-grade-security-and-compliance)
    * [Dogfooding](https://about.gitlab.com/direction/core_platform/dotcom/#dogfooding)
    * [Foundational Work](https://about.gitlab.com/direction/core_platform/dotcom/#foundational-work)
    * [What we're not doing](https://about.gitlab.com/direction/core_platform/dotcom/#what-were-not-doing)
  * [Success Metrics](https://about.gitlab.com/direction/core_platform/dotcom/#success-metrics)
  * [Footnotes](https://about.gitlab.com/direction/core_platform/dotcom/#footnotes)


## Overview[](https://about.gitlab.com/direction/core_platform/dotcom/#overview)
This page contains the strategy for GitLab's multi-tenant SaaS offering, GitLab.com. While this page is maintained by the [Infrastructure Product Manager](https://handbook.gitlab.com/handbook/engineering/infrastructure/product-management/), [GitLab.com is not a specific role](https://about.gitlab.com/company/team/structure/#gitlabcom-isnt-a-role) and customer success on GitLab.com is a shared responsibility across GitLab team members.
GitLab.com runs the same codebase as self-managed GitLab without customers [needing to install, administer, and operate the service](https://about.gitlab.com/pricing/feature-comparison/). GitLab.com is fully-managed by GitLab, Inc and is primarily hosted in [Google Cloud Platform in the United States](https://handbook.gitlab.com/handbook/engineering/infrastructure/production/architecture/). The service provides both free and paid options for individuals and teams as well as the added bonus of [free compute minutes in each tier](https://about.gitlab.com/pricing/).
The worldwide DevOps software tools market is expected to grow rapidly (15.6% 2021-2026 CAGR) [according to IDC](https://www.idc.com/getdoc.jsp?containerId=US48599322). IDC states that SaaS-based delivery of DevOps tools (19% 2021-2026 CAGR) has overtaken on-premise/other software (11.3% 2021-2026 CAGR).[1](https://about.gitlab.com/direction/core_platform/dotcom/#footnotes) This represents a large opportunity for GitLab, and our SaaS services.
When evaluating GitLab.com, enterprises tell us they need more sophisticated controls to better manage their users, groups, and projects on GitLab.com, increased availability and performance of the overall service, and security enhancements like industry standard certifications and customer audit logs.
## Market Opportunity[](https://about.gitlab.com/direction/core_platform/dotcom/#market-opportunity)
[According to IDC](https://www.idc.com/getdoc.jsp?containerId=US48599322), the worldwide DevOps software tools market will grow from $15.8B in 2021 to $32.8B in 2026. IDC predicts a stronger than previously expected adoption of SaaS-delivered solutions over this time period as part of a growing preference among enterprises for cloud-based architectures, which provide greater operational flexibility. Adoption of DevOps tools that enable better collaboration among development teams is also expected to accelerate over this time period according to IDC, as more work is done remotely due to the global pandemic. IDC predicts that the market for SaaS-based DevOps tools (52% of the market in 2021) will continue to accelerate and account for **$20.0B in revenue** (or 61% of DevOps software tools market) by 2026.[1](https://about.gitlab.com/direction/core_platform/dotcom/#footnotes) As a result, over this time period we expect to see an increase in existing self-managed users migrating to GitLab.com as well as the majority of prospective customers preferring SaaS over self-managed deployment.
## Competitive Landscape[](https://about.gitlab.com/direction/core_platform/dotcom/#competitive-landscape)
The expected shift in deployment preference to SaaS based cloud services in the upcoming years presents a large and growing opportunity for hosted git repository providers among which the major vendors are GitHub (56% usage share), BitBucket (30%), and GitLab.com (9%) [according to Bitrise repository counts](https://blog.bitrise.io/state-of-app-development-in-2019).
As the largest host of source-code in the world with over 100 million repositories, GitHub has high brand recognition and boasts a thriving developer community. GitHub can tap into the strengths of its parent company, Microsoft, by offering discounts to customers who commit to Azure, cross-selling GitHub to existing Azure customers, and deep integration with Azure services to make it easier to adopt GitHub. While GitHub offers strong Source Code Management capabilities, its CI/CD offering, Actions (launched in 2018) is less mature than competitors. GitHub is missing critical [planning features](https://about.gitlab.com/competition/github/) like milestones, issue weights, and due dates, all of which are available in GitLab. Finally, GitHub does not come with a [built-in deployment platform](https://about.gitlab.com/competition/github/) (unlike GitLab which provides out-of-the-box integration with Kubernetes) requiring customers to leverage third-party solutions to fill the gap.
Bitbucket saw a 3% decline in market share YoY according to Bitrise, but offers the advantages of tight integration with the rest of the Atlassian product suite including collaboration tools like Jira and Confluence.
Compared to competitors, GitLab.com offers a broader feature set providing customers with a complete, end-to-end DevOps platform delivered as a single application. Improved integration between Atlassian tools and GitLab will make it easier for customers to use solutions across the two ecosystems (e.g. support for Jira in GitLab) and provide a strong alternative to customers who don’t want to be locked into the Microsoft ecosystem.
IDC predicts continued M&A activity in the DevOps market through 2024 as larger vendors look to strengthen their portfolios to meet the needs of customers who want a single solution for their entire DevOps lifecycle. While this may consolidate competitive pressure, it may also drive adoption of GitLab as DevOps customers look to [standardize their toolchains](https://devops.com/challenges-devops-standardization/) around established players.
## Challenges[](https://about.gitlab.com/direction/core_platform/dotcom/#challenges)
We see the following challenges to growing paid-user adoption of GitLab.com in FY22:
  1. Budget constraints of DevOps Customers due to economic uncertainty over the next year
  2. Challenges unique to the SaaS offering 
    1. Controlling hosting-costs and maintaining sustainable margins across each pricing tier
    2. Feature parity with Self-Managed: ensuring newly-released features are immediately made available at the group level for SaaS users
    3. Infrastructure team balancing priority of KTLO ("keep the lights on") projects vs. delivering features needed by enterprises
    4. Stage teams balancing priority of .com customer needs vs. needs of self-managed customers
    5. Stage teams designing for multi-tenancy and [considering cost, operational, user experience, and performance impact of their feature set](https://handbook.gitlab.com/handbook/product/product-manager-role/#cost-profile-and-user-experience) throughout the product lifecycle with support from the Infrastructure Department.
  3. Increased competitive pressure from Microsoft 
    1. Synergies/price discounts with Azure


## Target Customer[](https://about.gitlab.com/direction/core_platform/dotcom/#target-customer)
We [segment customers](https://handbook.gitlab.com/handbook/sales/field-operations/gtm-resources/#segmentation) based on organization size (number of employees): large, mid-market, and SMB (small business). Thus far, we’ve had success attracting the SMB and mid-market segments by offering significant free tier value (including private repos and build minutes). We are working on a variety of optimizations to reduce costs of supporting free users as well as changes and experiments to improve the conversion rate of free customers into paid tiers, all of which we will continue into next year.
Compared to the SMB and mid-market segments, we’ve seen less adoption of GitLab.com among large enterprises. As large enterprises look to increase usage of SaaS delivered DevOps solutions and tools to enable collaboration among remote development teams through 2024, we believe this segment offers a substantial revenue opportunity. As a result, we will target large enterprise customers in FY22. While we will continue efforts towards making free users a cost effective customer acquisition source and meeting margin targets across each tier, we will now also focus on growing adoption of paid tiers by increasing our win rate of deals involving large enterprise customers.
## Top Customer Success/Sales issues[](https://about.gitlab.com/direction/core_platform/dotcom/#top-customer-successsales-issues)
To track key adoption blockers among enterprise customers, we use the label ~"GitLab.com Enterprise Readiness". The top issues needed to achieve enterprise readiness for GitLab.com are tracked on the following two boards:
  * [Within GitLab-org project](https://gitlab.com/groups/gitlab-org/-/boards/2037713?&label_name\[\]=GitLab.com%20Enterprise%20Readiness)
  * [Within GitLab-com project](https://gitlab.com/groups/gitlab-com/-/boards/2037722?&label_name\[\]=GitLab.com%20Enterprise%20Readiness)


## Top user issues[](https://about.gitlab.com/direction/core_platform/dotcom/#top-user-issues)
Customer needs generally fall into three categories:
  1. improved usability for administrators to better manage users across their organization on gitlab.com,
  2. increased performance and availability, and
  3. security enhancements.


Across these areas, customers want the same capabilities in self-managed [to be made available on GitLab.com](https://about.gitlab.com/pricing/feature-comparison/). Key examples include [access to audit logs](https://gitlab.com/groups/gitlab-org/-/epics/1217), and a [credentials inventory](https://docs.gitlab.com/ee/administration/credentials_inventory.html#credentials-inventory).
## Top Strategy Items[](https://about.gitlab.com/direction/core_platform/dotcom/#top-strategy-items)
A critical component of SaaS growth relies on focusing on the needs of enterprise customers. To improve our market position and increase our .com win rate, we must address key adoption blockers and feature gaps for this market segment. To accomplish this, we will focus on enterprise-readiness for GitLab.com.
## 1-Year Plan[](https://about.gitlab.com/direction/core_platform/dotcom/#1-year-plan)
The 12-month customer-facing roadmap for GitLab.com to achieve enterprise-readiness is presented below. Where applicable, we also highlight any supporting initiatives that need to be completed to deliver each roadmap item.
### Improved Usability for Admins[](https://about.gitlab.com/direction/core_platform/dotcom/#improved-usability-for-admins)
  1. Better tools for admins to manage their users 
    1. e.g. [Creating group-specific profiles using personas to enforce name and email address formats](https://gitlab.com/groups/gitlab-org/-/epics/4335)
    2. e.g. [Group level Credential Inventory](https://gitlab.com/groups/gitlab-org/-/epics/4123)
  2. [More control over how workspaces are isolated](https://gitlab.com/groups/gitlab-org/-/epics/3191)
  3. [Feature parity across instance/group levels](https://gitlab.com/groups/gitlab-org/-/epics/4257). Additionally, for net-new functionality moving forward, we will strive to [avoid building instance-level features when possible](https://handbook.gitlab.com/handbook/product/product-principles/#avoid-instance-level-features)


We will achieve this by helping the [Foundations Stage](https://handbook.gitlab.com/handbook/product/categories/#foundations-stage) better capture the opportunity and customer demand for each of these features. To learn more about how the Foundations stage is planning to close feature gaps needed to achieve enterprise readiness, see [this section in the Foundations direction page](https://about.gitlab.com/direction/foundations/#gitlabcom).
### Availability and Performance[](https://about.gitlab.com/direction/core_platform/dotcom/#availability-and-performance)
  1. [Consistently achieving a weighted SLA of 99.95%](https://gitlab.com/gitlab-com/www-gitlab-com/-/issues/8024)
  2. Improved overall [performance](https://gitlab.com/groups/gitlab-com/-/epics/734)
    1. We will achieve this by partnering with stage teams to prioritize performance improvements across the GitLab application.
  3. [Improved feature release communication](https://gitlab.com/gitlab-org/gitlab/-/issues/215227)
    1. We will achieve this via partnership with the GitLab marketing team.
  4. [Disaster recovery and multi-region failover](https://gitlab.com/gitlab-com/gl-infra/infrastructure/-/issues/9232)
  5. Increased redundancy of repository storage via [Gitaly Cluster](https://docs.gitlab.com/ee/administration/gitaly/praefect.html)
    1. Supporting Infrastructure initiative: [Drive Gitaly Cost Optimizations](https://gitlab.com/gitlab-com/gl-infra/infrastructure/-/issues/8422)
  6. Enabling additional regional instances of GitLab.com (locations to be determined based on customer demand) 
    1. Supporting Infrastructure initiative: [Kubernetes Migration](https://handbook.gitlab.com/handbook/engineering/infrastructure/production/kubernetes/gitlab-com/)


### Enterprise-Grade Security and Compliance[](https://about.gitlab.com/direction/core_platform/dotcom/#enterprise-grade-security-and-compliance)
  1. [Customer Audit Logs](https://gitlab.com/groups/gitlab-org/-/epics/1217)
  2. Industry-standard security certifications
  3. [Granular User Permissions](https://gitlab.com/groups/gitlab-org/-/epics/4035)
  4. Improved Visibility and control on user access


We will achieve this by [partnering with the Security Department](https://gitlab.com/gitlab-com/gl-infra/infrastructure/-/issues/10982) to drive delivery of these features across the appropriate stage groups.
### Dogfooding[](https://about.gitlab.com/direction/core_platform/dotcom/#dogfooding)
In FY22 we will continue to prioritize [Dogfooding efforts](https://handbook.gitlab.com/handbook/engineering/infrastructure/#dogfooding) to
  1. help Stage teams [improve the maturity of their features](https://about.gitlab.com/direction/#maturity) for enterprise customers and
  2. if possible, promote feature re-use to avoid having to re-build capabilities from scratch.


As part of our Dogfooding efforts in FY22, one of the major questions we'd like to answer is: can we leverage [Geo](https://gitlab.com/groups/gitlab-org/-/epics/575) to help meet our Disaster Recovery targets for GitLab.com?
### Foundational Work[](https://about.gitlab.com/direction/core_platform/dotcom/#foundational-work)
Besides closing feature gaps for enterprise customers, in FY22 we will also invest in foundational projects within the Infrastructure department to improve overall [efficiency of operating GitLab.com](https://handbook.gitlab.com/handbook/engineering/infrastructure/performance-indicators/). This bucket of work includes projects like:
  1. Improving our environments such as staging
  2. Tackling technical debt (e.g. Moving to a newer version of chef-server, Migrating old instances)
  3. [Automated rollbacks](https://gitlab.com/groups/gitlab-com/gl-infra/-/epics/281) and blue-green deployments


### What we're not doing[](https://about.gitlab.com/direction/core_platform/dotcom/#what-were-not-doing)
The following items are currently not in scope for FY22:
  1. [Federation](https://gitlab.com/gitlab-org/gitlab/-/issues/6468) between GitLab.com and self-managed instances.


## Success Metrics[](https://about.gitlab.com/direction/core_platform/dotcom/#success-metrics)
To ensure we are increasing our market share and gaining user adoption while maintaining a financially healthy and sustainable business we will track the following success metrics.
  1. Primary Performance Indicator: 
    1. Paid GMAU (Paid Monthly active users for gitlab.com)
  2. Secondary Performance Indicators: 
    1. .com win rate, that is the number of won opportunities as the percentage of total opportunities in which customers prefer SaaS.
    2. Gross Margin % by tier where profit is defined as (subscription revenue + consumption revenue) - (gitlab.com hosting + infra team + cust support cost)
    3. [Customer Retention](https://app.periscopedata.com/app/gitlab/412223/GitLab.com-Customer-Retention)
    4. [Free to paid user conversion rate](https://app.periscopedata.com/app/gitlab/710777/\[WIP\]-Infra-PM-Dashboard?widget=9417909&udv=0)
  3. Supporting Performance Indicators: 
    1. [Availability](https://handbook.gitlab.com/handbook/engineering/infrastructure/performance-indicators/#gitlab-com-availability)
    2. [Performance](https://handbook.gitlab.com/handbook/engineering/infrastructure/performance-indicators/#gitlab-com-performance)
    3. [Disaster Recovery Time-to-recover](https://handbook.gitlab.com/handbook/engineering/infrastructure/performance-indicators/#disaster-recovery-dr-time-to-recover)


## Footnotes[](https://about.gitlab.com/direction/core_platform/dotcom/#footnotes)
  1. IDC, Worldwide DevOps Software Tools Forecast, 2022–2026, Doc # US48599322, July 2022


[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/core_platform/dotcom/index.html.md) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/core_platform/dotcom/index.html.md)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fcore_platform%2Fdotcom%2F&_biz_t=1773332142021&_biz_i=%0ACategory%20Direction%20-%20GitLab.com%0A%7C%0AGitLab%0A&_biz_n=129&rnd=13315&cdn_o=a&_biz_z=1773332142175)
suggested results