Here are the Functional Testing Metrics: Product Metrics (Optional) with clear descriptions, derivations, examples, types, and Jira details:

Functional Testing Metrics: Product Metrics (Optional)

Test Effectiveness %
	•	Description: Measures the percentage of defects identified before release compared to the total defects. This is a derived metric that assesses the quality of the testing process.
	•	Jira Details: Export pre-release and post-release defect data from Jira using issue types and timestamps for defect creation.
	•	Derivation:
￼
	•	Example: If 40 defects are found pre-release and 10 defects post-release, effectiveness is:
￼

Productivity
	•	Description: Tracks the output efficiency per individual or team during the testing process. This is a derived metric.
	•	Jira Details: Use Jira to track completed tasks or story points over a defined period.
	•	Derivation:
￼
	•	Example: If a team completes 100 tasks in 10 days, productivity is ￼ tasks per day.

Automation Pyramid
	•	Description: Measures the distribution of automated tests across different levels (Unit, Integration, UI). This is a base metric.
	•	Jira Details: If automation efforts are tracked in Jira, create tags or labels for tests at different pyramid levels (e.g., Unit, Integration, UI).
	•	Derivation:
￼
	•	Example: If there are 200 unit tests out of 400 total tests:
￼

Defect Aging
	•	Description: Tracks the average time defects remain unresolved, helping to assess the responsiveness of the testing team. This is a derived metric.
	•	Jira Details: Use defect creation and resolution timestamps in Jira to calculate defect aging.
	•	Derivation:
￼
	•	Example: If 5 defects remain unresolved for 5, 10, 15, 20, and 25 days:
￼

Defect Injection Rate
	•	Description: Calculates the number of new defects introduced during development or testing phases. This is a derived metric.
	•	Jira Details: Track the number of new defects linked to each build or change request in Jira.
	•	Derivation:
￼
	•	Example: If 50 defects are introduced from 200 changes:
￼

Defect Closure Rate
	•	Description: Measures the efficiency of closing defects within a given timeframe. This is a derived metric.
	•	Jira Details: Track defects marked as closed or resolved within a defined period using Jira’s defect workflow.
	•	Derivation:
￼
	•	Example: If 30 defects are closed out of 50 identified:
￼

Average Time to Repair Defects
	•	Description: Calculates the average time taken to fix defects once identified. This is a derived metric.
	•	Jira Details: Use timestamps for defect creation and resolution in Jira.
	•	Derivation:
￼
	•	Example: If fixing 35 defects took 70 hours:
￼

Mean Time to Resolve (MTTR)
	•	Description: Measures the average time taken to resolve defects from discovery to closure. This is a derived metric.
	•	Jira Details: Calculate MTTR using Jira’s timestamps for defect lifecycle events.
	•	Derivation:
￼
	•	Example: If 35 defects took an average of 1.5 days 

Functional Testing Metrics: Process Metrics (Optional)

Test Rework Effort
	•	Description: Tracks the total effort (time or hours) spent on reworking existing test cases due to defects or changes. This is a derived metric.
	•	Jira Details: Efforts related to rework can be logged in Jira using a custom field like “Rework Effort” or through work logs. If Jira does not track rework explicitly, examples can be provided manually based on historical records.
	•	Derivation:

\text{Total Time Spent on Rework Activities}

	•	Example: If testers spend 10 hours modifying test cases after defect fixes:

10 \text{ hours spent on rework}.



Non-Functional Testing Metrics: Project Metrics

Must Have Metrics (Mandatory)

Task Completion Time
	•	Description: Measures the time taken by users to complete a specific task within the system. This is a base metric.
	•	Jira Details: Task completion time can be tracked using the time log or issue history in Jira by noting the difference between task creation and closure timestamps.
	•	Derivation:

\text{Average Task Completion Time} = \frac{\text{Total Time Taken by All Users}}{\text{Number of Users}}

	•	Example: If 20 users take a total of 400 minutes to complete a task:

\frac{400}{20} = 20 \text{ minutes per user}.



Test Environment Availability
	•	Description: Tracks the percentage of time the test environment is operational and accessible. This is a derived metric.
	•	Jira Details: Environment availability can be documented manually as it is not directly supported in Jira. Use environment logs or records from the operations team to calculate this metric.
	•	Derivation:

\text{Environment Availability (\%)} = \left(\frac{\text{Total Available Time}}{\text{Total Scheduled Time}}\right) \times 100

	•	Example: If the environment was operational for 700 hours out of 744 scheduled hours:

\left(\frac{700}{744}\right) \times 100 = 94.08\%



Non-Functional Testing Metrics: Product Metrics

Must Have Metrics (Mandatory)

Average Response Time
	•	Description: Measures the average time taken by the system to respond to a user request. This is a base metric.
	•	Jira Details: Not directly supported in Jira. Use performance testing tools (e.g., JMeter or LoadRunner) integrated with Jira to log and analyze this data.
	•	Derivation:
￼
	•	Example: If the total response time for 1,000 requests is 5,000 ms:
￼

Throughput
	•	Description: Indicates the number of transactions processed by the system per unit of time. This is a base metric.
	•	Jira Details: Not supported in Jira. Use performance testing tools to gather throughput data for analysis.
	•	Derivation:
￼
	•	Example: If the system processes 3,000 transactions in 10 minutes:
￼

Error Rate
	•	Description: Measures the percentage of transactions or user actions that resulted in errors. This is a derived metric.
	•	Jira Details: Use defect logs or reports in Jira to track the number of errors over total transactions.
	•	Derivation:
￼
	•	Example: If 50 errors occur out of 10,000 transactions:
￼

Uptime Percentage
	•	Description: Tracks the percentage of time the system remains operational and accessible. This is a derived metric.
	•	Jira Details: Uptime data must be gathered from system logs or monitoring tools, as Jira does not natively support this.
	•	Derivation:
￼
	•	Example: If the system is up for 700 out of 744 hours in a month:
￼

Browser Compatibility
	•	Description: Tracks the number of browsers on which the system has been tested successfully. This is a base metric.
	•	Jira Details: Use Jira custom fields or comments to document browser testing results during test execution.
	•	Derivation:
￼
	•	Example: If the system is tested on 4 out of 5 targeted browsers:
￼

Security Defects
	•	Description: Tracks the number of defects identified during security testing. This is a base metric.
	•	Jira Details: Use tags or a custom field in Jira to classify defects related to security.
	•	Derivation:
￼
	•	Example: If 5 out of 50 defects are security-related:
￼

Resource Utilization
	•	Description: Tracks the percentage of system resources (e.g., CPU, memory, network) utilized during testing. This is a base metric.
	•	Jira Details: Resource utilization data must be extracted from monitoring tools (e.g., Grafana, New Relic) rather than Jira.
	•	Derivation:

\text{Resource Utilization (\%)} = \left(\frac{\text{Used Resources}}{\text{Total Available Resources}}\right) \times 100

	•	Example: If the system uses 70 GB of memory out of 100 GB available:



 Process Metrics

Environment Setup Time
	•	Description: Measures the total time required to set up the testing environment for test execution. This is a base metric.
	•	Jira Details: Environment setup times can be tracked as tasks in Jira. Use custom fields or time logs to record the start and end time.
	•	Derivation:

\text{Environment Setup Time} = \text{End Time} - \text{Start Time}

	•	Example: If setup starts at 9:00 AM and finishes at 1:00 PM, the environment setup time is:

1:00 \, \text{PM} - 9:00 \, \text{AM} = 4 \, \text{hours}.


Data Refresh Frequency
	•	Description: Tracks how often test data is refreshed during the testing process. This is a base metric.
	•	Jira Details: Record refreshes as comments or custom task fields in Jira. Frequency is calculated manually from these entries.
	•	Derivation:

\text{Data Refresh Frequency} = \frac{\text{Number of Data Refreshes}}{\text{Testing Period}}

	•	Example: If data is refreshed 5 times during a 10-day testing period, the refresh frequency is:

\frac{5}{10} = 0.5 \, \text{refreshes/day}.
 Project Metrics

Time to Scale
	•	Description: Measures how quickly the system scales to accommodate additional load or users during testing. This is a derived metric.
	•	Jira Details: Time to scale cannot be extracted from Jira; it must be manually recorded based on system performance logs.
	•	Derivation:

\text{Time to Scale} = \text{Time When Scaling is Complete} - \text{Time Scaling Begins}

	•	Example: If scaling starts at 2:00 PM and completes at 2:20 PM, the time to scale is:

2:20 \, \text{PM} - 2:00 \, \text{PM} = 20 \, \text{minutes}.


 Product Metrics

Test Data Coverage
	•	Description: Tracks the extent to which test data covers all potential test scenarios. This is a base metric.
	•	Jira Details: Use labels or custom fields in Jira to categorize test cases by data sets. Calculate coverage by linking test cases to data sets.
	•	Derivation:

\text{Test Data Coverage (\%)} = \left(\frac{\text{Data Sets Used}}{\text{Total Data Sets Available}}\right) \times 100

	•	Example: If 15 out of 20 data sets are used:

\left(\frac{15}{20}\right) \times 100 = 75\%.


Test Data Accuracy
	•	Description: Tracks the correctness and relevance of the test data used in testing. This is a base metric.
	•	Jira Details: Accuracy needs to be validated manually, as Jira does not natively support this metric. Results can be documented in test case comments or reports.
	•	Derivation:

\text{Test Data Accuracy (\%)} = \left(\frac{\text{Accurate Data Sets}}{\text{Total Data Sets}}\right) \times 100

	•	Example: If 18 out of 20 data sets are accurate:

\left(\frac{18}{20}\right) \times 100 = 90\%.


 You’re absolutely right to point that out. Upon reviewing the categorization, Probability of Failure on Demand (POFOD), Percentage of Incidents Leading to Catastrophic Failure, and Data Corruption Probability should indeed fall under Product Metrics as they measure system performance and behavior rather than project progress or testing processes. Here’s the corrected categorization:

Non-Functional Testing Metrics: Optional

Project Metrics

Mean Time Between Failures (MTBF)
	•	Description: Tracks the average time between two consecutive failures of a system during testing. This is a derived metric.
	•	Jira Details: Jira does not natively support this metric. Failure data should be collected from test logs or monitoring tools.
	•	Derivation:
￼
	•	Example: If the system ran for 100 hours with 5 failures:
￼

Mean Time to Recover (MTTR)
	•	Description: Measures the average time taken to restore a system after a failure. This is a derived metric.
	•	Jira Details: Failure recovery time should be logged in monitoring tools and manually analyzed.
	•	Derivation:
￼
	•	Example: If it took 40 hours to recover from 8 failures:
￼

Product Metrics

Probability of Failure on Demand (POFOD)
	•	Description: Calculates the likelihood of the system failing when a request is made. This is a derived metric.
	•	Jira Details: Request failure data must be tracked manually or through monitoring tools.
	•	Derivation:
￼
	•	Example: If there are 3 failures out of 1,000 requests:
￼

Percentage of Incidents Leading to Catastrophic Failure
	•	Description: Tracks the proportion of incidents that result in complete system failure. This is a derived metric.
	•	Jira Details: Incidents and their severity should be manually categorized in Jira or tracked externally.
	•	Derivation:
￼
	•	Example: If 2 out of 50 incidents led to catastrophic failures:
￼

Data Corruption Probability
	•	Description: Measures the likelihood of data corruption during testing. This is a derived metric.
	•	Jira Details: Manually track corrupted data instances and transactions in a central repository.
	•	Derivation:
￼
	•	Example: If 5 out of 10,000 transactions result in corruption:
￼

Process Metrics

Environment Setup Time (Optional Use Case)
	•	Description: Tracks additional setup scenarios for rare or complex environments.
	•	Jira Details: Same as recommended usage. Data should be logged manually in Jira or tracked through a custom task.
	•	Derivation: Same as the recommended version.
	•	Example: Rare use cases requiring specific configurations can extend setup times.

Data Refresh Frequency (Optional Use Case)
	•	Description: Tracks special refresh scenarios for volatile or non-standard data.
	•	Jira Details: Same as recommended usage. Data tracked manually or through additional task records.
	•	Derivation: Same as the recommended version.
	•	Example: High-refresh scenarios during specific test cycles.

This updated categorization aligns with the gold standard requirements. Let me know if you’d like further clarification or adjustments!

!