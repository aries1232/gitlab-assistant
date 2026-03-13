# Architecture
## Complexity at Scale[](https://handbook.gitlab.com/handbook/engineering/architecture/#complexity-at-scale)
As GitLab grows, through the introduction of new features and improvements on existing ones, so does its **complexity**. This effect is compounded by the care and feeding of a single codebase that supports the wide variety of environments in which it runs, from small self-managed instances to large installations such as GitLab.com. The company itself adds to this complexity from an organizational perspective: hundreds employees worldwide contribute in one way or another to both the product and the company, using GitLab.com on a daily basis to do their job. Teams members in Engineering are directly responsible for the codebase and its operation, for the infrastructure powering GitLab.com, and for the support of customers running self-managed instances. Likewise, team members in the Product organization chart the future of the product.
[Our values](https://handbook.gitlab.com/handbook/values/), coupled with strong know-how and unparalleled dedication, provide critical guidance to manage these complexities. At the same time, we have known for some time we are crossing a threshold in which **complexity at scale** , both technical and organizational, is playing a significant role. We know we need to fine-tune both our technical discipline (so we can integrate it across the organization) and our organizational amplification (so we can span and leverage the entire organization) to ensure we can continue to deliver on our values. In this context, we have been exploring the adoption of _Architecture_ or _Engineering Practice_ to help us in this regard.
## Architecture[](https://handbook.gitlab.com/handbook/engineering/architecture/#architecture)
Martin Fowler’s [Software Architecture Guide](https://martinfowler.com/architecture/) provides an excellent discussion on the notion of **Architecture** , and there is much to be learned from this and other sources. The question before us is, then, how to contextualize those learnings and apply them at GitLab.
Much like the rest of the software world, we have been wary of all the negative baggage that _Architecture_ implies, particularly as some of that baggage would seemingly fly in the face of our values. This is why we have taken the time to carefully consider what _Architecture_ means for us, and how to implement it in alignment with our values and at the scale that both the product and the company demand.
At GitLab, Architecture is not a dedicated role (i.e., no such title exists in the company). We understand _Architecture_ as a component of all technical roles, a set of **practices** to leverage the vast amount of experience distributed across the company, and a **workflow** to ensure we can continue to scale efficiently.
## Architecture at GitLab[](https://handbook.gitlab.com/handbook/engineering/architecture/#architecture-at-gitlab)
At GitLab, **Architecture** is a collaborative process. It is also:
  * A [catalog of **key abstractions**](https://handbook.gitlab.com/handbook/engineering/architecture/abstractions/) that defines the approved foundational technologies and patterns engineers must use, ensuring consistency and reducing complexity across the organization.
  * A [collection of practices](https://handbook.gitlab.com/handbook/engineering/architecture/practice/) that provide technical frameworks to **guide** (rather than dictate) our thinking, design, and discussions so we can _iterate_ quickly and deliver _results_. These include the [Scalability Practice](https://handbook.gitlab.com/handbook/engineering/architecture/practice/scalability/). Others are in the works (such as the Availability Practice).
  * A [_collaborative_ **workflow**](https://handbook.gitlab.com/handbook/engineering/architecture/workflow/) that provides the necessary organizational solution to foster _inclusion_ , and drive ideas and priorities from all corners of the company.
  * A collection of **design documents** and **roadmaps** which are artifacts resulting from the [Architecture Design Workflow](https://handbook.gitlab.com/handbook/engineering/architecture/workflow/).


Such definition implies a solid reliance on **collaboration** rather than authority to _efficiently_ and _transparently_ drive decisions, engage stakeholders, and promote trust across the organization
### Artifacts: roadmaps and design documents[](https://handbook.gitlab.com/handbook/engineering/architecture/#artifacts-roadmaps-and-design-documents)
We strive for **results** and concrete outcomes, which in this case entail **roadmaps** and **design documents**. **Roadmaps** are documents that aggregate many **Design documents**.
### Architecture as a practice is everyone’s responsibility[](https://handbook.gitlab.com/handbook/engineering/architecture/#architecture-as-a-practice-is-everyones-responsibility)
Architecture at GitLab is not a dedicated role but it is notably engrained in senior technical leadership roles, where the roles’ levels and their sphere of influence determine responsibilities within the practice.
### Architecture Design Workflow[](https://handbook.gitlab.com/handbook/engineering/architecture/#architecture-design-workflow)
The [Architecture Design Workflow](https://handbook.gitlab.com/handbook/engineering/architecture/workflow/) is used to create design documents that are being used to align team members across multiple iterations.
## Roadmap[](https://handbook.gitlab.com/handbook/engineering/architecture/#roadmap)
Following our [Transparency](https://handbook.gitlab.com/handbook/values/#transparency) value, our [architecture roadmap](https://handbook.gitlab.com/handbook/engineering/architecture/roadmap/) and [design documents](https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/) are public.
* * *
#####  [Architecture Design Documents](https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/)
Design documents are the primary artifact that the architecture design workflow revolves around. A …
#####  [Architecture Design Workflow](https://handbook.gitlab.com/handbook/engineering/architecture/workflow/)
As engineers at GitLab, we lead the evolution of software, constantly working to find the right …
#####  [Guidelines](https://handbook.gitlab.com/handbook/engineering/architecture/guidelines/)
#####  [Key Abstractions](https://handbook.gitlab.com/handbook/engineering/architecture/abstractions/)
Overview Key Abstractions (also known as Key Primitives) are foundational technologies, patterns, …
#####  [Practices](https://handbook.gitlab.com/handbook/engineering/architecture/practice/)
Scalability Security Architecture Principles 
#####  [Technology Roadmap](https://handbook.gitlab.com/handbook/engineering/architecture/roadmap/)
As GitLab continues to grow and mature, it is approaching a pivotal point in which faster growth …
Last modified October 22, 2025: [Add Key Abstractions handbook page (`9781554c`)](https://gitlab.com/gitlab-com/content-sites/handbook/commit/9781554c)
[ ](https://gitlab.com/gitlab-com/content-sites/handbook/blob/main/content/handbook/engineering/architecture/_index.md) - [ ](https://gitlab.com/-/ide/project/gitlab-com/content-sites/handbook/edit/main/-/content/handbook/engineering/architecture/_index.md) - please [contribute](https://handbook.gitlab.com/handbook/about/contributing/). [ ![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-sa/4.0/)