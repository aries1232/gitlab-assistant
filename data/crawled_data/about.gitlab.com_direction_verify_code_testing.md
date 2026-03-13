#  Category Direction - Code Testing and Coverage 
  1. You are here:
  2. [GitLab Direction](https://about.gitlab.com/direction/)
  3. [Verify Stage Direction](https://about.gitlab.com/direction/verify/)
  4. Category Direction - Code Testing and Coverage


The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
  * [Code Testing and Coverage](https://about.gitlab.com/direction/verify/code_testing/#code-testing-and-coverage)
    * [Introduction and how you can help](https://about.gitlab.com/direction/verify/code_testing/#introduction-and-how-you-can-help)
    * [Overview](https://about.gitlab.com/direction/verify/code_testing/#overview)
    * [Strategy and Themes](https://about.gitlab.com/direction/verify/code_testing/#strategy-and-themes)
    * [1 year plan](https://about.gitlab.com/direction/verify/code_testing/#1-year-plan)
      * [What is next for us](https://about.gitlab.com/direction/verify/code_testing/#what-is-next-for-us)
      * [What is Not Planned Right Now](https://about.gitlab.com/direction/verify/code_testing/#what-is-not-planned-right-now)
    * [Best in Class Landscape](https://about.gitlab.com/direction/verify/code_testing/#best-in-class-landscape)
      * [Key Capabilities](https://about.gitlab.com/direction/verify/code_testing/#key-capabilities)
      * [Top Competitive Solutions](https://about.gitlab.com/direction/verify/code_testing/#top-competitive-solutions)
    * [Target Audience](https://about.gitlab.com/direction/verify/code_testing/#target-audience)
    * [Analyst Landscape](https://about.gitlab.com/direction/verify/code_testing/#analyst-landscape)


## Code Testing and Coverage[](https://about.gitlab.com/direction/verify/code_testing/#code-testing-and-coverage)
|   
---|---  
Stage | [Verify](https://about.gitlab.com/direction/verify/)  
Maturity | [Viable](https://about.gitlab.com/direction/#maturity)  
Content Last Reviewed | `2025-04-28`  
### Introduction and how you can help[](https://about.gitlab.com/direction/verify/code_testing/#introduction-and-how-you-can-help)
Thanks for visiting this category direction page on Code Testing and Coverage in GitLab. This page belongs to the [Pipeline Execution](https://handbook.gitlab.com/handbook/product/categories/#pipeline-execution-group) group of the Verify stage and is maintained by Rutvik Shah (E-Mail).
This direction page is a work in progress, and everyone can contribute:
  * Please comment and contribute in the linked [issues](https://gitlab.com/gitlab-org/gitlab/-/issues/?sort=updated_desc&state=opened&label_name%5B%5D=Category%3ACode%20Testing%20and%20Coverage&first_page_size=20) and [epics](https://gitlab.com/groups/gitlab-org/-/epics?state=opened&page=1&sort=start_date_desc&label_name\[\]=Category:Code+Testing+and+Coverage) on this page. Sharing your feedback directly on GitLab.com is the best way to contribute to our strategy and vision.
  * Please share feedback directly via email, Twitter, or on a video call. If you're a GitLab user and want to discuss how GitLab can better support your testing needs, we'd especially love to hear from you.


### Overview[](https://about.gitlab.com/direction/verify/code_testing/#overview)
We utilize [intelligence in testing](https://gitlab.com/groups/gitlab-org/-/epics/9638) to ensure that individual components built within a pipeline perform as expected and as efficiently as possible. We also aim to make testing accessible by making it easier to setup and start testing to drive quality early in the development process.
Our long term vision is to optimize pipelines to quickly deliver quality code with a high degree of confidence. We will do this by automating testing; reducing the amount of time between development and test cycles; broadening test scope and coverage (e.g. unit, functional, end-to-end); and dashboards to provide an aggregate view of test quality and observable trends to monitor product health.
### Strategy and Themes[](https://about.gitlab.com/direction/verify/code_testing/#strategy-and-themes)
Our offerings in the area of Testing are limited compared to our competitors; in particular, we do not offer test case management features. We are working with the Certify group to build an integrated test case management feature, providing traceability across product requirements and test cases/plans as part of [gitlab&9640](https://gitlab.com/groups/gitlab-org/-/epics/9640). Our long-term vision provides not only traceability, but also [group-level dashboards](https://gitlab.com/gitlab-org/gitlab/-/issues/388359) for various stakeholders to view both rolled up and individual project completion status. Quality remains an important driver for improving our users ability to confidently track deployments with GitLab and as noted above we are starting on that vision in the [Project Quality Summary epic](https://gitlab.com/groups/gitlab-org/-/epics/5430).
Pipeline efficiency has become increasingly important to developers, CI/CD leaders, and executives. As part of achieving our long-term goal of "smarter testing", we are evaluating opportunities to use [ML/AI to optimize pipelines](https://gitlab.com/gitlab-org/gitlab/-/issues/388531) and [additional opportunities to expand](https://gitlab.com/groups/gitlab-org/-/epics/9643) our current offering for [Fail Fast Testing](https://docs.gitlab.com/ee/ci/testing/fail_fast_testing.html). We are also evaluating mechanisms enabling users to [select which tests they want to execute or quarantine](https://gitlab.com/groups/gitlab-org/-/epics/9651).
In all features we build, we strive to continuously improve our user experience, including [ease of use](https://gitlab.com/gitlab-org/gitlab/-/issues/366347) and automation where possible. We also know users want more insights from their CI/CD pipelines and especially from their tests. We are evaluating [gitlab#210250](https://gitlab.com/gitlab-org/gitlab/-/issues/210250) as a way to provide those insights and further encourage users to upload test report artifacts within their CI/CD pipelines.
### 1 year plan[](https://about.gitlab.com/direction/verify/code_testing/#1-year-plan)
There are no new planned features in Code Testing and Coverage for FY26.As part of the [streamlining parent/child artifacts](https://gitlab.com/groups/gitlab-org/-/epics/4019) work we will be [displaying JUnit and Code Coverage Reports from a Child pipeline in a MR](https://gitlab.com/groups/gitlab-org/-/epics/8205#iteration-1-implement-high-priority-reports).Pipeline Execution will support high priority bug fixes in this category as they arise.
#### What is next for us[](https://about.gitlab.com/direction/verify/code_testing/#what-is-next-for-us)
We recently release support for [test coverage visualization for JaCoCo](https://gitlab.com/gitlab-org/gitlab/-/issues/227345)
#### What is Not Planned Right Now[](https://about.gitlab.com/direction/verify/code_testing/#what-is-not-planned-right-now)
Although we do not have any plans to release new features in the coming year, we welcome [community contributions](https://about.gitlab.com/community/contribute/) that align with our intelligence testing vision.
### Best in Class Landscape[](https://about.gitlab.com/direction/verify/code_testing/#best-in-class-landscape)
BIC (Best In Class) is an indicator of forecasted near-term market performance based on a combination of factors, including analyst views, market news, and feedback from the sales and product teams. It is critical that we understand where GitLab appears in the BIC landscape.
#### Key Capabilities[](https://about.gitlab.com/direction/verify/code_testing/#key-capabilities)
In the [2021 Continuous Software Delivery Forrester Tech Tide](https://www.forrester.com/report/The+Forrester+Tech+Tide+Continuous+Software+Delivery+Q1+2021/-/E-RES161669), Testing was cited as the number one key to unlock continuous delivery for organizations. Top areas for investment are a) API test automation, b) continuous functional test suites, c) shift-left performance testing. Industry leaders are seeking integrated suites over best in breed tools for testing and CD. Additionally, API testing is being marketed as a silver bullet that is cheaper, effective and efficient to modernize the toolchain for enterprises. Sample vendors include: API Fortress, Broadcom, Eggplant, and others. We are exploring how we expand our market share in this area via [product#2516](https://gitlab.com/gitlab-com/Product/-/issues/2516) and adding a new category in this [merge request](https://gitlab.com/gitlab-com/www-gitlab-com/-/merge_requests/80183).
#### Top Competitive Solutions[](https://about.gitlab.com/direction/verify/code_testing/#top-competitive-solutions)
Many other CI solutions can also consume standard JUnit test output or other formats to display insights natively like [CircleCI](https://circleci.com/docs/2.0/collect-test-data/) or through a plugin like [Jenkins](https://plugins.jenkins.io/junit). [Allure](https://demo.qameta.io/allure/) is a popular reporting tool for review of test executions and recently DataDog introduced [CI Visibility](https://docs.datadoghq.com/continuous_integration/) as part of their SaaS offering including [Flaky Test Management](https://docs.datadoghq.com/continuous_integration/guides/flaky_test_management/).
There are new entrants in the code testing space which uses ML/AI with the focus on:
Optimizing Test Execution - Predictive Test Selection uses code change log and test execution history as an input and applies machine learning to determine which tests are more likely to fail for a given pull request.[Launchable](https://launchableinc.com/solution/) and [Develocity by Gradle](https://gradle.com/gradle-enterprise-solutions/predictive-test-selection/)] are two examples of this.
Writing Test Cases - [Diffblue](https://www.diffblue.com/) generates unit regression tests.
In order to stay remain ahead of these competitors we will continue to push forward to make unit test data visible and actionable in the context of the Merge Request for developers with [unit test reports](https://docs.gitlab.com/ee/ci/unit_test_reports.html#viewing-unit-test-reports-on-gitlab) and historical insights to identify flaky tests with epics like [gitlab&3129](https://gitlab.com/groups/gitlab-org/-/epics/3129)
### Target Audience[](https://about.gitlab.com/direction/verify/code_testing/#target-audience)
Check out our [Ops Section Direction "Who's is it for?"](https://about.gitlab.com/direction/ops/#who-is-it-for) for an in-depth look at our target personas across Ops. For Code Testing and Coverage, our "What's Next & Why" are targeting the following personas, as ranked by priority for support:
  1. [Sasha - Software Developer](https://handbook.gitlab.com/handbook/product/personas/#sasha-software-developer)
  2. [Simone - Software Engineer in Test](https://handbook.gitlab.com/handbook/product/personas/#simone-software-engineer-in-test)
  3. [Devon - DevOps Engineer](https://handbook.gitlab.com/handbook/product/personas/#devon-devops-engineer)


### Analyst Landscape[](https://about.gitlab.com/direction/verify/code_testing/#analyst-landscape)
In 2020, Gartner has released the Artificial Intelligence Use Case Prism for Development and Testing on their [research website](https://www.gartner.com/en/documents/3994888/infographic-artificial-intelligence-use-case-prism-for-d). Directionally, several of the use cases are generation of unit tests from analyzing code patterns, using business logic to create API test scenarios, and using machine learning to fabricate test data as well as correlating testing results back to business metrics to convey meaningful connections like release success or quality.
[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/verify/code_testing/index.html.md) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/verify/code_testing/index.html.md)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fverify%2Fcode_testing%2F&_biz_t=1773332017774&_biz_i=%0ACategory%20Direction%20-%20Code%20Testing%20and%20Coverage%0A%7C%0AGitLab%0A&_biz_n=103&rnd=654279&cdn_o=a&_biz_z=1773332017898)
suggested results