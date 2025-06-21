import json
from task import Task
import os



def create_new_json():
    if not os.path.exists("tasks.json"):
        with open("tasks.json", "w") as f:
            json.dump([], f, indent=4)

create_new_json()
def load_tasks():

    with open('tasks.json') as f:
        data = json.load(f)
    return data

def generate_new_id(tasks):
    if not tasks:
        return 1
    return max(task.id for task in tasks) + 1

def save_tasks(title, description, due_date):
    tasks = load_tasks()  
    new_id = generate_new_id(tasks)
    
    new_task = Task(new_id, title, description, due_date)
    task_dict = new_task.to_dict()

    tasks.append(task_dict) 

    # Save full updated list back to file
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f, indent=4)

    print(f"✅ Saved '{title}' as task number {new_id}")



    