from tabulate import tabulate 

def show_tasks(tasks):
    rows = [
        [task.id, task.name, task.priority, task.date, task.status]
        for task in tasks 
    ]

    print(tabulate(
        rows,
        headers = ["ID", "Task", "Priority", "Due Date", "Status"]
    ))