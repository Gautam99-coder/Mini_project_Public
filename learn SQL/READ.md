This document contains 25 fundamental questions and answers about Database Management Systems (DBMS). These questions cover core concepts that are essential for understanding how databases work, their architecture, and their operations. Use this as a quick reference or study guide for DBMS fundamentals.

Questions and Answers
1. What is a DBMS?
Answer: A Database Management System (DBMS) is software that interacts with users, applications, and the database itself to capture and analyze data. It provides an interface between the database and end users or application programs.

2. What are the advantages of using a DBMS?
Answer: Advantages include:

Data redundancy control

Data consistency

Data sharing

Enforcement of standards

Improved data security

Data integrity maintenance

Concurrent access control

Backup and recovery

3. What is the difference between a database and a DBMS?
Answer: A database is an organized collection of data, while a DBMS is the software system that allows users to define, create, maintain and control access to the database.

4. What is SQL?
Answer: SQL (Structured Query Language) is a standard programming language used for managing and manipulating relational databases.

5. What are the different types of database models?
Answer: Main types include:

Relational model

Hierarchical model

Network model

Object-oriented model

Entity-relationship model

Document model

Key-value model

6. What is normalization?
Answer: Normalization is the process of organizing data in a database to minimize redundancy and dependency by dividing large tables into smaller tables and defining relationships between them.

7. What are the different normal forms?
Answer: The main normal forms are:

First Normal Form (1NF)

Second Normal Form (2NF)

Third Normal Form (3NF)

Boyce-Codd Normal Form (BCNF)

Fourth Normal Form (4NF)

Fifth Normal Form (5NF)
8. What is a primary key?
Answer: A primary key is a column or set of columns that uniquely identifies each row in a table. It cannot contain NULL values and must contain unique values.

9. What is a foreign key?
Answer: A foreign key is a column or set of columns in one table that references the primary key in another table, establishing a relationship between the two tables.

10. What is an index in a database?
Answer: An index is a database object that improves the speed of data retrieval operations on a table at the cost of additional storage space and slower writes.

11. What is a transaction in DBMS?
Answer: A transaction is a sequence of operations performed as a single logical unit of work that must be completed entirely or not at all (atomicity).

12. What are ACID properties in DBMS?
Answer: ACID stands for:

Atomicity: Transactions are all-or-nothing

Consistency: Database remains in a consistent state

Isolation: Concurrent transactions don't interfere

Durability: Completed transactions persist

13. What is a view in SQL?
Answer: A view is a virtual table based on the result set of a SQL statement. It contains rows and columns like a real table but doesn't store data physically.

14. What is the difference between DELETE and TRUNCATE?
Answer:

DELETE removes rows one at a time and logs each deletion; can use WHERE clause

TRUNCATE removes all rows by deallocating data pages; faster but can't be rolled back

15. What is a stored procedure?
Answer: A stored procedure is a prepared SQL code that you can save and reuse, allowing for better performance and security by reducing network traffic.

16. What is a trigger in DBMS?
Answer: A trigger is a stored procedure that automatically executes when a specific event occurs in the database (e.g., INSERT, UPDATE, DELETE).

17. What is data integrity?
Answer: Data integrity refers to the accuracy and consistency of data stored in a database, maintained through constraints, rules, and procedures.

18. What are the different types of joins in SQL?
Answer: Main types are:

INNER JOIN

LEFT (OUTER) JOIN

RIGHT (OUTER) JOIN

FULL (OUTER) JOIN

CROSS JOIN

SELF JOIN

19. What is the difference between clustered and non-clustered indexes?
Answer:

Clustered index determines the physical order of data in a table (only one per table)

Non-clustered index is a separate structure that points to the data (multiple allowed)

20. What is a deadlock in DBMS?
Answer: A deadlock occurs when two or more transactions are waiting indefinitely for one another to release locks on resources.

21. What is database concurrency control?
Answer: Concurrency control mechanisms ensure that database transactions are performed concurrently without violating data integrity.

22. What is a data warehouse?
Answer: A data warehouse is a large collection of business data used to help an organization make decisions, separate from operational databases.

23. What is the difference between OLTP and OLAP?
Answer:

OLTP (Online Transaction Processing) handles day-to-day transactions

OLAP (Online Analytical Processing) handles complex queries for analysis and decision making

24. What is NoSQL?
Answer: NoSQL databases are non-relational databases designed for large-scale data storage and high-performance needs, using flexible data models.

25. What is database sharding?
Answer: Sharding is a method for distributing data across multiple machines by partitioning a database into smaller, faster, more manageable pieces called shards.
