# create task, find task, update task, delete task, complete task, search task and calculate statistics
# task contains "ID", task, priority, due date, status
from storage import load_tasks, save_tasks 

def add_task(args):
    tasks = load_tasks()

    task = {
        "id": max([task["id"] for task in tasks], default=0) + 1,
        "title": args.title,
        "priority": args.priority,
        "due_date": args.due_date,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)

    print("Task added")

def delete_task(args):
    tasks = load_tasks()

    for task in tasks:
        if task["title"] == args.title:
            tasks.remove(task)
            save_tasks(tasks)
            print("Task deleted")
            return 

    print("Task not found")

def list_tasks(args):
    tasks = load_tasks()
    # display tasks

def complete_task(args):
    # find task
    # mark complete
    pass

def edit_task(args):
    print(f"Editting task...")

def search_task(args):
    print(f"Searching tasks...")

def display_tasks(args):
    print(f"Displaying tasks...")
