# Server Outage Incident Report (Created)
> By Daniel Mbedobe KUNJI (Mbedobe)

## Issue Summary:
On May 4, 2023, starting at 3:00 PM PST, users experienced a complete outage of our online retail website. This lasted for 2 hours and impacted 100% of our users, resulting in significant revenue loss.

## Timeline:
- 3:00 PM: The issue was detected when our monitoring system sent an alert to our on-call engineer about the website being down.
- 3:02 PM: The on-call engineer checked the website and confirmed that it was completely down.
- 3:03 PM: The engineer initiated investigations into the root cause of the issue.
- 3:10 PM: The engineer found that the website's database server was down and attempted to restart it.
- 3:15 PM: The website was still down, and the engineer escalated the issue to the database team.
- 3:20 PM: The database team started investigating the issue and found that the database server's disk was full.
- 3:30 PM: The database team cleared some disk space, restarted the server, and the website was back up.
- 5:00 PM: The root cause was identified as a log file rotation script that had filled up the disk with unnecessary logs.

## Root Cause and Resolution:
The root cause of the issue was a log file rotation script that was not configured correctly, causing it to generate unnecessary logs that filled up the disk space on the database server. This led to the database server being unable to write new data, resulting in the website going down. The issue was resolved by clearing up some disk space and restarting the database server.

## Corrective and Preventative Measures:
To prevent similar issues from happening in the future, we will be taking the following corrective and preventative measures:
- We will update the log file rotation script to ensure that it only generates necessary logs and does not fill up disk space unnecessarily.
- We will implement monitoring and alerting on the disk space usage on all our servers to detect and prevent disk space issues before they impact our services.
- We will review and improve our incident response process to ensure faster and more effective resolution of issues.
- We will conduct a thorough review of all our systems to identify any other potential sources of similar issues and take appropriate actions to mitigate them.

## Tasks to Address the Issue:
- Update the log file rotation script to ensure it only generates necessary logs.
- Implement monitoring and alerting on the disk space usage on all our servers.
- Review and improve our incident response process.
- Conduct a thorough review of all our systems to identify potential sources of similar issues and take appropriate actions.

----
## Author
* **Daniel Mbedobe** - [mbedobe](https://github.com/mbedobe)
