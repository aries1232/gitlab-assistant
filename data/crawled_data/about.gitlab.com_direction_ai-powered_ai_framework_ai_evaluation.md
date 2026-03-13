#  Category Direction - AI Evaluation 
  1. You are here:
  2. [GitLab Direction](https://about.gitlab.com/direction/)
  3. [Stage Direction - AI-powered](https://about.gitlab.com/direction/ai-powered/)
  4. [Group Direction - AI Framework](https://about.gitlab.com/direction/ai-powered/ai_framework/)
  5. Category Direction - AI Evaluation


The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
## On this page
  * [AI Evaluation](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_evaluation/#ai-evaluation)
  * [Overview](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_evaluation/#overview)
  * [Quick Links](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_evaluation/#quick-links)
  * [Goal](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_evaluation/#goal)
  * [What's Next & Why](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_evaluation/#whats-next--why)


## AI Evaluation[](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_evaluation/#ai-evaluation)
|   
---|---  
Stage | [AI-powered](https://about.gitlab.com/direction/ai-powered/)  
Group | [AI Model Validation](https://about.gitlab.com/direction/ai-powered/ai_framework)  
Content Last Reviewed | `2024-06-11`  
## Overview[](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_evaluation/#overview)
AI Validation is a critical cornerstone for successfully implementing GenAI solutions. It provides mechanisms to empirically measure GenAI outputs at scale, enabling data-driven decisions.
AI Validation empowers methodical iteration on AI features, creating greater efficiency in developing AI-enabled workflows across the platform. It ensures the reliability and quality of AI outputs, mitigating risks associated with GenAI.
The AI Validation Team's Centralized Evaluation Framework supports the entire end-to-end process of AI feature creation—from selecting appropriate models to evaluating feature outputs. AI Validation complements other evaluation types such as SET Quality testing and diagnostic testing, focusing specifically on GenAI interactions.
The Centralized Evaluation Framework relies on three main elements: a prompt library, [validation metrics](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_evaluation/metrics/), and comparative [foundational models](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_evaluation/foundation_models/). The prompt library contains diverse benchmark datasets tailored to various use cases, including code completion, code generation, and natural language questions. Validation metrics assess the accuracy and usefulness of GenAI outputs against industry benchmarks. The framework incorporates various validation methods, including but not limited to LLM consensus filtering, LLM judges, and cosine similarities. Foundational models provide baselines for measuring GitLab AI feature performance against industry standards. Additional information on our validation process is available [here](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_evaluation/procedures/).
The Evaluation Framework enables large-scale tests designed to be composable via CLI (Command Line Interface) and API. This allows feature teams to assess the impact of code changes on specific AI-generated content. For example, teams focusing on improving output for specific use cases can test only those cases rather than the entire test corpus. Test results are accessible locally, on BigQuery (Google's data warehouse), or via feature-specific dashboards. The AI Validation team began by supporting Code Suggestions and now actively supports Duo Chat.
## Quick Links[](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_evaluation/#quick-links)
  * [Validation metrics and methodologies](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_evaluation/metrics/)
  * [Foundational models and benchmarks](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_evaluation/foundation_models/)
  * [Validation procedures and best practices](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_evaluation/procedures/)


## Goal[](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_evaluation/#goal)
The AI Validation team continues iterating on and building the Centralized Evaluation Framework. Our goal is to expand support to future AI-powered features, enhance developer productivity, and instill confidence in the reliability and value of AI-powered processes across the software development lifecycle.
The AI Validation category focuses on assessing performance, tuning parameters, prompt engineering techniques, and quality of algorithms for various AI models. The Centralized Evaluation Framework incorporates numerous open source models as well as industry models from Google, Anthropic, and others.
Current work supports the Duo Chat team in assessing chat responses based on correctness, readability, and comprehensiveness. The AI Validation team uses industry models as benchmarks and has curated both open source and custom datasets for specific use cases identified by the Duo Chat team. We employ validation methods appropriate to chat use cases, including LLM consensus filtering, LLM judges, and cosine similarity scores. The AI Validation team works closely with the Duo Chat team to enable efficient, data-driven iteration on Chat tool engineering and production of high-quality responses.
## What's Next & Why[](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_evaluation/#whats-next--why)
[AI Validation Group Direction](https://gitlab.com/groups/gitlab-org/-/epics/11290 "AI Model Validation Group Direction")
[Our OKRs](https://gitlab.com/gitlab-com/gitlab-OKRs/-/issues/?sort=title_asc&state=opened&label_name%5B%5D=group%3A%3Aai%20model%20validation&first_page_size=20)
FY25 R&D Investment Themes: [Enable AI/ML Efficiencies Across DevSecOps](https://about.gitlab.com/direction/#enable-aiml-efficiencies-across-devsecops)
AI Validation enables data-driven decisions in creating and implementing GenAI features across the GitLab platform. We have provided support to Code Suggestions and Duo Chat, and will continue enabling efficient iteration on GenAI features. As a long-term initiative, we aim to expand our Centralized Evaluation Framework to evaluate various models based on Quality, Cost, and Latency.
Our short-term goals support scaling the Centralized Evaluation Framework and include:
  * Publishing the centralized blueprint for the end-to-end architecture of the Centralized Evaluation Framework and algorithmic basis for AI evaluation methods
  * Providing ongoing support to Duo Chat by augmenting Centralized Evaluation Framework datasets with prompt libraries supporting Code Generation, Code Explanation, and Search, plus adding two additional evaluation metrics
  * Solution validating an API access point for the Centralized Evaluation Framework, providing uniform access to the prompt library and versioning of inputs (including models, prompt engineering, and other inputs)
  * Solution validating a dynamic dashboard providing metrics updated weekly to track model drift and other potential issues, including all production models and previously tested industry benchmark models


Primary Decision Factors, inspired by this [paper](https://arxiv.org/pdf/2203.02155.pdf):
  1. Will the output be honest (consistent with facts)?
  2. Will the output be harmless (avoiding potentially offensive content)?
  3. Will the output be helpful (accomplishing the user's goal)?


[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/ai-powered/ai_framework/ai_evaluation/index.html.md.erb) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/ai-powered/ai_framework/ai_evaluation/index.html.md.erb)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fai-powered%2Fai_framework%2Fai_evaluation%2F&_biz_t=1773331935748&_biz_i=%0ACategory%20Direction%20-%20AI%20Evaluation%0A%7C%0AGitLab%0A&_biz_n=84&rnd=856453&cdn_o=a&_biz_z=1773331935914)
suggested results