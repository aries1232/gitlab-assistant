#  Group Direction - AI Framework 
  1. You are here:
  2. [GitLab Direction](https://about.gitlab.com/direction/)
  3. [Stage Direction - AI-powered](https://about.gitlab.com/direction/ai-powered/)
  4. Group Direction - AI Framework


The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
## On this page
  * [Overview](https://about.gitlab.com/direction/ai-powered/ai_framework/#overview)
    * [Goals](https://about.gitlab.com/direction/ai-powered/ai_framework/#goals)
  * [Vision](https://about.gitlab.com/direction/ai-powered/ai_framework/#vision)
  * [Themes](https://about.gitlab.com/direction/ai-powered/ai_framework/#themes)
    * [AI Gateway as a Tool to Increase Privacy and Performance](https://about.gitlab.com/direction/ai-powered/ai_framework/#ai-gateway-as-a-tool-to-increase-privacy-and-performance)
    * [Abstraction Layer for Enhanced AI Integration](https://about.gitlab.com/direction/ai-powered/ai_framework/#abstraction-layer-for-enhanced-ai-integration)
    * [Consolidated Evaluation Framework to Evaluate GenAI Models](https://about.gitlab.com/direction/ai-powered/ai_framework/#consolidated-evaluation-framework-to-evaluate-genai-models)
  * [FY26 Strategic Goals & Objectives](https://about.gitlab.com/direction/ai-powered/ai_framework/#fy26-strategic-goals--objectives)
    * [Quarterly Roadmap Overview](https://about.gitlab.com/direction/ai-powered/ai_framework/#quarterly-roadmap-overview)
      * [Q1: Establishing the Foundation](https://about.gitlab.com/direction/ai-powered/ai_framework/#q1-establishing-the-foundation)
      * [Q2: Building on Momentum](https://about.gitlab.com/direction/ai-powered/ai_framework/#q2-building-on-momentum)
      * [Q3: Scaling and Refining Infrastructure](https://about.gitlab.com/direction/ai-powered/ai_framework/#q3-scaling-and-refining-infrastructure)
      * [Q4: Finalization and Future-Proofing](https://about.gitlab.com/direction/ai-powered/ai_framework/#q4-finalization-and-future-proofing)
  * [Categories](https://about.gitlab.com/direction/ai-powered/ai_framework/#categories)
  * [Team HQ](https://about.gitlab.com/direction/ai-powered/ai_framework/#team-hq)


## Overview[](https://about.gitlab.com/direction/ai-powered/ai_framework/#overview)
The AI Framework group accelerates the adoption and innovation of advanced AI/ML technologies while ensuring quality. We develop tools for engineers and product teams to enhance their product offerings, enabling them to focus on customer needs and create solutions best suited to their use cases.
AI is evolving rapidly, and the AI Framework group leads the way with innovative approaches to improve efficiencies across the entire DevSecOps cycle. Our [Abstraction Layer](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_abstraction_layer) and [AI Gateway](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_gw) provide plug-and-play infrastructure, bringing AI as a service to the GitLab platform.
### Goals[](https://about.gitlab.com/direction/ai-powered/ai_framework/#goals)
We aim to:
  1. Increase the velocity of AI-powered feature development
  2. Enhance the quality of AI-powered features in the platform
  3. Drive the adoption of GitLab as a comprehensive platform


## Vision[](https://about.gitlab.com/direction/ai-powered/ai_framework/#vision)
We build reliable, scalable AI infrastructure that provides GitLab's AI feature teams with comprehensive, unified tools for testing, deployment, and monitoring.
By consolidating evaluation tools, optimizing datasets, and strengthening infrastructure capabilities, the team delivers reliable and scalable AI models while maintaining high standards of reliability and performance across all GitLab's AI features.
The AI Framework team lays the foundation for GitLab's AI initiatives by developing and maintaining robust, scalable infrastructure. This infrastructure supports unified testing, deployment, and monitoring, ensuring AI models are integrated, validated, and optimized efficiently. By consolidating tools and processes, the AI Framework team accelerates AI-powered feature development and ensures GitLab's infrastructure scales with increasing AI demands.
## Themes[](https://about.gitlab.com/direction/ai-powered/ai_framework/#themes)
### AI Gateway as a Tool to Increase Privacy and Performance[](https://about.gitlab.com/direction/ai-powered/ai_framework/#ai-gateway-as-a-tool-to-increase-privacy-and-performance)
The AI Gateway is a standalone service that provides access to AI features for all GitLab users, whether using self-managed, dedicated, or GitLab.com instances.
**Key Features:**
  * **Global Reach:** Handles traffic from a globally reachable route (cloud.gitlab.com/ai/*), directing it to AI providers and models
  * **Future Flexibility:** Enables potential regional or customer-specific gateways as needed
  * **Scalability:** Scales more easily than GitLab Rails as a stateless service
  * **Direct Connections:** Future plans include direct client connections to improve request latency, with optional backward compatibility
  * **Stable API:** Provides single-purpose, version-agnostic endpoints designed for future scalability, composability, and security
  * **Protocol:** Uses a JSON-based API for communication, with REST+JSON chosen for compatibility with existing and future features


### Abstraction Layer for Enhanced AI Integration[](https://about.gitlab.com/direction/ai-powered/ai_framework/#abstraction-layer-for-enhanced-ai-integration)
The Abstraction Layer standardizes and simplifies the integration of AI/ML technologies within GitLab, providing an extendable GraphQL API called `aiAction`.
**Key Features:**
  * **Standardized API:** Provides a consistent interface for different AI actions, such as code suggestions and chat features
  * **Modular Design:** Supports new AI actions by extending the `aiAction` input with key/value pairs
  * **Secure and Scalable:** Ensures secure access to AI features while scaling to accommodate new functionalities and models


### Consolidated Evaluation Framework to Evaluate GenAI Models[](https://about.gitlab.com/direction/ai-powered/ai_framework/#consolidated-evaluation-framework-to-evaluate-genai-models)
The Consolidated Evaluation Framework (CEF) provides a comprehensive system for evaluating and optimizing GenAI models within GitLab.
**Key Features:**
  * **Benchmark Model Performance:** Systematically test models against standardized datasets to measure accuracy, relevance, and quality
  * **Compare Model Outputs:** Evaluate different models side-by-side to identify strengths and weaknesses for specific use cases
  * **Optimize Prompts:** Refine prompts through iterative testing to improve model responses
  * **Validate Model Updates:** Ensure new model versions maintain or improve performance before deployment
  * **Automate Quality Assurance:** Run continuous evaluation pipelines to maintain high standards across all AI features


The CEF integrates with our AI Gateway and Abstraction Layer, providing a unified workflow for model selection, evaluation, and deployment that helps teams deliver more reliable and effective AI-powered features.
## FY26 Strategic Goals & Objectives[](https://about.gitlab.com/direction/ai-powered/ai_framework/#fy26-strategic-goals--objectives)
  * **Goal 1: Model Flexibility**
    * Enable teams to integrate, test, and switch between different AI models seamlessly
  * **Goal 2: Support Model Validation**
    * Improve model validation by building on the Consolidated Evaluation Framework (CEF)
    * Unify ELI5 and the Prompt Library to provide comprehensive and automated model testing
  * **Goal 3: AI Settings Management**
    * Centralize and streamline AI configuration and management to simplify feature management for users
  * **Goal 4: AI Infrastructure Development & Scalability**
    * Enhance the AI Gateway and other infrastructure components to achieve high availability, scalability, and efficient context management
  * **Goal 5: Stage-Level Metrics & Dashboards**
    * Develop accurate, comprehensive dashboards to track key metrics and operational performance


### Quarterly Roadmap Overview[](https://about.gitlab.com/direction/ai-powered/ai_framework/#quarterly-roadmap-overview)
#### Q1: Establishing the Foundation[](https://about.gitlab.com/direction/ai-powered/ai_framework/#q1-establishing-the-foundation)
  * Initialize model flexibility improvements
  * Begin unification of ELI5 and Prompt Library
  * Complete AI Settings Management
  * Establish stage-level metrics dashboards
  * Start Discussion Summary enhancement project


#### Q2: Building on Momentum[](https://about.gitlab.com/direction/ai-powered/ai_framework/#q2-building-on-momentum)
  * Complete Model Flexibility initiatives
  * Enhance CEF with automated validation
  * Advance AI Gateway scalability
  * Implement advanced Discussion Summary features


#### Q3: Scaling and Refining Infrastructure[](https://about.gitlab.com/direction/ai-powered/ai_framework/#q3-scaling-and-refining-infrastructure)
  * Optimize infrastructure performance
  * Implement Context Management Framework
  * Integrate user feedback for Discussion Summary
  * Refine multi-provider strategies


#### Q4: Finalization and Future-Proofing[](https://about.gitlab.com/direction/ai-powered/ai_framework/#q4-finalization-and-future-proofing)
  * Finalize infrastructure optimization
  * Complete Context Management Framework
  * Document best practices and blueprints
  * Conclude Discussion Summary enhancements


## Categories[](https://about.gitlab.com/direction/ai-powered/ai_framework/#categories)
This group consists of the following categories:
  * [AI Gateway](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_gw): The AI Gateway is a standalone service providing AI features to all GitLab users
  * [Abstraction Layer](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_abstraction_layer): An AI Architecture to standardize and abstract AI/ML technologies within GitLab.com
  * [Duo Context Enrichment](https://about.gitlab.com/direction/ai-powered/ai_framework/duo_context_enrichment): Increase GitLab Duo quality by enhancing the AI's understanding of user inputs and project context to provide more accurate and relevant assistance within the GitLab ecosystem
  * [AI Research](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_research): Identifies and explores AI/ML models to support use cases across GitLab's stages and groups, enhancing the DevSecOps experience for users
  * [AI Evaluation](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_evaluation): Builds automated and scalable tools to evaluate model performance, output quality, and accuracy against specific inputs


## Team HQ[](https://about.gitlab.com/direction/ai-powered/ai_framework/#team-hq)
  * [AI Framework Team HQ](https://gitlab.com/groups/gitlab-org/-/epics/11403)


_  
Last Reviewed: 2025-06-11  
Last Updated: 2025-06-11 _
[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/ai-powered/ai_framework/index.html.md.erb) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/ai-powered/ai_framework/index.html.md.erb)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fai-powered%2Fai_framework%2F&_biz_t=1773331619973&_biz_i=%0AGroup%20Direction%20-%20AI%20Framework%0A%7C%0AGitLab%0A&_biz_n=19&rnd=3825&cdn_o=a&_biz_z=1773331620182)
suggested results