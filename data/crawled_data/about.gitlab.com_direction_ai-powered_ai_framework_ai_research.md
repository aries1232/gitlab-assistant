#  Category Direction - AI Research 
  1. You are here:
  2. [GitLab Direction](https://about.gitlab.com/direction/)
  3. [Stage Direction - AI-powered](https://about.gitlab.com/direction/ai-powered/)
  4. [Group Direction - AI Framework](https://about.gitlab.com/direction/ai-powered/ai_framework/)
  5. Category Direction - AI Research


The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
## On this page
  * [AI Research](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_research/#ai-research)
  * [Overview](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_research/#overview)
  * [Evaluation Criteria](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_research/#evaluation-criteria)
  * [Evaluation Techniques](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_research/#evaluation-techniques)
  * [Continuous Monitoring](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_research/#continuous-monitoring)
  * [Future Direction](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_research/#future-direction)


## AI Research[](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_research/#ai-research)
|   
---|---  
Stage | [AI-powered](https://about.gitlab.com/direction/ai-powered/)  
Group | [AI Framework](https://about.gitlab.com/direction/ai-powered/ai_framework)  
Maturity | [Available](https://about.gitlab.com/direction/#maturity)  
Content Last Reviewed | `2026-06-11`  
## Overview[](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_research/#overview)
The AI Research category identifies and explores AI/ML models to support use cases that other GitLab sections, stages, and groups are developing to enrich the DevSecOps experience for GitLab users.
We continuously evaluate AI/ML model vendors, open source models, and generative AI foundation models. Models showing promising results from our initial research undergo further testing via the [AI Evaluation](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_evaluation/) platform. We compare these models against those already supported in our [AI Framework](https://about.gitlab.com/direction/ai-powered/ai_framework/) and actively powering [GitLab Duo](https://about.gitlab.com/gitlab-duo/) features, including [self-hosted models](https://about.gitlab.com/direction/ai-powered/custom_models/).
## Evaluation Criteria[](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_research/#evaluation-criteria)
We evaluate models using comprehensive criteria to support our enterprise customers' needs:
  * **Model capabilities** : Performance across various tasks and use cases
  * **Model interface** : API design, ease of integration, and developer experience
  * **Data governance policies** : Compliance with privacy regulations and data handling practices
  * **Security** : Authentication, encryption, and vulnerability management
  * **Deployment options** : Cloud, on-premises, and hybrid deployment flexibility
  * **Organizational track record** : Stability, support quality, and long-term viability of model providers
  * **Cost efficiency** : Pricing models and total cost of ownership
  * **Performance metrics** : Latency, throughput, and scalability characteristics


## Evaluation Techniques[](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_research/#evaluation-techniques)
GitLab has built an advanced model evaluation platform called the Prompt Library. This platform contains thousands of human and synthetic generated prompts that we use to evaluate various AI models and model versions.
We use this suite of evaluations to run large-scale testing of AI model quality output against both human and synthetic generated benchmarks. Our evaluation framework incorporates multiple techniques, including but not limited to:
  * **Cosine similarity** : Measures semantic similarity between model outputs and expected results
  * **Embedding similarity** : Compares vector representations of text to assess contextual understanding
  * **LLM evaluators** : Uses LLMs to evaluate other LLM outputs for quality and accuracy


These represent just a sample of our evaluation methods. Teams across GitLab continuously develop and implement additional metrics and evaluation techniques tailored to their specific use cases and requirements. While no single technique is perfect, we combine multiple methods to comprehensively compare the quality of different models and versions.
This system enables GitLab to evaluate both new models and updated versions of existing models. We've successfully used this system to identify issues with model updates from our AI vendors. In some cases, it has detected model drift that vendors neither anticipated nor communicated to GitLab.
## Continuous Monitoring[](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_research/#continuous-monitoring)
While our AI Evaluation suite currently provides point-in-time comparisons, we are developing automated testing capabilities. This will enable us to run the entire evaluation suite against models regularly, continuously detecting drift and model regressions.
## Future Direction[](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_research/#future-direction)
The AI Research category will continue expanding its capabilities to:
  * Broaden the range of evaluated models and use cases
  * Develop more sophisticated evaluation metrics
  * Enhance automation for continuous model assessment
  * Share insights with the broader GitLab community


_  
Last Reviewed: 2025-06-11  
Last Updated: 2025-06-11 _
[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/ai-powered/ai_framework/ai_research/index.html.md.erb) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/ai-powered/ai_framework/ai_research/index.html.md.erb)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fai-powered%2Fai_framework%2Fai_research%2F&_biz_t=1773331931438&_biz_i=%0ACategory%20Direction%20-%20AI%20Research%0A%7C%0AGitLab%0A&_biz_n=83&rnd=775385&cdn_o=a&_biz_z=1773331931553)
suggested results