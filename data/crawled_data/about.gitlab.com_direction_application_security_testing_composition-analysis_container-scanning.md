#  Category Direction - Container Scanning 
  1. You are here:
  2. [GitLab Direction](https://about.gitlab.com/direction/)
  3. [Product Stage Direction - Application Security Testing](https://about.gitlab.com/direction/application_security_testing/)
  4. [Group Direction - Composition Analysis](https://about.gitlab.com/direction/application_security_testing/composition-analysis/)
  5. Category Direction - Container Scanning


The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
  * [Container Scanning](https://about.gitlab.com/direction/application_security_testing/composition-analysis/container-scanning/#container-scanning)
    * [Introduction and how you can help](https://about.gitlab.com/direction/application_security_testing/composition-analysis/container-scanning/#introduction-and-how-you-can-help)
    * [Overview](https://about.gitlab.com/direction/application_security_testing/composition-analysis/container-scanning/#overview)
    * [Strategy and Themes](https://about.gitlab.com/direction/application_security_testing/composition-analysis/container-scanning/#strategy-and-themes)
    * [1 year plan](https://about.gitlab.com/direction/application_security_testing/composition-analysis/container-scanning/#1-year-plan)
      * [What we recently completed](https://about.gitlab.com/direction/application_security_testing/composition-analysis/container-scanning/#what-we-recently-completed)
      * [What we are currently working on](https://about.gitlab.com/direction/application_security_testing/composition-analysis/container-scanning/#what-we-are-currently-working-on)
      * [What is next for us](https://about.gitlab.com/direction/application_security_testing/composition-analysis/container-scanning/#what-is-next-for-us)
      * [What is Not Planned Right Now](https://about.gitlab.com/direction/application_security_testing/composition-analysis/container-scanning/#what-is-not-planned-right-now)
    * [Best in Class Landscape](https://about.gitlab.com/direction/application_security_testing/composition-analysis/container-scanning/#best-in-class-landscape)
      * [Key Capabilities](https://about.gitlab.com/direction/application_security_testing/composition-analysis/container-scanning/#key-capabilities)
      * [Roadmap](https://about.gitlab.com/direction/application_security_testing/composition-analysis/container-scanning/#roadmap)
      * [Top Competitive Solutions](https://about.gitlab.com/direction/application_security_testing/composition-analysis/container-scanning/#top-competitive-solutions)
    * [Target Audience](https://about.gitlab.com/direction/application_security_testing/composition-analysis/container-scanning/#target-audience)
    * [Pricing and Packaging](https://about.gitlab.com/direction/application_security_testing/composition-analysis/container-scanning/#pricing-and-packaging)
    * [Analyst Landscape](https://about.gitlab.com/direction/application_security_testing/composition-analysis/container-scanning/#analyst-landscape)


## Container Scanning[](https://about.gitlab.com/direction/application_security_testing/composition-analysis/container-scanning/#container-scanning)
|   
---|---  
Stage | [Secure](https://about.gitlab.com/direction/application_security_testing/)  
Maturity | [Viable](https://about.gitlab.com/direction/#maturity)  
Content Last Reviewed | `2024-06-25`  
Content Last Updated | `2024-06-25`  
### Introduction and how you can help[](https://about.gitlab.com/direction/application_security_testing/composition-analysis/container-scanning/#introduction-and-how-you-can-help)
Thanks for visiting this category direction page on Container Scanning in GitLab. This page belongs to the [Composition Analysis](https://handbook.gitlab.com/handbook/product/categories/#composition-analysis-group) group of the [Application Security Testing stage](https://about.gitlab.com/direction/application_security_testing/).
Everyone can contribute:
  * Please comment and contribute in the linked [issues](https://gitlab.com/groups/gitlab-org/-/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name\[\]=Category%3AContainer%20Scanning) or [epics](https://gitlab.com/groups/gitlab-org/-/epics?state=opened&page=1&sort=start_date_desc&label_name\[\]=Category:Container+Scanning) on this page. Sharing your feedback directly on GitLab.com is the best way to contribute to our strategy and vision.
  * Please share feedback directly via email or on a video call. If you're a GitLab user and have direct knowledge of your need for container scanning, we'd especially love to hear from you.


### Overview[](https://about.gitlab.com/direction/application_security_testing/composition-analysis/container-scanning/#overview)
Container scanning analyzes the packages and libraries used in a container image. It identifies dependencies that have been directly included and it also analyzes those dependencies to get a list of their dependencies (also known as indirect or transitive dependencies). Once a full listing of all direct and transitive dependencies has been obtained, container scanning solutions analyze those dependencies to identify known vulnerabilities in those dependencies.
Container Scanning is often considered an element of Software Composition Analysis and Application Security Testing.
Additional details about our current features and capabilities can be [viewed in our documentation](https://docs.gitlab.com/ee/user/application_security/container_scanning/).
### Strategy and Themes[](https://about.gitlab.com/direction/application_security_testing/composition-analysis/container-scanning/#strategy-and-themes)
We have three main themes in our container scanning strategy:
  1. Increase usability 
    1. [Better support scanning of multiple images](https://gitlab.com/groups/gitlab-org/-/epics/3139)
    2. [Archive File Scanning](https://gitlab.com/gitlab-org/gitlab/-/issues/501077)
  2. Improved information access 
    1. [Container Layer Attribition](https://gitlab.com/groups/gitlab-org/-/epics/11622)


### 1 year plan[](https://about.gitlab.com/direction/application_security_testing/composition-analysis/container-scanning/#1-year-plan)
#### What we recently completed[](https://about.gitlab.com/direction/application_security_testing/composition-analysis/container-scanning/#what-we-recently-completed)
In GitLab 18.1 we added support for license scanning of Operating System packages. See more details [here](https://gitlab.com/gitlab-org/gitlab/-/issues/472064).
#### What we are currently working on[](https://about.gitlab.com/direction/application_security_testing/composition-analysis/container-scanning/#what-we-are-currently-working-on)
During 18.2 we are working towards supporting [Archive File scanning](https://gitlab.com/gitlab-org/gitlab/-/issues/501077) for Container Scanning. This will permit users to more easily scan multiple `.tar` files by removing a workaround that caused duplicate findings.
#### What is next for us[](https://about.gitlab.com/direction/application_security_testing/composition-analysis/container-scanning/#what-is-next-for-us)
In the short-term, the Composition Analysis team will be focused on allowing users to more easily [scan multiple images](https://gitlab.com/groups/gitlab-org/-/epics/3139). We will be focused on optimizing performance and making iterative changes based on feedback from users.
#### What is Not Planned Right Now[](https://about.gitlab.com/direction/application_security_testing/composition-analysis/container-scanning/#what-is-not-planned-right-now)
We currently do not have plans to add the following functionality during the next 12 months:
  1. Improvements to our ability to [automatically generate merge requests to update dependencies](https://docs.gitlab.com/ee/user/application_security/vulnerabilities/index.html#resolve-a-vulnerability). We will be focused on rolling out similar functionality for Dependency Scanning and will then turn our attention to making improvements to Container Scanning.


### Best in Class Landscape[](https://about.gitlab.com/direction/application_security_testing/composition-analysis/container-scanning/#best-in-class-landscape)
BIC (Best In Class) is an indicator of forecasted near-term market performance based on a combination of factors, including analyst views, market news, and feedback from the sales and product teams. It is critical that we understand where GitLab appears in the BIC landscape.
#### Key Capabilities[](https://about.gitlab.com/direction/application_security_testing/composition-analysis/container-scanning/#key-capabilities)
For this product area, these are the capabilities a best-in-class solution should provide:
  1. The ability to accurately and comprehensively detect known vulnerabilities for both direct and transitive dependencies in a container image.
  2. Support for detecting vulnerabilities across a wide variety of operating systems.
  3. A robust advisory database that is curated to reduce false positives and contains data from a variety of sources.
  4. Support for shifting vulnerability results left into the IDE.
  5. Support for identifying fix versions when available.
  6. The ability to differentiate between vulnerabilities in packages that exist in the base image vs vulnerabilities in packages that were introduced in a new image layer.
  7. Support for automation to help keep dependencies up-to-date.
  8. Support for runtime analysis of code execution to help filter out vulnerabilities that exist in code that is never executed.
  9. Extensive analysis of other risk factors (quality, supply chain security, maintenance, etc) beyond just security vulnerabilities.


This list represents some key capabilities of a comprehensive container scanning solution. Not all of these capabilities are currently supported by GitLab today.
#### Roadmap[](https://about.gitlab.com/direction/application_security_testing/composition-analysis/container-scanning/#roadmap)
The latest Composition Analysis priorities can be found in the FY26 Execution Roadmap [here (internal)](https://docs.google.com/presentation/d/1ABoGLJkQZNs3Y92NELNrRvjsbo_PNEjGMyCRVz2sU2A/edit?slide=id.g3322950f2e3_12_120#slide=id.g3322950f2e3_12_120).
#### Top Competitive Solutions[](https://about.gitlab.com/direction/application_security_testing/composition-analysis/container-scanning/#top-competitive-solutions)
  * [Black Duck](https://www.blackducksoftware.com/solutions/container-security)
  * [Snyk](https://snyk.io/container-vulnerability-management)
  * [Sonatype Nexus](https://www.sonatype.com/containers)
  * [Qualys](https://www.qualys.com/apps/container-security/)
  * [sysdig](https://sysdig.com/products/kubernetes-security/image-scanning/)
  * [Aqua](https://www.aquasec.com/products/container-security/)
  * [StackRox](https://www.stackrox.com/use-cases/vulnerability-management/)
  * [Prisma Cloud - was TwistLock](https://www.paloaltonetworks.com/prisma/cloud/compute-security/container-security)


### Target Audience[](https://about.gitlab.com/direction/application_security_testing/composition-analysis/container-scanning/#target-audience)
Primary: [Sasha (Software Developer)](https://handbook.gitlab.com/handbook/product/personas/#sasha-software-developer) wants to know when adding a dependency to a container image if it has known vulnerabilities so alternate versions or dependencies can be considered.
Secondary: [Amy (Application Security Engineer)](https://handbook.gitlab.com/handbook/product/personas/#amy-application-security-engineer) and [Isaac (Infrastructure Security Engineer)](https://handbook.gitlab.com/handbook/product/personas/#isaac-infrastructure-security-engineer) want to know what dependencies in their container images have known vulnerabilities, to be alerted if a new vulnerability is published for an existing component, and to know how behind current version the components are.
Other:
  1. [Cameron (Compliance Manager)](https://handbook.gitlab.com/handbook/product/personas/#cameron-compliance-manager)
  2. [Devon (DevOps Engineer)](https://handbook.gitlab.com/handbook/product/personas/#devon-devops-engineer)
  3. [Sidney (Systems Administrator)](https://handbook.gitlab.com/handbook/product/personas/#sidney-systems-administrator)
  4. [Delaney (Development Team Lead)](https://handbook.gitlab.com/handbook/product/personas/#delaney-development-team-lead)


### Pricing and Packaging[](https://about.gitlab.com/direction/application_security_testing/composition-analysis/container-scanning/#pricing-and-packaging)
The GitLab Container Scanning features are all packaged as part of the [GitLab Ultimate tier](https://about.gitlab.com/pricing/ultimate/). This aligns with our [pricing strategy](https://handbook.gitlab.com/handbook/company/pricing/#pricing-strategy) as these features are relevant for executives who are concerned about keeping their organization secured from known vulnerabilities.
### Analyst Landscape[](https://about.gitlab.com/direction/application_security_testing/composition-analysis/container-scanning/#analyst-landscape)
Container Scanning is frequently bundled together with Dependency Scanning and License Compliance to provide an overall Software Composition Analysis (SCA) solution within the Application Security Testing (AST) market.
[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/application_security_testing/composition-analysis/container-scanning/index.html.md) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/application_security_testing/composition-analysis/container-scanning/index.html.md)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fapplication_security_testing%2Fcomposition-analysis%2Fcontainer-scanning%2F&_biz_t=1773331794292&_biz_i=%0ACategory%20Direction%20-%20Container%20Scanning%0A%7C%0AGitLab%0A&_biz_n=55&rnd=815840&cdn_o=a&_biz_z=1773331794414)
suggested results