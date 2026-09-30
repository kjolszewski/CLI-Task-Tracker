# load_tasks() and save_tasks() e.g. persistence
# task structure is ID, task, priority, due date, status
import json 

FILE = "tasks.json"

def load_tasks():
    try:
        with open(FILE, "r") as f:
            return json.load(f) 
    except FileNotFoundError:
        return [] 

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)