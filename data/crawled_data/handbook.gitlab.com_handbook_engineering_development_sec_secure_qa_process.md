# Secure QA Process
## Everything starts with a Merge Request[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/qa_process/#everything-starts-with-a-merge-request)
We expect and require all contributions to our products to go a merge request with a formal review. As such, we follow the [Merge Request workflow](https://docs.gitlab.com/ee/development/contributing/merge_request_workflow.html) and [code review guidelines](https://docs.gitlab.com/ee/development/code_review.html) articulated in GitLab’s developer documentation. We would, however, like to highlight a few items from these documents and add a few additional considerations for reviewers and authors.
### Additional considerations for Merge Request reviewers[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/qa_process/#additional-considerations-for-merge-request-reviewers)
  * The best way to unblock a peer or community member is to [provide feedback in a timely manner](https://handbook.gitlab.com/handbook/engineering/workflow/code-review/#review-turnaround-time). If you are at capacity and cannot facilitate a review in the SLO to which we aspire, please let folks know in the merge request so another reviewer may be found.


### Additional considerations for Merge Request authors[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/qa_process/#additional-considerations-for-merge-request-authors)
  * Being a globally distributed organization can, and frequently does, add latency to back-and-forth communication between folks. [Don’t take it personally](https://handbook.gitlab.com/handbook/values/#assume-positive-intent) if it’s taking longer than you expected to get feedback on your changes.


## Secure QA Process[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/qa_process/#secure-qa-process)
The secure analyzers verify merge requests by running a new commit against downstream test projects for their supported languages/frameworks (i.e. the [`gemnasium` analyzer](https://gitlab.com/gitlab-org/security-products/analyzers/gemnasium) of `Dependency Scanning` will trigger tests against `php`, `go`, and [several other](https://gitlab.com/gitlab-org/security-products/analyzers/gemnasium/-/blob/v2.21.0/.gitlab-ci.yml#L35-89) test projects). The verification is done by comparing the generated report output against an expected report committed to the analyzer’s repository. If analyzer behavior has changed, then the pipeline will fail because the contents of the expected and generated reports will no longer match.
The expectations for the `Dependency Scanning`, `SAST`, and `Secrets Detection` analyzers are stored in the project’s `qa/expect` directory with a sub-directory for each particular framework/language type.
### Test Projects[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/qa_process/#test-projects)
The test projects reside in the Secure [tests subgroup](https://gitlab.com/gitlab-org/security-products/tests/) and their use and best practices are found in the [common README](https://gitlab.com/gitlab-org/security-products/tests/common/-/blob/master/README.md).
### Changing Analyzer Behavior[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/qa_process/#changing-analyzer-behavior)
If a change to an analyzer changes the report output, then the expected report must change as well.
In `SAST`, `Dependency Scanning`, `Secret Detection` the expected reports are stored with the analyzer in a path corresponding to the test project in a subdirectory for the language/framework. For example, the expected report for scanning the dependencies of `java-maven` is stored in [gemnasium-maven/qa/expect](https://gitlab.com/gitlab-org/security-products/analyzers/gemnasium-maven/-/tree/master/qa/expect/java-maven). This way if an analyzer’s behavior changes, the expectation can be changed and packaged in the same commit.
For `License Compliance`, expectations are stored in the test project’s `qa/expect` directory (e.g. [ruby-bundler/qa/expect](https://gitlab.com/gitlab-org/security-products/tests/ruby-bundler/-/tree/master/qa/expect)).
More information about can be found in the [Security Products test projects repository](https://gitlab.com/gitlab-org/security-products/tests/common/-/blob/master/README.md).
### Testing on OpenShift[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/qa_process/#testing-on-openshift)
We currently do not have automated tests for OpenShift. If you want to see how a change affects the analyzer behavior on OpenShift, you can test it by setting up an OpenShift environment. There are two methods to do this:
#### 1. Automated Script[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/qa_process/#1-automated-script)
The distribution team has shared an [automated script](https://gitlab.com/gitlab-org/distribution/infrastructure/openshift-provisioning) for setting up an OpenShift cluster. While untested by our group, this method could potentially streamline the cluster creation process.
#### 2. Manual Setup[](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/qa_process/#2-manual-setup)
You can setup an OpenShift cluster following the steps below assuming that you already have access to the [GitLab Sandbox Cloud](https://gitlabsandbox.cloud/).
  1. Login to <https://gitlabsandbox.cloud/>.
  2. Create an AWS sandbox account and login to the AWS console by following steps `1` to `3` from [Static Analysis Group EC2 development machine setup guide](https://handbook.gitlab.com/handbook/engineering/development/sec/secure/static-analysis/ec2_dev_environment_setup/#static-analysis-group-ec2-development-machine-setup-guide).
  3. Once you are logged into the AWS console, you can search for “OpenShift” in the search field in the upper left corner, which should show `Red Hat OpenShift Service on AWS` under the Services category. ROSA provides an integrated OpenShift experience with AWS. Click on this search result to proceed.
![openshift-service-on-aws-search-results](https://handbook.gitlab.com/images/handbook/engineering/development/sec/secure/openshift/openshift-service-on-aws-search-results.png)
  4. You are redirected to the `Red Hat OpenShift Service on AWS (ROSA)` landing page. Click on the `Get started` link in the left sidebar, or the `Get started` orange button.
![openshift-service-on-aws-landing-page](https://handbook.gitlab.com/images/handbook/engineering/development/sec/secure/openshift/openshift-service-on-aws-landing-page.png)
  5. You will then be redirected to the `Verify ROSA prerequisites` page:
![verify-rosa-prerequisites](https://handbook.gitlab.com/images/handbook/engineering/development/sec/secure/openshift/verify-rosa-prerequisites.png)
Click on the `Enable ROSA HCP and ROSA classic` button in the `ROSA enablement` section, and keep the box `I agree to share my AWS account number...` checked. The `ROSA enablement` section will then explain `Your request to enable ROSA is pending and may take several minutes to resolve. We recommend keeping this page open so that you can review any errors.`
  6. After a few minutes, the `ROSA enablement` section will be updated and display the following messages:
     * `You have agreed to share your AWS account number and email address with red hat.`
     * `You have enabled ROSA and HCP and ROSA classic.`
![rosa-enabled](https://handbook.gitlab.com/images/handbook/engineering/development/sec/secure/openshift/rosa-enabled.png)
  7. Click on the `Continue to Red Hat` orange button in the bottom right corner. This will redirect you to <https://sso.redhat.com> and request you to `Log in to your Red Hat account`:
![login-to-your-redhat-account](https://handbook.gitlab.com/images/handbook/engineering/development/sec/secure/openshift/login-to-your-redhat-account.png)
  8. Click on `Log in with Google` and use your `gitlab.com` gmail account. You will be redirected to the `Register for a Red Hat account` page:
![register-for-red-hat-account](https://handbook.gitlab.com/images/handbook/engineering/development/sec/secure/openshift/register-for-red-hat-account.png)
Complete the required fields, using your `gitlab.com` gmail account for the `Email address`, then click on `Create my account`.
  9. You should now be redirected to a page to `Complete your account connection`. Check the `I have read and agreed to the terms and conditions` checkbox, then click on the `Connect accounts` button:
![complete-your-account-connection](https://handbook.gitlab.com/images/handbook/engineering/development/sec/secure/openshift/complete-your-account-connection.png)
  10. You’ll then be redirected to another page explaining `We need a little more information`. Complete the required fields, using your `gitlab.com` gmail account for the `Email address`, and select `Personal` for `Account type`:
![we-need-a-little-more-information](https://handbook.gitlab.com/images/handbook/engineering/development/sec/secure/openshift/we-need-a-little-more-information.png)
  11. The `Terms and conditions` box will now be displayed, click on `View Terms and Conditions` and accept them:
![terms-and-conditions](https://handbook.gitlab.com/images/handbook/engineering/development/sec/secure/openshift/terms-and-conditions.png)
  12. You’ll now be redirected to the [Red Hat Hybrid Cloud Console Overview](https://console.redhat.com/openshift/overview) screen, and can set up an OpenShift cluster by clicking the `Create cluster` in the `Red Hat OpenShift Service on AWS (ROSA)` dialog box:
![redhat-overview](https://handbook.gitlab.com/images/handbook/engineering/development/sec/secure/openshift/redhat-overview.png)
If you are only planning to use the cluster for testing, it is recommended to select the `OSD Trial` with a free trial period of 2 months. After this period, the cluster will be deleted. The free trial enables you to upgrade to a paid tier within time frame of two months.
  13. Once the cluster is set up, we have to create a user to login to the OpenShift cluster; you can select `Cluster List > <your cluster>` and select `htpasswd` for `Identity Provider`. Under `Cluster Roles and Access` you can create the user for accessing the OpenShift cluster. Make sure that this user belongs to the groups `dedicated-admin` and `cluster-admins`.
  14. Afterwards you can click on the `Open console` button and login with the cluster admin user you created in the previous step.
  15. Once you are logged into the OpenShift cluster, you can now install the GitLab Runner Operator by selecting `Operators > Operator Hub`. You can search GitLab Runner, click on the search result and then click on the `Install` button as explained [here](https://docs.gitlab.com/runner/install/operator.html).
  16. In order to set up the runner in the OpenShift cluster, you can follow the instructions that are included in the [README of the operator](https://gitlab.com/gitlab-org/gl-openshift/gitlab-runner-operator/-/blob/5f1134143f1b73171a7bb90d48b1fec948360db8/operator.yaml#L380).
Note that the [runner token](https://gitlab.com/gitlab-org/gl-openshift/gitlab-runner-operator/-/blob/master/README.md?plain=1#L43) referenced in the `gitlab-runner-operator README.md` can be obtained by selecting `CI/CD Settings > Runners > New Runner` from a GitLab project.
The runner setup requires the command line tool [`oc` (OpenShift client) to be installed](https://docs.redhat.com/en/documentation/red_hat_build_of_microshift/4.12/html/cli_tools/microshift-oc-cli-install#cli-installing-cli_cli-oc-installing). Before using `oc` you have to authenticate against your cluster. You can find the authentication credentials by clicking on your OpenShift cluster admin user name and then selecting `Copy login comand`. Note, that the default runner setup allows containers to be executed with root privileges. In order to restrict access to non root users, you can provide the configuration below:
```

[[runners]]
name = "gitlab-runner"
url = "https://gitlab.com"
executor = "kubernetes"
[runners.kubernetes]
    [runners.kubernetes.pod_security_context]
    run_as_non_root = true
    run_as_user = 1000

```

After applying this configuration with `oc create configmap my-runner-config --from-file=config.toml`, you can update the runner config as illustrated below and apply it with `oc appy -f gitlab-runner.yml`.
```

apiVersion: apps.gitlab.com/v1beta2
kind: Runner
metadata:
  name: gitlab-runner
spec:
  gitlabUrl: https://gitlab.com
  buildImage: alpine
  token: gitlab-runner-secret
  tags: openshift
  config: my-runner-config

```

  17. The OpenShift runner should now appear green in your GitLab project settings `CI/CD Settings > Runners`.


Last modified January 10, 2025: [Add automated script to openshift cluster setup (`68e14fe8`)](https://gitlab.com/gitlab-com/content-sites/handbook/commit/68e14fe8)
[ ](https://gitlab.com/gitlab-com/content-sites/handbook/blob/main/content/handbook/engineering/development/sec/secure/qa_process.md) - [ ](https://gitlab.com/-/ide/project/gitlab-com/content-sites/handbook/edit/main/-/content/handbook/engineering/development/sec/secure/qa_process.md) - please [contribute](https://handbook.gitlab.com/handbook/about/contributing/). [ ![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-sa/4.0/)