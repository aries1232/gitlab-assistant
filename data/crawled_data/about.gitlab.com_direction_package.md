#  Stage Direction - Package 
  1. You are here:
  2. [GitLab Direction](https://about.gitlab.com/direction/)
  3. Stage Direction - Package


The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
  * [Package - Enterprise artifact management in GitLab](https://about.gitlab.com/direction/package/#package---enterprise-artifact-management-in-gitlab)
    * [Our mission and goal](https://about.gitlab.com/direction/package/#our-mission-and-goal)
    * [What is Package?](https://about.gitlab.com/direction/package/#what-is-package)
    * [Our differentiators](https://about.gitlab.com/direction/package/#our-differentiators)
    * [What's next and why](https://about.gitlab.com/direction/package/#whats-next-and-why)
      * [2026 priorities](https://about.gitlab.com/direction/package/#2026-priorities)
        * [Virtual Registries](https://about.gitlab.com/direction/package/#virtual-registries)
        * [Migration & Management](https://about.gitlab.com/direction/package/#migration--management)
    * [What we aren't working on and why](https://about.gitlab.com/direction/package/#what-we-arent-working-on-and-why)
    * [Categories](https://about.gitlab.com/direction/package/#categories)
      * [Container Registry](https://about.gitlab.com/direction/package/#container-registry)
      * [Package registry](https://about.gitlab.com/direction/package/#package-registry)
      * [Virtual registries](https://about.gitlab.com/direction/package/#virtual-registries-1)
    * [Customer needs](https://about.gitlab.com/direction/package/#customer-needs)
      * [Non-enterprise Organizations](https://about.gitlab.com/direction/package/#non-enterprise-organizations)
      * [Enterprise organizations](https://about.gitlab.com/direction/package/#enterprise-organizations)
    * [GitLab Package - Market Analysis](https://about.gitlab.com/direction/package/#gitlab-package---market-analysis)
      * [Competitive landscape](https://about.gitlab.com/direction/package/#competitive-landscape)
      * [Key market trends](https://about.gitlab.com/direction/package/#key-market-trends)
      * [Product comparison](https://about.gitlab.com/direction/package/#product-comparison)
      * [GitLab's unique value proposition](https://about.gitlab.com/direction/package/#gitlabs-unique-value-proposition)
    * [Target customer segments](https://about.gitlab.com/direction/package/#target-customer-segments)
      * [Small to medium organizations](https://about.gitlab.com/direction/package/#small-to-medium-organizations)
      * [Enterprise organizations](https://about.gitlab.com/direction/package/#enterprise-organizations-1)
    * [Migration Path for JFrog and Nexus Users](https://about.gitlab.com/direction/package/#migration-path-for-jfrog-and-nexus-users)
      * [Automated Migration Capabilities](https://about.gitlab.com/direction/package/#automated-migration-capabilities)
      * [Migration Timeline](https://about.gitlab.com/direction/package/#migration-timeline)
    * [Customer success stories](https://about.gitlab.com/direction/package/#customer-success-stories)


## Package - Enterprise artifact management in GitLab[](https://about.gitlab.com/direction/package/#package---enterprise-artifact-management-in-gitlab)
![GitLab Artifact Management Diagram](https://about.gitlab.com/direction/package/Package_diagram_June_2025.png)
### Our mission and goal[](https://about.gitlab.com/direction/package/#our-mission-and-goal)
Our mission is to eliminate artifact management complexity by delivering enterprise-grade capabilities that are seamlessly integrated with your entire DevSecOps workflow.
Our goal is to become our customers' single source of truth for artifact management by 2027, replacing fragmented toolchains with a unified platform that reduces costs, improves security, and accelerates development velocity.
### What is Package?[](https://about.gitlab.com/direction/package/#what-is-package)
The Package stage is responsible for delivering a comprehensive artifact management solution that meets the needs of both small teams and enterprise organizations.
Artifact management involves storing, versioning, and tracking binary files, libraries, and dependencies used in software development. It's critical for ensuring consistency, reproducibility, and efficient collaboration in development projects. Artifact management systems help manage the software artifacts' lifecycle, from creation to deployment, facilitating easy access, sharing among team members, and integration with build and deployment tools.
### Our differentiators[](https://about.gitlab.com/direction/package/#our-differentiators)
While competitors like JFrog Artifactory claim to offer a "system of record," GitLab Package goes beyond this by:
  * **Deep Integration with Development Workflows** : Unlike standalone solutions, GitLab Package is natively integrated with your source code, CI/CD pipelines, and security scanning tools, creating a seamless experience.
  * **Enhanced Security and Compliance** : GitLab's built-in security features work directly with your artifacts, providing vulnerability scanning, dependency analysis, and compliance checking without requiring separate products or integrations.
  * **Reduced Context Switching** : Teams can manage code, builds, tests, and artifacts all within a single platform, eliminating the need to switch between multiple tools.
  * **Streamlined Troubleshooting** : Having artifacts alongside your source code makes troubleshooting issues significantly easier, with clear build provenance and traceability.
  * **Cost and Maintenance Efficiency** : Consolidate tools and reduce both licensing costs and maintenance overhead.
  * **Native Build Promotion and Complete Provenance** : GitLab uses a git-native approach to build promotion through semantic versioning with commit identifiers (e.g., `myapp-1.2.3-abc123f`) and git tags for releases. This provides complete build provenance by linking artifacts directly to their source code, CI/CD pipelines, and deployment history within a single platform - enabling rapid troubleshooting and ensuring supply chain security compliance without separate tooling.


### What's next and why[](https://about.gitlab.com/direction/package/#whats-next-and-why)
#### 2026 priorities[](https://about.gitlab.com/direction/package/#2026-priorities)
##### Virtual Registries[](https://about.gitlab.com/direction/package/#virtual-registries)
  * **[Maven Virtual Registry (GA)](https://gitlab.com/groups/gitlab-org/-/epics/15089)** - Q2 2026  
Production-ready virtual registry for Maven packages with Geo support (AWS, GCP, Azure) and allow/deny filtering.
  * **[Container Virtual Registry (GA)](https://gitlab.com/groups/gitlab-org/-/epics/18773)** - Q2 2026  
Production-ready virtual registry for container images with multi-upstream support including AWS ECR, Google Artifact Registry, and Azure Container Registry.
  * **[npm Virtual Registry](https://gitlab.com/groups/gitlab-org/-/epics/3608)** - Beta Q2 2026, GA Q3 2026  
Virtual registry for npm packages enabling JavaScript ecosystem consolidation with intelligent caching and security controls.
  * **[PyPI Virtual Registry](https://gitlab.com/groups/gitlab-org/-/epics/3612)** - Beta Q3 2026, GA Q4 2026  
Virtual registry for Python packages with upstream proxying and caching for improved build reliability.
  * **[NuGet Virtual Registry](https://gitlab.com/groups/gitlab-org/-/epics/3611)** - Beta Q3 2026, GA Q4 2026  
Virtual registry for .NET packages enabling enterprise consolidation of NuGet dependencies.


##### Migration & Management[](https://about.gitlab.com/direction/package/#migration--management)
  * **JFrog/Nexus Migration Tools** - Q3 2026 Automated bulk import from JFrog Artifactory and Sonatype Nexus with metadata preservation, dry-run validation, and progress tracking.
  * **[Organization-Level Dashboard](https://gitlab.com/groups/gitlab-org/-/epics/8064)** - Q4 2026  
Unified visibility into artifact usage, storage costs, and security metrics across your entire organization.


### What we aren't working on and why[](https://about.gitlab.com/direction/package/#what-we-arent-working-on-and-why)
  * **New Package Manager Formats** : We're focusing on improving our existing formats (OCI-artifacts, npm, Maven, NuGet, PyPI, Terraform, and generic packages) rather than expanding to additional formats in the near term. This approach ensures we maintain our high standards for performance and reliability while delivering the enterprise features our customers need most.


### Categories[](https://about.gitlab.com/direction/package/#categories)
#### Container Registry[](https://about.gitlab.com/direction/package/#container-registry)
The GitLab container registry is a secure and private registry for OCI artifacts, such as Docker container images. Use GitLab CI/CD to create and publish branch/release specific images, manage them via the GitLab API, and discover them through the intuitive user interface.
#### Package registry[](https://about.gitlab.com/direction/package/#package-registry)
Our package registry supports multiple formats including npm, Maven, NuGet, PyPI, Terraform, and generic packages. We provide project and group-level private package registries and are expanding capabilities to include virtual registries.
#### Virtual registries[](https://about.gitlab.com/direction/package/#virtual-registries-1)
Virtual registries provide a mechanism for storing and accessing external packages, enabling more reliable builds. They allow you to proxy and cache dependencies from external sources, reducing build times and improving supply chain reliability.
The virtual registry for container images currently allows you to proxy and cache images from DockerHub. In upcoming releases, we'll expand this feature to support multiple endpoints and additional package formats.
### Customer needs[](https://about.gitlab.com/direction/package/#customer-needs)
As the PM for the Package stage, I hear regularly from customers and prospects that would like to migrate off of JFrog's Artifactory. Their reasons for wanting to consolidate on GitLab are:
  1. Convenience (authentication, management, improved UX)
  2. Cost
  3. Better support and access to product teams


The needs of these customers can be predictably segmented by the size of their organization:
#### Non-enterprise Organizations[](https://about.gitlab.com/direction/package/#non-enterprise-organizations)
Typically they'd like to know if we support format `x` and if not when we will support it. If we support their requested format, these customers are often able to consolidate quickly.
#### Enterprise organizations[](https://about.gitlab.com/direction/package/#enterprise-organizations)
Enterprise organizations frequently express interest in consolidating on GitLab but are waiting for our Package product to mature. The key features they're waiting for include:
  * Virtual registries for managing upstream repositories
  * Dependency firewall to prevent supply chain attacks
  * Improved discoverability and visibility into dependency usage


We're addressing these needs directly in our 2025-2027 roadmap.
### GitLab Package - Market Analysis[](https://about.gitlab.com/direction/package/#gitlab-package---market-analysis)
#### Competitive landscape[](https://about.gitlab.com/direction/package/#competitive-landscape)
GitLab Package operates in a market dominated by established players like JFrog Artifactory and Sonatype Nexus, with cloud providers (AWS, Azure, Google) and other DevOps platforms (GitHub) offering varying levels of functionality.
#### Key market trends[](https://about.gitlab.com/direction/package/#key-market-trends)
  * **Consolidation of DevOps Toolchains** : Organizations are seeking to reduce tool sprawl by consolidating functionality into fewer platforms
  * **Supply Chain Security** : Increasing focus on securing the software supply chain from vulnerabilities and attacks
  * **Integration with CI/CD** : Demand for artifact management that integrates seamlessly with build and deployment processes
  * **Enterprise Scalability** : Need for solutions that can handle the volume and complexity of enterprise-level package management


#### Product comparison[](https://about.gitlab.com/direction/package/#product-comparison)
> **Note:** This comparison focuses on dedicated DevOps platforms and artifact management solutions. Cloud-native registries (AWS ECR/CodeArtifact, Azure ACR, Google Artifact Registry) serve different use cases and are typically chosen as part of broader cloud platform strategies rather than as standalone artifact management solutions.
Feature | GitLab | JFrog Artifactory | Sonatype Nexus | GitHub Packages  
---|---|---|---|---  
**Locally-Hosted Registries** |  |  |  |   
Container Registry | Available | Available | Available | Available  
Maven | Available | Available | Available | Available  
npm | Available | Available | Available | Available  
NuGet | Available | Available | Available | Available  
PyPI | Available | Available | Available | Not Available  
Generic Packages | Available | Available | Available | Not Available  
Terraform Modules | Available | Available | Available | Not Available  
Conan | Available | Available | Available | Not Available  
Helm Charts | Available | Available | Available | Not Available  
Go | Not Available | Available | Available | Not Available  
RPM | Not Available | Available | Available | Not Available  
Debian | Not Available | Available | Available | Not Available  
**Virtual Registries** |  |  |  |   
Container Virtual Registry | Beta (GA Q2 2026) | Available | Available | Not Available  
Maven Virtual Registry | Beta (GA Q2 2026) | Available | Available | Not Available  
npm Virtual Registry | Beta Q2 2026, GA Q3 2026 | Available | Available | Not Available  
PyPI Virtual Registry | Beta Q3 2026, GA Q4 2026 | Available | Available | Not Available  
NuGet Virtual Registry | Beta Q3 2026, GA Q4 2026 | Available | Available | Not Available  
Go Virtual Registry | Roadmap 2027 | Available | Available | Not Available  
Generic Virtual Registry | Roadmap 2027 | Available | Available | Not Available  
**Platform Features** |  |  |  |   
CI/CD Integration | Native | Plugin Required | Plugin Required | Native  
Security Scanning | Built-in | X-Ray | Built-in | Dependabot  
Access Control | Granular | Granular | Granular | Granular  
Dependency Firewall | Coming soon | Available | Available | Not Available  
User Interface | Modern & Intuitive | Complex | Basic | Modern  
#### GitLab's unique value proposition[](https://about.gitlab.com/direction/package/#gitlabs-unique-value-proposition)
  * Single platform for the entire DevSecOps lifecycle 
    * Unlike standalone solutions, GitLab Package is part of an integrated platform that includes source code management, CI/CD, security scanning, and deployment. This integration reduces context switching, simplifies workflows, and provides a unified experience across the software development lifecycle.
  * Native integration with GitLab CI/CD 
    * The tight integration with GitLab CI/CD means that packages can be built, tested, and published as part of the same pipeline without additional configuration or plugins. This simplifies setup and reduces maintenance overhead.
  * Built-in security scanning and compliance 
    * GitLab's integrated security features work directly with your artifacts, providing vulnerability scanning, dependency analysis, and compliance checking without requiring separate products or integrations.
  * Improved troubleshooting and traceability 
    * Having artifacts alongside your source code makes troubleshooting issues significantly easier, with clear build provenance and traceability from code to deployment.
  * Cost and maintenance efficiency 
    * By consolidating tools, organizations can reduce both licensing costs and the overhead of maintaining multiple systems.


### Target customer segments[](https://about.gitlab.com/direction/package/#target-customer-segments)
#### Small to medium organizations[](https://about.gitlab.com/direction/package/#small-to-medium-organizations)
  * Seeking to simplify their toolchain
  * Looking for cost-effective solutions
  * Value the convenience of integrated platforms


#### Enterprise organizations[](https://about.gitlab.com/direction/package/#enterprise-organizations-1)
  * Require advanced features like virtual registries
  * Need strong supply chain security
  * Value centralized management and governance
  * Looking to standardize artifact management across teams


### Migration Path for JFrog and Nexus Users[](https://about.gitlab.com/direction/package/#migration-path-for-jfrog-and-nexus-users)
For organizations looking to migrate from JFrog Artifactory or Sonatype Nexus, we're building automated tooling (Q3 2026) that reduces migration effort by 90%:
#### Automated Migration Capabilities[](https://about.gitlab.com/direction/package/#automated-migration-capabilities)
  * **Automated Assessment** : Scan your existing JFrog/Nexus instance to inventory artifacts, repositories, and configurations. Generate a compatibility report with GitLab feature mapping.
  * **Dry-Run Validation** : Preview migration without impacting production systems. Validate artifact formats and metadata preservation before committing.
  * **Bulk Import** : Batch import artifacts with progress tracking and error handling. Preserve all metadata, tags, and properties.
  * **Real-Time Dashboard** : Monitor migration progress with completion percentages, ETAs, and issue tracking.


#### Migration Timeline[](https://about.gitlab.com/direction/package/#migration-timeline)
Phase | Duration | Description  
---|---|---  
Assessment | 1 week | Automated inventory and compatibility analysis  
Planning | 1 week | Architecture design and configuration mapping  
Migration | 4-6 weeks | Automated import with validation  
Adoption | 2-3 weeks | Developer onboarding and CI/CD configuration updates  
Our professional services team can assist with migration planning and implementation to ensure a smooth transition.
### Customer success stories[](https://about.gitlab.com/direction/package/#customer-success-stories)
> "By consolidating our DevOps toolchain on GitLab, including artifact management, we reduced our annual licensing costs by 35% and improved developer productivity by eliminating context switching." - Enterprise Customer
> "The integration between GitLab's package registry and CI/CD pipelines simplified our deployment process and reduced the time spent troubleshooting dependency issues." - Mid-size SaaS Company
[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/package/template.html.md.erb) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/package/template.html.md.erb)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fpackage%2F&_biz_t=1773331571510&_biz_i=%0AStage%20Direction%20-%20Package%0A%7C%0AGitLab%0A&_biz_n=7&rnd=215698&cdn_o=a&_biz_z=1773331571638)
suggested results