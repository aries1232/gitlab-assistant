#  Group Direction - Custom Models 
  1. You are here:
  2. [GitLab Direction](https://about.gitlab.com/direction/)
  3. [Stage Direction - AI-powered](https://about.gitlab.com/direction/ai-powered/)
  4. Group Direction - Custom Models


The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
## On this page[](https://about.gitlab.com/direction/ai-powered/custom_models/#on-this-page)
  * [On this page](https://about.gitlab.com/direction/ai-powered/custom_models/#on-this-page)
  * [Custom Models](https://about.gitlab.com/direction/ai-powered/custom_models/#custom-models)
    * [Overview](https://about.gitlab.com/direction/ai-powered/custom_models/#overview)
    * [What Drives The Need For Custom Models?](https://about.gitlab.com/direction/ai-powered/custom_models/#what-drives-the-need-for-custom-models)
  * [Strategy](https://about.gitlab.com/direction/ai-powered/custom_models/#strategy)
    * [GitLab Duo Self-Hosted](https://about.gitlab.com/direction/ai-powered/custom_models/#gitlab-duo-self-hosted)
    * [Customization](https://about.gitlab.com/direction/ai-powered/custom_models/#customization)
    * [Logging](https://about.gitlab.com/direction/ai-powered/custom_models/#logging)
    * [Validation](https://about.gitlab.com/direction/ai-powered/custom_models/#validation)
  * [Focus](https://about.gitlab.com/direction/ai-powered/custom_models/#focus)
    * [Identify and validate models that can be customized using the following criteria:](https://about.gitlab.com/direction/ai-powered/custom_models/#identify-and-validate-models-that-can-be-customized-using-the-following-criteria)
    * [Deeply understand customer privacy and security concerns associated with AI/ML use cases](https://about.gitlab.com/direction/ai-powered/custom_models/#deeply-understand-customer-privacy-and-security-concerns-associated-with-aiml-use-cases)
    * [Research techniques to enable customer customization of models.](https://about.gitlab.com/direction/ai-powered/custom_models/#research-techniques-to-enable-customer-customization-of-models)
    * [Validate Customer Modification](https://about.gitlab.com/direction/ai-powered/custom_models/#validate-customer-modification)
    * [What We Are Not Doing](https://about.gitlab.com/direction/ai-powered/custom_models/#what-we-are-not-doing)


## Custom Models[](https://about.gitlab.com/direction/ai-powered/custom_models/#custom-models)
|   
---|---  
Stage | [AI-powered](https://about.gitlab.com/direction/ai-powered/)  
Group | [Custom Models](https://about.gitlab.com/direction/ai-powered/custom_models)  
Maturity | [Available](https://about.gitlab.com/direction/#maturity)  
Content Last Reviewed | `2024-10-05`  
### Overview[](https://about.gitlab.com/direction/ai-powered/custom_models/#overview)
The [Custom Models group ](https://gitlab.com/groups/gitlab-org/-/epics/13068) is dedicated to empowering GitLab users with the flexibility to deploy and customize GitLab Duo Features within their local environments. We also aim to allow customers to adapt Duo Features with their own data, based on their own code, needs, requirements and styles. Our goal is to give customers a more tailored Duo experience.
We will leverage a variety of open source and private-cloud hosted AI models to enable GitLab Duo functionality on all GitLab surfaces, to include Air-Gapped, Self-Managed, Dedicated, and Gitlab.com. We will ensure that supported features are of the highest possible quality using GitLab’s [validation process](https://about.gitlab.com/blog/developing-gitlab-duo-how-we-validate-and-test-ai-models-at-scale/), and support customers in tailoring GitLab Duo features with their own source code and data. We will also work with other teams within GitLab to explore opportunities for customizing AI models across the platform.
### What Drives The Need For Custom Models?[](https://about.gitlab.com/direction/ai-powered/custom_models/#what-drives-the-need-for-custom-models)
Regardless of how customers access GitLab, they deserve the chance to leverage Duo features. Customers have a wide variety of security and compliance requirements, some of which may preclude them from utilizing our existing Duo features that are enabled through GitLab.com. Providing customers with a self-hosted deployment option for Duo features will allow them to reap the benefits of AI while meeting their security and compliance requirements.
Customers may also want to adapt their Duo experience more directly to their own organization. For example, a customer may want the ability to adapt Code Suggestions to be based on their own code base so that any suggestions match their unique coding styles, standards, and programming language of preference. In addition, customers may want to be able to orient Duo Chat to their internal knowledge bases to answer questions on their own documentation.
## Strategy[](https://about.gitlab.com/direction/ai-powered/custom_models/#strategy)
The Custom Models team has dual focus of 1) enabling GitLab Duo Self-Hosted features leveraging customer's preferred model architecture (either on-premise or via private cloud) and 2) enabling customization of Duo features grounded in customer data.
### GitLab Duo Self-Hosted[](https://about.gitlab.com/direction/ai-powered/custom_models/#gitlab-duo-self-hosted)
Custom Models has released GitLab Duo Self-Hosted as generally available. You can now enable GitLab Duo AI features on their self-managed Gitlab environment using supported model platforms and models. With GitLab Duo Self-Hosted, you can use models hosted either on-premise or in a private cloud. We currently support open-source Mistral models on vLLM or AWS Bedrock, Claude 3.5 Sonnet on AWS Bedrock, and OpenAI models on Azure OpenAI.
GitLab Duo Self-Hosted now supports the following [Duo features](https://docs.gitlab.com/administration/gitlab_duo_self_hosted/#supported-gitlab-duo-features):
Feature | Available on GitLab Duo Self-Hosted | GitLab version  
---|---|---  
[GitLab Duo Chat](https://docs.gitlab.com/user/gitlab_duo_chat/) |  Yes | GitLab 17.9 and later  
[Code Suggestions](https://docs.gitlab.com/user/project/repository/code_suggestions/) |  Yes | GitLab 17.9 and later  
[Code Explanation](https://docs.gitlab.com/user/project/repository/code_explain/) |  Yes | GitLab 17.9 and later  
[Test Generation](https://docs.gitlab.com/user/gitlab_duo_chat/examples/#write-tests-in-the-ide) |  Yes | GitLab 17.9 and later  
[Refactor Code](https://docs.gitlab.com/user/gitlab_duo_chat/examples/#refactor-code-in-the-ide) |  Yes | GitLab 17.9 and later  
[Fix Code](https://docs.gitlab.com/user/gitlab_duo_chat/examples/#fix-code-in-the-ide) |  Yes | GitLab 17.9 and later  
[AI Impact Dashboard](https://docs.gitlab.com/user/analytics/ai_impact_analytics/) |  Beta | GitLab 17.9 and later  
[Root Cause Analysis](https://docs.gitlab.com/user/gitlab_duo_chat/examples/#troubleshoot-failed-cicd-jobs-with-root-cause-analysis) |  Beta | GitLab 17.10 and later  
[Vulnerability Explanation](https://docs.gitlab.com/user/application_security/vulnerabilities/#explaining-a-vulnerability) |  Beta | GitLab 17.11 and later  
[Vulnerability Resolution](https://docs.gitlab.com/user/application_security/vulnerabilities/#vulnerability-resolution) |  Beta | GitLab 17.11 and later  
[Discussion Summary](https://docs.gitlab.com/user/discussions/#summarize-issue-discussions-with-duo-chat) |  Beta | GitLab 17.11 and later  
[GitLab Duo for the CLI](https://docs.gitlab.com/editor_extensions/gitlab_cli/#gitlab-duo-for-the-cli) |  Beta | GitLab 17.11 and later  
[Summarize a Code Review](https://docs.gitlab.com/user/project/merge_requests/duo_in_merge_requests/#summarize-a-code-review) |  Experiment | GitLab 17.11 and later  
[Code Review](https://docs.gitlab.com/user/project/merge_requests/duo_in_merge_requests/#have-gitlab-duo-review-your-code) |  No | Not applicable  
[Merge Commit Message Generation](https://docs.gitlab.com/user/project/merge_requests/duo_in_merge_requests/#generate-a-merge-commit-message) |  Beta | GitLab 17.11 and later  
[Summarize New Merge Request](https://docs.gitlab.com/user/project/merge_requests/duo_in_merge_requests/#generate-a-description-by-summarizing-code-changes) |  Beta | GitLab 17.11 and later  
[Issue Description Generation](https://docs.gitlab.com/user/project/issues/managing_issues/#populate-an-issue-with-issue-description-generation) |  No | Not applicable  
For more information on how to set-up your self-hosted model, see [GitLab Duo Self-Hosted documentation](https://docs.gitlab.com/administration/gitlab_duo_self_hosted/). For information on how to trial GitLab Enterprise, see [Get Started with GitLab Duo](https://about.gitlab.com/solutions/gitlab-duo-pro/sales/?toggle=gitlab-duo-pro).
###  [Customization](https://gitlab.com/groups/gitlab-org/-/epics/13070)[](https://about.gitlab.com/direction/ai-powered/custom_models/#customization)
The Custom Models team is also dedicated to providing tailored customizations for GitLab Duo features. Not all Duo features will benefit from a customized approach and we are assessing the added value of customization for several of the Duo features. Our first approach to customization of Duo features is grounded in external context. Additional information on our considerations for customization can be found on our [Model Personalization epic](https://gitlab.com/groups/gitlab-org/-/epics/13070).
### Logging[](https://about.gitlab.com/direction/ai-powered/custom_models/#logging)
As we advance support for self-hosted models and customization approaches, we need to allow customers visibility into their own LLM flows for debugging, auditing, validation, and potentially accumulating data sets for supervised fine tuning. To that end, Custom Models will enable customer-facing logging (not visible to GitLab) on self-managed instances. Additional information can be found on the [Logging epic](https://gitlab.com/groups/gitlab-org/-/epics/14718).
### Validation[](https://about.gitlab.com/direction/ai-powered/custom_models/#validation)
As we offer additional configuration options, either in the form of enabling model choice for GitLab Duo features or in customizations, GitLab will not necessarily have insight into the performance of Duo features. Customers will want to assess the performance and functionality of their selected models and customizations. While GitLab has an internally facing validation process via the Centralized Evaluation Framework (CEF), configurations made within a self-managed customer space will not be visible to GitLab. Customers will require the ability to assess the performance of their chosen implementations. We are exploring a UI for validation that is fully integrated into the GitLab platform, allowing users to leverage prompt libraries to establish baselines performances for different models and RAG configurations.This will allow customers to deploy self-hosted models and leverage customization with confidence. Additional information on our plans can be found on the [Customer-Facing Validation epic](https://gitlab.com/groups/gitlab-org/-/epics/14719).
## Focus[](https://about.gitlab.com/direction/ai-powered/custom_models/#focus)
#### Identify and validate models that can be customized using the following criteria:[](https://about.gitlab.com/direction/ai-powered/custom_models/#identify-and-validate-models-that-can-be-customized-using-the-following-criteria)
  * open source or available via private-cloud hosting
  * minimal computing requirements
  * well suited for Duo feature use cases
  * high quality output


#### Deeply understand customer privacy and security concerns associated with AI/ML use cases[](https://about.gitlab.com/direction/ai-powered/custom_models/#deeply-understand-customer-privacy-and-security-concerns-associated-with-aiml-use-cases)
#### Research techniques to enable customer customization of models.[](https://about.gitlab.com/direction/ai-powered/custom_models/#research-techniques-to-enable-customer-customization-of-models)
  * How can we allow customization without sacrificing the quality of Duo features?
  * Techniques under consideration include: 
    * RAG
    * Fine-Tuning


#### Validate Customer Modification[](https://about.gitlab.com/direction/ai-powered/custom_models/#validate-customer-modification)
Develop or identify a lightweight validation framework that can give customers assurances that customized product is performing at a high level of quality output and haven’t degraded performance of the model
#### What We Are Not Doing[](https://about.gitlab.com/direction/ai-powered/custom_models/#what-we-are-not-doing)
  * Bring your own model - we are not currently supporting any and all model; the quality of GitLab Duo features is our first priority, and so will be starting with a set of pre-defined model options.
  * We are not supporting personalization at an individual user level, but rather Enterprise-level customization.


[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/ai-powered/custom_models/index.html.md.erb) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/ai-powered/custom_models/index.html.md.erb)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fai-powered%2Fcustom_models%2F&_biz_t=1773331632795&_biz_i=%0AGroup%20Direction%20-%20Custom%20Models%0A%7C%0AGitLab%0A&_biz_n=22&rnd=13326&cdn_o=a&_biz_z=1773331632935)
suggested results