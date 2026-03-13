#  Category Direction - Artifact Security 
  1. You are here:
  2. [GitLab Direction](https://about.gitlab.com/direction/)
  3. [Product Stage Direction - Software Supply Chain Security](https://about.gitlab.com/direction/software_supply_chain_security/)
  4. [Group Direction - Pipeline Security](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/)
  5. Category Direction - Artifact Security


The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
  * [Artifact Security](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#artifact-security)
    * [Mission](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#mission)
    * [Vision](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#vision)
    * [How](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#how)
    * [Comprehensive Artifact Security](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#comprehensive-artifact-security)
      * [Signing Capabilities](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#signing-capabilities)
      * [End-to-End SDLC Attestations](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#end-to-end-sdlc-attestations)
    * [Generate Provenance](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#generate-provenance)
    * [Generate and Sign Attestations](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#generate-and-sign-attestations)
    * [Publish Attestations](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#publish-attestations)
    * [Verify Artifacts](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#verify-artifacts)
    * [Compliance Framework](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#compliance-framework)
  * [Customers](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#customers)
    * [Customer Zero](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#customer-zero)
    * [Target Segments](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#target-segments)
  * [Roadmap](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#roadmap)
    * [Current](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#current)
    * [Next](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#next)
    * [Future](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#future)
      * [Additional Attestations](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#additional-attestations)
      * [Sigstore Infrastructure & Key Management](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#sigstore-infrastructure--key-management)
      * [Runner Hardening](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#runner-hardening)
      * [Compliance Frameworks](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#compliance-frameworks)
    * [How you can help](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#how-you-can-help)


## Artifact Security[](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#artifact-security)
|   
---|---  
Stage | [Software Supply Chain Security](https://about.gitlab.com/direction/software_supply_chain_security/)  
Maturity | [Minimal](https://about.gitlab.com/direction/#maturity)  
Content Last Reviewed | `2025-09-23`  
### Mission[](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#mission)
To secure software supply chains by creating secure, tamper-proof, and verifiable software artifacts and attestations.
### Vision[](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#vision)
The vision for Artifact Security is to make it easy for software teams to implement best practices to secure their release, packages, and containers, and provide simple mechanisms for their consumers to verify the authenticity. By making it low-friction, and easy to implement, more software teams will be able to secure their artifacts with little effort, increasing adoption, and improving software supply chain security overall.
### How[](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#how)
GitLab Secure Artifacts are designed to conform to the highest level (Build L3) of the [Supply-chain Levels for Software Artifacts](https://slsa.dev/spec/v1.0/), or SLSA ("salsa") specification. We intend to implement this specification using a suite of open source tools called [Sigstore](https://www.sigstore.dev/), which will be integrated into the GitLab Trusted Control Plane to create an end-to-end solution for securing software artifacts.
Architecture and workflow diagrams can be found in the [Architecture Design Document](https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/slsa_level_3/#design-details).
### Comprehensive Artifact Security[](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#comprehensive-artifact-security)
#### Signing Capabilities[](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#signing-capabilities)
  * Binary and package signing with keyless authentication
  * Container image signing with registry-native storage
  * Integration with GitLab's OIDC identity provider for seamless authentication


#### End-to-End SDLC Attestations[](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#end-to-end-sdlc-attestations)
GitLab will aggregate security metadata from across the entire software development lifecycle into comprehensive, verifiable attestations:
  * **Code stage:** Developer identity, commit provenance, code review data
  * **Build stage:** Dependencies, SBOM, test results, build environment details
  * **Security stage:** SAST, SCA, container scans, IaC analysis, DAST results
  * **Infrastructure stage:** GitLab Runner provenance, pipeline execution logs, environment hardening


This aggregated approach provides complete artifact security context in a single, verifiable attestation while maintaining simplicity for consumers.
### Generate Provenance[](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#generate-provenance)
Tamper-proof provenance will be automatically generated in the GitLab Trusted Control Plane, collecting security metadata from all pipeline stages.
### Generate and Sign Attestations[](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#generate-and-sign-attestations)
Comprehensive attestations will be generated and signed using Sigstore's keyless signing approach, leveraging GitLab's identity system for seamless integration.
### Publish Attestations[](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#publish-attestations)
Attestations will be published via the GitLab Attestations API and stored alongside artifacts in registries, with support for both public and self-managed Sigstore infrastructure.
### Verify Artifacts[](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#verify-artifacts)
Verification capabilities will include command-line tools (cosign, glab), Kubernetes admission controllers for automated policy enforcement, and developer workflow integrations.
### Compliance Framework[](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#compliance-framework)
A compliance framework will be developed to help teams maintain SLSA requirements and meet industry standards (SOC 2, NIST SSDF, FedRAMP) with automated monitoring and reporting.
## Customers[](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#customers)
Customers for Secure Artifacts range from small, open-source projects to large enterprise customers with the highest security and compliance requirements.
### Customer Zero[](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#customer-zero)
We have identified several internal customers within GitLab including the Delivery and Runner teams who will help validate and refine the solution.
### Target Segments[](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#target-segments)
  * **Open source projects** seeking simple, automated security
  * **Enterprise customers** requiring comprehensive compliance and audit capabilities
  * **Regulated industries** needing specific compliance attestations (financial, healthcare, government)


## Roadmap[](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#roadmap)
### Current[](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#current)
Job Artifacts for Public Projects
  * <https://gitlab.com/groups/gitlab-org/-/epics/15858>


### Next[](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#next)
Container Images for Public Projects
### Future[](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#future)
#### Additional Attestations[](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#additional-attestations)
Capture various artifacts from the build process: build logs, security scanning rules, security scan results, SBOM, runner SBOM
#### Sigstore Infrastructure & Key Management[](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#sigstore-infrastructure--key-management)
Support for self-hosted Sigstore, X.509 Keys for signing and attestation
#### Runner Hardening[](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#runner-hardening)
Review, implement and attest to controls of runner mapping to SLSA controls and work toward providing hermetic build capabilities and publish SBOM for validation Anomaly detection capabilities
#### Compliance Frameworks[](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#compliance-frameworks)
Provide compliance view for groups and projects to highlight adoption and gaps of SLSA specification controls
### How you can help[](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/artifact_security/#how-you-can-help)
Thanks for visiting this category direction page on Artifact Security in GitLab. This page belongs to the [Pipeline Security](https://handbook.gitlab.com/handbook/product/categories/#pipeline-security-group) group of the Software Supply Chain Security (SSCS) stage and is maintained by Jocelyn Eillis (E-Mail).
Please comment and contribute in the linked [issues](https://gitlab.com/gitlab-org/gitlab/-/issues/?sort=updated_desc&state=opened&label_name%5B%5D=group%3A%3Apipeline%20security&label_name%5B%5D=Category%3AArtifact%20Security&first_page_size=100) and [epics](https://gitlab.com/groups/gitlab-org/-/epics?sort=updated_desc&state=opened&label_name%5B%5D=Category%3AArtifact%20Security&first_page_size=20) on this page. Sharing your feedback directly on GitLab.com is the best way to contribute to our strategy and vision.
[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/software_supply_chain_security/pipeline_security/artifact_security/index.html.md.erb) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/software_supply_chain_security/pipeline_security/artifact_security/index.html.md.erb)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fsoftware_supply_chain_security%2Fpipeline_security%2Fartifact_security%2F&_biz_t=1773332114107&_biz_i=%0ACategory%20Direction%20-%20Artifact%20Security%0A%7C%0AGitLab%0A&_biz_n=123&rnd=118234&cdn_o=a&_biz_z=1773332114259)
suggested results