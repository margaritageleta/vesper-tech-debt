This zip file contains The Technical Debt Dataset [1] as an SQLite database with .db extension.

The contents of each table are the following:
* **PROJECTS:** This table contains the links to the GitHub repository and the Jira issue tracker of each project, as well as the SonarQube project key.
* **JIRA_ISSUES:** This table contains the Jira issues for the 33 projects analysed projects.
* **OLD_SONAR_MEASURES:** This table contains the different measures SonarQube analyses from the commits. (**NOTE:** Due to a missing character in the commitHash column this table cannot be joined using the commit)
* **SONAR_MEASURES:** This table contains the different measures SonarQube analyses from the commits. (**NOTE:** This table is a subset of the OLD_SONAR_MEASURES table with the commit issue fixed.)
* **SONAR_ISSUES:** This table lists all of the SonarQube issues as well as the anti-patterns and code smells detected.
* **SONAR_RULES:** This table lists the rules monitored by SonarQube.
* **GIT_COMMITS:** This table reports the commit information retrieved from the git log.
* **SZZ_FAULT_INDUCING_COMMITS:** This table reports the results from the execution of the SZZ algorithm, which labels the fault-inducing and -fixing commits.
* **GIT_COMMIT_CHANGES:** This table contains the changes performed in each commit.
* **REFACTORING_MINER:** This table reports the list of refactoring activities applied in the repositories.

(**NOTE:** This database has been slightly modified to make some table names more coherent with their contents.)

[1] Valentina Lenarduzzi, Nyyti Saarimäki, Davide Taibi. The Technical Debt Dataset. Proceedings for the 15th Conference on Predictive Models and Data Analytics in Software Engineering. Brazil. 2019. [Download the paper](http://www.taibi.it/sites/default/files/2019%20-%20Promise%20-%20The%20Technical%20Debt%20Dataset%20-%20ACM%20Version.pdf)
