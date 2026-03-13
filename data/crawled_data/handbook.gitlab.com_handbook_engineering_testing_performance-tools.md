# GitLab Performance Testing Tool Selection Guide
## Overview[](https://handbook.gitlab.com/handbook/engineering/testing/performance-tools/#overview)
Performance Testing is a broad discipline that includes various approaches to evaluate a system’s performance characteristics. Load Testing, while often considered synonymous with Performance Testing is one of many approaches to Performance Testing. There are other approaches that enable testing performance throughout the development lifecycle, from early development to production monitoring.
Use the decision tree below to find the right performance testing approach for your needs.
```

Performance Testing Kit
yes
no
yes
no
yes
no
GitLab Performance ToolComponent Performance Testing (alpha)Sitespeed Runway
Start
Testing API/backend performance?Testing page load performance?Testing a specific component in isolation?
```

### Testing API or Backend Performance[](https://handbook.gitlab.com/handbook/engineering/testing/performance-tools/#testing-api-or-backend-performance)
Use [GitLab Performance Tool](https://gitlab.com/gitlab-org/quality/performance) when you want to test how your APIs, database queries, or backend services perform under load. This includes testing response times, throughput, and system behavior under various load conditions.
**When to use:**
  * Testing REST API endpoints
  * Validating database query performance
  * Load testing backend services
  * Reference architecture validation


### Testing Components in Isolation[](https://handbook.gitlab.com/handbook/engineering/testing/performance-tools/#testing-components-in-isolation)
Use [Component Performance Testing Tool](https://gitlab.com/gitlab-org/quality/component-performance-testing) to run automated load tests on individual services or components at the Merge Request level, providing early feedback on performance changes before they reach production. It does this by running tests against internal API endpoints rather than end-user API endpoints.
**When to use:**
  * Testing containerized services that can be deployed independently (like Gitaly, AI Gateway, Registry)
  * Detecting performance regressions in MRs before merge
  * Validating that component changes don’t introduce throughput bottlenecks
  * Getting fast feedback on API response times and resource utilization
  * Testing component-specific caching strategies and configuration changes


**What it tests:**
  * Component throughput and response times
  * Resource utilization (CPU, memory, network I/O)
  * Error handling performance
  * Configuration-related performance impacts


**What it doesn’t test:**
  * Integration bottlenecks between components
  * Production-scale data volume issues
  * End-to-end system performance


> **⚠️ Alpha Status:** Component Performance Testing is currently in alpha trials. If you want to use it, please reach out in Slack to [#g_performance_enablement](https://gitlab.slack.com/channels/g_performance_enablement).
**Prerequisites for adoption:**
  * Component must be containerized and deployable in isolation
  * Must expose testable interfaces (HTTP APIs, gRPC, etc.)
  * Should support testing with mocked dependencies


### Testing Page Load Performance[](https://handbook.gitlab.com/handbook/engineering/testing/performance-tools/#testing-page-load-performance)
Use [Sitespeed Runway](https://gitlab.com/gitlab-org/quality/sitespeed-runway) to measure how fast your pages load for users, including metrics like Time to First Byte, Largest Contentful Paint, and other Core Web Vitals.
**When to use:**
  * Testing frontend performance
  * Measuring page load times
  * Validating user experience metrics
  * Browser-based performance testing


## Future improvements[](https://handbook.gitlab.com/handbook/engineering/testing/performance-tools/#future-improvements)
These tools have not been implemented and will complement the Performance Testing Kit and enhance our ability to detect performance problems early.
```

no
yes
yes
no
yes
Start
Performance checks in Unit TestsProfiling toolsObservability based Performance TestingTesting with new unit tests?Testing during development?Analyzing live performance data?
```

### Testing with new unit tests[](https://handbook.gitlab.com/handbook/engineering/testing/performance-tools/#testing-with-new-unit-tests)
Add performance assertions directly to your unit tests to catch performance regressions early in development. This provides fast feedback on code changes without requiring separate performance test suites.
**When to use:**
  * Writing new unit tests and want to include performance validation
  * Adding performance checks to existing test coverage
  * Ensuring critical methods maintain acceptable performance thresholds
  * Catching performance regressions during code review


**Example approaches:**
  * Execution time assertions (method completes under X milliseconds)
  * Memory allocation limits (method allocates fewer than Y objects)
  * Database query count validation


### Testing during development[](https://handbook.gitlab.com/handbook/engineering/testing/performance-tools/#testing-during-development)
Use lightweight profiling tools while actively developing to understand performance characteristics of your code before it reaches production.
**When to use:**
  * Optimizing algorithm performance during development
  * Understanding memory usage patterns in new features
  * Identifying performance bottlenecks in work-in-progress code
  * Getting quick feedback on code changes without full test suites


**Example tools:**
  * Code profiler for CPU and memory analysis
  * Database query analyzers
  * Benchmarking utilities for comparing implementations


### Analyzing live performance data[](https://handbook.gitlab.com/handbook/engineering/testing/performance-tools/#analyzing-live-performance-data)
Leverage existing monitoring and observability data to identify performance issues and validate improvements using real production metrics.
**When to use:**
  * Investigating performance issues reported by users
  * Validating that performance improvements are effective in production
  * Understanding real-world performance patterns
  * Correlating code changes with production performance metrics


**Example approaches:**
  * Dashboard analysis of key performance indicators
  * Log-based performance trend analysis
  * Correlation of deployment events with performance changes


### Performance Unit Testing[](https://handbook.gitlab.com/handbook/engineering/testing/performance-tools/#performance-unit-testing)
Performance unit testing allows developers to evaluate and enforce the performance characteristics of their code at the unit level. This approach provides fast feedback on performance during development, helping catch performance regressions early in the development lifecycle.
#### Using rspec-benchmark[](https://handbook.gitlab.com/handbook/engineering/testing/performance-tools/#using-rspec-benchmark)
We have [rspec-benchmark](https://github.com/piotrmurach/rspec-benchmark) included in our Gemfile. It is a gem that provides RSpec matchers for performance testing. It offers various matchers to assert on different performance aspects such as execution time, iterations per second, allocation counts, and memory usage.
Example Test Case
Here’s a complete example of using rspec-benchmark to test the performance of a method:
```

require 'spec_helper'

RSpec.describe UserFinder do
  describe '#find_active' do
    it 'performs query under 50ms' do
      users = create_list(:user, 100, status: :active)

      expect {
        UserFinder.new.find_active
      }.to perform_under(50).ms
    end

    it 'allocates less than 20 objects' do
      users = create_list(:user, 100, status: :active)

      expect {
        UserFinder.new.find_active
      }.to perform_allocation(count: 1..20)
    end

    it 'scales linearly with number of users' do
      expect do |n, i|
        users = create_list(:user, n, status: :active)
        UserFinder.new.find_active
      end.to perform_linear.in_range(10..100).sample(5)
    end
  end
end

```

### Profiling Tools[](https://handbook.gitlab.com/handbook/engineering/testing/performance-tools/#profiling-tools)
We already use profiling tools (i.e. RuboCop) in our pipelines to ensure that we meet coding guidelines and avoid common problematic patterns. Several performance focused ones that are in our codebase:
  1. [ruby-prof](https://ruby-prof.github.io/): A comprehensive profiling solution that supports both flat and graph profiles. ruby-prof can measure CPU time, memory allocation, and object creation.
  2. [Stackprof](https://github.com/tmm1/stackprof): A sampling call-stack profiler. It’s designed to be a faster and more memory-efficient alternative to ruby-prof for certain use cases.
  3. [memory profiler](https://github.com/SamSaffron/memory_profiler): A memory profiler that provides detailed information about memory usage, including object allocation and retention. [documentation](https://gitlab.com/gitlab-org/gitlab/-/blob/master/doc/development/performance.md?ref_type=heads#using-memory-profiler) in our performance guidelines.
  4. [rbspy](https://rbspy.github.io): A sampling profiler for Ruby, [documentation](https://gitlab.com/gitlab-org/gitlab/-/blob/master/doc/administration/sidekiq/sidekiq_troubleshooting.md?ref_type=heads#ruby-profiling-with-rbspy) in our Sidekiq troubleshooting docs
  5. [derailed benchmarks](https://github.com/zombocom/derailed_benchmarks): A set of benchmarks that measure various aspects of Rails application performance, including memory usage and load time. [documentation](https://gitlab.com/gitlab-org/gitlab/-/blob/master/doc/development/performance.md?ref_type=heads#derailed-benchmarks) in our performance guidelines.
  6. [benchmark-ips](https://github.com/evanphx/benchmark-ips): benchmarks a blocks iterations/second
  7. [rspec_profiling](https://github.com/foraker/rspec_profiling): collects data on spec execution times, [documentation](https://gitlab.com/gitlab-org/gitlab/-/blob/master/doc/development/performance.md?ref_type=heads#rspec-profiling) from our performance guidelines.


Some approaches to using these tools are detailed on the [profiling page](https://gitlab.com/gitlab-org/gitlab/-/blob/master/doc/development/profiling.md?ref_type=heads)
## References[](https://handbook.gitlab.com/handbook/engineering/testing/performance-tools/#references)
### External References[](https://handbook.gitlab.com/handbook/engineering/testing/performance-tools/#external-references)
Page | Description  
---|---  
[Netflix performance testing](https://netflixtechblog.com/fixing-performance-regressions-before-they-happen-eab2602b86fe) | Blog post about performance testing at Netflix  
[Automation Pyramid Model for Performance Testing Process](https://abstracta.us/blog/test-automation/performance-testing-automation-pyramid-model-process/) | Blog post looking into the test pyramid for performance testing  
[Continuous Performance Testing: A Comprehensive Guide](https://abstracta.us/blog/performance-testing/continuous-performance-testing-a-comprehensive-guide/) | Blog post on Continuous Performance Testing  
[3 Challenges to Effective Performance Testing in Continuous Integration](https://abstracta.us/blog/performance-testing/3-challenges-effective-performance-testing-continuous-integration/) | Blog post on challenges implementing performance testing in CI  
[When is the Best Time to Start Performance Testing?](https://abstracta.us/blog/performance-testing/best-time-start-performance-testing/) | Blog post on when to do performance testing  
### Internal References[](https://handbook.gitlab.com/handbook/engineering/testing/performance-tools/#internal-references)
#### Projects[](https://handbook.gitlab.com/handbook/engineering/testing/performance-tools/#projects)
Project | Description  
---|---  
[GPT](https://gitlab.com/gitlab-org/quality/performance) | The GitLab Performance Tool (GPT) provides load testing for GitLab instances  
[Sitespeed Runway](https://gitlab.com/gitlab-org/quality/sitespeed-runway) | SiteSpeed CI pipelines for browser performance testing  
[CPT (Alpha)](https://gitlab.com/gitlab-org/quality/component-performance-testing) | Component-level performance testing for individual services (currently in alpha trials)  
[sitespeed-measurement-setup](https://gitlab.com/gitlab-org/frontend/sitespeed-measurement-setup) | Setup to measure performance on GitLab websites through sitespeed.io  
#### Documentation pages[](https://handbook.gitlab.com/handbook/engineering/testing/performance-tools/#documentation-pages)
Page | Description  
---|---  
[Performance Strategy & Measurement](https://handbook.gitlab.com/handbook/engineering/performance/) | GitLab’s overall performance strategy, targets, and measurement approach  
[Profiling page](https://gitlab.com/gitlab-org/gitlab/-/blob/master/doc/development/profiling.md) | Documentation on profiling approaches for GitLab  
[Observability for stage groups](https://docs.gitlab.com/ee/development/stage_group_observability/index.html) | Documentation on Observability focused at Stage Groups  
[Performance Bar](https://docs.gitlab.com/ee/administration/monitoring/performance/performance_bar.html) | Performance Bar for analyzing performance in running GitLab instances  
[Dev Performance Guidelines](https://docs.gitlab.com/ee/development/performance.html) | Developer-focused Performance Guidelines  
[Merge Request Performance Guidelines](https://docs.gitlab.com/ee/development/merge_request_concepts/performance.html) | Performance guidelines specific to Merge Requests  
[Platform Triage Dashboard](https://dashboards.gitlab.net/d/general-triage/general3a-platform-triage) | Starting point dashboard for investigating performance issues  
Last modified February 25, 2026: [Update references from GBPT to sitespeed-runway (`9881a4f4`)](https://gitlab.com/gitlab-com/content-sites/handbook/commit/9881a4f4)
[ ](https://gitlab.com/gitlab-com/content-sites/handbook/blob/main/content/handbook/engineering/testing/performance-tools.md) - [ ](https://gitlab.com/-/ide/project/gitlab-com/content-sites/handbook/edit/main/-/content/handbook/engineering/testing/performance-tools.md) - please [contribute](https://handbook.gitlab.com/handbook/about/contributing/). [ ![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-sa/4.0/)