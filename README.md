## Logs Analysis Project
------------------------

Content

1. Project Description
2. Structure of Project Files
3. How to Run the Project


1. Project Description:
-----------------------

The purpose of this project is to develope a Python program that will be used
to analyse the news database. This program will display the following results:
   a. What are the most popular three articles of all time
   b. Who are the most popular article authors of all time
   c. On which days did more than 1% of requests lead to errors
All of these answers will be answered by using only one sql query for each
answer to question.

2. Structure of Project Files
-----------------------------

There are three files in this project, and they are: newsdata.sql,
loganalysis.py, and readme.md 

   a. newsdata.sql is used to store the information about database
      schema, in the form of SQL commands. It used create database and
      create table commands to create database and table for the project.
      In addition, this file is used to create the whole data for the project.
   b. loganalysis.py is used to store the code of the Python module. There are 
      several functions used to process the purpose of the project.
   c. readme.md: this file. Use to describe the project description and
      instruction of how to run the project.
      
    Note: file newsdata.sql is in the newsdata.zip file. Uncompress the zip
            file to get the newsdata.sql
      
3. How to Run the Project
-------------------------

Before running the code or create the tables, there will be a need to create 
database first. In this project, follow these steps in order to successfully 
run the code of the project:
   
   a. Suppose there is news database has been created, then create tables 
      from the statements in newsdata.sql
      There are two ways to do this:
         - Paste each statement into psql
         - Use the command `psql -d news -f newsdata.sql` this will run the 
           SQL statements in the file newdata.sql
           
      Note: If there is no database in the system use the following command
            to create the database:
            a. `psql`
            b. `CREATE DATABASE news;`
            
            
   b. Run the project by using command:
      `python loganalysis.py`
      
      If the program run correctly, it will show the result of the answers to
      the questions above.
