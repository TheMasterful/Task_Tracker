# Task Tracker

Hello! This is the task tracker that I made, and it saves onto a json file, saving your progress

## Commands:

### add "INSERT TASK HERE"
The add command creates the task and adds it to the task tracker. You must include the task you want to add in quotes.
After using the add command, the task gets assigned an id. The id is a number.

### update INSERT ID HERE "INSERT TASK HERE"
This updates a task based on the id. It basically replaces a task with a new one. The INSERT TASK HERE is the one that replaces the old task with the new ones

### delete INSERT ID HERE
Deletes a task from the task tracker. Once you delete it, you cannot get it back.

### mark-in-progress INSERT ID HERE
Marks a task "in-progress." The task is specified by the id. (note: when a task is created, its status is "todo")

### mark-done INSERT ID HERE
Marks a task "done." The task is specified by the id.

### list
Lists out all of the tasks that you've created, regardless of the status.

### list todo
Basically lists out only the tasks that have the "todo" status.

### list in-progress
Remember when you can change the status of the task? Well, this is the reason! You can list all of your tasks that you've marked "in-progress."

### list done
Same thing as above, but for the tasks you've marked "done."

---

Note: the task also has createdAt and updatedAt datetimes. To find them, look inside the JSON file. Look through the list until you find the task (it should be obvious when you find the task contents of the task you're looking for), and you should see two datetimes. The first one is  the createAt datetime, while the second one is the updatedAt datetime.

Heres some example json data from my task tracker for practice:
[["0", " bake some chocolate chip cookies", " todo", " 2026-03-07 16:02:31.926211", " 2026-03-07 16:04:03.020095"]]


License: CC BY-SA



