# Application Security Testing Sub-Department
The Application Security Testing engineering sub-department is responsible for the [Application Security Testing Stage](https://handbook.gitlab.com/handbook/product/categories/#sec-section) of the product.
## Vision[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#vision)
To provide content and tools to support the best possible assessment at the earliest possible moment.
Following our [single application](https://handbook.gitlab.com/handbook/product/categories/gitlab-the-product/single-application/) paradigm, we integrate and build scanning tools to supply security and compliance assessment data to the main GitLab application where we develop our vulnerability management system and other features. While it might be technically feasible, we do not aim at building standalone products that provide this data independently from the GitLab application.
For more details about the vision for this area of the product, see the [Secure stage](https://about.gitlab.com/stages-devops-lifecycle/#secure) page.
## Mission[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#mission)
To support the success of GitLab by developing highly usable, hiqh quality tools for customers to build more secure software.
The Application Security Testing team works on GitLab’s [Secure stage](https://about.gitlab.com/stages-devops-lifecycle/#secure).
## AI Prompts[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#ai-prompts)
## Sub-department development people leaders[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#sub-department-development-people-leaders)
Name | Role  
---|---  
To contact Application Security Testing stage development people leaders, use the following aliases:
  * GitLab: `@gitlab-org/secure/managers`
  * Slack: `@s_application_security_testing_managers`


## Team Members[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#team-members)
The following people are permanent members of the Application Security Testing Sub-Department:
### Composition Analysis[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#composition-analysis)
Team Page: [Composition Analysis](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/composition-analysis/)
Name | Role  
---|---  
Name | Role  
---|---  
### Static Analysis[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#static-analysis)
Team Page: [Static Analysis](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/static-analysis/)
Name | Role  
---|---  
### Dynamic Analysis[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#dynamic-analysis)
Team Page: [Dynamic Analysis](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/dynamic-analysis/dynamic-analysis/)
Name | Role  
---|---  
### Vulnerability Research[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#vulnerability-research)
Team Page: [Vulnerability Research](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/vulnerability-research/)
Name | Role  
---|---  
## Stable Counterparts[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#stable-counterparts)
The following members of other functional teams are our stable counterparts:
Name | Role  
---|---  
[![Albina Yusupova](https://about.gitlab.com/images/team/albinayusupova-crop.jpg)Albina Yusupova](https://handbook.gitlab.com/handbook/company/team/#albiyusupova) |  [Backend Engineer](https://handbook.gitlab.com/job-families/engineering/development/backend/intermediate), Secure:Composition Analysis  
[![Arpit Gogia](https://about.gitlab.com/images/gitlab-logo-extra-whitespace.png)Arpit Gogia](https://handbook.gitlab.com/handbook/company/team/#arpitgogia) | [Backend Engineer, Secure:Dynamic Analysis](https://handbook.gitlab.com/job-families/engineering/development/backend/)  
[![Fernando Cardenas](https://about.gitlab.com/images/gitlab-logo-extra-whitespace.png)Fernando Cardenas](https://handbook.gitlab.com/handbook/company/team/#fernando-c) | [Senior Frontend Engineer, Secure:Composition Analysis](https://handbook.gitlab.com/job-families/engineering/development/frontend/)  
[![Hannah Baker](https://about.gitlab.com/images/team/hbaker-crop.jpg)Hannah Baker](https://handbook.gitlab.com/handbook/company/team/#hbakergitlab) | [Backend Engineer, Secure:Dynamic Analysis](https://handbook.gitlab.com/job-families/engineering/development/backend/)  
[![Igor Frenkel](https://about.gitlab.com/images/team/igorfrenkel-crop.jpg)Igor Frenkel](https://handbook.gitlab.com/handbook/company/team/#ifrenkel) |  [Senior Backend Engineer](https://handbook.gitlab.com/job-families/engineering/development/backend/#secure), Secure:Composition Analysis  
[![Mike Eddington](https://about.gitlab.com/images/team/michaeleddington-crop.jpg)Mike Eddington](https://handbook.gitlab.com/handbook/company/team/#mikeeddington) | [Staff Backend Engineer, Secure:Dynamic Analysis](https://handbook.gitlab.com/job-families/engineering/development/backend/)  
[![Nick Ilieskou](https://about.gitlab.com/images/team/nickilieskou-crop.jpg)Nick Ilieskou](https://handbook.gitlab.com/handbook/company/team/#nilieskou) |  [Senior Backend Engineer](https://handbook.gitlab.com/job-families/engineering/development/backend/senior/), Secure:Composition Analysis  
[![Olivier Gonzalez](https://about.gitlab.com/images/team/oliviergonzalez-crop.jpg)Olivier Gonzalez](https://handbook.gitlab.com/handbook/company/team/#gonzoyumo) |  [Staff Backend Engineer](hhttps://handbook.gitlab.com/job-families/engineering/development/backend/#staff-backend-engineer), Secure:Composition Analysis  
[![Orin Naaman](https://about.gitlab.com/images/gitlab-logo-extra-whitespace.png)Orin Naaman](https://handbook.gitlab.com/handbook/company/team/#onaaman) |  [Backend Engineer](https://handbook.gitlab.com/job-families/engineering/development/backend/), Secure:Composition Analysis  
[![Russell Dickenson](https://about.gitlab.com/images/team/russelldickenson-crop.jpg)Russell Dickenson](https://handbook.gitlab.com/handbook/company/team/#rdickenson) |  [Senior Technical Writer](https://handbook.gitlab.com/job-families/product/technical-writer/), Secure  
[![Zamir Martins Filho](https://about.gitlab.com/images/team/ZamirMartinsFilho-crop.jpg)Zamir Martins Filho](https://handbook.gitlab.com/handbook/company/team/#zmartins) |  [Senior Fullstack Engineer](https://handbook.gitlab.com/job-families/engineering/development/fullstack/), Secure:Composition Analysis  
## Secure Team[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#secure-team)
The Application Security Testing Team is responsible for the security checks features in the GitLab platform, and maps to the [application security testing](https://handbook.gitlab.com/handbook/product/categories/#application-security-testing-stage) transversal stage. You can learn more about our approach on the [Application Security Testing Vision](https://about.gitlab.com/direction/application_security_testing/) page.
The features provided by the Application Security Testing Team are mostly present at the pipeline level, and mostly available as container images. This particularity shapes our processes and QA, which differs a bit from the other stages.
### Security Products[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#security-products)
We still refer to “ _Security Products_ ” as the tools developed by the Application Security Testing Team. Hence the home of our projects in GitLab: <https://gitlab.com/gitlab-org/security-products/>.
We strive to maintain a consistent User Experience across our Security Products but we do not enforce consistency at the implementation level. Each group faces its own challenges and is in the best position to make the technical choices it deems are the most suitable to achieve its goals. While [UX inconsistencies are considered as bugs](https://handbook.gitlab.com/handbook/product-development/how-we-work/issue-triage/#severity), we rely on individual teams to make smart decisions about when consistency is important and when divergence makes more sense — either because the divergence itself creates a better experience or because of velocity considerations.
### Domains of Expertise[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#domains-of-expertise)
#### SAST[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#sast)
[SAST](https://docs.gitlab.com/ee/user/application_security/sast/) (_Static Application Security Testing_) refers to static code analysis. GitLab leverages the power of various opensource tools to provide a wide range of checks for many languages and support. These tools are wrapped inside docker images which ensure we get a standard output from there. An orchestrator, [developed by GitLab](https://gitlab.com/gitlab-org/security-products/sast), is in charge of running these images, and gathering all the data needed to generate the final report.
#### DAST[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#dast)
[DAST](https://docs.gitlab.com/ee/user/application_security/dast/) (_Dynamic Application Security Testing_) is used to hit a live application. Because some vulnerabilities can only be detected once all the code is actually running, this method complements the static code analysis. DAST is relying on [OWASP Zed Attack Proxy Project](https://gitlab.com/gitlab-org/security-products/zaproxy), modified by GitLab to enable authentication.
#### Dependency Scanning[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#dependency-scanning)
[Dependency Scanning](https://docs.gitlab.com/ee/user/application_security/dependency_scanning/) is used to detect vulnerabilities introduced by external dependencies in the application. Because a large portion of the code shipped to production is actually coming from third-party libraries, it’s important to monitor them as well. Dependency Scanning is relying mostly on the Gemnasium engine.
#### Fuzz Testing[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#fuzz-testing)
Coverage-guided fuzzing and API fuzzing are used to automatically input data into applications or web apis that has the potential to cause crashes or bugs. Coverage-guided fuzzing relies on open-sourced [language-specific fuzzers](https://gitlab.com/gitlab-org/security-products/analyzers/fuzzers). API Fuzzing is based on a [proprietary GitLab engine](https://gitlab.com/gitlab-org/security-products/analyzers/api-fuzzing-src).
#### License Compliance[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#license-compliance)
[License Compliance](https://docs.gitlab.com/ee/user/compliance/license_approval_policies.html) helps with the licenses introduced by third-party libraries in the application. Licence management relies on the [LicenseFinder](https://github.com/pivotal/LicenseFinder) gem.
#### Vulnerability Research[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#vulnerability-research-1)
The [Vulnerability Research](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/vulnerability-research/) team’s purpose is to perform research and develop proofs of concepts that increase the capabilities and effectiveness of the [Secure stage](https://about.gitlab.com/stages-devops-lifecycle/secure/).
### Skills[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#skills)
Because we have a wide range of domains to cover, it requires a lot of different expertises and skills:
Technology skills | Areas of interest  
---|---  
Ruby on Rails | Backend development  
Go | SAST, Dependency Scanning, DAST  
Python | DAST  
SQL (PostgreSQL) | Dependency Scanning / all  
Docker | Container Scanning / all  
C# | API Security  
Our team also must have a good sense of security, with at least basic skills in [application security](https://en.wikipedia.org/wiki/Application_security).
We provide tools for many different languages (ex: [sast](https://docs.gitlab.com/ee/user/application_security/sast/#supported-languages-and-frameworks), [dependency scanning](https://docs.gitlab.com/ee/user/application_security/dependency_scanning/#supported-languages-and-dependency-managers), [license compliance](https://docs.gitlab.com/ee/user/compliance/license_approval_policies.html#supported-languages-and-package-managers)). It means our team is able to understand the basics of each of these languages, including their package managers. We maintain [tests projects](https://gitlab.com/gitlab-org/security-products/tests) to ensure our features are working release after release for each of them.
### Release process[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#release-process)
See [Versioning and release process](https://docs.gitlab.com/ee/development/sec/analyzer_development_guide.html).
### QA process[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#qa-process)
See [QA Process](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/qa_process/) for more info.
### Vulnerability Management process[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#vulnerability-management-process)
#### Automation[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#automation)
We use [The Vulnmapper tool](https://gitlab.com/gitlab-com/gl-security/product-security/vulnerability-management/vulnerability-management-internal/vulnmapper) to automate our vulnerability lifecycle, it performs these actions for us
  1. Creating Actionable Tracking issues with appropriate labels to clarify ownership, operating syste ect. This is filtered to FedRAMP Issues only at this stage.
  2. Creating Deviation Request issues for FedRAMP related security issues that should have one.
  3. Updating & Closing Issues when a vulnerability is resolved.


VulnMapper does not close vulnerabilities, this is performed by [Auto resolve vulnerabilites](https://gitlab.com/gitlab-org/gitlab-org-security-policy-project/-/blob/main/.gitlab/security-policies/policy.yml?ref_type=heads#L211) security policy at the `gitlab-org` level is configured to resolve vulnerabilities.
#### Automation failures[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#automation-failures)
It’s possible that our security automation tooling may [fail](https://gitlab.com/gitlab-org/security-products/release/-/pipelines?page=1&scope=all&status=failed). If this occurs, and the issue cannot be immediately resolved, open an issue to track the error. Then, announce the failure in `#s_application-security-testing` to raise awareness, and follow the manual security triage process outlined below.
View manual process fallback when automation fails
#### Manually reviewing and resolving vulnerabilities[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#manually-reviewing-and-resolving-vulnerabilities)
On a weekly basis: review the vulnerability report to resolve no longer detected ones and close related issues. Note: It is not necessary to investigate vulnerabilities that are no longer detected.
  1. Visit `Vulnerability Report Dashboards` to verify that there are vulnerabilities that can be resolved by the security policy noted above.
  2. Notify Vulnerability management of these vulnerabilities for investigation.
  3. Vulnmapper will automatically close a tracking issue within 24 hours of the linked vulnerability is marked as resolved.


#### Manually creating deviation requests for FedRAMP vulnerabilities[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#manually-creating-deviation-requests-for-fedramp-vulnerabilities)
Vulnmapper automatically creates Deviation Requests but may fail for various reasons, such as the absence of analysis from NVD.
In cases where automation fails, you must create the [Deviation Requests](https://handbook.gitlab.com/handbook/security/security-assurance/security-compliance/poam-deviation-request-procedure/) manually before the issues reach SLA. To do so, use the following procedure.
  1. Open a DR issue with the [operational requirement template](https://gitlab.com/gitlab-com/gl-security/security-assurance/team-security-dedicated-compliance/poam-deviation-requests/-/issues/new?issuable_template=operational_requirement_template).
    1. Update the `Vulnerability Details` section with a link to the advisory (RedHat tracker usually), CVE ID, severity, and CVSS score.
    2. Update the `Justification Section` with: 
> The OS vendor has published an updated advisory for <CVE_ID>, indicating that package <PACKAGE_NAME> has not yet had a fix released for this vulnerability. Until a fix is available for the package, this vulnerability cannot practically be remediated.
    3. Update the `Attached Evidence` section with: 
> As this operational requirement represents a dependency on a vendor-published package to address this vulnerability, no additional evidence has been supplied. Please refer to the linked vendor advisory in the above justification.
    4. Link it to the security issue: `/relate <issue_id>`
  2. Update the security issue accordingly
```

/label ~"FedRAMP::Vulnerability" ~"FedRAMP::DR Status::Open"
/milestone %Backlog

```



##### FedRAMP vulnerabilities[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#fedramp-vulnerabilities)
To ensure compliance, the management of FedRAMP vulnerabilities is handled by [automation](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#automation). Please check the manual process fallback for additional details.
##### Non-FedRAMP vulnerabilities[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#non-fedramp-vulnerabilities)
We do not yet have the same automation in place for non-FedRAMP vulnerabilities since it represents a too important volume to manage for our teams and some necessary [improvements in the vulnmapper tool](https://gitlab.com/gitlab-com/gl-security/product-security/vulnerability-management/vulnerability-management-internal/vulnmapper/-/milestones/4#tab-issues) are required prior to enabling this. In the meantime, we favor a more specialized approach for these vulnerabilities and there is no standardized process across the groups.
#### Error Monitoring[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#error-monitoring)
500 errors on gitlab.com are reported to Sentry. Below are some quick links to pull up Sentry errors related to Application Security Testing.
  * StoreSecurityReports Worker - [https://sentry.gitlab.net/gitlab/gitlabcom/?query=is%3Aunresolved+StoreSecurityReportsWorker&statsPeriod=14d](https://sentry.gitlab.net/gitlab/gitlabcom/?query=is%3Aunresolved+StoreSecurityReportsWorker&statsPeriod=14d)
  * SyncSecurityReportsToReportApprovalRules Worker - [https://sentry.gitlab.net/gitlab/gitlabcom/?query=is%3Aunresolved+SyncSecurityReportsToReportApprovalRulesWorker&statsPeriod=14d](https://sentry.gitlab.net/gitlab/gitlabcom/?query=is%3Aunresolved+SyncSecurityReportsToReportApprovalRulesWorker&statsPeriod=14d)
  * Vulnerabilities - [https://sentry.gitlab.net/gitlab/gitlabcom/?query=is%3Aunresolved+vulnerabilities&statsPeriod=14d](https://sentry.gitlab.net/gitlab/gitlabcom/?query=is%3Aunresolved+vulnerabilities&statsPeriod=14d)
  * On-Demand DAST - [https://sentry.gitlab.net/gitlab/gitlabcom/?query=is%3Aunresolved+Dast&statsPeriod=14d](https://sentry.gitlab.net/gitlab/gitlabcom/?query=is%3Aunresolved+Dast&statsPeriod=14d)


#### Brainstorming sessions[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#brainstorming-sessions)
Our team occasionally schedules synchronous brainstorming sessions as a method of deep-diving on a specific topic. This approach can be useful in breaking down complexity and deriving actionable steps for problems that lack definition.
These are purposefully freeform to allow for creative problem solving. When possible, time should be reserved for a list of actions to be taken from the open discussion.
Brainstorming Sessions Doc (Internal): [https://docs.google.com/document/d/179JL5RzbgSIz2XZewbYn79cuX7_vUtte_TcoLwUUC5o/edit#](https://docs.google.com/document/d/179JL5RzbgSIz2XZewbYn79cuX7_vUtte_TcoLwUUC5o/edit)
_Examples of previous brainstorming topics:_
  * [Reduce false positives in Security reports](https://gitlab.com/gitlab-org/gitlab/issues/33934)
  * How to manage occurrence uniqueness identification in the common report format? (CompareKey)
  * [One file with syntax errors should not stop SAST and similar kind of jobs from running](https://gitlab.com/gitlab-org/gitlab/issues/7102)


#### Resources[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#resources)
  * [How to triage a QA test pipeline failure](https://docs.gitlab.com/development/testing_guide/end_to_end/debugging_end_to_end_test_failures/)
  * [Beginner’s guide to writing end-to-end tests](https://docs.gitlab.com/ee/development/testing_guide/end_to_end/beginners_guide.html)
  * [GitLab QA README](https://gitlab.com/gitlab-org/gitlab/-/tree/master/qa)
  * [GitLab QA Scenarios](https://gitlab.com/gitlab-org/gitlab-qa/-/blob/master/docs/what_tests_can_be_run.md)
  * [E2E info for GitLab developers](https://docs.gitlab.com/ee/development/testing_guide/end_to_end/)
  * [Quality training video material](https://www.youtube.com/playlist?list=PL05JrBw4t0KoNUmi5MOeNURxjl_BtUBxH)


#### Product Documentation[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#product-documentation)
As the product evolves, it is important to maintain accurate and up to date documentation for our users. If it is not documented, customers may not know a feature exists.
To update the documentation, the following process should be followed:
  1. When an issue has been identified as needing documentation, add the `~Documentation` label, outline in the description of the issue what documentation is needed, and assign a Backend Engineer and Technical Writer(TW) to the issue (find the appropriate TW by searching the [product categories](https://handbook.gitlab.com/handbook/product/categories/)).
  2. If the task is documentation only, apply a `~Px` label.
  3. For documentation around features or bugs, a backend engineer should write the documentation and work with the technical writer for editing. If the documentation only needs styling cleanup, clarification, or reorganization, this work should be lead by the Technical Writer with support from a BE as necessary. The availability of a technical writer should in no way hold up work on the documentation. [Further information on the documentation process](https://docs.gitlab.com/ee/development/documentation/workflow.html).


#### Async Daily Standups[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#async-daily-standups)
Since we are a [remote](https://handbook.gitlab.com/handbook/company/culture/all-remote/) company, having daily standup meetings would not make any sense, since we’re not all in the same timezone. That’s why we have async daily standups, where everyone can give some insights into what they did yesterday, what they plan to do today, etc. For that, we rely on the [geekbot](https://geekbot.com/) slack plugin to automate the process.
##### Standup messages format[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#standup-messages-format)
  * Use the “`description in backquote` + `[link to issue](#)`” format when mentioning issues in your standup report.
  * Prepend CI status icons to the answer lines for `What did you do since yesterday?` to denote the current state: 
    * ![Accomplished](https://handbook.gitlab.com/images/engineering/development/sec/secure/ci-success.svg) for successfully accomplished tasks (`:ci_passing:` emoji)
    * ![Overdue](https://handbook.gitlab.com/images/engineering/development/sec/secure/ci-failed.svg) for tasks that were due on some period of time but were not accomplished (`:ci_failing:` emoji)
    * ![In progress](https://handbook.gitlab.com/images/engineering/development/sec/secure/ci-running.svg) for tasks currently in progress (`:ci_running:` emoji)
    * ![Paused](https://handbook.gitlab.com/images/engineering/development/sec/secure/ci-pending.svg) for paused or postponed tasks (`:ci_pending:` emoji)
    * any other `:ci_...` icon you find applicable


**Example:**
What did you do since yesterday?
  * ![Accomplished](https://handbook.gitlab.com/images/engineering/development/sec/secure/ci-success.svg) Accomplished the `Spotbugs java analyzer compareKey is not unique` <https://gitlab.com/gitlab-org/gitlab-ee/issues/10860>
  * ![In progress](https://handbook.gitlab.com/images/engineering/development/sec/secure/ci-running.svg) Still working on `Allow guests to create an issue from a vulnerability` <https://gitlab.com/gitlab-org/gitlab-ee/issues/7813>
  * ![Overdue](https://handbook.gitlab.com/images/engineering/development/sec/secure/ci-failed.svg) Catch-up on all emails and threads after the vacation


**Slack Channels:**
As our teams focus on different areas, we have Geekbot configured to broadcast to separate channels in addition to our common one at [#s_secure-standup].
  1. Composition Analysis: [#g_ast-composition-analysis-standup](https://gitlab.slack.com/archives/g_ast-composition-analysis-standup)
  2. Dynamic Analysis: [#g_ast-dynamic-analysis-standup](https://gitlab.slack.com/archives/g_ast-dynamic-analysis-standup)
  3. Secret Detection: [#g_ast-secret-detection-standup](https://gitlab.slack.com/archives/g_ast-secret-detection-standup)
  4. Static Analysis: [#g_ast-static-analysis-standup](https://gitlab.slack.com/archives/g_ast-static-analysis-standup)


#### Recorded meetings[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#recorded-meetings)
Our important meetings are recorded and published on YouTube, in the [Application Security Testing Stage playlist](https://www.youtube.com/playlist?list=PL05JrBw4t0Kq7yUrZazEF3diazV29RRo1). They give a good overview of the decision process, which is often a discussion with all the stakeholders. As we are a [remote](https://handbook.gitlab.com/handbook/company/culture/all-remote/) company, these video meetings help to synchronize and take decisions faster than commenting on issues. We prefer asynchronous work, but for large features and when the timing is tight, we can detail a lot of specifications. This will make the asynchronous work easier, since we have evaluated all edge cases.
### Calendar[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#calendar)
We welcome team members to join meetings that are on our shared calendar. The [Application Security Testing Calendar](https://calendar.google.com/calendar?cid=Z2l0bGFiLmNvbV9tZDBhbzM2Z3B2bDV2MWY0MTI4ZXJobmo2Z0Bncm91cC5jYWxlbmRhci5nb29nbGUuY29t) is available to all logged in GitLab team members.
### Staying informed[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#staying-informed)
GitLab is an extremely active organization which generates a lot of news and activity each week. Everyone in Application Security Testing are encouraged to keep themselves informed as to what is happening in the larger organzation. Everyone is also encouraged to contribute to these channels and communication paradigms when you have information to share.
In addition to this, each group in Application Security Testing conducts a weekly synchronous meeting. These meetings are publicized on the Application Security Testing Calendar mentioned above. As always at GitLab, we strive to [make meeting attendance optional](https://handbook.gitlab.com/handbook/company/culture/all-remote/meetings/#1-make-meeting-attendance-optional).
#### Keeping others informed[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#keeping-others-informed)
In addition to keeping yourself informed, team members are encouraged to keep others informed as well. Application Security Testing groups have adopted a practice of including the following topics as standing agenda items in their weekly meetings, with example topics for each bullet point.
  * **Current status**
    * Work recently achieved against top priorities for that milestone. 
      * Pre-recorded demos are appreciated and encouraged as part of these updates.
    * Newly discovered scope or dependencies.
  * **Risks**
    * Issues which are blocked or slowed, impacting whether they can be delivered in the desired timeframe.
  * **Help wanted**
    * Issues or topics on which the team or individuals on the team are getting stuck and could use some help.
  * **Praise**
    * Anyone doing a great job and you want to give them kudos?
    * Any bit of work which has been delivered that’s exceptional?


Engineering Managers are responsible for populating this section of weekly group meetings, though everyone can contribute. In addition to helping the group keep itself informed about what’s happening each week, the SEM for Application Security Testing will collect this information weekly and broadcast a curated list to the section.
#### Technical onboarding[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#technical-onboarding)
New hires should go through these steps and read the corresponding documentation when onboarding in the Application Security Testing Team. Every new hire will have an assigned [onboarding issue](https://gitlab.com/gitlab-org/security-products/onboarding/blob/master/.gitlab/issue_templates/Technical_Onboarding.md) that will guide them through the whole process.
#### Workflow and Refinement[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#workflow-and-refinement)
See [Application Security Testing Engineering Planning](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/planning/).
#### Coding standards and style guidelines[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#coding-standards-and-style-guidelines)
The Application Security Testing Team follows the coding standards and style guidelines outlined in the company-wide [Contributor and Development Docs](https://docs.gitlab.com/ee/development/), however, please consult the following guidelines which are specific to the Application Security Testing Team:
  * [Application Security Testing Team Go standards and style guidelines](https://docs.gitlab.com/ee/development/go_guide/#secure-team-standards-and-style-guidelines)


#### Cross group collaboration[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#cross-group-collaboration)
Some components of the architecture that support Application Security Testing features are shared between multiple groups like the [common](https://gitlab.com/gitlab-org/security-products/analyzers/common) Go library, the [Security Report Schemas](https://gitlab.com/gitlab-org/security-products/security-report-schemas), the [rails parsers](https://gitlab.com/gitlab-org/gitlab/-/tree/master/ee/lib/gitlab/ci/parsers/security), etc.
Modifying these shared pieces might impact other groups so we should rely as much as possible on approval rules to ensure such changes are reviewed by the relevant teams before being merged.
Impactless two-way door changes could skip the approval process, please use sound judgement and common sense in such situations.
The author of changes should announce broadly the changes made on these components to raise awareness (weekly meeting agenda, slack channel).
### Development of new analyzers[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#development-of-new-analyzers)
For a complete guide about developing a new analyzer please refer to our [user documentation](https://docs.gitlab.com/ee/development/sec/analyzer_development_guide.html#development-of-new-analyzers)
## Technical Documentation[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#technical-documentation)
As our product evolves, the engineering teams are researching ways to achieve new functionality and improve our architecture.
The outcome of this research can be found in our [Technical Documentation](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/tech-docs/) section.
### Data Sources[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#data-sources)
We keep a [list of data sources in our internal wiki](https://gitlab.com/gitlab-org/secure/data-feeds-and-sources/-/wikis/Data-Feeds-&-Sources). This includes advisory databases, package license information, and related data.
## Retrospectives[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#retrospectives)
The Application Security Testing sub-department conducts retrospectives at the group level.
Each group’s EM or delegated DRI is responsible to prepare and schedule the retrospective sync sessions and the async retrospective issues can be found in [the corresponding project](https://gitlab.com/gl-retrospectives/secure-sub-dept).
## Common Links[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/#common-links)
  * [#s_application-security-testing](https://gitlab.slack.com/archives/s_application-security-testing) in Slack
  * [Security Glossary](https://docs.gitlab.com/ee/user/application_security/terminology/)


* * *
#####  [API Security team in the Dynamic Analysis Group](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/dynamic-analysis/api-security/)
API Security The API Security team is a standalone team which is part of the Dynamic Analysis group …
#####  [Application Security Testing - Planning](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/planning/)
Overview Our stage follows the product development flow process, including the workflow labels. This …
#####  [Application Security Testing, Composition Analysis](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/composition-analysis/)
The Composition Analysis group at GitLab is charged with developing solutions which perform Container and Dependency Scanning and License Compliance.
#####  [Application Security Testing, Vulnerability Research](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/vulnerability-research/)
Mission Our mission is to advance GitLab’s security offerings toward their long-term vision …
#####  [Dynamic Analysis Group](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/dynamic-analysis/dynamic-analysis/)
Dynamic Analysis The Dynamic Analysis group at GitLab is charged with developing solutions which …
#####  [Products](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/products/)
#####  [Secret Detection Group](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/secret-detection/)
The Secret Detection group protects you against leaking credentials, tokens, or other secrets on GitLab.
#####  [Secure QA Process](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/qa_process/)
Everything starts with a Merge Request We expect and require all contributions to our products to go …
#####  [Secure Technical Documentation](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/tech-docs/)
Architecture Overview Severity Levels Feedback(Dismiss, create an issue or a Merge Request) Overview …
#####  [Static Analysis Group](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/static-analysis/)
Static Analysis The Static Analysis group at GitLab is charged with developing the Static …
#####  [Tutorial: Add observability metrics to a CI-based analyzer](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/analyzer-observability-metrics/)
Observability metrics help you understand how CI-based security analyzers perform in production. …
Last modified October 11, 2025: [Update Automation tooling to reflect migration to vulnmapper (`fb4bc5c2`)](https://gitlab.com/gitlab-com/content-sites/handbook/commit/fb4bc5c2)
[ ](https://gitlab.com/gitlab-com/content-sites/handbook/blob/main/content/handbook/engineering/development/sec/secure/_index.md) - [ ](https://gitlab.com/-/ide/project/gitlab-com/content-sites/handbook/edit/main/-/content/handbook/engineering/development/sec/secure/_index.md) - please [contribute](https://handbook.gitlab.com/handbook/about/contributing/). [ ![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-sa/4.0/)