#  Group Direction - Utilization 
  1. You are here:
  2. [GitLab Direction](https://about.gitlab.com/direction/)
  3. [Product Section Direction - Fulfillment](https://about.gitlab.com/direction/fulfillment/)
  4. Group Direction - Utilization


The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
  * [Fulfillment Utilization Overview](https://about.gitlab.com/direction/fulfillment/utilization/#fulfillment-utilization-overview)
  * [Vision](https://about.gitlab.com/direction/fulfillment/utilization/#vision)
  * [Feature Overview and Maturity](https://about.gitlab.com/direction/fulfillment/utilization/#feature-overview-and-maturity)
  * [1-year Plan](https://about.gitlab.com/direction/fulfillment/utilization/#1-year-plan)
    * [1-year Vision](https://about.gitlab.com/direction/fulfillment/utilization/#1-year-vision)
    * [Roadmap](https://about.gitlab.com/direction/fulfillment/utilization/#roadmap)
    * [Possible Future Opportunities](https://about.gitlab.com/direction/fulfillment/utilization/#possible-future-opportunities)
  * [Additional Information](https://about.gitlab.com/direction/fulfillment/utilization/#additional-information)
    * [Q&A](https://about.gitlab.com/direction/fulfillment/utilization/#qa)


## Fulfillment Utilization Overview[](https://about.gitlab.com/direction/fulfillment/utilization/#fulfillment-utilization-overview)
The Utilization group aims to ensure customers have access to consumables usage data (storage, compute minutes, and transfer units) so that they can make the optimal decisions for their business needs.
## Vision[](https://about.gitlab.com/direction/fulfillment/utilization/#vision)
_What is our long-term solution concept? Analogy: what will it look like at the top of the mountain?_
Consumables usage would provide predictability to our customers through transparent usage visibility, suggested usage management recommendations, and purchasing directions. Our sales teams would be empowered to have customer discussions about growth with detailed usage data as a foundation for that conversation.
## Feature Overview and Maturity[](https://about.gitlab.com/direction/fulfillment/utilization/#feature-overview-and-maturity)
_What features are the Utilization group responsible for and how mature are they?_
**Legend** :
  * 🙂 **Minimal** : Available and works for a small number of use cases. Some transparency for internal teams.
  * 😊 **Viable** : Available and works for the majority of use cases. Some transparency for internal teams.
  * 😁 **Complete** : Fully functional for all eligible use cases. Full transparency for internal teams.
  * 😍 **Lovable** : Glowing reviews from external and internal users.

Feature | Maturity | Description  
---|---|---  
Storage Usage Visibility | 😊 Viable | Customers understand how much storage they are using and what projects/file types are contributing to that usage.  
Storage Quota | 😊 Viable | Customers understand if they are within the storage limits threshold and how to take action (remove, add more, set storage limits)  
Compute Minutes Usage Visibility | 😊 Viable | Customers understand how many compute minutes they are using  
Quota of Compute Minutes | 😊 Viable | Customers understand if they are running out of compute minutes and how to buy more  
Transfer Usage Visibility | Not yet available | Customers understand how much transfer they are consuming  
Quota of Transfer | Not yet available | Customers understand if they are running out of transfer units and how to buy more  
## 1-year Plan[](https://about.gitlab.com/direction/fulfillment/utilization/#1-year-plan)
_Where are we focused over the next 12 months to make meaningful steps towards achieving our vision and increasing feature maturity?_
### 1-year Vision[](https://about.gitlab.com/direction/fulfillment/utilization/#1-year-vision)
In a year from now, we hope to have:
  1. ✅ Provided users with [MVC storage visibility](https://gitlab.com/gitlab-com/gitlab-OKRs/-/work_items/1769)
  2. ✅ Create a common layout for [Usage Quotas pages](https://gitlab.com/groups/gitlab-org/-/epics/7176). This reduced code duplications, improved developer experience by having all the code of the page in one directory,mitigated future code duplication, and enabled Usage Quotas for all tiers and editions.
  3. Complete [compute minute limit](https://gitlab.com/groups/gitlab-org/-/epics/13989) adjustment for GitLab.com Free Tier.


### Roadmap[](https://about.gitlab.com/direction/fulfillment/utilization/#roadmap)
  1. Complete [compute minute limit](https://gitlab.com/groups/gitlab-org/-/epics/13989) adjustment for GitLab.com Free Tier.


### Possible Future Opportunities[](https://about.gitlab.com/direction/fulfillment/utilization/#possible-future-opportunities)
What is the work to do? | Why are we considering doing it  
---|---  
Storage Usage [Visibility & Enforcement](https://gitlab.com/groups/gitlab-org/-/epics/10940) | Over time, a GitLab namespace can generate a significant amount of storage. This includes activities like pushing code, creating new containers and packages, running CI/CD jobs, and more. This storage increases the cost of operating a GitLab.  
Improve the [Self-Managed Storage Experience](https://gitlab.com/groups/gitlab-org/-/epics/11423) | Self-managed users need a UI that helps them achieve the jobs related to storage usage visibility and leveraging the storage limit [feature](https://docs.gitlab.com/ee/administration/settings/account_and_limit_settings.html#repository-size-limit). They do not need see UI related to storage enforcement limits.  
Transfer Visibility & Enforcement | Over time, a GitLab namespace can have significant transfer usage. This increased the cost of operating GitLab.  
[Paid Tier Storage Enforcement](https://gitlab.com/groups/gitlab-org/-/epics/8380) | Over time, a GitLab namespace can generate a significant amount of storage. This includes activities like pushing code, creating new containers and packages, running CI/CD jobs, and more. This storage increases the cost of operating a GitLab.  
Support [pricing & packaging innovation for storage product](https://gitlab.com/groups/gitlab-org/-/epics/11774) | Current storage limits are set with one size per plan, which does not account for the different needs that a namespace with a higher seat count may have, for example, 20 seats vs 2000 seats.  
Support [consumption pricing and packing innovation](https://gitlab.com/gitlab-org/fulfillment/meta/-/issues/1541) for our consumables products. | Seat pricing doesn’t scale with the value of automation. Software increasingly automates manual processes. The more successful a product is, the fewer user seats a customer needs.  
## Additional Information[](https://about.gitlab.com/direction/fulfillment/utilization/#additional-information)
### Q&A[](https://about.gitlab.com/direction/fulfillment/utilization/#qa)
Question | Answer  
---|---  
What type of customers does Utilization serve? | - SM & SaaS Self-service customers   
- SM & SaaS Sales assisted customers   
- SM & SaaS Channel Partners and their customers  
What customer personas are Utilization solving for? | Our customers fit the [buyer persona](https://handbook.gitlab.com/handbook/marketing/brand-and-product-marketing/product-and-solution-marketing/roles-personas/buyer-persona/) and may play a different role in the decision-making and purchasing process depending on their company size and their role.  
What customer segment is Utilization focused on? | - For SMB and mid-market companies: [The application development manager](https://handbook.gitlab.com/handbook/marketing/brand-and-product-marketing/product-and-solution-marketing/roles-personas/buyer-persona/#app-dev-avery) needs to have visibility into usage across their teams and be able to control usage in a way that fits their company preferences/processes/budget.   
- For large or enterprise company: [The release and change management director](https://handbook.gitlab.com/handbook/marketing/brand-and-product-marketing/product-and-solution-marketing/roles-personas/buyer-persona/#release-rory) is concerned with accurate billing and being able to make purchasing decisions based on usage information.  
What internal teams does Utilization serve? | - [Support](https://handbook.gitlab.com/handbook/support/)   
- [Customer Success](https://handbook.gitlab.com/handbook/customer-success/)   
- [Sales](https://handbook.gitlab.com/handbook/sales/)  
What is the Utilization group not responsible for? | The Utilization Group relies on calculations provided by other teams as part of building the right reporting and visualization for customers and admins. However, Utilization is not responsible for the collection or raw calculations of this underlying data. Specifically, Utilization relies on Enablement teams to provide accurate data around things such as:   
1. Project-level storage calculations (git repo + git LFS)  
2. Namespace storage calculation: git repo, LFS, artifacts, container registry, etc.   
3. Compute minutes  
[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/fulfillment/utilization/index.html.md) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/fulfillment/utilization/index.html.md)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Ffulfillment%2Futilization%2F&_biz_t=1773331971012&_biz_i=%0AGroup%20Direction%20-%20Utilization%0A%7C%0AGitLab%0A&_biz_n=92&rnd=49990&cdn_o=a&_biz_z=1773331971137)
suggested results