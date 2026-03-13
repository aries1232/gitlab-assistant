# AI Model Validation at GitLab
How we monitor the market for models to evaluate and respond to on-demand requests for new model evaluation.
## Introduction[](https://handbook.gitlab.com/handbook/engineering/development/data-science/ai-powered/model-validation/model_evaluation/#introduction)
GitLab’s approach to AI model validation combines rigorous assessment with practical efficiency to support our AI-powered features. Our framework helps enable teams to leverage cutting-edge AI technologies while maintaining GitLab’s quality and compliance standards. By establishing consistent validation practices, we help ensure models meet our performance, quality, and compliance requirements.
## Operational North Star Metric[](https://handbook.gitlab.com/handbook/engineering/development/data-science/ai-powered/model-validation/model_evaluation/#operational-north-star-metric)
The effectiveness of our validation system is measured primarily through **turnaround time** from model submission to validation report delivery. Note that we will only measure turnaround time for Open Source (OSS) model evaluations, because we are unable to control response time of model providers:
  * **Existing vendors (standard evaluation urgency)** : 5 business days
  * **New vendors** : 15 business days (best effort to achieve this, but we are dependent on vendor response times) 
    * New vendors **must be registered** with GitLab Legal as a new “sub-processor” before they can be used in customer-facing production products and features on GitLab dot-com. There is a 30 day notice to sign up a new sub-processor (i.e. a new model host). We don’t need to notify customers if we are moving off of a sub-processor or terminating the relationship, but we do need to notify if we are moving customer-facing features to a new model host.
    * To submit a new sub-processor, create a new Legal issue in the Legal project using the `general-legal-template` [issue template](https://gitlab.com/gitlab-com/legal-and-compliance/-/issues/new?issuable_template=general-legal-template) with the model provider details.


This turnaround time encompasses assessment across operational metrics (legal and compliance requirements), technical metrics (resource utilization and performance benchmarks), and integration metrics (deployment complexity and usability).
## Model Discovery and Selection Strategy[](https://handbook.gitlab.com/handbook/engineering/development/data-science/ai-powered/model-validation/model_evaluation/#model-discovery-and-selection-strategy)
GitLab maintains an active pipeline of AI models for evaluation through two complementary approaches:
### Market Monitoring[](https://handbook.gitlab.com/handbook/engineering/development/data-science/ai-powered/model-validation/model_evaluation/#market-monitoring)
The AI Framework team continuously surveys the AI landscape to identify promising models that might enhance GitLab’s features. We review academic publications, commercial releases, and open-source projects to identify models with potential applicability to GitLab features. We also benchmark notable models against our current production implementations and assess market adoption and community support to gauge long-term viability.
### Feature Team Requests[](https://handbook.gitlab.com/handbook/engineering/development/data-science/ai-powered/model-validation/model_evaluation/#feature-team-requests)
Feature teams can directly nominate specific models for evaluation based on their product requirements. When submitting a request, teams should provide:
  * Detailed justification for model evaluation, including intended use cases
  * Feature-specific evaluation criteria most relevant to their needs
  * Integration timeline requirements to help prioritize evaluations


## Bridge Process for Urgent Model Evaluation[](https://handbook.gitlab.com/handbook/engineering/development/data-science/ai-powered/model-validation/model_evaluation/#bridge-process-for-urgent-model-evaluation)
While our standard validation process provides comprehensive assessment for most situations, the **Bridge Process** applies to Open Source (OSS) models only, and provides an expedited evaluation path for high-urgency situations, enabling GitLab to respond quickly to significant market developments.
### When to Use the Bridge Process[](https://handbook.gitlab.com/handbook/engineering/development/data-science/ai-powered/model-validation/model_evaluation/#when-to-use-the-bridge-process)
The Bridge Process is appropriate when:
  * A newly released model presents significant competitive advantages
  * Rapid market positioning requires an immediate assessment
  * Feature teams face critical deadlines that require urgent evaluation


### Bridge Process Timeline and Activities[](https://handbook.gitlab.com/handbook/engineering/development/data-science/ai-powered/model-validation/model_evaluation/#bridge-process-timeline-and-activities)
The Bridge Process compresses our standard validation approach into a streamlined 5-day timeline:
  1. **Day 1-2: Initial Assessment**
     * Use a predefined prompt subset for a basic quality check
     * Review vendor terms and conditions for legal and operational risks 
       * **Note** : Feature teams accept the risk that even if the model passes technical evaluation, Legal may reject it
  2. **Day 3-4: Deep Evaluation**
     * Perform comprehensive testing using existing benchmarks
     * Assess scalability and integration requirements
  3. **Day 5: Final Review**
     * Compile results, document findings, and conduct stakeholder review
     * Provide clear next steps for feature teams


### Bridge Process Outputs[](https://handbook.gitlab.com/handbook/engineering/development/data-science/ai-powered/model-validation/model_evaluation/#bridge-process-outputs)
A successful Bridge Process delivers:
  1. Legal approval status of the model for production use
  2. An evaluation report based on our validation dimensions
  3. Stakeholder review and a go/no-go decision
  4. If approved, an iteration plan with target dates for model deployment


### Requesting a Bridge Process Evaluation[](https://handbook.gitlab.com/handbook/engineering/development/data-science/ai-powered/model-validation/model_evaluation/#requesting-a-bridge-process-evaluation)
Feature teams can initiate a Bridge Process by:
  1. Creating a dedicated issue using the [Model Validation Rapid Eval Request](https://gitlab.com/gitlab-org/gitlab/-/blob/master/.gitlab/issue_templates/AI%20Model%20Validation%20Rapid%20Eval%20Request.md) template
  2. Filling out the companion Legal intake issue to initiate the legal review


The AI Framework team reviews all Bridge Process requests within one business day.
## Validation Report Structure[](https://handbook.gitlab.com/handbook/engineering/development/data-science/ai-powered/model-validation/model_evaluation/#validation-report-structure)
For each evaluated model, we generate a comprehensive validation report containing:
### Performance Assessment[](https://handbook.gitlab.com/handbook/engineering/development/data-science/ai-powered/model-validation/model_evaluation/#performance-assessment)
  * **Comparative latency analysis against current production models** :
    * Response time benchmarks for standard input sizes
    * Tail latency comparison (p95, p99)
    * Time-to-first-token performance
  * **Resource requirements to match current performance baselines** :
    * GPU/CPU configurations needed
    * Memory footprint comparison
    * Infrastructure scaling requirements
  * **Cost Evaluation** :
    * Relative cost positioning using a simplified three-tier framework: 
      * Comparable to current baseline
      * Moderately higher cost impact (2-5x baseline)
      * Significant cost differential (>5x baseline)
  * **Partnership Status** :
    * Current relationship status with the model provider
    * Impact on decision-making when relevant


### Legal Status[](https://handbook.gitlab.com/handbook/engineering/development/data-science/ai-powered/model-validation/model_evaluation/#legal-status)
  * Legal team’s formal approval status (Approved/Not Approved)
  * Any conditional requirements or restrictions if approval is granted


### Quality Evaluation Results[](https://handbook.gitlab.com/handbook/engineering/development/data-science/ai-powered/model-validation/model_evaluation/#quality-evaluation-results)
Our quality assessment examines both raw model performance and feature-level implementation:
#### Short-term Evaluation Metrics[](https://handbook.gitlab.com/handbook/engineering/development/data-science/ai-powered/model-validation/model_evaluation/#short-term-evaluation-metrics)
  * Initial quality assessment focuses on GitLab’s core evaluation suite, measuring: 
    * Duo Chat performance metrics (readability, conciseness, correctness)
    * Code Suggestions accuracy
    * RCA averaged correctness scores
    * Vulnerability Resolution correctness scores


#### Long-term Monitoring Framework[](https://handbook.gitlab.com/handbook/engineering/development/data-science/ai-powered/model-validation/model_evaluation/#long-term-monitoring-framework)
We establish ongoing monitoring for:
  * Infrastructure stability (Apdex scores)
  * Workflow and tool response reliability
  * Upstream service availability
  * Feature-specific quality metrics


## Ownership and Responsibilities[](https://handbook.gitlab.com/handbook/engineering/development/data-science/ai-powered/model-validation/model_evaluation/#ownership-and-responsibilities)
### Model Validation Team Responsibilities[](https://handbook.gitlab.com/handbook/engineering/development/data-science/ai-powered/model-validation/model_evaluation/#model-validation-team-responsibilities)
  * Technical validation (resource usage, scalability)
  * Market monitoring and model pipeline management
  * Process coordination


### Feature Team Responsibilities[](https://handbook.gitlab.com/handbook/engineering/development/data-science/ai-powered/model-validation/model_evaluation/#feature-team-responsibilities)
  * Dataset creation for feature-specific evaluation
  * Feature quality ownership and implementation decisions


### Shared Responsibilities[](https://handbook.gitlab.com/handbook/engineering/development/data-science/ai-powered/model-validation/model_evaluation/#shared-responsibilities)
  * Model selection and prioritization
  * Evaluation criteria development
  * Results review and decision making


## Related Resources[](https://handbook.gitlab.com/handbook/engineering/development/data-science/ai-powered/model-validation/model_evaluation/#related-resources)
  * [AI Model Guidance](https://internal.gitlab.com/handbook/product/ai-strategy/ai-integration-effort/ai_model_guidance/)
  * [GitLab Model Vendor Selection Policy](https://docs.google.com/document/d/16PwPggN1wqWP2ezhCXIWc_vYzruYTlkM3Y8ZYyMetE4/edit?usp=sharing)


Last modified July 18, 2025: [Add 30 day subprocessor addition notice (`db8ecbae`)](https://gitlab.com/gitlab-com/content-sites/handbook/commit/db8ecbae)
[ ](https://gitlab.com/gitlab-com/content-sites/handbook/blob/main/content/handbook/engineering/development/data-science/ai-powered/model-validation/model_evaluation.md) - [ ](https://gitlab.com/-/ide/project/gitlab-com/content-sites/handbook/edit/main/-/content/handbook/engineering/development/data-science/ai-powered/model-validation/model_evaluation.md) - please [contribute](https://handbook.gitlab.com/handbook/about/contributing/). [ ![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-sa/4.0/)