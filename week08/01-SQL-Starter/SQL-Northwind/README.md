# Pure SQL

We are going to leave Python for a moment.

In the folder, there are 3 files:

 
* `northwind.db` - sqlite3 database, ready for querying
* `Northwind_relations.png` - this is the visual representation of the schema.
* `Northwind.sql` - the sql file to create the database. It is imported in `northwind.db`

We are going to make SQL queries to fetch data out from our database.

We recommend you to use [sqliteman](https://apps.ubuntu.com/cat/applications/precise/sqliteman/) - for syntax highlighting of the SQL.


## Queries

All queries are going to be some form of `SELECT`:

1. List all employees with their first name, last name and title.
2. List all employees from Seattle.
3. List all employees from London.
4. List all employees that work in the Sales department.
5. List all females employees that work in the Sales department.
6. List the 5 oldest employees.
7. List the first 5 hires of the company.
8. List the employee who reports to no one (the boss)
9. List all employes by their first and last name, and the first and last name of the employees that they report to.
10. Count all female employees.
11. Count all male employees.
12. Count how many employees are there from the different cities. For example, there are 4 employees from London.
13. List all OrderIDs and the employees (by first and last name) that have created them.
14. List all OrderIDs and the shipper name that the order is going to be shipped via.
15. List all contries and the total number of orders that are going to be shipped there.
16. Find the employee that has served the most orders.
17. Find the customer that has placed the most orders.
18. List all orders, with the employee serving them and the customer, that has placed them.
19. List for which customer, which shipper is going to deliver the order.

