# Software Supply Chain Security Sub-department
The Software Supply Chain Security sub-department teams are the engineering teams in the [Software Supply Chain Security Stage](https://about.gitlab.com/direction/software_supply_chain_security/) of the product.
## Vision[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/#vision)
To support GitLab’s product vision through alignment with the [Software Supply Chain Security stage](https://about.gitlab.com/direction/software_supply_chain_security/) product direction.
## SSCS Charter[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/#sscs-charter)
**Software Supply Chain Security (SSCS) Stage Team Charter**
### Our Mission[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/#our-mission)
Protect GitLab customers from supply chain attacks while maintaining developer velocity.
We secure the entire software development lifecycle - from code commit to production deployment - by ensuring every artifact is verified, every access is authorized, and every risk is visible.
### What We Do[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/#what-we-do)
SSCS secures three critical surfaces:
#### 1. Build & Pipeline Security[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/#1-build--pipeline-security)
  * Ensuring artifacts are verifiably built from trusted source code
  * SLSA compliance and artifact attestation
  * Runner security and isolation
  * Secrets management
  * Pipeline integrity


#### 2. Identity & Access Management[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/#2-identity--access-management)
  * Controlling who can do what across the platform
  * Authentication (how users prove identity)
  * Authorization (what authenticated users can do)
  * Zero-trust architecture


#### 3. Compliance & Policy[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/#3-compliance--policy)
  * Making security measurable and auditable
  * Security policies as code
  * Compliance evidence generation
  * Audit trails and visibility


### How Our Priorities Align with GitLab Executive Priorities[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/#how-our-priorities-align-with-gitlab-executive-priorities)
We maintain a 30% capacity buffer for unplanned cross-functional work that supports company-level priorities. This allows us to respond to company-level priorities such as:
  * **GitLab Duo & AI** - Anything blocking DAP or AI security
  * **Protocells** - Authentication/authorization foundations for Cells architecture


### Our Top 3 Priorities[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/#our-top-3-priorities)
#### Priority 1: Build a strong security foundation for AuthN/AuthZ[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/#priority-1-build-a-strong-security-foundation-for-authnauthz)
**Objective:** Reduce security incidents **Why it matters:** Every incident erodes customer trust and drains engineering capacity.
**What we’re doing:**
  * Authentication consolidation (CYCP)
  * Token security improvements
  * Critical auditing gaps


#### Priority 2: Engineering Excellence[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/#priority-2-engineering-excellence)
**Objective:** Become a high-performing, predictable engineering organization **Why it matters:** We can’t deliver strategic value if we’re drowning in firefighting and support escalations.
**What we’re doing:**
  * Reduce support escalation rate from 30% to <15%
  * Improve delivery confidence (currently 60-70% → 85%+)


#### Priority 3: Supply Chain Leadership[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/#priority-3-supply-chain-leadership)
**Objective:** Establish GitLab as the most trusted supply chain security platform **Why it matters:** Supply chain attacks are increasing YoY. Customers like GovTech and enterprises demand verifiable security.
**What we’re doing:**
  * SLSA Level 3 compliance
  * Runner identity and verification
  * End-to-end artifacts and containers attestation
  * Supply chain visibility dashboard


### How Our Top 3 Priorities Enable Strategic Cross-Functional Work[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/#how-our-top-3-priorities-enable-strategic-cross-functional-work)
Our priorities aren’t just about internal SSCS goals—they’re designed to enable the strategic cross-functional work that supports company objectives.
#### Priority 1: Build a strong foundation → Enables Platform Capabilities[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/#priority-1-build-a-strong-foundation--enables-platform-capabilities)
Code Yellow/Purple (CYCP) authentication consolidation and security architecture enables:
  * Workload Identity federation
  * OAuth for ProtoCells - Authentication foundation that ProtoCells depends on
  * Fine grained access controls for customers
  * Agentic authentication built on secure machine identities


#### Priority 2: Engineering Excellence → Creates Capacity for Unplanned Work[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/#priority-2-engineering-excellence--creates-capacity-for-unplanned-work)
Reducing support burden, improving delivery confidence, protecting capacity for quality enables:
  * Faster response time - Can pivot to urgent requests without breaking commitments
  * Higher quality - Strategic work doesn’t create technical debt that haunts us
  * Better estimation - Know true capacity available for unplanned work
  * Sustainable pace - Team doesn’t burn out from constant context switching


#### Priority 3: Supply Chain Leadership → Differentiates in Enterprise Deals[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/#priority-3-supply-chain-leadership--differentiates-in-enterprise-deals)
SLSA compliance, runner security, artifacts attestation, threat analysis, advanced compliance features enables:
  * Enterprise credibility - SLSA certification enables deals that fund strategic work
  * Compliance foundation - Security architecture that DAP and ProtoCells inherit


### AI Security: Our Newest Frontier[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/#ai-security-our-newest-frontier)
#### Why AI Security Matters[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/#why-ai-security-matters)
AI features (GitLab Duo, AI agents, code generation) are fundamentally changing our security model:
  * AI agents act on behalf of users - requiring composite identity
  * AI generates code and modifies repositories - requiring attribution and auditability
  * AI accesses customer data - requiring privacy and compliance controls
  * AI crosses organizational boundaries - requiring robust authorization


The challenge: We’re securing AI features while simultaneously building the platform capabilities they need. This creates unavoidable dependencies and unplanned work.
### How We Work[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/#how-we-work)
#### Resource Allocation Model[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/#resource-allocation-model)
  * **70%** - Planned work
  * **30%** - Unplanned work


Unplanned work is not the exception—it’s part of the job. Cross-functional dependencies, urgent customer needs, security issues, and tech debt from re-orgs consume 30% of capacity in typical milestones. We budget for this reality rather than pretending it doesn’t exist.
#### Managing Unplanned Work[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/#managing-unplanned-work)
The 30% unplanned budget includes:
  * Cross-functional dependencies (Protocells, Dedicated, DAP, etc.)
  * Security incidents and vulnerability fixes
  * Customer escalations and support
  * Tech debt from re-orgs and domain transfers
  * Infrastructure issues requiring urgent attention


#### Visibility & Accountability[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/#visibility--accountability)
**Unplanned Work Log** (updated weekly):
  * What unplanned work arrived
  * Capacity consumed (eng-weeks)
  * What got delayed as a result
  * Link to the relevant request


This visibility creates accountability and helps justify pushback on future requests.
## Groups[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/#groups)
  * [Authentication](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/authentication/)
  * [Authorization](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/authorization/)
  * [Compliance](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/compliance/)
  * [Pipeline Security](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/pipeline-security/)


### Product Documentation Links[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/#product-documentation-links)
  * [Authentication and Authorization](https://docs.gitlab.com/administration/auth/)
  * [Compliance Center](https://docs.gitlab.com/user/compliance/compliance_center/)
  * [Security glossary](https://docs.gitlab.com/ee/user/application_security/terminology/)
  * [Pipeline Security](https://docs.gitlab.com/ee/ci/pipelines/pipeline_security.html)


## All Team Members[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/#all-team-members)
### Authentication[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/#authentication)
Name | Role  
---|---  
[![Adil Farrukh](https://about.gitlab.com/images/team/adilfarrukh-crop.jpg)Adil Farrukh](https://handbook.gitlab.com/handbook/company/team/#adilfarrukh) |  [Engineering Manager](https://handbook.gitlab.com/job-families/engineering/development/management/fullstack-manager/), Software Supply Chain Security:Authentication  
[![Aleksei Lipniagov](https://about.gitlab.com/images/team/alekseilipniagov-crop.jpg)Aleksei Lipniagov](https://handbook.gitlab.com/handbook/company/team/#alipniagov) |  [Senior Backend Engineer](https://handbook.gitlab.com/job-families/engineering/development/backend/), Software Supply Chain Security:Authentication  
[![Andrew Evans](https://about.gitlab.com/images/team/andrewevans-crop.jpg)Andrew Evans](https://handbook.gitlab.com/handbook/company/team/#atevans) |  [Senior Backend Engineer](https://handbook.gitlab.com/job-families/engineering/development/backend/), Software Supply Chain Security:Authentication  
[![Bogdan Denkovych](https://about.gitlab.com/images/team/bdenkovych-crop.jpg)Bogdan Denkovych](https://handbook.gitlab.com/handbook/company/team/#bdenkovych) |  [Senior Backend Engineer](https://handbook.gitlab.com/job-families/engineering/development/backend/), Software Supply Chain Security:Authentication  
[![Daniele Bracciani](https://about.gitlab.com/images/gitlab-logo-extra-whitespace.png)Daniele Bracciani](https://handbook.gitlab.com/handbook/company/team/#daniele-gitlab) |  [Senior Backend Engineer](https://handbook.gitlab.com/job-families/engineering/backend-engineer/), Software Supply Chain Security:Authentication  
[![Eduardo Sanz-Garcia](https://about.gitlab.com/images/team/eduardosanz-crop.jpg)Eduardo Sanz-Garcia](https://handbook.gitlab.com/handbook/company/team/#eduardosanz) |  [Senior Frontend Engineer](https://handbook.gitlab.com/job-families/engineering/development/frontend/senior/), Software Supply Chain Security:Authentication  
[![Hakeem Abdul-Razak](https://about.gitlab.com/images/team/habdul-razak-crop.jpg)Hakeem Abdul-Razak](https://handbook.gitlab.com/handbook/company/team/#habdul-razak) |  [Associate Backend Engineer](https://handbook.gitlab.com/job-families/engineering/development/backend/associate/), Software Supply Chain Security:Authentication  
[![Imre Farkas](https://about.gitlab.com/images/team/imrefarkas-crop.jpg)Imre Farkas](https://handbook.gitlab.com/handbook/company/team/#ifarkas) |  [Staff Backend Engineer](https://handbook.gitlab.com/job-families/engineering/development/backend/), Software Supply Chain Security:Authentication  
[![Matthias Käppler](https://about.gitlab.com/images/team/matthiaskaeppler-crop.jpg)Matthias Käppler](https://handbook.gitlab.com/handbook/company/team/#mkaeppler) |  [Staff Backend Engineer](https://handbook.gitlab.com/job-families/engineering/development/backend/), Software Supply Chain Security:Authentication  
[![Shilpa Kundapur](https://about.gitlab.com/images/team/shilpakundapur-crop.jpg)Shilpa Kundapur](https://handbook.gitlab.com/handbook/company/team/#skundapur) |  [Staff Backend Engineer](https://handbook.gitlab.com/job-families/engineering/backend-engineer/), Software Supply Chain Security:Authentication  
[![Smriti Garg](https://about.gitlab.com/images/team/smriti_pic_minified-crop.jpg)Smriti Garg](https://handbook.gitlab.com/handbook/company/team/#sgarg_gitlab) |  [Senior Backend Engineer](https://handbook.gitlab.com/job-families/engineering/backend-engineer/), Software Supply Chain Security:Authentication  
[![Aboobacker MK](https://about.gitlab.com/images/team/aboobacker-crop.jpg)Aboobacker MK](https://handbook.gitlab.com/handbook/company/team/#tachyons-gitlab) |  [Senior Backend Engineer](https://handbook.gitlab.com/job-families/engineering/development/backend/senior/), Software Supply Chain Security:Authentication  
### Authorization[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/#authorization)
Name | Role  
---|---  
[![Ajay Thomas](https://about.gitlab.com/images/team/ajaythomas-crop.jpg)Ajay Thomas](https://handbook.gitlab.com/handbook/company/team/#ajaythomasinc) |  [Engineering Manager](https://handbook.gitlab.com/job-families/engineering/development/management/engineering-manager/), Software Supply Chain Security:Authorization  
[![Ayush Billore](https://about.gitlab.com/images/team/ayush-crop.jpg)Ayush Billore](https://handbook.gitlab.com/handbook/company/team/#abime) |  [Backend Engineer](https://handbook.gitlab.com/job-families/engineering/backend-engineer/), Software Supply Chain Security:Authorization  
[![Alex Buijs](https://about.gitlab.com/images/team/alexbuijs-crop.jpg)Alex Buijs](https://handbook.gitlab.com/handbook/company/team/#alexbuijs) |  [Senior Fullstack Engineer](https://handbook.gitlab.com/job-families/engineering/development/fullstack/), Software Supply Chain Security:Authorization  
[![Daniel Tian](https://about.gitlab.com/images/team/danieltian-crop.jpg)Daniel Tian](https://handbook.gitlab.com/handbook/company/team/#dftian) | [Senior Frontend Engineer, Software Supply Chain Security:Authorization](https://handbook.gitlab.com/job-families/engineering/development/frontend/#senior-frontend-engineer)  
[![Diane Russel](https://about.gitlab.com/images/team/dianerussel-crop.jpg)Diane Russel](https://handbook.gitlab.com/handbook/company/team/#dlrussel) |  [Backend Engineer](https://handbook.gitlab.com/job-families/engineering/backend-engineer/), Software Supply Chain Security:Authorization  
[![Eugie Limpin](https://about.gitlab.com/images/team/eugielimpin-crop.jpg)Eugie Limpin](https://handbook.gitlab.com/handbook/company/team/#eugielimpin) |  [Senior Fullstack Engineer](https://handbook.gitlab.com/job-families/engineering/development/fullstack/), Software Supply Chain Security:Authorization  
[![Hinam Mehra](https://about.gitlab.com/images/team/HinamMehra-crop.jpg)Hinam Mehra](https://handbook.gitlab.com/handbook/company/team/#hmehra) |  [Senior Fullstack Engineer](https://handbook.gitlab.com/job-families/engineering/development/fullstack/), Software Supply Chain Security:Authorization  
[![Ian Anderson](https://about.gitlab.com/images/gitlab-logo-extra-whitespace.png)Ian Anderson](https://handbook.gitlab.com/handbook/company/team/#imand3r) |  [Staff Backend Engineer](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/), Software Supply Chain Security:Authorization  
[![Jay Swain](https://about.gitlab.com/images/team/jayswain-crop.jpg)Jay Swain](https://handbook.gitlab.com/handbook/company/team/#jayswain) | [Senior Backend Engineer, Software Supply Chain Security:Authorization](https://handbook.gitlab.com/job-families/engineering/development/backend/senior/)  
[![Matthew MacRae-Bovell](https://about.gitlab.com/images/team/mmacrae-bovell-crop.jpg)Matthew MacRae-Bovell](https://handbook.gitlab.com/handbook/company/team/#mmacrae-bovell) |  [Backend Engineer](https://handbook.gitlab.com/job-families/engineering/backend-engineer/), Software Supply Chain Security:Authorization  
### Compliance[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/#compliance)
Name | Role  
---|---  
[![Nathan Rosandich](https://about.gitlab.com/images/team/nrosandich-crop.jpg)Nathan Rosandich](https://handbook.gitlab.com/handbook/company/team/#nrosandich) |  [Engineering Manager](https://handbook.gitlab.com/job-families/engineering/development/management/engineering-manager/), Software Supply Chain Security:Compliance  
[![Andrew Jung](https://about.gitlab.com/images/team/andrewjung-crop.jpg)Andrew Jung](https://handbook.gitlab.com/handbook/company/team/#andrewjung) |  [Backend Engineer](https://handbook.gitlab.com/job-families/engineering/development/backend/), Software Supply Chain Security:Compliance  
[![Harsimar Sandhu](https://about.gitlab.com/images/team/harsimarsandhu-crop.jpg)Harsimar Sandhu](https://handbook.gitlab.com/handbook/company/team/#harsimarsandhu) |  [Senior Backend Engineer](https://handbook.gitlab.com/job-families/engineering/development/backend/), Software Supply Chain Security:Compliance  
[![Hitesh Raghuvanshi](https://about.gitlab.com/images/team/hiteshraghuvanshi-crop.jpg)Hitesh Raghuvanshi](https://handbook.gitlab.com/handbook/company/team/#hraghuvanshi) |  [Senior Backend Engineer](https://handbook.gitlab.com/job-families/engineering/development/backend/), Software Supply Chain Security:Compliance  
[![Huzaifa Iftikhar](https://about.gitlab.com/images/team/huzaifaiftikhar-crop.jpg)Huzaifa Iftikhar](https://handbook.gitlab.com/handbook/company/team/#huzaifaiftikhar1) |  [Senior Backend Engineer](https://handbook.gitlab.com/job-families/engineering/development/backend/), Software Supply Chain Security:Compliance  
[![Illya Klymov](https://about.gitlab.com/images/team/illyaklymov-crop.jpg)Illya Klymov](https://handbook.gitlab.com/handbook/company/team/#xanf) |  [Staff Frontend Engineer](https://handbook.gitlab.com/job-families/engineering/development/frontend/), Software Supply Chain Security:Compliance  
[![Jean van der Walt](https://about.gitlab.com/images/team/jeanvanderwalt-crop.jpg)Jean van der Walt](https://handbook.gitlab.com/handbook/company/team/#jeanvdw) |  [Staff Backend Engineer](https://handbook.gitlab.com/job-families/engineering/development/backend/), Software Supply Chain Security:Compliance  
[![Sam Figueroa](https://about.gitlab.com/images/team/Sam-Figueroa-crop.jpg)Sam Figueroa](https://handbook.gitlab.com/handbook/company/team/#samfigueroa) |  [Fullstack Engineer](https://handbook.gitlab.com/job-families/engineering/development/fullstack/), Software Supply Chain Security:Compliance  
[![Scott Hampton](https://about.gitlab.com/images/team/scotthampton-crop.jpg)Scott Hampton](https://handbook.gitlab.com/handbook/company/team/#shampton) | [Senior Frontend Engineer, Software Supply Chain Security:Compliance](https://handbook.gitlab.com/job-families/engineering/development/frontend/)  
### Pipeline Security[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/#pipeline-security)
Name | Role  
---|---  
## Stable Counterparts[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/#stable-counterparts)
The following members of other functional teams are our stable counterparts:
Name | Role  
---|---  
[![Adil Farrukh](https://about.gitlab.com/images/team/adilfarrukh-crop.jpg)Adil Farrukh](https://handbook.gitlab.com/handbook/company/team/#adilfarrukh) |  [Engineering Manager](https://handbook.gitlab.com/job-families/engineering/development/management/fullstack-manager/), Software Supply Chain Security:Authentication  
[![Aaron Huntsman](https://about.gitlab.com/images/team/aaronhuntsman-crop.jpg)Aaron Huntsman](https://handbook.gitlab.com/handbook/company/team/#ahuntsman) |  [Senior Backend Engineer](https://handbook.gitlab.com/job-families/engineering/development/backend/), Software Supply Chain Security:Pipeline Security  
[![Ahmad Hussein](https://about.gitlab.com/images/team/ahmadhussein-crop.jpg)Ahmad Hussein](https://handbook.gitlab.com/handbook/company/team/#ahuss7) |  [Fullstack Engineer](https://handbook.gitlab.com/job-families/engineering/development/fullstack/intermediate-fullstack-engineer/), Software Supply Chain Security:Pipeline Security  
[![Ajay Thomas](https://about.gitlab.com/images/team/ajaythomas-crop.jpg)Ajay Thomas](https://handbook.gitlab.com/handbook/company/team/#ajaythomasinc) |  [Engineering Manager](https://handbook.gitlab.com/job-families/engineering/development/management/engineering-manager/), Software Supply Chain Security:Authorization  
[![Camellia X. Yang](https://about.gitlab.com/images/team/camelliaxueyiyang-crop.jpg)Camellia X. Yang](https://handbook.gitlab.com/handbook/company/team/#camx) |  [Senior Product Designer](https://handbook.gitlab.com/job-families/product/product-designer/#senior-product-designer) Software Supply Chain Security:Compliance and Security Risk Management:Security Policies  
[![Dmytro Biryukov](https://about.gitlab.com/images/team/dbiryukov-crop.jpg)Dmytro Biryukov](https://handbook.gitlab.com/handbook/company/team/#dbiryukov) | [Senior Backend Engineer, Software Supply Chain Security:Pipeline Security](https://handbook.gitlab.com/job-families/engineering/development/backend/)  
[![Erick Bajao](https://about.gitlab.com/images/team/erickbajao-crop.jpg)Erick Bajao](https://handbook.gitlab.com/handbook/company/team/#iamricecake) | [Senior Backend Engineer, Software Supply Chain Security:Pipeline Security](https://handbook.gitlab.com/job-families/engineering/development/backend/)  
[![Fabien Catteau](https://about.gitlab.com/images/team/fabiencatteau-crop.jpg)Fabien Catteau](https://handbook.gitlab.com/handbook/company/team/#fcatteau) |  [Staff Backend Engineer](https://handbook.gitlab.com/job-families/engineering/development/backend/#staff-backend-engineer), Software Supply Chain Security:Pipeline Security  
[![Jayakrishnan Mallissery](https://about.gitlab.com/images/team/jayakrishnanmallissery-crop.jpg)Jayakrishnan Mallissery](https://handbook.gitlab.com/handbook/company/team/#jmallissery) | [Backend Engineer, Software Supply Chain Security:Pipeline Security](https://handbook.gitlab.com/job-families/engineering/development/backend/)  
[![Joe Randazzo](https://about.gitlab.com/images/team/joerandazzo-crop.jpg)Joe Randazzo](https://handbook.gitlab.com/handbook/company/team/#jrandazzo) |  [Product Manager](https://handbook.gitlab.com/job-families/product/product-manager/), Software Supply Chain Security:Secrets Manager  
[![Ian Khor](https://about.gitlab.com/images/team/iankhor-crop.jpg)Ian Khor](https://handbook.gitlab.com/handbook/company/team/#khornergit) |  [Product Manager](https://handbook.gitlab.com/job-families/product/product-manager/), Software Supply Chain Security:Compliance  
[![Mireya Andres](https://about.gitlab.com/images/team/mireya-andres-crop.jpg)Mireya Andres](https://handbook.gitlab.com/handbook/company/team/#mgandres) | [Senior Frontend Engineer, Software Supply Chain Security:Pipeline Security](https://handbook.gitlab.com/job-families/engineering/development/frontend/)  
[![Nathan Rosandich](https://about.gitlab.com/images/team/nrosandich-crop.jpg)Nathan Rosandich](https://handbook.gitlab.com/handbook/company/team/#nrosandich) |  [Engineering Manager](https://handbook.gitlab.com/job-families/engineering/development/management/engineering-manager/), Software Supply Chain Security:Compliance  
[![Sam Joan Roque-Worcel](https://about.gitlab.com/images/team/samjoanroqueworcel-crop.jpg)Sam Joan Roque-Worcel](https://handbook.gitlab.com/handbook/company/team/#sroque-worcel) |  [Senior Backend Engineer](https://handbook.gitlab.com/job-families/engineering/development/backend/), Software Supply Chain Security:Pipeline Security  
## Software Supply Chain Security staff meeting[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/#software-supply-chain-security-staff-meeting)
The Software Supply Chain Security stage engineering department leaders meet weekly to discuss stage and group topics in the `Software Supply Chain Security staff meeting`. This meeting is open to all team members and is published on the Software Supply Chain Security stage calendar.
Meetings have an agenda and are async-first, where the aim is to resolve discussions async and leave time in the meeting to deep dive into topics that require more discussion.
We use the [Software Supply Chain Security Sub-department Board](https://gitlab.com/gitlab-com/software_supply_chain_security-sub-department/-/boards/4833026) to better organize our discussions.
### Weekly updates[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/#weekly-updates)
The Software Supply Chain Security development teams provide [weekly status updates](https://gitlab.com/groups/gitlab-com/-/epics/2126) using an issue template and CI scheduled job. As priorities change, engineering managers update the [template](https://gitlab.com/gitlab-com/software_supply_chain_security-sub-department/-/blob/main/.gitlab/issue_templates/sscs_stage_weekly_update.md) to include areas of interest such as priorities, opportunities, risks, and security and availability concerns. The updates are GitLab internal.
### Quarterly review updates[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/#quarterly-review-updates)
Every quarter, an engineering manager for each group in the Software Supply Chain Security Sub-department prepares the quarterly review update using the issue template and records approximately 5 minutes to summarize the last quarter from the engineering perspective and present a high-level plan for the group for the next one to respond to quarterly Product strategy and explain our goals for next quarter.
We aim to foster collaboration and communication between engineering managers in the Software Supply Chain Security Sub-department, align groups on product priorities for the next quarter, and celebrate our successes together.
Quarterly review update template can be found [here](https://gitlab.com/gitlab-com/software_supply_chain_security-sub-department/-/blob/main/.gitlab/issue_templates/sscs_stage_quarterly_review.md)).
### PTO[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/#pto)
We follow the [Engineering process for taking time off](https://handbook.gitlab.com/handbook/engineering/#taking-time-off) and [GitLab team members Guide to Time Off](https://handbook.gitlab.com/handbook/people-group/time-off-and-absence/time-off-types/).
#### Engineering Leadership - PTO or unavailable[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/#engineering-leadership---pto-or-unavailable)
Team members should contact any Software Supply Chain Security Engineering Manager by mentioning in `#sd_sscs_engineering` or `#sscs-development-people-leaders` if they need management support for a problem that arises, such as a production incident or feature change lock, when their direct manager is not available. The Software Supply Chain Security manager can provide guidance and coordination to ensure that the team member receives the appropriate help.
Some people management tasks, including [Workday](https://theloop.gitlab.com/site/4455aa7f-24d9-41f2-b940-467b54962e4d/page/0fa19bf4-fd6a-41b9-9316-c2dcf3add854) and [Navan Expense](https://handbook.gitlab.com/handbook/business-technology/enterprise-applications/guides/navan-expense-guide/), may require for escalation or delegation.
## Skills[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/#skills)
Because we have a wide range of domains to cover, it requires a lot of different expertise and skills:
Technology skills | Areas of interest  
---|---  
Ruby on Rails | Backend development  
Go | Backend development  
Vue, Vuex | Frontend development  
GraphQL | _Various_  
SQL (PostgreSQL) | _Various_  
Docker/Kubernetes | Threat Detection  
[New Auth Claude Expert](https://claude.ai/project/019a0ff4-0efe-7373-af96-82a23aaac734) | New Auth Design  
## Everyone can contribute[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/#everyone-can-contribute)
At GitLab our goal is that [everyone can contribute](https://handbook.gitlab.com/handbook/company/mission/#contribute-to-gitlab-application). This applies to GitLab team members and the wider community through community contributions. We welcome contributions to any and all features, but recognize that first time contributors may prefer to start with smaller features. To support this we maintain a list of `quick wins` that may be more suitable for first time contributors, and contributors new to the domains in Software Supply Chain Security.
If the contributor needs an EE license, we can point towards the [Contributing to the GitLab Enterprise Edition (EE)](https://handbook.gitlab.com/handbook/marketing/developer-relations/engineering/community-contributors-workflows/#contributing-to-the-gitlab-enterprise-edition-ee) section on the Community contributors workflows page.
## Testing[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/#testing)
During the planning phase of a milestone, the EM for each group will create a new issue using the template in [epic](https://gitlab.com/groups/gitlab-org/quality/quality-engineering/-/epics/70), for any major new features and tag Software Engineer in Test from Software Supply Chain Security. SETs from Test Engineering and EMs can periodically review/discuss the list of open issues, and add appropriate priority labels.
The intent of [shifting left and testing at the right level](https://docs.gitlab.com/ee/development/testing_guide/testing_levels.html#how-to-test-at-the-correct-level) is that teams are responsible for testing and to have engineers doing the feature coverage reviews and adding specs or E2E test as needed. The reason for including the SET is to give oversight across the groups and provide guidance/support. If the SET has capacity then they can contribute as needed, using the priority labels, but this is not the expectation.
## Links and resources[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/#links-and-resources)
  * Stage links 
    * Discussions and issues are located at [`gitlab-org/software-supply-chain-security`](https://gitlab.com/gitlab-org/software-supply-chain-security)
    * General Slack [#s_software-supply-chain-security](https://app.slack.com/client/T02592416/CFHGVJ06R)
    * Social channel [#sec-section-social](https://app.slack.com/client/T02592416/C01ACJRU5PH)
    * Engineering Slack [#sd_sscs_engineering](https://app.slack.com/client/T02592416/C040C6LNANB)
    * Software Supply Chain Security [Shared Calendar](https://calendar.google.com/calendar/embed?src=gitlab.com_ed6207uel78de0j1849vjjnb3k%40group.calendar.google.com&ctz=America%2FDetroit) (Calendar ID `gitlab.com_ed6207uel78de0j1849vjjnb3k@group.calendar.google.com`)
    * GitLab Managers: `@gitlab-org/software-supply-chain-security/managers`


### AI and Learning Resources[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/#ai-and-learning-resources)
  * [New Auth Expert Claude Project](https://claude.ai/project/019a0ff4-0efe-7373-af96-82a23aaac734) - AI expert for getting answers and information about the New Auth and Code Purple initiative, design, and progress 
    * **Note:** Access to this project requires organizational Claude access. Team members need to be part of the GitLab organization in Claude to access this project.


#### Example Prompts for New Auth Expert[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/#example-prompts-for-new-auth-expert)
**Architecture & Design**
  * “What is the GATE architecture and its L0/L1/L2 layers?”
  * “Explain the difference between TS (Topology Service) and IAM services”
  * “What are the key architectural decisions made for Code Purple?”
  * “Show me the 3-level architecture design”


**Timeline & Deliverables**
  * “What’s the delivery timeline for Code Yellow vs Code Purple?”
  * “What are the Q2/Q3 FY27 deliverables?”
  * “When will GATE be in production?”
  * “What’s the roadmap for token consolidation?”


**Token & Permissions**
  * “What’s the plan for granular Personal Access Token (PAT) permissions?”
  * “How will OAuth token permissions work?”
  * “Explain Workload Identity Federation timeline”
  * “What are the requirements for CI/CD job tokens?”


**Implementation Status**
  * “What POCs are currently in progress?”
  * “Which features are in scope vs out of scope for Code Purple?”
  * “What are the current blockers?”
  * “Show me the latest weekly status notes”


**Dependencies & Infrastructure**
  * “What infrastructure dependencies exist for GATE deployment?”
  * “How does this relate to the Cells architecture?”
  * “What database operations are needed?”
  * “What’s required for self-managed vs GitLab.com deployment?”


**Service Accounts & Machine Identity**
  * “How are service accounts being consolidated?”
  * “What’s the plan for machine identities?”
  * “When will service accounts be available on Free tier?”


**Specific Issues & Epics**
  * “Find GitLab issues related to granular PAT permissions”
  * “What epics are tracking Code Purple delivery?”
  * “Show me recent discussions about token scopes”


**Quick Status Checks**
  * “What’s the latest Code Purple status?”
  * “Are there any blockers this week?”
  * “What was decided in the most recent sync meeting?”


### Technical Documentation Links[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/#technical-documentation-links)
  * [End-to-end tests](https://gitlab.com/gitlab-org/gitlab/-/tree/master/qa/qa/specs/features/ee/browser_ui/10_govern)


* * *
#####  [Anti-Abuse Group](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/anti-abuse/)
The Anti-Abuse group creates controls to prevent abuse of the GitLab product
#####  [Authentication Group](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/authentication/)
SSCS:Authentication Mission Our mission is to empower GitLab system administrators with the toolkit …
#####  [Authorization Group](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/authorization/)
Planning Our Planning issues are the SSOT of what we’re working on now, and what we’re …
#####  [Compliance Group](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/compliance/)
Mission The Compliance group’s mission is to provide visibility into an organizations …
#####  [Software Supply Chain Security Tier 2 On Call](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/oncall/)
Welcome to the Software Supply Chain Security (SSCS) Tier 2 On-Call program! This documentation will …
#####  [Software Supply Chain Security:Pipeline Security Group](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/pipeline-security/)
The GitLab Software Supply Chain Security:Pipeline Security Group Handbook page
Last modified February 27, 2026: [Update Developer Relations contributor-success references to engineering (Sec/AI department section) (`68bb345d`)](https://gitlab.com/gitlab-com/content-sites/handbook/commit/68bb345d)
[ ](https://gitlab.com/gitlab-com/content-sites/handbook/blob/main/content/handbook/engineering/development/sec/software-supply-chain-security/_index.md) - [ ](https://gitlab.com/-/ide/project/gitlab-com/content-sites/handbook/edit/main/-/content/handbook/engineering/development/sec/software-supply-chain-security/_index.md) - please [contribute](https://handbook.gitlab.com/handbook/about/contributing/). [ ![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-sa/4.0/)