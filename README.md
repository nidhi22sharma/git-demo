
---

**Test Management & Execution**

**1. Test Case Preparation Status**
- **Description:** Tracks the progress of test case creation (e.g., designed, reviewed, approved)
- **Derivation/Formula:** Not calculated; tracked as number of test cases in each state
- **Example:** 50 designed, 30 reviewed, 20 approved

**2. % Test Cases Executed**
- **Description:** Percentage of total test cases that have been run
- **Derivation/Formula:** (Number of test cases executed / Total number of test cases) * 100%
- **Example:** If you have 100 test cases and have run 80, your % Test Cases Executed is 80%.

**3. Test Execution Progress**
- **Description:** Overall progress of test execution against the planned schedule
- **Derivation/Formula:** (Number of test cases executed / Total number of test cases) * 100%
- **Example:** If you planned to execute 100 test cases and have executed 60, your Test Execution Progress is 60%.

**4. Passed Test Cases %**
- **Description:** Percentage of executed test cases that passed
- **Derivation/Formula:** (Number of passed test cases / Total number of executed test cases) * 100%
- **Example:** If 80 tests were run and 65 passed, your Passed Test Cases % is 81.25%.

**5. Failed Test Cases %**
- **Description:** Percentage of executed test cases that failed
- **Derivation/Formula:** (Number of failed test cases / Total number of executed test cases) * 100%
- **Example:** If 15 tests failed out of 80 executed, your Failed Test Cases % is 18.75%.

**6. Blocked Test Cases %**
- **Description:** Percentage of test cases unable to be executed due to blockers
- **Derivation/Formula:** (Number of blocked test cases / Total number of test cases) * 100%
- **Example:** If 5 tests couldn't be run out of 100, your Blocked Test Cases % is 5%.

**7. Tests Run Per Time Period**
- **Description:** Number of test cases executed within a defined timeframe (e.g., day, week, sprint)
- **Derivation/Formula:** Total number of test cases executed within the specified time period
- **Example:** If you ran 25 tests in a week, your Tests Run Per Time Period (weekly) is 25.

**8. Test Execution Time (Average)**
- **Description:** Average time taken to execute a single test case
- **Derivation/Formula:** Total test execution time / Number of test cases executed
- **Example:** If 100 tests took a total of 5 hours (300 minutes), your average Test Execution Time is 3 minutes per test case.

**9. Test Automation Coverage**
- **Description:** Percentage of test cases that are automated
- **Derivation/Formula:** (Number of automated test cases / Total number of test cases) * 100%
- **Example:** If 60 out of 100 test cases are automated, your Test Automation Coverage is 60%.

**10. Test Rework Effort**
- **Description:** Effort (e.g., hours) spent fixing or updating existing test cases due to defects or changes
- **Derivation/Formula:** Track time spent on test case modifications
- **Example:** If you spent 5 hours updating test cases after defects were found, your Test Rework Effort is 5 hours.

**11. Test Execution Productivity**
- **Description:** Efficiency of test execution, usually measured as test cases executed per unit of time
- **Derivation/Formula:** Number of test cases executed / Total test execution time
- **Example:** If you execute 50 test cases in 10 hours, your Test Execution Productivity is 5 test cases per hour.

**12. Test Pass/Fail Ratio**
- **Description:** Ratio of passed tests to failed tests
- **Derivation/Formula:** Number of passed test cases / Number of failed test cases
- **Example:** If you have 65 passed tests and 15 failed tests, your Test Pass/Fail Ratio is 4.33.

**13. Defect Find Rate**
- **Description:** Number of defects found per unit of testing time
- **Derivation/Formula:** Number of defects found / Total testing time
- **Example:** If you find 20 defects in 40 hours of testing, your Defect Find Rate is 0.5 defects per hour.

**14. Test Case Efficiency**
- **Description:** Number of defects found per test case
- **Derivation/Formula:** Number of defects found / Number of test cases executed
- **Example:** If 50 test cases uncovered 10 defects, your Test Case Efficiency is 0.2 defects per test case.

**15. Test Suite Completeness**
- **Description:** Percentage of planned test cases that are written and ready for execution
- **Derivation/Formula:** (Number of completed test cases / Total number of planned test cases) * 100%
- **Example:** If you planned 120 test cases and have completed 90, your Test Suite Completeness is 75%.

---

**Defect Management**

**1. Fixed Defects %**
- **Description:** Percentage of identified defects that have been resolved
- **Derivation/Formula:** (Number of fixed defects / Total number of defects identified) * 100%
- **Example:** If 35 out of 40 defects were fixed, your Fixed Defects % is 87.5%.

**2. Accepted Defects**
- **Description:** Number of identified defects that are intentionally not fixed
- **Derivation/Formula:** Count of defects marked as "accepted"
- **Example:** If 2 out of 40 defects were accepted, your Accepted Defects is 2.

**3. Deferred Defects**
- **Description:** Number of identified defects that are postponed for a later release
- **Derivation/Formula:** Count of defects marked as "deferred"
- **Example:** If 3 out of 40 defects were deferred, your Deferred Defects is 3.

**4. Critical Defects %**
- **Description:** Percentage of identified defects that are classified as critical (high impact)
- **Derivation/Formula:** (Number of critical defects / Total number of defects identified) * 100%
- **Example:** If 5 out of 40 defects were critical, your Critical Defects % is 12.5%.

**5. Average Time to Repair Defects**
- **Description:** Average time taken to fix a defect after it's identified
- **Derivation/Formula:** Total time spent fixing defects / Number of defects fixed
- **Example:** If fixing 35 defects took 70 hours, your Average Time to Repair Defects is 2 hours per defect.

**6. Defect Density**
- **Description:** Number of defects per unit of software (e.g., per 1000 lines of code, per function point)
- **Derivation/Formula:** Number of defects found / Size of the software module (in chosen unit)
- **Example:** If you have 15 defects in a 5,000-line module, your Defect Density is 3 defects per 1,000 lines of code.

**7. Defect Removal Efficiency (DRE)**
- **Description:** Effectiveness of the testing process in identifying and removing defects before release
- **Derivation/Formula:** (Number of defects found during testing / Total number of defects) * 100%
- **Example:** If testing found 38 out of 40 total defects, your DRE is 95%.

**8. Mean Time to Detect (MTTD)**
- **Description:** Average time taken from a defect's introduction to its discovery
- **Derivation/Formula:** Total time from defect introduction to detection / Number of defects
- **Example:** If 20 defects were found with an average detection time of 2 days each, your MTTD is 2 days.

**9. Mean Time to Resolve (MTTR)**
- **Description:** Average time taken from a defect's discovery to its resolution
- **Derivation/Formula:** Total time from defect detection to resolution / Number of defects
- **Example:** If fixing 35 defects took an average of 1.5 days each, your MTTR is 1.5 days.

**10. Defect Leakage**
- **Description:** Number of defects that escape testing and are found in production
- **Derivation/Formula:** Count of defects found in production
- **Example:** If 2 out of 40 defects were found in production, your Defect Leakage is 2.

**11. Customer-Reported Defects**
- **Description:** Number of defects reported by end-users after the software release
- **Derivation/Formula:** Track the number of defects reported by customers
- **Example:** If customers reported 5 defects after release, your Customer-Reported Defects is 5.

**12. Defect Severity Distribution**
- **Description:** Categorization of defects by their impact on the system (e.g., critical, high, medium, low)
- **Derivation/Formula:** Track the number of defects in each severity category
- **Example:** Your distribution could be: Critical - 5, High - 10, Medium - 15, Low - 10.

---
Defect Management

1. Defect Severity Distribution

	•	Description: Categorization of defects by their impact on the system (e.g., critical, high, medium, low)
	•	Derivation/Formula: Track the number of defects in each severity category
	•	Example: If your defect distribution is: Critical - 5, High - 10, Medium - 15, Low - 10, it indicates varying impacts across different defects, helping prioritize fixes.

2. Defect Detection Rate (by Phase)

	•	Description: Effectiveness of each testing phase (e.g., unit, integration) in finding defects
	•	Derivation/Formula: (Number of defects found in a phase / Total number of defects in that phase) * 100%
	•	Example: If 12 defects were found during unit testing out of 15 total unit-level defects, your Unit Test Defect Detection Rate is 80%, indicating high effectiveness of unit tests in defect detection.

3. Defect Aging

	•	Description: The length of time a defect remains open and unresolved
	•	Derivation/Formula: Calculate the average or track individual defect ages
	•	Example: A defect open for 10 days has an age of 10 days. If 5 defects have ages of 5, 8, 12, 15, and 20 days, the average defect age is 12 days, showing the team’s responsiveness in fixing defects.

4. Defect Clustering

	•	Description: Identification of modules or areas of code with a high concentration of defects
	•	Derivation/Formula: Analyze defect distribution across modules or code areas
	•	Example: If Module A has 10 defects and Module B has 2, this suggests a clustering of defects in Module A, indicating the need for focused improvements in Module A.

Test Design & Review

1. Test Case Design Efficiency

	•	Description: Measures the time and effort spent designing effective test cases
	•	Derivation/Formula: Track time spent per test case or number of test cases designed per unit time
	•	Example: If you design 10 test cases in 5 hours, your Test Case Design Efficiency is 2 test cases per hour, reflecting the productivity of the test case design process.

2. Test Case Review Efficiency

	•	Description: Measures the time and effort spent reviewing and improving test cases
	•	Derivation/Formula: Track time spent per review or number of test cases reviewed per unit time
	•	Example: If you review 20 test cases in 2 hours, your Test Case Review Efficiency is 10 test cases per hour, indicating the thoroughness and speed of the review process.

3. Test Case Effectiveness

	•	Description: Measures how well test cases identify defects
	•	Derivation/Formula: (Number of defects found by a test case / Number of times the test case was executed) * 100%
	•	Example: If a test case finds a defect 3 times out of 10 executions, its Test Case Effectiveness is 30%, showing how effective the test case is in uncovering issues.

4. Requirement Traceability

	•	Description: Percentage of requirements linked to test cases, ensuring all requirements are tested
	•	Derivation/Formula: (Number of requirements linked to test cases / Total number of requirements) * 100%
	•	Example: If 45 out of 50 requirements have linked test cases, your Requirement Traceability is 90%, ensuring comprehensive coverage of all requirements.

5. Review Defect Density

	•	Description: Number of defects found during reviews per unit of test artifacts (e.g., per test case)
	•	Derivation/Formula: Number of defects found during reviews / Number of test artifacts reviewed
	•	Example: If you find 3 defects in 10 test cases during review, your Review Defect Density is 0.3 defects per test case, highlighting the quality of test case documentation.

6. Review Efficiency

	•	Description: Number of defects found during reviews per unit of review time
	•	Derivation/Formula: Number of defects found during reviews / Total review time
	•	Example: If you find 5 defects in a 2-hour review, your Review Efficiency is 2.5 defects per hour, indicating the effectiveness of the review process.

Project Management

1. Requirement Coverage

	•	Description: Percentage of requirements covered by test cases
	•	Derivation/Formula: (Number of requirements covered by test cases / Total number of requirements) * 100%
	•	Example: If 85 out of 100 requirements are covered, your Requirement Coverage is 85%, ensuring that the majority of requirements are validated through testing.

2. Test Coverage

	•	Description: Percentage of code lines executed by test cases
	•	Derivation/Formula: (Number of lines of code executed by tests / Total number of lines of code) * 100%
	•	Example: If your tests cover 8,000 lines out of a 10,000-line codebase, your Test Coverage is 80%, reflecting the extent to which the codebase is tested.

3. Schedule Variance (SV)

	•	Description: Deviation from the planned project schedule (positive is ahead, negative is behind)
	•	Derivation/Formula: Earned Value (EV) - Planned Value (PV)
	•	Example: If your EV is $50,000 and PV is $40,000, your SV is +$10,000, meaning you’re ahead of schedule.

4. Cost Variance (CV)

	•	Description: Deviation from the planned project budget (positive is under budget, negative is over budget)
	•	Derivation/Formula: Earned Value (EV) - Actual Cost (AC)
	•	Example: If your EV is $50,000 and AC is $55,000, your CV is -$5,000, meaning you’re over budget.

5. Effort Variance

	•	Description: Deviation from the planned effort (hours or person-days)
	•	Derivation/Formula: Estimated Effort - Actual Effort
	•	Example: If you estimated 100 hours but spent 120 hours, your Effort Variance is +20 hours, meaning you exceeded the planned effort.

6. Resource Utilization

	•	Description: Percentage of available resource time used for project tasks
	•	Derivation/Formula: (Total hours utilized by resources / Total available hours) * 100%
	•	Example: If a team of 5 has 40 hours/week each (200 total) and they work 180 hours, their Resource Utilization is 90%, indicating efficient use of resources.

7. Risk Exposure

	•	Description: Potential impact of identified risks on project goals (often quantified in monetary terms)
	•	Derivation/Formula: Assessed based on probability and impact of each risk
	•	Example: A risk with a 30% chance of occurring and a $10,000 impact would have a Risk Exposure of $3,000.

8. Test Environment Stability

	•	Description: Stability of the environment where tests are executed
	•	Derivation/Formula: Track downtime incidents or environment-related issues
	•	Example: If your test environment was down for 2 hours in a week, you had 2 hours of instability, indicating a need for more reliable test environments.

9. Team Velocity

	•	Description: Average amount of work completed per iteration in Agile projects
	•	Derivation/Formula: Total story points completed across iterations / Number of iterations
	•	Example: If your team completes 40, 50, and 60 story points in 3 sprints, your Team Velocity is 50 story points per sprint.

10. On-Time Delivery

	•	Description: Percentage of deliverables completed by their due date
	•	Derivation/Formula: (Number of deliverables completed on time / Total number of deliverables) * 100%
	•	Example: If 18 out of 20 deliverables were on time, your On-Time Delivery is 90%.

11. Project Scope Change Requests

	•	Description: Number of changes requested to the project’s scope after it has begun
	•	Derivation/Formula: Track the number of approved change requests
	•	Example: If there were 5 approved changes to the scope, your Project Scope Change Requests is 5.





********************

##
Performance

1. Time Taken by the System to Respond

	•	Description: Measures the time taken by the system to respond to a user request (e.g., average page load time).
	•	Derivation/Formula: Measured in milliseconds (ms) or seconds (s). Average response time can be calculated over a defined period or for specific user actions.
	•	Example: The average response time for a login request is 2 seconds, indicating system efficiency in handling user authentication.

2. Throughput

	•	Description: Measures the number of transactions the system can handle per unit of time.
	•	Derivation/Formula: Measured in transactions per second (TPS) or similar units. Throughput can be measured under various load conditions.
	•	Example: The system can handle 1000 transactions per second during peak usage, demonstrating its capacity to manage high volumes of transactions.

3. Resource Utilization

	•	Description: Measures how efficiently the system utilizes resources like CPU, memory, and network bandwidth (e.g., CPU usage percentage).
	•	Derivation/Formula: Measured as a percentage of available resources used.
	•	Example: CPU usage during peak load is typically around 70%, showing the system’s effectiveness in resource management.

Usability

1. Task Completion Time

	•	Description: Measures the time taken by users to complete a specific task within the software.
	•	Derivation/Formula: Measured in seconds or minutes. Average task completion time can be calculated for various user groups and tasks.
	•	Example: The average time it takes users to complete a purchase is 3 minutes, indicating the ease of use for completing transactions.

2. Error Rate

	•	Description: Measures the percentage of times users encounter errors while using the software.
	•	Derivation/Formula: Calculated as the number of errors divided by the total number of user actions, multiplied by 100%.
	•	Example: The error rate for searching products is 5%, reflecting the system’s reliability in handling search queries.

3. User Satisfaction Surveys

	•	Description: Gathers feedback from users on their experience with the software’s ease of use.
	•	Derivation/Formula: Conducted through surveys or interviews. Analyze responses to identify usability issues.
	•	Example: User satisfaction surveys reveal difficulty navigating the checkout process, indicating areas for improvement in user interface design.

Security

1. Number of Vulnerabilities Identified

	•	Description: Tracks the number of security vulnerabilities discovered during testing.
	•	Derivation/Formula: The total count of vulnerabilities identified through various security testing techniques.
	•	Example: 10 security vulnerabilities were identified during penetration testing, highlighting areas needing security enhancements.

2. Penetration Testing Results

	•	Description: Measures the effectiveness of security controls against simulated attacks.
	•	Derivation/Formula: Analyzes the outcome of penetration testing to identify vulnerabilities exploited by attackers.
	•	Example: Penetration testing revealed a vulnerability allowing unauthorized access, indicating the need for improved security measures.

3. Mean Time to Recover (MTTR)

	•	Description: The average time it takes to restore system functionality after a security breach.
	•	Derivation/Formula: Calculated as the total downtime after a security breach divided by the number of breaches.
	•	Example: The MTTR for security breaches is typically within 4 hours, demonstrating the team’s efficiency in restoring services.

Reliability

1. Uptime Percentage

	•	Description: Measures the percentage of time the system is operational and accessible to users.
	•	Derivation/Formula: Calculated as the total uptime divided by the total monitoring period, multiplied by 100%.
	•	Example: The system uptime for the past month was 99.5%, indicating high reliability.

2. Mean Time Between Failures (MTBF)

	•	Description: Measures the average time between system failures.
	•	Derivation/Formula: Calculated as the total uptime divided by the number of failures during that period.
	•	Example: The MTBF for the server is 24 hours, indicating the frequency of system interruptions.

3. Defect Escape Rate

	•	Description: Measures the percentage of defects that remain undetected after testing and reach production.
	•	Derivation/Formula: Calculated as the number of defects found in production divided by the total number of defects identified during testing, multiplied by 100%.
	•	Example: The defect escape rate for this release is 2%, indicating the effectiveness of pre-release testing.

Scalability

1. Time to Scale

	•	Description: Measures the time it takes for the system to adapt to increased user load or data volume.
	•	Derivation/Formula: Measured in minutes or hours.
	•	Example: The system can scale to handle additional users within 10 minutes, showing its ability to quickly adapt to changing demands.

2. Performance Under Load

	•	Description: Measures how well the system performs under increased load conditions.
	•	Derivation/Formula: Measured through performance metrics like response time and throughput under simulated load scenarios.
	•	Example: System performance remains stable under increased load with minimal response time increase, demonstrating robustness under stress.

Compatibility

1. Number of Supported Platforms

	•	Description: Tracks the number of operating systems and devices the software is compatible with.
	•	Derivation/Formula: Maintained list of compatible platforms through testing on various systems.
	•	Example: The software is compatible with Windows 10, macOS 12, and major mobile phone operating systems, ensuring broad usability.

2. Compatibility Testing Results

	•	Description: Measures how well the software functions on different platforms and browsers.
	•	Derivation/Formula: Analyzes functionality and performance across various platforms and browsers.
	•	Example: Compatibility testing revealed a minor display issue on a specific browser version, which will be addressed, ensuring a consistent user experience.






