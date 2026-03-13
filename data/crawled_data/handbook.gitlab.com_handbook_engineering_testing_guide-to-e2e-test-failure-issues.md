# End-to-End Test Failure Issue Debugging Guide
Concise guide for product engineers to debug End-to-End Test failure issues
[Troubleshooting Failure Issues (Video 3 minutes)](https://www.youtube.com/watch?v=KbQzrVJMvNQ&t=1552s)
### Most Common Fixes[](https://handbook.gitlab.com/handbook/engineering/testing/guide-to-e2e-test-failure-issues/#most-common-fixes)
  * **Element not found?** → Check if UI changed in recent MRs
  * **Timing out?** → Look for spinners in screenshot, check performance, check for page errors
  * **401 Unauthorized?** → Token expiration issue
  * **Only in staging-canary/staging environment?** → Check #staging channel for environmental issues and recent feature flag toggles


### Debugging the Failure[](https://handbook.gitlab.com/handbook/engineering/testing/guide-to-e2e-test-failure-issues/#debugging-the-failure)
  1. **Check the screenshot and exception** for any obvious errors, examples:
     * `ElementNotFound` → UI element missing/changed
     * `TimeoutError` → Unexpected behavior or slow loading
     * `AssertionError` → Unexpected data or behavior
     * `WaitExceededError` → Look for spinners still loading in screenshot
     * `401 Unauthorized` → Check expiring tokens
     * Server errors displayed in the UI → environmental issues or test set-up issues
  2. **Check GitLab instance under test** - Use the `found:` labels (note: failure can be across multiple instances)
     * `found:master` → Ephemeral environment, failed in scheduled pipeline against `master` branch 
       * Open the latest failed job from the **Reports** section
       * Check where the test is failing (**GDK** , **CNG** , **Omnibus**)
       * View the job name - this indicates the test configuration
> **Note:** Merge Requests will be blocked when tests are failing against **GDK** and **CNG**. These failures tend to be flaky failures as the test would have usually failed in a previous merge request. Tests against **Omnibus** are optional and allowed to fail.
     * `found:<environment>` → Failed in a live environment ([debugging guide](https://docs.gitlab.com/development/testing_guide/end_to_end/debugging_end_to_end_test_failures/)) 
       * Open job to see if failure was a `smoke` job, or check metadata of test to see if test is a smoke test
       * If test is failing in a single environment, check environment status (#staging, #production)
> **Note:** `:smoke` test failures in `staging-canary` will [block deployments](https://docs.gitlab.com/development/testing_guide/end_to_end/debugging_end_to_end_test_failures/#staging-canary).
  3. **Check failure frequency and timing**
     * Observe when the failure issue created to identify the first occurrence
     * Observe the frequency of occurrences in the Reports section
     * **Failure patterns:**
       * Multiple recent consistent failures are more likely to be a real issue, needing immediate action
       * Sporadic failures could mean test flakiness OR application instability (race conditions, timing issues)
       * Use the first occurrence time to check commits/deployments immediately prior to the issue occurring
  4. **View the test file for recent changes**
     * Click the `File URL` link in the failure issue metadata and review recent commits to the test file
  5. **Try to reproduce locally** [against your GDK](https://docs.gitlab.com/development/testing_guide/end_to_end/feature_flag_testing/#running-e2e-tests-against-gdk), example:
```

   cd qa
   bundle install
   WEBDRIVER_HEADLESS=false GITLAB_QA_ADMIN_ACCESS_TOKEN=<admin PAT> QA_LOG_LEVEL=DEBUG QA_GITLAB_URL=http://gdk.test bundle exec rspec qa/specs/features/browser_ui/3_create/repository/add_file_template_spec.rb

```

  6. **If failure is from a live environment and passing against GDK, try against live environment** or manually verify the functionality works in live environment.
     * <https://docs.gitlab.com/development/testing_guide/end_to_end/feature_flag_testing/#running-e2e-tests-against-staging>
  7. **Check application logs** for signs of failure
     * Check job artifacts for `master` failures
     * Check <https://nonprod-log.gitlab.net> for `staging` failures
     * Check <https://log.gprd.gitlab.net> for `production` failures
  8. **Check subsequent test runs**
     * Click **Test case** link in this issue
     * Check labels in test case issue for latest status of test case → If the test has subsequently passed the test or environment may be flaky
  9. **Check recent feature flag toggles** (if failure is in a live environment)


### Triage Actions[](https://handbook.gitlab.com/handbook/engineering/testing/guide-to-e2e-test-failure-issues/#triage-actions)
Apply appropriate label per [classification guide](https://handbook.gitlab.com/handbook/engineering/testing/pipeline-triage/#classify-and-triage-the-test-failure)
> **Note:** Failure issues will be auto-closed after 30 days of no updates.
Symptom | Label | Action  
---|---|---  
Feature broken, urgent (affects users) | `~failure::bug` | Create bug fix or revert MR  
Feature broken, non-urgent | `~failure::bug` | Create bug fix or quarantine + schedule fix for future milestone  
Test stale/broken | `~failure::stale-test` | Update test or quarantine + schedule fix for future milestone  
[Flaky test](https://docs.gitlab.com/development/testing_guide/unhealthy_tests/#flaky-tests)* | `~failure::flaky-test` | Investigate root cause + schedule fix for future milestone  
One-off environment issue | `~failure::test-environment` | Monitor and close issue if does not re-occur  
External dependency failure | `~failure::external-dependency` | Monitor and close issue if does not re-occur  
*Flakiness can be caused by the test OR the application itself being unreliable under certain conditions
### Quarantining tests[](https://handbook.gitlab.com/handbook/engineering/testing/guide-to-e2e-test-failure-issues/#quarantining-tests)
Quarantine is a **temporary measure** for:
  * Stale/broken tests (Feature works for users)
  * Known acceptable issue causing `:smoke` test failures or excessive noise


  1. **Use[Fast Quarantine](https://handbook.gitlab.com/handbook/engineering/testing/quarantine-process/#fast-quarantine)** for an urgent quarantine
  2. **Follow up with a[long-term quarantine](https://handbook.gitlab.com/handbook/engineering/testing/quarantine-process/#long-term-quarantine)**
  3. Tag this issue with `~quarantine` and `~automation:prevent-auto-close`


For detailed quarantine workflows, see the [Test Quarantine Process](https://handbook.gitlab.com/handbook/engineering/testing/quarantine-process/)
### Need further assistance?[](https://handbook.gitlab.com/handbook/engineering/testing/guide-to-e2e-test-failure-issues/#need-further-assistance)
Contact **#g_test_governance** Slack channel or create a [Test Governance Request for help issue](https://gitlab.com/gitlab-org/quality/test-governance/request-for-help/-/issues/new)
Last modified January 8, 2026: [Consolidate quarantine documentation into one page (`2a35a9d6`)](https://gitlab.com/gitlab-com/content-sites/handbook/commit/2a35a9d6)
[ ](https://gitlab.com/gitlab-com/content-sites/handbook/blob/main/content/handbook/engineering/testing/guide-to-e2e-test-failure-issues.md) - [ ](https://gitlab.com/-/ide/project/gitlab-com/content-sites/handbook/edit/main/-/content/handbook/engineering/testing/guide-to-e2e-test-failure-issues.md) - please [contribute](https://handbook.gitlab.com/handbook/about/contributing/). [ ![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-sa/4.0/)