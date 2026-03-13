#  Category Direction - AI Gateway 
  1. You are here:
  2. [GitLab Direction](https://about.gitlab.com/direction/)
  3. [Stage Direction - AI-powered](https://about.gitlab.com/direction/ai-powered/)
  4. [Group Direction - AI Framework](https://about.gitlab.com/direction/ai-powered/ai_framework/)
  5. Category Direction - AI Gateway


The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
## On this page
  * [AI Gateway](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_gw/#ai-gateway)
    * [Key Features](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_gw/#key-features)
    * [Future Plans](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_gw/#future-plans)
    * [API and Protocol](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_gw/#api-and-protocol)
    * [Authentication & Authorization](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_gw/#authentication--authorization)
    * [Deployment](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_gw/#deployment)
  * [Future Work](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_gw/#future-work)
  * [Related Components](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_gw/#related-components)

|   
---|---  
Stage | [AI-powered](https://about.gitlab.com/direction/ai-powered/)  
Group | [AI Framework](https://about.gitlab.com/direction/ai-powered/ai_framework/)  
Maturity | [Planned](https://about.gitlab.com/direction/#maturity)  
Content Last Reviewed | `2024-01-30`  
## AI Gateway[](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_gw/#ai-gateway)
The AI Gateway is a standalone service that provides access to AI features for all GitLab users, regardless of their instance type (self-managed, dedicated, or GitLab.com). It acts as an API Gateway, handling traffic from cloud.gitlab.com/ai/* and directing it to AI providers and their models.
### Key Features[](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_gw/#key-features)
  * Centralized access point for AI features
  * Scalable and stateless service
  * Enables self-managed installations to access AI features without hosting their own models
  * Written in Python for ease of use by data and ML engineers


### Future Plans[](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_gw/#future-plans)
  * Multi-region deployment (currently under consideration)
  * Direct connections from clients (tracked in an epic)
  * Support for the last 2 major GitLab versions


### API and Protocol[](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_gw/#api-and-protocol)
  * JSON-based API with single-purpose endpoints
  * Version-agnostic design for cross-version compatibility
  * Uses a simple JSON envelope for transporting feature-specific information


### Authentication & Authorization[](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_gw/#authentication--authorization)
  * GitLab provides the first layer of authorization
  * AI Gateway accessed through Cloud Connector for instance authentication
  * Plans for end-user authentication support


### Deployment[](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_gw/#deployment)
  * Currently deployed from the project repository in gitlab-org/modelops/applied-ml/code-suggestions/ai-assist
  * Future plans to deploy using Runway with production and staging environments


## Future Work[](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_gw/#future-work)
  1. Centralized Access Through AI Gateway
  2. Unit Primitives 
     * Initial support for Code Suggestions and Chat
     * Future decomposition of Chat into multiple primitives
  3. Self Managed AI Gateway 
     * Option for self-managed instances to use GitLab-hosted AI Gateway or deploy their own


## Related Components[](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_gw/#related-components)
  * AI Agents: For creating and managing agents and prompts
  * Model Registry: For managing and deploying machine learning models


_  
Last Reviewed: 2024-06-28  
Last Updated: 2024-06-28 _
[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/ai-powered/ai_framework/ai_gw/index.html.md.erb) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/ai-powered/ai_framework/ai_gw/index.html.md.erb)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fai-powered%2Fai_framework%2Fai_gw%2F&_biz_t=1773331922746&_biz_i=%0ACategory%20Direction%20-%20AI%20Gateway%0A%7C%0AGitLab%0A&_biz_n=81&rnd=299374&cdn_o=a&_biz_z=1773331922918)
suggested results