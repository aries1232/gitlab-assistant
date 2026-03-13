#  Category Direction - Static Application Security Testing (SAST) 
  1. You are here:
  2. [GitLab Direction](https://about.gitlab.com/direction/)
  3. [Product Stage Direction - Application Security Testing](https://about.gitlab.com/direction/application_security_testing/)
  4. [Static Analysis group priorities](https://about.gitlab.com/direction/application_security_testing/static-analysis/)
  5. Category Direction - Static Application Security Testing (SAST)


####  Maintained by:
[ ![Chris Widstrom](https://about.gitlab.com/images/team/chriswidstrom-crop.jpg) ](https://gitlab.com/cwidstrom) [ ![VP of Product Management](https://about.gitlab.com/images/gitlab-logo-extra-whitespace.png) ](https://gitlab.com/oazaria)
The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
  * [Overview](https://about.gitlab.com/direction/application_security_testing/static-analysis/sast/#overview)
  * [Strategy and themes](https://about.gitlab.com/direction/application_security_testing/static-analysis/sast/#strategy-and-themes)
    * [Specific product areas](https://about.gitlab.com/direction/application_security_testing/static-analysis/sast/#specific-product-areas)
      * [Language support](https://about.gitlab.com/direction/application_security_testing/static-analysis/sast/#language-support)
      * [Detection accuracy](https://about.gitlab.com/direction/application_security_testing/static-analysis/sast/#detection-accuracy)
      * [Advanced SAST scan times](https://about.gitlab.com/direction/application_security_testing/static-analysis/sast/#advanced-sast-scan-times)
  * [1 year plan](https://about.gitlab.com/direction/application_security_testing/static-analysis/sast/#1-year-plan)
    * [What is next for us](https://about.gitlab.com/direction/application_security_testing/static-analysis/sast/#what-is-next-for-us)
  * [What we recently completed](https://about.gitlab.com/direction/application_security_testing/static-analysis/sast/#what-we-recently-completed)
  * [What is not planned right now](https://about.gitlab.com/direction/application_security_testing/static-analysis/sast/#what-is-not-planned-right-now)
  * [Get involved](https://about.gitlab.com/direction/application_security_testing/static-analysis/sast/#get-involved)
  * [Page updates](https://about.gitlab.com/direction/application_security_testing/static-analysis/sast/#page-updates)


This direction page describes GitLab's plans for the SAST category, which checks source code to find possible security vulnerabilities.
## Overview[](https://about.gitlab.com/direction/application_security_testing/static-analysis/sast/#overview)
[GitLab SAST](https://docs.gitlab.com/ee/user/application_security/sast/) runs on merge requests and the default branch of your software projects so you can continuously monitor and improve the security of the code you write. SAST jobs run in your CI/CD pipelines alongside existing builds, tests, and deployments, so it's easy for developers to interact with.
While SAST uses sophisticated techniques, we want it to be simple to understand and use day-to-day, especially by developers who may not have specific security expertise. So, when you [enable GitLab SAST](https://docs.gitlab.com/ee/user/application_security/sast/#configuration), it automatically detects the programming languages used in your project and runs the right security analyzers.
While [basic SAST scans](https://docs.gitlab.com/ee/user/application_security/sast/#summary-of-features-per-tier) are available in every GitLab tier, organizations that use GitLab SAST in their security programs should use Ultimate. Only GitLab Ultimate [includes](https://docs.gitlab.com/ee/user/application_security/sast/#summary-of-features-per-tier):
  * Advanced SAST: proprietary scanning technology that delivers higher-quality results.
  * Advanced Vulnerability Tracking: proprietary technology that keeps track of vulnerabilities as they move around a codebase.
  * Workflows: SAST results integrated into the merge request workflow.
  * Related security and compliance features: Vulnerability Management, Security Policies, and other capabilities that help you enforce security requirements.


## Strategy and themes[](https://about.gitlab.com/direction/application_security_testing/static-analysis/sast/#strategy-and-themes)
Our strategy depends on [understanding our customers and the broader market](https://about.gitlab.com/direction/application_security_testing/static-analysis/sast/market_context.html).
### Specific product areas[](https://about.gitlab.com/direction/application_security_testing/static-analysis/sast/#specific-product-areas)
This section summarizes our plans for specific parts of GitLab SAST.
#### Language support[](https://about.gitlab.com/direction/application_security_testing/static-analysis/sast/#language-support)
We are currently working to upgrade more languages to Advanced SAST. We will continue until we have enabled Advanced SAST for all languages that GitLab SAST [currently scans](https://docs.gitlab.com/ee/user/application_security/sast/#supported-languages-and-frameworks) using Semgrep-based scanning. See documentation for the current [languages Advanced SAST supports](https://docs.gitlab.com/ee/user/application_security/sast/gitlab_advanced_sast.html#supported-languages).
Status of new languages is [tracked in epic 14312](https://gitlab.com/groups/gitlab-org/-/epics/14312#language-priority-and-status). As of 2025-09-16, the status is:
Language | Expected release | Notes  
---|---|---  
[C/C++](https://gitlab.com/groups/gitlab-org/-/epics/14271) | During 2025 | Experiment released. Beta in progress. GA targeted by the end of January 2026.  
[Kotlin](https://gitlab.com/groups/gitlab-org/-/epics/15173) | Pending |   
[Scala](https://gitlab.com/groups/gitlab-org/-/epics/15174) | Pending |   
[iOS (Swift and Objective-C)](https://gitlab.com/groups/gitlab-org/-/epics/16318) | Pending |   
When you enable Advanced SAST, it [takes over coverage](https://docs.gitlab.com/ee/user/application_security/sast/gitlab_advanced_sast.html) for the languages it supports.
We plan to [enable Advanced SAST by default](https://docs.gitlab.com/update/deprecations/#gitlab-advanced-sast-will-be-enabled-by-default) for SAST users in 19.0.
When we complete this initiative, we will then evaluate the future plans for the Semgrep CE-based analyzer, because it will serve fewer Ultimate customers over time.
For details on what is _not_ included in this initiative, see [What is not planned right now](https://about.gitlab.com/direction/application_security_testing/static-analysis/sast/#what-is-not-planned-right-now).
#### Detection accuracy[](https://about.gitlab.com/direction/application_security_testing/static-analysis/sast/#detection-accuracy)
GitLab Vulnerability Research analyzes and improves coverage for already-supported languages as part of a continuous program of assessment and improvement. This program includes:
  * In-house security research.
  * Proactive assessments of real-world codebases and benchmark/example projects.
  * Reacting to feedback from customers and from internal users within GitLab.
  * Identifying opportunities to improve the Advanced SAST engine to enable new detection techniques.


#### Advanced SAST scan times[](https://about.gitlab.com/direction/application_security_testing/static-analysis/sast/#advanced-sast-scan-times)
GitLab SAST is designed to run in merge requests and on the default branch of your repository, so we know how important it is to get results quickly.
In most cases, [Advanced SAST](https://docs.gitlab.com/user/application_security/sast/gitlab_advanced_sast/) returns results within a few minutes. However, because Advanced SAST scans your program in detail, large repositories can sometimes take longer to scan.
As part of our ongoing maintenance of the Advanced SAST engine, we have already:
  * Updated many components of the Advanced SAST engine to improve scan performance.
  * Implemented multi-core scanning to better utilize available Runner resources. (See [documentation](https://docs.gitlab.com/user/application_security/sast/gitlab_advanced_sast/#optimize-scans-with-multi-core-scanning).)
  * Documented [steps you can take to improve performance](https://docs.gitlab.com/user/application_security/sast/gitlab_advanced_sast/#slow-scans-or-timeouts-with-advanced-sast), and how to collect data if you reach out for support.


Looking forward, we plan to:
  * Continue to routinely identify, schedule, and implement performance improvements to the Advanced SAST engine. 
    * Note: Because every codebase is different, it's difficult to predict whether any given change will improve performance for a specific codebase.
  * Implement incremental scanning approaches to reduce the amount of processing the engine has to complete. 
    * First (in progress, nearing delivery no later than 18.5 / October 2025): [Faster Advanced SAST: Diff-based scanning in MRs](https://gitlab.com/groups/gitlab-org/-/epics/16790).
    * Next (scheduled for Feb.–Apr. 2026): [Incremental scanning for Advanced SAST (skip unchanged code)](https://gitlab.com/groups/gitlab-org/-/epics/15545).
  * Explore [multi-threaded scanning](https://gitlab.com/groups/gitlab-org/-/epics/16792) as a further iteration on existing multi-core scanning.


Many of these work items are tracked in the epic for [Advanced SAST performance and scalability](https://gitlab.com/groups/gitlab-org/-/epics/16560). Note that we use confidential issues for some tasks, so you won't see every issue that we've implemented or that we have planned.
If you have concerns about Advanced SAST scan times in your repositories, see the [troubleshooting guide for slow scans](https://docs.gitlab.com/user/application_security/sast/gitlab_advanced_sast/#slow-scans-or-timeouts-with-advanced-sast).
## 1 year plan[](https://about.gitlab.com/direction/application_security_testing/static-analysis/sast/#1-year-plan)
GitLab Static Analysis and Vulnerability Research teams are collaborating to improve the customer experience with SAST.
Our plans align with the themes for the Security use case:
  1. **Detection accuracy:** Security professionals and developers should be able to trust every result from GitLab SAST. This work improves the user experience directly, but also indirectly by reducing the number of times users have to go through other workflows.
  2. **Shift left security:** GitLab SAST already scans code as soon as it's pushed, before code reviews even begin. But, we can make it easier to improve security by scanning code even earlier, including before code leaves developer machines.
  3. **Faster remediation:** We value our users' time, and we know that vulnerabilities are resolved more often if they're easier to understand and interact with.


### What is next for us[](https://about.gitlab.com/direction/application_security_testing/static-analysis/sast/#what-is-next-for-us)
In the next 3 months, we are planning to work on:
Name | Overall status | One-month plan | Three-month plan  
---|---|---|---  
[**Faster Advanced SAST: Diff-based scanning in MRs**](https://gitlab.com/groups/gitlab-org/-/epics/16790) | In progress | Complete backend changes | Complete frontend changes and fully ship the feature  
[**Implement Advanced SAST for C/C++**](https://gitlab.com/groups/gitlab-org/-/epics/14271) | Full delivery expected by FY26Q4, with Experiment and Beta releases earlier | Release Experiment and update plan for Beta |   
After the next 3 months, we plan to work on:
Name | Overall status  
---|---  
[**Reduce false negatives in C# Advanced SAST**](https://gitlab.com/gitlab-org/gitlab/-/issues/509461) | Expected FY26Q2. (Primarily Vulnerabilty Research.)  
[**Customizable detection logic for Advanced SAST**](https://gitlab.com/groups/gitlab-org/-/epics/16604) | Expected FY26Q3  
[**Real-time IDE SAST scanning: Beta release**](https://gitlab.com/groups/gitlab-org/-/epics/15386) | Expected FY26Q4  
[**Incremental scanning for Advanced SAST (skip unchanged code)**](https://gitlab.com/groups/gitlab-org/-/epics/15545) | Assessing technical plan and delivery estimate.  
[**Real-time IDE SAST scanning: GA release**](https://gitlab.com/groups/gitlab-org/-/epics/16851) | Expected FY27Q1  
## What we recently completed[](https://about.gitlab.com/direction/application_security_testing/static-analysis/sast/#what-we-recently-completed)
Our recent work includes:
  * 2-3x improvement in Advanced SAST scan runtime
  * [PHP support for Advanced SAST](https://about.gitlab.com/releases/2025/06/19/gitlab-18-1-released/#php-support-for-advanced-sast).
  * [Expanded CWE support in GitLab Duo Vulnerability Resolution](https://about.gitlab.com/releases/2025/06/19/gitlab-18-1-released/#increased-sast-coverage-for-duo-vulnerability-resolution).
  * [Significantly improved detection accuracy in Python, Go, and Java](https://gitlab.com/groups/gitlab-org/-/epics/14685).
  * [Multi-core Advanced SAST scanning](https://about.gitlab.com/releases/2025/02/20/gitlab-17-9-released/#multi-core-advanced-sast-offers-faster-scans).


Check [older release posts](https://gitlab-com.gitlab.io/cs-tools/gitlab-cs-tools/what-is-new-since/?tab=features&selectedCategories=SAST&minVersion=13_00) for our previous work in this area.
## What is not planned right now[](https://about.gitlab.com/direction/application_security_testing/static-analysis/sast/#what-is-not-planned-right-now)
We understand the value of many potential improvements to GitLab SAST, but aren't currently planning to work on the following initiatives:
  * **Expanding language support:** Currently, we're focusing on delivering better-quality results, faster, for [the many languages and frameworks we already support](https://docs.gitlab.com/ee/user/application_security/sast/#supported-languages-and-frameworks). We're not actively adding adding support for new languages. However, if we don't support a language you use, you can: 
    * [Integrate third-party tools](https://docs.gitlab.com/ee/development/integrations/secure.html) (open-source or proprietary) using our [documented, open report format](https://docs.gitlab.com/ee/development/integrations/secure.html#report).
    * Document your request by opening an issue or commenting on an existing issue in [epic 297](https://gitlab.com/groups/gitlab-org/-/epics/297).
  * **More analyzer consolidations:** We are not currently focusing on consolidating more analyzers into Semgrep-based scanning with [GitLab-managed rules](https://docs.gitlab.com/ee/user/application_security/sast/rules.html#source-of-rules). 
    * We recently completed work to consolidate scanning coverage from many language-specific scanners to Semgrep-based scanning. This provides a simpler, more consistent operational experience; allows GitLab to directly manage rules; and makes scans run faster.
    * We released these changes as part of [GitLab 17.0](https://docs.gitlab.com/ee/update/deprecations.html#sast-analyzer-coverage-changing-in-gitlab-170), [GitLab 16.0](https://docs.gitlab.com/ee/update/deprecations.html#sast-analyzer-coverage-changing-in-gitlab-160), and [GitLab 15.4](https://docs.gitlab.com/ee/update/deprecations.html#sast-analyzer-consolidation-and-cicd-template-changes).
    * The remaining analyzers cover less-commonly-used languages that we cannot immediately convert due to technical limitations.


## Get involved[](https://about.gitlab.com/direction/application_security_testing/static-analysis/sast/#get-involved)
You can contribute to where GitLab SAST goes next by:
  * Commenting or contributing to existing [SAST issues](https://gitlab.com/gitlab-org/gitlab/-/issues/?sort=created_date&state=opened&label_name%5B%5D=Category%3ASAST) in the public `gitlab-org/gitlab` issue tracker.
  * If you don't see an issue that matches, filing [a new issue](https://gitlab.com/gitlab-org/gitlab/-/issues/new?issuable_template=Feature%20Proposal%20-%20basic). 
    * Post a comment that says `@gitlab-bot label ~"group::static analysis" ~"Category:SAST"` so your issue lands in our triage workflow.
  * If you're a GitLab customer, [contacting Support](https://support.gitlab.com/hc/en-us/articles/11626483177756-GitLab-Support) or discussing your needs with your account team.


## Page updates[](https://about.gitlab.com/direction/application_security_testing/static-analysis/sast/#page-updates)
|   
---|---  
Stage | [Application Security Testing](https://about.gitlab.com/direction/application_security_testing/)  
Content Last Reviewed | 2025-09-16  
[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/application_security_testing/static-analysis/sast/index.html.md.erb) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/application_security_testing/static-analysis/sast/index.html.md.erb)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fapplication_security_testing%2Fstatic-analysis%2Fsast%2F&_biz_t=1773331763523&_biz_i=%0ACategory%20Direction%20-%20Static%20Application%20Security%20Testing%20\(SAST\)%0A%7C%0AGitLab%0A&_biz_n=48&rnd=686683&cdn_o=a&_biz_z=1773331763919)
suggested results