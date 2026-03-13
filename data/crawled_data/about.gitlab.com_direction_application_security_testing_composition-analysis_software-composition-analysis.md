#  Category Direction - Software Composition Analysis 
  1. You are here:
  2. [GitLab Direction](https://about.gitlab.com/direction/)
  3. [Product Stage Direction - Application Security Testing](https://about.gitlab.com/direction/application_security_testing/)
  4. [Group Direction - Composition Analysis](https://about.gitlab.com/direction/application_security_testing/composition-analysis/)
  5. Category Direction - Software Composition Analysis


The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
  * [Software Composition Analysis](https://about.gitlab.com/direction/application_security_testing/composition-analysis/software-composition-analysis/#software-composition-analysis)
    * [Introduction and how you can help](https://about.gitlab.com/direction/application_security_testing/composition-analysis/software-composition-analysis/#introduction-and-how-you-can-help)
    * [Overview](https://about.gitlab.com/direction/application_security_testing/composition-analysis/software-composition-analysis/#overview)
    * [Strategy and Themes](https://about.gitlab.com/direction/application_security_testing/composition-analysis/software-composition-analysis/#strategy-and-themes)
    * [1 year plan](https://about.gitlab.com/direction/application_security_testing/composition-analysis/software-composition-analysis/#1-year-plan)
      * [What we recently completed](https://about.gitlab.com/direction/application_security_testing/composition-analysis/software-composition-analysis/#what-we-recently-completed)
      * [What we are currently working on](https://about.gitlab.com/direction/application_security_testing/composition-analysis/software-composition-analysis/#what-we-are-currently-working-on)
      * [What is next for us](https://about.gitlab.com/direction/application_security_testing/composition-analysis/software-composition-analysis/#what-is-next-for-us)
      * [What is Not Planned Right Now](https://about.gitlab.com/direction/application_security_testing/composition-analysis/software-composition-analysis/#what-is-not-planned-right-now)
    * [Best in Class Landscape](https://about.gitlab.com/direction/application_security_testing/composition-analysis/software-composition-analysis/#best-in-class-landscape)
      * [Key Capabilities](https://about.gitlab.com/direction/application_security_testing/composition-analysis/software-composition-analysis/#key-capabilities)
      * [Roadmap](https://about.gitlab.com/direction/application_security_testing/composition-analysis/software-composition-analysis/#roadmap)
      * [Top Competitive Solutions](https://about.gitlab.com/direction/application_security_testing/composition-analysis/software-composition-analysis/#top-competitive-solutions)
    * [Target Audience](https://about.gitlab.com/direction/application_security_testing/composition-analysis/software-composition-analysis/#target-audience)
    * [Pricing and Packaging](https://about.gitlab.com/direction/application_security_testing/composition-analysis/software-composition-analysis/#pricing-and-packaging)
    * [Analyst Landscape](https://about.gitlab.com/direction/application_security_testing/composition-analysis/software-composition-analysis/#analyst-landscape)


## Software Composition Analysis[](https://about.gitlab.com/direction/application_security_testing/composition-analysis/software-composition-analysis/#software-composition-analysis)
|   
---|---  
Stage | [Secure](https://about.gitlab.com/direction/application_security_testing/)  
Maturity | [Viable](https://about.gitlab.com/direction/#maturity)  
Content Last Reviewed | `2024-11-20`  
Content Last Updated | `2024-11-20`  
### Introduction and how you can help[](https://about.gitlab.com/direction/application_security_testing/composition-analysis/software-composition-analysis/#introduction-and-how-you-can-help)
Thanks for visiting this category direction page on Software Composition Analysis (Dependency Scanning and License Compliance) in GitLab. This page belongs to the [Composition Analysis](https://handbook.gitlab.com/handbook/product/categories/#composition-analysis-group) group of the [Application Security Testing stage](https://about.gitlab.com/direction/application_security_testing/).
Everyone can contribute:
  * Please comment and contribute in the linked [issues](https://gitlab.com/groups/gitlab-org/-/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name\[\]=Category:Software+Composition+Analysis) or [epics](https://gitlab.com/groups/gitlab-org/-/epics?state=opened&page=1&sort=start_date_desc&label_name\[\]=Category:Software+Composition+Analysis) on this page. Sharing your feedback directly on GitLab.com is the best way to contribute to our strategy and vision.
  * Please share feedback directly via email or on a video call. If you're a GitLab user and have direct knowledge of your need for dependency scanning, we'd especially love to hear from you.


### Overview[](https://about.gitlab.com/direction/application_security_testing/composition-analysis/software-composition-analysis/#overview)
Dependency scanning analyzes the dependencies used in a project. It identifies dependencies that have been directly included and it also analyzes those dependencies to get a list of their dependencies (also known as indirect or transitive dependencies). Once a full listing of all direct and transitive dependencies has been obtained, dependency scanning solutions analyze those dependencies to identify known vulnerabilities in those dependencies.
Dependency Scanning leverages the GitLab Advisory Database to check if any of these dependencies have known vulnerabilities, and it indicates if a package upgrade is needed.
Dependency Scanning and License Compliance are often considered two elements of Software Composition Analysis and Application Security Testing.
Dependency Scanning analyzes the dependencies used in a project. It identifies dependencies that have been directly included and it also analyzes those dependencies to get a list of their dependencies (also known as indirect or transitive dependencies). Once a full listing of all direct and transitive dependencies has been obtained, license compliance solutions analyze those dependencies to identify how those dependencies are licensed. Typically this information is stored in the metadata for the package; however, it may also be present in a file in the dependency's code repository. This type of analysis allows users to get a full list of all the licenses they are using in the project so they can ensure they are willing to adhere to the associated terms and conditions.
Additional details about our current features and capabilities can be [viewed in our documentation](https://docs.gitlab.com/ee/user/application_security/dependency_scanning/).
  * [License scanning](https://docs.gitlab.com/ee/user/compliance/license_scanning_of_cyclonedx_files/)
  * [License approval policies](https://docs.gitlab.com/ee/user/compliance/license_approval_policies.html)
  * [License list](https://docs.gitlab.com/ee/user/compliance/license_list.html)


### Strategy and Themes[](https://about.gitlab.com/direction/application_security_testing/composition-analysis/software-composition-analysis/#strategy-and-themes)
We have five main themes in our software composition analysis strategy:
  1. **Shifting dependency scanning and license compliance left** - Our goal is to provide Dependency Scanning and License Compliance as part of the standard development process. This means that Dependency Scanning and License Compliance are executed every time a new commit is pushed to a branch, identifying newly introduced vulnerabilities in the merge request. We also include Dependency Scanning and License Compliance as part of [Auto DevOps](https://docs.gitlab.com/ee/topics/autodevops/).
  2. **Accurate component detection** - Our goal is to be able to identify the correct dependencies and versions accurately for the languages that we support. For this reason, we attempt to build Java and Python projects before identifying dependencies so that we are not forced to guess which version in a version range is actually used in the final application.
  3. **Accurate license detection** - Our goal is to support multiple license detection methods and to allow those methods to work together to identify licenses accurately. Eventually we would like to add support for full SPDX expressions so we can accurately handle packages with complex license scenarios.
  4. **Continuous scanning** - Scanning for known vulnerabilities needs to be a continuous effort because the list of known vulnerabilities is constantly growing. To stay secure, users need a solution that will be updated constantly with the latest threat data.
  5. **Comprehensive license detection** - Our goal is to continue to add data to our license database so we can cover both a high percentage of the total open source packages available for the languages that we support. Ideally we will achieve full coverage for the most popular packages for each language that we support.


### 1 year plan[](https://about.gitlab.com/direction/application_security_testing/composition-analysis/software-composition-analysis/#1-year-plan)
#### What we recently completed[](https://about.gitlab.com/direction/application_security_testing/composition-analysis/software-composition-analysis/#what-we-recently-completed)
In GitLab 17.5 we added [Static Reachability for Java and Python](https://gitlab.com/groups/gitlab-org/-/epics/14177) as an experimental feature. This was a product of our [Oxeye acquisition](https://about.gitlab.com/press/releases/2024-03-20-gitlab-acquires-oxeye-to-advance-application-security-and-governance-capabilities/).
In GitLab 17.6 we added support for the [Exploit Prediction Scoring System](https://gitlab.com/groups/gitlab-org/-/epics/11544). This data is available through our GraphQL API and will be available in the GitLab UI in a future milestone.
#### What we are currently working on[](https://about.gitlab.com/direction/application_security_testing/composition-analysis/software-composition-analysis/#what-we-are-currently-working-on)
During 17.7 we are working toward adding better vulnerability data to help prioritize remediation efforts. This will be accomplished by adding support for the [Known Exploitable Vulnerability catalog](https://gitlab.com/groups/gitlab-org/-/epics/11912), also known as KEV. Users will be able to better prioritize results by understanding which vulnerabilities have been exploited. Using KEV, EPSS, and CVSS Severity will provide a more accurate picture of the threat profile of projects.
#### What is next for us[](https://about.gitlab.com/direction/application_security_testing/composition-analysis/software-composition-analysis/#what-is-next-for-us)
Over the next few months, we will be focused on rolling out our [new dependency scanning analyzer](https://gitlab.com/gitlab-org/gitlab/-/issues/458920), which will replace Gemnasium. Our new analyzer will use the SBOM as the core scanning target. This change will better serve users by allowing us to more rapidly deliver features, support more languages, accept third party SBOMs for analysis, and reduce the overall maintenance burden for our team. Users will enable the new analyzer via a CI/CD component.
#### What is Not Planned Right Now[](https://about.gitlab.com/direction/application_security_testing/composition-analysis/software-composition-analysis/#what-is-not-planned-right-now)
We currently do not have plans to add the following functionality during the next 12 months:
  1. Support for runtime analysis of code execution to help filter out vulnerabilities that exist in code that is never executed.
  2. Automatic categorization of licenses by type


### Best in Class Landscape[](https://about.gitlab.com/direction/application_security_testing/composition-analysis/software-composition-analysis/#best-in-class-landscape)
BIC (Best In Class) is an indicator of forecasted near-term market performance based on a combination of factors, including analyst views, market news, and feedback from the sales and product teams. It is critical that we understand where GitLab appears in the BIC landscape.
#### Key Capabilities[](https://about.gitlab.com/direction/application_security_testing/composition-analysis/software-composition-analysis/#key-capabilities)
For this product area, these are the capabilities a best-in-class solution should provide:
  1. The ability to accurately and comprehensively detect known vulnerabilities for both direct and transitive dependencies in a project.
  2. Support for detecting vulnerabilities across a wide variety of programming languages.
  3. A robust advisory database that is curated to reduce false positives and contains data from a variety of sources.
  4. Support for shifting vulnerability results left into the IDE.
  5. Support for identifying fix versions when available.
  6. Support for viewing the hierarchical chain of dependencies (typically in a dependency graph or dependency tree) to allow developers to see which upstream dependency will needs to be updated to fix a downstream vulnerability.
  7. Support for automation to help keep dependencies up-to-date.
  8. Support for runtime analysis of code execution to help filter out vulnerabilities that exist in code that is never executed.
  9. Extensive analysis of other risk factors (quality, supply chain security, maintenance, etc) beyond just security vulnerabilities.
  10. The ability to accurately and comprehensively detect licenses for both direct and transitive dependencies in a project.
  11. Support for detecting licenses across a wide variety of programming languages.
  12. Support for multiple methods of detecting licenses (metadata, files, embedded licenses).
  13. The ability to detect licenses for closed-source dependencies.
  14. The ability to support both basic and complex SPDX expressions.
  15. The ability to easily show legal and compliance teams the terms and conditions of licenses that are being included.
  16. The ability to enforce policies prohibiting specific licenses from being used in an organization.
  17. Reporting and filtering to allow users to easily see which licenses are already in use.
  18. Automatic license classification to organize licenses into categories based on their terms and conditions.


This list represents some key capabilities of a comprehensive software composition analysis solution. Not all of these capabilities are currently supported by GitLab today.
#### Roadmap[](https://about.gitlab.com/direction/application_security_testing/composition-analysis/software-composition-analysis/#roadmap)
Our [prioritized roadmap](https://about.gitlab.com/direction/application_security_testing/composition-analysis/#priorities) can be viewed on our group direction page. Plans to move the category from [Viable to Complete](https://gitlab.com/groups/gitlab-org/-/epics/1664) are tracked in GitLab.
#### Top Competitive Solutions[](https://about.gitlab.com/direction/application_security_testing/composition-analysis/software-composition-analysis/#top-competitive-solutions)
  * [Black Duck by Synopsys](https://www.blackducksoftware.com/solutions/application-security)
  * [CA Veracode](https://www.veracode.com/security/)
  * [Contrast](https://www.contrastsecurity.com/open-source-security-software)
  * [Datadog](https://www.datadoghq.com/)
  * [GitHub](https://github.com/)
  * [greenkeeper](https://greenkeeper.io/)
  * [HCL AppScan](https://www.hcltechsw.com/wps/portal/products/appscan/features)
  * [JFrog Xray](https://jfrog.com/xray/)
  * [Micro Focus Fortify](https://www.microfocus.com/en-us/portfolio/application-security)
  * [Snyk](https://snyk.io/product/)
  * [Sonatype Nexus](https://www.sonatype.com/nexus-auditor)
  * [Whitesource](https://www.whitesourcesoftware.com/open-source-security/)


### Target Audience[](https://about.gitlab.com/direction/application_security_testing/composition-analysis/software-composition-analysis/#target-audience)
Primary: [Sasha (Software Developer)](https://handbook.gitlab.com/handbook/product/personas/#sasha-software-developer) wants to know when adding a dependency if it has known vulnerabilities so alternate versions or dependencies can be considered.
Secondary: [Amy (Application Security Engineer)](https://handbook.gitlab.com/handbook/product/personas/#amy-application-security-engineer) and [Isaac (Infrastructure Security Engineer)](https://handbook.gitlab.com/handbook/product/personas/#isaac-infrastructure-security-engineer) want to know what dependencies have known vulnerabilities, to be alerted if a new vulnerability is published for an existing component, and to know how behind current version the components are.
Other:
  1. [Cameron (Compliance Manager)](https://handbook.gitlab.com/handbook/product/personas/#cameron-compliance-manager)
  2. [Devon (DevOps Engineer)](https://handbook.gitlab.com/handbook/product/personas/#devon-devops-engineer)
  3. [Sidney (Systems Administrator)](https://handbook.gitlab.com/handbook/product/personas/#sidney-systems-administrator)
  4. [Delaney (Development Team Lead)](https://handbook.gitlab.com/handbook/product/personas/#delaney-development-team-lead)


### Pricing and Packaging[](https://about.gitlab.com/direction/application_security_testing/composition-analysis/software-composition-analysis/#pricing-and-packaging)
The GitLab Dependency Scanning features are all packaged as part of the [GitLab Ultimate tier](https://about.gitlab.com/pricing/ultimate/). This aligns with our [pricing strategy](https://handbook.gitlab.com/handbook/company/pricing/#pricing-strategy) as these features are relevant for executives who are concerned about keeping their organization secured from known vulnerabilities.
### Analyst Landscape[](https://about.gitlab.com/direction/application_security_testing/composition-analysis/software-composition-analysis/#analyst-landscape)
Dependency Scanning and License Compliance are frequently bundled together with Container Scanning to provide an overall Software Composition Analysis (SCA) solution within the Application Security Testing (AST) market.
[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/application_security_testing/composition-analysis/software-composition-analysis/index.html.md) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/application_security_testing/composition-analysis/software-composition-analysis/index.html.md)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fapplication_security_testing%2Fcomposition-analysis%2Fsoftware-composition-analysis%2F&_biz_t=1773331789987&_biz_i=%0ACategory%20Direction%20-%20Software%20Composition%20Analysis%0A%7C%0AGitLab%0A&_biz_n=54&rnd=958478&cdn_o=a&_biz_z=1773331790199)
suggested results