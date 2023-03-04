# SQL_Integrations
An exercise in timing for SQL integrations in Python and R, in addition to visualizations in Seaborn

The process was as follows:

1) collect student grades from a remote SQL server using sqlalchemy in Python
2) create a user input for which form to use for grading (A-D)
3) find the domain with the lowest mean score, and create an autograding function for the standard and curved grades
4) send the results to a local SQL server, and export to a csv
5) create a connector using RMySQL in R Studio to select descriptive statistics from the uploaded table
6) collate the queries into a single request
7) back to Python, read the exported CSV, and create visualizations for the distributions of normal and curved grades 
8) all of this is run through a Shell script, timing the process for the R code and running each script in one Bash job

The data, scripts, and visualizations are all included. 
