#  Category Direction - API Security 
  1. You are here:
  2. [GitLab Direction](https://about.gitlab.com/direction/)
  3. [Product Stage Direction - Application Security Testing](https://about.gitlab.com/direction/application_security_testing/)
  4. [Group Direction - Dynamic Analysis](https://about.gitlab.com/direction/application_security_testing/dynamic-analysis/)
  5. Category Direction - API Security


####  Maintained by:
[ ![Joel Patterson](https://about.gitlab.com/images/team/joelpatterson-crop.jpg) ](https://gitlab.com/joelpatterson) [ ![VP of Product Management](https://about.gitlab.com/images/gitlab-logo-extra-whitespace.png) ](https://gitlab.com/oazaria)
The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
  * [API Security](https://about.gitlab.com/direction/application_security_testing/dynamic-analysis/api-security/#api-security)
    * [Introduction and how you can help](https://about.gitlab.com/direction/application_security_testing/dynamic-analysis/api-security/#introduction-and-how-you-can-help)
    * [Overview](https://about.gitlab.com/direction/application_security_testing/dynamic-analysis/api-security/#overview)
    * [Strategy and Themes](https://about.gitlab.com/direction/application_security_testing/dynamic-analysis/api-security/#strategy-and-themes)
    * [1 year plan](https://about.gitlab.com/direction/application_security_testing/dynamic-analysis/api-security/#1-year-plan)
      * [Roadmap](https://about.gitlab.com/direction/application_security_testing/dynamic-analysis/api-security/#roadmap)
      * [What's Next & Why](https://about.gitlab.com/direction/application_security_testing/dynamic-analysis/api-security/#whats-next--why)
    * [3 year plan](https://about.gitlab.com/direction/application_security_testing/dynamic-analysis/api-security/#3-year-plan)
    * [Best in Class Landscape](https://about.gitlab.com/direction/application_security_testing/dynamic-analysis/api-security/#best-in-class-landscape)
      * [Key Capabilities](https://about.gitlab.com/direction/application_security_testing/dynamic-analysis/api-security/#key-capabilities)
  * [Competitive Landscape](https://about.gitlab.com/direction/application_security_testing/dynamic-analysis/api-security/#competitive-landscape)
  * [Pricing and Packaging](https://about.gitlab.com/direction/application_security_testing/dynamic-analysis/api-security/#pricing-and-packaging)
  * [Analyst Landscape](https://about.gitlab.com/direction/application_security_testing/dynamic-analysis/api-security/#analyst-landscape)


## API Security[](https://about.gitlab.com/direction/application_security_testing/dynamic-analysis/api-security/#api-security)
|   
---|---  
Stage | [Secure](https://about.gitlab.com/direction/application_security_testing/)  
Maturity | [Viable](https://about.gitlab.com/direction/#maturity)  
Content Last Reviewed | `2025-06-25`  
### Introduction and how you can help[](https://about.gitlab.com/direction/application_security_testing/dynamic-analysis/api-security/#introduction-and-how-you-can-help)
Thank you for visiting this category direction page on API Security Testing at GitLab. This page belongs to the [Dynamic Analysis](https://handbook.gitlab.com/handbook/product/categories/#dynamic-analysis-group) group of the [Application Security Testing stage](https://about.gitlab.com/direction/application_security_testing/).
Everyone can contribute:
  * Please comment and contribute in the linked [issues](https://gitlab.com/gitlab-org/gitlab/-/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name\[\]=Category%3AAPI%20Security) on this page. Sharing your feedback directly on GitLab.com is the best way to contribute to our strategy and vision.
  * Please share feedback directly via email or on a video call. If you're a GitLab user and have direct knowledge of your need for API Security, we'd especially love to hear from you.


### Overview[](https://about.gitlab.com/direction/application_security_testing/dynamic-analysis/api-security/#overview)
API Security encompasses many features that reduce security risks in Application Programming Interfaces (APIs) and protect them from attacks. Modern applications consist of numerous APIs, which make it efficient for software programs to interact with one another. APIs make it easy for developers to build and maintain applications, and they make it easy for machines to share and modify data. APIs frequently transmit sensitive data and expose business logic, making them attractive targets for hackers. Traditional application security techniques should be used in the API development phase, and WAFs and gateways should be used in production, but these methods must also be augmented by additional API-focused security tools and techniques. As API security has historically been the domain of security teams, rather than developers, testing the API in its running state often is overlooked during the development process. Yet, the shift-right methods that many organizations use, including WAFs and gateways, have proven to be insufficient to stop security incidents on their own. It's clear that a shift-everywhere, defense-in-depth approach, which includes identifying and remediating security weaknesses early in the API management lifecycle is critical.
As a category, API Security includes: API Security Testing (dynamic) and API Fuzz Testing for REST, GraphQL, and SOAP APIs. Future capabilities include: [API Discovery](https://www.akamai.com/glossary/what-is-api-discovery), [API Inventory](https://www.cequence.ai/blog/api-security/what-is-api-inventory), API [Risk Scoring](https://www.crowdstrike.com/cybersecurity-101/risk-based-vulnerability-management), API Analysis, [ABAC API Service Mesh](https://www.cncf.io/blog/simplifying-microservices-security-with-a-service-mesh), [OpenAPI Spec Audit](https://docs.42crunch.com/latest/content/concepts/api_contract_security_audit.htm), and [gRPC support](https://grpc.io/docs/what-is-grpc/introduction) . This feature set will evolve over time to address the most pressing API Security issues.
  * API Security Testing includes dynamic tests that simulate the way a hacker would make malicious requests. The goal is to identify weaknesses (CWEs) that could be exploited and lead to data breaches or other security incidents.
  * API Fuzz Testing sets operation parameters to unexpected values in an effort to cause unexpected behavior and errors in the API backend. This helps identify bugs and potential security issues that other QA processes may miss.


### Strategy and Themes[](https://about.gitlab.com/direction/application_security_testing/dynamic-analysis/api-security/#strategy-and-themes)
Our goal is to help customers reduce the security risks and compliance challenges they face while building and maintaining APIs. We do this by focusing on the earliest phases of the API lifecycle including: design, build, and test. By incorporating security testing early in the API lifecycle, we can help organizations become secure by design. Our themes include:
  1. **Shifting API Security Testing and Compliance left** - Our goal is to provide API Security scanning as part of the standard development process. This means that API security is executed every time a new review app is available or a build is deployed to a server.
  2. **Accurate API Specifications** - Strong API security begins with a well-defined OpenAPI spec. Open API specifications define the expected behavior of an API. Our goal is to be able to analyze pre-existing API specifications and to automatically generate accurate API specifications where they do not exist, to help enable API Security Testing. Accurately defining the expected behavior helps to identify potential authorization and authentication, data validation, and other security risks in APIs.
  3. **Accurate API Inventory** - Our goal is to be able to identify all of the APIs in an organization because one cannot protect what one cannot see. Many organizations today do not have visibility into their API attack surface.
  4. **Continuous scanning** - Scanning for security weaknesses needs to be a continuous effort because the list of API-based threats is constantly growing. To stay secure, users need a solution that will be updated constantly with the latest detections.
  5. **Secure by Design** - Providing API design and build guardrails within a DevSecOps platform, can help developers and security teams greatly reduce the biggest security gaps that impact APIs today–authentication and authorization failures.


### 1 year plan[](https://about.gitlab.com/direction/application_security_testing/dynamic-analysis/api-security/#1-year-plan)
#### Roadmap[](https://about.gitlab.com/direction/application_security_testing/dynamic-analysis/api-security/#roadmap)
See our [prioritized roadmap here](https://about.gitlab.com/direction/application_security_testing/dynamic-analysis/#priorities).
#### What's Next & Why[](https://about.gitlab.com/direction/application_security_testing/dynamic-analysis/api-security/#whats-next--why)
At the moment, the API Security roadmap has been put on hold as we focus our efforts on high-impact projects like browser-based DAST. Once we restart our development efforts, we will update the roadmap with what will be coming up next. We aim to reorient our roadmap in second half FY2027 to focus on both browser-based DAST and API Security. The category has not seen much recent investment due to other pressing priorities. 
### 3 year plan[](https://about.gitlab.com/direction/application_security_testing/dynamic-analysis/api-security/#3-year-plan)
Looking forward, we will continue to focus on features that enable customers to efficiently reduce risk. We want to ensure API security risks are easy to prioritize and remediate, and easy to address earlier in the API management lifecycle. Future capabilities focus on helping teams design and build secure APIs, and perform security testing that is as close to real-world API requests as possible.
  1. [API Risk Score](https://gitlab.com/gitlab-org/gitlab/-/issues/442808) will enable customers to better prioritize API Security findings based on the risk associated with each API endpoint. Risk scores will be affected by whether an API transmits sensitive data and by what kind of security testing has been performed. Customers will also be able to influence the score by marking APIs as business critical.
  2. [API Analysis](https://gitlab.com/groups/gitlab-org/-/epics/10504) expands the depth of our API Security Testing by correctly determining how a sequence of API calls should be tested together. Rather than assessing the security results of one API call via one check, this enables testing to more accurately emmulate the API calls real-world users might make, and the responses they would get.
  3. [ABAC API Service Mesh](https://gitlab.com/gitlab-org/gitlab/-/issues/455929) would enable customers to configure and maintain a YAML-based service mesh from within GitLab's UI. This would help shift security left by centralizing API authorization policies early in the development lifecycle. This would help reduce customer risk for 3 out of the top 10 OWASP API Top 10 risks (authorization risks).
  4. [OpenAPI Spec Audit](https://gitlab.com/gitlab-org/gitlab/-/issues/442776) is related to API Discovery, but approaches the problem from a different angle. API Discovery assumes an OpenAPI spec has not yet been generated for an API, whereas OpenAPI Spec Audit applies whenever a spec already exists. This feature is most relevant for large enterprises that have API management teams. The audit score analyses an OpenAPI spec and identifies security gaps, validation gaps, and the level of data validation that's defined, so that customers can remediate issues with their OpenAPI specs and ensure that API Security Testing provides as much coverage as possible.
  5. [gRPC support](https://gitlab.com/gitlab-org/gitlab/-/issues/442507) will ensure all API formats can be analyzed by API Security Testing so customers have full coverage for identifying security issues in their APIs.


### Best in Class Landscape[](https://about.gitlab.com/direction/application_security_testing/dynamic-analysis/api-security/#best-in-class-landscape)
BIC (Best In Class) is an indicator of forecasted near-term market performance based on a combination of factors, including analyst views, market news, and feedback from the sales and product teams. It is critical that we understand where GitLab appears in the BIC landscape.
#### Key Capabilities[](https://about.gitlab.com/direction/application_security_testing/dynamic-analysis/api-security/#key-capabilities)
For this product area, these are the capabilities a best-in-class solution should provide:
  1. The ability to accurately and comprehensively detect security weaknesses outlined in the OWASP Top 10:2021.
  2. The ability to accurately and comprehensively detect security weaknesses outlined in the OWASP Top 10:2024.
  3. The ability to accurately and comprehensively detect security weaknesses outlined in the OWASP API Top 10:2023.
  4. Support for detecting weaknesses across REST, GraphQL, SOAP, and gRPC APIs.
  5. Support for detecting API business logic flaws.
  6. The ability to automatically generate OpenAPI specifications for APIs that are not documented and to automatically enable security testing on those specs.
  7. The ability to analyze pre-existing OpenAPI specifications for security flaws and to provide remediation recommendations.
  8. The ability to accurately and comprehensively provide an inventory of APIs.
  9. Support for shifting security results left into the IDE.
  10. Extensive analysis of other risk factors (business logic, sensitive data, PII, etc.).
  11. The ability to enforce policies preventing API security flaws from being merged into the default branch.
  12. Reporting and filtering to allow users to easily see the security posture of their APIs.
  13. The ability to provide mature security analysis of multiple API calls to replicate real-world attacks.
  14. The ability to enforce ABAC policies to reduce the liklihood of API authorization security flaws.


## Competitive Landscape[](https://about.gitlab.com/direction/application_security_testing/dynamic-analysis/api-security/#competitive-landscape)
  * [Noname Security](https://nonamesecurity.com/)
  * [Salt Security](https://salt.security/)
  * [TraceableAI](https://www.traceable.ai/)
  * [Cequence Security](https://www.cequence.ai/)
  * [42Crunch](https://42crunch.com/)
  * [APIsec](https://www.apisec.ai/)
  * [Akto](https://www.akto.io/)
  * [Firetail](https://www.firetail.io/)
  * [Wallarm](https://www.wallarm.com/)
  * [Synopsys](https://www.synopsys.com/software-integrity/security-testing/api-security-testing.html)
  * [Netsparker](https://www.netsparker.com/)
  * [StackHawk](https://www.stackhawk.com/)


We have an advantage of being able to provide testing results before the app is deployed into the production environment, by using Review Apps. This means that we can provide API security scan results for every single commit. The easy integration of API security scanning early in the software development life cycle is a unique position that GitLab has in the API Security market. We also have the advantage of being able to provide secure design and build guardrails within our platform as developers and security teams are outlining requirements and developing APIs. Integrating other tools at this stage of the SDLC is typically difficult, at best.
## Pricing and Packaging[](https://about.gitlab.com/direction/application_security_testing/dynamic-analysis/api-security/#pricing-and-packaging)
The GitLab API Security features are all packaged as part of the [GitLab Ultimate tier](https://about.gitlab.com/pricing/ultimate/). This aligns with our [pricing strategy](https://handbook.gitlab.com/handbook/company/pricing/#pricing-strategy) as these features are relevant for executives who are concerned about keeping their organization secured from security weaknesses (CWEs).
## Analyst Landscape[](https://about.gitlab.com/direction/application_security_testing/dynamic-analysis/api-security/#analyst-landscape)
API Security is not a standalone market evaluated by analysts, but is included in the analysis of DevSecOps, Application Security, and API Management markets.
  * [Gartner Application Security Testing Reviews](https://www.gartner.com/reviews/market/application-security-testing)


[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/application_security_testing/dynamic-analysis/api-security/index.html.md) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/application_security_testing/dynamic-analysis/api-security/index.html.md)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fapplication_security_testing%2Fdynamic-analysis%2Fapi-security%2F&_biz_t=1773331781447&_biz_i=%0ACategory%20Direction%20-%20API%20Security%0A%7C%0AGitLab%0A&_biz_n=52&rnd=71694&cdn_o=a&_biz_z=1773331782050)
suggested results