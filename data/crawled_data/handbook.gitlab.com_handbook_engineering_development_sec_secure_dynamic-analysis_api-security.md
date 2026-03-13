# API Security team in the Dynamic Analysis Group
## API Security[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/dynamic-analysis/api-security/#api-security)
The API Security team is a standalone team which is part of the Dynamic Analysis group at GitLab. It is charged with developing solutions which perform Fuzzing.
Repo | Purpose  
---|---  
[API Fuzzer](https://gitlab.com/gitlab-org/security-products/analyzers/api-fuzzing-src) - Private | GitLab’s API Fuzzing scanner.  
### Important Fuzzing repositories[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/dynamic-analysis/api-security/#important-fuzzing-repositories)
Repo | Purpose  
---|---  
[API Security](https://gitlab.com/gitlab-org/security-products/analyzers/api-fuzzing-src) | Private - The API Security tool performs API Fuzzing and API DAST scans  
[API Fuzzing E2E Tests](https://gitlab.com/gitlab-org/security-products/tests/api-fuzzing-e2e) | Private - API End to End Tests  
[DAST API demos](https://gitlab.com/gitlab-org/security-products/demos/api-dast/) | Public - DAST API demos linked from the documentation.  
[API Fuzzing demos](https://gitlab.com/gitlab-org/security-products/demos/api-fuzzing) | Public - API Fuzzing demos linked from the documentation.  
[API Fuzzing demos](https://gitlab.com/gitlab-org/security-products/demos/api-fuzzing-example/) | Public - API Fuzzing demos linked from the documentation (har/openapi branches).  
## How to Contact Us[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/dynamic-analysis/api-security/#how-to-contact-us)
  * Slack channel: #g_ast-dynamic-analysis
  * Slack alias: @secure_dynamic_analysis_be
  * Google groups: dynamic-analysis-be@gitlab.com
  * GitLab mention: @gitlab-org/secure/dynamic-analysis-be


## How We Work[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/dynamic-analysis/api-security/#how-we-work)
The Dynamic Analysis group largely follows GitLab’s [Product Development Flow](https://handbook.gitlab.com/handbook/product-development/how-we-work/product-development-flow/).
Issues worked by this team are backend-centric and are typically in one the above repos, [vendored templates](https://gitlab.com/gitlab-org/gitlab/-/tree/master/lib/gitlab/ci/templates/Security), and GitLab’s [Rails monolith](https://gitlab.com/gitlab-org/gitlab). At times, issues can require support from AST’s frontend team if UI changes are required. We will require more notice for initiatives like these.
## Repeated tasks[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/dynamic-analysis/api-security/#repeated-tasks)
There are several maintenance tasks that need to be completed each milestone. Each iteration, an issue is opened and assigned to an engineer on a rotating basis. Those rotating tasks are:
  * Review upstream changes, and open an issue to upgrade DAST if the upstream changes provide important improvements
  * Review the [security dashboard](https://gitlab.com/gitlab-org/security-products/dast/-/security/vulnerability_report) for DAST and address all critical and high issues. Review the dashboards for upstream projects, [ZAP](https://gitlab.com/gitlab-org/security-products/dependencies/zaproxy) and [ZAP Extensions](https://gitlab.com/gitlab-org/security-products/dependencies/zap-extensions)


### Fuzzing Technologies[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/dynamic-analysis/api-security/#fuzzing-technologies)
  * The API Security product is built using mostly C# with some small amounts of Python. Our engineers use Windows VMs for development.


### Specialized Labels[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/dynamic-analysis/api-security/#specialized-labels)
When opening up issues, the following label snippet often added:
```

/label ~"Category:API Security"
/label ~"group::dynamic analysis"
/label ~"devops::application security testing"
/label ~"backend"
/label ~"section::sec"

```

#### Targets[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/dynamic-analysis/api-security/#targets)
For our Merge Request types, we have an initial soft target ratio of 60% features, 30% maintenance, and 10% bugs based on the [cross-functional prioritization process](https://handbook.gitlab.com/handbook/engineering/workflow/cross-functional-prioritization/). This is not a hard target and we expect to see variation in this ratio as we mature and our focus evolves.
### Support Requests[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/dynamic-analysis/api-security/#support-requests)
The Dynamic Analysis engineering team provides support to GitLab Support Engineers [following the process outlined in the Sec Section support project](https://gitlab.com/gitlab-com/sec-sub-department/section-sec-request-for-help/).
## Issue Boards[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/dynamic-analysis/api-security/#issue-boards)
  * [API Security - Delivery Workflow Board](https://gitlab.com/groups/gitlab-org/-/boards/4543953?label_name\[\]=Category%3AAPI%20Security)
  * [API Security Planning Board](https://gitlab.com/gitlab-org/gitlab/-/boards/4127408?label_name\[\]=Category%3AAPI%20Security)
  * [Dynamic Analysis EM Board](https://gitlab.com/groups/gitlab-org/-/boards/1353832?scope=all&utf8=%E2%9C%93&state=opened)


Last modified March 2, 2026: [docs: consolidate engineering workflow pages (`90fb9145`)](https://gitlab.com/gitlab-com/content-sites/handbook/commit/90fb9145)
[ ](https://gitlab.com/gitlab-com/content-sites/handbook/blob/main/content/handbook/engineering/development/sec/secure/dynamic-analysis/api-security.md) - [ ](https://gitlab.com/-/ide/project/gitlab-com/content-sites/handbook/edit/main/-/content/handbook/engineering/development/sec/secure/dynamic-analysis/api-security.md) - please [contribute](https://handbook.gitlab.com/handbook/about/contributing/). [ ![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-sa/4.0/)