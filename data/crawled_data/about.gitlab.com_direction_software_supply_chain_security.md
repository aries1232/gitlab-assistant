#  Product Stage Direction - Software Supply Chain Security 
  1. You are here:
  2. [GitLab Direction](https://about.gitlab.com/direction/)
  3. Product Stage Direction - Software Supply Chain Security


####  Maintained by:
[ ![Amit Shalem](https://about.gitlab.com/images/gitlab-logo-extra-whitespace.png) Amit Shalem  @ashalem  ](https://gitlab.com/ashalem)
The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
## On this page
  * [Stage Overview](https://about.gitlab.com/direction/software_supply_chain_security/#stage-overview)
    * [Groups](https://about.gitlab.com/direction/software_supply_chain_security/#groups)
  * [3 Year Stage Themes](https://about.gitlab.com/direction/software_supply_chain_security/#3-year-stage-themes)
    * [Top-down security controls](https://about.gitlab.com/direction/software_supply_chain_security/#top-down-security-controls)
    * [No compromises with compliance](https://about.gitlab.com/direction/software_supply_chain_security/#no-compromises-with-compliance)
    * [Coordinate governance across GitLab](https://about.gitlab.com/direction/software_supply_chain_security/#coordinate-governance-across-gitlab)
    * [Emphasize usability and convention over configuration](https://about.gitlab.com/direction/software_supply_chain_security/#emphasize-usability-and-convention-over-configuration)
    * [Secure the software supply chain](https://about.gitlab.com/direction/software_supply_chain_security/#secure-the-software-supply-chain)
  * [3 Year Strategy](https://about.gitlab.com/direction/software_supply_chain_security/#3-year-strategy)
  * [1 Year Plan](https://about.gitlab.com/direction/software_supply_chain_security/#1-year-plan)
    * [What We're Not Doing](https://about.gitlab.com/direction/software_supply_chain_security/#what-were-not-doing)
  * [Key Performance Metrics](https://about.gitlab.com/direction/software_supply_chain_security/#key-performance-metrics)
  * [Target Audience](https://about.gitlab.com/direction/software_supply_chain_security/#target-audience)
    * [Today](https://about.gitlab.com/direction/software_supply_chain_security/#today)
    * [Medium Term (1-2 years)](https://about.gitlab.com/direction/software_supply_chain_security/#medium-term-1-2-years)
  * [Pricing](https://about.gitlab.com/direction/software_supply_chain_security/#pricing)
    * [Free](https://about.gitlab.com/direction/software_supply_chain_security/#free)
    * [Premium](https://about.gitlab.com/direction/software_supply_chain_security/#premium)
    * [Ultimate](https://about.gitlab.com/direction/software_supply_chain_security/#ultimate)
  * [Categories](https://about.gitlab.com/direction/software_supply_chain_security/#categories)
    * [System Access](https://about.gitlab.com/direction/software_supply_chain_security/#system-access)
    * [Permissions](https://about.gitlab.com/direction/software_supply_chain_security/#permissions)
    * [Dependency Firewall](https://about.gitlab.com/direction/software_supply_chain_security/#dependency-firewall)
    * [Audit Events](https://about.gitlab.com/direction/software_supply_chain_security/#audit-events)
    * [Compliance Management](https://about.gitlab.com/direction/software_supply_chain_security/#compliance-management)
    * [Software Supply Chain Security](https://about.gitlab.com/direction/software_supply_chain_security/#software-supply-chain-security)
    * [Insider Threat](https://about.gitlab.com/direction/software_supply_chain_security/#insider-threat)
    * [Instance Resiliency](https://about.gitlab.com/direction/software_supply_chain_security/#instance-resiliency)
    * [Secrets Management](https://about.gitlab.com/direction/software_supply_chain_security/#secrets-management)
    * [Artifact Security](https://about.gitlab.com/direction/software_supply_chain_security/#artifact-security)
    * [Release Evidence](https://about.gitlab.com/direction/software_supply_chain_security/#release-evidence)
    * [User Profile](https://about.gitlab.com/direction/software_supply_chain_security/#user-profile)


**Organization-wide security vulnerability, policy, compliance, and user management**
|   
---|---  
Section | [Sec](https://about.gitlab.com/direction/security/)  
Content Last Reviewed | `2025-04-15`  
Content Last Updated | `2025-04-15`  
The Software Supply Chain Security (SSCS) stage helps organizations to reduce their overall risk by applying appropriate management and governance oversight across the entire DevSecOps lifecycle. SSCS provides management tools to secure the GitLab platform itself by restricting access to authenticated users and ensuring they are provisioned with the least amount of required privileges. To help manage and monitor risk levels, the SSCS stage provides visibility into user permissions and activity; project dependencies; security findings; and adherence to compliance standards. This visibility is then coupled with enforcement capabilities to proactively prevent risks by automating compliance and securing the software supply chain.
DevSecOpsPlanCodeBuildTestReleaseDeployOperateMonitorSecurityCompliance
Software Supply Chain Security
## Stage Overview[](https://about.gitlab.com/direction/software_supply_chain_security/#stage-overview)
The Software Supply Chain Security (SSCS) stage provides the capabilities necessary to meet security and compliance requirements for organizations at any scale.
### Groups[](https://about.gitlab.com/direction/software_supply_chain_security/#groups)
The SSCS Stage is made up of four groups:
  * [Authentication](https://about.gitlab.com/direction/software_supply_chain_security/authentication/) - Complete user lifecycle management and assurance that all points of authentication into GitLab are performed securely.
  * [Authorization](https://about.gitlab.com/direction/software_supply_chain_security/authorization/) - Ensure that users have roles and permissions that balance security and ease of performing their job within GitLab.
  * [Compliance](https://about.gitlab.com/direction/software_supply_chain_security/compliance/tactical-priorities.html) - Provide users with the tools and features necessary to achieve visibility of checks, violations and audit events across the DevSecOps lifecycle.
  * [Pipeline Security](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/) - Protect access to secrets and provide verifiable evidence that artifacts were created securely.


## 3 Year Stage Themes[](https://about.gitlab.com/direction/software_supply_chain_security/#3-year-stage-themes)
### Top-down security controls[](https://about.gitlab.com/direction/software_supply_chain_security/#top-down-security-controls)
Security teams need centralized management for their security and compliance workflows. Features such as user management, compliance labels, security policies, and the vulnerability and dependency lists need to allow for centralized management that applies across all of an organization's projects.
### No compromises with compliance[](https://about.gitlab.com/direction/software_supply_chain_security/#no-compromises-with-compliance)
SSCS capabilities will ensure that compliance regulations are strictly followed in a way that they cannot be bypassed without the proper approvals. This includes providing the necessary tools to audit, monitor, and manage the compliance controls that are enforced.
### Coordinate governance across GitLab[](https://about.gitlab.com/direction/software_supply_chain_security/#coordinate-governance-across-gitlab)
SSCS capabilities will serve as a connection point for a seamless workflow spanning across the DevSecOps lifecycle. By enabling collaboration between types of users, SSCS can help solidify the advantages GitLab has to offer as a single application. For example, these areas might include the following:
  * Facilitating a continuous experience for scanning across repositories, registries, and production environments.
  * Centralizing security and compliance controls across GitLab, including merge request approvals, anomalous user activity, and anomalous pipeline/job activity.
  * Leveraging data about production environment configuration to reduce false positives in scanners.
  * Leveraging data about vulnerabilities in development to inform and drive threat mitigation in production.


### Emphasize usability and convention over configuration[](https://about.gitlab.com/direction/software_supply_chain_security/#emphasize-usability-and-convention-over-configuration)
SSCS capabilities will be [pre-configured with reasonable defaults](https://handbook.gitlab.com/handbook/product/product-principles/#convention-over-configuration) out-of-the-box whenever possible. When not possible, they will be easy to configure either through code or through a guided UI workflow that is friendly to users without coding knowledge. Regardless of how the capabilities are configured, they will be stored as code for ease of management.
For example, GitLab's [security policy editor](https://docs.gitlab.com/ee/user/application_security/policies/#policy-editor) supports editing policies in both a `rule mode` and in `yaml mode`.
### Secure the software supply chain[](https://about.gitlab.com/direction/software_supply_chain_security/#secure-the-software-supply-chain)
SSCS capabilities allow organizations to lock down every aspect of their supply chain. This includes securely authenticating users into GitLab, hardening the GitLab platform itself, and verifying every step along the DevSecOps lifecycle as code is created, built, and deployed.
## 3 Year Strategy[](https://about.gitlab.com/direction/software_supply_chain_security/#3-year-strategy)
Building on those themes, some specific capabilities that we envision developing over the next 3 years include the following:
**Anti-Abuse**
  1. Adaptive user-based rate limiting based on a trust score.
  2. Insider threat policies to allow organizations to monitor and reduce risk.
  3. Monitoring and alert system for new URLs in a pipeline network.


**Authentication**
  1. Centralized management of users and tokens at scale, including visibility into access logs and automated notifications when credentials are required to be rotated.
  2. Reduced friction from authentication flows across GitLab including support for new methods of authenticating.
  3. Enforcement of authentication policies to increase security while minimizing disruption to automated workflows.


**Authorization**
  1. Extended support for the Principle of Least Privilege to tokens in GitLab.
  2. Improved management tools for custom roles as well as support for additional custom permissions.
  3. More robust logic before granting access to a resource - consider not only the role of the user, but also other attributes such as security policies, trust score, etc.


**Compliance**
  1. Added support to view how projects adhere to an expanded list of compliance and regulatory requirements.
  2. Support for creating customized frameworks, with related requirements and checks to meet individual organizational needs.
  3. Expanded support for out-of-the-box configurations that can be used to quickly bring projects into compliance.


**Pipeline Security**
  1. Support for a GitLab-native secrets manager.
  2. New tools to support SLSA L3 and automate generation of SLSA L3 compliant attestations.


## 1 Year Plan[](https://about.gitlab.com/direction/software_supply_chain_security/#1-year-plan)
Over the next 12 months, the SSCS stage is focused on addressing critical needs for security and compliance teams. Some of the key initiatives include the following:
  1. **Custom role improvements** - additional permissions, better management (bulk role assignment), support for LDAP sync.
  2. **Compliance standards adherence report** - added support for requirements and checks as well as support for some customization.
  3. **Enterprise token management** - gitlab.com support for the Credential Inventory, additional tools for managing access logs and for rotating tokens
  4. **GitLab Secrets Manager** - a GitLab-native secrets manager that can be used to keep sensitive data secure.
  5. **Expanded token security** - More granular permissioning for tokens across GitLab.


### What We're Not Doing[](https://about.gitlab.com/direction/software_supply_chain_security/#what-were-not-doing)
Although we will likely address many of these areas in the future (as described above in our [3 year strategy](https://about.gitlab.com/direction/software_supply_chain_security/#3-year-strategy)), we are not planning to make progress on the following initiatives in the next 12 months:
  * Attempting to build our own Security Information and Event Management (SIEM) system
  * Building analytics or algorithms to auto-tune or auto-recommend policy improvements


## Key Performance Metrics[](https://about.gitlab.com/direction/software_supply_chain_security/#key-performance-metrics)
The following metrics are used to evaluate the success of the Govern stage:
  * Anti-Abuse: Monthly active users are not relevant for this group. Instead success is measured in the observed abuse rate combined with the impact to paid conversion.
  * Authentication **Group Monthly Active Users** : This is the total number of users in a paid SAML group.
  * Authorization **Group Monthly Active Users** : The number of unique users who are assigned to a custom role.
  * Compliance **Group Monthly Active Users** : This is the total number of unique users viewing the Audit Events, Compliance Dashboard, or Credential Inventory pages in the last 28 days of the given month.
  * Pipeline Security: TBD


Note: We do not yet have a single metric to track the success of the Govern stage as a whole. This is being tracked in [this issue](https://gitlab.com/gitlab-data/product-analytics/-/issues/883).
## Target Audience[](https://about.gitlab.com/direction/software_supply_chain_security/#target-audience)
GitLab identifies who our DevSecOps application is built for utilizing the following categorization. We list our view of who we will support when in priority order.
  * 🟩- Targeted with strong support
  * 🟨- Targeted but incomplete support
  * ⬜️- Not targeted but might find value


### Today[](https://about.gitlab.com/direction/software_supply_chain_security/#today)
To capitalize on the opportunities listed above, the Govern Stage has features that make it useful to the following personas today.
  1. 🟩 Developers / Development Teams
  2. 🟩 Application Security Teams
  3. 🟨️ Compliance Specialists / Manager
  4. 🟨️ Legal Teams
  5. 🟨 Infrastructure Security Teams


### Medium Term (1-2 years)[](https://about.gitlab.com/direction/software_supply_chain_security/#medium-term-1-2-years)
As we execute our [3 year strategy](https://about.gitlab.com/direction/software_supply_chain_security/#3-year-strategy), our medium term (1-2 year) goal is to provide a single DevSecOps application that enables SecOps to work collaboratively with DevOps and development to mitigate vulnerabilities in production environments.
  1. 🟩 Developers / Development Teams
  2. 🟩 Application Security Teams
  3. 🟩 Compliance Specialists / Manager
  4. 🟩 Legal Teams
  5. 🟨 Infrastructure Security Teams


## Pricing[](https://about.gitlab.com/direction/software_supply_chain_security/#pricing)
SSCS is focused on providing governance and compliance features that span across the DevSecOps lifecycle. SSCS's tiering strategy aligns with the GitLab approach of selecting the tier based on [who cares most about the feature](https://handbook.gitlab.com/handbook/company/pricing/#three-tiers). Because Executives generally care most about governance features, it is expected that most SSCS features will land in the Ultimate tier.
##### Free[](https://about.gitlab.com/direction/software_supply_chain_security/#free)
This tier is the primary way to increase broad adoption of the SSCS stage, as well as encouraging community contributions and improving security across the entire GitLab user base.
As a general rule of thumb, features will fall in the Free tier when they meet one or more of the following criteria:
  * The feature is highly useful for an individual with a few small projects rather than meeting the needs of an organization or enterprise that is operating at scale.
  * The feature is provided by an integration with an open source project rather than being natively developed by GitLab.


##### Premium[](https://about.gitlab.com/direction/software_supply_chain_security/#premium)
This tier is not a significant part of SSCS's pricing strategy; however, a few features features that primarily appeal to Directors rather than Executives may fall into the Premium tier. One example of this is our audit event functionality that is available in this tier.
##### Ultimate[](https://about.gitlab.com/direction/software_supply_chain_security/#ultimate)
This tier is the primary focus for the SSCS stage as most SSCS features enable executives to ensure that their organization meets compliance requirements and maintains an acceptable security posture.
As a general rule of thumb, features will fall in the Ultimate tier when they meet one or more of the following criteria:
  * The feature is focused on enabling an organization or enterprise to operate at scale rather than an individual with a few small projects.
  * The feature is natively developed by GitLab rather than being provided by an open source project.


## Categories[](https://about.gitlab.com/direction/software_supply_chain_security/#categories)
##### System Access[](https://about.gitlab.com/direction/software_supply_chain_security/#system-access)
System Access provides tools to authenticate through all points of GitLab (UI, CLI, API). These tools allow you to configure what an individual/process has access to once they authenticate, determined by their role. GitLab integrates with several OmniAuth providers, LDAP, SAML, and more.
[Documentation](https://docs.gitlab.com/administration/auth/) • [Direction](https://about.gitlab.com/direction/software_supply_chain_security/authentication/system-access)
##### Permissions[](https://about.gitlab.com/direction/software_supply_chain_security/#permissions)
GitLab provides various permissions and roles in order to evaluate what access or rights an identity should have in an environment. Custom roles can also be created to allow an organization to create user roles with the precise privileges and permissions desired.
[Documentation](https://docs.gitlab.com/user/permissions/) • [Direction](https://about.gitlab.com/direction/software_supply_chain_security/authorization)
##### Dependency Firewall[](https://about.gitlab.com/direction/software_supply_chain_security/#dependency-firewall)
GitLab ensures that the dependencies stored in your package registries conform to your corporate compliance guidelines. This means you can prevent your organization from using dependencies that are insecure or out of policy. This category is planned, but not yet available.
[Direction](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/dependency_firewall/)
##### Audit Events[](https://about.gitlab.com/direction/software_supply_chain_security/#audit-events)
Audit Events track important actions within GitLab along with who performed the actions and the time in which they occurred. These events can be used in a security audit to assess risk, strengthen security measures, respond to incidents, and adhere to compliance. This category is planned, but not yet available.
Priority: high • [Documentation](https://docs.gitlab.com/administration/compliance/audit_event_reports/) • [Direction](https://about.gitlab.com/direction/software_supply_chain_security/compliance/audit-events/)
##### Compliance Management[](https://about.gitlab.com/direction/software_supply_chain_security/#compliance-management)
Compliance Management provides customers with the tools necessary to ensure and manage their compliance programs. Compliance Workflow Automation is provided to enforce custom pipelines to run on projects which have specific compliance needs. For compliance oversight, the Compliance Center provides a central location for compliance teams to manage their compliance standards adherence reporting, violations reporting, and compliance frameworks for their group. This category is planned, but not yet available.
Priority: high • [Documentation](https://docs.gitlab.com/administration/compliance/) • [Direction](https://about.gitlab.com/direction/software_supply_chain_security/compliance/compliance-management/)
##### Software Supply Chain Security[](https://about.gitlab.com/direction/software_supply_chain_security/#software-supply-chain-security)
GitLab allows you to secure your software supply chain including push rules, code scanning, SBOM management, and enforcement of compliance policies. This category is planned, but not yet available.
Priority: high • [Learn more](https://about.gitlab.com/solutions/supply-chain/) • [Documentation](https://about.gitlab.com/solutions/supply-chain/) • [Direction](https://about.gitlab.com/direction/supply-chain/)
##### Insider Threat[](https://about.gitlab.com/direction/software_supply_chain_security/#insider-threat)
Insider Threat identifies attacks and high risk behaviors by correlating different data sources and observing user behavioral patterns
[Documentation](https://docs.gitlab.com/integration/arkose/) • [Direction](https://about.gitlab.com/direction/software_supply_chain_security/anti-abuse/insider_threat/)
##### Instance Resiliency[](https://about.gitlab.com/direction/software_supply_chain_security/#instance-resiliency)
Instance Resiliency provides tools to prevent malicious activity from occurring within GitLab Instances. These tools include external pipeline validation allowing you to use an external service to validate a pipeline before it is created.
[Documentation](https://docs.gitlab.com/administration/external_pipeline_validation/) • [Direction](https://about.gitlab.com/direction/software_supply_chain_security/anti-abuse/instance_resiliency/)
##### Secrets Management[](https://about.gitlab.com/direction/software_supply_chain_security/#secrets-management)
Secure and protect access to secrets, such as API keys and passwords, to ensure that sensitive data is protected throughout your development process. This category is planned, but not yet available.
[Documentation](https://docs.gitlab.com/ci/pipelines/pipeline_security/) • [Direction](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/secrets_management/)
##### Artifact Security[](https://about.gitlab.com/direction/software_supply_chain_security/#artifact-security)
Artifact Security focuses on the hardening of artifacts, to ensure the authenticity of artifacts.
[Documentation](https://docs.gitlab.com/ci/) • [Direction](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/secure_artifacts/)
##### Release Evidence[](https://about.gitlab.com/direction/software_supply_chain_security/#release-evidence)
Release Evidence provides assurances and evidence collection that are necessary for you to trust the changes you're delivering. When a release is created, GitLab takes a snapshot of relevant release data as evidence that it occurred. This category is planned, but not yet available.
[Documentation](https://docs.gitlab.com/user/project/releases/release_evidence) • [Direction](https://about.gitlab.com/direction/release/release_evidence/)
##### User Profile[](https://about.gitlab.com/direction/software_supply_chain_security/#user-profile)
Managing your user profile and configuring what will be visible to others.
Priority: low • [Documentation](https://docs.gitlab.com/user/profile/) • [Direction](https://about.gitlab.com/direction/tenant-scale/user-profile/)
[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/software_supply_chain_security/template.html.md.erb) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/software_supply_chain_security/template.html.md.erb)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fsoftware_supply_chain_security%2F&_biz_t=1773331590960&_biz_i=%0AProduct%20Stage%20Direction%20-%20Software%20Supply%20Chain%20Security%0A%7C%0AGitLab%0A&_biz_n=12&rnd=53904&cdn_o=a&_biz_z=1773331591507)
suggested results