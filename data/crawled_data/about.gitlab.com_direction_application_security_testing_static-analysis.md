#  Static Analysis group priorities 
  1. You are here:
  2. [GitLab Direction](https://about.gitlab.com/direction/)
  3. [Product Stage Direction - Application Security Testing](https://about.gitlab.com/direction/application_security_testing/)
  4. Static Analysis group priorities


The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
  * [Categories](https://about.gitlab.com/direction/application_security_testing/static-analysis/#categories)
  * [Priorities](https://about.gitlab.com/direction/application_security_testing/static-analysis/#priorities)
    * [Features](https://about.gitlab.com/direction/application_security_testing/static-analysis/#features)
    * [Maintenance](https://about.gitlab.com/direction/application_security_testing/static-analysis/#maintenance)
    * [Documentation](https://about.gitlab.com/direction/application_security_testing/static-analysis/#documentation)
    * [Research](https://about.gitlab.com/direction/application_security_testing/static-analysis/#research)
  * [Group mission](https://about.gitlab.com/direction/application_security_testing/static-analysis/#group-mission)
    * [Our responsibility](https://about.gitlab.com/direction/application_security_testing/static-analysis/#our-responsibility)
  * [What this page is and isn't](https://about.gitlab.com/direction/application_security_testing/static-analysis/#what-this-page-is-and-isnt)
  * [Page updates](https://about.gitlab.com/direction/application_security_testing/static-analysis/#page-updates)


## Categories[](https://about.gitlab.com/direction/application_security_testing/static-analysis/#categories)
This page combines priorities across the feature categories that Static Analysis maintains. For details on each category, see the category direction pages:
  * [Static Application Security Testing (SAST)](https://about.gitlab.com/direction/application_security_testing/static-analysis/sast/)
  * [Code Quality](https://about.gitlab.com/direction/application_security_testing/static-analysis/code-quality/)


## Priorities[](https://about.gitlab.com/direction/application_security_testing/static-analysis/#priorities)
### Features[](https://about.gitlab.com/direction/application_security_testing/static-analysis/#features)
These are primarily feature enhancements, curated by Product Management.
Name | Overall status | One-month plan | Three-month plan  
---|---|---|---  
[**Faster Advanced SAST: Diff-based scanning in MRs**](https://gitlab.com/groups/gitlab-org/-/epics/16790) | In progress | Complete backend changes | Complete frontend changes and fully ship the feature  
[**Implement Advanced SAST for C/C++**](https://gitlab.com/groups/gitlab-org/-/epics/14271) | Full delivery expected by FY26Q4, with Experiment and Beta releases earlier | Release Experiment and update plan for Beta |   
[**Reduce false negatives in C# Advanced SAST**](https://gitlab.com/gitlab-org/gitlab/-/issues/509461) | Expected FY26Q2. (Primarily Vulnerabilty Research.) |  |   
[**Customizable detection logic for Advanced SAST**](https://gitlab.com/groups/gitlab-org/-/epics/16604) | Expected FY26Q3 |  |   
[**Real-time IDE SAST scanning: Beta release**](https://gitlab.com/groups/gitlab-org/-/epics/15386) | Expected FY26Q4 |  |   
[**Incremental scanning for Advanced SAST (skip unchanged code)**](https://gitlab.com/groups/gitlab-org/-/epics/15545) | Assessing technical plan and delivery estimate. |  |   
[**Real-time IDE SAST scanning: GA release**](https://gitlab.com/groups/gitlab-org/-/epics/16851) | Expected FY27Q1 |  |   
### Maintenance[](https://about.gitlab.com/direction/application_security_testing/static-analysis/#maintenance)
These are primarily technical tasks, curated by Engineering Management.
Priority | Name | Target release  
---|---|---  
1 | [AST CI-templates improvements](https://gitlab.com/groups/gitlab-org/-/epics/16159) | `TBD`  
2 | [Static Analysis 18.0 deprecations, removals and breaking changes](https://gitlab.com/gitlab-org/gitlab/-/issues/507931) | `18.0`  
### Documentation[](https://about.gitlab.com/direction/application_security_testing/static-analysis/#documentation)
These are proactive documentation-focused tasks, outside of the context of feature or maintenance efforts already tracked elsewhere. Curated by Product Management.
Name | Overall status | One-month plan | Three-month plan  
---|---|---|---  
[**Provide guidance on how to evaluate GitLab SAST**](https://gitlab.com/groups/gitlab-org/-/epics/15295) | Initial [guide](https://docs.gitlab.com/ee/user/application_security/sast/evaluation_guide.html) shipped | Implement further edits to the evaluation guide | Publish benchmark/example project guide, based on [analysis project listed below](https://gitlab.com/groups/gitlab-org/-/epics/14685)  
[**Restructure and update Advanced SAST docs now that the feature is GA**](https://gitlab.com/groups/gitlab-org/-/epics/15401) | In progress. (Primarily documentation.) | Complete most issues in this epic | Complete entire epic  
### Research[](https://about.gitlab.com/direction/application_security_testing/static-analysis/#research)
These are priorities that Static Analysis has, where we believe we would benefit from support from Vulnerability Research. Curated by Product Management and Engineering Management.
Name | Overall status | One-month plan | Three-month plan  
---|---|---|---  
[**Address false-negative results in C# Advanced SAST coverage**](https://gitlab.com/gitlab-org/gitlab/-/issues/509461) | Expected by FY26Q2. |  | Analyze existing cases; diagnose gaps; analyze and improve source/sink coverage; analyze and improve rule coverage  
[**Update Java rules based on benchmark/example analysis**](https://gitlab.com/groups/gitlab-org/-/epics/14685) | To be scheduled. Will involve refreshing our ground-truth analysis and implementing rule changes. |  |   
[**Create Advanced SAST ruleset for C++**](https://gitlab.com/groups/gitlab-org/-/epics/14271) |  |  |   
[**Expand detection of dangerous query construction without traceable user input**](https://gitlab.com/gitlab-org/gitlab/-/issues/500376) |  |  |   
[**Implement the next level of documentation for rule/CWE coverage**](https://gitlab.com/groups/gitlab-org/-/epics/15343) | Assessing implementation options. | Interview internal users and develop technical plan | Ship documentation  
## Group mission[](https://about.gitlab.com/direction/application_security_testing/static-analysis/#group-mission)
We believe that the world is safer when [everyone can contribute](https://handbook.gitlab.com/handbook/company/mission/#mission) to software security. Our customers, and those they serve, are better protected when developers and security professionals can fix potential security risks earlier.
The earliest possible time to catch a security issue is when the code is first written. GitLab sees code very early in the software development lifecycle, since we store production code and also support customer workflows (like merge requests) for pre-production development. So, our group is uniquely positioned to integrate static analysis everywhere as part of a comprehensive DevSecOps platform. We can do what others can't by making security omnipresent, and by supporting collaboration right in the tools that development teams are already using to do their jobs.
Building on those fundamental beliefs, the Static Analysis group's _business_ purpose is to build value for GitLab and our customers…
  1. By encouraging organizations to use GitLab Ultimate…
  2. By delivering more value to them in the GitLab platform…
  3. By enabling them to secure their code early in the development process…
  4. By using static analysis techniques.


### Our responsibility[](https://about.gitlab.com/direction/application_security_testing/static-analysis/#our-responsibility)
We are responsible for ensuring that customers can use GitLab Ultimate to:
  * Remove existing security “point solutions”, with a special focus on SAST, IaC Scanning, Code Quality, and similar static analysis disciplines. (Customers often use the savings from removing other tools to pay for GitLab Ultimate.)
  * Satisfy their security and compliance requirements relevant to these areas.
  * Meaningfully increase their confidence in the security of their code as soon as it is written.


Our responsibility is for the **full customer experience** —not just security analyzers or specific software systems we maintain. At times this may mean:
  * Imagining and implementing workflows that helps everyone know about and fix security issues.
  * Integrating open-source tools into GitLab.
  * Creating innovative static analysis technology.
  * Driving changes in other areas of the GitLab platform.
  * Contributing to documentation or other educational material that helps explain how to use GitLab effectively.


**We will do what it takes** to deliver these customer results—our customers use the entire product to do their jobs, so it's important that we collaborate effectively with other groups to deliver end-to-end results.
## What this page is and isn't[](https://about.gitlab.com/direction/application_security_testing/static-analysis/#what-this-page-is-and-isnt)
This page is designed to clarify competing priorities between feature categories and provide a high-level summary of the problems the Static Analysis group plans to tackle.
It includes "headline" items that we're planning to work on, and ranks them across the feature categories that Static Analysis maintains.
However, it doesn't:
  * Include every task that our group will do, since the single source of truth for our task list is [the issue tracker](https://gitlab.com/gitlab-org/gitlab/-/issues/?sort=created_date&state=opened&label_name%5B%5D=group%3A%3Astatic%20analysis).
  * Include community contributions that we facilitate, since we can't predict when these will land.
  * Replace direction pages, since these pages describe the vision and strategy holistically for each feature category. 
    * For details, check the directions for [SAST](https://about.gitlab.com/direction/application_security_testing/static-analysis/sast/) and [Code Quality](https://about.gitlab.com/direction/application_security_testing/static-analysis/code-quality/).
  * Guarantee delivery order or delivery timing, since these aspects of planning are always subject to the realities encountered during development. 
    * See the [disclaimer](https://about.gitlab.com/direction/application_security_testing/static-analysis/#legal-disclaimer) at the top of the page for details.


## Page updates[](https://about.gitlab.com/direction/application_security_testing/static-analysis/#page-updates)
|   
---|---  
Stage | [Application Security Testing](https://about.gitlab.com/direction/application_security_testing/)  
Content Last Reviewed | 2025-02-18  
[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/application_security_testing/static-analysis/index.html.md.erb) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/application_security_testing/static-analysis/index.html.md.erb)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fapplication_security_testing%2Fstatic-analysis%2F&_biz_t=1773331870982&_biz_i=%0AStatic%20Analysis%20group%20priorities%0A%7C%0AGitLab%0A&_biz_n=69&rnd=104913&cdn_o=a&_biz_z=1773331871151)
suggested results