Metric Name	Description	Derivation/Formula	Example
Test Management & Execution			
Test Case Preparation Status	Tracks the progress of test case creation (e.g., designed, reviewed, approved)	Not calculated; tracked as number of test cases in each state	50 designed, 30 reviewed, 20 approved
% Test Cases Executed	Percentage of total test cases that have been run	(Number of test cases executed / Total number of test cases) * 100%	If you have 100 test cases and have run 80, your % Test Cases Executed is 80%.
Test Execution Progress	Overall progress of test execution against the planned schedule	(Number of test cases executed / Total number of test cases) * 100%	If you planned to execute 100 test cases and have executed 60, your Test Execution Progress is 60%.
Passed Test Cases %	Percentage of executed test cases that passed	(Number of passed test cases / Total number of executed test cases) * 100%	If 80 tests were run and 65 passed, your Passed Test Cases % is 81.25%.
Failed Test Cases %	Percentage of executed test cases that failed	(Number of failed test cases / Total number of executed test cases) * 100%	In the same example, 15 tests failed, making your Failed Test Cases % 18.75%.
Blocked Test Cases %	Percentage of test cases unable to be executed due to blockers	(Number of blocked test cases / Total number of test cases) * 100%	If 5 tests couldn't be run out of 100, your Blocked Test Cases % is 5%.
Tests Run Per Time Period	Number of test cases executed within a defined timeframe (e.g., day, week, sprint)	Total number of test cases executed within the specified time period	If you ran 25 tests in a week, your Tests Run Per Time Period (weekly) is 25.
Test Execution Time (Average)	Average time taken to execute a single test case	Total test execution time / Number of test cases executed	If 100 tests took a total of 5 hours (300 minutes), your average Test Execution Time is 3 minutes per test case.
Test Automation Coverage	Percentage of test cases that are automated	(Number of automated test cases / Total number of test cases) * 100%	If 60 out of 100 test cases are automated, your Test Automation Coverage is 60%.
Test Rework Effort	Effort (e.g., hours) spent fixing or updating existing test cases due to defects or changes	Track time spent on test case modifications	If you spent 5 hours updating test cases after defects were found, your Test Rework Effort is 5 hours.
Test Execution Productivity	Efficiency of test execution, usually measured as test cases executed per unit of time	Number of test cases executed / Total test execution time	If you execute 50 test cases in 10 hours, your Test Execution Productivity is 5 test cases per hour.
Test Pass/Fail Ratio	Ratio of passed tests to failed tests	Number of passed test cases / Number of failed test cases	If you have 65 passed tests and 15 failed tests, your Test Pass/Fail Ratio is 4.33.
Defect Find Rate	Number of defects found per unit of testing time	Number of defects found / Total testing time	If you find 20 defects in 40 hours of testing, your Defect Find Rate is 0.5 defects per hour.
Test Case Efficiency	Number of defects found per test case	Number of defects found / Number of test cases executed	If 50 test cases uncovered 10 defects, your Test Case Efficiency is 0.2 defects per test case.
Test Suite Completeness	Percentage of planned test cases that are written and ready for execution	(Number of completed test cases / Total number of planned test cases) * 100%	If you planned 120 test cases and have completed 90, your Test Suite Completeness is 75%.
Defect Management			
Fixed Defects %	Percentage of identified defects that have been resolved	(Number of fixed defects / Total number of defects identified) * 100%	If 35 out of 40 defects were fixed, your Fixed Defects % is 87.5%.
Accepted Defects	Number of identified defects that are intentionally not fixed	Count of defects marked as "accepted"	If 2 out of 40 defects were accepted, your Accepted Defects is 2.
Deferred Defects	Number of identified defects that are postponed for a later release	Count of defects marked as "deferred"	If 3 out of 40 defects were deferred, your Deferred Defects is 3.
Critical Defects %	Percentage of identified defects that are classified as critical (high impact)	(Number of critical defects / Total number of defects identified) * 100%	If 5 out of 40 defects were critical, your Critical Defects % is 12.5%.
Average Time to Repair Defects	Average time taken to fix a defect after it's identified	Total time spent fixing defects / Number of defects fixed	If fixing 35 defects took 70 hours, your Average Time to Repair Defects is 2 hours per defect.
Defect Density	Number of defects per unit of software (e.g., per 1000 lines of code, per function point)	Number of defects found / Size of the software module (in chosen unit)	If you have 15 defects in a 5,000-line module, your Defect Density is 3 defects per 1,000 lines of code.
Defect Removal Efficiency (DRE)	Effectiveness of the testing process in identifying and removing defects before release	(Number of defects found during testing / Total number of defects) * 100%	If testing found 38 out of 40 total defects, your DRE is 95%.
Mean Time to Detect (MTTD)	Average time taken from a defect's introduction to its discovery	Total time from defect introduction to detection / Number of defects	If 20 defects were found with an average detection time of 2 days each, your MTTD is 2 days.
Mean Time to Resolve (MTTR)	Average time taken from a defect's discovery to its resolution	Total time from defect detection to resolution / Number of defects	If fixing 35 defects took an average of 1.5 days each, your MTTR is 1.5 days.
Defect Leakage	Number of defects that escape testing and are found in production	Count of defects found in production	If 2 out of 40 defects were found in production, your Defect Leakage is 2.
Customer-Reported Defects	Number of defects reported by end-users after the software release	Track the number of defects reported by customers	If customers reported 5 defects after release, your Customer-Reported Defects is 5.
Defect Severity Distribution	Categorization of defects by their impact on the system (e.g., critical, high, medium, low)	Track the number of defects in each severity category	Your distribution could be: Critical - 5
drive_spreadsheetExport to Sheets