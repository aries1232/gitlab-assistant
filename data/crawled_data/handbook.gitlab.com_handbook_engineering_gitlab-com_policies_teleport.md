# GitLab Teleport Access Policy
## Purpose[](https://handbook.gitlab.com/handbook/engineering/gitlab-com/policies/teleport/#purpose)
To ensure an audited access to our terminal/CLI tools like [Database Access](https://gitlab.com/gitlab-com/runbooks/-/blob/master/docs/teleport/Connect_to_Database_Console_via_Teleport.md) and [Rails Console](https://gitlab.com/gitlab-com/runbooks/-/blob/master/docs/teleport/Connect_to_Rails_Console_via_Teleport.md), GitLab uses Teleport.
## Scope[](https://handbook.gitlab.com/handbook/engineering/gitlab-com/policies/teleport/#scope)
The Teleport Access policy applies to all systems within our production environment that require a terminal or CLI access.
## Roles & Responsibilities[](https://handbook.gitlab.com/handbook/engineering/gitlab-com/policies/teleport/#roles--responsibilities)
Role | Responsibility  
---|---  
GitLab Team Members | Responsible for following the requirements in this policy  
System Owners | Alignment to this policy  
Code Owners | Responsible for approving changes and exceptions to this policy  
## Procedure[](https://handbook.gitlab.com/handbook/engineering/gitlab-com/policies/teleport/#procedure)
  * Teleport access is managed through [Okta](https://handbook.gitlab.com/handbook/security/corporate/end-user-services/okta/) and is provided as part of a role’s baseline group assignment or through an [access request](https://handbook.gitlab.com/handbook/security/corporate/services/access-requests/) with appropriate approval
  * Access reviews are performed on a quarterly basis to ensure that all users are appropriate and have appropriate access levels.
  * Teleport Audit Logs must be retained for a defined period of 1 year
  * Teleport Audit Logs must not be modified and or deleted before the defined time of 1 year
  * Access to Teleport Audit log data must be limited based on the principle of least privilege


## Exceptions[](https://handbook.gitlab.com/handbook/engineering/gitlab-com/policies/teleport/#exceptions)
Exceptions to this policy will be tracked as per the [Information Security Policy Exception Management Process](https://handbook.gitlab.com/handbook/security/#information-security-policy-exception-management-process)
## References[](https://handbook.gitlab.com/handbook/engineering/gitlab-com/policies/teleport/#references)
  * [What is considered production](https://gitlab.com/gitlab-com/gl-security/security-assurance/sec-compliance/compliance/-/blob/master/production_definition.md)
  * [Production Architecture](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production/architecture/)
  * [Runbook: How to connect to a Database console using Teleport](https://gitlab.com/gitlab-com/runbooks/-/blob/master/docs/teleport/Connect_to_Database_Console_via_Teleport.md)
  * [Runbook: How to connect to a Rails Console using Teleport](https://gitlab.com/gitlab-com/runbooks/-/blob/master/docs/teleport/Connect_to_Rails_Console_via_Teleport.md)
  * [Teleport](https://goteleport.com/docs/)


Last modified January 23, 2026: [Move infrastructure/production to infrastructure-platforms (`6a8ad9a7`)](https://gitlab.com/gitlab-com/content-sites/handbook/commit/6a8ad9a7)
[ ](https://gitlab.com/gitlab-com/content-sites/handbook/blob/main/content/handbook/engineering/gitlab-com/policies/teleport/_index.md) - [ ](https://gitlab.com/-/ide/project/gitlab-com/content-sites/handbook/edit/main/-/content/handbook/engineering/gitlab-com/policies/teleport/_index.md) - please [contribute](https://handbook.gitlab.com/handbook/about/contributing/). [ ![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-sa/4.0/)