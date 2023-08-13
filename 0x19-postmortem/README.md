# My first postmortem

## __Outage Postmoterm: Database Replication Failure__


### Issue Summary:
  -  __Duration:__ July 29, 2023, 09:00 AM - Aug 04, 2023, 04:30 AM (UTC)
  - __Impact:__ Unavailability of critical services leading to a complete downtime of our application. 74% of users were unable to access the platform.
  - __Root Cause:__ Configuration mismatch and communication breakdown between primary and replica databases.


### Timeline:
  - __Issue Detected:__ July 29, 09:00 AM (UTC)
  - __Detection Method:__ Monitoring alert triggered due to a spike in latency on the database server.
  - __Actions Taken:__ Initial investigation focused on the application servers due to latency reports. Assumed potential application code bottlenecks.
  - __Misleading Investigation:__ Believed the issue was related to an ongoing server maintenance task. Invested time in assessing recent changes to application code.
  - __Escalation:__ Incident escalated to the database team when no code or server-related issues were found.
  - __Resolution:__ Aug 04, 04:30 AM (UTC). Identified configuration mismatch between primary and replica databases. Applied correct configurations and performed a manual synchronization.


### Root Cause and Resolution
  - __Root Cause:__ The issue was caused by a configuration mismatch between the primary and replica databases. The mismatch led to failed replication attempts and data divergence between the two databases.
  - __Resolution:__ To address the issue, we reconfigured the replica database to match the primary's configuration settings. After ensuring the settings were consistent, we manually synchronized the data from the primary database to the replica. This resolved the replication failure and brought the replica up-to-date.


## Corrective and Preventative Measures:

### Improvements/Fixes:
    - Strengthen monitoring: Enhance monitoring to detect configuration inconsistencies between critical components.
    - Documentation: Maintain up-to-date documentation for database configuration and replication processes.
    - Regular Testing: Implement regular testing of database failover and replication scenarios to identify issues beforehand.

### Tasks to Address the Issue:
    - Update Monitoring: Configure alerts for detecting database configuration inconsistencies and replication failures.
    - Automation: Develop scripts to automate the synchronization process between primary and replica databases.
    - Documentation: Revise and improve documentation for database configuration and replication procedures.
    - Training: Conduct training sessions for the operations team on identifying and addressing database replication issues.

## Conclusion
The outage exposed the vulnerability of our database replication setup to configuration discrepancies. Prompt identification and collaboration across teams were crucial in restoring service and minimizing user impact. Going forward, we are committed to improving our monitoring capabilities, automation processes, and documentation practices to prevent such incidents. By addressing these corrective measures, we aim to enhance our system's resilience and provide a more stable experience for our users.
