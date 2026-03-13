#  Category Direction - Dependency Management 
  1. You are here:
  2. Category Direction - Dependency Management


####  Maintained by:
[ ![Dean Agron](https://about.gitlab.com/images/gitlab-logo-extra-whitespace.png) Dean Agron  @dagron1  ](https://gitlab.com/dagron1)
The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
  * [Introduction and how you can help](https://about.gitlab.com/direction/security_risk_management/security-insights/dependency_management/#introduction-and-how-you-can-help)
  * [Overview](https://about.gitlab.com/direction/security_risk_management/security-insights/dependency_management/#overview)
  * [Vision](https://about.gitlab.com/direction/security_risk_management/security-insights/dependency_management/#vision)
  * [What is next for us](https://about.gitlab.com/direction/security_risk_management/security-insights/dependency_management/#what-is-next-for-us)
  * [Roadmap](https://about.gitlab.com/direction/security_risk_management/security-insights/dependency_management/#roadmap)
  * [Key Capabilities](https://about.gitlab.com/direction/security_risk_management/security-insights/dependency_management/#key-capabilities)
  * [Competitive Landscape](https://about.gitlab.com/direction/security_risk_management/security-insights/dependency_management/#competitive-landscape)

|   
---|---  
Stage | [Security Risk Management](https://about.gitlab.com/direction/security_risk_management/)  
Maturity | [Viable](https://about.gitlab.com/direction/#maturity)  
Features & Demos | [Our Youtube playlist](https://www.youtube.com/playlist?list=PL05JrBw4t0Kp8oA6OJ6_wm7uw0muud_mZ)  
Content Last Reviewed | `2024-12-20`  
Content Last Updated | `2024-12-20`  
### Introduction and how you can help[](https://about.gitlab.com/direction/security_risk_management/security-insights/dependency_management/#introduction-and-how-you-can-help)
Thanks for visiting this category strategy page on Dependency Management in GitLab. This category belongs to the [Security Insights](https://handbook.gitlab.com/handbook/product/categories/#security-insights-group) group of the Security Risk Management stage and is maintained by [Dean Agron](https://gitlab.com/dagron1)
This direction page is a work in progress, and everyone can contribute:
  * Please comment and contribute in the linked [issues](https://gitlab.com/groups/gitlab-org/-/epics?state=opened&page=1&sort=UPDATED_AT_DESC&label_name\[\]=Category:Dependency+Management) and [epics](https://gitlab.com/groups/gitlab-org/-/epics?state=opened&page=1&sort=UPDATED_AT_DESC&label_name\[\]=Category:Dependency+Management) on this page. Sharing your feedback directly on GitLab.com is the best way to contribute to our strategy and vision.
  * If you're a GitLab user and have direct knowledge of your need for vulnerability management, we'd especially love to hear from you.


### Overview[](https://about.gitlab.com/direction/security_risk_management/security-insights/dependency_management/#overview)
Dependency Management aims to help developers and security professionals understand exactly what 3rd-party software organizations are using to create their own applications. Vulnerabilities are ever present in 3rd-party software, surfacing a software bill of materials (SBOM) will aid in exposing what components need to be updated. Further the current regulatory landscape with references to SBOM requirements in numerous draft legislation in both the U.S. and non-U.S., executive orders and directives, customer requests, and numerous community frameworks and formatting specifications. The ability to generate and consume complete and accurate SBOMs is essential for securing our software and managing our software supply chain risk.
SBOMs have been referenced as a requirement for U.S. Federal Agencies to do business with software providers in and Executive Order, the National Cybersecurity Strategy, NIST SSDF standard, CISA, and is already appearing in draft legislation and Requests for Information (RFI). Non-U.S. public sector and commercial regulatory frameworks are following suit, and the regulatory landscape is expected to very dynamic over the coming years.
### Vision[](https://about.gitlab.com/direction/security_risk_management/security-insights/dependency_management/#vision)
Our vision captures what we want to deliver to customers in the next 10 years.
  1. The vision is to create complete, near-real time, organization-wide visibility into all 3rd-party dependencies—and any risks present.
  2. Auto-update dependencies to minimize risk.
  3. _Everyone can contribute_ to fix a vulnerable dependency.


### What is next for us[](https://about.gitlab.com/direction/security_risk_management/security-insights/dependency_management/#what-is-next-for-us)
Over the next year (major milestone 16.0-16.11), we aim to enable the abilitiy for leadership to have visibility to dependencies in any project, sub-group, group or instance level view. We also want to make sure teams can quickly triage their dependencies with filters, searching and grouping within the dependency list.
### Roadmap[](https://about.gitlab.com/direction/security_risk_management/security-insights/dependency_management/#roadmap)
We are working on multiple iterations of the Group/Sub-Group Level Dependency List. Enhancements will include:
  * Introducing a column for the License. If a license security policy is in place, show a violation icon next to the license name. When clicked, this badge should link to the policies page.
  * Introducing vulnerabilities, where vulnerabilities are listed using "X critical, X high, and X other" pattern.
  * When vulnerability count is clicked, navigate to the project-level Vulnerability Report with component filter auto-applied.
  * Introducing an info badge with the most recent version of that component currently available. This will help users understand how far behind their component is from the most recent. On hover, it would list how many more recent versions are available.


### Key Capabilities[](https://about.gitlab.com/direction/security_risk_management/security-insights/dependency_management/#key-capabilities)
**Insights** Visibility on dependencies, versioned component, vulnerability state, and adherence to compliance. The importance of insights is the ability to prioritize and triage dependencies from a project and organizational level. This allows organizations to assess risk and meet compliance to internal/external requirements.
**Remediation** A combination of manual and automated methods can be used to update and resolve dependencies. By manual is informing the user of its version, vulnerable state, and upgradability. By automated are solutions involving a MR to update the package file with version and description of changes such as changelog, CVE, and merge confidence.
**Policies** A policy can include remediation rules, authorized dependencies, CVE validation, vulnerable tolerance, compliance and more. This policy can then be flagged at the MR, continuously, or on-demand.
**Alerting** A combination of notifications to chat platforms (Slack, Teams, etc) or email alerts. Notifications include a report of a new vulnerable dependency or weekly report of dependency insights. These can be scheduled or policy-driven.
### Competitive Landscape[](https://about.gitlab.com/direction/security_risk_management/security-insights/dependency_management/#competitive-landscape)
  * [Black Duck](https://www.synopsys.com/software-integrity/software-composition-analysis-tools/black-duck-sca.html)
  * [Mend](https://www.mend.io/)
  * [Renovate](https://docs.renovatebot.com/)
  * [Sonatype](https://www.sonatype.com/)
  * [Snyk](https://snyk.io/product/open-source-security-management/)


[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/security_risk_management/security-insights/dependency_management/index.html.md) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/security_risk_management/security-insights/dependency_management/index.html.md)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fsecurity_risk_management%2Fsecurity-insights%2Fdependency_management%2F&_biz_t=1773331747501&_biz_i=%0ACategory%20Direction%20-%20Dependency%20Management%0A%7C%0AGitLab%0A&_biz_n=44&rnd=365739&cdn_o=a&_biz_z=1773331747748)
suggested results