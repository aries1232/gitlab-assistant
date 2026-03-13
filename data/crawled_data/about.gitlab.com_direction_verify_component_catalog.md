#  Category Direction - Component Catalog 
  1. You are here:
  2. [GitLab Direction](https://about.gitlab.com/direction/)
  3. [Verify Stage Direction](https://about.gitlab.com/direction/verify/)
  4. Category Direction - Component Catalog


The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
  * [Component Catalog](https://about.gitlab.com/direction/verify/component_catalog/#component-catalog)
    * [Introduction and how you can help](https://about.gitlab.com/direction/verify/component_catalog/#introduction-and-how-you-can-help)
  * [Vision](https://about.gitlab.com/direction/verify/component_catalog/#vision)
    * [Strategy and Themes](https://about.gitlab.com/direction/verify/component_catalog/#strategy-and-themes)
    * [Roadmap](https://about.gitlab.com/direction/verify/component_catalog/#roadmap)
      * [What are we currently working on](https://about.gitlab.com/direction/verify/component_catalog/#what-are-we-currently-working-on)
      * [Analyst Discussion](https://about.gitlab.com/direction/verify/component_catalog/#analyst-discussion)
      * [What We Recently Completed](https://about.gitlab.com/direction/verify/component_catalog/#what-we-recently-completed)
    * [Best in Class Landscape](https://about.gitlab.com/direction/verify/component_catalog/#best-in-class-landscape)
      * [Key Capabilities](https://about.gitlab.com/direction/verify/component_catalog/#key-capabilities)
  * [Competitive Landscape](https://about.gitlab.com/direction/verify/component_catalog/#competitive-landscape)
  * [Glossary](https://about.gitlab.com/direction/verify/component_catalog/#glossary)


## Component Catalog[](https://about.gitlab.com/direction/verify/component_catalog/#component-catalog)
|   
---|---  
Stage | [verify](https://about.gitlab.com/direction/verify/)  
Maturity | [Minimal](https://about.gitlab.com/direction/#maturity)  
Content Last Reviewed | `2025-11-11`  
### Introduction and how you can help[](https://about.gitlab.com/direction/verify/component_catalog/#introduction-and-how-you-can-help)
Thanks for visiting this direction page on the Components catalog category at GitLab. This page belongs to the [Pipeline Authoring Group](https://handbook.gitlab.com/handbook/engineering/development/ops/verify/pipeline-authoring/) in the Verify Stage and is maintained by Dov Hershkovitch. You can submit your feature requests using [GitLab issue tracker](https://gitlab.com/gitlab-org/gitlab/-/issues/new).
## Vision[](https://about.gitlab.com/direction/verify/component_catalog/#vision)
The CI/CD Component Catalog will establish GitLab as the definitive enterprise CI/CD automation platform. By seamlessly integrating with GitLab Duo Agents, it transforms how organizations discover, govern, and deploy reusable components. What we're building isn't just a collection of features—it's a complete DevSecOps platform that takes components from open innovation to enterprise-grade security and control, positioning GitLab CI/CD as the industry standard for enterprise DevSecOps workflows.
### Strategy and Themes[](https://about.gitlab.com/direction/verify/component_catalog/#strategy-and-themes)
DevOps is all about speed, it delivers value faster by shortening the software development life cycle. Organizations that want to accelerate their DevOps adoption need to set up a working pipeline so other teams can use it to automate their workflow. During the development of a pipeline configuration, engineers frequently encounter the following challenges:
  1. _"Where can I find it?"_ - Whenever engineers embark on setting up a new pipeline, they often search for existing pipelines in their organization or externally. This is because someone, at some point, has likely attempted to configure a similar pipeline.
  2. _"How do I use it?"_ - After engineers locate a suitable pipeline to work with, they require clear instructions on effectively using it. This guidance is crucial for understanding the pipeline's functionalities and ensuring its proper usage.
  3. _"Does it always work as expected?"_ - Engineers often question whether the pipeline is consistently reliable and delivers the expected results. They also evaluate its reusability and whether it can be shared effectively with other teams within the organization. These aspects are vital for determining the pipeline's suitability for wider adoption and collaboration.


While it is possible to solve each problem separately, GitLab believes that we need to solve those problems holistically by building a framework that contains tools that add functionality and improve your CI/CD workflow. We aspire to provide the best-in-class experience for building and maintaining CI/CD pipelines.
Our strategy is to provide an opinionated framework that:
  1. Is the SSoT for users to browse and search for the desired pipeline components.
  2. Contains shareable and reusable package components that could be attached to any CI/CD configuration.
  3. Has an easy way to document the usage of each component.
  4. Fosters a collaborative methodology by allowing users to contribute to the catalog by developing and publishing their own components.


We should adopt a bottom-up approach to construct this solution, starting with the smallest building blocks and gradually progressing upwards. By starting from the foundational elements and gradually building on them, we can create a robust and cohesive solution.
### Roadmap[](https://about.gitlab.com/direction/verify/component_catalog/#roadmap)
We aim to enhance our CI/CD catalog by introducing features tailored for enterprise customers, thereby delivering additional value to their operations.
  * [Support .com components in Self Manage instance](https://gitlab.com/groups/gitlab-org/-/epics/15224) - In our effort to support all customer segments we would like to help our Self manage customers and customers in an air-gapped environment to easily consume components that exist today in our [.com catalog](https://gitlab.com/explore/catalog). This approach aligns with our goal, where every customer, regardless of their setup, can readily explore and implement additional functionalities from our platform.
  * [Developer security workflows](https://gitlab.com/groups/gitlab-org/-/epics/15112) - When publishing or utilizing CI components, teams require a secure and reliable method to verify that the components are free from vulnerabilities and tampering. This safeguards CI/CD pipelines from potential security risks while preserving trust in both internal and third-party components.
  * [Component analytics dashboard](https://gitlab.com/groups/gitlab-org/-/epics/14027) - We aim to provide visibility into component usage across project pipelines across organizations by addressing the current lack of traceability. This enhancement will empower users with seamless control over component management, enabling them to quickly identify which projects are using outdated versions, notify relevant teams, ensure required components are included, and support full lifecycle management—including deprecation. By providing clear insights into component usage, we promote precise version control and better project alignment, allowing users to take timely corrective actions and maintain consistency across pipelines.
  * [Block users from using unofficial components](https://gitlab.com/gitlab-org/gitlab/-/issues/441102) - We want to allow administrators to restrict component domain usage to specific users or groups, ensuring tighter governance and alignment with organizational policies. This capability reflects our commitment to delivering a refined catalog experience that meets enterprise needs while fostering a secure and well-regulated ecosystem
  * [Mature the CI/CD catalog to a competitive maturity level](https://gitlab.com/groups/gitlab-org/-/epics/11538) - We aim to advance the CI/CD catalog to a competitive level of maturity by introducing capabilities that enhance both functionality and user experience. This includes adding advanced search and filtering options, improving page navigation, and delivering targeted UI enhancements. These improvements will provide robust features, seamless usability, and enterprise-grade governance, ensuring the catalog effectively supports the diverse needs of users, aligns with organizational goals, and strengthens GitLab’s position as a leader in CI/CD pipeline management.


#### What are we currently working on[](https://about.gitlab.com/direction/verify/component_catalog/#what-are-we-currently-working-on)
[Read inputs from a file](https://gitlab.com/gitlab-org/gitlab/-/issues/415636) - Inputs are the recommended way to pass any parameter to a component. It has multiple benefits over the usage of variables, and since its launch, it has been widely adopted by our users and customers. This is why we decided to continue our investment in inputs and increase its scope and flexibility.
#### Analyst Discussion[](https://about.gitlab.com/direction/verify/component_catalog/#analyst-discussion)
  * [Notes](https://docs.google.com/document/d/1ZOEl7ycibtxN6dDGfsQlfoc-09p7GXEqDUgCCrocUFQ/edit) from Gartner discussion (internal)
  * Related articles 
    * [DevEx, a New Metrics Framework from the Authors of SPACE](https://www.infoq.com/articles/devex-metrics-framework/)
    * [DevEx: What Actually Drives Productivity](https://queue.acm.org/detail.cfm?id=3595878)


#### What We Recently Completed[](https://about.gitlab.com/direction/verify/component_catalog/#what-we-recently-completed)
**[Restrict who can publish components to the Catalog](https://gitlab.com/groups/gitlab-org/-/epics/14060)** - PREMIUM TIER ✅ **SHIPPED FY25**
  * **Why This Matters:** GitLab admins can now restrict specific individuals or groups from publishing components to a catalog, enabling organizations to enforce tighter control over catalog contributions and ensure only authorized users or teams can publish components.
  * **Customer Impact:** Addresses #1 enterprise requirement from multiple customer conversations. This was a blocking issue preventing enterprise adoption.


### Best in Class Landscape[](https://about.gitlab.com/direction/verify/component_catalog/#best-in-class-landscape)
BIC (Best In Class) is an indicator of forecasted near-term market performance based on a combination of factors, including analyst views, market news, and feedback from the sales and product teams. It is critical that we understand where GitLab appears in the BIC landscape.
#### Key Capabilities[](https://about.gitlab.com/direction/verify/component_catalog/#key-capabilities)
  1. [Centralized Component Catalog:](https://gitlab.com/groups/gitlab-org/-/epics/12153) Create a centralized component catalog that serves as a single source of truth for users to browse and search for pipeline components. The catalog should be easily accessible and provide comprehensive information about each component, including its purpose, usage, and documentation.
  2. Shareable and Reusable Components: Enable users to develop and publish their pipeline components to the catalog. Components should be designed to be shareable and reusable, allowing developers to easily attach them to their CI/CD configurations. This promotes collaboration and reduces duplication of effort within the organization.
  3. [Versioning: Implement versioning for components](https://gitlab.com/gitlab-org/gitlab/-/issues/427286) to ensure users can pin their pipelines to a specific component revision. This helps in maintaining stability and allows for controlled updates.
  4. [Component Abstraction and Encapsulation:](https://gitlab.com/groups/gitlab-org/-/epics/12464) Encourage the development of components that abstract away complex pipeline configuration units. Components should encapsulate implementation details and provide a clear interface, enabling users to use them without needing to know the underlying details.
  5. Documentation: Provide a mechanism for users to document the usage of each component. This should include clear guidelines, examples, and best practices to help users understand how to use the components effectively.
  6. Collaborative Contribution: Foster a collaborative community where developers can contribute to the component catalog by developing and publishing their own components. Implement mechanisms for peer review, feedback, and contribution management to ensure the quality and reliability of the catalog assets.
  7. Accessibility: Design the platform to be inclusive and accessible to all community members. Provide intuitive interfaces, clear navigation, and comprehensive search capabilities, making it easy for users to find the components they need.
  8. [Continuous Improvement and Learning:](https://gitlab.com/gitlab-org/gitlab/-/issues/407556) Establish a culture of continuous learning and improvement within the community. Encourage feedback from users, collect analytics on component usage, and iterate on the catalog based on user needs and preferences. Regularly update and enhance the catalog with new components, improved documentation, and additional features based on community contributions.
  9. [Securing users workflow:](https://gitlab.com/groups/gitlab-org/-/epics/12713) - we are committed to providing our users with means to ensure the security and reliability of their workflows and underlying capabilities


## Competitive Landscape[](https://about.gitlab.com/direction/verify/component_catalog/#competitive-landscape)
Notable competitors in this space are:
  * GitHub actions with their [actions marketplace](https://github.com/marketplace?category=&query=&type=actions&verification=).
  * [Circle CI orbs](https://circleci.com/developer/orbs).
  * CodeFresh also provide their users with a [CI step library](https://codefresh.io/steps/).


Watch this walkthrough video of the different contribution frameworks available by these competitors:
## Glossary[](https://about.gitlab.com/direction/verify/component_catalog/#glossary)
This section defines the terminology used throughout this project. With these terms we are only identifying abstract concepts, and they are subject to changes as we refine the design by discovering new insights:
  * **Component** : A reusable single pipeline configuration unit. Use them to compose an entire pipeline configuration or a small part of a larger pipeline..
  * **Component Project** : A component project is a GitLab project with a repository that hosts one or more components..
  * **Catalog** : Collaborative platform that presents the collection of CI/CD projects and components.
  * **Version** : The release name of a tag in the project, which allows components to be pinned to a specific revision, components of the same project and versioned together.


[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/verify/component_catalog/index.html.md) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/verify/component_catalog/index.html.md)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fverify%2Fcomponent_catalog%2F&_biz_t=1773332056678&_biz_i=%0ACategory%20Direction%20-%20Component%20Catalog%0A%7C%0AGitLab%0A&_biz_n=110&rnd=147983&cdn_o=a&_biz_z=1773332056830)
suggested results