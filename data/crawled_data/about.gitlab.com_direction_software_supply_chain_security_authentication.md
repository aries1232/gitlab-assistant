#  Group Direction - Authentication 
  1. You are here:
  2. [GitLab Direction](https://about.gitlab.com/direction/)
  3. [Product Stage Direction - Software Supply Chain Security](https://about.gitlab.com/direction/software_supply_chain_security/)
  4. Group Direction - Authentication


The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
  * [Introduction and how you can help](https://about.gitlab.com/direction/software_supply_chain_security/authentication/#introduction-and-how-you-can-help)
  * [Overview](https://about.gitlab.com/direction/software_supply_chain_security/authentication/#overview)
    * [Target audience and experience](https://about.gitlab.com/direction/software_supply_chain_security/authentication/#target-audience-and-experience)
  * [Priorities](https://about.gitlab.com/direction/software_supply_chain_security/authentication/#priorities)

Group | **Authentication**  
---|---  
Stage | [Software Supply Chain Security](https://handbook.gitlab.com/handbook/product/categories/#software-supply-chain-security-stage)  
Group | [Authentication](https://handbook.gitlab.com/handbook/product/categories/#authentication-group)  
Content Last Reviewed | `2025-05-27`  
## Introduction and how you can help[](https://about.gitlab.com/direction/software_supply_chain_security/authentication/#introduction-and-how-you-can-help)
Thanks for visiting the direction page for Authentication in GitLab.
We've previously been called the "Access" team and the "Authentication and Authorization" team. Our focus has narrowed, and we are now the "Authentication" team.
If you'd like to have influence on what the group is working on, the best way to help is to comment on individual issues if they are of interest, and tag `@hsutor`, Product Manager, so she sees your message.
## Overview[](https://about.gitlab.com/direction/software_supply_chain_security/authentication/#overview)
We are on a mission to empower GitLab system administrators with the toolkit they need to create their desired balance of security and accessibility for their GitLab experience.
Authentication is the first impression any new customer has when they configure their shiny new GitLab instance, and we aim to make it as seamless as possible: from that moment of first logging in, to onboarding users, to managing the basic security rules for their instance.
We recognize that authentication is more than a shiny frontend. It is comprised of elecements that are foundational to keeping resources _secure but accessible_.
No matter the size of a company, for an authentication strategy to function, it must be secure, flexible, and scalable.
Our objective, as a team, is to enable GitLab administrators to strike their desired balance between security and accessibility for their users.
### Target audience and experience[](https://about.gitlab.com/direction/software_supply_chain_security/authentication/#target-audience-and-experience)
The primary audience for Auth is administrators in medium to large enterprises. These are privileged, sophisticated users in companies managing employee identities with a single source of truth; this may be a series of [LDAP servers or an IDaaS service](https://docs.gitlab.com/ee/administration/auth/) like Okta, Azure AD, or GSuite.
Our audience cares deeply about security, and is well-versed in all of the areas of the platform where authentication loopholes exist. They are often under tremendous scrutiny to meet various compliance and audit standards from organizations outside their own.
They expect ease of use in terms of onboarding, offboarding, and maintaining control over their users, particularly in an Enterprise context.
We recognize that every user that works in GitLab needs to authenticate, so this experience must be secure and scalable for everyone. Our target persona is administrators who implement identity, but end users of identity our are customers, too.
## Priorities[](https://about.gitlab.com/direction/software_supply_chain_security/authentication/#priorities)
Item | Name | DRI | Target Release  
---|---|---|---  
1 | [Completion of vulnerabilities open](https://gitlab.com/gitlab-org/gitlab/-/boards/4374016?not\[label_name\]\[\]=Quality&label_name\[\]=group%3A%3Aauthentication&label_name\[\]=Deliverable&label_name\[\]=bug%3A%3Avulnerability&milestone_title=17.7) | `Across the team` | `18.1`  
2 | [CI_Job_Token - Infinite Loop](https://gitlab.com/gitlab-org/gitlab/-/issues/475705) | `@aboobackermk` | `18.1`  
3 | [Personal Access Tokens and impersonation tokens - display recently expired tokens](https://gitlab.com/gitlab-org/gitlab/-/issues/425053) | `fernando-c` | `18.1`  
4 | [Retain properly attributed activity log events for expired/revoked project/group access token activity](https://gitlab.com/gitlab-org/gitlab/-/issues/432790) | `bdenkovych` | `18.1`  
5 | [Authn and Authz Blueprint](https://gitlab.com/gitlab-org/gitlab/-/issues/504771) | `@bdenkovych, @ifarkas` | `18.1`  
6 | [Allow group and project members to subscribe to service account pipeline notifications](https://gitlab.com/gitlab-org/gitlab/-/issues/515629) | `@dblessing` | `18.1`  
7 | [Retain properly attributed audit events for tokens](https://gitlab.com/gitlab-org/gitlab/-/issues/432790) | `@bdenkovych` | `18.1`  
8 | [Additional credential types in the Credentials Inventory](https://gitlab.com/groups/gitlab-org/-/epics/14557) | `@sgarg_gitlab, @dblessing` | `18.1`  
9 | [Disable User Invitations - Enterprise Users](https://gitlab.com/gitlab-org/gitlab/-/issues/19618) | `@sgarg_gitlab` | `18.1`  
10 | [Instrument adoption of Enterprise Users](https://gitlab.com/gitlab-org/gitlab/-/issues/515688) | `@habdul-razak` | `18.1`  
11 | [Add group setting to hide members emails on public facing profile](https://gitlab.com/gitlab-org/gitlab/-/issues/472057) | `@TBD` | `18.1`  
12 | [Warn users when adding SSH keys of weaker types or smaller lengths](https://gitlab.com/gitlab-org/gitlab/-/issues/432624) | `TBD` | `18.2`  
13 | [SAML MR approval with ACS url on Geo support](https://gitlab.com/gitlab-org/gitlab/-/issues/491634) | `@sgarg_gitlab` | `18.0`  
14 | [Redesign invite flow for member invite](https://gitlab.com/gitlab-org/gitlab/-/issues/460261) | `@bdenkovych` | `18.1`  
15 | [Internal bot users POC for Cells](https://gitlab.com/gitlab-org/gitlab/-/issues/442780) | `@atevans` | `18.0`  
16 | [Evaluate external IAM services and libraries](https://gitlab.com/gitlab-org/gitlab/-/issues/513328) | `@dblessing, @tachyons-gitlab` | `N/A`  
17 | [Authentication owned gem Ruby 3.3 and 3.4 readiness validation](https://gitlab.com/gitlab-org/gitlab/-/issues/525599) | `@habdul-razak` | `N/A`  
18 | [UserDeletionWorker Improvements](https://gitlab.com/groups/gitlab-org/-/epics/9022) | `@atevans` | `18.3`  
19 | [P0 POCs for Auth redesign](https://gitlab.com/groups/gitlab-org/-/epics/17712) | `Multiple DRIs` | `18.3`  
20 | [PAT prefix null bug](https://gitlab.com/gitlab-org/gitlab/-/issues/536734) | `@dblessing` | `18.0`  
21 | [Credential controller scalability investigation](https://gitlab.com/gitlab-org/gitlab/-/issues/524159) | `@dblessing` | `18.0`  
22 | [Convert top_level group cretion to setting](https://gitlab.com/gitlab-org/gitlab/-/issues/506673) | `@@habdul-razak` | `18.0`  
23 | [OIDC Step-Up Auth - Beta](https://gitlab.com/gitlab-org/gitlab/-/issues/512659) | `@tachyons-gitlab` | `18.2`  
24 | [Passkey Implementation Design](https://gitlab.com/gitlab-org/gitlab/-/issues/480242) | `@bdenkovych` | `18.2`  
25 | [GitLab Workload Identity Federation](https://gitlab.com/groups/gitlab-org/-/epics/13974) | `TBD` | `TBD`  
26 | [Passwordless Authentication via FIDO Passkey](https://gitlab.com/groups/gitlab-org/-/epics/10897) | `TBD` | `18.4`  
[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/software_supply_chain_security/authentication/index.html.md.erb) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/software_supply_chain_security/authentication/index.html.md.erb)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fsoftware_supply_chain_security%2Fauthentication%2F&_biz_t=1773331888042&_biz_i=%0AGroup%20Direction%20-%20Authentication%0A%7C%0AGitLab%0A&_biz_n=73&rnd=142851&cdn_o=a&_biz_z=1773331888043)
suggested results