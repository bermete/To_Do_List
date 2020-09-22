Project: To-Do List
from https://hyperskill.org

Objectives
Let's store the data about our tasks in the database. Here's what you need to do:

Create a database file. Its name should be todo.db.
Create a table in this database. The table name should be task.
The table task should have the following columns:
Integer column named id. It should be the primary key.
String column named task.
Date column named deadline. 

The menu should have the following items:
Today's tasks. Prints all tasks for today. Also, Today's tasks item should print today's date.
Week's tasks: prints all tasks for 7 days from today.
All tasks: prints all tasks sorted by deadline.
Missed tasks: prints all tasks whose deadline was missed, that is, tasks whose deadline date is earlier than today's date. Missed tasks should print the tasks ordered by the deadline date.
Add task. Asks for task description and saves it in the database. Now Add task item should ask for the deadline of the task. Users should input the deadline in this format: YYYY-MM-DD.
Delete task: deletes the chosen task. Print 'Nothing to delete' if the tasks list is empty. Delete task should print all the tasks sorted by the deadline date and ask to enter the number of the task to delete.
Exit.
