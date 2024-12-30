Description:

This metric measures the average time between two consecutive failures in the system. It indicates system reliability and is crucial for assessing the stability of applications under real-world conditions. This is a derived metric, calculated based on system uptime and failure occurrence over a defined period.

Jira Details:

Jira does not natively support MTBF calculations. However, failure logs can be tracked using Jira issue types such as “Incident” or “Defect”. A custom field, “Failure Timestamp,” can be added to record failure times. These records can be exported and analyzed externally to calculate MTBF.

Derivation:


\text{MTBF} = \frac{\text{Total Uptime}}{\text{Number of Failures}}

	•	Total Uptime: The cumulative operational time of the system.
	•	Number of Failures: The total count of system failures during the monitoring period.

Example:

If a system operates for 10,000 hours and experiences 5 failures:

\text{MTBF} = \frac{10,000}{5} = 2,000 \text{ hours}

This means the system operates reliably for an average of 2,000 hours between failures.


Mean Time to Recover (MTTR)

Metric: Mean Time to Recover (MTTR)

Description:

MTTR measures the average time required to restore a system or service after a failure. It is a derived metric that reflects the efficiency of recovery processes and helps evaluate the organization’s ability to minimize downtime.

Jira Details:

MTTR is not natively supported in Jira. However, recovery timestamps can be logged using custom fields like “Recovery Start Time” and “Recovery End Time” in Incident or Defect issues. These logs can then be exported for calculation.

Derivation:

￼
	•	Total Recovery Time: The sum of all durations between failure and restoration.
	•	Number of Failures: The total number of recovery incidents.

Example:

If a system experiences 5 failures and the total recovery time is 10 hours:
￼
The system takes an average of 2 hours to recover from a failure.

Probability of Failure on Demand (POFOD)

Metric: Probability of Failure on Demand (POFOD)

Description:

This metric evaluates the likelihood of a system failing when a service request is made. It is a derived metric that indicates the reliability of the system under demand.

Jira Details:

POFOD is not directly supported in Jira. Failure logs can be tracked using Incident or Defect issue types, and total service request data can be sourced from external logs or monitoring tools. Manual analysis is required to calculate this metric.

Derivation:

￼

Example:

If a system processes 10,000 service requests and encounters 5 failures:
￼
This indicates a 0.05% probability of failure on demand.

Percentage of Incidents Leading to Catastrophic Failure

Metric: Percentage of Incidents Leading to Catastrophic Failure

Description:

This metric measures the percentage of total incidents that result in complete system failure, significantly impacting operations. It is a derived metric used to evaluate system stability and risk.

Jira Details:

Jira does not natively support this metric. However, incidents categorized as “Catastrophic” can be tagged using a custom field or label. Export these tagged incidents and total incidents for calculation.

Derivation:

￼

Example:

If there are 50 total incidents, of which 5 are categorized as catastrophic:
￼
This indicates 10% of incidents result in catastrophic failures.

Data Corruption Probability

Metric: Data Corruption Probability

Description:

This metric evaluates the likelihood of data corruption occurring during system operations. It is a derived metric used to assess data integrity risks.

Jira Details:

Jira does not natively calculate this metric. However, data corruption incidents can be tracked using Defect or Incident issue types with a custom label like “Data Corruption”. Export this data for analysis.

Derivation:

￼

Example:

If a system processes 100,000 transactions and encounters 3 data corruption incidents:
￼
This means the probability of data corruption is 0.003%.


