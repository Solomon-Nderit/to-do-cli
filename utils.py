import json
from task import Task
import os
from datetime import datetime




def create_new_json():
    if not os.path.exists("tasks.json"):
        with open("tasks.json", "w") as f:
            json.dump([], f, indent=4)

create_new_json()
def read_tasks():

    with open('tasks.json') as f:
        data = json.load(f)
    return data

def generate_new_id(tasks):
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1

def save_tasks(title, description, due_date):
    try:
        tasks = read_tasks()  
        new_id = generate_new_id(tasks)
        
        new_task = Task(new_id, title, description, due_date)
        task_dict = new_task.to_dict()

        tasks.append(task_dict) 

        # Save full updated list back to file
        with open('tasks.json', 'w') as f:
            json.dump(tasks, f, indent=4)

        print(f"✅ Saved '{title}' as task number {new_id}")
    except Exception as e:
        print(f"❌ Error saving task: {e}")
    except json.JSONDecodeError:
        print("❌ Error decoding JSON. Please check the tasks.json file.")
    except FileNotFoundError:
        print("❌ tasks.json file not found. Please create it first.")
        create_new_json()
    return

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No tasks found")
        return

    if not data:
        print("No tasks to show.")
        return
    
    for task_dict in data:
        task = Task(**task_dict)
        print(task)


def complete(id):
    id=int(id)
    try:
        with open('tasks.json') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("❌ Could not load tasks.")
        return

    found = False
    for task in data:
        if task['id'] == id:
            task['completed'] = True
            title = task['title']
            found = True
            break
    if not found:
        print(f"❌ Task with ID {id} not found.")
    else:
        try:
            with open("tasks.json","w") as f:
                json.dump(data,f,indent=4)
            print(f"✅Marked  '{title}' as complete")
        except Exception as e:
            print(f"❌ Error saving completed task: {e}")

import json

def delete(task_id):
    task_id = int(task_id)
    try:
        with open("tasks.json", "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("❌ Could not load tasks.")
        return
    found = False
    for index, task in enumerate(data):
        if task["id"] == task_id:
            title = task["title"]
            del data[index]
            found = True
            break
    if not found:
        print(f"❌ Task with ID {task_id} not found.")
        return
    try:
        with open("tasks.json", "w") as f:
            json.dump(data, f, indent=4)
        print(f"✅ Deleted '{title}'")
    except Exception as e:
        print(f"❌ Error saving after delete: {e}")

def list_todays_tasks():
    today=datetime.day()
    try:
        with open("tasks.json", "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("❌ Could not load tasks.")
        return
    
    for index, task in enumerate(data):
        if task["due_date"] == today:
            task = Task(**task)
            print(task)
            break
        else:
            print("No tasks due today😁")


