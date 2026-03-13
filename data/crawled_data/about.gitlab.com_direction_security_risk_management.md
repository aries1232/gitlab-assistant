#  Product Stage Direction - Security Risk Management 
  1. You are here:
  2. [GitLab Direction](https://about.gitlab.com/direction/)
  3. Product Stage Direction - Security Risk Management


####  Maintained by:
[ ![Manav Khurana](https://about.gitlab.com/images/team/manav_khurana-crop.jpg) ](https://gitlab.com/manav-gl) [ G ](https://gitlab.com/gl-product-plt) [ G ](https://gitlab.com/gl-product-leaders)
The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
## On this page
  * [Stage Overview](https://about.gitlab.com/direction/security_risk_management/#stage-overview)
    * [Stage Vision and Scope of Operations](https://about.gitlab.com/direction/security_risk_management/#stage-vision-and-scope-of-operations)
    * [Stage Strategy](https://about.gitlab.com/direction/security_risk_management/#stage-strategy)
    * [Groups and Areas of Focus](https://about.gitlab.com/direction/security_risk_management/#groups-and-areas-of-focus)
    * [Categories](https://about.gitlab.com/direction/security_risk_management/#categories)
      * [Security Policy Management](https://about.gitlab.com/direction/security_risk_management/#security-policy-management)
      * [Vulnerability Management](https://about.gitlab.com/direction/security_risk_management/#vulnerability-management)
      * [Dependency Management](https://about.gitlab.com/direction/security_risk_management/#dependency-management)
      * [Security Testing Configuration](https://about.gitlab.com/direction/security_risk_management/#security-testing-configuration)
      * [Security Asset Inventories](https://about.gitlab.com/direction/security_risk_management/#security-asset-inventories)
      * [Security Testing Integrations](https://about.gitlab.com/direction/security_risk_management/#security-testing-integrations)


**Driving Actionable Security Risk Management with Seamless Automation and Scalability**
DevSecOpsPlanCodeBuildTestReleaseDeployOperateMonitorSecurityCompliance
Security Risk Management
## Stage Overview[](https://about.gitlab.com/direction/security_risk_management/#stage-overview)
### Stage Vision and Scope of Operations[](https://about.gitlab.com/direction/security_risk_management/#stage-vision-and-scope-of-operations)
The Security Risk Management stage will deliver actionable insights and seamless workflows that empower Application Security (AppSec) and Development teams to rapidly assess risk through comprehensive visibility, intelligent prioritization, and automated resolution workflows across the software development lifecycle (SDLC).
The stage will own the end-to-end user journey, including:
  * Seamless onboarding.
  * Configuration and orchestration of our suite of analyzers.
  * Assesment, proiritization and resolution of the security risks.
  * Enhanced automation through security policies and integrations.


The Security Risk Management stage is also responsible for building and maintaining the underlying infrastructure that ensures high performance, scalability, and extensibility. This infrastructure will be foundational in driving continuous innovation, while addressing scale and efficiency needs as the landscape evolves
### Stage Strategy[](https://about.gitlab.com/direction/security_risk_management/#stage-strategy)
GitLab Security Stage stands at a unique position in the application security market by offering a broad set of integrated security scanners embedded directly within developers' daily workflows. Our strength lies in consolidating security capabilities within the platform developers already use, significantly reducing the integration costs typically associated with application security solutions. With integration across all stages of the software development lifecycle and strong AI investments, we enable security to shift left while maintaining visibility throughout the entire process, making security an accessible part of development rather than a specialized discipline requiring separate tooling.
Our strategy will focus on three key areas:
  1. Deliver an enterprise-ready solution with broad deployment capabilities across the SDLC (IDE, CI, on-demand), comprehensive asset visibility, advanced reporting, and vulnerability management workflows.
  2. Leverage the GitLab platform's advantages through integration with additional SDLC steps, utilizing our unique data for improved functionality, and enhancing capabilities with AI.
  3. Build strategic partnerships with relevant security vendors for ingestion of risks and threat inteligence for broader and improved contextual analysis


### Groups and Areas of Focus[](https://about.gitlab.com/direction/security_risk_management/#groups-and-areas-of-focus)
The SRM stage is made up of four groups:
[Security Insights](https://docs.gitlab.com/user/application_security/security_dashboard/) - Enable application security and development teams to efficiently assess, prioritize, triage, and remediate application security risks while keeping an up-to-date, comprehensive view of their applications' structure. Core areas of focus include:
  * Modern Security Dashboards to address modern application security posture management challenges
  * Vulnerability report and dependency list management improvements to allow advanced risk assessment and seamless integration as part of the GitLab platform and developers' day-to-day workflows
  * Introduction of Application/Business unit risk assessment to support modern distributed and cloud-native applications across different development teams
  * Track vulnerabilities outside of the default branch


[Security Platform Management](https://about.gitlab.com/direction/security_risk_management/security-platform-management/) - Enable application security and development teams to orchestrate and control their application security tools from within the GitLab platform, integrate seamlessly with external tools, and provide a frictionless, holistic operational experience across GitLab's suite of security offerings. Core areas of focus include:
  * Asset inventory and scanner coverage to enhance orchestration and identify security gaps
  * Simplified, scalable configuration to allow deployment of scanners across the different stages of the SDLC
  * Guided and seamless onboarding to improve time-to-value for our customers


[Security Policies](https://about.gitlab.com/direction/security_risk_management/security_policies/) - Enable Application security teams to define and enforce security policies across their organization’s fleet of applications and services. Empower developers to adhere to organizational security standards within the context of their daily workflows. Support the underlying frameworks for GitLab’s security and compliance enforcement functionality. Core areas of focus include:
  * Security and compliance pipeline enforcement of relevant jobs within GitLab pipeline that scale reliably.
  * Seamless and centralized policy management for application security team via improved accuracy, instance level management and easier management
  * Faster triage through vulnerability management workflow automation for issue tracking, auto triage, improved filtering, etc.


Security Infrastructure Group - Provide the required infrastructure and database resources to meet enterprise customer demand and required functionalities as a competitive application security platform. Core areas of focus include:
  * Next-generation Vulnerability and Dependency Data Layer, enabling faster feature development
  * Enhanced data model for vulnerabilities to support vulnerabilities as Work Items
  * Support Database Decomposition Effort


### Categories[](https://about.gitlab.com/direction/security_risk_management/#categories)
##### Security Policy Management[](https://about.gitlab.com/direction/security_risk_management/#security-policy-management)
Unified security policy management provides security and compliance teams with a way to enforce controls across their organization for all of GitLab's scanners and security technologies. Policies can be used to ensure security scanners are enforced in development team pipelines with proper configuration, all scan jobs execute without any changes or alterations, and proper approvals are provided on merge requests based on results from those findings. This category is planned, but not yet available.
Priority: medium • [Documentation](https://docs.gitlab.com/user/application_security/policies/) • [Direction](https://about.gitlab.com/direction/security_risk_management/security_policies/security_policy_management/)
##### Vulnerability Management[](https://about.gitlab.com/direction/security_risk_management/#vulnerability-management)
Vulnerability Management enables collaboration between security teams by providing a uniform interface to assess the security posture of their applications. Security teams can view, triage, trend, track, and resolve vulnerabilities detected by the various GitLab scanners. This category is planned, but not yet available.
Priority: high • [Documentation](https://docs.gitlab.com/user/application_security/security_dashboard/) • [Direction](https://about.gitlab.com/direction/security_risk_management/threat_insights/vulnerability_management/)
##### Dependency Management[](https://about.gitlab.com/direction/security_risk_management/#dependency-management)
Dependency Management allows users to review project/group dependencies and key details about those dependencies, including their vulnerabilities, licenses, and packager. This category is planned, but not yet available.
Priority: high • [Documentation](https://docs.gitlab.com/user/application_security/dependency_list/) • [Direction](https://about.gitlab.com/direction/security_risk_management/security-insights/dependency_management/)
##### Security Testing Configuration[](https://about.gitlab.com/direction/security_risk_management/#security-testing-configuration)
Seamlessly configure and onboard application security testing. This category is planned, but not yet available.
[Direction](https://about.gitlab.com/direction/security_risk_management/security-platform-management/security-testing-configuration)
##### Security Asset Inventories[](https://about.gitlab.com/direction/security_risk_management/#security-asset-inventories)
Identify security gaps by understanding which assets are covered by security testing, and when and where security tests have run. This category is planned, but not yet available.
[Direction](https://about.gitlab.com/direction/security_risk_management/security-platform-management/security-asset-inventories)
##### Security Testing Integrations[](https://about.gitlab.com/direction/security_risk_management/#security-testing-integrations)
Integrate external security testing tools for complete visibility and consolidation of your security workflows. This category is planned, but not yet available.
[Direction](https://about.gitlab.com/direction/security_risk_management/security-platform-management/security-testing-integrations)
_  
Last Updated: 2025-03-18_
[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/security_risk_management/template.html.md.erb) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/security_risk_management/template.html.md.erb)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fsecurity_risk_management%2F&_biz_t=1773331595153&_biz_i=%0AProduct%20Stage%20Direction%20-%20Security%20Risk%20Management%0A%7C%0AGitLab%0A&_biz_n=13&rnd=867291&cdn_o=a&_biz_z=1773331595416)
suggested results