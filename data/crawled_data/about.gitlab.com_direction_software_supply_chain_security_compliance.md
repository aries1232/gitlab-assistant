#  Group Direction - Compliance 
  1. You are here:
  2. [GitLab Direction](https://about.gitlab.com/direction/)
  3. [Product Stage Direction - Software Supply Chain Security](https://about.gitlab.com/direction/software_supply_chain_security/)
  4. Group Direction - Compliance


The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
  * [Compliance](https://about.gitlab.com/direction/software_supply_chain_security/compliance/#compliance)
  * [Overview](https://about.gitlab.com/direction/software_supply_chain_security/compliance/#overview)
  * [Company Vision](https://about.gitlab.com/direction/software_supply_chain_security/compliance/#company-vision)
  * [Company Guiding Principle](https://about.gitlab.com/direction/software_supply_chain_security/compliance/#company-guiding-principle)
  * [Software Supply Chain Security Stage vision](https://about.gitlab.com/direction/software_supply_chain_security/compliance/#software-supply-chain-security-stage-vision)
  * [Compliance Group Mission](https://about.gitlab.com/direction/software_supply_chain_security/compliance/#compliance-group-mission)
    * [Key definitions of terms from the mission statement](https://about.gitlab.com/direction/software_supply_chain_security/compliance/#key-definitions-of-terms-from-the-mission-statement)
    * [What does compliance visibility of checks, violations and audit events mean?](https://about.gitlab.com/direction/software_supply_chain_security/compliance/#what-does-compliance-visibility-of-checks-violations-and-audit-events-mean)
    * [What is the customer problem or opportunity behind the mission?](https://about.gitlab.com/direction/software_supply_chain_security/compliance/#what-is-the-customer-problem-or-opportunity-behind-the-mission)
  * [How can we achieve our mission?](https://about.gitlab.com/direction/software_supply_chain_security/compliance/#how-can-we-achieve-our-mission)
    * [Personas we work with](https://about.gitlab.com/direction/software_supply_chain_security/compliance/#personas-we-work-with)
  * [How we approach problems](https://about.gitlab.com/direction/software_supply_chain_security/compliance/#how-we-approach-problems)
    * [Categories we focus on](https://about.gitlab.com/direction/software_supply_chain_security/compliance/#categories-we-focus-on)
  * [What are our priorities?](https://about.gitlab.com/direction/software_supply_chain_security/compliance/#what-are-our-priorities)
  * [Out of scope](https://about.gitlab.com/direction/software_supply_chain_security/compliance/#out-of-scope)


## Compliance[](https://about.gitlab.com/direction/software_supply_chain_security/compliance/#compliance)
|   
---|---  
Stage | [Software Supply Chain Security](https://about.gitlab.com/direction/software_supply_chain_security/)  
Maturity | [Minimal](https://about.gitlab.com/direction/#maturity)  
Content Last Updated | `2024-04-22`  
**NOTE** Please watch this [video](https://www.youtube.com/watch?v=5Tv4RGj-msw) explaining the mission & vision of the Compliance group
## Overview[](https://about.gitlab.com/direction/software_supply_chain_security/compliance/#overview)
Compliance is a [group](https://handbook.gitlab.com/handbook/product/categories/#compliance-group) in the Software Supply Chain Security stage. It describes high-level goals and direction for our group. Check out the [Software Supply Chain Security section](https://about.gitlab.com/direction/software_supply_chain_security/) page to see what the rest of our stage is working on, how we fit in, and our individual category pages to get fine-grained details.
## Company Vision[](https://about.gitlab.com/direction/software_supply_chain_security/compliance/#company-vision)
**NOTE** : Please visit this [link](https://handbook.gitlab.com/handbook/company/vision/)
Our vision in the next 10 years is to deliver on not just being a DevSecOps platform but to be an AllOps platform - which means being a single application for all R&D. To do this, we will invest in developing best-in-class features in areas such as security and compliance.
## Company Guiding Principle[](https://about.gitlab.com/direction/software_supply_chain_security/compliance/#company-guiding-principle)
**NOTE** Please visit this [link](https://about.gitlab.com/direction/#fiscal-year-guiding-principles) to read more about our fiscal year guiding principles respectively.
To help achieve the company vision, the company is focused on increasing the value of GitLab Ultimate by improving security and compliance functionality.
## Software Supply Chain Security Stage vision[](https://about.gitlab.com/direction/software_supply_chain_security/compliance/#software-supply-chain-security-stage-vision)
**NOTE** Please visit this [link](https://about.gitlab.com/direction/software_supply_chain_security/) to read more about the vision and goals of the Software Supply Chain Security stage
In line with the company vision and guiding principles, the Software Supply Chain Security stage provides the capabilities necessary to meet security and compliance requirements for organizations at any scale, from one project to tens of thousands of projects. These capabilities will not only ensure that compliance regulations are strictly followed in a way that they cannot be bypassed without the proper approvals, but will also serve as a connection point for a seamless workflow spanning across the DevSecOps lifecycle. It does this by, for example, centralizing security and compliance controls across GitLab, including merge request approvals, anomalous user activity, and anomalous pipeline/job activity.
## Compliance Group Mission[](https://about.gitlab.com/direction/software_supply_chain_security/compliance/#compliance-group-mission)
Increase the value of GitLab Ultimate by giving compliance managers best-in-class features within GitLab to achieve compliance **visibility** of **checks** , **violations** and **audit events** throughout the entire DevSecOps lifecycle.
### Key definitions of terms from the mission statement[](https://about.gitlab.com/direction/software_supply_chain_security/compliance/#key-definitions-of-terms-from-the-mission-statement)
![Compliance Management Anatomy](https://about.gitlab.com/images/direction/software_supply_chain_security/Compliance_Management_Anatomy.png)
Term | Definition  
---|---  
Visibility | To provide compliance managers a simple, quick and efficient way to view, find and organize compliance issues that surface via checks, violations or policies  
Checks | To help compliance managers easily identify if settings are properly enforced for a standard requirement (e.g. for SOC2, are we enforcing multiple users on each MR?)  
Violations | To help compliance managers evidence of adherence to the checks (e.g. a violation event is created if an MR request is merged without multiple approvers)  
Audit events | To help compliance managers identify and capture the most important user-driven events within GitLab, making that data easily available (via APIs, webhooks, and exportable reports), and providing a reasonable duration of storage for the data that follows compliance requirements (7 years)  
### What does compliance visibility of checks, violations and audit events mean?[](https://about.gitlab.com/direction/software_supply_chain_security/compliance/#what-does-compliance-visibility-of-checks-violations-and-audit-events-mean)
At GitLab, we view the visibility of compliance under 3 prongs:
  * Checks to help us validate settings are properly enabled;
  * Violation events provide evidence of compliance; and
  * Audit events for the most critical and sensitive types of actions inside GitLab allows for a detailed record of what happened, when it happened, and who did it.


The combination of all 3 prongs will give compliance users a way to understand their compliance posture, to generate reports for auditors, as well as to create their own tooling and automation based on their events.
For example, let us say there is a requirement that every MR must be approved by two users, and the approvers must not be the author or committer of the MR:
  * A requirement is based on an overarching framework or standard that organizations are legally bound to adhere to and apply to the DevSecOps lifecycle. In this case, the requirement is that every MR must be approved by two users;
  * A check identifies the project setting that is applied as a method or way to adhere with the particular requirement, such as confirming project settings are enabled to require multiple approvers on every MR, and to block MR authors from approving their own MRs;
  * A violation event will occur if the MR with fewer than 2 approvers is merged or if an MR author approved their own MR. This violation is captured at the time of the merge as an event and stored in GitLab compliance reporting; and
  * An audit event is surfaced as evidence of a user driven action that relates to the particular check and/or violation that has just occurred, for example a user event is captured that an MR has been raised and approved by the author.


### What is the customer problem or opportunity behind the mission?[](https://about.gitlab.com/direction/software_supply_chain_security/compliance/#what-is-the-customer-problem-or-opportunity-behind-the-mission)
Customers deal with many different challenges in compliance beyond GitLab. Governance, risk and compliance (GRC) describes the broader compliance space. There are many GRC tools that already exist today to help organizations understand risk and meet compliance requirements broadly across the organization. This includes multiple functional areas such as physical security; availability of services; and operations and people management.
Our opportunity is to focus on the areas where compliance and risk management meet up with the DevSecOps lifecycle. For many of our customers, they depend on the software applications they are building and maintaining, e.g. financial applications, healthcare software, telecommunications and government agencies. Disruption to their production apps or vulnerabilities that occur in the process of building them pose a great risk to their businesses. We want to empower customers and build confidence in GitLab as the only DevSecOps tool that truly addresses compliance. This strengthens our position in the market and solves real customer pain points.
## How can we achieve our mission?[](https://about.gitlab.com/direction/software_supply_chain_security/compliance/#how-can-we-achieve-our-mission)
To achieve our group mission, we will be focusing on the following ways to help our customers achieve compliance in the DevSecOps lifecycle:
  1. Provide visibility to compliance users at each step of the lifecycle.
  2. Help users understand where risks are that align with their business requirements (e.g. internal or external objectives).
  3. Give users reporting and data to prove compliance with internal and external auditors.
  4. Help users map requirements and controls to relevant standards and frameworks.
  5. Make the experience more intuitive - simpler to onboard and simpler to manage.
  6. Bring more compliance and security personas into GitLab.


### Personas we work with[](https://about.gitlab.com/direction/software_supply_chain_security/compliance/#personas-we-work-with)
[Cameron](https://handbook.gitlab.com/handbook/product/personas/#cameron-compliance-manager), the Compliance Manager, is one of our key personas we focus on. Cameron has many different jobs, such as those listed above, and we want to ensure they can be effective in doing them and making those jobs easier.
We know that Compliance affects an entire organization when policies and business requirements are added. While not our primary personas, we focus on how our capabilities impact others, such as [Sasha](https://handbook.gitlab.com/handbook/product/personas/#sasha-software-developer), [Delaney](https://handbook.gitlab.com/handbook/product/personas/#delaney-development-team-lead), [Devon](https://handbook.gitlab.com/handbook/product/personas/#devon-devops-engineer). Our goal is to ensure those other personas are minimally impacted and can do their jobs while still remaining compliant with the organization's policies. Reducing the friction between the compliance needs of a business and team's needs to get work done will be a key way GitLab can add value for our users.
## How we approach problems[](https://about.gitlab.com/direction/software_supply_chain_security/compliance/#how-we-approach-problems)
The problems and use cases we focus on can be quite large, so it helps to break them down into smaller pieces. As a result we focus on discovering the most [minimal viable change](https://handbook.gitlab.com/handbook/values/#minimal-viable-change-mvc) possible that still solves a particular problem by trying ["boring solutions"](https://handbook.gitlab.com/handbook/values/#boring-solutions) first.
#### Categories we focus on[](https://about.gitlab.com/direction/software_supply_chain_security/compliance/#categories-we-focus-on)
  1. [Compliance Management](https://about.gitlab.com/direction/software_supply_chain_security/compliance/compliance-management)
  2. [Audit Events](https://about.gitlab.com/direction/software_supply_chain_security/compliance/audit-events)


## What are our priorities?[](https://about.gitlab.com/direction/software_supply_chain_security/compliance/#what-are-our-priorities)
Please view our [tactical priorities](https://about.gitlab.com/direction/software_supply_chain_security/compliance/tactical-priorities.html) here.
## Out of scope[](https://about.gitlab.com/direction/software_supply_chain_security/compliance/#out-of-scope)
The Compliance group does not undertake any initiative or solve any customer problems that relate to the **enforcement** of compliance across the DevSecOps lifecycle. For example, in terms of enforcement, policies help us manage controls globally, maintain separation of duties and serve as a technical mechanism for taking a requirement from a compliance objective and turning it into a control in GitLab to influence particular behaviour. Policies fall under the scope of the [Security Policies group](https://about.gitlab.com/direction/software_supply_chain_security/security_policies/) in GitLab.
[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/software_supply_chain_security/compliance/index.html.md.erb) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/software_supply_chain_security/compliance/index.html.md.erb)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fsoftware_supply_chain_security%2Fcompliance%2F&_biz_t=1773332090789&_biz_i=%0AGroup%20Direction%20-%20Compliance%0A%7C%0AGitLab%0A&_biz_n=118&rnd=761735&cdn_o=a&_biz_z=1773332090926)
suggested results