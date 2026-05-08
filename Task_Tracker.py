import datetime
import shlex
from pathlib import Path
import json
class All_Tasks:
    def __init__(self):
        self.tasks = set()

    def _id_in_tasks(self, id):
        for task in self.tasks:
            if task.id == id:
                return task
        return False

    
    def add(self, task):
        tasks_length = len(self.tasks)
        self.tasks.add(Task(tasks_length, task, "todo"))
        print(f"Task is successfully added (ID: {len(self.tasks)-1})")
    
    def update(self, id, task):
        try:
            id = int(id)
        except:
            print("ID must be an int")
            return
        if id >= len(self.tasks) or id < 0:
            print("ID is not found")
            return
        found_task = self._id_in_tasks(id)

        found_task.task = task
        found_task.updatedAt = datetime.datetime.now()
        print(f"Task of ID {id} is successfully updated")
    
    def delete(self, id):
        try:
            id = int(id)
        except:
            print("ID must be an int")
        task_remove = self._id_in_tasks(id)
        self.tasks.remove(task_remove)
        counter = 0
        for item in self.tasks:
            item.id = counter
            counter += 1
        print(f"Task of ID {id} is successfully deleted")
    
    def mark_task(self, mark, id):
        try:
            id = int(id)
        except:
            print("ID must be an int")
        idv_task = self._id_in_tasks(id)
        if mark == "in-progress":
            idv_task.status = "in-progress"
            print("Successfully marked 'in progress'")
        elif mark == "done":
            idv_task.status = "done"
            print("Successfully marked 'done'")
        else:
            print("Not a valid marking")
    
    def list_tasks(self, list_type="all"):
        if list_type == "all":
            for task in self.tasks:
                print(task.task)
        else:
            for task in self.tasks:
                if task.status == list_type:
                    print(task.task)

    def __repr__(self):
        return f"All_Tasks()"
    
    def __str__(self):
        return str(list(self.tasks))
    





class Task:
    def __init__(self, id, task, status, createdAt=None, updatedAt=None):
        self.id = id
        self.task = task
        #there will be three statuses: todo, in progress, and done
        self.status = status
        if createdAt == None and updatedAt == None:
            self.createdAt = datetime.datetime.now()
            self.updatedAt = datetime.datetime.now()
        else:
            self.createdAt = createdAt
            self.updatedAt = updatedAt
    def __repr__(self):
        return f"Task({self.id}, {self.task}, {self.status})"
    def __str__(self):
        return f"{self.id}, {self.task}, {self.status}, {self.createdAt}, {self.updatedAt}"


if __name__ == "__main__":
    print("TASK TRACKER")
    print("Version 1.0.0")
    print("*******************")
    print("""Welcome to this task tracker! If you need help on how to use, refer to the README.md! """)
    all_tasks = All_Tasks()
    path = Path("Task_JSON.json")
    contents = path.read_text()
    
    if len(contents) != 0:
        json_contents = json.loads(contents)
        for task in json_contents:
            
            all_tasks.tasks.add(Task(task[0], task[1], task[2], task[3], task[4]))
            
    while True:
        try:
            command = input("task-cli ")
            
            command_analysis = shlex.split(command)
            
            if command_analysis[0] == "add":
                all_tasks.add(command_analysis[1])
            elif command_analysis[0] == "update":
                all_tasks.update(command_analysis[1], command_analysis[2])
            elif command_analysis[0] == "delete":
                all_tasks.delete(command_analysis[1])
            elif command_analysis[0] == "mark-in-progress":
                all_tasks.mark_task("in-progress", command_analysis[1])
            elif command_analysis[0] == "mark-done":
                all_tasks.mark_task("done", command_analysis[1])
            elif command_analysis[0] == "list":
                try:
                    all_tasks.list_tasks(command_analysis[1])
                except:
                    all_tasks.list_tasks()
            else:
                print("Uh oh! Not a valid command!")
        except:
            print("Uh oh! Something went wrong! Please check to make sure your command is correct. Refer to READ_ME.txt for reference.")
                
        json_tasks = []
        
        
        for task in all_tasks.tasks:
            
            json_tasks.append(str(task).split(","))
            
        contents = json.dumps(json_tasks)
        path.write_text(contents)
        

