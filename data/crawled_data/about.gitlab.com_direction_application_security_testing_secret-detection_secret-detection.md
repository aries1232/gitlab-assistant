#  Category Direction - Secret Detection 
  1. You are here:
  2. [GitLab Direction](https://about.gitlab.com/direction/)
  3. [Product Stage Direction - Application Security Testing](https://about.gitlab.com/direction/application_security_testing/)
  4. [Secret Detection Priorities, 18.0-18.11](https://about.gitlab.com/direction/application_security_testing/secret-detection/)
  5. Category Direction - Secret Detection


The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
  * [Secret Detection](https://about.gitlab.com/direction/application_security_testing/secret-detection/secret-detection/#secret-detection)
    * [Introduction and how you can help](https://about.gitlab.com/direction/application_security_testing/secret-detection/secret-detection/#introduction-and-how-you-can-help)
    * [Overview](https://about.gitlab.com/direction/application_security_testing/secret-detection/secret-detection/#overview)
      * [The problem](https://about.gitlab.com/direction/application_security_testing/secret-detection/secret-detection/#the-problem)
      * [GitLab's solution](https://about.gitlab.com/direction/application_security_testing/secret-detection/secret-detection/#gitlabs-solution)
    * [Vision](https://about.gitlab.com/direction/application_security_testing/secret-detection/secret-detection/#vision)
    * [Strategy and Themes](https://about.gitlab.com/direction/application_security_testing/secret-detection/secret-detection/#strategy-and-themes)
    * [1 year plan](https://about.gitlab.com/direction/application_security_testing/secret-detection/secret-detection/#1-year-plan)
      * [What is next for us](https://about.gitlab.com/direction/application_security_testing/secret-detection/secret-detection/#what-is-next-for-us)
      * [What we are currently working on](https://about.gitlab.com/direction/application_security_testing/secret-detection/secret-detection/#what-we-are-currently-working-on)
      * [What we recently completed](https://about.gitlab.com/direction/application_security_testing/secret-detection/secret-detection/#what-we-recently-completed)
      * [What is Not Planned Right Now](https://about.gitlab.com/direction/application_security_testing/secret-detection/secret-detection/#what-is-not-planned-right-now)
    * [Best in Class Landscape](https://about.gitlab.com/direction/application_security_testing/secret-detection/secret-detection/#best-in-class-landscape)
      * [Key Capabilities](https://about.gitlab.com/direction/application_security_testing/secret-detection/secret-detection/#key-capabilities)
      * [Roadmap](https://about.gitlab.com/direction/application_security_testing/secret-detection/secret-detection/#roadmap)
      * [Top Competitive Solutions](https://about.gitlab.com/direction/application_security_testing/secret-detection/secret-detection/#top-competitive-solutions)
    * [Target Audience](https://about.gitlab.com/direction/application_security_testing/secret-detection/secret-detection/#target-audience)
    * [Pricing and Packaging](https://about.gitlab.com/direction/application_security_testing/secret-detection/secret-detection/#pricing-and-packaging)
    * [Analyst Landscape](https://about.gitlab.com/direction/application_security_testing/secret-detection/secret-detection/#analyst-landscape)


## Secret Detection[](https://about.gitlab.com/direction/application_security_testing/secret-detection/secret-detection/#secret-detection)
|   
---|---  
Stage | [Application Security Testing](https://about.gitlab.com/direction/application_security_testing/)  
Maturity | [Viable](https://about.gitlab.com/direction/#maturity)  
Content Last Reviewed | `2025-01-15`  
### Introduction and how you can help[](https://about.gitlab.com/direction/application_security_testing/secret-detection/secret-detection/#introduction-and-how-you-can-help)
This direction page describes GitLab's plans for the Secret Detection category, which protects you against leaking credentials, tokens, or other secrets on GitLab. Everyone can contribute to where GitLab Secret Detection goes next, and we'd love to hear from you. The best ways to participate in the conversation are to:
  * Comment or contribute to existing [Secret Detection issues](https://gitlab.com/gitlab-org/gitlab/-/issues/?sort=created_date&state=opened&label_name%5B%5D=Category%3ASecret%20Detection) in the public `gitlab-org/gitlab` issue tracker.
  * If you don't see an issue that matches, file [a new issue](https://gitlab.com/gitlab-org/gitlab/-/issues/new?issuable_template=Feature%20Proposal%20-%20basic). 
    * Post a comment that says `@gitlab-bot label ~"group::secret detection" ~"Category:Secret Detection"` so your issue lands in our triage workflow.
  * If you're a GitLab customer, discuss your needs with your account team.


### Overview[](https://about.gitlab.com/direction/application_security_testing/secret-detection/secret-detection/#overview)
GitLab Secret Detection helps prevent a critical mistake: leaking credentials or other secrets. We want GitLab to be a safe place to develop software, so we're working to make Secret Detection a standard part of the software development lifecycle (SDLC). No one should have to _think_ about secrets to be protected from _leaking_ them.
We believe that the world is safer when [everyone can contribute](https://handbook.gitlab.com/handbook/company/mission/#mission) to software security. Our customers, and those they serve, are better protected when developers and security professionals can fix potential security risks earlier.
The earliest possible time to catch a security issue is when the code is first written. GitLab sees code very early in the software development lifecycle, since we store production code and also support customer workflows (like merge requests) for pre-production development. Our group is uniquely positioned to integrate static analysis everywhere as part of a comprehensive DevSecOps platform. Our unique position allows us to embed security seamlessly and support collaboration within the tools teams already use.
The Secret Detection group's _business_ purpose is to build value for GitLab and our customers by:
  1. Driving adoption of GitLab Ultimate through integrated security tools and removing the need for "point solutions".
  2. Help teams confidently secure their code from the moment it’s written.


#### The problem[](https://about.gitlab.com/direction/application_security_testing/secret-detection/secret-detection/#the-problem)
Even experienced developers and teams can slip up and cause serious risk by committing secrets into their code repositories.
The potential damage is significant:
  * Secrets often provide access to sensitive data, production systems, or cloud resources that can be abused.
  * If a repository is public, automated tools or malicious users can detect and abuse leaked secrets—there are public sites dedicated to listing these leaks.
  * Even if a repository is private within a team or organization, leaked secrets can no longer be trusted to uniquely identify the authorized user(s) in a [non-repudiable](https://en.wikipedia.org/wiki/Non-repudiation) way.


#### GitLab's solution[](https://about.gitlab.com/direction/application_security_testing/secret-detection/secret-detection/#gitlabs-solution)
GitLab Secret Detection helps you prevent the unintentional leak of sensitive information like authentication tokens and private keys.
Secret Detection checks your Git repositories to detect secrets or credentials, then it reports potential findings. Today, Secret Detection jobs run in your CI/CD pipelines.
We want everyone to be secure, so:
  * [Parts of Secret Detection](https://docs.gitlab.com/ee/user/application_security/secret_detection/#features-per-tier) are available in every GitLab tier.
  * Secret Detection is on by default in [Auto DevOps](https://docs.gitlab.com/ee/topics/autodevops/).


In GitLab Ultimate, after you enable Secret Detection:
  * You can see and address new Secret Detection findings in [merge requests](https://docs.gitlab.com/ee/user/application_security/#view-security-scan-information-in-merge-requests).
  * Results appear in the [Vulnerability Report](https://docs.gitlab.com/ee/user/application_security/vulnerability_report/).
  * [Automatic responses](https://docs.gitlab.com/ee/user/application_security/secret_detection/automatic_response.html) help mitigate leaks as soon as they occur.
  * [Push protection](https://docs.gitlab.com/ee/user/application_security/secret_detection/secret_push_protection/) blocks secrets from being pushed to your GitLab repository.


Secret Detection doesn't target a specific language, so you can easily [enable it in any project](https://docs.gitlab.com/ee/user/application_security/secret_detection/). Our approach takes advantage of [patterns for well-identifiable credentials](https://docs.gitlab.com/ee/user/application_security/secret_detection/detected_secrets.html) like service account keys and API tokens, but also searches for more generic secret types like passwords in certain contexts.
Our approach emphasizes the value of the most comprehensive DevSecOps platform by:
  * Protecting the entire DevSecOps lifecycle, including code, issues, and other content.
  * Shifting security earlier in the development process, so everyone can contribute to security.


To learn more, check the [Secret Detection documentation](https://docs.gitlab.com/ee/user/application_security/secret_detection/).
Outside of the Secret Detection category, GitLab also offers other features that relate to secret values:
  * [Push rules](https://docs.gitlab.com/ee/user/project/repository/push_rules.html#prevent-pushing-secrets-to-the-repository) block files with certain names from being pushed to your repositories.
  * The [Secrets Management](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/secrets_management/) category focuses on enabling GitLab to use and manage secret values.


### Vision[](https://about.gitlab.com/direction/application_security_testing/secret-detection/secret-detection/#vision)
Our vision captures what we want to deliver to customers in the next 3-5 years.
  1. GitLab users are protected from credential-related security breaches.
  2. Secret detection is 100% adopted by all Ultimate namespaces.


### Strategy and Themes[](https://about.gitlab.com/direction/application_security_testing/secret-detection/secret-detection/#strategy-and-themes)
We're focusing on addressing the following user problems:
  * **Coverage** : Ensuring protection against credential leaks across all areas of a Git repository—whether in code, issues, job logs, or elsewhere.
  * **Time to Remediate** : Reducing the amount of time between when a secret is leaked and when it no longer poses a threat.
  * **Prioritization** : Enabling teams to identify and address the most critical leaks quickly.


Solving these user problems support two primary goals:
  1. Helping organizations meet security and compliance requirements within a unified DevSecOps platform.
  2. Making GitLab a secure environment for software development.


### 1 year plan[](https://about.gitlab.com/direction/application_security_testing/secret-detection/secret-detection/#1-year-plan)
Over the next major milestone, 17.0 - 17.11 (May 2024 - April 2025), we will be investing in the [next generation of Secret Detection](https://gitlab.com/groups/gitlab-org/-/epics/8667). This includes: - [Push protection](https://gitlab.com/groups/gitlab-org/-/epics/11439), which blocks commits from being pushed if they contain secrets. - [Pipelineless post-receive scanning](https://gitlab.com/groups/gitlab-org/-/epics/8626), which replaces the [existing scanning system](https://docs.gitlab.com/ee/user/application_security/secret_detection/) that runs in CI/CD pipelines after content is pushed.
Specifically, we plan to focus on:
  1. [Tracking leaks better](https://gitlab.com/gitlab-org/gitlab/-/issues/387583) as they move through a codebase, to avoid repeatedly surfacing the same leaks.
  2. Speeding triage by [allowing more exceptions and ruleset customization](https://gitlab.com/groups/gitlab-org/-/epics/10325).
  3. Scanning codebases [without pipeline jobs](https://gitlab.com/groups/gitlab-org/-/epics/8626), replacing the current pipeline-based approach. This will likely involve rethinking the end-to-end [workflow](https://gitlab.com/gitlab-org/gitlab/-/issues/425994) for detected secrets. This includes providing better organization-wide visibility of possible leaks and better context as leaks are detected.


#### What is next for us[](https://about.gitlab.com/direction/application_security_testing/secret-detection/secret-detection/#what-is-next-for-us)
In the next 3 months, we are planning to:
  * [Verify validity of GitLab Secrets](https://gitlab.com/groups/gitlab-org/-/epics/13988)
  * Continue to add support for [push protection default rules](https://gitlab.com/gitlab-org/gitlab/-/issues/504680)
  * [Improve GitLab-maintained Secret Detection rulesets](https://gitlab.com/groups/gitlab-org/-/epics/14009)
  * Conduct [performance testing of secret push protection](https://gitlab.com/gitlab-org/gitlab/-/issues/480688)


We are also _looking forward_ by refining the [system architecture](https://docs.gitlab.com/ee/architecture/blueprints/secret_detection/) for pipelineless post-receive scanning. This will share significant architectural elements with the new pre-receive secret detection feature.
#### What we are currently working on[](https://about.gitlab.com/direction/application_security_testing/secret-detection/secret-detection/#what-we-are-currently-working-on)
We are currently working on:
  * [Improving GitLab-maintained Secret Detection rulesets](https://gitlab.com/groups/gitlab-org/-/epics/14009)
  * Completing [performance testing of secret push protection](https://gitlab.com/gitlab-org/gitlab/-/issues/480688)
  * Designing the vision for [validity checks for GitLab Secrets](https://gitlab.com/groups/gitlab-org/-/epics/13988) in the vulnerability report.


#### What we recently completed[](https://about.gitlab.com/direction/application_security_testing/secret-detection/secret-detection/#what-we-recently-completed)
In the last three months we releaseed [secret push protection (SPP) to general availability](https://gitlab.com/groups/gitlab-org/-/epics/13107). In addition we made enhancements to SPP including:
  1. Added audit events whenever a push protection _exclusion_ occurs. For example, we’ve detected a secret, but your _exclusion_ allowed the developer to push it anyway without being blocked.
  2. Added REST API endpoints that make it easier to enable push protection: 
     * Enable the feature in self-managed instance (so it can be enabled on project-by-project basis)
     * Check whether the feature has been enabled for a project
     * Enable the feature for a project and for all projects in a group


In early 2025, secret detection now includes remediation steps for each type of detected secret. This guidance helps you systematically address exposures and reduce the risk of security breaches. Remediation steps will appear on all vulnerabilities upon the completion of a pipeline.
Check [older release posts](https://gitlab-com.gitlab.io/cs-tools/gitlab-cs-tools/what-is-new-since/?tab=features&selectedCategories=Secret+Detection&minVersion=15_00) for our previous work in this area.
#### What is Not Planned Right Now[](https://about.gitlab.com/direction/application_security_testing/secret-detection/secret-detection/#what-is-not-planned-right-now)
  * **Repositories outside of GitLab:** We don't plan to offer protections for projects hosted outside of GitLab.
  * **Credentials not common in software:** We plan to focus on the types of credentials that are most common in DevSecOps workflows and in software development. This means we **won't** actively pursue rules that are: 
    * For services unlikely to be used in a software project.
    * Closer to Data Loss Prevention, for example searching for personally identifiable information (PII) or credit card numbers.


### Best in Class Landscape[](https://about.gitlab.com/direction/application_security_testing/secret-detection/secret-detection/#best-in-class-landscape)
_ℹ️ Best In Class (BIC) is an indicator of forecasted near-term market performance based on a combination of factors, including analyst views, market news, and feedback from the sales and product teams. It is critical that we understand where GitLab appears in the BIC landscape._
#### Key Capabilities[](https://about.gitlab.com/direction/application_security_testing/secret-detection/secret-detection/#key-capabilities)
Secret Detection products should:
  * Help developers avoid making leaks in the first place.
  * Enable quick responses to any leaks that are made.
  * Deliver trustworthy, accurate findings, with appropriate priority, so that the right findings are remediated quickly.
  * Automatically respond to leaks, without human intervention, when possible.
  * Provide security users with overall visibility into exposures anywhere within their organization.


#### Roadmap[](https://about.gitlab.com/direction/application_security_testing/secret-detection/secret-detection/#roadmap)
See our [prioritized roadmap here](https://about.gitlab.com/direction/application_security_testing/secret-detection/#priorities).
In addition to those main themes, we are exploring additional detection techniques including:
  * Checks for whether detected credentials are still active.
  * Machine Learning or other solutions for identifying generic or lower-confidence secrets. These secrets, which include passwords and tokens that don't have an identifiable structure, are more difficult to detect while minimizing false-positive results.


#### Top Competitive Solutions[](https://about.gitlab.com/direction/application_security_testing/secret-detection/secret-detection/#top-competitive-solutions)
There are dozens of vendors providing security detection as a standalone offering, integrated as a feature within the platforms they protect or as part of a larger solution. Here’s an overview of the top competitive tools for secret detection:
  1. [Fortify](https://www.microfocus.com/en-us/cyberres/application-security/static-code-analyzer)
  2. [Endor Labs](https://www.endorlabs.com/)
  3. [GitGuardian](https://www.gitguardian.com/)
  4. [GitHub Advanced Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security)
  5. [Gitleaks](https://github.com/gitleaks/gitleaks)
  6. [Semgrep](https://semgrep.dev/products/semgrep-secrets/)
  7. [Snyk](https://docs.snyk.io/scan-application-code/snyk-code/introducing-snyk-code/key-features/ai-engine#hardcoded-secrets)
  8. [TruffleHog Enterprise](https://trufflesecurity.com/trufflehog/)
  9. [Veracode](https://www.veracode.com/security/static-analysis-tool)


### Target Audience[](https://about.gitlab.com/direction/application_security_testing/secret-detection/secret-detection/#target-audience)
The target audience for secret detection tools includes security-focused roles like [Alex, the Security Operations Engineer](https://handbook.gitlab.com/handbook/product/personas/#alex-security-operations-engineer), and [Sam, the Security Analyst](https://handbook.gitlab.com/handbook/product/personas/#sam-security-analyst). Their primary responsibility is to protect the organization from leaked secrets, which includes responding to alerts and managing incidents involving compromised credentials. Alex and Sam are instrumental in selecting, deploying, and fine-tuning tools like Secret Detection to enhance security posture.
In contrast, [Sasha, the Software Developer](https://handbook.gitlab.com/handbook/product/personas/#sasha-software-developer), may unintentionally expose credentials while coding or pushing updates. Although Sasha prioritizes security, her main focus is on building and shipping features, so she values tools that are effective yet minimally disruptive. Secret detection tools need to support Sasha's workflow by providing seamless, reliable protection without adding burdensome processes or frequent false positives.
### Pricing and Packaging[](https://about.gitlab.com/direction/application_security_testing/secret-detection/secret-detection/#pricing-and-packaging)
At GitLab, Secret Detection is primarily included in the Ultimate tier, though basic protection features are available across all tiers. We plan to enhance the level of protection provided in every tier, while continuing to offer distinct [organization-level value](https://handbook.gitlab.com/handbook/company/pricing/#three-tiers) in Ultimate.
| Free | Premium | Ultimate  
---|---|---|---  
Pipeline Secret Detection | ✅ | ✅ | ✅  
Push Protection |  |  | ✅  
Client-side warnings (UI) | ✅ | ✅ | ✅  
Automatic Response to leaked secrets (public projects) |  |  | ✅  
### Analyst Landscape[](https://about.gitlab.com/direction/application_security_testing/secret-detection/secret-detection/#analyst-landscape)
Analysts usually include Secret Detection as a secondary feature of Application Security Testing (AST) coverage. See [Category Direction - Static Application Security Testing (SAST)](https://about.gitlab.com/direction/application_security_testing/static-analysis/sast/) for up-to-date analyst coverage.
[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/application_security_testing/secret-detection/secret-detection/index.html.md) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/application_security_testing/secret-detection/secret-detection/index.html.md)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fapplication_security_testing%2Fsecret-detection%2Fsecret-detection%2F&_biz_t=1773331769296&_biz_i=%0ACategory%20Direction%20-%20Secret%20Detection%0A%7C%0AGitLab%0A&_biz_n=49&rnd=181196&cdn_o=a&_biz_z=1773331769400)
suggested results