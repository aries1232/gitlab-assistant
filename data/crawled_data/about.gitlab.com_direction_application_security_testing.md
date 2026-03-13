#  Product Stage Direction - Application Security Testing 
  1. You are here:
  2. [GitLab Direction](https://about.gitlab.com/direction/)
  3. Product Stage Direction - Application Security Testing


####  Maintained by:
[ ![VP of Product Management](https://about.gitlab.com/images/gitlab-logo-extra-whitespace.png) VP of Product Management  @oazaria  ](https://gitlab.com/oazaria)
The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
## On this page
  * [Overview](https://about.gitlab.com/direction/application_security_testing/#overview)
    * [Groups](https://about.gitlab.com/direction/application_security_testing/#groups)
  * [3-year strategy](https://about.gitlab.com/direction/application_security_testing/#3-year-strategy)
  * [3-year themes](https://about.gitlab.com/direction/application_security_testing/#3-year-themes)
    * [Scan everything, but don't get in the way](https://about.gitlab.com/direction/application_security_testing/#scan-everything-but-dont-get-in-the-way)
    * [Make better risk decisions with richer context](https://about.gitlab.com/direction/application_security_testing/#make-better-risk-decisions-with-richer-context)
    * [Take action, not just inventory](https://about.gitlab.com/direction/application_security_testing/#take-action-not-just-inventory)
  * [1-year plan](https://about.gitlab.com/direction/application_security_testing/#1-year-plan)
  * [Pricing](https://about.gitlab.com/direction/application_security_testing/#pricing)
    * [Ultimate](https://about.gitlab.com/direction/application_security_testing/#ultimate)
    * [Free and Premium](https://about.gitlab.com/direction/application_security_testing/#free-and-premium)
  * [Categories](https://about.gitlab.com/direction/application_security_testing/#categories)
    * [SAST](https://about.gitlab.com/direction/application_security_testing/#sast)
    * [Secret Detection](https://about.gitlab.com/direction/application_security_testing/#secret-detection)
    * [Code Quality](https://about.gitlab.com/direction/application_security_testing/#code-quality)
    * [DAST](https://about.gitlab.com/direction/application_security_testing/#dast)
    * [API Security](https://about.gitlab.com/direction/application_security_testing/#api-security)
    * [Fuzz Testing](https://about.gitlab.com/direction/application_security_testing/#fuzz-testing)
    * [Software Composition Analysis](https://about.gitlab.com/direction/application_security_testing/#software-composition-analysis)
    * [Container Scanning](https://about.gitlab.com/direction/application_security_testing/#container-scanning)
    * [GitLab Advisory Database](https://about.gitlab.com/direction/application_security_testing/#gitlab-advisory-database)
    * [Attack Emulation](https://about.gitlab.com/direction/application_security_testing/#attack-emulation)


**Security scanning that AppSec teams trust, and developers love**
DevSecOpsPlanCodeBuildTestReleaseDeployOperateMonitorSecurityCompliance
Application Security Testing
## Overview[](https://about.gitlab.com/direction/application_security_testing/#overview)
The Application Security Testing (AST) stage helps customers find vulnerabilities in applications before they reach production. We focus on developing scanning capabilities to find these vulnerabilities, then we work closely with the [Security Risk Management](https://about.gitlab.com/direction/security_risk_management/) and [Software Supply Chain Security](https://about.gitlab.com/direction/software_supply_chain_security/) stages to ensure that organizations can take action on the vulnerabilities our scanners detect.
### Groups[](https://about.gitlab.com/direction/application_security_testing/#groups)
The AST stage is made up of five groups:
  * [Static Analysis](https://about.gitlab.com/direction/application_security_testing/static-analysis/): Assess applications and services for vulnerabilities and weaknesses by scanning source code.
  * [Secret Detection](https://about.gitlab.com/direction/application_security_testing/secret-detection/): Assess code to prevent leaked secrets, before and after commit.
  * [Dynamic Analysis](https://about.gitlab.com/direction/application_security_testing/dynamic-analysis/): Assess running applications and services for vulnerabilities and weaknesses by analyzing application behavior at runtime.
  * [Composition Analysis](https://about.gitlab.com/direction/application_security_testing/composition-analysis/): Assess applications and services by analyzing your dependencies and containers for vulnerabilities and weaknesses. Confirm that only approved licenses are in use.
  * [Vulnerability Research](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/vulnerability-research/): Lead the ideation and evolution of GitLab's security capabilities via the application of innovative security research and emerging technologies. Curate high-quality detection rules across GitLab's suite of security analyzers.


## 3-year strategy[](https://about.gitlab.com/direction/application_security_testing/#3-year-strategy)
Customer needs for Application Security Testing (AST) are evolving rapidly, driven by the increasing pace and complexity of modern software development and the growing sophistication of security threats. We see at least two major themes in the AST market today:
  1. Developer-centricity: 
     * Analyst firms like Gartner and Forrester highlight a "seismic shift" towards more _integrated, developer-centric solutions_ that seamlessly fit into existing workflows.
     * Organizations are prioritizing tools that offer _high accuracy_ , _minimal friction_ , and _actionable insights_ so developers can cut through the noise and focus on impactful changes.
     * There is a growing emphasis on _continuous scanning_ across the entire software development lifecycle (SDLC), enabling _real-time security feedback and remediation_ and aligning with the broader industry movement toward "shifting security left".
  2. Platforms. The AST market has also continued a long-term trend toward a more bundled, _platform-oriented_ model, meaning that organizations can increasingly buy all of their key capabilities from a single vendor.


In the next 3 years, we expect the AST market will:
  1. Shift from standalone security _tools_ to security _capabilities_ that are deeply embedded in development platforms and IDEs, making security testing a streamlined part of the development workflow.
  2. Increasingly emphasize AI-enhanced testing that moves beyond pattern matching and understands application context and business logic, dramatically reducing false positives while catching complex vulnerabilities.
  3. Deliver more actionable security insights by synthesizing context across different scan types in unified platforms and interfaces.
  4. Move beyond just _finding_ vulnerabilities, toward more actively helping _fix_ them through automated patches and intelligent code suggestions.


As a unified, AI-powered DevSecOps platform, GitLab is well-suited to deliver what the market needs. We will continue to invest in our AST capabilities to enable security teams to scale their impact and achieve their security goals.
## 3-year themes[](https://about.gitlab.com/direction/application_security_testing/#3-year-themes)
### Scan everything, but don't get in the way[](https://about.gitlab.com/direction/application_security_testing/#scan-everything-but-dont-get-in-the-way)
The increasing pace of modern software development demands that we push security testing further left than before, integrating it into existing workflows rather than forcing teams to adapt their processes or context-switch to separate tools.
Moving security scanning directly into the IDE and pre-commit stages enables developers to catch vulnerabilities, exposed secrets, and dependency issues before they even enter the codebase, dramatically reducing remediation costs and team overhead.
For this proactive approach to succeed, security tools must provide clear, actionable feedback that developers can understand without deep security expertise, including precise code locations and step-by-step remediation guidance with examples of secure coding patterns.
By making security both approachable and efficient, we help organizations build a true DevSecOps culture where security becomes a natural part of every developer's daily work, transforming how organizations approach application security while significantly reducing the burden on overburdened security specialists.
**To achieve this theme, GitLab will pursue capabilities like:**
  * Delivering scan results at the speed of software development by offering: 
    * Real-time scanning for SAST and SCA vulnerabilities and leaked secrets.
    * Intelligent incremental scans that avoid re-scanning parts of the application that haven't changed.
  * Identifying runtime security issues early in the development phase with DAST unit tests and by running DAST scans in development environments like `localhost`.
  * Integrating Secret Detection scanning across the platform to prevent leaked secrets in every written place like descriptions and comments on issues, epics, and merge requests, wikis, and more.
  * Automatically scanning for CVEs in repositories and registries for dependencies, packages, and containers.
  * Detecting malicious packages and prevent them from entering your software supply chain


### Make better risk decisions with richer context[](https://about.gitlab.com/direction/application_security_testing/#make-better-risk-decisions-with-richer-context)
In today's complex security landscape, presenting raw vulnerability data without context can lead teams to work on less impactful tasks or accept risks without realizing the consequences. That doesn't work well for anyone.
By combining multiple security scanning methods and leveraging more advanced techniques like AI and machine learning, we can provide deeper context and more accurate risk assessments for each security finding. This intelligence-driven approach helps teams cut through the noise of security alerts, focusing remediation efforts on vulnerabilities that pose the greatest actual risk to their applications. Integration across different security disciplines creates a comprehensive view of each vulnerability's impact and exploitability, enabling more confident decision-making about when and how to remediate issues.
The power of machine learning transforms security scanning from a simple detection tool into an intelligent advisory system that helps teams make informed, strategic decisions about their security posture and resource allocation.
**To achieve this theme, GitLab will pursue capabilities like:**
  * Integrating detection capabilities across scanning disciplines to provide more actionable outcomes.
  * Using SAST for advanced tasks like reachability analysis and API discovery, so we can enrich DAST and other scanning processes.
  * Correlating and deduplicating scanning outputs to reduce noise, uncover the most urgent exploitable issues, and focus attention on the most impactful remediations.
  * Leveraging AI/ML to reduce false positives by understanding normal code structure, commit history, and runtime behavior.


### Take action, not just inventory[](https://about.gitlab.com/direction/application_security_testing/#take-action-not-just-inventory)
When tools identify vulnerabilities but don't provide a clear path to resolution, organizations end up exposed to security risks for longer than necessary. Worse still, as backlogs of security issues grow, organizations end up accepting risks without realizing it—an untriaged and unresolved vulnerability is one that's tacitly accepted.
Modern security tools must go beyond detection to provide automated remediation pathways that help both developers and security teams efficiently address vulnerabilities.
  * Developers can make larger impacts when they receive automated merge requests for dependency updates, intelligent suggestions for fixing vulnerable code, and clear guidance on implementing secure alternatives directly within their development environment.
  * Security professionals benefit from automated workflows that can immediately revoke exposed secrets, quarantine vulnerable dependencies, and orchestrate large-scale security updates across multiple repositories without manual legwork.


As applications and security threats grow more complex, effective security programs have to rely on automation to scale up. By transforming security findings into automated actions, intelligent tools help organizations dramatically reduce their mean time to remediation while allowing both development and security teams to focus on strategic work rather than routine maintenance.
**To achieve this theme, GitLab will pursue capabilities like:**
  * Automating remediation actions like revoking exposed secrets, blocking insecure code, and upgrading vulnerable dependencies.
  * Continuing to invest in GitLab Duo Vulnerability Explanation and Vulnerability Resolution to produce better recommendations.
  * Providing automated system hardening, such as removing dependencies that are not in use.
  * Improving AST scan results so that they are easier to understand and act on.


## 1-year plan[](https://about.gitlab.com/direction/application_security_testing/#1-year-plan)
To see what we're planning, check the individual [group](https://about.gitlab.com/direction/application_security_testing/#groups) or [category](https://about.gitlab.com/direction/application_security_testing/#categories) direction pages.
## Pricing[](https://about.gitlab.com/direction/application_security_testing/#pricing)
Application Security Testing pricing and tiering reflects GitLab's overall [pricing model](https://handbook.gitlab.com/handbook/company/pricing/).
##### Ultimate[](https://about.gitlab.com/direction/application_security_testing/#ultimate)
We focus our efforts primarily on Ultimate. Advanced security is [an Ultimate pricing theme](https://handbook.gitlab.com/handbook/company/pricing/#ultimate) and helps customers deliver on organization-wide security and compliance priorities.
Advanced features, including technology developed in-house at GitLab and technology we've [acquired](https://handbook.gitlab.com/handbook/acquisitions/), are available only in Ultimate.
##### Free and Premium[](https://about.gitlab.com/direction/application_security_testing/#free-and-premium)
We make a subset of our AST scanners available in all tiers (including Free). We typically do this when the scanners are themselves open-source.
We do not specifically focus on Premium.
## Categories[](https://about.gitlab.com/direction/application_security_testing/#categories)
##### SAST[](https://about.gitlab.com/direction/application_security_testing/#sast)
Scans your application source code and binaries to spot potential vulnerabilities before deployment. SAST supports scanning a variety of different programming languages and automatically chooses the right analyzer even if your project uses more than one language. Vulnerabilities, additional data, and solutions are shown in-line with every merge request. Scanner results are collected and presented as a single report. This category is planned, but not yet available.
Priority: high • [Documentation](https://docs.gitlab.com/user/application_security/sast/) • [Direction](https://about.gitlab.com/direction/application_security_testing/static-analysis/sast/)
##### Secret Detection[](https://about.gitlab.com/direction/application_security_testing/#secret-detection)
Scans your repository to help prevent your secrets from being exposed. Secret Detection scanning works on all text files, regardless of the language or framework used. Code pushed to a remote Git branch can be rejected if a secret is detected. This category is planned, but not yet available.
Priority: medium • [Documentation](https://docs.gitlab.com/user/application_security/secret_detection/) • [Direction](https://about.gitlab.com/direction/application_security_testing/secret-detection/secret-detection/)
##### Code Quality[](https://about.gitlab.com/direction/application_security_testing/#code-quality)
Analyzes your source code quality and complexity. This helps keep your project’s code simple, readable, and easier to maintain. This category is planned, but not yet available.
[Documentation](https://docs.gitlab.com/ci/testing/code_quality) • [Direction](https://about.gitlab.com/direction/application_security_testing/static-analysis/code-quality/)
##### DAST[](https://about.gitlab.com/direction/application_security_testing/#dast)
Runs automated penetration tests to find vulnerabilities in web applications and APIs as they are running. DAST can run live attacks against a Review App, an externally deployed application, or an active API. Scans can be run for every merge request, on a schedule, or even on-demand. DAST supports user inputted HTTP credentials to test private areas of your application. Vulnerabilities, additional data, and solutions are shown in-line with every merge request. Scanner results are presented as a single report. This category is planned, but not yet available.
Priority: high • [Documentation](https://docs.gitlab.com/user/application_security/dast/) • [Direction](https://about.gitlab.com/direction/application_security_testing/dynamic-analysis/dast/)
##### API Security[](https://about.gitlab.com/direction/application_security_testing/#api-security)
Secures and protects web Application Programming Interfaces from unauthorized access, misuse, and attacks. Tests for known vulnerabilities by performing penetration testing of APIs with DAST. Finds unknown vulnerabilities by performing Fuzz Testing of web API operation parameters.Users can provide credentials to test authenticated APIs. Vulnerabilities, additional data, and solutions are shown in-line with every merge request.. Scanner results are collected and presented as a single report. This category is planned, but not yet available.
Priority: high • [Documentation](https://docs.gitlab.com/user/application_security/api_security_testing/) • [Direction](https://about.gitlab.com/direction/application_security_testing/dynamic-analysis/api-security/)
##### Fuzz Testing[](https://about.gitlab.com/direction/application_security_testing/#fuzz-testing)
Sends random inputs to an instrumented version of your application in an effort to cause unexpected behavior in order to identify a bug that needs to be addressed. Helps you discover bugs and potential security issues that other QA processes may miss. This category is planned, but not yet available.
Priority: high • [Documentation](https://docs.gitlab.com/user/application_security/coverage_fuzzing/) • [Direction](https://about.gitlab.com/direction/application_security_testing/dynamic-analysis/fuzz-testing/)
##### Software Composition Analysis[](https://about.gitlab.com/direction/application_security_testing/#software-composition-analysis)
Analyzes external dependencies within your application for known vulnerabilities on each CI/CD code commit. Vulnerabilities, additional data, and solutions are shown in-line with every merge request. Scanner results are collected and presented as a single report. Upon code commit, project dependencies are searched for approved and denied licenses defined by per project custom policies. Software licenses are identified if they are not within policy and are shown in-line for every merge request for immediate resolution. This category is planned, but not yet available.
Priority: high • [Documentation](https://docs.gitlab.com/user/application_security/dependency_scanning/) • [Direction](https://about.gitlab.com/direction/application_security_testing/composition-analysis/software-composition-analysis)
##### Container Scanning[](https://about.gitlab.com/direction/application_security_testing/#container-scanning)
Scans your container images for known vulnerabilities within the application environment. Image contents are analyzed against public vulnerability databases.Security findings, additional data, and solutions reported in-line with every merge request along with additional data including solutions. Results are presented as a single report. Container Scanning is considered part of Software Composition Analysis. This category is planned, but not yet available.
Priority: medium • [Documentation](https://docs.gitlab.com/user/application_security/container_scanning/) • [Direction](https://about.gitlab.com/direction/application_security_testing/composition-analysis/container-scanning/)
##### GitLab Advisory Database[](https://about.gitlab.com/direction/application_security_testing/#gitlab-advisory-database)
The GitLab Advisory Database serves as a repository for security advisories related to software dependencies.
Priority: high • [Direction](https://about.gitlab.com/direction/application_security_testing/composition-analysis/software-composition-analysis/)
##### Attack Emulation[](https://about.gitlab.com/direction/application_security_testing/#attack-emulation)
Continuously assess your applications and services are not vulnerable to security threats through automated, real-world emulated scenarios to identify weaknesses in your attack surface
Priority: low • [Documentation](https://docs.gitlab.com/security/hardening/)
_  
Last Reviewed: 2025-02-20  
Last Updated: 2025-02-20 _
[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/application_security_testing/template.html.md.erb) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/application_security_testing/template.html.md.erb)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fapplication_security_testing%2F&_biz_t=1773331586937&_biz_i=%0AProduct%20Stage%20Direction%20-%20Application%20Security%20Testing%0A%7C%0AGitLab%0A&_biz_n=11&rnd=961317&cdn_o=a&_biz_z=1773331587335)
suggested results