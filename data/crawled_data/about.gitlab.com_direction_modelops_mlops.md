#  Group Direction - MLOps 
  1. You are here:
  2. [GitLab Direction](https://about.gitlab.com/direction/)
  3. [Product Stage Direction - ModelOps](https://about.gitlab.com/direction/modelops/)
  4. Group Direction - MLOps


####  Maintained by:
[ ![Taylor McCaslin](https://about.gitlab.com/images/team/taylormccaslin-crop.jpg) ](https://gitlab.com/tmccaslin) [ G ](https://gitlab.com/gl-product-leaders)
The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
## On this page
  * [MLOps](https://about.gitlab.com/direction/modelops/mlops/#mlops)
    * [Overview](https://about.gitlab.com/direction/modelops/mlops/#overview)
    * [Vision](https://about.gitlab.com/direction/modelops/mlops/#vision)
      * [Why is GitLab suitable for MLOPs?](https://about.gitlab.com/direction/modelops/mlops/#why-is-gitlab-suitable-for-mlops)
    * [Roadmap](https://about.gitlab.com/direction/modelops/mlops/#roadmap)
      * [Model Registry](https://about.gitlab.com/direction/modelops/mlops/#model-registry)
      * [Model Deployment](https://about.gitlab.com/direction/modelops/mlops/#model-deployment)
      * [Observability](https://about.gitlab.com/direction/modelops/mlops/#observability)
      * [LLMOps](https://about.gitlab.com/direction/modelops/mlops/#llmops)
      * [DevSecMLOps](https://about.gitlab.com/direction/modelops/mlops/#devsecmlops)


# MLOps[](https://about.gitlab.com/direction/modelops/mlops/#mlops)
|   
---|---  
Stage | [ModelOps](https://about.gitlab.com/direction/modelops/)  
Maturity | [minimal](https://about.gitlab.com/direction/#maturity)  
Content Last Reviewed | `2024-10-05`  
## Overview[](https://about.gitlab.com/direction/modelops/mlops/#overview)
Machine Learning Operations (MLOps) aims to bring together data exploration, experimentation, evaluation, deployment, management, and automation of machine learning models in production reliably and efficiently.
![MLOps Concept Map](https://about.gitlab.com/direction/modelops/mlops/MLOpsConceptMap.png)
The concept map above shows the key activities of MLOps, mapped to the user personas, and mapped to the tools and capabilities that help users accomplish those activities. You can further explore this [MLOps concept map](https://www.figma.com/file/gWegSkebhBXYdPxfkvT7LY/ModelOps-Concept-Map?type=whiteboard&node-id=0%3A1&t=3WCkMxPXSEiaJhBf-1) (along with DataOps and LLMOps).  
or watch the accompanying [overview video](https://youtu.be/74tpoTUMmeY).
## Vision[](https://about.gitlab.com/direction/modelops/mlops/#vision)
Data Scientist, ML Engineers, and stakeholders work together in GitLab to experiment, evaluate, verify, deploy, monitor and keep models secure and up-to-date. Their processes are reproducible, automated, collaborative, scalable, and monitored.
They further collaborate with other product development teams in GitLab so that there is tight coordination between models and their dependent applications. Teams stay informed on status of various components and can seamlessly coordinate making changes to production systems.
### Why is GitLab suitable for MLOPs?[](https://about.gitlab.com/direction/modelops/mlops/#why-is-gitlab-suitable-for-mlops)
Like software development, machine learning and model development benefit from automation and collaboration to consistently and iteratively deliver value. As machine learning becomes more prevalent, the number of individuals, roles, and frequency of changes increases. This causes friction and often results in costly errors. Instead of maintaining siloed workflows, bringing ML workflows into GitLab as a single collaboration platform extends the DevSecOps culture to data scientists, helping organizations achieve better results.
## Roadmap[](https://about.gitlab.com/direction/modelops/mlops/#roadmap)
Over the course of FY25, GitLab ramped up a team dedicated to MLOps. They are focused on the core of managing models and their versions, along with developing a MVC of model deployment.
### Model Registry[](https://about.gitlab.com/direction/modelops/mlops/#model-registry)
Succeeding with complex AI/ML workflows centers around managing models. Data scientists experiment and create model candidates, after validation candidates are promoted to models destined for production software. These promoted models need to be tracked and version just as any other code in a software project to ensure governance with any model workflows. As these models change over time the lineage of the data they were trained on, the source code they were generated with, and the software versions they are deployed into all needs to be tracked to produce lineage of the model for proper compliance and governance. A model registry is central to all these tasks and is the fundamental aspect of MLOPs. Everything we build to support AI/ML workflows will integrate to and from the model registry.
### Model Deployment[](https://about.gitlab.com/direction/modelops/mlops/#model-deployment)
Once models are versioned and tracked, they need to be deployed. This allows models to be excercised for evaluation to ensure they produce expected results but also to ensure that they operate as intended. We'll built an automated model deployment platform built atop the model registry to make it easy for the model registry to trigger GitLab CI/CD and enable dynamic evaluation within CI jobs. By doing this, models can be built, tested, and deployed just like any other part of a software system, all with automated CI/CD, source code management, and even security testing.
Our vision for model deploymnet will allow data scientists and software engineers to work together more seemlessly to build AI/ML powered software that powers our world.
### Observability[](https://about.gitlab.com/direction/modelops/mlops/#observability)
Once models are deployed, whether in development, staging, or production, they need to be tracked and observed for quality, performance, and model drift. Leveraging existing observability capabilieis within the GitLab platform, we'll extend observability to models managed and deployed by GitLab. This will allow data scientists to easily excercise and test model candidates and ensure they are operating as expected. This will also make it easier to track model drift and automate how problems with models are addressed, even when running in production.
### LLMOps[](https://about.gitlab.com/direction/modelops/mlops/#llmops)
The rise of large language models (LLMs) has further complicated the AI/ML space with even larger models, continuous data training NEEDS, high velocity changes, and increased utilization of AI/ML models in production software. GitLab intends to help customers build, personalize, and operate LLMs. We'll share more in 2025 as this space develops.
### DevSecMLOps[](https://about.gitlab.com/direction/modelops/mlops/#devsecmlops)
With our MLOps capabilities integrated into the wider DevSecOps platform, GitLab will bring data scientists, software engineers, and DevOps engineers into closer collaboration. It will enable these different personas to work more smoothly together and enhance the feedback loop between AI development and traditional software development. Additionally it'll bring the best practices of DevOps to AI/ML workloads improving how enterprises build next generation software powered by AI/ML systems.
[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/modelops/mlops/index.html.md.erb) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/modelops/mlops/index.html.md.erb)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fmodelops%2Fmlops%2F&_biz_t=1773331607694&_biz_i=%0AGroup%20Direction%20-%20MLOps%0A%7C%0AGitLab%0A&_biz_n=16&rnd=284768&cdn_o=a&_biz_z=1773331607696)
suggested results