# Availability Measurement for GitLab SaaS Services
This policy specifies how availability is measured for GitLab.com, GitLab Dedicated and GitLab Dedicated for Government
#### This is a Controlled Document
In line with GitLab’s regulatory obligations, changes to [ controlled documents](https://handbook.gitlab.com/handbook/security/controlled-document-procedure/) must be approved or merged by a code owner. All contributions are welcome and encouraged. 
## GitLab Service Level Agreement - Availability Definition[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/service-level-agreement/#gitlab-service-level-agreement---availability-definition)
The following service level agreement applies to SaaS Software purchased or renewed as Ultimate tier on or after 2026-01-01.
### Service Availability Commitment[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/service-level-agreement/#service-availability-commitment)
GitLab commits to make the [Covered Experiences](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/service-level-agreement/#covered-experiences) available with a Monthly Uptime Percentage of at least **99.9%** during each calendar month.
### Covered Experiences[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/service-level-agreement/#covered-experiences)
The following GitLab features and services are covered under this SLA (“Covered Experiences”):
  1. Issues and Merge Requests
  2. Git Operations (push, pull, clone via HTTPS and SSH)
  3. Container Registry operations
  4. Package Registry operations
  5. API Requests (limited to the above Covered Experiences only)


### Downtime Minute Definition[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/service-level-agreement/#downtime-minute-definition)
A **“Downtime Minute”** occurs when:
The Service experiences degraded availability, meaning **5% or more** of [Valid Customer Requests](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/service-level-agreement/#valid-request-definition) to [Covered Experiences](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/service-level-agreement/#covered-experiences) in a given minute result in server errors (defined as HTTP `5xx` status codes or connection timeouts exceeding 30 seconds) as determined by GitLab’s internal and external monitoring systems.
Downtime Minutes do not include any [Excluded Minutes](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/service-level-agreement/#excluded-minutes) as defined in this document.
### Valid Request Definition[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/service-level-agreement/#valid-request-definition)
**“Valid Request”** means a request that meets all of the following criteria:
  1. **Properly authenticated and authorized** - The request includes valid authentication credentials and the user has appropriate permissions for the requested operation
  2. **Correctly formed** - The request:
    1. Uses documented API endpoints, parameters, and methods
    2. Follows GitLab’s published API specifications and documentation
    3. Contains syntactically correct Git commands (for Git operations)
    4. Includes required headers and properly formatted request bodies
  3. **Within usage limits** - The request:
    1. Does not exceed documented rate limits
    2. Does not exceed size limits (e.g., file size, repository size, payload size)
    3. Originates from non-blocked IP addresses or users
    4. Complies with fair use policies
  4. **Non-malicious** - The request:
    1. Does not attempt to exploit security vulnerabilities
    2. Does not contain malicious code or payloads
    3. Is not part of a DDoS or other attack pattern
    4. Does not attempt to circumvent access controls
  5. **Supported operations** - The request:
    1. Targets features included in the customer’s subscription tier
    2. Uses generally available features (not experimental/beta)


The following are excluded from Valid Requests:
  1. Requests that receive HTTP `4xx` errors due to client-side issues
  2. Requests to deprecated API endpoints after the deprecation date
  3. Requests from automated testing or monitoring tools not operated by GitLab
  4. Preflight/OPTIONS requests
  5. Health check or status endpoint requests


### Excluded Minutes[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/service-level-agreement/#excluded-minutes)
The following minutes are excluded from being counted as Downtime Minutes:
  1. Scheduled Maintenance windows
  2. Emergency maintenance necessary to address critical security or data integrity issues
  3. Force Majeure events or general Internet connectivity issues
  4. Issues caused by Customer’s use of the Service in violation of the Terms of Service
  5. Issues caused by equipment, software, or services not provided or controlled by GitLab
  6. Features or services explicitly labeled as Alpha, Beta, or Preview


### Calculating Monthly Uptime Percentage[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/service-level-agreement/#calculating-monthly-uptime-percentage)
**“Monthly Uptime Percentage”** is calculated as:
Monthly Uptime Percentage=Total Minutes in MonthTotal Minutes in Month−Downtime Minutes​×100
Where:
  * **“Total Minutes in Month”** = Total number of minutes in the calendar month
  * **“Downtime Minutes”** = Total number of minutes in a calendar month when Covered Experiences met the Downtime Minute definition, excluding any Excluded Minutes


### Service Credits[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/service-level-agreement/#service-credits)
If the Monthly Uptime Percentage falls below 99.9%, GitLab Ultimate tier Customers may request (defined below) Service Credits according to:
Monthly Uptime Percentage | Service Credit  
---|---  
99.5% - <99.9% | 5% of monthly fees  
< 99.5% | 10% of monthly fees  
### Credit Request Process[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/service-level-agreement/#credit-request-process)
To receive a Service Credit, an eligible customer must:
  * Submit a Support request at [support.gitlab.com](https://support.gitlab.com) within thirty (30) days after the end of the affected month;
  * Include all relevant information about when the SaaS Service was unavailable; and
  * Provide reasonable detail about the attempted access to Covered Experiences


Once received, GitLab will then verify the claim against its own internal monitoring data and, if validated, issue Service Credits against Customer’s next issued invoice. In no event shall an issued Service Credit result in a refund of Fees to Customer.
### Credit eligibility[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/service-level-agreement/#credit-eligibility)
Raise a request through [support.GitLab.com](https://support.gitlab.com) to check if you are eligible for credits caused by downtime.
Last modified February 9, 2026: [Remove trailing spaces (`d8a6afc1`)](https://gitlab.com/gitlab-com/content-sites/handbook/commit/d8a6afc1)
[ ](https://gitlab.com/gitlab-com/content-sites/handbook/blob/main/content/handbook/engineering/infrastructure-platforms/service-level-agreement/_index.md) - [ ](https://gitlab.com/-/ide/project/gitlab-com/content-sites/handbook/edit/main/-/content/handbook/engineering/infrastructure-platforms/service-level-agreement/_index.md) - please [contribute](https://handbook.gitlab.com/handbook/about/contributing/). [ ![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-sa/4.0/)