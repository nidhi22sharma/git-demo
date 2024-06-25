

**Performance**

**1. Time Taken by the System to Respond**
- **Description:** Measures the time taken by the system to respond to a user request (e.g., average page load time).
- **Derivation/Formula:** Measured in milliseconds (ms) or seconds (s). Average response time can be calculated over a defined period or for specific user actions.
- **Example:** To calculate the average response time for login requests over a week, measure the time taken for each login attempt. If the total time for 100 login attempts is 200 seconds, the average response time is 200 seconds / 100 attempts = 2 seconds per login.

**2. Throughput**
- **Description:** Measures the number of transactions the system can handle per unit of time.
- **Derivation/Formula:** Measured in transactions per second (TPS) or similar units. Throughput can be measured under various load conditions.
- **Example:** During a peak load test, count the number of transactions processed in a 10-second window. If 10,000 transactions are processed in 10 seconds, the throughput is 10,000 transactions / 10 seconds = 1,000 TPS.

**3. Resource Utilization**
- **Description:** Measures how efficiently the system utilizes resources like CPU, memory, and network bandwidth (e.g., CPU usage percentage).
- **Derivation/Formula:** Measured as a percentage of available resources used.
- **Example:** To find CPU utilization during peak load, monitor the CPU usage over the peak period. If the CPU usage is recorded as 70% during peak load, it means 70% of the CPU capacity is utilized under those conditions.

---

**Usability**

**4. Task Completion Time**
- **Description:** Measures the time taken by users to complete a specific task within the software.
- **Derivation/Formula:** Measured in seconds or minutes. Average task completion time can be calculated for various user groups and tasks.
- **Example:** To calculate the average time to complete a purchase, measure the time taken by 50 users to complete a purchase. If the total time is 150 minutes, the average task completion time is 150 minutes / 50 users = 3 minutes per user.

**5. Error Rate**
- **Description:** Measures the percentage of times users encounter errors while using the software.
- **Derivation/Formula:** Calculated as the number of errors divided by the total number of user actions, multiplied by 100%.
- **Example:** If users encounter 25 errors out of 500 total actions in a week, the error rate is (25 / 500) * 100% = 5%.

**6. User Satisfaction Surveys**
- **Description:** Gathers feedback from users on their experience with the software's ease of use.
- **Derivation/Formula:** Conducted through surveys or interviews. Analyze responses to identify usability issues.
- **Example:** After a new feature release, survey 100 users on their satisfaction. If 80 users report satisfaction, the user satisfaction rate is 80%.

---

**Security**

**7. Number of Vulnerabilities Identified**
- **Description:** Tracks the number of security vulnerabilities discovered during testing.
- **Derivation/Formula:** The total count of vulnerabilities identified through various security testing techniques.
- **Example:** Conduct a security audit and record the number of vulnerabilities found. If 10 vulnerabilities are identified, this metric tracks the total number of these security issues.

**8. Penetration Testing Results**
- **Description:** Measures the effectiveness of security controls against simulated attacks.
- **Derivation/Formula:** Analyzes the outcome of penetration testing to identify vulnerabilities exploited by attackers.
- **Example:** Perform penetration testing and count the number of successful exploits. If 3 vulnerabilities are exploited, this indicates the areas where security controls need improvement.

**9. Mean Time to Recover (MTTR)**
- **Description:** Measures the average time it takes to restore system functionality after a security breach.
- **Derivation/Formula:** Calculated as the total downtime after a security breach divided by the number of breaches.
- **Example:** If the total downtime from 4 security breaches is 16 hours, the MTTR is 16 hours / 4 breaches = 4 hours.

---

**Reliability**

**10. Uptime Percentage**
- **Description:** Measures the percentage of time the system is operational and accessible to users.
- **Derivation/Formula:** Calculated as the total uptime divided by the total monitoring period, multiplied by 100%.
- **Example:** If the system was operational for 720 hours out of 744 hours in a month, the uptime percentage is (720 / 744) * 100% = 96.77%.

**11. Mean Time Between Failures (MTBF)**
- **Description:** Measures the average time between system failures.
- **Derivation/Formula:** Calculated as the total uptime divided by the number of failures during that period.
- **Example:** If the system ran for 240 hours before experiencing a failure, the MTBF is 240 hours.

**12. Defect Escape Rate**
- **Description:** Measures the percentage of defects that remain undetected after testing and reach production.
- **Derivation/Formula:** Calculated as the number of defects found in production divided by the total number of defects identified during testing, multiplied by 100%.
- **Example:** If 5 defects are found in production out of 100 total defects identified, the defect escape rate is (5 / 100) * 100% = 5%.

---

**Scalability**

**13. Time to Scale**
- **Description:** Measures the time it takes for the system to adapt to increased user load or data volume.
- **Derivation/Formula:** Measured in minutes or hours.
- **Example:** If the system takes 10 minutes to scale up and handle additional users during a simulated test, the time to scale is 10 minutes.

**14. Performance Under Load**
- **Description:** Measures how well the system performs under increased load conditions.
- **Derivation/Formula:** Measured through performance metrics like response time and throughput under simulated load scenarios.
- **Example:** During a load test, monitor response times. If the system maintains a response time of 3 seconds under load conditions of 5,000 users, it indicates good performance under load.

---

**Compatibility**

**15. Number of Supported Platforms**
- **Description:** Tracks the number of operating systems and devices the software is compatible with.
- **Derivation/Formula:** Maintained list of compatible platforms through testing on various systems.
- **Example:** If the software is tested and confirmed to work on Windows 10, macOS 12, iOS, and Android, the number of supported platforms is 4.

**16. Compatibility Testing Results**
- **Description:** Measures how well the software functions on different platforms and browsers.
- **Derivation/Formula:** Analyzes functionality and performance across various platforms and browsers.
- **Example:** Test the software on various browsers and devices. If a display issue is found on a specific browser version, this metric highlights the need to address compatibility issues.

---

**Additional Non-Functional Metrics**

**17. Load Handling Capability**
- **Description:** Measures the system's capability to handle a specific load without performance degradation.
- **Derivation/Formula:** Analyzes system performance metrics under defined load conditions.
- **Example:** During a load test, measure the response time and throughput. If the system handles 10,000 concurrent users with response times remaining below 2 seconds, it demonstrates strong load handling capability.

**18. Stress Tolerance**
- **Description:** Measures the system's ability to maintain functionality under extreme conditions.
- **Derivation/Formula:** Monitors system performance under high load conditions until the system fails.
- **Example:** During stress testing, the system remains stable up to 15,000 concurrent users. This indicates the system's breaking point and its stress tolerance level.

**19. Recovery Time Objective (RTO)**
- **Description:** The maximum acceptable amount of time to restore a system after a failure.
- **Derivation/Formula:** Defined as part of the disaster recovery plan and measured during recovery testing.
- **Example:** If the RTO for critical systems is 1 hour, test whether systems can be restored within this timeframe. Successful recovery within 1 hour indicates compliance with the RTO.

**20. Disaster Recovery Readiness**
- **Description:** Measures the preparedness of the system and processes to recover from a disaster.
- **Derivation/Formula:** Evaluated through regular disaster recovery drills and tests.
- **Example:** Conduct a disaster recovery drill and measure the time to restore services. If all critical systems are restored within the defined RTO, it confirms disaster recovery readiness.

---
