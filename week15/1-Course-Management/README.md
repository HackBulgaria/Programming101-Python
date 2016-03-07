# Course Management System

We are going to implement a simple course management system to hold courses & lectures.

Make a fresh Django app.

The specification is as follows:

## Courses

First of all, our system should know about courses.

We are interested in the following attributes for one course:

* Name - should be unique
* Description
* Start Date
* End Date

For our courses, we should have the following HTML views:

* `GET /` should display a nice table with all courses, sorted by their start date. The table should look like this:

| Course Name                 | Description | Start Date | End Date   | Approximate Duration |
|-----------------------------|-------------|------------|------------|----------------------|
| Programming 101 with Python | Python!     | 01.01.2016 | 01.03.2016 | 3 months             |
| Programming 101 with Ruby   | Ruby.       | 10.01.2016 | 01.03.2016 | 2 months             |

The **Approximate Duration** should be really an approximation. Figure it out ;)

**Also, each course name should be a link to a detailed course page.**

* `GET /course/<name>/` - this is the detailed course page. There should be all lectures & tasks for the given course. The `<name>` part should  be the name of the course.
* `GET /course/new/` - this should display a form for creating new course.
* `POST /course/new/` - this should be handled by Django for creating new courses.
* `GET /course/edit/<course-name>` - this should display a form to edit some of the course details.
* `POST /course/edit/<course-name>` - this should be handled by Django for editing existing courses.

## Lectures

Having only courses is pointless. So lets add some lectures to the mix!

Our lecture should have:

* Unique Identifier
* Name
* Week - like the weeks in HackBulgaria
* Course **Hint, hint, FK, hint, hint**
* URL - where the real lecture or slides are be located.

We should have a set of URLs for creating and editing lectures:

* `GET /lecture/new` - the form for creating a new lecture
* `POST /lecture/new` - handled by Django for saving the lecture
* `GET /lecture/edit/<lecture-id>` - the form for editing an existing lecture
* `POST /lecture/edit/<lecture-id>` - handled by Django for editing an existing lecture

We should have a detailed lecture display page:

* `GET /lecture/<lecture-id>` should display (in a table) the information for our lecture.

**In the detailed view for a course, there should be a list / table of all lectures for that course, and each lecture should have a link to its detail page**
