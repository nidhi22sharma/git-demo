

**Performance**

**1. Time Taken by the System to Respond**
- **Description:** Measures the time taken by the system to respond to a user request (e.g., average page load time).
- **Derivation/Formula:** Average Response Time = Total Response Time / Number of Requests
- **Example:** To calculate the average response time for login requests over a week, measure the time taken for each login attempt. If the total time for 100 login attempts is 200 seconds, the average response time is 200 seconds / 100 attempts = 2 seconds per login.

**2. Throughput**
- **Description:** Measures the number of transactions the system can handle per unit of time.
- **Derivation/Formula:** Throughput = Number of Transactions / Time Period
- **Example:** During a peak load test, count the number of transactions processed in a 10-second window. If 10,000 transactions are processed in 10 seconds, the throughput is 10,000 transactions / 10 seconds = 1,000 TPS.

**3. Resource Utilization**
- **Description:** Measures how efficiently the system utilizes resources like CPU, memory, and network bandwidth (e.g., CPU usage percentage).
- **Derivation/Formula:** Resource Utilization (%) = (Resource Used / Total Available Resource) * 100
- **Example:** To find CPU utilization during peak load, monitor the CPU usage over the peak period. If the CPU usage is recorded as 70% during peak load, it means 70% of the CPU capacity is utilized under those conditions.

---

**Usability**

**4. Task Completion Time**
- **Description:** Measures the time taken by users to complete a specific task within the software.
- **Derivation/Formula:** Average Task Completion Time = Total Time Taken / Number of Users
- **Example:** To calculate the average time to complete a purchase, measure the time taken by 50 users to complete a purchase. If the total time is 150 minutes, the average task completion time is 150 minutes / 50 users = 3 minutes per user.

**5. Error Rate**
- **Description:** Measures the percentage of times users encounter errors while using the software.
- **Derivation/Formula:** Error Rate (%) = (Number of Errors / Total Number of User Actions) * 100
- **Example:** If users encounter 25 errors out of 500 total actions in a week, the error rate is (25 / 500) * 100% = 5%.

**6. User Satisfaction Surveys**
- **Description:** Gathers feedback from users on their experience with the software's ease of use.
- **Derivation/Formula:** User Satisfaction (%) = (Number of Satisfied Users / Total Number of Surveyed Users) * 100
- **Example:** After a new feature release, survey 100 users on their satisfaction. If 80 users report satisfaction, the user satisfaction rate is 80%.

---

**Security**

**7. Number of Vulnerabilities Identified**
- **Description:** Tracks the number of security vulnerabilities discovered during testing.
- **Derivation/Formula:** Count of identified vulnerabilities through various security testing techniques.
- **Example:** Conduct a security audit and record the number of vulnerabilities found. If 10 vulnerabilities are identified, this metric tracks the total number of these security issues.

**8. Penetration Testing Results**
- **Description:** Measures the effectiveness of security controls against simulated attacks.
- **Derivation/Formula:** Count of vulnerabilities successfully exploited during penetration testing.
- **Example:** Perform penetration testing and count the number of successful exploits. If 3 vulnerabilities are exploited, this indicates the areas where security controls need improvement.

**9. Mean Time to Recover (MTTR)**
- **Description:** Measures the average time it takes to restore system functionality after a security breach.
- **Derivation/Formula:** MTTR = Total Downtime / Number of Incidents
- **Example:** If the total downtime from 4 security breaches is 16 hours, the MTTR is 16 hours / 4 breaches = 4 hours.

**10. Security Defects**
- **Description:** Tracks the number of defects related to security identified during testing.
- **Derivation/Formula:** Count of identified security defects through testing.
- **Example:** During a security review, if 15 security defects are identified, this metric tracks those defects.

---

**Reliability**

**11. Uptime Percentage**
- **Description:** Measures the percentage of time the system is operational and accessible to users.
- **Derivation/Formula:** Uptime (%) = (Total Uptime / Total Monitoring Period) * 100
- **Example:** If the system was operational for 720 hours out of 744 hours in a month, the uptime percentage is (720 / 744) * 100% = 96.77%.

**12. Mean Time Between Failures (MTBF)**
- **Description:** Measures the average time between system failures.
- **Derivation/Formula:** MTBF = Total Uptime / Number of Failures
- **Example:** If the system ran for 240 hours before experiencing a failure, the MTBF is 240 hours.

**13. Defect Escape Rate**
- **Description:** Measures the percentage of defects that remain undetected after testing and reach production.
- **Derivation/Formula:** Defect Escape Rate (%) = (Number of Defects Found in Production / Total Number of Defects Identified) * 100
- **Example:** If 5 defects are found in production out of 100 total defects identified, the defect escape rate is (5 / 100) * 100% = 5%.

---

**Scalability**

**14. Time to Scale**
- **Description:** Measures the time it takes for the system to adapt to increased user load or data volume.
- **Derivation/Formula:** Measured in minutes or hours.
- **Example:** If the system takes 10 minutes to scale up and handle additional users during a simulated test, the time to scale is 10 minutes.

**15. Performance Under Load**
- **Description:** Measures how well the system performs under increased load conditions.
- **Derivation/Formula:** Monitors response time, throughput, and resource utilization under simulated load scenarios.
- **Example:** During a load test, monitor response times. If the system maintains a response time of 3 seconds under load conditions of 5,000 users, it indicates good performance under load.

**16. Scalability Index**
- **Description:** Measures the system's ability to scale efficiently as demand increases.
- **Derivation/Formula:** Scalability Index = (Performance at Increased Load / Performance at Base Load) * 100
- **Example:** If the system performance at base load is 100 transactions per second (TPS) and at increased load it is 95 TPS, the scalability index is (95 / 100) * 100 = 95%.

---

**Compatibility**

**17. Number of Supported Platforms**
- **Description:** Tracks the number of operating systems and devices the software is compatible with.
- **Derivation/Formula:** Count of tested and confirmed compatible platforms.
- **Example:** If the software is tested and confirmed to work on Windows 10, macOS 12, iOS, and Android, the number of supported platforms is 4.

**18. Browser Compatibility**
- **Description:** Measures the software's compatibility with different web browsers.
- **Derivation/Formula:** Count of supported and tested web browsers.
- **Example:** If the software works on Chrome, Firefox, Safari, and Edge, the browser compatibility count is 4.

**19. Compatibility Testing Results**
- **Description:** Measures how well the software functions on different platforms and browsers.
- **Derivation/Formula:** Analyzes functionality and performance across various platforms and browsers.
- **Example:** Test the software on various browsers and devices. If a display issue is found on a specific browser version, this metric highlights the need to address compatibility issues.

---

**Additional Non-Functional Metrics**

**20. Probability of Failure on Demand (POFOD)**
- **Description:** Measures the likelihood that the system will fail when a service request is made.
- **Derivation/Formula:** POFOD = (Number of Failures / Number of Service Requests) * 100
- **Example:** If there are 2 failures out of 1,000 service requests, the POFOD is (2 / 1,000) * 100 = 0.2%.

**21. Percentage of Incidents Leading to Catastrophic Failure**
- **Description:** Measures the percentage of incidents that result in a complete system failure.
- **Derivation/Formula:** Percentage = (Number of Catastrophic Failures / Total Number of Incidents) * 100
- **Example:** If 1 out of 20 incidents leads to a catastrophic failure, the percentage is (1 / 20) * 100 = 5%.

**22. Data Corruption Probability**
- **Description:** Measures the likelihood of data corruption occurring during system operations.
- **Derivation/Formula:** Data Corruption Probability = (Number of Data Corruption Incidents / Total Number of Transactions) * 100
- **Example:** If there are 3 data corruption incidents out of 10,000 transactions, the probability is (3 / 10,000) * 100 = 0.03%.

**23. Recovery Time Objective (RTO)**
- **Description:** The maximum acceptable amount of time to restore a system after a failure.
- **Derivation/Formula:** Defined in the disaster recovery plan.


- **Example:** If the RTO for critical systems is 1 hour, test whether systems can be restored within this timeframe. Successful recovery within

1 hour indicates compliance with the RTO.

24. Disaster Recovery Readiness

	•	Description: Measures the preparedness of the system and processes to recover from a disaster.
	•	Derivation/Formula: Evaluated through regular disaster recovery drills and tests.
	•	Example: Conduct a disaster recovery drill and measure the time to restore services. If all critical systems are restored within the defined RTO, it confirms disaster recovery readiness.



