# SQLite Database Browser & Polyglot

We are going to start with a GUI (Graphical User Interface) tool, for managing sqlite - just to see that the things are working correctly!

If you are using Ubuntu, you can install [SQLite Database Browser](https://apps.ubuntu.com/cat/applications/sqlitebrowser/), which is simple enough for our needs!

Now, go back to the [Polyglot repository](https://github.com/HackBulgaria/Programming101-2/tree/master/week1/0-Polyglot), and locate the ```polyglot.db``` file and open it in the SQLite Database Browser!

When the file is loaded, take a look at the tables.

## sqlite3 shell tool

Now, back to the console.

__First, check if you have the tool for running sqlite3 shell client, by typing:__

```
$ sqlite3
```

If you see:

```
SQLite version 3.7.9 2011-11-01 00:52:41
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite>
```

Everything is OK! If there is an error, you should install ```sqlite3```:

```
sudo apt-get install sqlite3 libsqlite3-dev
```

Now, navigate to the ```Polyglot``` directory and call the following command:

```
$ sqlite3 polyglot.db
```

And run the following SQL statement:

```
sqlite>SELECT * FROM languages;
```

You will get the following result:

```
1|Python|google|0|A folder named Python was created. Go there and fight with program.py!
2|Go|200 OK|0|A folder named Go was created. Go there and try to make Google Go run.
3|Java|object oriented programming|0|A folder named Java was created. Can you handle the class?
4|Haskell|Lambda|0|Something pure has landed. Go to Haskell folder and see it!
5|C#|NDI=|0|Do you see sharp? Go to the C# folder and check out.
6|Ruby|https://www.ruby-lang.org/bg/|0|Ruby, ruby, rubyyy, aaahaaaahaa! (music). Go to Ruby folder!
7|C++|header files|0|Here be dragons! It's C++ time. Go to the C++ folder.
8|JavaScript|Douglas Crockford|0|NodeJS time. Go to JavaScript folder and Node your way!
sqlite> SELECT * FROM languages;
1|Python|google|0|A folder named Python was created. Go there and fight with program.py!
2|Go|200 OK|0|A folder named Go was created. Go there and try to make Google Go run.
3|Java|object oriented programming|0|A folder named Java was created. Can you handle the class?
4|Haskell|Lambda|0|Something pure has landed. Go to Haskell folder and see it!
5|C#|NDI=|0|Do you see sharp? Go to the C# folder and check out.
6|Ruby|https://www.ruby-lang.org/bg/|0|Ruby, ruby, rubyyy, aaahaaaahaa! (music). Go to Ruby folder!
7|C++|header files|0|Here be dragons! It's C++ time. Go to the C++ folder.
8|JavaScript|Douglas Crockford|0|NodeJS time. Go to JavaScript folder and Node your way!
```

## Tables, tables everywhere! SELECT, UPDATE, INSERT, DELETE

Now, we know that our languages table looks like this:

| id      | language  | answer  | answered | guide |
| ------------- |:-------------:| --- | --- |-----:|
1|Python|google|0|A folder named Python was created. Go there and fight with program.py!
2|Go|200 OK|0|A folder named Go was created. Go there and try to make Google Go run.
3|Java|object oriented programming|0|A folder named Java was created. Can you handle the class?
4|Haskell|Lambda|0|Something pure has landed. Go to Haskell folder and see it!
5|C#|NDI=|0|Do you see sharp? Go to the C# folder and check out.
6|Ruby|https://www.ruby-lang.org/bg/|0|Ruby, ruby, rubyyy, aaahaaaahaa! (music). Go to Ruby folder!
7|C++|header files|0|Here be dragons! It's C++ time. Go to the C++ folder.
8|JavaScript|Douglas Crockford|0|NodeJS time. Go to JavaScript folder and Node your way!


A ```SELECT``` statement, returns a list of rows. We ```SELECT``` by giving the name of the columns we want.

Run the following SELECT statements in the sqilite3 shell:


```sql
SELECT id FROM languages;
```

```sql
SELECT id, language FROM languages;
```

```sql
SELECT id, language, answer, answered FROM languages;
```

```sql
SELECT id, language FROM languages WHERE answered = 0;
```

```sql
SELECT id, language FROM languages WHERE answered = 1;
```

__Now, lets update few languages to be answered. We will change the answered value for each language from 0 to 1:__


```sql
UPDATE languages SET answered = 1 WHERE language = "Python";
```

```sql
SELECT id, language FROM languages WHERE answered = 1;
```

Now, if we run the ```polyglot.py``` program and give the ```list``` command, we will see:

```
DONE [1] - Python
NOT_DONE [2] - Go
NOT_DONE [3] - Java
NOT_DONE [4] - Haskell
NOT_DONE [5] - C#
NOT_DONE [6] - Ruby
NOT_DONE [7] - C++
NOT_DONE [8] - JavaScript
```

As you can see, if we control the data, we control the program!

__Now, let's insert a new language in our table!__

Execute the following statements:


```sql
INSERT INTO languages(id, language, answer, answered, guide) VALUES(9, "PHP", "$$$", 0, "Can you handle this piece of PHP?");
```

```sql
SELECT language FROM languages;
```

Now, if we go to our Polyglot program, again, we will see that PHP was added too:

```
DONE [1] - Python
NOT_DONE [2] - Go
NOT_DONE [3] - Java
NOT_DONE [4] - Haskell
NOT_DONE [5] - C#
NOT_DONE [6] - Ruby
NOT_DONE [7] - C++
NOT_DONE [8] - JavaScript
NOT_DONE [9] - PHP
```

Now, to finish the cycles of SQL statements, we are going to ```DELETE``` the added PHP language

We can achieve that by running the following query:

```sql
DELETE FROM languages WHERE language = "PHP";
```

Now, if we run:

```sql
SELECT language FROM languages;
```

We won't see PHP!

### SUID = CRUD

We were talking about CRUD operations - Create, Read, Update, Delete of a given object.

If we take a look at the SQL query statements, we can relate:

* `SELECT` = Read
* `UPDATE` = Update
* `INSERT` = Create
* `DELETE` = Delete




# Database relationships

In the relational database world, relations are a key concept that helps us model our data.

**The idea is to define how two tables are connected in terms of their data.**

Lets have the following example:

* We want to have a databases, holding users in our blog system. We will have the following schemas:

```sql
CREATE TABLE Users(
  user_id INTEGER PRIMARY KEY,
  user_name TEXT,
  user_email TEXT
)

CREATE TABLE Posts(
  post_id INTEGER PRIMARY KEY,
  post_title TEXT,
  post_content TEXT,
  author INTEGER
)
```

The interesting part is the connection between a post and his author.

Should we keep the author's name? Or his email? Or should we use the fact that PK will always give us a unique row from `Users`.

Then, what happens if we keep in the `author` column, the `user_id` of the given user, that wrote the post?

We can have data like that:

| user_id | user_name | user_email                |
|---------|-----------|---------------------------|
| 1       | RadoRado  | radorado@hackbulgaria.com |
| 2       | Ivo       | ivaylo@hackbulgaria.com   |
| 3       | Tony      | tony@hackbulgaria.com     |

and

| post_id | post_title  | post_content            | author |
|---------|-------------|-------------------------|--------|
| 1       | Hello World | The first blog post     | 1      |
| 2       | New courses | Something interesting.. | 3      |


Then the `author` column holds the `user_id` of the given user. We have now built a relationship!

* **Such relationship is called 1:N or one-to-many!**
* The `author` column is called a **foreign key**, because it holds values that are values of a primary key column elsewhere!

## 1:N relationship

The one-to-many relationship can be described as follows:

* One user can have many articles
* One article has only 1 author (user)

This means that we can have repating values in the `author` column in `Posts`.

**1:N relationships are build using Foreign keys.**

## N:M relationship

This is called **many-to-many** relationship.

Lets have the following example:

* We want to have students
* We want to have courses
* One student can go to multiple courses
* One course can be attented by mutiple students

How do we model such relationship in our database?

For many-to-many relations, we always need something, that is called a **junction table!**

Our tables would look like that:

**Students:**

| student_id | student_name |
|------------|--------------|
| 1          | Ivo          |
| 2          | Maria        |
| 3          | Tony         |
| 4          | Rado         |
| 5          | Rosi         |
| 6          | Ani          |

and **Courses:** 

| course_id | course_name   |
|-----------|---------------|
| 1         | 101           |
| 2         | Java          |
| 3         | JS            |
| 4         | Ruby on Rails |
| 5         | NodeJS        |
| 6         | Algorithms    |

and the **junction table**:

| student_id | course_id |
|------------|-----------|
| 1          | 1         |
| 2          | 1         |
| 3          | 1         |
| 4          | 2         |
| 5          | 2         |
| 6          | 6         |


As you can see, each row in the junction table tells us which student is attending which course! This is our relation.

**In the junction table, both columns are foreign keys to the tables in the many-to-many relation!**


## Foreign Keys

We have two type of keys - Primary (PK) and Foreign (FK).

If a column is a PK for the table, it can hold only unique values. And one value from that column should be able to "identify" the entire row. If we search in the `WHERE` clause with a PK, we should always get 1 value.

FK are different. They are used to express relations between two tables.

In the previous examples, the `author` column was a FK column. `student_id` and `course_id` in the junction table are FKs too.

Here is the deal with the FK:

* This is a **constraint** over what values can be inserted in the column, defined as a foreign key.
* Usually, when you define your table, you say that a given column is going to be a FK to another table's PK column.

Lets see the SQL for that:

Now, when you have the general idea, you can read more about FK's here - https://www.sqlite.org/foreignkeys.html



Lets see the SQL for that:


```sql
CREATE TABLE Users(
  user_id INTEGER PRIMARY KEY,
  user_name TEXT,
  user_email TEXT
)

CREATE TABLE Posts(
  post_id INTEGER PRIMARY KEY,
  post_title TEXT,
  post_content TEXT,
  author INTEGER,
  FOREIGN KEY(author) REFERENCES Users(user_id)
)
```

There is an additional `FOREIGN KEY` statement. This is the required thing.

**Here is the SQL for the Student-Courses tables:**

```sql
CREATE TABLE Students(
  student_id INTEGER PRIMARY KEY,
  student_name TEXT
)

CREATE TABLE Courses(
  course_id INTEGER PRIMARY KEY,
  course_name TEXT
)

CREATA TABLE Student_To_Course(
  student_id INTEGER,
  course_id INTEGER,
  FOREIGN KEY(student_id) REFERENCES Students(student_id),
  FOREIGN KEY(course_id) REFERENCES Courses(course_id)
)
```

Now, when you have the general idea, you can read more about FK's here - https://www.sqlite.org/foreignkeys.html