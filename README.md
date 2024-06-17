
### Non-Functional Testing Metrics

### Transaction Time per Second

**Description**: Measures the average time taken to complete a transaction per second.

**Formula**:
```
Transaction Time per Second = Total Transaction Time / Number of Transactions per Second
```

**Recommendation**: Recommended

**Duplication or Redundancy**: Unique, measures the efficiency of transaction processing.

### Response Time

**Description**: Measures the time taken to receive a response for a request.

**Formula**:
```
Response Time = Total Response Time / Number of Requests
```

**Recommendation**: Recommended

**Duplication or Redundancy**: Unique, critical for performance testing.

### Time to Complete Operation

**Description**: Measures the total time taken to complete a specific operation.

**Formula**:
```
Time to Complete Operation = End Time - Start Time
```

**Recommendation**: Recommended

**Duplication or Redundancy**: Unique, essential for evaluating operation efficiency.

### Time to Interact (Speed Index)

**Description**: Measures the time until the user can start interacting with the system.

**Formula**:
```
Time to Interact = Time when Page is Usable - Start Time
```

**Recommendation**: Recommended

**Duplication or Redundancy**: Unique, important for user experience evaluation.

### Main Memory Usage

**Description**: Measures the amount of main memory used during operation.

**Formula**:
```
Main Memory Usage = Amount of Main Memory Used
```

**Recommendation**: Recommended

**Duplication or Redundancy**: Unique, crucial for performance and resource management.

### Auxiliary Memory Usage

**Description**: Measures the amount of auxiliary memory (e.g., disk space) used during operation.

**Formula**:
```
Auxiliary Memory Usage = Amount of Auxiliary Memory Used
```

**Recommendation**: Recommended

**Duplication or Redundancy**: Unique, essential for evaluating resource utilization.

### Training Time

**Description**: Measures the time required to train users or systems.

**Formula**:
```
Training Time = Total Time Spent on Training
```

**Recommendation**: Optional

**Duplication or Redundancy**: Unique, relevant for systems requiring user training.

### Number of Choices (Ease of Usability)

**Description**: Measures the number of choices or options presented to the user, affecting ease of use.

**Formula**:
```
Number of Choices = Total Number of User Options
```

**Recommendation**: Optional

**Duplication or Redundancy**: Unique, important for usability testing.

### Mouse Clicks

**Description**: Measures the number of mouse clicks required to complete a task.

**Formula**:
```
Mouse Clicks = Total Number of Clicks for a Task
```

**Recommendation**: Optional

**Duplication or Redundancy**: Unique, relevant for usability and efficiency.

### Downtime Probability

**Description**: Measures the probability of system downtime.

**Formula**:
```
Downtime Probability = (Total Downtime / Total Operation Time) x 100
```

**Recommendation**: Recommended

**Duplication or Redundancy**: Unique, critical for reliability assessment.

### Availability

**Description**: Measures the percentage of time the system is operational and accessible.

**Formula**:
```
Availability = (Uptime / Total Time) x 100
```

**Recommendation**: Recommended

**Duplication or Redundancy**: Unique, essential for service level agreements.

### Mean Time to Failure (MTTF)

**Description**: Measures the average time between failures.

**Formula**:
```
MTTF = Total Operating Time / Number of Failures
```

**Recommendation**: Recommended

**Duplication or Redundancy**: Unique, important for reliability metrics.

### Mean Time Between Failures (MTBF)

**Description**: Measures the average time between failures and includes repair time.

**Formula**:
```
MTBF = MTTF + MTTR
```

**Recommendation**: Recommended

**Duplication or Redundancy**: Unique, crucial for reliability and maintenance planning.

### Probability of Failure on Demand (POFOD)

**Description**: Measures the probability that a system will fail when a demand is made.

**Formula**:
```
POFOD = (Number of Failures / Number of Demands) x 100
```

**Recommendation**: Optional

**Duplication or Redundancy**: Unique, relevant for high-reliability systems.

### Time to Recovery

**Description**: Measures the time taken to recover from a failure.

**Formula**:
```
Time to Recovery = Total Recovery Time / Number of Failures
```

**Recommendation**: Recommended

**Duplication or Redundancy**: Unique, important for disaster recovery planning.

### Percentage of Incidents Leading to Catastrophic Failure

**Description**: Measures the percentage of incidents that result in a catastrophic failure.

**Formula**:
```
Percentage of Catastrophic Failures = (Number of Catastrophic Failures / Total Number of Incidents) x 100
```

**Recommendation**: Optional

**Duplication or Redundancy**: Unique, crucial for risk management.

### Data Corruption Probability

**Description**: Measures the probability of data corruption occurring.

**Formula**:
```
Data Corruption Probability = (Number of Data Corruptions / Total Data Transactions) x 100
```

**Recommendation**: Optional

**Duplication or Redundancy**: Unique, important for data integrity assessment.

### Number of Target Systems

**Description**: Measures the number of systems the software is deployed on.

**Formula**:
```
Number of Target Systems = Total Number of Systems Deployed
```

**Recommendation**: Optional

**Duplication or Redundancy**: Unique, relevant for deployment and scalability.

### Throughput

**Description**: Measures the number of transactions processed per unit of time.

**Formula**:
```
Throughput = Total Transactions / Total Time
```

**Recommendation**: Recommended

**Duplication or Redundancy**: Unique, critical for performance testing.

### Load Time

**Description**: Measures the time taken to load a system or application.

**Formula**:
```
Load Time = Time Taken to Load System
```

**Recommendation**: Optional

**Duplication or Redundancy**: Unique, important for performance evaluation.

### Resource Utilization

**Description**: Measures the percentage of system resources used during operation.

**Formula**:
```
Resource Utilization = (Resources Used / Total Available Resources) x 100
```

**Recommendation**: Recommended

**Duplication or Redundancy**: Unique, crucial for performance and capacity planning.

### Browser Compatibility

**Description**: Measures the software's compatibility across different browsers.

**Formula**:
```
Browser Compatibility = Number of Supported Browsers / Total Number of Major Browsers x 100
```

**Recommendation**: Optional

**Duplication or Redundancy**: Unique, relevant for web applications.

### Scalability

**Description**: Measures the ability of the system to handle increased load.

**Formula**:
```
Scalability = Performance at High Load / Performance at Normal Load
```

**Recommendation**: Recommended

**Duplication or Redundancy**: Unique, essential for capacity planning.

### Maintainability

**Description**: Measures the ease with which a system can be maintained.

**Formula**:
```
Maintainability = Total Maintenance Time / Total Operating Time x 100
```

**Recommendation**: Optional

**Duplication or Redundancy**: Unique, important for long-term system management.

---

This comprehensive list includes detailed descriptions, formulas, and recommendations for each non-functional testing metric, ensuring that each metric is properly categorized and relevant.